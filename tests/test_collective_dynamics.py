"""Finite controls for collective two-layer dynamics and quotient metrics."""

from fractions import Fraction
import itertools
import unittest

import numpy as np


def quotient_data(metric, interface):
    """Return the minimal-norm right inverse and induced quotient metric."""
    adjoint = np.linalg.solve(metric, interface.T)
    quotient_metric = np.linalg.inv(interface @ adjoint)
    return adjoint @ quotient_metric, quotient_metric


class CollectiveDynamicsTests(unittest.TestCase):
    def test_small_integer_operators_exactly(self):
        # Exact rational arithmetic; no numerical tolerance decides closure.
        rows = [row for row in itertools.product((-1, 0, 1), repeat=2)
                if row != (0, 0)]
        for t0, t1 in rows:
            hidden = (-t1, t0)
            pivot = 0 if t0 else 1
            for a, b, c, d in itertools.product((-1, 0, 1), repeat=4):
                tk = (t0 * a + t1 * c, t0 * b + t1 * d)
                hidden_response = tk[0] * hidden[0] + tk[1] * hidden[1]
                kbar = Fraction(tk[pivot], (t0, t1)[pivot])
                intertwines = (tk == (kbar * t0, kbar * t1))
                self.assertEqual(hidden_response == 0, intertwines)
                if not intertwines:
                    # Initial pairs (0, 0) and (0, hidden) look identical,
                    # but their next observations differ by this amount.
                    self.assertEqual(t0 * hidden[0] + t1 * hidden[1], 0)
                    self.assertNotEqual(-hidden_response, 0)
                    continue
                for p, q, x, z in itertools.product((-1, 0, 1), repeat=4):
                    observed_next = (t0 * (2 * x - p - a * x - b * z)
                                     + t1 * (2 * z - q - c * x - d * z))
                    effective_next = (2 * (t0 * x + t1 * z)
                                      - (t0 * p + t1 * q)
                                      - kbar * (t0 * x + t1 * z))
                    self.assertEqual(observed_next, effective_next)

    def test_sum_closes_across_coupled_components(self):
        interface = np.array([[1., 1.]])
        for b in (-1.5, -0.5, 0.5, 1.5):
            operator = np.array([[2., b], [b, 2.]])
            np.testing.assert_allclose(interface @ operator,
                                       (2 + b) * interface)
            previous, current = np.array([1., -2.]), np.array([3., 1.])
            observed_previous = float((interface @ previous)[0])
            observed_current = float((interface @ current)[0])
            for _ in range(40):
                nxt = 2 * current - previous - operator @ current
                observed_next = -b * observed_current - observed_previous
                self.assertAlmostEqual(float((interface @ nxt)[0]),
                                       observed_next, places=10)
                previous, current = current, nxt
                observed_previous, observed_current = observed_current, observed_next

    def test_coordinate_interface_does_not_close(self):
        interface = np.array([[1., 0.]])
        hidden = np.array([0., 1.])
        for b in (-1.5, -0.5, 0.5, 1.5):
            operator = np.array([[2., b], [b, 2.]])
            np.testing.assert_array_equal(interface @ hidden, [0.])
            next_observation = interface @ (2 * hidden - operator @ hidden)
            np.testing.assert_allclose(next_observation, [-b])
            self.assertNotEqual(float(next_observation[0]), 0)

    def test_second_initial_layer_is_necessary(self):
        operator = np.array([[2., 0.5], [0.5, 2.]])
        interface = np.array([[1., 1.]])
        current = np.array([1., -1.])
        next_with_zero_previous = 2 * current - operator @ current
        next_with_other_previous = next_with_zero_previous - np.array([1., 0.])
        self.assertAlmostEqual(float((interface @ next_with_zero_previous)[0]), 0)
        self.assertAlmostEqual(float((interface @ next_with_other_previous)[0]), -1)

    def test_general_metric_and_minimal_lift(self):
        metric = np.diag([2., 3., 5.])
        interface = np.array([[1., 1., 0.], [0., 1., 1.]])
        lift, quotient_metric = quotient_data(metric, interface)
        np.testing.assert_allclose(interface @ lift, np.eye(2), atol=1e-14)
        np.testing.assert_allclose(lift.T @ metric @ lift, quotient_metric)
        hidden = np.array([-1., 1., -1.])
        np.testing.assert_allclose(lift.T @ metric @ hidden, 0, atol=1e-14)
        for y in (np.array([1., 0.]), np.array([2., -3.])):
            minimal = lift @ y
            for scale in (-3., -1., 1., 2.):
                other = minimal + scale * hidden
                np.testing.assert_allclose(interface @ other, y, atol=1e-14)
                self.assertGreater(other @ metric @ other,
                                   minimal @ metric @ minimal)

    def test_self_adjoint_positive_operator_uses_quotient_metric(self):
        metric = np.diag([2., 3., 5.])
        interface = np.array([[1., 1., 0.], [0., 1., 1.]])
        lift, quotient_metric = quotient_data(metric, interface)
        effective = np.linalg.solve(quotient_metric, np.diag([1., 2.]))
        hidden_projection = np.eye(3) - lift @ interface
        operator = lift @ effective @ interface + 2 * hidden_projection
        np.testing.assert_allclose(metric @ operator, operator.T @ metric,
                                   atol=1e-14)
        self.assertGreater(np.linalg.eigvalsh(metric @ operator).min(), 0)
        np.testing.assert_allclose(interface @ operator,
                                   effective @ interface, atol=1e-14)
        np.testing.assert_allclose(operator @ lift, lift @ effective, atol=1e-14)
        np.testing.assert_allclose(quotient_metric @ effective,
                                   effective.T @ quotient_metric, atol=1e-14)
        self.assertGreater(np.linalg.eigvalsh(quotient_metric @ effective).min(), 0)
        self.assertFalse(np.allclose(effective, effective.T))

    def test_invisible_stable_mode_has_nonzero_action_invariant(self):
        b = 0.5
        operator = np.array([[2., b], [b, 2.]])
        hidden_mode = np.array([1., -1.]) / np.sqrt(2)
        interface = np.array([[1., 1.]])
        kappa = 2 - b
        cosine = 1 - kappa / 2
        sine = np.sqrt(1 - cosine ** 2)

        def action(previous, current):
            return (sine * current ** 2
                    + (cosine * current - previous) ** 2 / sine) / 2

        previous, current = 0., 1.
        initial_action = action(previous, current)
        self.assertGreater(initial_action, 0)
        for _ in range(40):
            state = current * hidden_mode
            np.testing.assert_allclose(interface @ state, 0, atol=1e-14)
            np.testing.assert_allclose(operator @ state, kappa * state, atol=1e-14)
            self.assertAlmostEqual(action(previous, current), initial_action, places=12)
            previous, current = current, (2 - kappa) * current - previous

    def test_discrete_lagrangian_separates_visible_and_hidden_parts(self):
        metric = np.diag([2., 3., 5.])
        interface = np.array([[1., 1., 0.], [0., 1., 1.]])
        lift, quotient_metric = quotient_data(metric, interface)
        effective = np.linalg.solve(quotient_metric, np.diag([1., 2.]))
        hidden_projection = np.eye(3) - lift @ interface
        operator = lift @ effective @ interface + 2 * hidden_projection

        def lagrangian(current, nxt, matrix, inner_product):
            change = nxt - current
            return (change @ inner_product @ change
                    - current @ inner_product @ matrix @ current) / 2

        for values in itertools.product((-1., 0., 1.), repeat=6):
            current, nxt = np.array(values[:3]), np.array(values[3:])
            total = lagrangian(current, nxt, operator, metric)
            visible = lagrangian(interface @ current, interface @ nxt,
                                 effective, quotient_metric)
            hidden = lagrangian(hidden_projection @ current,
                                hidden_projection @ nxt, operator, metric)
            self.assertAlmostEqual(total, visible + hidden, places=11)

    def test_longer_memory_can_close_a_nonclosing_interface(self):
        for b in (-1.5, -0.5, 0.5, 1.5):
            operator = np.array([[2., b], [b, 2.]])
            previous, current = np.array([0., 1.]), np.array([1., 2.])
            observed = [previous[0], current[0]]
            for _ in range(20):
                previous, current = current, 2 * current - previous - operator @ current
                observed.append(current[0])
            for index in range(2, len(observed) - 2):
                residual = (observed[index + 2] + (2 - b ** 2) * observed[index]
                            + observed[index - 2])
                self.assertAlmostEqual(residual, 0, places=10)


if __name__ == "__main__":
    unittest.main()
