# Instantaneous material-vorticity budget in spectral DNS

This note develops research targets 1, 2 and 4 of the [manuscript](../manuscript.md): a separately computed vorticity budget, a signed transverse decomposition and a resolution audit. The supplied CSV tables report the author's computation of 4 October 2026. The 5 October integration reruns small automated controls, not the full production simulations; the commands below specify that longer reproduction.

**Status:** [Computational observation — forced isotropic DNS at $Re_\lambda\approx38$–$53$]. The decomposition in §2 is [Exact]; everything measured is conditional on these flows, this forcing and these resolutions.

## 1. Data

The supplied experiment uses a purpose-built pseudo-spectral DNS ([solver](../scripts/dns_forced_isotropic.py)): periodic box $[0,2\pi)^3$, spherical 2/3 dealiasing, integrating-factor RK4, and constant-power solenoidal forcing on $0<|k|\le2$ with input power 0.1. The forcing is explicitly available to the budget. These are new model fields, separate from the bundled JHTDB data; matching a forcing band does not make the datasets equivalent.

| Run | $N$ | $\nu$ | $Re_\lambda$ | $k_{\max}\eta$ | Snapshots |
|---|---:|---:|---:|---:|---|
| A | 128 | 0.008 | 48–53 | 1.96–2.07 | $t=15,\dots,19$ (5, about one large-eddy time apart) |
| A$_{192}$ | 192 | 0.008 | 48–54 | 2.94–3.14 | A at $t=15,17,19$, spectrally refined and evolved $0.6\approx2.2\,\tau_\eta$ |
| B | 128 | 0.0135 | 38–39 | 2.99–3.03 | $t=14,\dots,17$ (4) |

$k_{\max}=N/3$. Run A$_{192}$ is the same flow as A with the newly resolved scales allowed to develop; it is the reference for A. Detailed run diagnostics are in the `budget_*_snapshots.csv` tables.

## 2. Exact decomposition of the transverse law

With $\mathcal N=D_t\omega=S\omega+\nu\Delta\omega+\nabla\times f$, $\mathcal V=\mathcal N/q$ and $\mathcal Y=D_t\mathcal V$, differentiating the velocity-gradient equation $D_tA=-A^2-H+\nu\Delta A+\nabla f$ ($H=\nabla\nabla p$) gives

$$
D_t(S\omega)=-H\omega+\nu(\Delta S\,\omega+S\Delta\omega)+(\nabla f)_s\,\omega+S\,\nabla\times f ,
$$

because the $S^2\omega$ terms cancel: the rotation tensor annihilates $\omega$. Hence $D_t\mathcal N=\Pi+\mathcal{V}_{\rm is}+\mathcal F_{\rm rc}$ with

$$
\Pi=-H\omega,\qquad
\mathcal V_{\rm is}=\nu\left(\Delta S\,\omega+S\Delta\omega+D_t\Delta\omega\right),\qquad
\mathcal F_{\rm rc}=(\nabla f)_s\,\omega+S\,\nabla\times f+D_t(\nabla\times f),
$$

and, since $\mathcal Y=D_t\mathcal N/q-a\mathcal V$, on $a>0$

$$
\boxed{
P_\xi^\perp\frac{db}{dG}=\mathcal P+\mathcal V_c+\mathcal F-2b,
\qquad
\mathcal P=-\frac{P_\xi^\perp H\xi}{a},\quad
\mathcal V_c=\frac{P_\xi^\perp\mathcal V_{\rm is}}{aq},\quad
\mathcal F=\frac{P_\xi^\perp\mathcal F_{\rm rc}}{aq}.
}
$$

For $\nu=0$, $f=0$ this reduces to the Euler form of the manuscript (§6). Only the deviatoric part of $H$ survives the projection, so the pressure term is entirely nonlocal; restricted Euler sets it to zero. Projecting on $\hat b$ gives signed rates per e-fold of vorticity growth,

$$
\frac{d\log|b|}{dG}=s_P+s_V+s_F-2,\qquad s_X=\frac{\hat b\cdot X}{|b|}.
$$

