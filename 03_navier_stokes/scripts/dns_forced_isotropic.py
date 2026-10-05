"""Pseudo-spectral DNS of forced homogeneous isotropic turbulence.

Periodic box [0, 2*pi)^3, rotational form, spherical 2/3 dealiasing,
integrating-factor RK4 for the viscous term, and constant-power forcing on the
band 0 < |k| <= kf:

    f_hat = (eps_in / (2 E_f)) * u_hat   on the band,   E_f = band energy.

The forcing is solenoidal and known exactly at every instant, which is what the
instantaneous material-vorticity budget requires. The module is importable
(the budget script reuses `Spectral`, `nonlinear_rhs`, `forcing` and `step`)
and runnable:

    python dns_forced_isotropic.py spinup --N 128 --nu 0.008 --T 15 \
        --snapshots 15,17,19,21,23 --out runs/n128

Everything is deterministic for a given seed.
"""

from __future__ import annotations

import argparse
import json
import os
import time

import numpy as np
import scipy.fft as sfft

WORKERS = int(os.environ.get("DNS_WORKERS", "2"))


class Spectral:
    """Wavenumbers, masks and FFT helpers for an N^3 periodic grid.

    `dtype` selects float64 (default; used for every budget evaluation) or
    float32 (optional for evolution; precision sensitivity must be checked
    for the observables and time interval being measured).
    """

    def __init__(self, N: int, dtype=np.float64):
        if not isinstance(N, (int, np.integer)) or N < 4 or N % 2:
            raise ValueError("N must be an even integer >= 4")
        if np.dtype(dtype) not in (np.dtype("float32"), np.dtype("float64")):
            raise ValueError("dtype must be float32 or float64")
        self.N = N
        self.rdtype = np.dtype(dtype)
        self.cdtype = np.result_type(self.rdtype, np.complex64)
        k = sfft.fftfreq(N, 1.0 / N).astype(self.rdtype)
        kz = sfft.rfftfreq(N, 1.0 / N).astype(self.rdtype)
        self.kx = k[:, None, None]
        self.ky = k[None, :, None]
        self.kz = kz[None, None, :]
        self.k = (self.kx, self.ky, self.kz)
        self.ik = tuple((1j * kk).astype(self.cdtype) for kk in self.k)
        self.k2 = self.kx**2 + self.ky**2 + self.kz**2
        self.k2inv = np.where(self.k2 > 0, 1.0 / np.where(self.k2 > 0, self.k2, 1.0), 0.0).astype(self.rdtype)
        self.kmax = N / 3.0
        self.mask = self.k2 < self.kmax**2
        w = np.full(kz.shape, 2.0)
        w[0] = 1.0
        if N % 2 == 0:
            w[-1] = 1.0
        self.w = w[None, None, :]
        self.norm = float(N) ** 6
        self._band = {}

    def fwd(self, f):
        return sfft.rfftn(f, axes=(-3, -2, -1), workers=WORKERS)

    def inv(self, F):
        n = self.N
        return sfft.irfftn(F, s=(n, n, n), axes=(-3, -2, -1), workers=WORKERS)

    def curl(self, U):
        ikx, iky, ikz = self.ik
        out = np.empty_like(U)
        np.subtract(iky * U[2], ikz * U[1], out=out[0])
        np.subtract(ikz * U[0], ikx * U[2], out=out[1])
        np.subtract(ikx * U[1], iky * U[0], out=out[2])
        return out

    def project(self, F, out=None):
        kx, ky, kz = self.k
        div = kx * F[0]
        div += ky * F[1]
        div += kz * F[2]
        div *= self.k2inv
        if out is None:
            out = np.empty_like(F)
        np.subtract(F[0], kx * div, out=out[0])
        np.subtract(F[1], ky * div, out=out[1])
        np.subtract(F[2], kz * div, out=out[2])
        return out

    def energy(self, U):
        return 0.5 * float(np.sum(self.w * np.sum(np.abs(U) ** 2, axis=0))) / self.norm

    def enstrophy(self, U):
        """<|omega|^2> for a solenoidal field."""
        return float(np.sum(self.w * self.k2 * np.sum(np.abs(U) ** 2, axis=0))) / self.norm

    def band(self, kf: float):
        """Index arrays and weights of the forcing band 0 < |k| <= kf."""
        if not np.isfinite(kf) or not 0 < kf < self.kmax:
            raise ValueError("forcing cutoff must lie in (0, N/3)")
        if kf not in self._band:
            m = (self.k2 > 0) & (self.k2 <= kf**2 + 1e-9)
            idx = np.nonzero(m)
            wb = np.broadcast_to(self.w, self.k2.shape)[idx]
            self._band[kf] = (m, idx, wb)
        return self._band[kf]


def band_mask(sp: Spectral, kf: float):
    return sp.band(kf)[0]


