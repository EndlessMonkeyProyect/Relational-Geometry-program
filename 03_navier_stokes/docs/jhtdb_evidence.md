# JHTDB evidence and limits

The bundled tables come from a forced homogeneous-isotropic JHTDB computation and selected trajectory audits.

They support only a narrow statement: high-vorticity states with small measured material turning occur in the retained sample. They do not establish a universal statistical law or a regularity mechanism.

Key limitations:

- the most extreme $\rho_\perp$ values are sensitive to temporal stencil and vorticity reconstruction;
- the stored extraction does not include the complete query/filter logic for the 437 retained extreme-tail states;
- the residual used for the exploratory cancellation factorization is reconstructed as $v-S\xi$, so physical compensation is not independently measured;
- derivative-sensitive PDE budgets require an observable-specific spatial-resolution study; the [separate DNS study](instantaneous_budget.md) reports improvements for its own flows and does not establish a transferable error threshold for JHTDB;
- endpoint $\log(q_2/q_1)$ should be preferred over integrated reconstructed $a$ when reporting episode growth.

The instantaneous balance

$$
D_t\omega=S\omega+\nu\Delta\omega+\nabla\times f
$$

has been computed and closed in resolved DNS rather than in these tables; see [the budget note](instantaneous_budget.md). Repeating it on JHTDB would require a better-resolved dataset than `isotropic1024coarse`.
