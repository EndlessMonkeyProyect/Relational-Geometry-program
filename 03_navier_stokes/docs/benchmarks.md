# Benchmarks for amplification and turning

The same observables connect three levels of evidence: an exact analytic calibration, a reproducible local model, and selected full-PDE turbulence data. Each level answers a different review question.

## 1. Burgers vortex — exact control

Purpose: calibrate the separation of material amplification and turning. The axial direction is fixed, so $b=0$, while radial contraction gives $a>0$ off the axis. The exact endpoint ratio $G=\log(q_2/q_1)$ checks the accumulated-growth diagnostic.

Scope: the classical whole-space Burgers vortex has infinite total kinetic energy. It provides an analytic control for the observables; finite-energy Navier–Stokes questions require separate assumptions.

## 2. Restricted Euler — local model

Purpose: test the channel law under an explicit local pressure closure. The bundled script reproduces the approach toward $\rho_\perp\to0$ while the model approaches its finite-time singular event.

Scope: numerical evidence for the restricted Euler model. Review centers on reproducing the integration and checking the growth-coordinate identity against the model dynamics.

## 3. DNS/JHTDB — full viscous dynamics

Purpose: measure the terms sustaining transverse change in full viscous dynamics and test resolution and stencil sensitivity.

Scope: the bundled JHTDB states document high vorticity with small estimated material turning, along with method-dependent values. The [instantaneous budget](instantaneous_budget.md) evaluates the strain, viscous, forcing and pressure terms independently in resolved spectral DNS, closes them against the evolving flow, and audits resolution; reconstructed residuals are no longer needed for the cancellation question at those parameters.

The [manuscript](../manuscript.md) gives the derivations and quantitative sensitivity audit. The [status table](../STATUS.md) identifies the evidence available for each result and the measurements needed next.
