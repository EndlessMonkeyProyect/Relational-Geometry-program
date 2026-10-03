# Order-four operator realization

The [minimal reflexive extension](reflexive_extension.es.md) derives the condition below from an antisymmetric comparison and norm preservation. This note records its discrete and continuous consequences.

Assume a real vector space equipped with an operator $J$ such that

$$
J^2=-I.
$$

Then

$$
J^3=-J,\qquad J^4=I.
$$

Hence the orbit of every nonzero real vector $x$ under integer powers of $J$ is

$$
x,\;Jx,\;-x,\;-Jx,\;x.
$$

This is an exact order-four cycle: equality of adjacent phases would produce a real eigenvalue whose square is $-1$, and $x=-x$ would force $x=0$.

If the space also carries an inner product for which $J$ is orthogonal and skew-adjoint, then

$$
\langle x,Jx\rangle=0.
$$

The continuous one-parameter subgroup is

$$
e^{\theta J}=\cos\theta I+\sin\theta J,
$$

with period $2\pi$.

Status: **[Exact under stated hypotheses]**. The next review question is which operational or physical systems realize the antisymmetric, norm-preserving comparison.
