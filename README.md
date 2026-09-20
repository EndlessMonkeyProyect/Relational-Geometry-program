# Relational Geometry Program
## Difference, closure, identity, rate comparison, and a Navier–Stokes laboratory

**Author:** Le Matt Ansatz Di Ego  
**Public release:** 1.0 — September 2026

This repository presents a self-contained research program built from a strict order of logical dependence:

$$
\text{singular unit}
\to \text{reflection}
\to \text{difference}
\to \text{relation}
\to \text{comparison}
\to \text{residue}
\to \text{recursion}
\to \text{closure}
\to \text{identity}.
$$

The program asks whether categories usually taken as primitive—cardinality, dimension, geometry, time, force, particle, and physical scale—can instead be introduced only when they become necessary to preserve distinguishable information.

The repository deliberately separates five layers:

1. **ontology and definitions** — what the words mean inside the program;
2. **formal realizations** — mathematics that follows from explicit assumptions;
3. **correspondences** — structural similarities that do not establish identity;
4. **physical laboratories** — systems used to test whether the formal language acquires predictive content;
5. **falsifiers and open problems** — explicit places where the program can fail.

The main conceptual text is [`publication/relational_geometry_core.es.md`](publication/relational_geometry_core.es.md).

For academic positioning, neighboring frameworks, and concrete research interfaces, see [`publication/academic_context_and_research_interfaces.md`](publication/academic_context_and_research_interfaces.md).

The Navier–Stokes branch is a technical laboratory, not a claimed solution of the regularity problem. Its current core result is an exact material decomposition and an exact evolution law for the transverse channel in growth coordinates. See [`03_navier_stokes/manuscript.md`](03_navier_stokes/manuscript.md).

## What is established inside the repository

- Difference is treated as logically prior to counting.
- Comparison is represented as resolved content plus residue.
- Closure is not identified with return, a small residual, or disappearance of difference; it is modeled as internal reconstructibility/autoreference.
- In a conditional algebraic realization with $J^2=-I$, the local discrete cycle has order four and $J^4=I$.
- The continuous interpolation $e^{\theta J}=\cos\theta I+\sin\theta J$ has period $2\pi$; $\pi$ enters at the continuous periodic representation, not in the four-step discrete count itself.
- A quadratic variational dynamics with comparator $G=C^\dagger C$ yields $\ddot f+\Gamma Gf=0$, hence $\varpi_i^2=\Gamma\lambda_i$ and, for $R_i=\lambda_i^{-1/2}$, $R_i|\varpi_i|=\sqrt\Gamma$ within that realization.
- Navier–Stokes has a different, parabolic scaling; a physically meaningful scale–rate lift must respect that distinction rather than importing a universal $R\varpi=\mathrm{const}$ law.

## What is not claimed

This repository does **not** claim:

- a derivation of physics from first principles;
- that all appearances of the number four have a single proven origin;
- that $\pi$ has been derived from nothing;
- that a proton, vortex, or other physical object is identical to the abstract closure construction;
- that $c$ is a primitive constant of incompressible Navier–Stokes;
- that low transverse turning implies singularity or closure;
- a proof of regularity or blowup for unforced three-dimensional Navier–Stokes.

## Navigation

- [`00_orientation/START_HERE.md`](00_orientation/START_HERE.md) — reading order.
- [`00_orientation/EPISTEMIC_LEGEND.md`](00_orientation/EPISTEMIC_LEGEND.md) — status labels.
- [`publication/academic_context_and_research_interfaces.md`](publication/academic_context_and_research_interfaces.md) — academic positioning, neighboring frameworks, and testable interfaces.
- [`01_foundations/`](01_foundations/) — conceptual core and the roles of four, $\pi$, rate, and time.
- [`02_formal_core/`](02_formal_core/) — compact formal constructions.
- [`03_navier_stokes/`](03_navier_stokes/) — technical fluid-dynamics branch.
- [`04_results/`](04_results/) — result, no-go, and open-problem registers.
- [`tests/`](tests/) — exact-identity and release-consistency tests.

## Reproducibility

From the repository root:

```bash
python -m pytest -q
python 03_navier_stokes/scripts/restricted_euler_benchmark.py   # quick smoke test
python 03_navier_stokes/scripts/restricted_euler_benchmark.py --full  # documented 200 trajectories; slower
python 03_navier_stokes/scripts/review_checks.py
```

The bundled JHTDB files are compact derived tables, not a replacement for a complete database extraction. Their limitations are documented in `03_navier_stokes/data/README.md`.
