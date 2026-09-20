# Data provenance and limitations

These files are compact derived tables from a JHTDB forced-isotropic turbulence exploration. They are included so that every numerical statement in the manuscript can be traced to a concrete table.

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
