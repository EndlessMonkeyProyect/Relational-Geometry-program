from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RepositoryTests(unittest.TestCase):
    def test_required_public_entry_points_exist(self):
        required = [
            'README.md', 'README.es.md', 'STATUS.md', 'REVIEW.md', 'CONTRIBUTING.md',
            '03_navier_stokes/manuscript.md', '04_results/RESULTS_REGISTER.md',
            'tools/public_release.py',
            '01_foundations/ontology_of_difference_and_closure.es.md',
            '02_formal_core/relational_action_and_phase.es.md',
            '02_formal_core/harmonic_inheritance_and_novelty.es.md',
            '02_formal_core/causal_propagation_and_closure_resources.es.md',
            '02_formal_core/novelty_incorporation_and_dynamical_modes.es.md',
            '02_formal_core/local_comparators_and_relational_laplacian.es.md',
            '02_formal_core/novelty_and_global_control.es.md',
        ]
        for relative in required:
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file(), relative)

    def test_no_public_history_folders(self):
        for name in ('archive', 'history', '07_HISTORY'):
            self.assertFalse((ROOT / name).exists(), name)

    def test_no_internal_register_in_public_results(self):
        self.assertFalse((ROOT / '04_results/NO_GO_REGISTER.md').exists())


if __name__ == '__main__':
    unittest.main()
