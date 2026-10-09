"""Positive finite controls for resolution, reference projection and composition."""
from itertools import product
from math import log2
import unittest

import numpy as np


def quantities(p):
    p = np.asarray(p, dtype=float)
    collision = float(p @ p)
    resolution = log2(len(p) * collision)
    return collision, resolution, 1 / (len(p) * collision)


def pauli_basis(qubits):
    single = (np.eye(2), np.array([[0, 1], [1, 0]]),
              np.array([[0, -1j], [1j, 0]]), np.diag([1, -1]))
    result = []
    for indices in product(range(4), repeat=qubits):
        matrix = np.ones((1, 1), complex)
        for index in indices:
            matrix = np.kron(matrix, single[index])
        result.append(matrix)
    return result


class ResolutionModalWeightsTests(unittest.TestCase):
    def test_reference_projection_and_resolution_identity(self):
        for p in ([1.], [.5, .5], [1., 0., 0., 0.],
                  [.1, .2, .3, .4], [1 / 8] * 8):
            p = np.asarray(p)
            n = len(p)
            u = np.ones(n) / np.sqrt(n)
            projector = np.outer(u, u)
            v, difference = projector @ p, (np.eye(n) - projector) @ p
            collision, resolution, weight = quantities(p)
            np.testing.assert_allclose(v, np.ones(n) / n)
            self.assertAlmostEqual(v @ difference, 0)
            self.assertAlmostEqual(v @ v, 1 / n)
            self.assertAlmostEqual(difference @ difference, collision - 1 / n)
            self.assertAlmostEqual(weight, 2 ** (-resolution))
            self.assertAlmostEqual(1 / weight - 1, 2 ** resolution - 1)
            self.assertGreaterEqual(resolution, -1e-14)
            self.assertLessEqual(resolution, log2(n) + 1e-14)

    def test_ambient_reflection_and_transitive_reference(self):
        for n in (2, 4, 8):
            u = np.ones(n) / np.sqrt(n)
            projector = np.outer(u, u)
            reflection = 2 * projector - np.eye(n)
            np.testing.assert_allclose(reflection @ reflection, np.eye(n), atol=1e-14)
            np.testing.assert_allclose(reflection.T @ reflection, np.eye(n), atol=1e-14)
            np.testing.assert_allclose(reflection @ u, u, atol=1e-14)
            difference = np.arange(n, dtype=float)
            difference -= difference.mean()
            np.testing.assert_allclose(reflection @ difference, -difference, atol=1e-14)
            translations = []
            for shift in range(n):
                permutation = np.zeros((n, n))
                for x in range(n):
                    permutation[x ^ shift, x] = 1
                translations.append(permutation)
            average = sum(translations) / n
            np.testing.assert_allclose(average, projector)
            self.assertEqual(np.linalg.matrix_rank(average), 1)

    def test_uniform_support_realizations(self):
        for n in (4, 8, 16):
            for support in range(1, n + 1):
                p = np.array([1 / support] * support + [0.] * (n - support))
                collision, resolution, weight = quantities(p)
                self.assertAlmostEqual(collision, 1 / support)
                self.assertAlmostEqual(resolution, log2(n / support))
                self.assertAlmostEqual(weight, support / n)
                if support & (support - 1) == 0:
                    depth = int(log2(n)) - int(log2(support))
                    self.assertAlmostEqual(weight, 2 ** (-depth))

    def test_connected_incidence_image_and_resolved_state_angle(self):
        for n in range(2, 8):
            for edges in ([(i, i + 1) for i in range(n - 1)],
                          [(0, i) for i in range(1, n)]):
                incidence = np.zeros((n, len(edges)))
                for column, (i, j) in enumerate(edges):
                    incidence[i, column], incidence[j, column] = -1, 1
                self.assertEqual(np.linalg.matrix_rank(incidence), n - 1)
                np.testing.assert_allclose(np.ones(n) @ incidence, 0)
                projector = incidence @ np.linalg.pinv(incidence)
                np.testing.assert_allclose(projector, np.eye(n) - np.ones((n, n)) / n,
                                           atol=1e-12)
                for x in range(n):
                    p = np.eye(n)[x]
                    weight = quantities(p)[2]
                    self.assertAlmostEqual(1 / weight - 1, n - 1)

    def test_walsh_parities_and_resolved_coefficients(self):
        for bits in range(1, 5):
            n = 2 ** bits
            walsh = np.array([[(-1) ** ((s & x).bit_count()) / np.sqrt(n)
                               for x in range(n)] for s in range(n)])
            np.testing.assert_allclose(walsh @ walsh.T, np.eye(n), atol=1e-14)
            np.testing.assert_allclose(walsh[0], np.ones(n) / np.sqrt(n))
            np.testing.assert_allclose(walsh[1:].sum(axis=1), 0, atol=1e-14)
            for x in range(n):
                np.testing.assert_allclose((walsh @ np.eye(n)[x]) ** 2, 1 / n)

    def test_independent_tensor_composition(self):
        for p, q in (([.2, .3, .5], [.25, .75]),
                     ([1., 0., 0., 0.], [.1, .2, .3, .4])):
            c1, r1, w1 = quantities(p)
            c2, r2, w2 = quantities(q)
            c12, r12, w12 = quantities(np.kron(p, q))
            self.assertAlmostEqual(c12, c1 * c2)
            self.assertAlmostEqual(r12, r1 + r2)
            self.assertAlmostEqual(w12, w1 * w2)
            n1, n2 = len(p), len(q)
            self.assertEqual(n1 * n2 - 1,
                             (n1 - 1) + (n2 - 1) + (n1 - 1) * (n2 - 1))

    def test_classical_relational_resolution_and_marginal_bound(self):
        correlated = np.diag([.5, .5])
        self.assertAlmostEqual(quantities(correlated.ravel())[1], 1)
        self.assertAlmostEqual(quantities(correlated.sum(axis=0))[1], 0)
        self.assertAlmostEqual(quantities(correlated.sum(axis=1))[1], 0)
        rng = np.random.default_rng(113)
        for rows, columns in ((2, 3), (4, 2), (5, 5)):
            joint = rng.random((rows, columns))
            joint /= joint.sum()
            c_joint, r_joint, _ = quantities(joint.ravel())
            c_marginal, r_marginal, _ = quantities(joint.sum(axis=1))
            self.assertLessEqual(c_joint, c_marginal + 1e-14)
            self.assertLessEqual(r_joint, r_marginal + log2(columns) + 1e-14)

    def test_hilbert_schmidt_reference_and_pauli_expansion(self):
        rng = np.random.default_rng(2113)
        for qubits in (1, 2):
            n = 2 ** qubits
            basis = pauli_basis(qubits)
            psi = rng.normal(size=n) + 1j * rng.normal(size=n)
            psi /= np.linalg.norm(psi)
            pure = np.outer(psi, psi.conj())
            for rho in (pure, np.eye(n) / n, .6 * pure + .4 * np.eye(n) / n):
                purity = float(np.trace(rho @ rho).real)
                reference = np.eye(n) / np.sqrt(n)
                projection = np.trace(reference @ rho).real * reference
                np.testing.assert_allclose(projection, np.eye(n) / n, atol=1e-14)
                self.assertAlmostEqual(np.trace(rho - projection).real, 0)
                resolution = log2(n * purity)
                self.assertAlmostEqual(1 / (n * purity), 2 ** (-resolution))
                coefficients = np.array([np.trace(rho @ observable).real for observable in basis])
                rebuilt = sum(a * observable for a, observable in zip(coefficients, basis)) / n
                np.testing.assert_allclose(rebuilt, rho, atol=1e-14)
                self.assertAlmostEqual(float(coefficients[1:] @ coefficients[1:]),
                                       n * purity - 1)
            self.assertAlmostEqual(log2(n * np.trace(pure @ pure).real), log2(n))


if __name__ == "__main__":
    unittest.main()