The first-order budget uses the same fields: $b=\tau+r_{\nu\perp}+r_{f\perp}$ with $\tau=P_\xi^\perp S\xi$, $r_{\nu\perp}=\nu P_\xi^\perp\Delta\omega/q$ and $r_{f\perp}=P_\xi^\perp\nabla\times f/q$, each computed from spatial derivatives. Unlike the JHTDB reconstruction, $r_\perp$ is not formed as $b-\tau$.

## 3. Closure against the evolving flow

The instantaneous $\mathcal N$ and $\mathcal Y$ are compared with evolution: five DNS states $\delta=2\times10^{-3}$ apart give fourth-order time differences, and $D_t=\partial_t+u\cdot\nabla$ is completed spectrally. The difference tests combined numerical consistency; attribution to spatial truncation requires separate time-step and precision controls. Below, $\mathcal N_G$ denotes the DNS material derivative (Galerkin tendency plus advection) and $e_\perp=P_\xi^\perp(\mathcal N_G-\mathcal N)/q$ its transverse spatial-truncation contribution.

Median relative residual at the most intense vorticity points:

| Flow / points | $k_{\max}\eta$ | $\lvert D_t\omega-\mathcal N\rvert/\lvert\mathcal N\rvert$ | $\lvert P^\perp(\mathcal Y_{\rm fd}-\mathcal Y)\rvert/\lvert\mathcal Y_\perp\rvert$ |
|---|---:|---:|---:|
| A, top 4000 | 1.96 | 0.121 (p90 0.41) | 0.113 |
| A$_{192}$, top 4000 | 2.94 | 0.016 (p90 0.062) | 0.018 |
| B, top 4000 | 3.0 | 0.008 (p90 0.024) | 0.008 |
| Small test flow, $N=24\to48$ | 2.51 → 5.01 | $3.6\times10^{-2}\to2.4\times10^{-5}$ | $2.9\times10^{-2}\to3.6\times10^{-5}$ |

The small-flow residual decreases strongly under refinement. This supports implementation consistency for that test; the derivation in §2 establishes the analytic identity. The automated test does not exclude every possible implementation error.

On the supplied small-flow refinement study (top 0.3 % of $q$), $|\mathcal N_G-\mathcal N|/|\mathcal N|$ was 0.22, 0.060 and 0.0025 at $k_{\max}\eta=2.05,2.74,4.10$. In the production tables, moving from approximately 2 to 3 is associated with median first-order residuals falling from 12 % to 0.8–1.6 %. These are flow- and observable-specific observations, not a universal resolution threshold. The JHTDB states retain their separately documented method sensitivity; these DNS do not calibrate JHTDB errors.

## 4. Results

### 4.1 Low turning becomes rarer at high vorticity

Volume-weighted probability of the low-turning channel among positive-growth points (all grid points of every snapshot; refined run: complete set above $2q_{\rm rms}$ plus a 2 % uniform sample below):

| $q/q_{\rm rms}$ | A: $P(\rho_\perp<0.05)$ | A$_{192}$ | B | median $\rho_\perp$ (B) |
|---|---:|---:|---:|---:|
| 0–1 | 0.038 | 0.040 | 0.039 | 0.69 |
| 1–2 | 0.029 | 0.031 | 0.033 | 0.72 |
| 2–3 | 0.019 | 0.024 | 0.028 | 0.75 |
| 3–4 | 0.017 | 0.016 | 0.014 | 0.83 |
| 4–5 | 0.013 | 0.009 | 0.013 | 0.75 |

In these flows intense vorticity is typically turning-dominated ($|b|\approx2a$), and the channel $\rho_\perp<0.05$ occupies about 1–2 % of the strongest positive-growth points. These Eulerian statistics are conditional on $a>0$ and the stated vorticity bin, without preselecting the sample for low turning. Grid points and successive snapshots are correlated; the counts are not numbers of independent trials.

### 4.2 First order: low turning is compensation, not scarcity

For high-vorticity states ($q>3q_{\rm rms}$, $a>0$), comparing the low-turning subset with the rest:

