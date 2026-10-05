"""Finite controls for the action, signature-content and harmonic notes."""

import math
import unittest
from fractions import Fraction


def factors(value):
    result = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            result[divisor] = result.get(divisor, 0) + 1
            value //= divisor
        divisor += 1
    if value > 1:
        result[value] = result.get(value, 0) + 1
    return result


def canonical_pair(a, previous, omega):
    s, c = math.sin(omega), math.cos(omega)
    return math.sqrt(s) * a, (c * a - previous) / math.sqrt(s)


class ActionAndHarmonicTests(unittest.TestCase):
    def test_canonical_map_rotation_and_invariant(self):
        for omega in (0.15, 0.6, 1.2, math.pi / 2, 2.7):
            s, c = math.sin(omega), math.cos(omega)
            # Jacobian from (a,p) to (Qc,Pc).
            self.assertAlmostEqual(math.sqrt(s) / math.sqrt(s), 1)
            a, previous = 1.7, -0.4
            q0, p0 = canonical_pair(a, previous, omega)
            invariant = (q0*q0 + p0*p0) / 2
            for _ in range(100):
                q, p = canonical_pair(a, previous, omega)
                next_a = 2*c*a - previous
                qn, pn = canonical_pair(next_a, a, omega)
                self.assertAlmostEqual(qn, c*q + s*p, places=11)
                self.assertAlmostEqual(pn, -s*q + c*p, places=11)
                self.assertAlmostEqual((qn*qn + pn*pn)/2, invariant, places=10)
                previous, a = a, next_a

    def test_circle_and_polygon_actions(self):
        action = 2.3
        for period in (3, 4, 5, 7, 12):
            omega = 2*math.pi / period
            radius = math.sqrt(2*action)
            points = [(radius*math.cos(n*omega), -radius*math.sin(n*omega))
                      for n in range(period)]
            polygon = sum((p+pn)*(qn-q)/2 for (q,p),(qn,pn)
                          in zip(points, points[1:] + points[:1]))
            self.assertAlmostEqual(polygon, period*action*math.sin(omega))
            steps = 4096
            circular = sum(2*action*math.sin(2*math.pi*n/steps)**2
                           for n in range(steps)) * (2*math.pi/steps)
            self.assertAlmostEqual(circular, 2*math.pi*action, places=10)
            self.assertLess(polygon, circular)

    def test_uniform_content_and_selected_amplitude(self):
        for size in (4, 16):
            atom = Fraction(1, size)
            for mask in range(1 << size):
                cardinality = mask.bit_count()
                content = sum((atom for i in range(size) if mask & (1 << i)), Fraction())
                self.assertEqual(content, cardinality * atom)
                radius = math.sqrt(2*float(content))
                self.assertAlmostEqual(radius*radius/2, float(content))

    def test_harmonic_classification_and_primitive_orders(self):
        inherited = set()
        for n in range(1, 33):
            value = 2**n - 1
            fs = factors(value)
            old = math.prod(p**a for p,a in fs.items() if p in inherited)
            new = math.prod(p**a for p,a in fs.items() if p not in inherited)
            self.assertEqual(old*new, value)
            self.assertEqual(math.gcd(old, new), 1)
            if n == 1:
                self.assertEqual((old,new), (1,1))
            elif len(factors(n)) == 1 and next(iter(factors(n).values())) == 1:
                self.assertEqual(old, 1)
                self.assertGreater(new, 1)
            elif n == 6:
                self.assertEqual((old,new), (63,1))
            else:
                self.assertGreater(old, 1)
                self.assertGreater(new, 1)
            for p in fs:
                order = next(j for j in range(1, n+1) if pow(2, j, p) == 1)
                self.assertEqual(p not in inherited, order == n)
            inherited.update(fs)

    def test_valuation_signature_witness(self):
        old_primes, new_prime = (3,7), 5
        for value in (1,3,7,9,21,63):
            a, b = factors(value), factors(value*new_prime)
            self.assertEqual(tuple(a.get(p,0) for p in old_primes),
                             tuple(b.get(p,0) for p in old_primes))
            self.assertNotEqual(a.get(new_prime,0), b.get(new_prime,0))


if __name__ == "__main__":
    unittest.main()
