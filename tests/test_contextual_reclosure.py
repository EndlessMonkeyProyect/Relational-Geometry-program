"""Small exact controls for contextual reclosure, residues and resource contracts."""

import itertools
import unittest


def contextual_signature(state, observable, continuations, action):
    return tuple(observable(action(state, context)) for context in continuations)


def class_map(states, observable, continuations, action):
    signatures = {}
    result = {}
    for state in states:
        signature = contextual_signature(state, observable, continuations, action)
        result[state] = signatures.setdefault(signature, len(signatures))
    return result


def build_boundary_table(relation, interior_bits, boundary_bits):
    """Enumerate internal witnesses; entry index = (internal << b) | boundary."""
    expected = 1 << (interior_bits + boundary_bits)
    if len(relation) != expected:
        raise ValueError("Relation length does not match the declared variables")
    return tuple(any(relation[(i << boundary_bits) | s]
                     for i in range(1 << interior_bits))
                 for s in range(1 << boundary_bits))


def update_boundary_table(table, continuation):
    if len(table) != len(continuation):
        raise ValueError("The continuation must use the same boundary table")
    return tuple(a and b for a, b in zip(table, continuation))


def read_boundary_table(table):
    return any(table)


class ContextualReclosureTests(unittest.TestCase):
    def test_complete_modular_action_and_contextual_stability(self):
        states = contexts = tuple(range(8))
        action = lambda x, c: (x + c) % 8
        for x, c, d in itertools.product(states, contexts, contexts):
            self.assertEqual(action(x, 0), x)
            self.assertIn((c + d) % 8, contexts)
            self.assertEqual(action(action(x, c), d), action(x, (c + d) % 8))
        for modulus in (2, 4):
            observable = lambda x, modulus=modulus: x % modulus
            classes = class_map(states, observable, contexts, action)
            self.assertEqual(len(set(classes.values())), modulus)
            for x, y, c in itertools.product(states, states, contexts):
                self.assertEqual(classes[x] == classes[y], x % modulus == y % modulus)
                if classes[x] == classes[y]:
                    self.assertEqual(classes[action(x, c)], classes[action(y, c)])

    def test_coarsest_interface_factorization_on_a_finite_family(self):
        states = tuple(range(4))
        parity = lambda x: x % 2
        for labels in itertools.product(range(4), repeat=4):
            sufficient = all(labels[x] != labels[y] or parity(x) == parity(y)
                             for x, y in itertools.product(states, repeat=2))
            if not sufficient:
                continue
            decoder = {}
            for state in states:
                label = labels[state]
                if label in decoder:
                    self.assertEqual(decoder[label], parity(state))
                decoder[label] = parity(state)
            self.assertEqual(set(decoder), set(labels))
            self.assertEqual([decoder[labels[x]] for x in states],
                             [parity(x) for x in states])
            self.assertGreaterEqual(len(set(labels)), 2)

    def test_binary_composition_requires_congruence(self):
        states = range(8)
        compose = lambda x, y: (x + y) % 8
        for modulus in (2, 4):
            for x, xp, y, yp in itertools.product(states, repeat=4):
                if x % modulus == xp % modulus and y % modulus == yp % modulus:
                    self.assertEqual(compose(x, y) % modulus,
                                     compose(xp, yp) % modulus)
        # A separate operation may depend on information absent from parity.
        depends_on_hidden_bit = lambda x, y: (x // 2 + y) % 8
        self.assertEqual(0 % 2, 2 % 2)
        self.assertNotEqual(depends_on_hidden_bit(0, 0) % 2,
                            depends_on_hidden_bit(2, 0) % 2)

    def test_refinement_fibers_and_exact_residual_update(self):
        coarse = lambda x: x % 2
        fine = lambda x: x % 4
        fibers = {s: {fine(x) for x in range(8) if coarse(x) == s}
                  for s in range(2)}
        self.assertEqual(fibers, {0: {0, 2}, 1: {1, 3}})
        self.assertEqual(max(map(len, fibers.values())), 2)
        for x, y in itertools.product(range(8), repeat=2):
            s1, r1 = fine(x) % 2, fine(x) // 2
            s2, r2 = fine(y) % 2, fine(y) // 2
            s_next = s1 ^ s2
            r_next = r1 ^ r2 ^ (s1 * s2)
            self.assertEqual(s_next + 2 * r_next, (x + y) % 4)

    def test_minimal_residual_labels_including_unequal_fibers(self):
        for sizes in ((1,), (1, 2), (2, 2), (1, 2, 3)):
            states = tuple((fiber, local) for fiber, size in enumerate(sizes)
                           for local in range(size))
            minimum = max(sizes)
            # Reusing local labels between different fibers attains the bound.
            self.assertEqual(len(set(states)), sum(sizes))
            self.assertEqual(len({local for _, local in states}), minimum)
            if len(set(sizes)) > 1:
                self.assertLess(len(states), len(sizes) * minimum)
            # Exhaust every labeling with fewer labels: one fiber collides.
            for label_count in range(minimum):
                for labels in itertools.product(range(label_count), repeat=len(states)):
                    encoded = {(fiber, label) for (fiber, _), label in zip(states, labels)}
                    self.assertLess(len(encoded), len(states))

    def test_fixed_and_variable_maximum_code_lengths(self):
        for count in range(1, 66):
            fixed_length = (count - 1).bit_length()
            self.assertGreaterEqual(1 << fixed_length, count)
            if fixed_length:
                self.assertLess(1 << (fixed_length - 1), count)
            variable_maximum = count.bit_length() - 1
            self.assertGreaterEqual((1 << (variable_maximum + 1)) - 1, count)
            if variable_maximum:
                self.assertLess((1 << variable_maximum) - 1, count)

    def test_boolean_residual_is_exact_contextual_quotient(self):
        # One internal bit and one boundary bit: all 16 relations, all 4 contexts.
        relations = tuple(itertools.product((False, True), repeat=4))
        contexts = tuple(itertools.product((False, True), repeat=2))
        for first, second in itertools.product(relations, repeat=2):
            first_residual = build_boundary_table(first, 1, 1)
            second_residual = build_boundary_table(second, 1, 1)
            same_responses = all(
                any(first[(i << 1) | s] and context[s]
                    for i, s in itertools.product(range(2), repeat=2))
                == any(second[(i << 1) | s] and context[s]
                       for i, s in itertools.product(range(2), repeat=2))
                for context in contexts)
            self.assertEqual(same_responses, first_residual == second_residual)

    def test_all_two_bit_residuals_have_distinguishing_pinning_contexts(self):
        tables = tuple(itertools.product((False, True), repeat=4))
        self.assertEqual(len(tables), 2 ** (2 ** 2))
        checked = 0
        for first, second in itertools.combinations(tables, 2):
            differing = next(i for i in range(4) if first[i] != second[i])
            pinning = tuple(i == differing for i in range(4))
            self.assertNotEqual(read_boundary_table(update_boundary_table(first, pinning)),
                                read_boundary_table(update_boundary_table(second, pinning)))
            checked += 1
        self.assertEqual(checked, 120)

    def test_build_update_read_commutes_for_all_small_boolean_blocks(self):
        # 256 relations on one internal and two boundary bits, 16 continuations.
        contexts = tuple(itertools.product((False, True), repeat=4))
        checked = 0
        for relation in itertools.product((False, True), repeat=8):
            built = build_boundary_table(relation, 1, 2)
            self.assertEqual(read_boundary_table(built), any(relation))
            for context in contexts:
                continued = tuple(value and context[index % 4]
                                  for index, value in enumerate(relation))
                updated = update_boundary_table(built, context)
                self.assertEqual(updated, build_boundary_table(continued, 1, 2))
                self.assertEqual(read_boundary_table(updated), any(continued))
                checked += 1
        self.assertEqual(checked, 4096)

    def test_iterated_updates_preserve_the_continuation_monoid(self):
        tables = tuple(itertools.product((False, True), repeat=4))
        identity = (True,) * 4
        for initial, first, second in itertools.product(tables, repeat=3):
            self.assertEqual(update_boundary_table(initial, identity), initial)
            iterated = update_boundary_table(update_boundary_table(initial, first), second)
            composed_context = update_boundary_table(first, second)
            self.assertEqual(iterated, update_boundary_table(initial, composed_context))

    def test_table_inputs_respect_declared_boundary(self):
        with self.assertRaises(ValueError):
            build_boundary_table((True, False), 1, 1)
        with self.assertRaises(ValueError):
            update_boundary_table((True, False), (True,))


if __name__ == "__main__":
    unittest.main()
