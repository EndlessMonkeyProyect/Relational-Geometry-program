"""Release safety checks runnable with unittest or pytest (standard library only)."""

import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile


SPEC = importlib.util.spec_from_file_location(
    "public_release", Path(__file__).resolve().parents[1] / "tools" / "public_release.py"
)
release = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(release)


class PublicReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write("README.md", "# Public program\n[Results](04_results/RESULTS_REGISTER.md)\n")
        self.write("04_results/RESULTS_REGISTER.md", "# Results\nPositive result.\n")

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_zip_uses_allowlist_and_excludes_private_sentinels(self):
        private = [
            "internal/audit.md", "NP/private.md", "NP.rar", "dist/old.md",
            "unlisted/private.md", "04_results/NO_GO_REGISTER.md",
            "publication/internal/audit.md", "publication/source.zip",
            "tests/__pycache__/cached.pyc", "publication/07_HISTORY/audit.md",
        ]
        for path in private:
            self.write(path, "PRIVATE_SENTINEL_DO_NOT_EXPORT")
        release.write_manifest(self.root)
        archive_path = release.build_release(self.root)
        with zipfile.ZipFile(archive_path) as archive:
            self.assertEqual(set(archive.namelist()), {
                "README.md", "04_results/RESULTS_REGISTER.md", "MANIFEST.json",
            })
            for name in archive.namelist():
                self.assertNotIn(b"PRIVATE_SENTINEL_DO_NOT_EXPORT", archive.read(name))
            manifest = json.loads(archive.read("MANIFEST.json"))
            self.assertEqual(manifest["file_count"], 2)
            for entry in manifest["files"]:
                content = archive.read(entry["path"])
                self.assertEqual(entry["sha256"], hashlib.sha256(content).hexdigest())
                self.assertEqual(entry["bytes"], len(content))

    def test_changed_added_and_removed_public_files_are_detected(self):
        release.write_manifest(self.root)
        self.write("README.md", "# Changed\n")
        self.write("STATUS.md", "# Added\n")
        (self.root / "04_results/RESULTS_REGISTER.md").unlink()
        errors = "\n".join(release.check_manifest(self.root))
        self.assertIn("Hash or size mismatch: README.md", errors)
        self.assertIn("Missing from manifest: STATUS.md", errors)
        self.assertIn("Not a current public file: 04_results/RESULTS_REGISTER.md", errors)
        with self.assertRaisesRegex(ValueError, "Release validation failed"):
            release.build_release(self.root)

    def test_private_missing_and_outside_links_are_rejected(self):
        self.write("internal/audit.md", "private")
        self.write("README.md", "\n".join([
            "[Private](internal/audit.md)", "[Missing](missing.md)",
            "[Outside](../outside.md)", "[Web](https://example.org)",
            "[Anchor](#title)", "```markdown", "[Example](placeholder.md)", "```",
        ]))
        errors = release.check_markdown_links(self.root)
        self.assertEqual(len(errors), 3, errors)
        self.assertTrue(any("link leaves repository" in error for error in errors))

    def test_valid_relative_directory_and_reference_links(self):
        self.write("publication/with space.md", "[Home](../README.md)\n")
        self.write("README.md", "\n".join([
            "[Results](04_results/)", "[Page](<publication/with space.md>)",
            "[Encoded](publication/with%20space.md)", "[Reference][result]",
            "[result]: 04_results/RESULTS_REGISTER.md#title",
        ]))
        self.assertEqual(release.check_markdown_links(self.root), [])

    def test_build_is_reproducible_and_manifest_has_no_self_reference(self):
        manifest = release.write_manifest(self.root)
        self.assertNotIn(b"\r\n", (self.root / "MANIFEST.json").read_bytes())
        self.assertNotIn("MANIFEST.json", [entry["path"] for entry in manifest["files"]])
        first = release.build_release(self.root).read_bytes()
        second = release.build_release(self.root).read_bytes()
        self.assertEqual(first, second)
        self.assertEqual(release.check_manifest(self.root), [])


if __name__ == "__main__":
    unittest.main()
