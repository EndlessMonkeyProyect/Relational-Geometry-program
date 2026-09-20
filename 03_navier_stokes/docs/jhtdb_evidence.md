# JHTDB evidence and limits

The bundled tables come from a forced homogeneous-isotropic JHTDB computation and selected trajectory audits.

They support only a narrow statement: high-vorticity states with small measured material turning occur in the retained sample. They do not establish a universal statistical law or a regularity mechanism.

Key limitations:

- the most extreme \(\rho_\perp\) values are sensitive to temporal stencil and vorticity reconstruction;
- the stored extraction does not include the complete query/filter logic for the 437 retained extreme-tail states;
- the residual used for the exploratory cancellation factorization is reconstructed as \(v-S\xi\), so physical compensation is not independently measured;
- derivative-sensitive PDE budgets require a dedicated spatial-resolution study;
- endpoint \(\log(q_2/q_1)\) should be preferred over integrated reconstructed \(a\) when reporting episode growth.

The direct next step is to compute

\[
D_t\omega=S\omega+\nu\Delta\omega+\nabla\times f
\]

from instantaneous fields and close the balance with uncertainty estimates.
