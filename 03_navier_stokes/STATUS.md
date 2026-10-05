# Navier–Stokes branch status

The established contribution is the exact separation of material amplification and turning, together with its evolution in growth coordinates. The table connects each result to the evidence available for review.

| Item | Status | Evidence / scope |
|---|---|---|
| $D_t\omega/q=a\xi+b$, $b\perp\xi$ | **[Exact]** | material differentiation for $q>0$ |
| $\rho_\perp=\lvert b\rvert^2/(a^2+\lvert b\rvert^2)$ | **[Definition]** | positive-growth diagnostic |
| $\lvert b\rvert/a=\mathcal D_\perp\Lambda_\perp$ | **[Exact — diagnostic, exact by construction]** | algebraic factorization |
| Physical strain–viscous transverse cancellation in low-turning, high-vorticity states | **[Computational observation — DNS, $Re_\lambda\approx38$–$53$]** | independent $r_\perp$, closed budget: median $\cos\varphi(\tau,r_\perp)\approx-0.95$, $\mathcal D_\perp\approx0.24$–$0.30$; scarcity suffices in 5–15 % ([budget note](docs/instantaneous_budget.md) §4.2) |
| $dG=\cos\theta\,dN$ | **[Exact]** | rate-space reparametrization |
| $P_\xi^\perp db/dG=\mathcal Y_\perp/a-b$ | **[Exact]** | direct differentiation on $a>0$ |
| Euler $\lvert\beta\rvert$ law with pressure Hessian | **[Exact]** | reduction of Euler Lagrangian orientation dynamics |
| $P_\xi^\perp db/dG=\mathcal P+\mathcal V_c+\mathcal F-2b$ (pressure, viscous, forcing) | **[Exact]** | differentiation of the velocity-gradient equation; closure converges spectrally under refinement ([budget note](docs/instantaneous_budget.md) §§2–3) |
| Pressure sustains and viscosity removes transverse change at high vorticity | **[Computational observation — DNS]** | $q>3q_{\rm rms}$: $s_P>0$ in 86–87 %, $s_V<0$ in 87–92 %, each about $4$–$5\times$ the kinematic rate; forcing negligible ([budget note](docs/instantaneous_budget.md) §4.3) |
| Resolution sensitivity of pointwise budgets | **[Reported computational observation]** | In the supplied flows, median residual is 12 % at $k_{\max}\eta\approx2$ and 0.8–1.6 % near 3; not a universal threshold ([budget note](docs/instantaneous_budget.md) §3) |
| Burgers calibration of independent growth and turning | **[Exact — analytic benchmark]** | $b=0$ with $a>0$ off the axis; classical whole-space vortex with infinite total kinetic energy |
| Restricted Euler: approach to low-turning channel with model blowup | **[Computational observation — model]** | 200/200 bundled initial conditions reach numerical event; script included |
| High-vorticity low-turning states in bundled JHTDB sample | **[Computational observation — sensitivity-limited]** | selected states survive some independent audits; strongest values are method-sensitive |
| Sensitivity audit for selected state 995 | **[Computational observation — method comparison]** | $\rho_\perp=0.0168$ with m2q8 7pt and 0.0715 with FD4 7pt at $t=1$; threshold classification depends on method |
| Population-level tail law vs $q$ in JHTDB | **[Pending]** | complete filter/query provenance and unbiased sample required |
| Eulerian low-turning fraction vs $q$ in DNS | **[Reported computational observation]** | Conditional on $a>0$ and vorticity bin; includes weighted sampling in the refined run ([budget note](docs/instantaneous_budget.md) §4.1) |
| Relational physical scale for $\Omega$ | **[Hypothesis]** | must be obtained independently and respect NS scaling |

Production DNS values above are supplied results; the 5 October integration reruns small implementation controls rather than the full production protocol. The priority is independent reproduction, precision sensitivity, observable-specific resolution studies and Lagrangian episodes. The current scope is local material dynamics and diagnostics.
