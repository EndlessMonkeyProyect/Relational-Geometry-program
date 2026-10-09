"""Finite counterexamples for canonical boundaries, not physical validation."""
from fractions import Fraction
from itertools import product
import math


def test_refinement_need_not_fill_the_product():
    states = {(0, 0), (0, 1), (1, 0)}
    assert any(x[0] == y[0] and x[1] != y[1] for x, y in product(states, repeat=2))
    assert states != set(product({x[0] for x in states}, {x[1] for x in states}))


def test_common_upper_bounds_can_be_minimal_without_a_join():
    nodes = set('xyab')
    order = {(x, x) for x in nodes} | {(x, y) for x in 'xy' for y in 'ab'}
    upper = {z for z in nodes if ('x', z) in order and ('y', z) in order}
    minimal = {z for z in upper if not any(w != z and (w, z) in order for w in upper)}
    least = {z for z in upper if all((z, w) in order for w in upper)}
    assert upper == minimal == set('ab')
    assert not least


def test_fixed_phase_leaves_action_continuously_scalable():
    phase = math.pi / 2
    areas = []
    for radius in [0.3, 1.0, math.sqrt(2)]:
        point = complex(radius, 0)
        for _ in range(4):
            point *= complex(math.cos(phase), math.sin(phase))
        assert abs(point - radius) < 1e-12
        areas.append(math.pi * radius**2)
    assert math.isclose(areas[0] / areas[1], 0.09)
    assert math.isclose(areas[2] / areas[1], 2)


def test_proton_alternatives_have_different_squared_lengths():
    quadratic_fraction = Fraction(1, 16)
    complement = 1 - quadratic_fraction
    master_to_projection_squared = 1 / quadratic_fraction
    confinement_to_projection_squared = complement / quadratic_fraction
    assert master_to_projection_squared == 16
    assert confinement_to_projection_squared == 15
    assert Fraction(1, 4)**2 == quadratic_fraction
    assert master_to_projection_squared != confinement_to_projection_squared
