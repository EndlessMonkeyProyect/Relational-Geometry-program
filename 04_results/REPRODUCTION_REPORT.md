# Reproduction report

Checks executed on 3 October 2026 for the local review edition. The results below identify what a reviewer can reproduce and which protocol was used.

| Check | Result | Scope |
|---|---|---|
| Automated suite | 31 tests and 920 subtests passed | Exact finite controls, numerical algebraic consistency, repository structure and public-package behavior |
| Novelty criterion | 1 296 pairs of finite signatures and comparisons checked | Refinement agrees with failure of factorization in the enumerated domain |
| Phase realization | 65 536 graphs enumerated; counts 6 561 / 2 401 / 1 753 reproduced | Outgoing phase lift / layerwise bijections / choices with exact four-step return |
| Capsule composition | Exhaustive two-variable relations and seeded multi-factor checks passed | Join and valid existential projection agree with full assignment enumeration |
| $SU(2)$ observable | Matrix, angular and trace expressions agree in seeded numerical controls | Includes common-conjugation invariance, central signs and Q8 examples |
| Restricted Euler quick benchmark | 12/12 trajectories reached the numerical event; median $\rho_\perp=2.849309\times10^{-23}$ | Default 12-trajectory model protocol |
| Euler identity checkpoints | Numeric and predicted values agree to six printed decimals | At $t/T=0.7$: $-12.851267$; at $0.9$: $-3.023353$ |
| JHTDB derived-table checks | Script completed and reported endpoint/integral and differentiation sensitivities | Recalculation of bundled tables; original extraction was not rerun |
| Gaussian quick control | Six finite cases completed | $L=4,6$, block side 2, squared masses 0, 0.5, 0.1 |

The Gaussian protocol and numerical values are recorded in [GAUSSIAN_CONTROL.md](../06_yang_mills/GAUSSIAN_CONTROL.md). The fluid-data scope is described in the [data guide](../03_navier_stokes/data/README.md).

## Commands

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python 03_navier_stokes/scripts/restricted_euler_benchmark.py
python 03_navier_stokes/scripts/review_checks.py
python 06_yang_mills/scripts/gaussian_control.py --quick --json
python tools/public_release.py
```

The automated suite and these computations support the stated finite and numerical checks. General proofs are supplied in the mathematical notes; physical interpretation and independent specialist review have their own evidence requirements. The extended 200-trajectory Euler protocol and the large Gaussian sweep are available for subsequent reproduction.
