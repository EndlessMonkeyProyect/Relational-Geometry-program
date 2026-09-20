# Material Vorticity Amplification in Growth Coordinates
## Exact transverse dynamics, diagnostic factorization, and adversarial benchmarks

**Le Matt Ansatz Di Ego**  
**September 2026**

## Abstract

For nonzero vorticity $\omega=q\xi$ in three-dimensional incompressible Navier–Stokes flow, the normalized material change splits exactly as

$$
\frac{D_t\omega}{q}=a\xi+b,
\qquad a=D_t\log q,
\qquad b=D_t\xi\perp\xi.
$$

We use this decomposition to separate logarithmic amplification from material turning. A diagnostic transverse factorization, exact by construction, distinguishes small turning caused by low transverse activity from small turning caused by compensation among transverse contributions. The current database reconstruction does not independently establish a physical viscous–strain cancellation; that balance is left as a direct PDE-budget test.

Defining the total normalized change rate $\Omega=(a^2+|b|^2)^{1/2}$, the material rate angle $\theta$, and the growth coordinate $dG=a\,dt=d\log q$, we derive the exact transverse evolution law

$$
\boxed{
P_\xi^\perp\frac{db}{dG}
=
\frac{\mathcal Y_\perp}{a}-b,
\qquad
\mathcal Y=D_t\!\left(\frac{D_t\omega}{q}\right),
}
$$

valid on positive-growth segments. Thus transverse change is not automatically preserved while vorticity magnitude grows: it must be continually supplied by the projected second material dynamics. In Euler flow this law reduces to the known pressure-Hessian-controlled Lagrangian orientation dynamics. A Burgers-vortex benchmark gives an exact no-go against any universal pointwise lower bound on turning and against any unnormalized uniform bound on nearly-parallel accumulated growth in a class containing that vortex. Restricted Euler supplies a complementary model benchmark in which the nearly-parallel channel is approached while growth diverges.

A finite JHTDB screen is retained only as diagnostic evidence: it contains high-vorticity, low-turning states, but the most extreme values are method-sensitive and the extraction filters are not yet fully reproducible. The next decisive computation is therefore an instantaneous PDE budget for $D_t\omega$, including direct viscous and forcing contributions. We make no regularity or blowup claim for the unforced 3D Navier–Stokes equations.

## 1. Scope and relation to existing work

Vorticity-direction geometry and geometric depletion have a substantial literature. Constantin and Fefferman established a foundational direction-of-vorticity regularity criterion. Gibbon, Holm, Kerr and Roulstone formulated Euler vorticity growth and rotation along particles in a quaternionic/Lagrangian framework governed by the pressure Hessian. Later work has emphasized tangential strain, viscous tilting, and the role of twist/anti-twist in intense turbulence.

This manuscript does not claim novelty for the vorticity-direction equation, tangential strain, or pressure-Hessian control of Euler orientation. Its narrower contribution is to organize the material-vorticity state into growth coordinates, derive the exact transverse evolution law used below, and subject candidate mechanisms to explicit no-go examples and numerical sensitivity tests.

## 2. Governing equation and exact material channels

Consider

$$
\partial_tu+u\cdot\nabla u+\nabla p=\nu\Delta u+f,
\qquad \nabla\cdot u=0.
$$

With $\omega=\nabla\times u$ and $S=(\nabla u+\nabla u^T)/2$,

$$
D_t\omega=S\omega+\nu\Delta\omega+\nabla\times f.
$$

On $q=|\omega|>0$, write $\omega=q\xi$, $|\xi|=1$. Then

$$
D_t\omega=(D_tq)\xi+qD_t\xi.
$$

Define

$$
a=D_t\log q,\qquad b=D_t\xi.
$$

Because $\xi\cdot b=0$,

$$
\boxed{\frac{D_t\omega}{q}=a\xi+b},
\qquad
\boxed{\frac{|D_t\omega|^2}{q^2}=a^2+|b|^2}.
$$

For $a>0$, define

$$
\rho_\perp=\frac{|b|^2}{a^2+|b|^2},
\qquad
\mathscr R=\frac{|b|^2}{a^2}.
$$

