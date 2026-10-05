"""Instantaneous material-vorticity budget from spectral DNS fields.

Implements research targets 1, 2 and 4 of the Navier–Stokes manuscript (§11):

1. Direct PDE budget. The transverse PDE residual

       r_perp = P_perp (nu Lap(omega) + curl f) / q

   is computed from spatial fields, independently of any temporal fit, and the
   balance D_t omega = S omega + nu Lap(omega) + curl f is closed against the
   time-resolved DNS evolution.

2. Signed channel forcing. With N = D_t omega, V = N/q and Y = D_t V, exact
   differentiation of the Navier–Stokes velocity-gradient equation gives

       D_t(S omega) = -H omega + nu (Lap(S) omega + S Lap(omega))
                      + sym(grad f) omega + S curl f,

   with H the pressure Hessian (the S^2 omega terms cancel because the
   rotation tensor annihilates omega). Hence D_t N = Pi + Vis + Frc with

       Pi  = -H omega
       Vis = nu (Lap(S) omega + S Lap(omega) + D_t Lap(omega))
       Frc = sym(grad f) omega + S curl f + D_t curl f

   and Y = D_t N / q - a V, so that on a > 0

       P_perp db/dG = Y_perp/a - b = P + V_c + F - 2 b,
       P = P_perp Pi /(a q),  V_c = P_perp Vis /(a q),  F = P_perp Frc /(a q).

   Only the deviatoric pressure Hessian survives the transverse projection.

4. Resolution audit. The same quantities are evaluated on a spectrally refined
   field (N=192) and compared pointwise on the common grid points.

Subcommands
-----------
    stats    full-grid budget statistics for one or more N=128 snapshots
    closure  time-resolved closure of D_t omega and Y at high-vorticity points
    audit    refine a snapshot, evolve both resolutions, compare pointwise
    refine   refine snapshots and evolve the added scales

All tables are written as CSV; see docs/instantaneous_budget.md.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dns_forced_isotropic import (  # noqa: E402
    Spectral, band_energy, diagnostics, forcing_coefficient,
    full_tendency, load_state, refine, step,
)

RHO_LOW = 0.05
CHUNK = 400_000  # points per budget evaluation (bounds peak memory)


# ----------------------------------------------------------------------------
# spectral evaluation helpers
# ----------------------------------------------------------------------------

class Sampler:
    """Inverse transforms followed by sampling at a fixed set of grid points.

    Components are transformed one at a time so that the peak memory stays at a
    few full-grid scalars even for N=192 tensor gradients.
    """

    def __init__(self, sp: Spectral, sel=None):
        self.sp = sp
        self.sel = sel  # None (all points, flattened) or tuple of 3 index arrays
        self.n = sp.N**3 if sel is None else sel[0].size

    def take(self, phys):
        lead = phys.shape[:-3]
        if self.sel is None:
            return phys.reshape(lead + (-1,))
        return phys[(Ellipsis,) + self.sel]

    def __call__(self, F):
        lead = F.shape[:-3]
        out = np.empty(lead + (self.n,))
        for ix in np.ndindex(*lead):
            out[ix] = self.take(self.sp.inv(F[ix]))
        return out

    def grad(self, F):
        """Sampled gradient: out[..., j, :] = d_j of the field F[...]."""
        lead = F.shape[:-3]
        out = np.empty(lead + (3, self.n))
        for ix in np.ndindex(*lead):
            for j in range(3):
                out[ix + (j,)] = self.take(self.sp.inv(self.sp.ik[j] * F[ix]))
        return out


def grad_hat(sp: Spectral, F):
    """Spectral gradient: F[..., kx, ky, kz] -> G[..., j, ...] = i k_j F."""
    ik = sp.ik
    return np.stack([ik[0] * F, ik[1] * F, ik[2] * F], axis=F.ndim - 3)


def forcing_parts(sp: Spectral, U, dUdt, eps_in, kf):
    """Exact forcing, its curl, gradient and time derivative (band-limited)."""
    _, idx, wb = sp.band(kf)
    sel = (slice(None),) + idx
    Ef = band_energy(sp, U, kf)
    c = forcing_coefficient(Ef, eps_in)
    dEf = float(np.sum(wb * np.sum(np.real(np.conj(U[sel]) * dUdt[sel]), axis=0))) / sp.norm
    cdot = -c * dEf / Ef if c != 0 else 0.0
    Fh = np.zeros_like(U)
    Fh[sel] = c * U[sel]
    dFh = np.zeros_like(U)
    dFh[sel] = c * dUdt[sel] + cdot * U[sel]
    return Fh, dFh, c, cdot


def budget(sp: Spectral, U, nu, eps_in, kf, sel=None, with_gradients=False):
    """Evaluate every budget field at the selected points.

    Returns a dict of arrays with the spatial index last. Vectors have shape
    (3, n), tensors (3, 3, n) with T[i, j] = d_j (.)_i where relevant.
    """
    sp_ = sp
    S_ = Sampler(sp_, sel)
    U = U.astype(sp_.cdtype)
    out = {}

    out["u"] = S_(U)
    Ah = grad_hat(sp_, U)                      # Ah[i, j] = i k_j U_i
    full = Sampler(sp_, None)
    A_full = np.empty((3, 3) + (sp_.N,) * 3)
    for i in range(3):
        for j in range(3):
            A_full[i, j] = sp_.inv(Ah[i, j])   # A[i, j] = d_j u_i
    trA2 = np.einsum("ij...,ji...->...", A_full, A_full)
    A = S_.take(A_full)
    del A_full, full
    ph = sp_.fwd(trA2) * sp_.mask * sp_.k2inv   # Lap p = -tr(A^2)
    del trA2
    kx, ky, kz = sp_.k
    kk = (kx, ky, kz)
    H = np.empty((3, 3) + A.shape[2:])
    for i in range(3):
        for j in range(i, 3):
            H[i, j] = S_(-kk[i] * kk[j] * ph)
            H[j, i] = H[i, j]
    out["A"], out["H"] = A, H
    S = 0.5 * (A + A.transpose(1, 0, *range(2, A.ndim)))
    om = np.stack([A[2, 1] - A[1, 2], A[0, 2] - A[2, 0], A[1, 0] - A[0, 1]])
    out["S"], out["om"] = S, om

    LA = np.empty((3, 3, S_.n))
    for i in range(3):
        for j in range(3):
            LA[i, j] = S_.take(sp_.inv(-sp_.k2 * Ah[i, j]))
    out["LapS"] = 0.5 * (LA + LA.transpose(1, 0, *range(2, LA.ndim)))
    out["Lapom"] = np.stack([LA[2, 1] - LA[1, 2], LA[0, 2] - LA[2, 0], LA[1, 0] - LA[0, 1]])
    del LA

    dUdt = full_tendency(sp_, U, nu, eps_in, kf)
    Fh, dFh, c, cdot = forcing_parts(sp_, U, dUdt, eps_in, kf)
    out["forcing_c"], out["forcing_cdot"] = c, cdot

    omh = sp_.curl(U)
    Lomh = -sp_.k2 * omh
    out["dt_Lapom"] = S_(-sp_.k2 * sp_.curl(dUdt))
    out["grad_Lapom"] = S_.grad(Lomh)                    # [i, j] = d_j Lap(om)_i
    cfh = sp_.curl(Fh)
    out["curlf"] = S_(cfh)
    out["gradf"] = S_.grad(Fh)                           # [i, j] = d_j f_i
    out["dt_curlf"] = S_(sp_.curl(dFh))
    out["grad_curlf"] = S_.grad(cfh)
    # Galerkin-consistent material derivative of omega (what the DNS evolves);
    # its difference from S omega + nu Lap(omega) + curl f is the spatial
    # truncation of the nonlinear term and is reported as a resolution term.
    out["dt_om_G"] = S_(sp_.curl(dUdt))
    out["grad_om"] = S_.grad(omh)                         # [i, k] = d_k om_i
    if with_gradients:
        Sh = 0.5 * (Ah + Ah.transpose(1, 0, 2, 3, 4))
        out["grad_S"] = S_.grad(Sh)                       # [i, j, k] = d_k S_ij
    del Ah
    return assemble(out, nu)


def mv(T, v):
    return np.einsum("ij...,j...->i...", T, v)


def dot(a, b):
    return np.sum(a * b, axis=0)


def perp(x, xi):
    return x - dot(xi, x) * xi


def assemble(f, nu):
    """Combine raw fields into the first- and second-order budget."""
    u, S, om, H = f["u"], f["S"], f["om"], f["H"]
    q_raw = np.sqrt(dot(om, om))
    q = np.where(q_raw > 0, q_raw, np.nan)
    xi = om / q
    adv = lambda G: np.einsum("j...,ij...->i...", u, G)  # noqa: E731  (u . grad) of a vector
    Dt_Lapom = f["dt_Lapom"] + adv(f["grad_Lapom"])
    Dt_curlf = f["dt_curlf"] + adv(f["grad_curlf"])
    Sf = 0.5 * (f["gradf"] + f["gradf"].transpose(1, 0, *range(2, f["gradf"].ndim)))

    Som = mv(S, om)
    N = Som + nu * f["Lapom"] + f["curlf"]
    V = N / q
    a = dot(xi, V)
    b = V - a * xi

    Pi = -mv(H, om)
    Vis = nu * (mv(f["LapS"], om) + mv(S, f["Lapom"]) + Dt_Lapom)
    Frc = mv(Sf, om) + mv(S, f["curlf"]) + Dt_curlf
    DtN = Pi + Vis + Frc
    Y = DtN / q - a * V

    N_G = f["dt_om_G"] + adv(f["grad_om"])
    E_trunc = N_G - N

    tau = perp(Som / q, xi)
    r_nu = perp(nu * f["Lapom"] / q, xi)
    r_f = perp(f["curlf"] / q, xi)

    ap = np.where(a > 0, a, np.nan)
    g = {
        "q": q_raw, "xi": xi, "a": a, "b": b, "N": N, "V": V, "Y": Y, "DtN": DtN,
        "alpha": dot(xi, Som / q), "tau": tau, "r_nu": r_nu, "r_f": r_f,
        "P": perp(Pi, xi) / (ap * q), "Vc": perp(Vis, xi) / (ap * q),
        "F": perp(Frc, xi) / (ap * q),
        "u": u, "om": om, "S": S, "N_G": N_G, "e_perp": perp(E_trunc / q, xi),
        "b_G": perp(N_G / q, xi), "a_G": dot(xi, N_G / q),
    }
    for key in ("grad_om", "grad_S", "Lapom", "grad_Lapom", "grad_curlf", "curlf"):
        if key in f:
            g[key] = f[key]
    return g


# ----------------------------------------------------------------------------
# derived observables
# ----------------------------------------------------------------------------

def observables(g):
    """Scalar diagnostics per point (only meaningful where a > 0)."""
    a, b = g["a"], g["b"]
    bn = np.sqrt(dot(b, b))
    rho = np.where(a > 0, bn**2 / (a**2 + bn**2), np.nan)
    T = np.sqrt(dot(g["tau"], g["tau"]))
    r = g["r_nu"] + g["r_f"]
    M = np.sqrt(dot(r, r))
    Mnu = np.sqrt(dot(g["r_nu"], g["r_nu"]))
    Mf = np.sqrt(dot(g["r_f"], g["r_f"]))
    TM = T + M
    with np.errstate(invalid="ignore", divide="ignore"):
        Dperp = bn / TM
        Lam = np.where(a > 0, TM / a, np.nan)
        cosphi = dot(g["tau"], r) / (T * M)
        bh = b / bn
        sP = dot(bh, g["P"]) / bn
        sV = dot(bh, g["Vc"]) / bn
        sF = dot(bh, g["F"]) / bn
    bG = np.sqrt(dot(g["b_G"], g["b_G"]))
    aG = g["a_G"]
    rhoG = np.where(aG > 0, bG**2 / (aG**2 + bG**2), np.nan)
    Me = np.sqrt(dot(g["e_perp"], g["e_perp"]))
    return {
        "rhoG": rhoG, "Me": Me,
        "q": g["q"], "a": a, "bn": bn, "rho": rho, "T": T, "M": M, "Mnu": Mnu, "Mf": Mf,
        "Dperp": Dperp, "Lam": Lam, "cosphi": cosphi,
        "sP": sP, "sV": sV, "sF": sF, "dlogb_dG": sP + sV + sF - 2.0,
        "Pmag": np.sqrt(dot(g["P"], g["P"])), "Vmag": np.sqrt(dot(g["Vc"], g["Vc"])),
        "Fmag": np.sqrt(dot(g["F"], g["F"])),
    }


def masked_stats(x, m):
    x = x[m & np.isfinite(x)]
    if x.size == 0:
        return dict(n=0, median=np.nan, p10=np.nan, p90=np.nan, mean=np.nan, frac_pos=np.nan)
    return dict(n=int(x.size), median=float(np.median(x)), p10=float(np.percentile(x, 10)),
                p90=float(np.percentile(x, 90)), mean=float(np.mean(x)), frac_pos=float(np.mean(x > 0)))


# ----------------------------------------------------------------------------
# subcommands
# ----------------------------------------------------------------------------

def load(path, N_target=None):
    U, t, meta = load_state(path)
    U = U.astype(np.complex128)
    if N_target and N_target != meta["N"]:
        U = refine(U, meta["N"], N_target)
        meta = dict(meta, N=N_target)
    return U, t, meta


def classes(o, qrms):
    pos = (o["a"] > 0) & np.isfinite(o["rho"])
    z = o["q"] / qrms
    return {
        "all_a>0": pos,
        "q>2qrms": pos & (z > 2),
        "q>3qrms": pos & (z > 3),
        "q>3qrms_rho<0.05": pos & (z > 3) & (o["rho"] < RHO_LOW),
        "q>3qrms_rho>=0.05": pos & (z > 3) & (o["rho"] >= RHO_LOW),
        "q>4qrms": pos & (z > 4),
        "q>4qrms_rho<0.05": pos & (z > 4) & (o["rho"] < RHO_LOW),
    }


STAT_VARS = ["rho", "Lam", "Dperp", "cosphi", "sP", "sV", "sF", "dlogb_dG"]
KEEP = ["rhoG", "Me", "bn", "q", "a", "rho", "T", "M", "Mnu", "Mf", "Lam", "Dperp", "cosphi", "sP", "sV", "sF", "dlogb_dG"]


def wquantile(x, w, qs):
    o = np.argsort(x)
    x, w = x[o], w[o]
    c = np.cumsum(w)
    c = (c - 0.5 * w) / c[-1]
    return np.interp(qs, c, x)


def wstats(x, w, m):
    ok = m & np.isfinite(x)
    x, w = x[ok], w[ok]
    if x.size == 0:
        return dict(n=0, median=np.nan, p10=np.nan, p90=np.nan, mean=np.nan, frac_pos=np.nan)
    p10, med, p90 = wquantile(x, w, [0.1, 0.5, 0.9])
    return dict(n=int(x.size), median=float(med), p10=float(p10), p90=float(p90),
                mean=float(np.average(x, weights=w)), frac_pos=float(np.average(x > 0, weights=w)))


def wfrac(cond, w, m):
    return float(np.average(cond[m], weights=w[m])) if m.any() else np.nan


def select_high(sp, U, qrms, z_min=2.0, frac_rest=0.02, seed=0):
    """All points with q > z_min*qrms plus a uniform sample of the rest.

    Returns (sel, weights): weight 1 for the complete high set and
    1/frac_rest for sampled points, so weighted averages are volume averages.
    """
    om = sp.inv(sp.curl(U.astype(sp.cdtype)))
    q = np.sqrt(np.sum(om**2, axis=0)).ravel()
    hi = np.nonzero(q > z_min * qrms)[0]
    lo = np.nonzero(q <= z_min * qrms)[0]
    rng = np.random.default_rng(seed)
    lo = rng.choice(lo, int(frac_rest * lo.size), replace=False)
    idx = np.concatenate([hi, lo])
    w = np.concatenate([np.ones(hi.size), np.full(lo.size, 1.0 / frac_rest)])
    return np.unravel_index(idx, (sp.N,) * 3), w


def stats_from_states(items, outdir, tag, mode="full"):
    """items: iterable of (U, t, meta, label). mode: 'full' or 'high'."""
    rows_tail, rows_cond, rows_meta = [], [], []
    acc = {}
    for U, t, meta, label in items:
        sp = Spectral(meta["N"])
        nu, eps_in, kf = meta["nu"], meta["eps_in"], meta["kf"]
        d = diagnostics(sp, U, nu)
        qrms = np.sqrt(sp.enstrophy(U))
        if mode == "full":
            flat = np.arange(sp.N**3)
            weight_all = np.ones(flat.size)
        else:
            sel_hi, weight_all = select_high(sp, U, qrms)
            flat = np.ravel_multi_index(sel_hi, (sp.N,) * 3)
        t0 = time.time()
        n_eval = 0
        for c0 in range(0, flat.size, CHUNK):
            sl = slice(c0, c0 + CHUNK)
            sel = np.unravel_index(flat[sl], (sp.N,) * 3)
            g = budget(sp, U, nu, eps_in, kf, sel=sel)
            o = observables(g)
            for k in KEEP:
                acc.setdefault(k, []).append(o[k].astype(np.float32))
            acc.setdefault("z", []).append((o["q"] / qrms).astype(np.float32))
            acc.setdefault("w", []).append(weight_all[sl])
            n_eval += o["q"].size
            del g, o
        rows_meta.append(dict(tag=tag, snapshot=label, t=t, N=meta["N"], nu=nu,
                              **{k: d[k] for k in ("urms", "eps", "eta", "kmax_eta", "Re_lambda", "L", "tau_eta")},
                              qrms=qrms, n_evaluated=n_eval, seconds=time.time() - t0))
    for k in acc:
        acc[k] = np.concatenate(acc[k])
    o, z, w = acc, acc["z"], acc["w"]
    pos = (o["a"] > 0) & np.isfinite(o["rho"])
    edges = [0, 1, 2, 3, 4, 5, np.inf]
    for lo, hi in zip(edges[:-1], edges[1:]):
        inbin = (z >= lo) & (z < hi)
        m = pos & inbin
        rows_tail.append(dict(
            tag=tag, q_over_qrms_lo=lo, q_over_qrms_hi=hi, n_points=int(m.sum()),
            frac_growth=wfrac(o["a"] > 0, w, inbin),
            P_rho_lt_0p05=wfrac(o["rho"] < 0.05, w, m),
            P_rho_lt_0p01=wfrac(o["rho"] < 0.01, w, m),
            P_rhoG_lt_0p05=wfrac(o["rhoG"] < 0.05, w, m),
            median_rho=wstats(o["rho"], w, m)["median"]))
    oz = dict(o)
    oz["q"] = z
    for cname, m in classes(oz, 1.0).items():
        for var in STAT_VARS:
            rows_cond.append(dict(tag=tag, cls=cname, var=var, **wstats(o[var].astype(float), w, m)))
        if not m.any():
            continue
        extra = {
            "frac_Dperp_lt_0.5": wfrac(o["Dperp"] < 0.5, w, m),
            "frac_Lam_lt_0.229": wfrac(o["Lam"] < np.sqrt(0.05 / 0.95), w, m),
            "frac_cosphi_lt_-0.5": wfrac(o["cosphi"] < -0.5, w, m),
            "median_Mnu_over_T": wstats((o["Mnu"] / o["T"]).astype(float), w, m)["median"],
            "median_Mf_over_Mnu": wstats((o["Mf"] / o["Mnu"]).astype(float), w, m)["median"],
            "median_Mtrunc_over_b": wstats((o["Me"] / o["bn"]).astype(float), w, m)["median"],
            "median_Mtrunc_over_Mnu": wstats((o["Me"] / o["Mnu"]).astype(float), w, m)["median"],
            "frac_rhoG_lt_0.05": wfrac(o["rhoG"] < RHO_LOW, w, m),
            "frac_dlogb_dG_pos": wfrac(o["dlogb_dG"] > 0, w, m),
        }
        for var, val in extra.items():
            rows_cond.append(dict(tag=tag, cls=cname, var=var, n=int(m.sum()), median=val,
                                  p10=np.nan, p90=np.nan, mean=np.nan, frac_pos=np.nan))
    write_csv(os.path.join(outdir, f"budget_{tag}_snapshots.csv"), rows_meta)
    write_csv(os.path.join(outdir, f"budget_{tag}_tail_vs_q.csv"), rows_tail)
    write_csv(os.path.join(outdir, f"budget_{tag}_conditional.csv"), rows_cond)
    return rows_meta, rows_tail, rows_cond


def iter_snapshots(paths):
    for p in paths:
        U, t, meta = load(p)
        yield U, t, meta, os.path.basename(p)


def refine_and_evolve(path, N_hi, T_evolve, dt, dtype=np.float32):
    """Spectrally refine a snapshot and evolve it so the new scales fill in."""
    U, t, meta = load(path)
    sp = Spectral(N_hi, dtype=dtype)
    V = refine(U, meta["N"], N_hi).astype(sp.cdtype)
    nu, eps_in, kf = meta["nu"], meta["eps_in"], meta["kf"]
    for _ in range(int(round(T_evolve / dt))):
        V, _ = step(sp, V, dt, nu, eps_in, kf)
    meta = dict(meta, N=N_hi, refined_from=os.path.basename(path), refine_T=T_evolve,
                refine_dt=dt, refine_dtype=np.dtype(dtype).name)
    return V.astype(np.complex128), t + T_evolve, meta


def top_points(sp, U, n_top, n_rand=0, seed=0, require_growth=False, nu=None, eps_in=None, kf=None):
    """Indices of the n_top largest-|omega| points plus n_rand uniform points."""
    om = sp.inv(sp.curl(U.astype(sp.cdtype)))
    q = np.sqrt(np.sum(om**2, axis=0)).ravel()
    if not 1 <= n_top <= q.size or not 0 <= n_rand <= q.size:
        raise ValueError("sample sizes must fit the grid")
    idx = np.argpartition(-q, n_top - 1)[:n_top]
    if n_rand:
        rng = np.random.default_rng(seed)
        idx = np.unique(np.concatenate([idx, rng.choice(q.size, n_rand, replace=False)]))
    return np.unravel_index(idx, (sp.N,) * 3)


def evolve_levels(sp, U, nu, eps_in, kf, delta, nlev=5):
    """States at t0 + m*delta, m = -2..2, starting from U at t0 - 2 delta."""
    levels = [U]
    for _ in range(nlev - 1):
        U, _ = step(sp, U, delta, nu, eps_in, kf)
        levels.append(U)
    return levels


def closure(sp, U_start, nu, eps_in, kf, sel, delta):
    """Compare instantaneous D_t omega and Y with 5-level time differences."""
    levels = evolve_levels(sp, U_start, nu, eps_in, kf, delta)
    oms, Vs = [], []
    for L in levels:
        gl = budget_light(sp, L, nu, eps_in, kf, sel)
        oms.append(gl["om"])
        Vs.append(gl["V"])
    c4 = np.array([1.0, -8.0, 0.0, 8.0, -1.0]) / (12.0 * delta)
    dt_om = sum(ci * x for ci, x in zip(c4, oms))
    dt_V = sum(ci * x for ci, x in zip(c4, Vs))
    g = budget(sp, levels[2], nu, eps_in, kf, sel=sel, with_gradients=True)
    u, om = g["u"], g["om"]
    q = np.where(g["q"] > 0, g["q"], np.nan)
    adv = lambda G: np.einsum("j...,ij...->i...", u, G)  # noqa: E731
    Dt_om_fd = dt_om + adv(g["grad_om"])
    # grad V by the chain rule: V = N / q
    gradN = (np.einsum("ijk...,j...->ik...", g["grad_S"], om)
             + np.einsum("ij...,jk...->ik...", g["S"], g["grad_om"])
             + nu * g["grad_Lapom"] + g["grad_curlf"])
    gradq = np.einsum("j...,jk...->k...", om, g["grad_om"]) / q
    gradV = gradN / q - np.einsum("i...,k...->ik...", g["N"], gradq) / q**2
    Y_fd = dt_V + adv(gradV)
    return g, Dt_om_fd, Y_fd


def budget_light(sp, U, nu, eps_in, kf, sel):
    """omega and V = N/q only (used at the extra time levels)."""
    S_ = Sampler(sp, sel)
    A = S_.grad(U)                                      # [i, j] = d_j u_i
    S = 0.5 * (A + A.transpose(1, 0, *range(2, A.ndim)))
    om = np.stack([A[2, 1] - A[1, 2], A[0, 2] - A[2, 0], A[1, 0] - A[0, 1]])
    Lom = S_(-sp.k2 * sp.curl(U))
    dUdt = full_tendency(sp, U, nu, eps_in, kf)
    Fh, _, _, _ = forcing_parts(sp, U, dUdt, eps_in, kf)
    cf = S_(sp.curl(Fh))
    N = mv(S, om) + nu * Lom + cf
    q = np.sqrt(dot(om, om))
    return {"om": om, "V": N / np.where(q > 0, q, np.nan)}


def rel(x, ref):
    return np.sqrt(dot(x, x)) / np.sqrt(dot(ref, ref))


def summarize_closure(tag, g, Dt_om_fd, Y_fd, mask_hi):
    xi = g["xi"]
    eN = Dt_om_fd - g["N"]
    eY = Y_fd - g["Y"]
    Yp = perp(g["Y"], xi)
    eYp = perp(eY, xi)
    bn = np.sqrt(dot(g["b"], g["b"]))
    rnu = np.sqrt(dot(g["r_nu"], g["r_nu"]))
    rows = []
    for name, m in (("top_q", mask_hi), ("top_q_a>0", mask_hi & (g["a"] > 0))):
        def st(x):
            x = x[m & np.isfinite(x)]
            return dict(median=float(np.median(x)), p90=float(np.percentile(x, 90)),
                        max=float(np.max(x)), n=int(x.size))
        rows += [
            dict(tag=tag, set=name, quantity="|DtOmega_fd - N| / |N|", **st(rel(eN, g["N"]))),
            dict(tag=tag, set=name, quantity="|P_perp(DtOmega_fd - N)|/q / |b|", **st(np.sqrt(dot(perp(eN, xi), perp(eN, xi))) / g["q"] / bn)),
            dict(tag=tag, set=name, quantity="|P_perp(DtOmega_fd - N)|/q / |r_nu_perp|", **st(np.sqrt(dot(perp(eN, xi), perp(eN, xi))) / g["q"] / rnu)),
            dict(tag=tag, set=name, quantity="|Y_fd - Y| / |Y|", **st(rel(eY, g["Y"]))),
            dict(tag=tag, set=name, quantity="|P_perp(Y_fd - Y)| / |Y_perp|", **st(rel(eYp, Yp))),
        ]
    return rows


def cmd_closure(path, outdir, tag, n_top=4000, delta=2e-3, N_target=None, U=None, meta=None):
    if U is None:
        U, _, meta = load(path, N_target)
    sp = Spectral(meta["N"])
    nu, eps_in, kf = meta["nu"], meta["eps_in"], meta["kf"]
    sel = top_points(sp, U, n_top)
    g, Dt_om_fd, Y_fd = closure(sp, U, nu, eps_in, kf, sel, delta)
    m = np.ones(g["q"].shape, bool)
    rows = summarize_closure(tag, g, Dt_om_fd, Y_fd, m)
    return rows


def cmd_audit(path, outdir, T_evolve=0.6, dt=4e-3, N_lo=128, N_hi=192, n_top_closure=4000, delta=2e-3,
              save_dir=None):
    U0, t0, meta = load(path)
    nu, eps_in, kf = meta["nu"], meta["eps_in"], meta["kf"]
    out = {}
    for N in (N_lo, N_hi):
        sp = Spectral(N)
        U = U0 if N == N_lo else refine(U0, meta["N"], N)
        nsteps = int(round(T_evolve / dt))
        tw = time.time()
        for _ in range(nsteps):
            U, _ = step(sp, U, dt, nu, eps_in, kf)
        out[N] = (sp, U, time.time() - tw)
        if save_dir:
            from dns_forced_isotropic import save_state
            os.makedirs(save_dir, exist_ok=True)
            save_state(os.path.join(save_dir, f"audit{N}_" + os.path.basename(path)), U, t0 + T_evolve,
                       dict(meta, N=N, audit_from=os.path.basename(path), refine_T=T_evolve, refine_dt=dt,
                            refine_dtype="float64"))
    # common points: i_lo = 2m  <->  i_hi = 3m
    m = np.arange(N_lo // 2)
    I, J, K = np.meshgrid(m, m, m, indexing="ij")
    sel_lo = (2 * I.ravel(), 2 * J.ravel(), 2 * K.ravel())
    sel_hi = (3 * I.ravel(), 3 * J.ravel(), 3 * K.ravel())
    gl = budget(out[N_lo][0], out[N_lo][1], nu, eps_in, kf, sel=sel_lo)
    gh = budget(out[N_hi][0], out[N_hi][1], nu, eps_in, kf, sel=sel_hi)
    ol, oh = observables(gl), observables(gh)
    qrms_h = np.sqrt(out[N_hi][0].enstrophy(out[N_hi][1]))
    diag = {N: diagnostics(out[N][0], out[N][1], nu) for N in (N_lo, N_hi)}
    rows = []
    z = oh["q"] / qrms_h
    for cname, msk in (("q>2qrms_a>0", (z > 2) & (oh["a"] > 0) & (ol["a"] > 0)),
                       ("q>3qrms_a>0", (z > 3) & (oh["a"] > 0) & (ol["a"] > 0))):
        for key, kind in (("om", "vec"), ("b", "vec"), ("tau", "vec"), ("r_nu", "vec"),
                          ("P", "vec"), ("Vc", "vec"), ("F", "vec"), ("Y", "vec")):
            e = rel(gl[key] - gh[key], gh[key])[msk]
            e = e[np.isfinite(e)]
            rows.append(dict(cls=cname, quantity=f"|{key}_128 - {key}_192| / |{key}_192|", n=int(e.size),
                             median=float(np.median(e)), p90=float(np.percentile(e, 90))))
        for key in ("rho", "Lam", "Dperp", "sP", "sV", "sF"):
            x, y = ol[key][msk], oh[key][msk]
            ok = np.isfinite(x) & np.isfinite(y)
            agree = float(np.mean(np.sign(x[ok]) == np.sign(y[ok]))) if key.startswith("s") else np.nan
            rows.append(dict(cls=cname, quantity=f"{key}: median 128 / median 192", n=int(ok.sum()),
                             median=float(np.median(x[ok]) / np.median(y[ok])), p90=agree))
    write_csv(os.path.join(outdir, "budget_resolution_audit.csv"), rows)
    meta_rows = [dict(N=N, **diag[N], evolve_seconds=out[N][2], T_evolve=T_evolve, dt=dt,
                      start=os.path.basename(path)) for N in (N_lo, N_hi)]
    write_csv(os.path.join(outdir, "budget_resolution_audit_runs.csv"), meta_rows)
    # closure at both resolutions from the evolved states
    crow = []
    for N in (N_lo, N_hi):
        sp, U, _ = out[N]
        sel = top_points(sp, U, n_top_closure)
        g, Dt_om_fd, Y_fd = closure(sp, U, nu, eps_in, kf, sel, delta)
        crow += summarize_closure(f"N{N}", g, Dt_om_fd, Y_fd, np.ones(g["q"].shape, bool))
    write_csv(os.path.join(outdir, "budget_closure.csv"), crow)
    # refined-field statistics at high vorticity (N_hi, top points + uniform sample)
    return rows, meta_rows, crow, out


def write_csv(path, rows):
    if not rows:
        return
    keys = []
    for r in rows:
        for k in r:
            if k not in keys:
                keys.append(k)
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: (f"{v:.6g}" if isinstance(v, float) else v) for k, v in r.items()})


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("stats")
    s.add_argument("snapshots", nargs="+")
    s.add_argument("--outdir", required=True)
    s.add_argument("--tag", default="n128")
    s.add_argument("--mode", choices=["full", "high"], default="full")
    r = sub.add_parser("refine", help="refine snapshots, evolve, save refined states")
    r.add_argument("snapshots", nargs="+")
    r.add_argument("--N", type=int, default=192)
    r.add_argument("--T", type=float, default=0.6)
    r.add_argument("--dt", type=float, default=4e-3)
    r.add_argument("--dtype", choices=["float32", "float64"], default="float32")
    r.add_argument("--outdir", required=True)
    c = sub.add_parser("closure")
    c.add_argument("snapshot")
    c.add_argument("--outdir", required=True)
    c.add_argument("--n-top", type=int, default=4000)
    c.add_argument("--delta", type=float, default=2e-3)
    c.add_argument("--tag", default="N128")
    a_ = sub.add_parser("audit")
    a_.add_argument("snapshot")
    a_.add_argument("--outdir", required=True)
    a_.add_argument("--T", type=float, default=0.6)
    a_.add_argument("--dt", type=float, default=4e-3)
    a_.add_argument("--save-dir", default=None)
    args = ap.parse_args()
    os.makedirs(args.outdir, exist_ok=True)
    if args.cmd == "stats":
        stats_from_states(iter_snapshots(args.snapshots), args.outdir, args.tag, mode=args.mode)
    elif args.cmd == "refine":
        from dns_forced_isotropic import save_state
        for p in args.snapshots:
            V, t, meta = refine_and_evolve(p, args.N, args.T, args.dt, np.dtype(args.dtype))
            save_state(os.path.join(args.outdir, f"refined{args.N}_" + os.path.basename(p)), V, t, meta)
    elif args.cmd == "closure":
        rows = cmd_closure(args.snapshot, args.outdir, args.tag, n_top=args.n_top, delta=args.delta)
        write_csv(os.path.join(args.outdir, f"budget_closure_{args.tag}.csv"), rows)
    elif args.cmd == "audit":
        cmd_audit(args.snapshot, args.outdir, T_evolve=args.T, dt=args.dt, save_dir=args.save_dir)


if __name__ == "__main__":
    main()
