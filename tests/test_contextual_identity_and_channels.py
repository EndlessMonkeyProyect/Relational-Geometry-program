"""Exact finite controls for contextual identities and information channels."""

import itertools
import unittest


STATES = tuple(itertools.product((0, 1), repeat=2))


def factors(signature, observable, states=STATES):
    answers = {}
    for state in states:
        key = signature(state)
        value = observable(state)
        if key in answers and answers[key] != value:
            return False
        answers[key] = value
    return True


def minimal_recoverers(channels, observable):
    sufficient = []
    for mask in range(1 << len(channels)):
        signature = lambda x: tuple(f(x) for i, f in enumerate(channels)
                                    if mask & (1 << i))
        if factors(signature, observable):
            sufficient.append(mask)
    return [mask for mask in sufficient
            if not any(other != mask and other & mask == other
                       for other in sufficient)]


class ContextualIdentityTests(unittest.TestCase):
    def test_parity_contexts_and_composition(self):
        parity = lambda x: x[0] ^ x[1]
        xor = lambda x, y: (x[0] ^ y[0], x[1] ^ y[1])
        for x, xp in itertools.product(STATES, repeat=2):
            same_contexts = all(parity(xor(x, z)) == parity(xor(xp, z))
                                for z in STATES)
            self.assertEqual(same_contexts, parity(x) == parity(xp))
        for x, xp, y, yp in itertools.product(STATES, repeat=4):
            if parity(x) == parity(xp) and parity(y) == parity(yp):
                self.assertEqual(parity(xor(x, y)), parity(xor(xp, yp)))

    def test_recoverability_and_refined_contract(self):
        parity = lambda x: x[0] ^ x[1]
        self.assertFalse(factors(parity, lambda x: x[0]))
        self.assertFalse(factors(parity, lambda x: x[1]))
        refined = lambda x: (parity(x), x[0])
        self.assertTrue(factors(refined, lambda x: x))
        # Exhaust every four-label interface: injectivity is equivalent
        # to recovery of all declared constitutive coordinates.
        for labels in itertools.product(range(4), repeat=4):
            mapping = dict(zip(STATES, labels))
            signature = mapping.__getitem__
            recover_all = all(factors(signature, lambda x, i=i: x[i])
                              for i in range(2))
            self.assertEqual(recover_all, len(set(labels)) == len(STATES))

    def test_minimal_channel_patterns(self):
        a, b = lambda x: x[0], lambda x: x[1]
        zero = lambda x: 0
        parity = lambda x: x[0] ^ x[1]
        self.assertEqual(minimal_recoverers((a, zero, b), parity), [5])
        self.assertEqual(minimal_recoverers((a, a, zero), a), [1, 2])
        self.assertEqual(minimal_recoverers((parity, a, zero), a), [2])
        self.assertEqual(minimal_recoverers((parity, a, zero), b), [3])
        self.assertEqual(minimal_recoverers((parity, a, zero), parity), [1])
        self.assertEqual(minimal_recoverers((a, b, zero), zero), [0])
        self.assertEqual(minimal_recoverers((zero, zero, zero), a), [])

    def test_minimal_sets_determine_all_recovering_sets(self):
        # Exhaust all binary observables and all subsets of three channels.
        channels = (lambda x: x[0], lambda x: x[1],
                    lambda x: x[0] ^ x[1])
        for values in itertools.product((0, 1), repeat=4):
            observable = dict(zip(STATES, values)).__getitem__
            minima = minimal_recoverers(channels, observable)
            for mask in range(8):
                signature = lambda x: tuple(f(x) for i, f in enumerate(channels)
                                            if mask & (1 << i))
                self.assertEqual(factors(signature, observable),
                                 any(m & mask == m for m in minima))


if __name__ == "__main__":
    unittest.main()