def band_energy(sp: Spectral, U, kf: float):
    _, idx, wb = sp.band(kf)
    Ub = U[(slice(None),) + idx]
    return 0.5 * float(np.sum(wb * np.sum(np.abs(Ub) ** 2, axis=0))) / sp.norm


def forcing_coefficient(Ef: float, eps_in: float):
    """Well-defined constant-power forcing; zero input permits an empty band."""
    if not np.isfinite(eps_in) or eps_in < 0:
        raise ValueError("forcing power must be finite and nonnegative")
    if eps_in == 0:
        return 0.0
    if not np.isfinite(Ef) or Ef <= 0:
        raise ValueError("positive forcing power requires positive finite band energy")
    return eps_in / (2.0 * Ef)


def forcing(sp: Spectral, U, eps_in: float, kf: float):
    """Constant-power band forcing; returns (F_hat, coefficient c, band energy)."""
    m, idx, _ = sp.band(kf)
    Ef = band_energy(sp, U, kf)
    c = forcing_coefficient(Ef, eps_in)
    F = np.zeros_like(U)
    sel = (slice(None),) + idx
    F[sel] = c * U[sel]
    return F, c, Ef


def nonlinear_rhs(sp: Spectral, U, eps_in: float, kf: float):
    """Explicit tendency (advection + pressure + forcing), viscous term excluded."""
    u = sp.inv(U)
    om = sp.inv(sp.curl(U))
    n = np.empty_like(u)
    np.subtract(u[1] * om[2], u[2] * om[1], out=n[0])
    np.subtract(u[2] * om[0], u[0] * om[2], out=n[1])
    np.subtract(u[0] * om[1], u[1] * om[0], out=n[2])
    Nh = sp.fwd(n)
    Nh *= sp.mask
    R = sp.project(Nh, out=Nh)
    _, idx, _ = sp.band(kf)
    sel = (slice(None),) + idx
    c = forcing_coefficient(band_energy(sp, U, kf), eps_in)
    R[sel] += c * U[sel]
    return R, u


def full_tendency(sp: Spectral, U, nu: float, eps_in: float, kf: float):
    """Galerkin d/dt u_hat including viscosity."""
    R, _ = nonlinear_rhs(sp, U, eps_in, kf)
    return R - nu * sp.k2 * U


def step(sp: Spectral, U, dt: float, nu: float, eps_in: float, kf: float):
    """One integrating-factor RK4 step. Returns (U_new, max|u| at the start)."""
    E = np.exp(-nu * sp.k2 * dt / 2.0)
    E2 = E * E
    k1, u = nonlinear_rhs(sp, U, eps_in, kf)
    umax = float(np.max(np.abs(u)))
    k2, _ = nonlinear_rhs(sp, E * (U + 0.5 * dt * k1), eps_in, kf)
    k3, _ = nonlinear_rhs(sp, E * U + 0.5 * dt * k2, eps_in, kf)
    k4, _ = nonlinear_rhs(sp, E2 * U + dt * E * k3, eps_in, kf)
    Un = E2 * U + (dt / 6.0) * (E2 * k1 + 2.0 * E * (k2 + k3) + k4)
    return Un * sp.mask, umax


def initial_field(sp: Spectral, E0: float = 0.5, k0: float = 2.5, seed: int = 20261004):
    rng = np.random.default_rng(seed)
    noise = rng.standard_normal((3, sp.N, sp.N, sp.N))
    U = sp.fwd(noise)
    kk = np.sqrt(sp.k2)
    spec = kk**4 * np.exp(-2.0 * (kk / k0) ** 2)
    amp = np.sqrt(np.where(kk > 0, spec / np.maximum(kk, 1e-12) ** 2, 0.0))
    U = sp.project(U * amp) * sp.mask
    U *= np.sqrt(E0 / sp.energy(U))
    return U


def diagnostics(sp: Spectral, U, nu: float):
    E = sp.energy(U)
    Z = sp.enstrophy(U)
    eps = nu * Z
    up2 = 2.0 * E / 3.0
    eta = (nu**3 / eps) ** 0.25
    re_lambda = up2 * np.sqrt(15.0 / (nu * eps))
    kk = np.sqrt(sp.k2)
    # integral scale L = (pi / (2 u'^2)) * int E(k)/k dk
    Ek_over_k = np.sum(sp.w * np.sum(np.abs(U) ** 2, axis=0) * np.where(kk > 0, 1.0 / np.maximum(kk, 1e-12), 0.0)) / sp.norm * 0.5
    L = np.pi / (2.0 * up2) * Ek_over_k
    return {
        "E": E, "eps": eps, "urms": float(np.sqrt(up2)), "eta": float(eta),
        "kmax_eta": float(sp.kmax * eta), "Re_lambda": float(re_lambda),
        "L": float(L), "tau_eta": float(np.sqrt(nu / eps)),
    }


