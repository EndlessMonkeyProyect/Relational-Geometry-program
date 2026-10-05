# Navier–Stokes laboratory

This laboratory makes a basic distinction in three-dimensional incompressible flow measurable: **how quickly vorticity grows, and how quickly its direction turns along a fluid particle**. Separating these channels gives exact observables, an evolution law in units of logarithmic growth, and a concrete way to examine which physical terms sustain directional change during amplification.

The contribution available for review is an exact diagnostic framework, supported by analytic calibration, a reproducible local-model benchmark, and selected turbulence data. Its scope is the geometry and measurement of material amplification; global regularity and blowup for unforced 3D Navier–Stokes remain open research questions within this program.

## Core exact objects

For $\omega=q\xi$, $q>0$,

$$
\frac{D_t\omega}{q}=a\xi+b,
\qquad a=D_t\log q,
\qquad b=D_t\xi\perp\xi.
$$

Define

$$
\Omega=\sqrt{a^2+|b|^2},\qquad
\rho_\perp=\frac{|b|^2}{a^2+|b|^2}.
$$

With $\mathcal V=D_t\omega/q$, $\mathcal Y=D_t\mathcal V$, and $dG=a\,dt$ on positive-growth segments,

$$
\boxed{P_\xi^\perp\frac{db}{dG}=\frac{\mathcal Y_\perp}{a}-b.}
$$

The homogeneous term $-b$ relaxes transverse change per unit logarithmic growth, while the signed term $\mathcal Y_\perp/a$ supplies or opposes it. This identifies the balance that a physical mechanism must explain. Dominance of either term is a dynamical question.

## Evidence and next review

- **Exact calibration:** the Burgers vortex realizes positive material amplification with fixed vorticity direction, making the distinction between growth and turning explicit.
- **Reproducible model:** the restricted Euler computation tests the growth-coordinate law in a local pressure closure and records the approach to small turning relative to growth.
- **Turbulence diagnostics:** selected bundled JHTDB states combine high vorticity with small material turning. Their numerical sensitivity is documented in the manuscript and status table.

- **Instantaneous budget in resolved DNS:** the strain, viscous, forcing and pressure contributions are computed separately, closed against the evolving flow and audited for resolution. Low turning at high vorticity is mainly a strain–viscous compensation, and the projected pressure Hessian sustains turning against viscosity, at $Re_\lambda\approx38$–$53$ ([budget note](docs/instantaneous_budget.md)).

The next review is to reproduce the production budget, measure precision sensitivity and extend it to higher Reynolds number with observable-specific convergence tests and Lagrangian episodes.

Read the [manuscript](manuscript.md), [evidence status](STATUS.md), [benchmark guide](docs/benchmarks.md), [instantaneous budget](docs/instantaneous_budget.md), and [data provenance](data/README.md). For focused review across the program, see [REVIEW](../REVIEW.md).
