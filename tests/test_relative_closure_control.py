"""Small independent controls for relative closure and uniform estimates.

No source experiments or internal data are imported. These checks supplement
the mathematical proofs in relative_closure_and_uniform_control.es.md.
"""

from fractions import Fraction as F
from itertools import combinations, product
import math
import unittest


def variance(values, weights):
    total = sum(weights, F(0))
    mean = sum(w * v for w, v in zip(weights, values)) / total
    return sum(w * (v - mean) ** 2 for w, v in zip(weights, values))


def conditional_energy(states, values, weights, coordinate):
    groups = {}
    for state, value, weight in zip(states, values, weights):
        exterior = state[:coordinate] + state[coordinate + 1:]
        groups.setdefault(exterior, []).append((value, weight))
    return sum((variance([v for v, _ in group], [w for _, w in group])
                for group in groups.values()), F(0))


def block_energy(states, values, weights):
    return sum((conditional_energy(states, values, weights, coordinate)
                for coordinate in range(len(states[0]))), F(0))


def clauses_of_width_two(n):
    clauses = {frozenset()}
    clauses.update(frozenset((sign * variable,))
                   for variable in range(1, n + 1) for sign in (-1, 1))
    clauses.update(frozenset((s * a, t * b))
                   for a, b in combinations(range(1, n + 1), 2)
                   for s, t in product((-1, 1), repeat=2))
    return clauses


class RelativeClosureControlTests(unittest.TestCase):
    def test_product_spectrum_and_sum_vs_average_normalization(self):
        for n in range(1, 5):
            states = list(product((0, 1), repeat=n))
            weights = [F(1, len(states))] * len(states)
            for mask in range(1, 1 << n):
                values = [F((-1) ** sum(state[i] for i in range(n)
                                       if mask & (1 << i))) for state in states]
                var = variance(values, weights)
                energy = block_energy(states, values, weights)
                self.assertEqual(var, 1)
                self.assertEqual(energy, mask.bit_count() * var)
                self.assertLessEqual(var, energy)
                if mask.bit_count() == 1:
                    self.assertEqual(var / energy, 1)
                    self.assertEqual(var / (energy / n), n)

    def test_density_comparison_and_kernel_with_exact_rationals(self):
        states = list(product((0, 1), repeat=2))
        reference = [F(1, 4)] * 4
        weights = [F(i, 10) for i in (1, 2, 3, 4)]
        density = [w / base for w, base in zip(weights, reference)]
        lower, upper = min(density), max(density)
        for values in product((F(-1), F(0), F(1)), repeat=4):
            var = variance(values, weights)
            energy = block_energy(states, values, weights)
            self.assertLessEqual(var, (upper / lower) * energy)
            self.assertEqual(energy == 0, len(set(values)) == 1)
            self.assertLessEqual(var, upper * variance(values, reference))
            for coordinate in range(2):
                self.assertGreaterEqual(
                    conditional_energy(states, values, weights, coordinate),
                    lower * conditional_energy(states, values, reference, coordinate),
                )

    def test_contraction_bound_covers_both_maximum_channels(self):
        values = [F(i, 4) for i in range(9)]
        for theta in (F(0), F(1, 3), F(3, 4)):
            for first, second, residual in product(values, repeat=3):
                maximum = max(first, second)
                if first <= theta * maximum + residual:
                    # A=second is the tight controlled-channel majorant.
                    bound = max(second, residual / (1 - theta))
                    self.assertLessEqual(maximum, bound)
                    self.assertLessEqual(bound, second + residual / (1 - theta))
        # Loss of a uniform margin matters: pointwise contraction alone does
        # not give an integrable majorant near t=1.
        for n in (2, 4, 8, 16):
            theta = 1 - F(1, n)
            self.assertEqual(F(1) / (1 - theta), n)

    def test_relative_channel_derivative_on_a_smooth_rotating_curve(self):
        # q=exp(a0*t + a1*t^2/2), phase=v0*t + v1*t^2/2.
        # b=phase' times the unit tangent and q''/q=a1+a^2.
        for a0, a1, v0, v1 in (
                (F(2), F(1, 3), F(1), F(1, 2)),
                (F(3), F(-1, 4), F(2), F(-1, 3)),
                (F(1), F(0), F(3, 2), F(0))):
            for t in (F(0), F(1, 3), F(2, 3)):
                a, speed = a0 + a1 * t, v0 + v1 * t
                self.assertGreater(a, 0)
                self.assertGreater(speed, 0)
                acceleration_parallel = a1 + a*a - speed*speed
                acceleration_tangent = v1 + 2*a*speed
                self.assertEqual(a1, acceleration_parallel - a*a + speed*speed)
                zeta = speed / a
                gamma = acceleration_tangent / (a*a) - zeta * (
                    1 + zeta*zeta + acceleration_parallel / (a*a))
                direct_derivative_per_G = (v1*a - speed*a1) / (a*a*a)
                self.assertEqual(gamma, direct_derivative_per_G)

    def test_conditional_residence_and_logarithmic_growth(self):
        eta = F(1, 2)
        threshold = F(1)  # sqrt(eta/(1-eta)).
        self.assertEqual(threshold**2 / (1 + threshold**2), eta)
        entry, delta = F(1, 4), F(3, 2)
        bound = (threshold - entry) / delta
        for slope in (delta, delta + 1, 3 * delta):
            duration = (threshold - entry) / slope
            self.assertLessEqual(duration, bound)
            self.assertEqual(entry + slope * duration, threshold)
            amplification = math.exp(float(duration))
            self.assertLessEqual(amplification, math.exp(float(bound)))
        # Physical duration depends on a; the bound is on G, not on time.
        self.assertNotEqual(bound / F(1), bound / F(2))

    def test_vorticity_magnitude_identity_and_active_maximum(self):
        # Local Gaussian intensity q=exp(-(x^2+y^2)/r^2), constant direction.
        # At its peak Delta q/q=-4/r^2. This is a local profile check,
        # not a global periodic Navier--Stokes solution.
        nu, alpha = F(1, 10), F(3, 2)
        radius_squared = 4 * nu / alpha
        laplacian_over_q = -4 / radius_squared
        curvature_radius_squared = -1 / laplacian_over_q
        self.assertEqual(alpha + nu * laplacian_over_q, 0)
        self.assertEqual(alpha * curvature_radius_squared / nu, 1)
        # q(x,t)=2+cos(2x)+t*cos(x) has two active maxima at t=0.
        # For small positive t, Q(t)=3+t; right derivative log(Q)=1/3.
        active_rates = (F(1, 3), F(-1, 3))
        derivative = max(active_rates)
        step = 1e-6
        observed = (math.log(3 + step) - math.log(3)) / step
        self.assertAlmostEqual(observed, float(derivative), places=6)
        self.assertNotEqual(derivative, active_rates[1])

    def test_binary_clause_count_and_resolution_width(self):
        for n in range(1, 6):
            clauses = clauses_of_width_two(n)
            self.assertEqual(len(clauses), 2*n*n + 1)
            for pivot in range(1, n + 1):
                positive = [c for c in clauses if pivot in c]
                negative = [c for c in clauses if -pivot in c]
                for first, second in product(positive, negative):
                    resolvent = (first - {pivot}) | (second - {-pivot})
                    if any(-literal in resolvent for literal in resolvent):
                        continue
                    self.assertLessEqual(len(resolvent), 2)
                    self.assertIn(resolvent, clauses)
                    self.assertNotIn(pivot, resolvent)
                    self.assertNotIn(-pivot, resolvent)


if __name__ == "__main__":
    unittest.main()
