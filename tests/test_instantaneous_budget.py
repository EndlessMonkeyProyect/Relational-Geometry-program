"""Checks for the instantaneous material-vorticity budget (Navier–Stokes branch).

The closure test evolves a small, very well resolved spectral DNS and compares
the instantaneous formulas for D_t(omega) and Y = D_t(D_t omega / q) with
five-level time differences of the actual evolution.
"""

from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "03_navier_stokes" / "scripts"))

from dns_forced_isotropic import Spectral, forcing, initial_field, refine, step  # noqa: E402
from instantaneous_budget import (  # noqa: E402
    budget, closure, perp, rel, top_points,
)

NU, EPS, KF = 0.06, 0.1, 2.0


def _flow(N=24, T=0.4, seed=7):
    sp = Spectral(N)
    U = initial_field(sp, E0=0.3, k0=2.0, seed=seed)
    for _ in range(int(round(T / 0.01))):
        U, _ = step(sp, U, 0.01, NU, EPS, KF)
    return sp, U


def test_growth_coordinate_decomposition_is_an_identity():
    sp, U = _flow()
    g = budget(sp, U, NU, EPS, KF)
    m = g["a"] > 0
    lhs = perp(g["Y"], g["xi"])[:, m] / g["a"][m] - g["b"][:, m]
    rhs = g["P"][:, m] + g["Vc"][:, m] + g["F"][:, m] - 2.0 * g["b"][:, m]
    assert np.max(np.abs(lhs - rhs)) <= 1e-10 * np.max(np.abs(lhs))


def test_refinement_preserves_the_field():
    sp, U = _flow(T=0.1)
    sp2 = Spectral(36)
    u1 = sp.inv(U)
    u2 = sp2.inv(refine(U, 24, 36))
    assert np.max(np.abs(u1[:, ::2, ::2, ::2] - u2[:, ::3, ::3, ::3])) < 1e-12


def test_budget_closes_and_converges_under_refinement():
    """The residual is spatial truncation: it must collapse when N doubles.

    This checks implementation consistency on a declared flow; the analytic
    derivation, rather than this one numerical test, establishes the identity.
    """
    nu = 0.12
    sp, U = Spectral(24), None
    U = initial_field(sp, E0=0.3, k0=2.0, seed=7)
    for _ in range(40):
        U, _ = step(sp, U, 0.01, nu, EPS, KF)
    errs = {}
    for N in (24, 48):
        spN = Spectral(N)
        V = refine(U, 24, N) if N > 24 else U
        for _ in range(20):
            V, _ = step(spN, V, 0.01, nu, EPS, KF)
        sel = top_points(spN, V, 200)
        g, Dt_om_fd, Y_fd = closure(spN, V, nu, EPS, KF, sel, 2e-3)
        errs[N] = (np.median(rel(Dt_om_fd - g["N"], g["N"])),
                   np.median(rel(perp(Y_fd - g["Y"], g["xi"]), perp(g["Y"], g["xi"]))))
    assert errs[48][0] < 1e-3 and errs[48][1] < 1e-3
    assert errs[48][0] < errs[24][0] / 100 and errs[48][1] < errs[24][1] / 100


def test_small_flow_precision_sensitivity():
    """Short paired run only; not a precision audit of production turbulence."""
    sp64, sp32 = Spectral(24), Spectral(24, dtype=np.float32)
    start = initial_field(sp64, E0=0.3, k0=2.0, seed=7)
    high, low = start.copy(), start.astype(np.complex64)
    for _ in range(20):
        high, _ = step(sp64, high, 0.01, NU, EPS, KF)
        low, _ = step(sp32, low, 0.01, NU, EPS, KF)
    field_error = np.linalg.norm(sp64.inv(high)-sp64.inv(low.astype(complex))) / np.linalg.norm(sp64.inv(high))
    sel = top_points(sp64, high, 200)
    gh = budget(sp64, high, NU, EPS, KF, sel=sel)
    gl = budget(sp64, low.astype(complex), NU, EPS, KF, sel=sel)
    assert field_error < 1e-4
    for name in ("N", "Y", "b"):
        assert np.linalg.norm(gl[name]-gh[name]) / np.linalg.norm(gh[name]) < 1e-3


def test_undefined_direction_and_invalid_inputs():
    import pytest
    sp = Spectral(12)
    zero = np.zeros((3,12,12,7), complex)
    with pytest.raises(ValueError, match="band energy"):
        forcing(sp, zero, 0.1, 2)
    with pytest.raises(ValueError, match="even integer"):
        Spectral(13)
    with pytest.raises(ValueError, match="refinement"):
        refine(zero, 12, 8)
    with pytest.raises(ValueError, match="sample sizes"):
        top_points(sp, zero, 0)
    with np.errstate(divide="raise", invalid="raise"):
        g = budget(sp, zero, NU, 0.0, 2)
    assert np.all(g["q"] == 0)
    assert np.all(np.isnan(g["xi"]))
    assert np.all(np.isnan(g["b"]))
