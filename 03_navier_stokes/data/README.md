# Data provenance and limitations

This directory separates two sources: selected JHTDB-derived tables from the earlier exploration, and budget_*.csv tables from the supplied purpose-built DNS experiment. Neither is a raw snapshot release.

They are **not** a complete raw-data release. In particular:

- the complete JHTDB query script and token-free extraction recipe are not yet bundled;
- the complete criteria behind the retained/stability screen are not fully reconstructed from the bundled tables;
- `chi_med` / `chi_parallel` is present in stored output but its generating definition is not recovered here, so no physical interpretation is assigned to it;
- `fit5`, `fit7`, and `rho_diff` are numerical fit diagnostics; the manuscript does not use them as independent physical observables;
- labels containing `robust_rho` in `phase4_episodes.csv` are source-table labels only. The public manuscript does not adopt the $rho<0.05$ label as a robust result.

For episode growth, use the exact endpoint quantity

$$
G=\log(q_2/q_1)
$$

as the primary budget and use `G_int_a_dt - log_q_ratio` as a reconstruction-error diagnostic.

## DNS budget tables

The budget_*.csv files were supplied with the author's 4 October 2026 DNS patch. They are retained unchanged. The [budget note](../docs/instantaneous_budget.md) supplies commands, precision conventions and scope; the 5 October integration did not regenerate production tables. Small automated closure and refinement tests were rerun.

| File | Content |
|---|---|
| `budget_{n128,n192,lowre128}_snapshots.csv` | run diagnostics per snapshot ($Re_\lambda$, $k_{\max}\eta$, $\varepsilon$, $\eta$, $q_{\rm rms}$) |
| budget_{n128,n192,lowre128}_tail_vs_q.csv | Volume-weighted low-turning probabilities conditional on positive growth and the stated vorticity bin |
| `budget_{n128,n192,lowre128}_conditional.csv` | weighted medians, deciles and sign fractions of $\rho_\perp$, $\Lambda_\perp$, $\mathcal D_\perp$, $\cos\varphi$, $s_P$, $s_V$, $s_F$, $d\log\lvert b\rvert/dG$ and resolution diagnostics, by vorticity class |
| `budget_resolution_audit.csv`, `budget_resolution_audit_runs.csv` | pointwise $N=128$ vs $N=192$ comparison on common grid points |
| `budget_closure*.csv` | residuals of the instantaneous $D_t\omega$ and $\mathcal Y$ against five-level time differences |

The supplied resolution-audit CSV uses its p90 column for sign agreement in rows whose quantity starts with sP, sV or sF; in vector-error rows it is a 90th percentile. Read that field together with the quantity label. These legacy columns are preserved rather than silently changing supplied values.

Run tags: `n128` = run A ($k_{\max}\eta\approx2$), `n192` = run A refined to $N=192$ ($k_{\max}\eta\approx2.9$, complete set above $2q_{\rm rms}$ plus a 2 % weighted uniform sample), `lowre128` = run B ($k_{\max}\eta\approx3$).