| | A$_{192}$ low | A$_{192}$ rest | B low | B rest |
|---|---:|---:|---:|---:|
| states | 803 | 50 291 | 151 | 10 568 |
| median $\Lambda_\perp=(T+M)/a$ | 0.50 | 2.9 | 0.64 | 2.9 |
| fraction with $\Lambda_\perp<0.229$ (scarcity suffices) | 0.15 | 0.00 | 0.05 | 0.00 |
| median $\mathcal D_\perp=\lvert b\rvert/(T+M)$ | 0.30 | 0.78 | 0.24 | 0.83 |
| fraction with $\mathcal D_\perp<0.5$ | 0.75 | 0.15 | 0.87 | 0.12 |
| median $\cos\varphi(\tau,r_\perp)$ | −0.95 | −0.35 | −0.96 | −0.37 |
| median $\lvert r_{\nu\perp}\rvert/\lvert\tau\rvert$ | 0.82 | 0.30 | 0.79 | 0.20 |
| median $\lvert r_{f\perp}\rvert/\lvert r_{\nu\perp}\rvert$ | 0.04 | 0.04 | 0.06 | 0.10 |
| truncation $\lvert e_\perp\rvert/\lvert b\rvert$ (median) | 0.11 | 0.014 | 0.12 | 0.008 |
| still $\rho_\perp<0.05$ with the DNS's own turning | 0.91 | — | 0.97 | — |

In the low-turning states, strain-induced turning $\tau$ is still large compared with the growth rate ($\Lambda_\perp$ is not small), and the viscous transverse term points almost exactly against it with comparable magnitude. The forcing contributes a few percent. This answers the question left open in the manuscript (§3): with $r_\perp$ computed independently and the budget closed, small turning at high vorticity in these flows is predominantly a **physical strain–viscous compensation**.

The resolution matters here. In run A ($k_{\max}\eta\approx2$) the truncation term is comparable to $|b|$ in the low-turning set (median 0.92) and only half of those states remain low-turning when the DNS's own material derivative is used; the classification of individual states is unreliable at that resolution, although the class medians agree with B and A$_{192}$.

### 4.3 Second order: pressure sustains turning, viscosity removes it

Signed contributions to $d\log|b|/dG$ for all high-vorticity growth states ($q>3q_{\rm rms}$):

| | A$_{192}$ | B | A |
|---|---:|---:|---:|
| states | 51 094 | 10 719 | 23 653 |
| $s_P$ median (fraction $>0$) | 9.1 (0.86) | 8.9 (0.87) | 9.7 (0.86) |
| $s_V$ median (fraction $>0$) | −7.9 (0.11) | −8.3 (0.09) | −8.8 (0.13) |
| $s_F$ median | 0.03 | 0.12 | 0.02 |
| $d\log\lvert b\rvert/dG$ median (fraction $>0$) | −0.7 (0.46) | −1.0 (0.43) | −0.5 (0.47) |

The projected deviatoric pressure Hessian reaccredits transverse change in most intense states, and viscosity removes it; each is about four to five times the kinematic relaxation $-2$, and their near cancellation leaves a net rate of order one per e-fold, with broad spread. The forcing is negligible at these scales. In the low-turning subset the same signs hold with weaker majorities (A$_{192}$: $s_P>0$ in 64 %, $s_V<0$ in 57 %; B: 68 % and 68 %). The net rate inside that subset has opposite median signs in A$_{192}$ (+2.8) and B (−0.5), so these instantaneous data say nothing reliable about entry into or exit from the channel; that needs Lagrangian episodes.

### 4.4 Resolution audit

A snapshot of run A was evolved $0.6$ time units at $N=128$ and, after spectral refinement, at $N=192$; quantities were compared on the $64^3$ common grid points (720 points with $q>3q_{\rm rms}$, $a>0$ at both resolutions).

| Quantity | median pointwise relative difference | 90th percentile |
|---|---:|---:|
| $\omega$ | 0.006 | 0.013 |
| $\tau$ | 0.026 | 0.084 |
| $b$ | 0.094 | 0.34 |
| $r_{\nu\perp}$ | 0.27 | 1.06 |
| $\mathcal P$ | 0.14 | 0.66 |
| $\mathcal V_c$ | 0.43 | 1.48 |
| $\mathcal Y$ | 0.26 | 0.87 |