These are dimensionless and invariant under the natural Navier–Stokes scaling.

## 3. Diagnostic transverse factorization

Write

$$
\frac{D_t\omega}{q}=S\xi+r_{\rm PDE},
\qquad
r_{\rm PDE}=\frac{\nu\Delta\omega+\nabla\times f}{q}.
$$

Project transversely:

$$
\tau=P_\xi^\perp S\xi,
\qquad
r_\perp=P_\xi^\perp r_{\rm PDE},
\qquad
b=\tau+r_\perp.
$$

Let $T=|\tau|$, $M=|r_\perp|$, and define

$$
\mathcal D_\perp=\frac{|b|}{T+M},
\qquad
\Lambda_\perp=\frac{T+M}{a}.
$$

Then, for $a>0$,

$$
\boxed{\frac{|b|}{a}=\mathcal D_\perp\Lambda_\perp.}
$$

This identity is exact by construction. Its value is diagnostic: $\Lambda_\perp\ll1$ represents transverse scarcity, whereas $\mathcal D_\perp\ll1$ with appreciable $\Lambda_\perp$ represents net compensation among transverse components.

In the bundled JHTDB reconstruction, however, the residual was formed numerically as $r=v-S\xi$ with $v=D_t\omega/q$; hence $r_\perp=b-\tau$ is algebraically imposed. Small $|b|$ relative to $|\tau|$ then forces near compensation in that reconstruction. Therefore a physical viscous/forcing compensation mechanism remains **[Pending]** until $r_\perp^{\rm PDE}$ is computed independently from spatial fields and the full vorticity budget is closed.

## 4. Rate space and growth coordinate

Define

$$
\Omega=\frac{|D_t\omega|}{q}=\sqrt{a^2+|b|^2}.
$$

For $a>0$, let

$$
a=\Omega\cos\theta,\qquad |b|=\Omega\sin\theta.
$$

Then

$$
\rho_\perp=\sin^2\theta.
$$

Define the dimensionless accumulated material-change count

$$
dN=\Omega\,dt.
$$

Because $dG=d\log q=a\,dt$,

$$
\boxed{dG=\cos\theta\,dN}.
$$

On a low-turning interval $\rho_\perp<\eta$,

$$
\sqrt{1-\eta}\,\Delta N<G\le\Delta N.
$$

Thus $G$ and $\Delta N$ are equivalent within the channel up to the fixed factor $\sqrt{1-\eta}$; bounding $\Delta N$ is an in-channel reformulation, not a stronger theorem target by itself.

## 5. Exact transverse evolution in growth coordinates

Let

$$
\mathcal V=\frac{D_t\omega}{q}=a\xi+b,
\qquad
\mathcal Y=D_t\mathcal V.
$$

Differentiating and using $\xi\cdot b=0$ gives

$$
D_ta=|b|^2+\xi\cdot\mathcal Y,
$$

$$
D_tb=P_\xi^\perp\mathcal Y-ab-|b|^2\xi.
$$

Therefore

$$
\boxed{P_\xi^\perp D_tb=\mathcal Y_\perp-ab.}
$$

On $a>0$, using $dG=a\,dt$,

$$
\boxed{
P_\xi^\perp\frac{db}{dG}
=
\frac{\mathcal Y_\perp}{a}-b.
}
$$

The homogeneous term $-b$ is a unit-rate relaxation per e-fold of vorticity growth. This does **not** imply that the nearly-parallel channel is a universal attractor: the signed forcing term $\mathcal Y_\perp/a$ can dominate. The mathematical question is therefore to identify and control the signed projected terms that reaccredit transverse change.

An alternative scalar identity,

$$
\frac{d\rho_\perp}{dG}=2\kappa,
$$

is exact but is secondary here: endpoint averages of $\kappa$ are finite-difference slopes of $\rho_\perp$ against $\log q$ and do not independently identify a mechanism.

## 6. Euler reduction and the pressure Hessian

For incompressible Euler,

$$
D_t\omega=S\omega.
$$

Let $\alpha=\xi\cdot S\xi$ and $\tau=P_\xi^\perp S\xi$. Then $a=\alpha$, $b=\tau$. If $P=\nabla\nabla p$, the Euler gradient equation implies

