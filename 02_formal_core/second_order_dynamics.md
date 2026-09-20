# Reflection-symmetric second-order dynamics

Let $C:V\to Y$ and define

$$
G=C^\dagger C\ge0.
$$

For discrete configurations $f_n$ separated by a relational step $\delta$, the local linear combination using both neighbors, invariant under $n-1\leftrightarrow n+1$, and annihilating constants and linear progressions is proportional to

$$
f_{n+1}-2f_n+f_{n-1}.
$$

Consider the discrete action

$$
S_\delta[f]
=\sum_n\left[
\frac{\|f_{n+1}-f_n\|^2}{2\delta^2}
-\frac{\Gamma}{2}\langle f_n,Gf_n\rangle
\right].
$$

Stationarity gives

$$
\frac{f_{n+1}-2f_n+f_{n-1}}{\delta^2}+\Gamma Gf_n=0.
$$

Under a smooth continuum limit,

$$
\boxed{\ddot f+\Gamma Gf=0.}
$$

For $Gu_i=\lambda_i u_i$,

$$
\boxed{\varpi_i^2=\Gamma\lambda_i.}
$$

The result is conditional on the quadratic local action and reflection-symmetric discretization. It does not establish that every physical realization of the program must be second order.
