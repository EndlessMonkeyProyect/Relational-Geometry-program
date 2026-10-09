"""Finite controls for contextual contracts, scaled rotations and modal events.

These tests instantiate the public proofs; they do not select physical
registers, channels, dynamics, or particle parameters.
"""
from fractions import Fraction as F
from itertools import permutations, product
from math import sqrt
import unittest


def binary_states(k):
    return list(product((0, 1), repeat=k))


def contextual_signature(state, coordinate_permutations, translations):
    return tuple(state[permutation[0]] ^ shift[0]
                 for permutation in coordinate_permutations for shift in translations)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def scale(factor, vector):
    return tuple(factor * value for value in vector)


def multiply_row(row, matrix):
    return [sum(row[i] * matrix[i][j] for i in range(len(row)))
            for j in range(len(row))]


class FiniteComparisonContractTests(unittest.TestCase):
    def test_translation_contract_and_induced_bit_operations(self):
        for k in range(1, 5):
            with self.subTest(k=k):
                states = binary_states(k)
                identity = [tuple(range(k))]
                signatures = {state: contextual_signature(state, identity, states)
                              for state in states}
                self.assertEqual(len(set(signatures.values())), 2)
                for x, y in product(states, repeat=2):
                    self.assertEqual(signatures[x] == signatures[y], x[0] == y[0])
                for state, shift in product(states, repeat=2):
                    translated = tuple(x ^ a for x, a in zip(state, shift))
                    self.assertEqual(translated[0], state[0] ^ shift[0])

    def test_coordinate_permutations_recover_the_complete_register(self):
        for k in range(1, 5):
            with self.subTest(k=k):
                states = binary_states(k)
                perms = list(permutations(range(k)))
                signatures = {contextual_signature(state, perms, states) for state in states}
                self.assertEqual(len(signatures), 2 ** k)
                for state in states:
                    recovered = []
                    for i in range(k):
                        permutation = next(p for p in perms if p[0] == i)
                        recovered.append(state[permutation[0]])
                    self.assertEqual(tuple(recovered), state)

    def test_geometric_scale_and_normalized_four_phase_closure(self):
        for rho in (F(1, 4), F(1, 2), F(1), F(2)):
            reference = (F(0), F(0), rho)
            for x, y in ((1, 0), (2, -3), (-5, 4)):
                a = (F(x), F(y), F(0))
                ja = cross(a, reference)
                j2a = cross(ja, reference)
                self.assertEqual(dot(ja, a), 0)
                self.assertEqual(dot(ja, reference), 0)
                self.assertEqual(dot(ja, ja), rho ** 2 * dot(a, a))
                self.assertEqual(j2a, scale(-(rho ** 2), a))
                orbit = [a]
                for _ in range(4):
                    orbit.append(scale(1 / rho, cross(orbit[-1], reference)))
                self.assertEqual(orbit[-1], a)
                self.assertEqual(len(set(orbit[:-1])), 4)
                j4a = cross(cross(j2a, reference), reference)
                self.assertEqual(j4a, scale(rho ** 4, a))
        # The double-product formula also holds away from the perpendicular plane.
        reference, a = (F(1), F(2), F(3)), (F(4), F(-2), F(5))
        right = tuple(dot(a, reference) * r - dot(reference, reference) * x
                      for r, x in zip(reference, a))
        self.assertEqual(cross(cross(a, reference), reference), right)

    def test_uniform_measure_and_diagonal_event_projectors(self):
        for k in range(1, 7):
            n = 2 ** k
            uniform = [F(1, n)] * n
            # Averaging the orbit of a point mass over all translations.
            averaged = [sum(F(1, n) if (0 ^ shift) == x else F(0)
                            for shift in range(n)) for x in range(n)]
            self.assertEqual(averaged, uniform)
            for shift in range(n):
                self.assertEqual([uniform[x ^ shift] for x in range(n)], uniform)
            for rank in (0, 1, min(3, n), n):
                event = set(range(rank))
                probability = sum(uniform[x] for x in event)
                self.assertEqual(probability, F(rank, n))
                self.assertEqual(probability + sum(uniform[x] for x in range(n)
                                                  if x not in event), 1)
                amplitudes = [sqrt(float(p)) for p in uniform]
                projected_norm_squared = sum(amplitudes[x] ** 2 for x in event)
                self.assertAlmostEqual(projected_norm_squared, float(probability), places=13)

    def test_invariant_measure_with_prescribed_orbit_masses(self):
        orbits = ({0, 1, 2}, {3, 4})
        orbit_masses = (F(1, 3), F(2, 3))
        measure = [F(1, 9)] * 3 + [F(1, 3)] * 2
        self.assertEqual(sum(measure), 1)
        for permutation in ((1, 2, 0, 3, 4), (0, 1, 2, 4, 3)):
            self.assertEqual([measure[x] for x in permutation], measure)
        event = {0, 3}
        by_orbits = sum(mass * F(len(event & orbit), len(orbit))
                        for orbit, mass in zip(orbits, orbit_masses))
        self.assertEqual(sum(measure[x] for x in event), by_orbits)
        self.assertEqual(by_orbits, F(4, 9))

    def test_mixing_formula_and_total_variation_exactly(self):
        for n, alpha in product((2, 4, 8), (F(1, 3), F(1, 2), F(1))):
            matrix = [[(1 - alpha) * int(i == j) + alpha / n
                       for j in range(n)] for i in range(n)]
            uniform = [F(1, n)] * n
            self.assertEqual([sum(row) for row in matrix], [1] * n)
            self.assertEqual([sum(matrix[i][j] for i in range(n)) for j in range(n)],
                             [1] * n)
            self.assertEqual(multiply_row(uniform, matrix), uniform)
            initial_states = ([F(1)] + [F(0)] * (n - 1),
                              [F(i + 1, n * (n + 1) // 2) for i in range(n)])
            for initial in initial_states:
                current = list(initial)
                tv_initial = sum(abs(a - b) for a, b in zip(initial, uniform)) / 2
                for t in range(7):
                    expected = [u + (1 - alpha) ** t * (value - u)
                                for value, u in zip(initial, uniform)]
                    self.assertEqual(current, expected)
                    tv = sum(abs(a - b) for a, b in zip(current, uniform)) / 2
                    self.assertEqual(tv, (1 - alpha) ** t * tv_initial)
                    current = multiply_row(current, matrix)

    def test_conditional_mass_compatibility_and_radius_choices(self):
        # Internal rational example: no experimental constants or measured data.
        c, hbar = F(12), F(2)
        omega_u, omega_v, omega_m = F(5), F(3), F(4)
        self.assertEqual(omega_u ** 2, omega_v ** 2 + omega_m ** 2)
        mass_a = hbar * omega_m / c ** 2
        choices = (
            (c / omega_v, omega_v, F(4, 3)),
            (c / omega_u, omega_v, F(12, 25)),
            (c / omega_m, omega_v, F(3, 4)),
            (c / omega_u, omega_u, F(4, 5)),
        )
        for radius, omega_f, angular_ratio in choices:
            angular_momentum = hbar * angular_ratio
            mass_f = angular_momentum / (omega_f * radius ** 2)
            self.assertEqual(angular_ratio, omega_m * omega_f * radius ** 2 / c ** 2)
            self.assertEqual(mass_f, mass_a)
            inertia = mass_f * radius ** 2
            self.assertEqual(inertia * omega_f, angular_momentum)
        # Zero complementary frequency is allowed in the general iff formula.
        self.assertEqual(F(0) / (F(3) * F(4) ** 2), hbar * F(0) / c ** 2)
        # Conditional p=2^-4: squares fix the four positive angular ratios
        # sqrt(15), sqrt(15)/16, 1/sqrt(15), and sqrt(15)/4 exactly.
        p = F(1, 2 ** 4)
        squared_ratios = ((1 - p) / p, p * (1 - p), p / (1 - p), 1 - p)
        self.assertEqual(squared_ratios, (F(15), F(15, 256), F(1, 15), F(15, 16)))


if __name__ == "__main__":
    unittest.main()
