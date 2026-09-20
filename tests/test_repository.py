from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def test_required_files_exist():
    req=['README.md','README.es.md','STATUS.md','publication/relational_geometry_core.es.md',
         '03_navier_stokes/manuscript.md','04_results/RESULTS_REGISTER.md','04_results/NO_GO_REGISTER.md']
    for r in req: assert (ROOT/r).exists(), r


def test_no_public_history_folders():
    assert not (ROOT/'archive').exists()
    assert not (ROOT/'history').exists()


def test_no_draft_version_tags_in_public_manuscripts():
    for r in ['publication/relational_geometry_core.es.md','03_navier_stokes/manuscript.md']:
        txt=(ROOT/r).read_text(encoding='utf-8').lower()
        assert 'v0.' not in txt
        assert 'draft for technical review' not in txt
