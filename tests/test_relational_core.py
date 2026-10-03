"""Finite reproductions of the relational core, using only the standard library.

These tests verify the declared finite realizations; they are not experimental
validation or substitutes for the general mathematical arguments in the notes.
Run directly with Python, with unittest discovery, or with pytest.
"""

from fractions import Fraction
from itertools import product
import random
import unittest


def phase_quarter_turn(vector):
    """Direct sum of J(x, y)=(-y, x) on a real even-dimensional space."""
    if len(vector) % 2:
        raise ValueError("The realization requires an even-dimensional space.")
    return tuple(value for i in range(0, len(vector), 2)
                 for value in (-vector[i + 1], vector[i]))


def finite_lift_counts():
    """Enumerate four 2-by-2 bipartite layers (16**4 directed graphs).

    A lift admits an outgoing edge from every microstate in every layer.
    Reversibility requires a perfect matching in each layer. Exact C4 return
    requires a choice of those matchings whose fourfold composition is identity.
    """
    row_complete = {}
    permutations = {}
    for mask in range(16):
        row_complete[mask] = bool(mask & 0b0011) and bool(mask & 0b1100)
        permutations[mask] = tuple(
            parity for parity, edges in ((0, 0b1001), (1, 0b0110))
            if mask & edges == edges
        )

    counts = {"graphs": 0, "lift": 0, "reversible": 0, "exact_return": 0}
    for layers in product(range(16), repeat=4):
        counts["graphs"] += 1
        if all(row_complete[layer] for layer in layers):
            counts["lift"] += 1
        choices = [permutations[layer] for layer in layers]
        if all(choices):
            counts["reversible"] += 1
            # On two states, a matching is identity or swap. Their composition
            # returns both microstates exactly iff the number of swaps is even.
            if any(sum(selection) % 2 == 0 for selection in product(*choices)):
                counts["exact_return"] += 1
    return counts


