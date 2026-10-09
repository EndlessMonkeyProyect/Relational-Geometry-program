from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RepositoryTests(unittest.TestCase):
    def test_required_public_entry_points_exist(self):
        required = [
            'README.md', 'README.es.md', 'STATUS.md', 'REVIEW.md', 'CONTRIBUTING.md',
            '03_navier_stokes/manuscript.md', '04_results/RESULTS_REGISTER.md',
            'tools/public_release.py', 'STATUS_CANONICAL.md',
            '02_formal_core/contextual_reclosure_and_resource_cost.es.md',
            '02_formal_core/finite_comparison_contract_and_modal_weights.es.md',
            '02_formal_core/relative_closure_and_uniform_control.es.md',
            'publication/UPDATE_3_0.md',
            '01_foundations/canonical_relational_language.es.md',
            '02_formal_core/resolution_and_modal_weights.es.md',
            '05_computation/contextual_sat_and_representation_cost.es.md',
            'publication/spin_composition_and_relational_information.es.md',
            'publication/proton_radius_hypothesis.es.md',
            'publication/composition_dependent_gravity_constraints.es.md',
            '07_emergence_laboratory/chemistry/validation_protocol.es.md',
            '01_foundations/ontology_of_difference_and_closure.es.md',
            '02_formal_core/relational_action_and_phase.es.md',
            '02_formal_core/harmonic_inheritance_and_novelty.es.md',
            '02_formal_core/causal_propagation_and_closure_resources.es.md',
            '02_formal_core/novelty_incorporation_and_dynamical_modes.es.md',
            '02_formal_core/local_comparators_and_relational_laplacian.es.md',
            '02_formal_core/novelty_and_global_control.es.md',
            '02_formal_core/contextual_identity_and_scale_promotion.es.md',
            '02_formal_core/redistributive_closure_and_information_channels.es.md',
            '02_formal_core/collective_dynamics_on_quotients.es.md',
            '07_emergence_laboratory/README.md',
            '07_emergence_laboratory/chemistry/README.es.md',
            '07_emergence_laboratory/growth/README.es.md',
        ]
        for relative in required:
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file(), relative)

    def test_canonical_audit_has_no_document_integrity_errors(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            'canonical_audit', ROOT / 'tools/canonical_audit.py')
        audit = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(audit)
        self.assertEqual(audit.audit(ROOT)['errors'], [])


if __name__ == '__main__':
    unittest.main()
