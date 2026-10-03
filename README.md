# Relational Geometry Program

**How distinguishable information supports geometry, identity, and composition**

Le Matt Ansatz Di Ego · [Español](README.es.md) · [Review invitation](REVIEW.md)

The Relational Geometry Program develops a common language for a concrete question: **what information must a system preserve to distinguish states, retain its identity, and compose with other systems?** Its central move is to start with distinctions and comparisons, then construct the representations needed to retain them.

This repository brings together conceptual foundations, explicit mathematical constructions, and computational laboratories. Its value is structural and practical: it connects questions about information and geometry to objects that can be calculated, checked, and extended. We invite focused review of those connections and their applications.

## Contributions worth examining

| Contribution | What it establishes | Why it matters |
|---|---|---|
| **Information and closure** | A signature partitions states by the questions they can answer; a new comparison refines that partition exactly when it does not factor through the existing signature. | Gives an operational criterion for new information and sufficient descriptions. |
| **Minimal reflexive extension** | An antisymmetric, norm-preserving linear comparison satisfies $J^2=-I$. A nonzero new direction generates a real plane and a four-phase orbit. | Connects stated comparison rules to dimension, orthogonality, and a closed phase structure. |
| **Sixteen phase signatures and invariant measure** | Two independently accessible four-phase coordinates give $\mathbb Z_4^2$. A normalized local inner product invariant under both phase translations assigns weight $1/16$ to each signature and $15/16$ to its complement. | Makes the chain from phase structure to counting and measure explicit and reviewable. |
| **Exact composition of capsules** | Joining compatible relations and eliminating internal variables preserves the full relation visible at the external boundary. | Provides a compositional foundation for constraint solving and reusable interfaces. |
| **Navier–Stokes observables** | Exact material identities separate vorticity amplification from turning and express transverse evolution per unit logarithmic growth. | Supplies measurable diagnostics and a target for pressure, viscosity, and forcing budgets. |
| **Non-Abelian relational observable** | An explicit $SU(2)$ commutator observable measures failure of two holonomies to commute. | Gives the Yang–Mills branch a computable object and a route toward coercivity questions. |

These results have different scopes. Algebraic statements apply under the hypotheses written in their proofs; model computations have documented protocols; physical interpretations identify additional maps to observables that need review. The [results register](04_results/RESULTS_REGISTER.md) connects each contribution to its evidence.

## Read according to your interest

- **Understand the program:** [Spanish overview](publication/PROGRAM_OVERVIEW.es.md) and [integrated conceptual and mathematical core](publication/relational_geometry_core.es.md).
- **Check the mathematics:** [information and closure](02_formal_core/closure_information.es.md), [reflexive extension](02_formal_core/reflexive_extension.es.md), [phase structure and invariant measure](02_formal_core/phase_measure.es.md), and [composition theorem](02_formal_core/compatible_reclosure.es.md).
- **Explore applications:** [computation and constraints](05_computation/README.md), [Navier–Stokes](03_navier_stokes/README.md), [Yang–Mills](06_yang_mills/README.md), and [physical research targets](publication/physical_bridges.es.md).
- **Contribute a review:** choose a [specific review question](REVIEW.md). A focused check of one proof, implementation, or physical bridge is a useful contribution.

The shared architecture is the research program's organizing proposal. Each domain supplies its own objects, hypotheses, and evidence. Computational complexity bounds, dynamical selection of comparisons, and conversion of formal measure into physical observables are active research targets.

## Reproduce and inspect

Use Python 3.11 or later. From the repository root:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python 03_navier_stokes/scripts/restricted_euler_benchmark.py
python 03_navier_stokes/scripts/review_checks.py
python 06_yang_mills/scripts/gaussian_control.py --quick
python tools/public_release.py
```

The tests check finite examples, algebraic consistency, and release integrity. Proofs and assumptions are included in the documents. See [status](STATUS.md) for evidence levels and [contributing](CONTRIBUTING.md) for review and reproduction details.

Authorship and reuse terms are recorded in [CITATION.cff](CITATION.cff) and [NOTICE.md](NOTICE.md).
