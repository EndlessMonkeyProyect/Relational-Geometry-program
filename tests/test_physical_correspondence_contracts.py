"""Positive arithmetic controls for explicitly conditional physical maps."""
import math
import unittest


class PhysicalCorrespondenceContractTests(unittest.TestCase):
    def test_frequency_partition_and_compton_length(self):
        c, hbar, mass = 299792458.0, 1.054571817e-34, 1.67262192595e-27
        total = mass * c * c / hbar
        visible = total / 4
        radius = c / visible
        self.assertAlmostEqual((visible / total) ** 2, 1 / 16)
        self.assertAlmostEqual(radius / (hbar / (mass * c)), 4)
        self.assertAlmostEqual(radius * 1e15, 0.841235641, places=8)

    def test_proton_comparison_uses_declared_measurement_uncertainty(self):
        predicted, measured, sigma = 0.841235641, 0.84075, 0.00064
        self.assertAlmostEqual((predicted - measured) / sigma, 0.7588140625)

    def test_exact_differential_charge_formula(self):
        for epsilon in (0.001, 0.01, -0.01):
            a, b, f0 = 0.5965, 0.5412, 1.7
            fa, fb = f0 * (1 + epsilon * a), f0 * (1 + epsilon * b)
            observed = 2 * abs(fa - fb) / (fa + fb)
            formula = abs(epsilon * (a - b)) / abs(1 + epsilon * (a + b) / 2)
            self.assertAlmostEqual(observed, formula, places=14)
            approximation = abs(epsilon * (a - b))
            self.assertLess(abs(observed / approximation - 1), 0.006)

    def test_microscope_bound_under_single_parameter_contract(self):
        bound = 1.5e-15 + 2 * math.hypot(2.3e-15, 1.5e-15)
        self.assertAlmostEqual(bound / 1e-15, 6.991812087, places=8)
        self.assertLess(bound / 0.0553, 1.3e-13)
        self.assertGreater(bound / 0.0553, 1.2e-13)

    def test_composition_mixture_is_mass_weighted(self):
        # Dominant-isotope approximation; all masses in atomic mass units.
        isotopes = {'Pt': (117, 194.9647917), 'Rh': (58, 102.9054980),
                    'Ti': (26, 47.9479409), 'Al': (14, 26.9815384),
                    'V': (28, 50.9439570)}
        def descriptor(weights):
            self.assertAlmostEqual(sum(weights.values()), 1)
            return sum(w * isotopes[s][0] / isotopes[s][1] for s, w in weights.items())
        delta = descriptor({'Pt': .9, 'Rh': .1}) - descriptor({'Ti': .9, 'Al': .06, 'V': .04})
        self.assertAlmostEqual(delta, .0553, places=4)


if __name__ == '__main__':
    unittest.main()
