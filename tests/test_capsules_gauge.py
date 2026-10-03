"""Reproducible finite controls for the capsule and SU(2) public notes.

These controls compare independent calculations on finite examples. The
mathematical proofs and their assumptions are in the accompanying public notes.
Run with: python -m unittest discover -s tests -p test_capsules_gauge.py -v
"""

from dataclasses import dataclass
from itertools import product
import random
import unittest

import numpy as np


@dataclass(frozen=True)
class Relation:
    variables: tuple
    rows: frozenset


def boolean_rows(variables):
    return product((0, 1), repeat=len(variables))


def from_predicate(variables, predicate):
    return Relation(
        tuple(variables),
        frozenset(row for row in boolean_rows(variables) if predicate(*row)),
    )


def join(left, right):
    """Natural join by matching the two explicit tables on their common keys."""
    variables = left.variables + tuple(
        name for name in right.variables if name not in left.variables
    )
    common = tuple(name for name in left.variables if name in right.variables)
    rows = set()
    for left_row in left.rows:
        left_values = dict(zip(left.variables, left_row))
        for right_row in right.rows:
            right_values = dict(zip(right.variables, right_row))
            if all(left_values[name] == right_values[name] for name in common):
                merged = {**left_values, **right_values}
                rows.add(tuple(merged[name] for name in variables))
    return Relation(variables, frozenset(rows))


def project(relation, visible):
    """Existential projection as table-column selection and deduplication."""
    visible = tuple(visible)
    indices = tuple(relation.variables.index(name) for name in visible)
    return Relation(
        visible,
        frozenset(tuple(row[index] for index in indices) for row in relation.rows),
    )


def enumerate_conjunction(factors, visible):
    """Independent reference: evaluate every full assignment of all factors."""
    variables = tuple(sorted({name for factor in factors for name in factor.variables}))
    rows = set()
    for row in boolean_rows(variables):
        values = dict(zip(variables, row))
        if all(
            tuple(values[name] for name in factor.variables) in factor.rows
            for factor in factors
        ):
            rows.add(tuple(values[name] for name in visible))
    return Relation(tuple(visible), frozenset(rows))


def truth_table(variables, mask):
    return Relation(
        tuple(variables),
        frozenset(
            row
            for index, row in enumerate(boolean_rows(variables))
            if mask & (1 << index)
        ),
    )


class CapsuleControls(unittest.TestCase):
    def test_all_two_variable_interfaces_match_global_enumeration(self):
        # All 16 truth tables on (x,s), paired with all 16 on (s,y).
        for mask_a, mask_b in product(range(16), repeat=2):
            with self.subTest(mask_a=mask_a, mask_b=mask_b):
                block_a = truth_table(("x", "s"), mask_a)
                block_b = truth_table(("s", "y"), mask_b)
                compatibility = join(
                    project(block_a, ("s",)), project(block_b, ("s",))
                )
                self.assertEqual(
                    compatibility,
                    enumerate_conjunction((block_a, block_b), ("s",)),
                )
                self.assertEqual(
                    project(compatibility, ()),
                    enumerate_conjunction((block_a, block_b), ()),
                )

    def test_recierre_on_smaller_boundary_matches_global_enumeration(self):
        rng = random.Random(6301)
        for case in range(128):
            block_a = truth_table(("x", "i", "z"), rng.randrange(256))
            block_b = truth_table(("i", "z", "y"), rng.randrange(256))
            compatibility = join(
                project(block_a, ("i", "z")),
                project(block_b, ("i", "z")),
            )
            with self.subTest(case=case):
                self.assertEqual(
                    project(compatibility, ("z",)),
                    enumerate_conjunction((block_a, block_b), ("z",)),
                )

    def test_association_preserves_variables_needed_by_later_factors(self):
        block_a = from_predicate(("x", "s"), lambda x, s: x == s)
        block_b = from_predicate(("s", "t"), lambda s, t: s == t)
        block_c = from_predicate(("t", "y"), lambda t, y: t != y)

        # Left grouping removes s, while t is retained for the later C join.
        left_interface = project(join(block_a, block_b), ("x", "t"))
        left_result = project(join(left_interface, block_c), ("x", "y"))

        # Right grouping removes t, while s is retained for the later A join.
        right_interface = project(join(block_b, block_c), ("s", "y"))
        right_result = project(join(block_a, right_interface), ("x", "y"))

        expected = enumerate_conjunction((block_a, block_b, block_c), ("x", "y"))
        self.assertEqual(expected.rows, frozenset({(0, 1), (1, 0)}))
        self.assertEqual(left_result, expected)
        self.assertEqual(right_result, expected)

        # This assertion makes the test sensitive to forgetting a shared key.
        premature = join(project(left_interface, ("x",)), block_c)
        self.assertNotEqual(project(premature, ("x", "y")), expected)

    def test_random_three_factor_association(self):
        rng = random.Random(6302)
        for case in range(128):
            block_a = truth_table(("x", "s"), rng.randrange(16))
            block_b = truth_table(("s", "t"), rng.randrange(16))
            block_c = truth_table(("t", "y"), rng.randrange(16))
            left = project(
                join(project(join(block_a, block_b), ("x", "t")), block_c),
                ("x", "y"),
            )
            right = project(
                join(block_a, project(join(block_b, block_c), ("s", "y"))),
                ("x", "y"),
            )
            with self.subTest(case=case):
                expected = enumerate_conjunction(
                    (block_a, block_b, block_c), ("x", "y")
                )
                self.assertEqual(left, expected)
                self.assertEqual(right, expected)

    def test_empty_and_closed_interfaces(self):
        false_relation = Relation(("x",), frozenset())
        true_relation = Relation(("x",), frozenset({(0,), (1,)}))
        self.assertEqual(project(false_relation, ()).rows, frozenset())
        self.assertEqual(project(true_relation, ()).rows, frozenset({()}))
        self.assertEqual(join(project(true_relation, ()), true_relation), true_relation)
        self.assertEqual(join(project(false_relation, ()), true_relation), false_relation)


