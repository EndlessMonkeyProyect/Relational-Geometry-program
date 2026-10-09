# Reproduction report — 3.0.0-review

The complete automated suite was executed locally on 9 October 2026: **134 tests and 953 subtests passed**. The offline document audit found no integrity errors in 135 selected files, including 74 Markdown documents. These checks distinguish reproducible controls from supplied production data and independent specialist review.

## Executed for version 3.0

The suite covers the existing formal and laboratory controls and adds explicit tests of contextual reclosure, finite comparison contracts, relative uniform control, resolution weights, spin composition, SAT representation costs and conditional physical correspondences.

The four new LV2-related test modules contain 31 test methods: eight for resolution and modal weights, nine for spin composition, nine for SAT representations, and five for the algebra and numerical values used in the physical correspondence notes. These are finite controls under declared assumptions, not independent empirical confirmation of the physical hypotheses.

The suite ran on Windows with NumPy 2.5.3, SciPy 1.18.1 and pytest 9.1.1. The public-package checks validate the selected files and local links. Production DNS, large Monte Carlo runs and new chemistry experiments were not rerun for this edition.

## Earlier executed controls — 5 October 2026

The following records retain the earlier reproduction results. The standalone quick scripts listed here were run on that date; their historical numerical outputs are not presented as new version-3 production runs.

| Check | Result | Scope |
|---|---|---|
| Automated suite | 47 tests and 927 subtests passed | Exact finite controls, numerical consistency, repository structure and public-package behavior |
| Novelty criterion | 1 296 pairs of finite signatures and comparisons checked | Refinement agrees with failure of factorization in the enumerated domain |
| Phase realization | 65 536 graphs enumerated; counts 6 561 / 2 401 / 1 753 reproduced | Outgoing phase lift / layerwise bijections / choices with exact four-step return |
| Capsule composition | Exhaustive two-variable relations and seeded multi-factor checks passed | Join and valid existential projection agree with full assignment enumeration |
| Action and harmonic structure | Five new test methods passed | Canonical coordinates, invariant and phase, circular versus polygonal area, finite signature content and factor classification through index 32 |
| Comparators and incorporation | Six new test methods passed | Weighted incidence, shift invariance, compatible cycles, weighted novelty projection, coupling and two-layer causal propagation |
| Instantaneous-budget controls | Five test methods passed | Small-flow closure, refinement, forcing/input validation, undefined direction at zero vorticity, and a short single-versus-double-precision evolution |
| $SU(2)$ observable | Matrix, angular and trace expressions agree in seeded controls | Common-conjugation invariance, central signs and Q8 examples |
| Restricted Euler quick benchmark | 12/12 trajectories reached the numerical event; median $\rho_\perp=2.849309\times10^{-23}$ | Default 12-trajectory model protocol |
| Euler identity checkpoints | Numeric and predicted values agree to six printed decimals | At $t/T=0.7$: $-12.851267$; at $0.9$: $-3.023353$ |
| JHTDB derived-table checks | Completed; reported differentiation sensitivity and endpoint/integral differences | Recalculation of bundled tables; original extraction was not rerun |
| Gaussian quick control | Six finite cases completed | $L=4,6$, block side 2, squared masses 0, 0.5, 0.1 |

The numerical environment used NumPy 2.5.3 and SciPy 1.18.1 on Windows. The test suite and quick scripts are deterministic for their declared seeds. The Gaussian values and method are documented in [GAUSSIAN_CONTROL.md](../06_yang_mills/GAUSSIAN_CONTROL.md).

The tests are controls on the stated constructions, not a replacement for their proofs. The small precision test does not certify the full production simulations.

## Supplied production data

The author supplied thirteen budget CSV tables with the Navier–Stokes patch dated 4 October. Their values are retained unchanged. They cover moderate-Reynolds-number runs A ($N=128$, $Re_\lambda\approx48$–$53$), A refined to $N=192$, and B ($N=128$, $Re_\lambda\approx38$).

In those tables, median first-order closure residuals at the most intense points are approximately 12 %, 1.6 % and 0.8 % at $k_{\max}\eta\approx2$, 2.9 and 3.0. These are reported observations for those flows, not a universal resolution threshold.

**The complete production simulations were not rerun for this integration.** Their protocol, mixed-precision provenance, statistical conditioning and resolution limitations are in the [budget note](../03_navier_stokes/docs/instantaneous_budget.md). The source estimates about two hours on two CPU cores; that runtime was not independently measured here. Full production reproduction and convergence studies are explicit next review tasks.

## Commands

~~~bash
python -m pip install -r requirements.txt
python -m pytest -q
python 03_navier_stokes/scripts/restricted_euler_benchmark.py
python 03_navier_stokes/scripts/review_checks.py
python 06_yang_mills/scripts/gaussian_control.py --quick --json
python tools/public_release.py
~~~

To regenerate the public manifest and ZIP after editing:

~~~bash
python tools/public_release.py --write-manifest --build
~~~

The public builder checks local Markdown destinations and hashes the selected files. Raw DNS snapshots, runtime products and internal working materials are excluded. The extended Euler protocol, large Gaussian sweep and production DNS remain available for independent reproduction.
