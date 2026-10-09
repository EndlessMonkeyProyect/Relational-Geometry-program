"""Offline document-integrity audit; keyword hits require editorial review.

Checks the public selection, excluding internal archives and reviews. Does not fetch URLs,
validate mathematical proofs, or alter documents. --json includes all findings.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

_SPEC = importlib.util.spec_from_file_location(
    "release_for_audit", Path(__file__).with_name("public_release.py"))
release = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(release)

TERMS = re.compile(
    r"validated|first[- ]principles|derived gravity|derivation of G|mass gap solved|"
    r"P\s*=\s*NP|proof of|n\s*=\s*4|1/16|1:15|4\s*(?:ħ|\\hbar)|future|"
    r"maximum relational|unification", re.I)


def prose_and_fences(text):
    """Ignore fenced examples, retaining line numbers for diagnostics."""
    result = []
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            token, tail = marker.groups()
            if fence is None:
                fence = (token, number)
            elif token[0] == fence[0][0] and len(token) >= len(fence[0]) and not tail.strip():
                fence = None
            continue
        if fence is None:
            result.append((number, line))
    return result, fence


def heading_anchors(text):
    result, counts = set(), {}
    lines, _ = prose_and_fences(text)
    for _, line in lines:
        match = re.match(r"^ {0,3}#{1,6}\s+(.+?)(?:\s+#+)?$", line)
        if not match:
            continue
        title = re.sub(r"<[^>]+>", "", match.group(1)).lower()
        # GitHub-style anchors for the plain Markdown headings used here.
        slug = ''.join(c for c in title if c.isalnum() or c in '_- ')
        slug = slug.replace(' ', '-')
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug if count == 0 else f"{slug}-{count}")
    result.update(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', text))
    return result


def audit(root):
    root = Path(root).resolve()
    files = release.public_files(root)
    errors = release.check_markdown_links(root)
    claims, mentions, hashes, md_count = [], [], {}, 0
    for relative in files:
        p = root / relative
        content = p.read_bytes()
        hashes.setdefault(hashlib.sha256(content).hexdigest(), []).append(relative.as_posix())
        if p.suffix == '.py':
            try:
                ast.parse(content.decode('utf-8-sig'), filename=str(relative))
            except (SyntaxError, UnicodeError) as exc:
                errors.append(f"{relative}: Python syntax: {exc}")
        if p.suffix != '.md':
            continue
        md_count += 1
        text = content.decode('utf-8-sig')
        lines, fence = prose_and_fences(text)
        if fence:
            errors.append(f"{relative}:{fence[1]}: unclosed code fence")
        if sum(line.strip() == '$$' for _, line in lines) % 2:
            errors.append(f"{relative}: odd number of standalone math fences")
        if '\ufffd' in text:
            errors.append(f"{relative}: Unicode replacement character")
        if re.search(r'^(?:<{7}|={7}|>{7})(?:\s|$)', text, re.M):
            errors.append(f"{relative}: possible conflict marker")
        expected_columns = None
        for number, line in lines:
            if not line.lstrip().startswith('|'):
                expected_columns = None
                continue
            # Pipes inside inline math also delimit Markdown table cells unless escaped.
            columns = len(re.findall(r'(?<!\\)\|', line))
            if expected_columns is None:
                expected_columns = columns
            elif columns != expected_columns:
                errors.append(f"{relative}:{number}: inconsistent Markdown table columns")
        for destination in release._markdown_destinations(text):
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc or not parsed.fragment:
                continue
            target = ((root / unquote(parsed.path).lstrip('/')) if parsed.path.startswith('/')
                      else (p.parent / unquote(parsed.path))) if parsed.path else p
            target = target.resolve()
            if target.is_relative_to(root) and target.is_file() and target.suffix == '.md':
                if unquote(parsed.fragment) not in heading_anchors(target.read_text(encoding='utf-8-sig')):
                    errors.append(f"{relative}: missing heading anchor: {destination}")
        for number, line in lines:
            if TERMS.search(line):
                claims.append({'path': relative.as_posix(), 'line': number, 'text': line})
            # File-like inline code is a candidate reference, not automatically a link.
            for value in re.findall(r'(?<!`)`([^`\n]+)`(?!`)', line):
                if not re.fullmatch(r'[\w./ -]+\.(?:md|py|csv|json|cff|txt|zip|rar)', value):
                    continue
                if (p.parent / value).exists() or (root / value).exists():
                    continue
                mentions.append({'path': relative.as_posix(), 'line': number, 'reference': value})
    return {
        'scope': 'Current public allowlist; offline, no proof or external URL verification',
        'files': len(files), 'markdown_files': md_count,
        'errors': sorted(set(errors)), 'claim_occurrences': claims,
        'unresolved_literal_mentions': mentions,
        'duplicate_file_groups': [v for v in hashes.values() if len(v) > 1],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    report = audit(args.root)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Audited {report['files']} files / {report['markdown_files']} Markdown documents.")
        print(f"Integrity errors: {len(report['errors'])}; claim hits requiring review: "
              f"{len(report['claim_occurrences'])}; unresolved file-like mentions: "
              f"{len(report['unresolved_literal_mentions'])}.")
        for error in report['errors']:
            print(error)
        for mention in report['unresolved_literal_mentions']:
            print(f"Mention: {mention['path']}:{mention['line']}: {mention['reference']}")
    return bool(report['errors'])


if __name__ == '__main__':
    raise SystemExit(main())