def cfl_dt(umax: float, N: int, cfl: float):
    dx = 2.0 * np.pi / N
    return cfl * dx / max(umax, 1e-12)


def save_state(path: str, U, t: float, meta: dict):
    np.savez(path, U=U, t=t, meta=json.dumps(meta))


def load_state(path: str):
    d = np.load(path)
    return d["U"], float(d["t"]), json.loads(str(d["meta"]))


def refine(U, N_from: int, N_to: int):
    """Exact spectral interpolation of a band-limited field to a finer grid."""
    if N_from < 4 or N_from % 2 or N_to < N_from:
        raise ValueError("refinement requires even N_from >= 4 and N_to >= N_from")
    if U.shape != (3, N_from, N_from, N_from // 2 + 1):
        raise ValueError("state shape does not match N_from")
    sp_to = Spectral(N_to)
    V = np.zeros((3, N_to, N_to, N_to // 2 + 1), dtype=complex)
    h = N_from // 2
    nz = N_from // 2 + 1
    scale = (N_to / N_from) ** 3
    V[:, :h, :h, :nz] = U[:, :h, :h, :nz]
    V[:, -h:, :h, :nz] = U[:, -h:, :h, :nz]
    V[:, :h, -h:, :nz] = U[:, :h, -h:, :nz]
    V[:, -h:, -h:, :nz] = U[:, -h:, -h:, :nz]
    # Nyquist planes of the coarse grid are zero after dealiasing, so no halving is needed.
    return V * scale * sp_to.mask


def run(sp, U, t, t_end, nu, eps_in, kf, cfl, snapshots, out, meta, log_every=50, dt_max=None):
    os.makedirs(out, exist_ok=True)
    snapshots = sorted(s for s in snapshots if s > t - 1e-12)
    logf = open(os.path.join(out, "log.jsonl"), "a")
    _, u0 = nonlinear_rhs(sp, U, eps_in, kf)
    dt = cfl_dt(float(np.max(np.abs(u0))), sp.N, cfl)
    if dt_max:
        dt = min(dt, dt_max)
    nstep = 0
    t0 = time.time()
    while t < t_end - 1e-12:
        target = min([s for s in snapshots if s > t + 1e-12] + [t_end])
        h = min(dt, target - t)
        U, umax = step(sp, U, h, nu, eps_in, kf)
        t += h
        nstep += 1
        dt = cfl_dt(umax, sp.N, cfl)
        if dt_max:
            dt = min(dt, dt_max)
        if nstep % log_every == 0:
            d = diagnostics(sp, U, nu)
            d.update(t=t, dt=dt, umax=umax, wall=time.time() - t0)
            logf.write(json.dumps(d) + "\n")
            logf.flush()
        if any(abs(t - s) < 1e-9 for s in snapshots):
            d = diagnostics(sp, U, nu)
            save_state(os.path.join(out, f"state_t{t:07.3f}.npz"), U, t, {**meta, **d})
            logf.write(json.dumps({"snapshot": t, **d}) + "\n")
            logf.flush()
    save_state(os.path.join(out, "state_final.npz"), U, t, {**meta, **diagnostics(sp, U, nu)})
    logf.close()
    return U, t


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("spinup")
    s.add_argument("--N", type=int, default=128)
    s.add_argument("--nu", type=float, default=0.008)
    s.add_argument("--eps", type=float, default=0.1)
    s.add_argument("--kf", type=float, default=2.0)
    s.add_argument("--cfl", type=float, default=0.4)
    s.add_argument("--T", type=float, default=15.0)
    s.add_argument("--snapshots", type=str, default="")
    s.add_argument("--seed", type=int, default=20261004)
    s.add_argument("--resume", type=str, default="",
                   help="state file to continue from; refined spectrally if its N is smaller")
    s.add_argument("--dtype", choices=["float64", "float32"], default="float64")
    s.add_argument("--out", type=str, required=True)
    a = ap.parse_args()

    sp = Spectral(a.N, dtype=np.dtype(a.dtype))
    meta = {"N": a.N, "nu": a.nu, "eps_in": a.eps, "kf": a.kf, "seed": a.seed, "dtype": a.dtype}
    if a.resume:
        U, t, m0 = load_state(a.resume)
        U = U.astype(np.complex128)
        if m0["N"] != a.N:
            U = refine(U, m0["N"], a.N)
        meta["resumed_from"] = os.path.basename(a.resume)
    else:
        U, t = initial_field(Spectral(a.N), seed=a.seed), 0.0
    U = U.astype(sp.cdtype)
    snaps = [float(x) for x in a.snapshots.split(",") if x.strip()]
    run(sp, U, t, a.T, a.nu, a.eps, a.kf, a.cfl, snaps, a.out, meta)


if __name__ == "__main__":
    main()
