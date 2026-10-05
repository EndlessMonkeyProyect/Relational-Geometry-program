"""Numerical controls for graph comparators, novelty and causal propagation."""

import itertools
import unittest
import numpy as np


def incidence(vertices, edges):
    matrix = np.zeros((len(edges), vertices))
    for row, (i,j) in enumerate(edges):
        matrix[row,i], matrix[row,j] = -1, 1
    return matrix


class ComparatorsAndIncorporationTests(unittest.TestCase):
    def test_local_linear_reference_invariance(self):
        for a,b in itertools.product(range(-4,5), repeat=2):
            if a+b != 0:
                continue
            for x,y in itertools.product(range(-2,3), repeat=2):
                self.assertEqual(a*x+b*y, b*(y-x))
                self.assertEqual(a*(x+7)+b*(y+7), a*x+b*y)
                self.assertEqual(a*y+b*x, -(a*x+b*y))

    def test_weighted_graph_kernel_orientation_and_symmetry(self):
        B = incidence(4, [(0,1),(1,2),(2,3),(3,0)])
        w = np.array([1.,2.,3.,4.])
        C = w[:,None]*B
        K = C.T@C
        np.testing.assert_allclose(K@np.ones(4), 0)
        self.assertEqual(np.linalg.matrix_rank(K), 3)
        self.assertGreaterEqual(np.linalg.eigvalsh(K).min(), -1e-12)
        flipped = np.array([-1,1,-1,1])[:,None]*C
        np.testing.assert_allclose(flipped.T@flipped, K)
        # Equal weights respect cycle rotations.
        P = np.roll(np.eye(4),1,axis=0)
        np.testing.assert_allclose(P.T@(B.T@B)@P, B.T@B)

    def test_log_scale_cycle_compatibility_and_hessian(self):
        B = incidence(3, [(0,1),(1,2),(0,2)])
        s = np.log([1.,2.,6.])
        tau = np.log([2.,3.,6.])
        W = np.diag([1.,2.,3.])
        np.testing.assert_allclose(B@s, tau, atol=1e-14)
        np.testing.assert_allclose(B@(s+4), B@s, atol=1e-14)
        inconsistent = np.log([2.,3.,5.])
        cycle = np.array([1.,1.,-1.])
        np.testing.assert_allclose(cycle@B, 0)
        self.assertAlmostEqual(cycle@inconsistent, np.log(6/5))
        h, direction = 1e-5, np.array([.3,-.2,.7])
        gradient = lambda v: B.T@W@(B@v-inconsistent)
        np.testing.assert_allclose((gradient(s+h*direction)-gradient(s-h*direction))/(2*h),
                                   B.T@W@B@direction, atol=1e-9)

    def test_weighted_representation_refinement(self):
        weights = np.array([1.,2.,3.,4.])
        phi, d = np.array([0,0,1,1]), np.array([0,1,0,0])
        old = np.stack([phi==i for i in (0,1)],axis=1).astype(float)
        labels = list(zip(phi,d))
        unique = sorted(set(labels))
        new = np.array([[pair==key for key in unique] for pair in labels],float)
        P = old@np.linalg.inv(old.T@(weights[:,None]*old))@(old.T*weights)
        residue = (np.eye(4)-P)@new
        self.assertEqual(np.linalg.matrix_rank(new)-np.linalg.matrix_rank(old), 1)
        self.assertEqual(np.linalg.matrix_rank(residue), 1)
        np.testing.assert_allclose(old.T@(weights[:,None]*residue), 0, atol=1e-14)
        # A redundant comparison leaves precisely the old two classes.
        self.assertEqual(len(set(zip(phi, phi+2))), 2)

    def test_incorporation_coupling_stable_modes_and_ratio(self):
        P, Q = np.diag([1.,0.]), np.diag([0.,1.])
        for b in (0.,.2,1.1):
            K = np.array([[2.,b],[b,2.]])
            cross = P@K@Q
            comm = K@Q-Q@K
            self.assertAlmostEqual(np.linalg.norm(comm,2), abs(b))
            self.assertAlmostEqual(np.linalg.norm(cross,2), abs(b))
            vals, vecs = np.linalg.eigh(K)
            np.testing.assert_allclose(vals, [2-abs(b),2+abs(b)])
            self.assertTrue(np.all((vals>0)&(vals<4)))
            if b:
                self.assertTrue(np.all(np.linalg.norm(P@vecs,axis=0)>0))
                self.assertTrue(np.all(np.linalg.norm(Q@vecs,axis=0)>0))
            ratio = np.linalg.norm(cross,2)/np.sqrt(np.linalg.norm(P@K@P,2)*np.linalg.norm(Q@K@Q,2))
            self.assertLessEqual(ratio, 1)

    def test_two_layer_causal_cone(self):
        size, center = 31, 15
        for radius in (1,2):
            previous, current = np.zeros(size), np.zeros(size)
            previous[center], current[center] = 2, 1
            distance = np.abs(np.arange(size)-center)
            for n in range(7):
                self.assertTrue(np.all(current[distance>radius*n]==0))
                nxt = previous + current
                for offset in range(1,radius+1):
                    nxt[offset:] += current[:-offset]
                    nxt[:-offset] += current[offset:]
                previous,current = current,nxt


if __name__ == "__main__":
    unittest.main()