Class medians of $\rho_\perp$, $\Lambda_\perp$, $\mathcal D_\perp$, $s_P$ and $s_V$ agree within 4 % between the two resolutions, and the signs of $s_P$, $s_V$, $s_F$ agree at 97 %, 92 % and 96 % of the points. At $k_{\max}\eta\approx2$ the statistical conclusions survive; pointwise viscous and second-order terms do not.

## 5. Scope

- Two moderate Reynolds numbers, one forcing scheme and single-time Eulerian statistics. Extend Reynolds number with an observable-specific convergence study, time-step checks and precision controls.
- The classes are instantaneous states, not Lagrangian episodes; the duration of low-turning intervals and the unconditional episode distributions (§11, target 3) remain open.
- "Viscous" groups every term with an explicit $\nu$, including $\nu D_t\Delta\omega$; the split is exact but not unique, and other groupings answer other questions.
- Nothing here bears on global regularity. The measurements describe which terms sustain or remove turning in resolved turbulence at these parameters.

## 6. Reproduction

Python 3.11+, NumPy and SciPy. Snapshots are not bundled (about 50 MB each). The seed and protocol are fixed; floating-point results may depend on numerical-library versions and hardware. The source reports about two hours on two CPU cores for the full protocol; runtime was not remeasured in this integration. Shell examples below use Bash brace expansion.

```bash
cd 03_navier_stokes/scripts
# run A
python dns_forced_isotropic.py spinup --N 64  --nu 0.008 --T 10 --out runs/n64
python dns_forced_isotropic.py spinup --N 128 --nu 0.008 --T 19 --dtype float32 \
    --resume runs/n64/state_final.npz --snapshots 15,16,17,18,19 --out runs/n128
# run B
python dns_forced_isotropic.py spinup --N 64  --nu 0.0135 --T 10 --out runs/n64_lowre
python dns_forced_isotropic.py spinup --N 128 --nu 0.0135 --T 17 --dtype float32 \
    --resume runs/n64_lowre/state_final.npz --snapshots 14,15,16,17 --out runs/n128_lowre
# statistics, audit, refinement, closure
python instantaneous_budget.py stats runs/n128/state_t01{5,6,7,8,9}.000.npz --outdir ../data --tag n128
python instantaneous_budget.py stats runs/n128_lowre/state_t01{4,5,6,7}.000.npz --outdir ../data --tag lowre128
python instantaneous_budget.py audit runs/n128/state_t015.000.npz --outdir ../data --save-dir refined
python instantaneous_budget.py refine runs/n128/state_t017.000.npz runs/n128/state_t019.000.npz --dtype float32 --outdir refined
python instantaneous_budget.py stats refined/audit192_state_t015.000.npz \
    refined/refined192_state_t017.000.npz refined/refined192_state_t019.000.npz \
    --outdir ../data --tag n192 --mode high
python instantaneous_budget.py closure runs/n128_lowre/state_t016.000.npz --outdir ../data --tag lowre128
```

### Precision and scope of reproduction

| Stage of the supplied protocol | Precision |
|---|---|
| Initial N=64 spin-up | float64 |
| N=128 A/B evolution, including sampled states | float32 |
| N=192 audit from t=15, evolved by the audit command | float64, starting from the stored N=128 state |
| N=192 refinements from t=17,19 | float32 (explicit above) |
| Budget evaluation and short closure evolutions | float64 |
| Aggregated statistic arrays in stats_from_states | float32 before weighted summaries |

Conversion to float64 does not recover precision lost during earlier evolution or aggregation. A small paired-precision test is included; it does not certify precision independence of the long production runs. Reproduce those runs with float64 evolution and compare observables before making that stronger claim.

Zero-vorticity points have undefined direction and are marked NaN in directional diagnostics; signed rates additionally require positive growth and nonzero turning. Raw tables remain unchanged from the supplied experiment.

Tables are written to [data](../data/README.md). Keep regenerated runs and refined snapshots outside the public package; the release builder excludes them.