$$
D_t^2\omega=-P\omega.
$$

Equivalently,

$$
\mathcal Y=-P\xi-\alpha S\xi.
$$

Hence

$$
P_\xi^\perp D_t\tau=-2\alpha\tau-P_\xi^\perp P\xi.
$$

This is the pressure-Hessian-controlled orientation dynamics already represented in the Lagrangian framework of Gibbon et al.

Define $\beta=\tau/\alpha$, $\alpha_p=\xi\cdot P\xi$, and

$$
\Pi_\perp=\frac{P_\xi^\perp P\xi}{\alpha^2}.
$$

On positive-growth segments,

$$
\boxed{
\frac{d|\beta|}{dG}
=-|\beta|\left(1+|\beta|^2-\frac{\alpha_p}{\alpha^2}\right)
-\hat\beta\cdot\Pi_\perp.
}
$$

The sign of the projected pressure-Hessian term matters; a bound on $|\Pi_\perp|$ alone cannot determine exit from or entry into the channel.

## 7. Exact no-go benchmark: Burgers vortex

The classical Burgers vortex supplies an exact counterexample to overly strong channel conjectures. With

$$
u_r=-\frac{\gamma r}{2},\qquad u_z=\gamma z,
$$

and axial vorticity

$$
q(r)=q_0\exp\!\left(-\frac{\gamma r^2}{4\nu}\right),
\qquad \xi=\hat z,
$$

one has

$$
b\equiv0,\qquad \rho_\perp\equiv0,
$$

while along a trajectory

$$
a=D_t\log q=\frac{\gamma^2r^2}{4\nu}>0.
$$

For radial contraction from $r_1$ to $r_2$,

$$
G=\log\frac{q(r_2)}{q(r_1)}
=\frac{\gamma(r_1^2-r_2^2)}{4\nu}.
$$

Thus, in any class containing the classical Burgers vortex:

- **NO-GO [Exact]:** no universal positive lower bound of the form $|D_t\xi|\ge c(D_t\log q)_+$;
- **NO-GO [Exact]:** no unnormalized uniform bound on accumulated nearly-parallel growth $G_\eta$.

The standard Burgers vortex on $\mathbb R^3$ has infinite total kinetic energy, so these no-go statements do not automatically rule out hypotheses restricted by finite energy, domain, or relative-vorticity conditions.

## 8. Restricted Euler model benchmark

Restricted Euler replaces the anisotropic pressure Hessian by its isotropic local closure. In this model $\Pi_\perp=0$, and the dynamics is known to develop finite-time singular behavior for generic initial data.

Running the bundled reproducibility script with `--full` samples 200 Gaussian trace-free initial velocity-gradient matrices. All 200 reach the numerical event $\|A\|=10^6$ within the integration horizon. At the sampled point $t=T(1-10^{-4})$, the median $\rho_\perp$ is approximately $4.7\times10^{-23}$. The exact $|\beta|$-law above matches finite-difference estimates to six decimal places at the two documented checkpoints.

This is **[Computational observation — model system]**, not evidence that Navier–Stokes itself follows restricted Euler. Its role is adversarial: local blowup can coexist with collapse toward the nearly-parallel channel when the nonlocal anisotropic pressure mechanism is removed.

## 9. JHTDB diagnostics and limitations

The bundled data derive from the forced homogeneous-isotropic `isotropic1024coarse` JHTDB dataset. They were used to search for high-vorticity states with small $\rho_\perp$ and to audit selected trajectories with independent finite-difference vorticity reconstructions.

Two selected states illustrate both the signal and the uncertainty:

| ID | $q$ m2q8 | $q$ FD4 | $\rho$ m2q8, 7pt | $\rho$ FD4, 7pt | $\rho$ FD4, 5pt |
|---:|---:|---:|---:|---:|---:|
| 995 | 226.526 | 223.441 | 0.0168 | 0.0715 | 0.0465 |
| 961 | 146.673 | 146.364 | 0.0423 | 0.0404 | 0.0411 |

