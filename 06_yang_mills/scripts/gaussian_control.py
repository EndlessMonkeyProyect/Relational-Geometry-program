"""Gaussian block control in four dimensions.

Evaluates exact finite-matrix identities in floating point for a selected
gauge-invariant linear field-strength observable. The massless covariance is
interpreted on the quotient by the kernel (Moore-Penrose inverse). R=Var/D is a
test-function lower bound on an optimal variance constant; numerical saturation
of R alone does not bound that optimal constant from above.

Adapted from the supplied control_gaussiano_U1_bloques.py. See ../GAUSSIAN_CONTROL.md.
"""
import itertools
import argparse
import json
import time

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

D_DIM = 4


def build_d(L, d=D_DIM):
    """Matriz dispersa del operador d: R^{enlaces} -> R^{plaquetas} en el toro."""
    N = L ** d
    coords = np.array(np.unravel_index(np.arange(N), (L,) * d)).T  # N x d
    pairs = [(m, n) for m in range(d) for n in range(m + 1, d)]

    def vid(c):
        return np.ravel_multi_index(tuple((c % L).T), (L,) * d)

    rows, cols, vals = [], [], []
    x = np.arange(N)
    for pi, (m, n) in enumerate(pairs):
        em = np.zeros(d, int); em[m] = 1
        en = np.zeros(d, int); en[n] = 1
        xm, xn = vid(coords + em), vid(coords + en)
        prow = x * len(pairs) + pi
        # (dA)_p = A_m(x) + A_n(x+e_m) - A_m(x+e_n) - A_n(x)
        for link, s in [(x * d + m, 1.0), (xm * d + n, 1.0),
                        (xn * d + m, -1.0), (x * d + n, -1.0)]:
            rows.append(prow); cols.append(link); vals.append(np.full(N, s))
    Dop = sp.csr_matrix((np.concatenate(vals),
                         (np.concatenate(rows), np.concatenate(cols))),
                        shape=(N * len(pairs), N * d))
    return Dop, coords, pairs, vid


def block_links(origin, l, L, vid, d=D_DIM):
    """Enlaces (y, mu) con y y y+e_mu dentro del cubo origin + {0..l-1}^d."""
    links = []
    for off in itertools.product(range(l), repeat=d):
        y = np.array(origin) + np.array(off)
        for mu in range(d):
            if off[mu] <= l - 2:
                links.append(int(vid(y[None, :])[0]) * d + mu)
    return np.array(links)


def run(L, l, m2=0.0):
    if not isinstance(L, int) or not isinstance(l, int):
        raise ValueError("L and block side must be integers")
    if l < 2 or l % 2 or L <= l or L % (l // 2):
        raise ValueError("Require even block side >= 2, L > side, and side/2 dividing L")
    if not np.isfinite(m2) or m2 < 0:
        raise ValueError("Squared mass must be finite and nonnegative")
    Dop, coords, pairs, vid = build_d(L)
    nlinks = Dop.shape[1]
    M = (Dop.T @ Dop).tocsr()
    if m2 > 0:
        M = (M + m2 * sp.identity(nlinks, format="csr")).tocsr()

    # funcion de prueba
    phi = np.zeros(Dop.shape[0])
    p01 = pairs.index((0, 1))
    x = np.arange(L ** D_DIM)
    phi[x * len(pairs) + p01] = np.cos(2 * np.pi * coords[:, 0] / L)
    c = Dop.T @ phi

    # Var(f) = c^T M^+ c   (c esta en la imagen de M)
    sol, info = spla.cg(M, c, rtol=1e-12, maxiter=20000)
    assert info == 0, "CG no convergio"
    var = float(c @ sol)

    # bloques: origenes en (l/2) Z^4
    step = l // 2
    origins = list(itertools.product(range(0, L, step), repeat=D_DIM))
    B0 = block_links(origins[0], l, L, vid)
    G = M[B0][:, B0].toarray()
    # verificacion de invariancia por traslacion de Q_BB
    B1 = block_links(origins[len(origins) // 2], l, L, vid)
    G1 = M[B1][:, B1].toarray()
    assert np.allclose(G, G1), "Q_BB no es invariante por traslacion"
    # pseudo-inversa (para l >= 4 hay modos gauge locales en el nucleo)
    w, V = np.linalg.eigh(G)
    keep = w > 1e-9 * w.max()
    Gp = (V[:, keep] / w[keep]) @ V[:, keep].T
    ker_dim = int((~keep).sum())

    Cmat = np.stack([c[block_links(o, l, L, vid)] for o in origins], axis=1)
    # chequeo: c_B ortogonal al nucleo de Q_BB (gauge-invariancia)
    if ker_dim:
        assert np.abs(V[:, ~keep].T @ Cmat).max() < 1e-8 * max(1, np.abs(Cmat).max())
    Dform = float(np.einsum("ib,ib->", Cmat, Gp @ Cmat))
    return var, Dform, ker_dim, len(B0), len(origins)



def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--quick", action="store_true", help="L=4,6 and block side 2 (default)")
    modes.add_argument("--full", action="store_true", help="Original larger finite-volume sweep")
    parser.add_argument("--json", action="store_true", help="Machine-readable results")
    args = parser.parse_args(argv)
    cases = [(2, [4, 6])]
    if args.full:
        cases = [(2, [4, 6, 8, 10, 12, 16, 20]), (4, [8, 12, 16, 20])]
    rows = []
    for side, sizes in cases:
        for size in sizes:
            for m2 in (0.0, 0.5, 0.1):
                started = time.perf_counter()
                variance, form, kernel, links, blocks = run(size, side, m2)
                rows.append({
                    "L": size, "block_side": side, "mass_squared": m2,
                    "variance": variance, "block_form": form,
                    "ratio": variance / form, "ratio_over_L2": variance / form / size**2,
                    "local_kernel_dimension": kernel, "links_per_block": links,
                    "block_count": blocks,
                    "seconds": round(time.perf_counter() - started, 4),
                })
    report = {
        "model": "4D linear Gaussian field; one field-strength test function",
        "precision": "floating point; CG rtol=1e-12; local eigenvalue cutoff=1e-9",
        "mode": "full" if args.full else "quick",
        "results": rows,
    }
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print("L  side  mass^2       Var/D     (Var/D)/L^2")
        for row in rows:
            print(f"{row['L']:2d} {row['block_side']:5d} {row['mass_squared']:7.2f} "
                  f"{row['ratio']:11.7f} {row['ratio_over_L2']:15.8f}")
        print("Scope: selected test-function ratios in finite Gaussian models.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
