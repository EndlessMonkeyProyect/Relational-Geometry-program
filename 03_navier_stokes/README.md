# Navier–Stokes laboratory

This branch studies material vorticity amplification in three-dimensional incompressible flow. Its purpose is to isolate exact observables and test structural conjectures adversarially.

The branch does **not** claim a proof of regularity or blowup for the unforced 3D Navier–Stokes equations.

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

The homogeneous term $-b$ relaxes transverse change per unit logarithmic growth, while $\mathcal Y_\perp/a$ reaccredits it. This is an exact identity; whether either term dominates is a dynamical question.

## Current empirical status

The bundled JHTDB data show selected high-vorticity states with small material turning, but the most extreme estimates are method-sensitive. The reconstructed residual used in the exploratory cancellation factorization is algebraically dependent on $b$ and strain, so a physical strain–viscous cancellation mechanism remains **[Pending]** until the PDE residual is computed independently.

See `manuscript.md`, `STATUS.md`, and `data/README.md`.
