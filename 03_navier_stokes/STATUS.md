# Navier–Stokes branch status

| Item | Status | Evidence / scope |
|---|---|---|
| \(D_t\omega/q=a\xi+b\), \(b\perp\xi\) | **[Exact]** | material differentiation for \(q>0\) |
| \(\rho_\perp=|b|^2/(a^2+|b|^2)\) | **[Definition]** | positive-growth diagnostic |
| \(|b|/a=\mathcal D_\perp\Lambda_\perp\) | **[Exact — diagnostic, exact by construction]** | algebraic factorization |
| Physical strain–viscous/forcing transverse cancellation | **[Pending]** | requires independent PDE residual and budget closure |
| \(dG=\cos\theta\,dN\) | **[Exact]** | rate-space reparametrization |
| \(P_\xi^\perp db/dG=\mathcal Y_\perp/a-b\) | **[Exact]** | direct differentiation on \(a>0\) |
| Euler \(|\beta|\) law with pressure Hessian | **[Exact]** | reduction of Euler Lagrangian orientation dynamics |
| Positive order-one pointwise lower bound on turning | **NO-GO [Exact, class containing Burgers]** | Burgers vortex has \(b=0,a>0\) |
| Unnormalized uniform \(G_\eta\) bound | **NO-GO [Exact, class containing Burgers]** | arbitrarily large parallel growth from large radial deficit |
| Restricted Euler: approach to low-turning channel with model blowup | **[Computational observation — model]** | 200/200 bundled initial conditions reach numerical event; script included |
| High-vorticity low-turning states in bundled JHTDB sample | **[Computational observation — sensitivity-limited]** | selected states survive some independent audits; strongest values are method-sensitive |
| \(\rho_\perp<0.05\) episode 995 as robust | **[Not established]** | FD4 7pt gives 0.0715 at \(t=1\) |
| Population-level tail law vs \(q\) | **[Pending]** | complete filter/query provenance and unbiased sample required |
| OpenAI forced blowup construction | **[External announced result / adversarial benchmark]** | public manuscript + Lean; independent evaluation ongoing as of 19 Sep 2026 |
| Relational physical scale for \(\Omega\) | **[Hypothesis]** | must be obtained independently and respect NS scaling |