class RelationalCoreTests(unittest.TestCase):
    def test_novelty_equals_fiber_splitting_for_all_finite_maps(self):
        # Every sigma:{0,1,2,3}->{0,1,2} and tau:{0,1,2,3}->{0,1}:
        # 81*16=1296 pairs, including nonsurjective and constant signatures.
        checked = 0
        for sigma in product(range(3), repeat=4):
            for tau in product(range(2), repeat=4):
                splits_fiber = any(
                    sigma[x] == sigma[y] and tau[x] != tau[y]
                    for x in range(4) for y in range(4)
                )
                factors = any(
                    all(tau[x] == factor[sigma[x]] for x in range(4))
                    for factor in product(range(2), repeat=3)
                )
                self.assertEqual(splits_fiber, not factors, (sigma, tau))
                old_fibers = len(set(sigma))
                joint_fibers = len(set(zip(sigma, tau)))
                self.assertEqual(splits_fiber, joint_fibers > old_fibers)
                checked += 1
        self.assertEqual(checked, 1296)

    def test_quarter_turn_in_multiple_even_dimensions(self):
        rng = random.Random(16)
        for dimension in (2, 4, 6, 8, 12):
            basis = [tuple(int(i == j) for i in range(dimension))
                     for j in range(dimension)]
            vectors = basis + [tuple(rng.randint(-9, 9) for _ in range(dimension))
                               for _ in range(20)]
            for vector in vectors:
                first = phase_quarter_turn(vector)
                second = phase_quarter_turn(first)
                third = phase_quarter_turn(second)
                fourth = phase_quarter_turn(third)
                self.assertEqual(second, tuple(-value for value in vector))
                self.assertEqual(fourth, vector)
                self.assertEqual(sum(x * x for x in first), sum(x * x for x in vector))
                if any(vector):
                    self.assertEqual(len({vector, first, second, third}), 4)

    def test_c4_regular_representation_splits_into_declared_sectors(self):
        constant = (1, 1, 1, 1)
        alternating = (1, -1, 1, -1)
        cosine = (1, 0, -1, 0)
        sine = (0, 1, 0, -1)
        shift = lambda vector: (vector[-1], *vector[:-1])
        self.assertEqual(shift(constant), constant)
        self.assertEqual(shift(alternating), tuple(-x for x in alternating))
        self.assertEqual(shift(cosine), sine)
        self.assertEqual(shift(sine), tuple(-x for x in cosine))
        basis = (constant, alternating, cosine, sine)
        for i, left in enumerate(basis):
            for j, right in enumerate(basis):
                inner = sum(x * y for x, y in zip(left, right))
                self.assertEqual(inner == 0, i != j)

    def test_independent_phase_actions_generate_all_sixteen_signatures(self):
        signatures = set(product(range(4), repeat=2))
        advance_a = lambda state: ((state[0] + 1) % 4, state[1])
        advance_b = lambda state: (state[0], (state[1] + 1) % 4)
        for start in signatures:
            self.assertEqual(advance_a(advance_b(start)), advance_b(advance_a(start)))
            orbit = {((start[0] + a) % 4, (start[1] + b) % 4)
                     for a, b in signatures}
            self.assertEqual(orbit, signatures)
            # Every group element has order dividing four; the independent
            # two-coordinate support contains 16 states and has capacity 4 bits.
            self.assertEqual(((4 * start[0]) % 4, (4 * start[1]) % 4), (0, 0))
        self.assertEqual(len(signatures), 2 ** 4)

    def test_translation_averaging_selects_uniform_normalized_measure(self):
        signatures = tuple(product(range(4), repeat=2))
        rng = random.Random(115)
        for _ in range(10):
            weights = {state: Fraction(rng.randint(1, 40)) for state in signatures}
            total = sum(weights.values())
            averaged = {
                state: sum(weights[((state[0] + a) % 4, (state[1] + b) % 4)]
                           for a, b in signatures) / (16 * total)
                for state in signatures
            }
            self.assertEqual(set(averaged.values()), {Fraction(1, 16)})
            self.assertEqual(sum(averaged.values()), 1)
            atom = averaged[(0, 0)]
            complement = sum(weight for state, weight in averaged.items() if state != (0, 0))
            self.assertEqual(complement, Fraction(15, 16))
            self.assertEqual(complement / atom, 15)

    def test_complex_hermitian_locality_uses_conjugated_multiplier(self):
        # B is antilinear in the first argument. Arbitrary complex multipliers
        # exercise B(fg,h)=B(f,conj(g)h), beyond real indicator functions.
        rng = random.Random(20261003)
        for dimension in (2, 4, 16):
            weights = [rng.randint(1, 9) for _ in range(dimension)]

            def inner(left, right):
                return sum(weight * x.conjugate() * y
                           for weight, x, y in zip(weights, left, right))

            for _ in range(50):
                vectors = [tuple(complex(rng.randint(-5, 5), rng.randint(-5, 5))
                                 for _ in range(dimension)) for _ in range(3)]
                f, g, h = vectors
                fg = tuple(x * y for x, y in zip(f, g))
                conjugate_g_h = tuple(x.conjugate() * y for x, y in zip(g, h))
                self.assertEqual(inner(fg, h), inner(f, conjugate_g_h))
                self.assertEqual(inner(f, h), inner(h, f).conjugate())
                self.assertEqual(inner(f, f).imag, 0)
                self.assertGreaterEqual(inner(f, f).real, 0)
            for i in range(dimension):
                for j in range(dimension):
                    e_i = tuple(complex(k == i) for k in range(dimension))
                    e_j = tuple(complex(k == j) for k in range(dimension))
                    self.assertEqual(inner(e_i, e_j), weights[i] if i == j else 0)

    def test_all_65536_graphs_reproduce_lift_reversibility_and_return_counts(self):
        self.assertEqual(finite_lift_counts(), {
            "graphs": 65536,
            "lift": 6561,
            "reversible": 2401,
            "exact_return": 1753,
        })


if __name__ == "__main__":
    unittest.main()
