"""Finite controls for the stated spin, measurement and correlation contracts."""
import itertools
import unittest
import numpy as np

I2 = np.eye(2, dtype=complex)
SIGMA = [np.array([[0, 1], [1, 0]], complex),
         np.array([[0, -1j], [1j, 0]], complex), np.diag([1., -1.])]
DOT = sum(np.kron(s, s) for s in SIGMA)
SINGLET = (np.eye(4) - DOT) / 4
TRIPLET = (3 * np.eye(4) + DOT) / 4


def density(vector):
    return (I2 + sum(x * s for x, s in zip(vector, SIGMA))) / 2


def marginal(rho, keep):
    return np.trace(rho.reshape(2, 2, 2, 2), axis1=1 if keep == 0 else 0,
                    axis2=3 if keep == 0 else 2)


def cycle_operator():
    matrix = np.zeros((8, 8), complex)
    for a, b, c in itertools.product((0, 1), repeat=3):
        matrix[4 * c + 2 * a + b, 4 * a + 2 * b + c] = 1
    return matrix


class SpinCompositionTests(unittest.TestCase):
    def test_total_spin_projectors(self):
        for projector, rank in ((SINGLET, 1), (TRIPLET, 3)):
            np.testing.assert_allclose(projector @ projector, projector)
            self.assertAlmostEqual(np.trace(projector).real, rank)
        np.testing.assert_allclose(SINGLET + TRIPLET, np.eye(4))
        np.testing.assert_allclose(SINGLET @ TRIPLET, 0)

    def test_product_probabilities_for_pure_and_mixed_inputs(self):
        vectors = [np.zeros(3), np.array([0, 0, 1.]), np.array([0, 0, -1.]),
                   np.array([.2, .3, .4]), np.array([1., 0, 0])]
        for a, b in itertools.product(vectors, repeat=2):
            rho = np.kron(density(a), density(b))
            self.assertAlmostEqual(np.trace(rho @ TRIPLET).real, (3 + a @ b) / 4)
            self.assertAlmostEqual(np.trace(rho @ SINGLET).real, (1 - a @ b) / 4)

    def test_reusable_bloch_interface_from_three_companions(self):
        for vector in ([0., 0., 1.], [.2, .3, .4], [0., 0., 0.]):
            rho = density(vector)
            answers = [np.trace(np.kron(rho, density(axis)) @ TRIPLET).real
                       for axis in np.eye(3)]
            np.testing.assert_allclose(4 * np.array(answers) - 3, vector, atol=1e-14)

    def test_singlet_correlations_and_resolution(self):
        rho = SINGLET
        for i, first in enumerate(SIGMA):
            for j, second in enumerate(SIGMA):
                self.assertAlmostEqual(np.trace(rho @ np.kron(first, second)).real,
                                       -1 if i == j else 0)
        for keep in (0, 1):
            reduced = marginal(rho, keep)
            np.testing.assert_allclose(reduced, I2 / 2)
            self.assertAlmostEqual(np.log2(2 * np.trace(reduced @ reduced).real), 0)
        self.assertAlmostEqual(np.log2(4 * np.trace(rho @ rho).real), 2)

    def test_diagonal_rotation_invariant_density_family(self):
        for weight in (0, .25, .7, 1):
            rho = weight * SINGLET + (1 - weight) * TRIPLET / 3
            for sigma in SIGMA:
                generator = np.kron(sigma, I2) + np.kron(I2, sigma)
                np.testing.assert_allclose(rho @ generator, generator @ rho, atol=1e-14)
            self.assertAlmostEqual(np.trace(rho @ SINGLET).real, weight)

    def test_independent_unpolarized_ensemble(self):
        rho = np.kron(I2 / 2, I2 / 2)
        self.assertAlmostEqual(np.trace(rho @ SINGLET).real, .25)
        self.assertAlmostEqual(np.trace(rho @ TRIPLET).real, .75)

    def test_projective_measurement_updates_and_record_labels(self):
        rho = np.kron(density([0, 0, 1]), density([0, 0, -1]))
        records = []
        probabilities = []
        for label, projector in ((0, SINGLET), (1, TRIPLET)):
            probability = np.trace(rho @ projector).real
            posterior = projector @ rho @ projector / probability
            self.assertAlmostEqual(np.trace(posterior).real, 1)
            self.assertAlmostEqual(np.trace(posterior @ projector).real, 1)
            probabilities.append(probability)
            records.append(('1s', label))
        self.assertAlmostEqual(sum(probabilities), 1)
        self.assertEqual(len(records), 2)
        self.assertEqual({record[0] for record in records}, {'1s'})

    def test_effective_hyperfine_spectrum_and_units(self):
        energies = np.linalg.eigvalsh(DOT / 4)
        np.testing.assert_allclose(energies, [-.75, .25, .25, .25])
        frequency = 1420.405751768e6
        self.assertAlmostEqual(299792458 / frequency * 100, 21.106, places=3)
        self.assertAlmostEqual(6.62607015e-34 * frequency / 1.602176634e-19 * 1e6,
                               5.874, places=3)

    def test_ternary_chirality_and_cycle(self):
        chi = np.zeros((8, 8), complex)
        for permutation in itertools.permutations(range(3)):
            inversions = sum(permutation[i] > permutation[j] for i in range(3) for j in range(i + 1, 3))
            a, b, c = permutation
            chi += (-1) ** inversions * np.kron(np.kron(SIGMA[a], SIGMA[b]), SIGMA[c])
        np.testing.assert_allclose(chi, chi.conj().T)
        cycle = cycle_operator()
        np.testing.assert_allclose(cycle - cycle.conj().T, -.5j * chi)
        rng = np.random.default_rng(114)
        for _ in range(20):
            vectors = rng.normal(size=(3, 3))
            vectors /= np.linalg.norm(vectors, axis=1)[:, None]
            rho = np.kron(np.kron(density(vectors[0]), density(vectors[1])), density(vectors[2]))
            self.assertAlmostEqual(np.trace(rho @ chi).real,
                                   vectors[0] @ np.cross(vectors[1], vectors[2]))


if __name__ == '__main__':
    unittest.main()
