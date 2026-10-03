# Navier–Stokes branch status

The established contribution is the exact separation of material amplification and turning, together with its evolution in growth coordinates. The table connects each result to the evidence available for review.

| Item | Status | Evidence / scope |
|---|---|---|
| $D_t\omega/q=a\xi+b$, $b\perp\xi$ | **[Exact]** | material differentiation for $q>0$ |
| $\rho_\perp=\lvert b\rvert^2/(a^2+\lvert b\rvert^2)$ | **[Definition]** | positive-growth diagnostic |
| $\lvert b\rvert/a=\mathcal D_\perp\Lambda_\perp$ | **[Exact — diagnostic, exact by construction]** | algebraic factorization |
| Physical strain–viscous/forcing transverse cancellation | **[Pending]** | requires independent PDE residual and budget closure |
| $dG=\cos\theta\,dN$ | **[Exact]** | rate-space reparametrization |
| $P_\xi^\perp db/dG=\mathcal Y_\perp/a-b$ | **[Exact]** | direct differentiation on $a>0$ |
| Euler $\lvert\beta\rvert$ law with pressure Hessian | **[Exact]** | reduction of Euler Lagrangian orientation dynamics |
| Burgers calibration of independent growth and turning | **[Exact — analytic benchmark]** | $b=0$ with $a>0$ off the axis; classical whole-space vortex with infinite total kinetic energy |
| Restricted Euler: approach to low-turning channel with model blowup | **[Computational observation — model]** | 200/200 bundled initial conditions reach numerical event; script included |
| High-vorticity low-turning states in bundled JHTDB sample | **[Computational observation — sensitivity-limited]** | selected states survive some independent audits; strongest values are method-sensitive |
| Sensitivity audit for selected state 995 | **[Computational observation — method comparison]** | $\rho_\perp=0.0168$ with m2q8 7pt and 0.0715 with FD4 7pt at $t=1$; threshold classification depends on method |
| Population-level tail law vs $q$ | **[Pending]** | complete filter/query provenance and unbiased sample required |
| Relational physical scale for $\Omega$ | **[Hypothesis]** | must be obtained independently and respect NS scaling |

The priority for independent review is to verify the exact growth-coordinate derivation, reproduce the benchmark calculations, and compute the strain–viscous/forcing balance directly from the PDE. The current scope is local material dynamics and diagnostics; an extension to a global regularity or blowup theorem requires additional estimates.
