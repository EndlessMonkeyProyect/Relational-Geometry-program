"""Exact material-vorticity observables used by the repository.

Public notation reserves E for physical energy and uses D_perp for the
transverse cancellation defect.
"""

from __future__ import annotations
import numpy as np


def material_channels(omega: np.ndarray, Dtomega: np.ndarray):
    """Return q, xi, a, bvec, b, rho for arrays (...,3)."""
    omega = np.asarray(omega, dtype=float)
    Dtomega = np.asarray(Dtomega, dtype=float)
    q = np.linalg.norm(omega, axis=-1)
    if np.any(q <= 0):
        raise ValueError('material_channels requires |omega|>0 on every evaluated state')
    xi = omega / q[..., None]
    v = Dtomega / q[..., None]
    a = np.sum(xi * v, axis=-1)
    bvec = v - a[..., None] * xi
    b = np.linalg.norm(bvec, axis=-1)
    ap = np.maximum(a, 0.0)
    den = ap * ap + b * b
    rho = np.divide(b*b, den, out=np.full_like(b, np.nan), where=den > 0)
    return q, xi, a, bvec, b, rho


def transverse_factorization(xi: np.ndarray, v: np.ndarray, S: np.ndarray):
    """Return tau, r_perp, D_perp, Lambda_perp and geometry.

    Here v = Dtomega/q and S is the symmetric velocity-gradient tensor.
    For a>0, |b|/a = D_perp * Lambda_perp exactly up to floating precision.
    If v is reconstructed independently, the residual may include numerical error;
    this function alone does not establish a physical viscous/forcing balance.
    """
    xi = np.asarray(xi, dtype=float)
    v = np.asarray(v, dtype=float)
    S = np.asarray(S, dtype=float)

    a = np.sum(xi * v, axis=-1)
    Sxi = np.einsum('...ij,...j->...i', S, xi)
    alpha = np.sum(xi * Sxi, axis=-1)
    tau = Sxi - alpha[..., None] * xi

    r = v - Sxi
    rpar = np.sum(xi * r, axis=-1)
    rperp = r - rpar[..., None] * xi

    T = np.linalg.norm(tau, axis=-1)
    M = np.linalg.norm(rperp, axis=-1)
    TM = T + M
    bvec = tau + rperp
    b = np.linalg.norm(bvec, axis=-1)

    D_perp = np.divide(b, TM, out=np.full_like(b, np.nan), where=TM > 0)
    Lambda = np.divide(TM, a, out=np.full_like(a, np.nan), where=a > 0)
    zeta = D_perp * Lambda

    dot = np.sum(tau * rperp, axis=-1)
    cosphi = np.divide(dot, T*M, out=np.full_like(T, np.nan), where=T*M > 0)
    cosphi = np.clip(cosphi, -1.0, 1.0)
    phi = np.arccos(cosphi)

    D_mag = np.divide(np.abs(T-M), TM, out=np.full_like(T, np.nan), where=TM > 0)
    D_ang = np.divide(
        np.sqrt(np.maximum(2*T*M*(1+cosphi), 0.0)),
        TM,
        out=np.full_like(T, np.nan),
        where=TM > 0,
    )

    return {
        'a': a,
        'alpha': alpha,
        'tau': tau,
        'r_parallel': rpar,
        'r_perp': rperp,
        'T': T,
        'M': M,
        'phi_rad': phi,
        'D_mag': D_mag,
        'D_ang': D_ang,
        'D_perp': D_perp,
        'Lambda_perp': Lambda,
        'zeta': zeta,
    }


def episode_integrals(time: np.ndarray, a: np.ndarray, b: np.ndarray):
    """Return G=∫a dt and L=∫|b|dt using NumPy's trapezoidal integration with a compatibility fallback."""
    time = np.asarray(time, dtype=float)
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    if len(time) < 2:
        return 0.0, 0.0
    trap = getattr(np, 'trapezoid', None)
    if trap is None:
        trap = np.trapz
    return float(trap(a, time)), float(trap(b, time))


def dynamic_exit_curvature(
    xi: np.ndarray,
    a: np.ndarray,
    bvec: np.ndarray,
    Y: np.ndarray,
):
    """Return Omega, Q, and kappa for the exact rho evolution law.

    Definitions
    -----------
    V = Dtomega/q = a*xi + bvec
    Y = Dt V
    B = |bvec|^2
    Omega^2 = a^2 + B
    Q = a (bvec·Y) - B (xi·Y) - B Omega^2
    kappa = Q / Omega^4

    Then, wherever q>0 and Omega>0,

        Dt rho_perp = 2 a kappa,

    and on positive-growth segments a>0,

        d rho_perp / d log(q) = 2 kappa.
    """
    xi = np.asarray(xi, dtype=float)
    a = np.asarray(a, dtype=float)
    bvec = np.asarray(bvec, dtype=float)
    Y = np.asarray(Y, dtype=float)

    B = np.sum(bvec * bvec, axis=-1)
    Omega2 = a*a + B
    bY = np.sum(bvec * Y, axis=-1)
    xiY = np.sum(xi * Y, axis=-1)
    Q = a*bY - B*xiY - B*Omega2
    Omega4 = Omega2*Omega2
    kappa = np.divide(
        Q,
        Omega4,
        out=np.full_like(Omega2, np.nan),
        where=Omega4 > 0,
    )
    Omega = np.sqrt(Omega2)
    return Omega, Q, kappa


def kappa_interval_mean(q1, q2, rho1, rho2):
    """Growth-weighted mean kappa from endpoint data.

    Exact on any interval with positive growth a>0:

        kappa_bar_G = (rho2-rho1) / (2 log(q2/q1)).

    This avoids estimating a second material derivative when only endpoint
    q and rho_perp are available.
    """
    q1 = np.asarray(q1, dtype=float)
    q2 = np.asarray(q2, dtype=float)
    rho1 = np.asarray(rho1, dtype=float)
    rho2 = np.asarray(rho2, dtype=float)
    dG = np.log(q2/q1)
    return np.divide(
        rho2-rho1,
        2*dG,
        out=np.full(np.broadcast(q1,q2,rho1,rho2).shape, np.nan, dtype=float),
        where=dG != 0,
    )

