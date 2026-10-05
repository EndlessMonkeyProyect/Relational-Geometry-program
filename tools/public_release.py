"""Build a public release from an explicit allowlist, independently of Git staging.

Usage: python tools/public_release.py [--write-manifest] [--build]
The manifest counts and hashes public files, excluding itself. The ZIP includes
those files plus MANIFEST.json. Files outside the allowlist are never exported.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import zipfile


PUBLIC_DIRECTORIES = (
    "00_orientation", "01_foundations", "02_formal_core", "03_navier_stokes",
    "04_results", "05_computation", "06_yang_mills", "publication",
    "references", "tests", "tools", ".github",
)
PUBLIC_FILES = (
    "README.md", "README.es.md", "STATUS.md", "REVIEW.md", "CONTRIBUTING.md",
    "requirements.txt", "pytest.ini", "CITATION.cff", "NOTICE.md", ".gitignore", ".gitattributes",
)
EXCLUDED_NAMES = {
    "internal", "_internal", ".internal", "np", "np.rar", "dist", ".git",
    "archive", "history", "07_history", "no_go_register.md", "__pycache__",
    ".pytest_cache", ".mypy_cache", ".ruff_cache", ".tox", ".venv", "venv",
    "node_modules", ".ds_store", "runs", "refined",
}
EXCLUDED_SUFFIXES = {".zip", ".rar", ".7z", ".pyc", ".pyo", ".tmp", ".bak", ".npz"}
MANIFEST_NAME = "MANIFEST.json"


def _excluded(path: Path) -> bool:
    return (
        any(part.lower() in EXCLUDED_NAMES for part in path.parts)
        or path.suffix.lower() in EXCLUDED_SUFFIXES
    )


def public_files(root: Path) -> list[Path]:
    """Return sorted relative files; refuse symlinks in any public candidate."""
    root = root.resolve()
    result = []
    for name in (*PUBLIC_FILES, *PUBLIC_DIRECTORIES):
        candidate = root / name
        if candidate.is_symlink():
            raise ValueError(f"Public release does not accept symlinks: {name}")
        if not candidate.exists():
            continue
        candidates = candidate.rglob("*") if candidate.is_dir() else [candidate]
        for path in candidates:
            relative = path.relative_to(root)
            if _excluded(relative):
                continue
            if path.is_symlink():
                raise ValueError(f"Public release does not accept symlinks: {relative}")
            if path.is_file():
                # Also catch Windows junctions or other aliases leaving the root.
                if not path.resolve().is_relative_to(root):
                    raise ValueError(f"Public file resolves outside repository: {relative}")
                result.append(relative)
    return sorted(set(result), key=lambda item: item.as_posix())


def _entries(root: Path) -> list[dict]:
    entries = []
    for relative in public_files(root):
        content = (root / relative).read_bytes()
        entries.append({
            "path": relative.as_posix(),
            "sha256": hashlib.sha256(content).hexdigest(),
            "bytes": len(content),
        })
    return entries


def _citation_metadata(root: Path) -> dict:
    citation = root / "CITATION.cff"
    if not citation.is_file():
        return {}
    text = citation.read_text(encoding="utf-8-sig")
    metadata = {}
    for key, field in (("version", "release"), ("date-released", "date")):
        match = re.search(rf"^{key}:\s*([^\n]+)", text, re.MULTILINE)
        if match:
            metadata[field] = match.group(1).strip().strip("\"'")
    return metadata


def write_manifest(root: Path) -> dict:
    root = root.resolve()
    entries = _entries(root)
    manifest = {
        "manifest_version": 1,
        **_citation_metadata(root),
        "file_count": len(entries),
        "counting_rule": "Public files excluding MANIFEST.json (included separately in ZIP).",
        "files": entries,
    }
    (root / MANIFEST_NAME).write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8", newline="\n",
    )
    return manifest


def check_manifest(root: Path) -> list[str]:
    root = root.resolve()
    try:
        manifest = json.loads((root / MANIFEST_NAME).read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as exc:
        return [f"Cannot read {MANIFEST_NAME}: {exc}"]
    if not isinstance(manifest, dict) or not isinstance(manifest.get("files"), list):
        return ["Invalid manifest structure."]
    expected = _entries(root)
    errors = []
    if manifest.get("file_count") != len(expected):
        errors.append(f"Manifest file_count must be {len(expected)}, excluding itself.")
    actual = manifest["files"]
    if any(not isinstance(entry, dict) or not isinstance(entry.get("path"), str)
           for entry in actual):
        return errors + ["Invalid manifest file entry."]
    actual_by_path = {entry["path"]: entry for entry in actual}
    expected_by_path = {entry["path"]: entry for entry in expected}
    if len(actual_by_path) != len(actual):
        errors.append("Manifest contains duplicate paths.")
    for path in sorted(expected_by_path.keys() - actual_by_path.keys()):
        errors.append(f"Missing from manifest: {path}")
    for path in sorted(actual_by_path.keys() - expected_by_path.keys()):
        errors.append(f"Not a current public file: {path}")
    for path in sorted(actual_by_path.keys() & expected_by_path.keys()):
        if actual_by_path[path] != expected_by_path[path]:
            errors.append(f"Hash or size mismatch: {path}")
    for key, value in _citation_metadata(root).items():
        if manifest.get(key) != value:
            errors.append(f"Manifest {key} differs from CITATION.cff.")
    return errors


def _markdown_destinations(text: str):
    # Code examples can intentionally contain placeholder links and paths.
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    text = re.sub(r"(`+).*?\1", "", "\n".join(lines))
    # Inline and reference-style links; angle brackets permit spaces in paths.
    inline = r"!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)"
    references = r"^\s{0,3}\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)"
    for pattern in (inline, references):
        for match in re.finditer(pattern, text, re.MULTILINE):
            yield match.group(1).strip("<>")


def check_markdown_links(root: Path) -> list[str]:
    """Check local file/directory destinations against the actual public export.

    URL targets and heading anchors are not fetched or validated. This checks
    that local links will work in the ZIP, including absence of private links.
    """
    root = root.resolve()
    paths = public_files(root)
    available = {path.as_posix() for path in paths} | {MANIFEST_NAME}
    errors = []
    for relative in paths:
        if relative.suffix.lower() != ".md":
            continue
        source = root / relative
        for destination in _markdown_destinations(source.read_text(encoding="utf-8-sig")):
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            decoded = unquote(parsed.path)
            target = ((root / decoded.lstrip("/")) if decoded.startswith("/")
                      else (source.parent / decoded)).resolve()
            if not target.is_relative_to(root):
                errors.append(f"{relative.as_posix()}: link leaves repository: {destination}")
                continue
            target_name = target.relative_to(root).as_posix()
            directory_prefix = "" if target_name == "." else target_name.rstrip("/") + "/"
            directory_is_public = target.is_dir() and any(
                name.startswith(directory_prefix) for name in available
            )
            if target_name not in available and not directory_is_public:
                errors.append(f"{relative.as_posix()}: target absent from public release: {destination}")
    return sorted(set(errors))


def build_release(root: Path) -> Path:
    root = root.resolve()
    errors = check_manifest(root) + check_markdown_links(root)
    if errors:
        raise ValueError("Release validation failed:\n" + "\n".join(errors))
    destination = root / "dist" / "relational_geometry_program_public.zip"
    if destination.parent.is_symlink() or not destination.parent.resolve().is_relative_to(root):
        raise ValueError("Release output directory must remain inside the repository.")
    destination.parent.mkdir(exist_ok=True)
    if destination.is_symlink():
        raise ValueError("Release output cannot be a symlink.")
    files = public_files(root) + [Path(MANIFEST_NAME)]
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative in sorted(files, key=lambda item: item.as_posix()):
            info = zipfile.ZipInfo(relative.as_posix(), date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, (root / relative).read_bytes())
    return destination


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write-manifest", action="store_true", help="Regenerate public hashes.")
    parser.add_argument("--build", action="store_true", help="Validate and build the public ZIP in dist/.")
    args = parser.parse_args(argv)
    try:
        if args.write_manifest:
            manifest = write_manifest(args.root)
            print(f"Wrote {MANIFEST_NAME}: {manifest['file_count']} public files.")
        errors = check_manifest(args.root) + check_markdown_links(args.root)
        if errors:
            for error in errors:
                print(error, file=sys.stderr)
            return 1
        print("Public manifest and local Markdown links: OK.")
        if args.build:
            print(f"Built {build_release(args.root)}")
        return 0
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