def saturated_count(bits, threshold):
    state = 0
    for bit in bits:
        state = min(threshold + 1, state + bit)
    return state


class CounterControls(unittest.TestCase):
    def test_all_short_prefixes_with_same_state_have_same_continuations(self):
        for threshold in range(5):
            for prefix_length in range(5):
                groups = {}
                for prefix in boolean_rows(range(prefix_length)):
                    state = saturated_count(prefix, threshold)
                    groups.setdefault(state, []).append(prefix)
                for state, prefixes in groups.items():
                    for continuation in boolean_rows(range(3)):
                        expected = state + sum(continuation) <= threshold
                        for prefix in prefixes:
                            self.assertEqual(
                                sum(prefix) + sum(continuation) <= threshold, expected
                            )

    def test_random_disjoint_blocks_and_zero_threshold(self):
        rng = random.Random(6303)
        for length in range(41):
            bits = [rng.randrange(2) for _ in range(length)]
            blocks = [[], [], []]
            for bit in bits:
                blocks[rng.randrange(3)].append(bit)
            for threshold in {0, length // 2, length}:
                cap = threshold + 1
                states = [saturated_count(block, threshold) for block in blocks]
                left = min(cap, min(cap, states[0] + states[1]) + states[2])
                right = min(cap, states[0] + min(cap, states[1] + states[2]))
                expected = min(cap, sum(bits))
                with self.subTest(length=length, threshold=threshold):
                    self.assertEqual(left, expected)
                    self.assertEqual(right, expected)
                    self.assertEqual(saturated_count(bits, threshold), expected)
                    self.assertEqual(expected <= threshold, sum(bits) <= threshold)

    def test_saturated_addition_associativity_for_all_small_states(self):
        for threshold in range(8):
            cap = threshold + 1
            for a, b, c in product(range(cap + 1), repeat=3):
                self.assertEqual(
                    min(cap, min(cap, a + b) + c),
                    min(cap, a + min(cap, b + c)),
                )


IDENTITY = np.eye(2, dtype=complex)
PAULI = np.array(
    [
        [[0, 1], [1, 0]],
        [[0, -1j], [1j, 0]],
        [[1, 0], [0, -1]],
    ],
    dtype=complex,
)


def quaternion_matrix(quaternion):
    return quaternion[0] * IDENTITY + 1j * np.einsum("i,ijk->jk", quaternion[1:], PAULI)


def unit_quaternion(rng):
    coordinates = rng.normal(size=4)
    return coordinates / np.linalg.norm(coordinates)


def nu_from_group_commutator(u, v):
    commutator = u @ v @ np.linalg.inv(u) @ np.linalg.inv(v)
    return float(1 - np.trace(commutator).real / 2)


class GaugeControls(unittest.TestCase):
    def test_random_su2_formulas_from_independent_expressions(self):
        rng = np.random.default_rng(6304)
        for case in range(200):
            q, r = unit_quaternion(rng), unit_quaternion(rng)
            u, v = quaternion_matrix(q), quaternion_matrix(r)
            nu = nu_from_group_commutator(u, v)
            difference = u @ v - v @ u
            norm_value = float(np.vdot(difference, difference).real / 4)

            alpha, beta = np.arccos(q[0]), np.arccos(r[0])
            axis_u = q[1:] / np.linalg.norm(q[1:])
            axis_v = r[1:] / np.linalg.norm(r[1:])
            angular = 2 * np.sin(alpha) ** 2 * np.sin(beta) ** 2 * (
                1 - float(axis_u @ axis_v) ** 2
            )
            x, y, z = np.trace(u), np.trace(v), np.trace(u @ v)
            traces = 2 - (x * x + y * y + z * z - x * y * z) / 2

            with self.subTest(case=case):
                np.testing.assert_allclose(u.conj().T @ u, IDENTITY, atol=1e-13)
                np.testing.assert_allclose(v.conj().T @ v, IDENTITY, atol=1e-13)
                self.assertAlmostEqual(abs(np.linalg.det(u) - 1), 0, delta=1e-13)
                self.assertAlmostEqual(abs(np.linalg.det(v) - 1), 0, delta=1e-13)
                self.assertAlmostEqual(nu, norm_value, delta=2e-12)
                self.assertAlmostEqual(nu, angular, delta=2e-12)
                self.assertAlmostEqual(nu, traces.real, delta=2e-12)
                self.assertAlmostEqual(traces.imag, 0, delta=2e-12)
                self.assertGreaterEqual(nu, -1e-12)
                self.assertLessEqual(nu, 2 + 1e-12)

    def test_q8_witness_and_extreme_values(self):
        i, j = 1j * PAULI[0], 1j * PAULI[1]
        np.testing.assert_allclose(np.linalg.matrix_power(i, 4), IDENTITY)
        np.testing.assert_allclose(np.linalg.matrix_power(j, 4), IDENTITY)
        np.testing.assert_allclose(i @ i, -IDENTITY)
        np.testing.assert_allclose(j @ j, -IDENTITY)
        np.testing.assert_allclose(i @ j, -(j @ i))
        np.testing.assert_allclose(i @ j @ np.linalg.inv(i) @ np.linalg.inv(j), -IDENTITY)
        self.assertEqual((np.trace(i), np.trace(i)), (np.trace(i), np.trace(j)))
        self.assertAlmostEqual(nu_from_group_commutator(i, i), 0, delta=1e-13)
        self.assertAlmostEqual(nu_from_group_commutator(i, j), 2, delta=1e-13)
        for central in (IDENTITY, -IDENTITY):
            self.assertAlmostEqual(nu_from_group_commutator(central, j), 0, delta=1e-13)

    def test_common_conjugation_and_central_sign_invariance(self):
        rng = np.random.default_rng(6305)
        for case in range(80):
            u, v, g = [quaternion_matrix(unit_quaternion(rng)) for _ in range(3)]
            expected = nu_from_group_commutator(u, v)
            inverse_g = np.linalg.inv(g)
            with self.subTest(case=case):
                self.assertAlmostEqual(
                    nu_from_group_commutator(g @ u @ inverse_g, g @ v @ inverse_g),
                    expected,
                    delta=2e-12,
                )
                for sign_u, sign_v in product((-1, 1), repeat=2):
                    self.assertAlmostEqual(
                        nu_from_group_commutator(sign_u * u, sign_v * v),
                        expected,
                        delta=2e-12,
                    )

    def test_common_cartan_axis_commutes(self):
        for alpha, beta in product(np.linspace(-np.pi, np.pi, 9), repeat=2):
            u = np.cos(alpha) * IDENTITY + 1j * np.sin(alpha) * PAULI[2]
            v = np.cos(beta) * IDENTITY + 1j * np.sin(beta) * PAULI[2]
            np.testing.assert_allclose(u @ v, v @ u, atol=1e-13)
            self.assertAlmostEqual(nu_from_group_commutator(u, v), 0, delta=1e-13)


if __name__ == "__main__":
    unittest.main()