The 995 estimate is strongly method-sensitive. Even within the stored m2q8 temporal fits, ID 961 at $t=1.002$ changes from $\rho_7=0.0102$ to $\rho_5=0.0506$. Therefore the repository does not designate a $\rho_\perp<0.05$ episode as robust.

For two illustrative endpoint intervals, the exact endpoint growth budgets are

$$
G_{961,[1.000,1.004]}=0.06853,
\qquad
G_{995,[0.998,1.004]}=0.05136.
$$

The trapezoidal integrals of the reconstructed $a$ differ from these endpoint logarithms by about $-8\%$ and $+4\%$, respectively; other bundled intervals show larger discrepancies. Endpoint $\log(q_2/q_1)$ is therefore the primary growth budget.

The extreme-tail table contains 437 retained positive-growth states after a screening/stability stage whose complete query logic is not bundled. Consequently the tabulated small-$\rho$ counts are descriptive of the retained sample and are not treated as population-level statistics. A complete public query script and unconditional trajectory sample are required before stronger statistical claims are made.

The next decisive computation is instantaneous:

$$
D_t\omega=S\omega+\nu\Delta\omega+\nabla\times f.
$$

This removes shared temporal-fit windows, but it does not remove numerical difficulty: $\Delta\omega$ and $\nabla\times f$ require high-order spatial information. Resolution convergence must be tested explicitly.

## 10. External adversarial benchmark

On 8 September 2026, OpenAI publicly announced a finite-time blowup construction for forced three-dimensional incompressible Navier–Stokes, together with a Lean formalization. The public formalization metadata records `review.status: self-assessed`; on 11 September the Clay Mathematics Institute described the announcement as one that "has apparently been settled" while stating that its evaluation process will be deliberately unhurried.

This repository uses that work only as an **external adversarial benchmark**. No theorem here depends on its validity. If the announced construction withstands evaluation, the material observables should be computed on its explicit asymptotic structure. If it does not, the exact identities and local benchmarks in this repository are unchanged.

## 11. Relational correspondence and scaling

The broader relational program interprets time operationally as comparison of rates and contains a conditional oscillatory realization with $R\varpi=\mathrm{const}$. That law must not be imposed on incompressible Navier–Stokes.

Under

$$
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
$$

lengths scale as $\lambda^{-1}$ and material rates as $\lambda^2$. Thus $R^2\varpi$, not $R\varpi$, is scale-invariant.

Accordingly, any physical relational bridge to Navier–Stokes must first identify an independent spatial scale and then test whether its rate relation is parabolic, linear, or neither. Introducing $c$ into incompressible Navier–Stokes by definition would not provide new content.

## 12. Research targets

1. **Direct PDE budget.** Compute $r_\perp^{\rm PDE}=P_\xi^\perp(\nu\Delta\omega+\nabla\times f)/q$ and close $D_t\omega-S\omega-\nu\Delta\omega-\nabla\times f$ within quantified uncertainty.
2. **Signed channel forcing.** Decompose $\mathcal Y_\perp/a$ into pressure, viscous, and forcing contributions and identify the signed terms controlling transverse reaccreditation.
3. **Unconditional episodes.** Seed trajectories without conditioning on extreme $q$ and report $G_\eta$ distributions conditional on initial vorticity and available headroom.
4. **Resolution audit.** Repeat instantaneous diagnostics on a better-resolved dataset/snapshot and test convergence of derivative-sensitive quantities.
5. **Benchmark ladder.** Maintain Burgers $\to$ restricted Euler $\to$ DNS $\to$ explicit singular constructions as progressively harder falsifiers.

## 13. Conclusion

The exact material split turns vorticity amplification into a two-channel problem: growth of magnitude along the current direction and transverse change of that direction. In growth coordinates, the transverse evolution satisfies an exact relaxation-plus-reaccreditation law. This local law neither proves regularity nor makes the nearly-parallel channel intrinsically dangerous: Burgers and restricted Euler show why both conclusions would be too strong.

The useful open problem is narrower and more concrete: determine which signed nonlocal and viscous terms maintain or destroy transverse difference during sustained amplification, and whether their dynamics imply a quantitative restriction in a physically relevant class.
