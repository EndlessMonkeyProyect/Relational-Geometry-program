import importlib.util
from pathlib import Path
import tempfile

SPEC = importlib.util.spec_from_file_location(
    'canonical_audit_tests', Path(__file__).resolve().parents[1] / 'tools/canonical_audit.py')
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


def test_duplicate_unicode_heading_anchors_and_fenced_examples():
    text = '# Solución\n## Solución\n```md\n# Ignored\n```\n'
    assert audit.heading_anchors(text) == {'solución', 'solución-1'}


def test_missing_anchor_and_unclosed_fence_are_reported():
    with tempfile.TemporaryDirectory() as folder:
        root = Path(folder)
        (root / 'README.md').write_text('# Start\n[Missing](#absent)\n```\n', encoding='utf-8')
        errors = audit.audit(root)['errors']
        assert any('missing heading anchor' in e for e in errors)
        assert any('unclosed code fence' in e for e in errors)


def test_unescaped_table_pipe_is_reported_and_escaped_pipe_is_valid():
    with tempfile.TemporaryDirectory() as folder:
        root = Path(folder)
        p = root / 'README.md'
        p.write_text('| A | B |\n|---|---|\n| $|x|$ | b |\n', encoding='utf-8')
        assert any('table columns' in e for e in audit.audit(root)['errors'])
        p.write_text('| A | B |\n|---|---|\n| $\\lvert x\\rvert$ | b |\n', encoding='utf-8')
        assert audit.audit(root)['errors'] == []
