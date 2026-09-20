# Relational Geometry as a Research Program
## Academic context, neighboring frameworks, and testable interfaces

**Author:** Le Matt Ansatz Di Ego  
**Release:** 1.0 — September 2026  
**Purpose:** positioning document for academic readers

---

## Abstract

The Relational Geometry Program asks whether several structures commonly taken as primitive in physical description—cardinality, dimension, geometry, time, identity, and physical scale—can instead be introduced in a strict order of logical dependence beginning from distinguishability, comparison, residue, recursion, and closure. Its canonical dependency chain is

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

This document does not claim that this program is equivalent to any established framework. Its purpose is narrower and more useful: to locate the program relative to existing academic traditions, identify genuine mathematical overlaps, distinguish superficial analogies from testable correspondences, and specify interfaces through which the proposal can be evaluated by specialists.

The nearest conceptual neighbors include relational approaches to physical state and motion, structural realism, operational and informational reconstructions of physical theories, mathematical treatments of self-reference and fixed points, information geometry, complex and quaternionic realizations of rotation, and geometric/Lagrangian approaches to vorticity dynamics. The Navier–Stokes branch is treated as a physical laboratory in which the program's language of reference, transverse difference, reaccreditation, and scale can be confronted with exact equations and numerical data.

The central academic claim of this positioning paper is therefore not that the program subsumes these literatures. It is that they provide a set of **comparison classes and mathematical instruments** capable of turning the program's ontology into precise theorems, NO-GO results, and discriminating experiments.

---

## 1. Scope and epistemic boundary

The program is best read as a research architecture rather than as a completed physical theory. Its current documents distinguish:

- **[Exact]** mathematical identities under explicit hypotheses;
- **[Program derivation]** consequences internal to a chosen formal realization;
- **[Correspondence]** structural similarity with an established mathematical or physical object;
- **[Hypothesis]** a proposed bridge not yet derived;
- **[Pending]** a specific unresolved obligation;
- **NO-GO** a route already shown to be insufficient or false within its stated scope.

This distinction is essential for academic comparison. A neighboring theory can be relevant in at least four different ways:

1. it may provide a **formal language** for a concept already present in the program;
2. it may provide a **known theorem** that limits what the program can claim;
3. it may provide a **physical analogue** suitable for testing a proposed correspondence;
4. it may expose a **difference** sharp enough to become a falsifiable prediction.

No external framework is cited here as retrospective justification for the program's ontology. The intended direction remains

$$
\text{concept}
\to \text{formal obligation}
\to \text{mathematical realization}
\to \text{physical bridge}
\to \text{measurement or falsification}.
$$

For the internal conceptual statement, see [`relational_geometry_core.es.md`](relational_geometry_core.es.md).

---

## 2. The program in neutral academic language

Before comparing it with other traditions, it is useful to restate the proposal without its internal metaphors.

### 2.1 Distinguishability before metric structure

The program begins from the claim that **difference is logically prior to a numerical measure of difference**. A distinction can be accredited before one has distance, angle, probability, energy, or even a cardinality assigned to it.

This is not yet a physical statement. It is a dependency rule: one should not use a metric notion to derive the existence of the distinctions that the metric is supposed to measure.

### 2.2 Comparison and residue

A comparison is modeled schematically as

$$
\mathcal C(a,b)=(q,r),
$$

where $q$ denotes the part resolved under the current comparison and $r$ the residue that remains unrepresented by the current architecture.

The residue is not identified with energy, matter, entropy, or noise. It is a formal placeholder for **unabsorbed distinguishability**. If a residue must be preserved and cannot be represented by the current relational degrees of freedom, the architecture must be enlarged.

### 2.3 Recursion, closure, and identity

Products of comparison may themselves become references for later comparison. This recursion introduces an internal order without yet requiring physical time.

Closure is defined more strongly than mere return:

> a structure closes when it can contain and recognize a new self-related image without reducing that image to trivial repetition.

Identity is then interpreted as the capacity to remain internally recognizable under admissible transformations. This makes identity a structural condition rather than a primitive substance.

### 2.4 Conditional order-four realization

One formal realization introduces a generator $J$ satisfying

$$
J^2=-I.
$$

Then

$$
J^4=I,
$$

and the discrete orbit

$$
x,\;Jx,\;-x,\;-Jx,\;x
$$

has order four. This is **not** taken to prove that nature is fundamentally four-fold. It is a conditional realization showing that a minimal algebraic notion of repeated transversal transformation can generate an order-four cycle.

When that discrete cycle is embedded in a continuous one-parameter group,

$$
e^{\theta J}=\cos\theta\,I+\sin\theta\,J,
$$

$2\pi$ appears as the period of the continuous parametrization. Thus the program separates two questions that are often conflated:

- why a discrete closure can have order four;
- why its continuous realization carries a $2\pi$ period.

### 2.5 Rate and operational time

In a quadratic spectral realization,

$$
G=C^\dagger C,
\qquad
\ddot f+\Gamma Gf=0,
$$

and an eigenmode $Gu_i=\lambda_i u_i$ has

$$
\varpi_i^2=\Gamma\lambda_i.
$$

If $R_i=\lambda_i^{-1/2}$, then

$$
R_i|\varpi_i|=\sqrt\Gamma.
$$

This relation is internal to that realization. It motivates an operational reading of time as comparison of rates, but it is not exported universally. In particular, incompressible Navier–Stokes has parabolic scaling, for which a scale-rate invariant has the form $R^2\varpi$, not $R\varpi$.

---

## 3. Neighboring academic perspectives

### 3.1 Relational state: Rovelli's relational quantum mechanics

Carlo Rovelli's relational quantum mechanics (RQM) rejects an observer-independent physical state as a universal primitive and instead treats values of physical quantities as relative to interactions between systems. The important point for the present program is not quantum interpretation itself, but the methodological shift: **state-description becomes relational rather than absolute**.

**[Correspondence]** Both approaches refuse to treat an isolated description as automatically more fundamental than relations among systems.

**[Difference]** RQM begins with the quantum formalism and reinterprets its states and observables relationally. The Relational Geometry Program instead asks whether relation, difference, and comparison can be placed logically before a chosen physical formalism.

**[Research interface]** An academic test would be to ask whether the program's notions of reference, residue, and closure can be represented inside a general operational theory in a way that distinguishes them from ordinary conditional state update.

### 3.2 Relational motion and time: Machian and Barbour–Bertotti approaches

Machian programs and Barbour–Bertotti relational dynamics attempt to formulate motion using only relational quantities rather than absolute space and motion. Modern shape-dynamics research continues this tradition in a more geometric setting.

**[Correspondence]** The present program likewise treats absolute spatial and temporal backgrounds as structures that should not be introduced before relational comparison requires them.

**[Difference]** Barbour-type approaches typically start with a comparatively rich configuration space of relative distances or shapes. The current program places its foundational question earlier: what must be present before distance, shape, or dimension are available at all?

**[Research interface]** The most concrete overlap is time. Rovelli's partial-observable framework and relational dynamics both motivate descriptions in which evolution is expressed as correlation between changing quantities. The program's proposal that operational duration arises from comparing rates belongs near this literature, but requires a precise clock construction before equivalence can be claimed.

### 3.3 Ontic structural realism

Structural realism, especially ontic structural realism (OSR), gives explanatory priority to structure and relations over an ontology of independently constituted objects.

**[Correspondence]** The program's idea that identity can emerge from a sufficiently closed relational architecture is naturally legible within a structuralist vocabulary.

**[Difference]** OSR is primarily a philosophical position about what successful science licenses us to regard as real. The Relational Geometry Program is trying to formulate a generative mechanism: not merely that structure is primary, but how distinguishability, residue, recursive closure, and identity could arise in a dependency order.

**[Research interface]** Philosophers of physics can help sharpen whether "identity by closure" is a substantive criterion or only a re-description of structural individuation already available in structuralist accounts.

### 3.4 Operational and informational reconstructions of physical theory

Hardy and, later, Chiribella–D'Ariano–Perinotti showed that major parts of quantum theory can be reconstructed from comparatively transparent operational or informational principles rather than assumed directly in Hilbert-space form.

**[Correspondence]** The methodological similarity is strong: both programs ask whether familiar formal structures can be recovered from a smaller set of principles and dependency constraints.

**[Difference]** Reconstruction programs normally begin with operational primitives such as systems, transformations, outcomes, distinguishability, and composition. The current program asks whether some of those primitives—especially distinguishability, composition, dimension, and identity—can themselves be staged in a deeper generative order.

**[Research interface]** General probabilistic theories provide a natural testbed. One could attempt to encode comparison, residue, closure, and sectorization in an operational framework and ask whether the resulting axioms select a known theory, define a broader class, or collapse into already familiar operational principles.

### 3.5 Information geometry

Information geometry equips families of probability distributions with differential-geometric structure, including the Fisher–Rao metric and dual affine connections.

**[Correspondence]** It is a mature example of geometry emerging from a notion of distinguishability—specifically statistical distinguishability.

**[Difference]** Information geometry does not derive distinguishability itself, nor does it claim that physical space emerges from statistical distance. Its objects are probability models already endowed with sufficient smooth structure.

**[Research interface]** The program's abstract "comparison" could be tested against divergence functions. If a comparator induces a divergence with suitable convexity and regularity properties, one can ask whether a metric and connection emerge canonically. This would provide a rigorous route from comparison to geometry without assuming Euclidean structure at the start.

### 3.6 Self-reference, diagonalization, and fixed-point mathematics

Lawvere's fixed-point theorem and the broader family of diagonal arguments provide a categorical language for self-reference. They show that under precise representation and evaluation hypotheses, sufficiently expressive self-description forces fixed points.

**[Correspondence]** The program's definition of closure as the capacity of an architecture to contain a self-related image is close enough to this mathematical territory to make category theory an obvious candidate language.

**[Difference]** A fixed point is not automatically an identity-generating closure, and self-reference alone does not imply novelty, sectorization, or physical structure.

**[Research interface]** One of the highest-value formal tasks is to translate the program's closure requirement into a categorical statement involving representation, evaluation, and a nontriviality condition. The result should distinguish:

- trivial fixed points;
- recurrent states;
- genuine self-representation;
- self-representation with irreducible novelty.

If no such distinction can be formalized, the ontological notion of closure remains too weak.

---

## 4. Algebraic interfaces: complex structures, quaternions, and order four

The conditional relation

$$
J^2=-I
$$

places the program in contact with a large and mature mathematical landscape: complex structures, symplectic geometry, Clifford algebras, quaternionic structures, rotations, and spin representations.

The academic opportunity is not to claim novelty for $J^2=-I$ or for quaternionic algebra. Those are standard structures. The question is whether a **minimal closure requirement selects one of them without inserting orthogonality by hand**.

Three distinctions are especially important.

### 4.1 Independence is not orthogonality

A new degree of freedom need not be perpendicular to an old one. Orthogonality requires additional structure: an inner product, symplectic form plus compatibility, normed algebra, or equivalent data.

Therefore the program's route from residue to a new degree of freedom is logically prior to any route from a new degree of freedom to a transverse direction.

### 4.2 Order four is conditional, not numerological

Once $J^2=-I$ is available, order four follows exactly. But the scientific question lies one step earlier: **what generative condition selects such a $J$?**

A convincing theorem would need to show that a minimal nontrivial self-referential closure satisfying explicit economy and nondegeneracy axioms necessarily carries a complex/quaternionic structure, or else state the additional assumptions required.

### 4.3 Continuous periodicity and $\pi$

The appearance of $2\pi$ in $e^{\theta J}$ is mathematically standard once a continuous rotation group has been chosen. The potentially interesting claim is therefore not that $\pi$ is produced ex nihilo, but that a discrete closure and its continuous representation may occupy different logical layers.

This separation suggests a clean academic problem:

> characterize the minimal hypotheses under which a finite closure orbit admits a canonical continuous interpolation, and determine what geometric structure is thereby introduced.

---

## 5. Emergent time: comparison with relational-clock programs

The program's current time proposal can be stated modestly:

> duration is operationally meaningful only as comparison between changes.

If two processes have rates $\varpi_i$ and $\varpi_j$, the primitive comparison is the dimensionless ratio

$$
\frac{\varpi_i}{\varpi_j}.
$$

A dimensional time parameter is introduced only after choosing a reference process.

This is compatible in spirit with relational-clock approaches, partial observables, and generally covariant formulations in which one dynamical variable is used to parameterize another.

However, three problems remain open before the program can claim more:

1. **Clock admissibility:** what makes a process a valid clock rather than merely another changing quantity?
2. **Composition:** how do local rate comparisons synchronize across interacting subsystems?
3. **Relativistic compatibility:** how does the construction reproduce proper time or causal structure where those notions are already experimentally established?

For this reason, the program should present "time as rate comparison" as a research hypothesis and operational framework, not as a replacement for relativistic time.

---

## 6. Navier–Stokes as a technical laboratory

The Navier–Stokes branch is currently the program's strongest contact with a mature PDE problem because it provides exact equations, established geometric criteria, accessible simulations, and adversarial benchmark solutions.

The branch writes

$$
\omega=q\xi,
\qquad
\frac{D_t\omega}{q}=a\xi+b,
$$

with

$$
a=D_t\log q,
\qquad
b=D_t\xi,
\qquad
b\perp\xi.
$$

The exact growth-coordinate evolution law is

$$
\boxed{
P_\xi^\perp\frac{db}{dG}
=
\frac{\mathcal Y_\perp}{a}-b,
}
\qquad
\mathcal Y=D_t\left(\frac{D_t\omega}{q}\right),
\qquad dG=a\,dt.
$$

This equation is useful academically because it converts a broad relational idea into a precise PDE question: **during positive vorticity amplification, what continuously re-accredits transverse change, and what causes it to decay relative to the growing reference direction?**

### 6.1 Vorticity-direction regularity criteria

Constantin–Fefferman and later Beirão da Veiga–Berselli established that geometric coherence or regularity of the vorticity direction can have regularizing consequences for three-dimensional Navier–Stokes.

Recent work by Grujić further isolates the direction equation and emphasizes that strain enters it through the tangential component

$$
P_{\xi^\perp}S\xi,
$$

which is precisely the strain-induced transverse tilting used in the present decomposition.

**Relation to the program:** this literature shows that direction is not decorative geometry; it can enter rigorous regularity mechanisms. The program's contribution, if any, must therefore be more specific than "direction matters." Its candidate contribution is the organization of growth, turning, and reaccreditation in material growth coordinates.

### 6.2 Lagrangian quaternionic dynamics and the pressure Hessian

Gibbon, Holm, Kerr, and Roulstone reformulated Euler vorticity dynamics using a quaternionic tetrad containing the vorticity growth rate and rotation rate. Their Lagrangian equations expose the role of the pressure Hessian in controlling the evolution of direction.

**Relation to the program:** the Euler limit of the present $(a,b,\mathcal Y)$ formulation overlaps directly with this established Lagrangian structure. The correct academic positioning is therefore not that the Euler directional law is new, but that the program embeds a closely related structure into a broader viscous/material diagnostic and interprets it through its own reference–difference language.

This literature also identifies the pressure Hessian as a natural place to look for a nonlocal mechanism capable of opposing the local collapse of transverse turning.

### 6.3 Viscous tilting

Holzner and collaborators demonstrated experimentally and numerically that viscosity can locally reorient vorticity, not merely dissipate its magnitude.

**Relation to the program:** this directly supports the need to compute the PDE residual

$$
r_\perp^{\mathrm{PDE}}
=
P_\xi^\perp\frac{\nu\Delta\omega+\nabla\times f}{q}
$$

independently. Any claim of strain–viscous compensation must be based on this independently evaluated quantity, not on a residual reconstructed by subtraction.

### 6.4 Twist and anti-twist during amplification

Buaria, Lawson, and Wilczek report that vorticity amplification is accompanied by increasing twisting of vortex lines followed by an anti-twist associated with arrest of growth in their studied configurations.

**Relation to the program:** this is a strong empirical/theoretical neighbor of the "exit from a low-turning channel" question. The two descriptions are not identical: vortex-line twist is a spatial geometric quantity, whereas $b=D_t\xi$ is a material directional rate. A valuable project is to compute both on the same trajectories and test whether one predicts the other.

### 6.5 Burgers vortex as an exact NO-GO benchmark

The Burgers vortex provides an exact regular configuration with perfectly aligned vorticity direction and positive amplification along appropriate trajectories. In the program's language it shows that small transverse turning, even identically zero turning, is not by itself a signature of singular behavior.

**Consequence:** any useful criterion must combine directional information with scale, relative amplitude, domain/energy assumptions, or another dimensionless discriminator.

### 6.6 Restricted Euler as a model benchmark

The restricted Euler system deletes the anisotropic pressure-Hessian and viscous/nonlocal terms from the local velocity-gradient dynamics. It is known to develop finite-time singular behavior for broad initial conditions.

In the repository's benchmark, the model collapses strongly toward the low-turning channel. This does not prove anything about full Navier–Stokes, but it sharpens the mechanism question:

> what terms absent from restricted Euler prevent the same collapse in the full equation?

The pressure Hessian and viscous directional terms become immediate candidates.

### 6.7 External forced-blowup construction

As of September 2026, OpenAI has publicly released a manuscript and Lean formalization claiming finite-time blowup for the forced three-dimensional incompressible Navier–Stokes equations. Independent evaluation is ongoing. The repository uses this construction only as an **external adversarial benchmark**.

The relevant question for the program is not whether the external proof is "the same idea." It is whether the program's observables—growth, turning, pressure-Hessian contribution, viscous/forcing contribution, and scale-rate behavior—can classify the explicit mechanism of the construction without post hoc adjustment.

That provides a high-quality falsification test.

---

## 7. A comparison matrix for specialists

| Program concept | Established neighboring concept | Genuine overlap | Important difference | Concrete test |
|---|---|---|---|---|
| Difference before metric | operational distinguishability; structural relations | distinguishability can precede a chosen geometry | most operational theories already assume systems/outcomes | formalize comparator in GPT or category framework |
| Residue | complement, defect, unresolved mode | tracks information not represented in current substructure | not yet tied to a canonical algebraic quotient | derive a universal closure/sufficiency criterion |
| Closure by self-representation | fixed points, recursion, categorical self-reference | self-description can be formalized abstractly | fixed point alone does not imply novelty or identity | construct nontrivial closure theorem with novelty condition |
| Identity as invariant closure | structural individuation; symmetry orbit | identity linked to preserved invariants | program requires generative emergence of invariants | classify transformations preserving closure class |
| $J^2=-I$ and order four | complex/quaternionic structures | exact algebraic match | selection of $J$ is not derived | prove or falsify necessity from minimal closure axioms |
| Continuous $2\pi$ cycle | one-parameter rotation groups | exact once continuous complex structure exists | does not derive $\pi$ from the discrete count | characterize canonical interpolation conditions |
| Time as rate comparison | relational clocks; partial observables | evolution expressed by correlations | no clock admissibility theorem yet | recover proper/operational time in known models |
| NS material direction $b$ | vorticity-direction dynamics | exact overlap in directional variable | relational interpretation adds no theorem by itself | derive a new bound or classifier using full PDE terms |
| Transverse reaccreditation | pressure-Hessian/viscous reorientation | exact PDE terms can sustain turning | "information" language must map quantitatively | compute signed contributions on DNS and benchmarks |
| Sectorization | superselection, dynamical phases, orbit classes | discrete classes may arise from invariant structure | no equivalence currently established | derive disconnected closure classes from explicit axioms |

---

## 8. What would count as a substantive academic contribution?

The program will become more than a reinterpretive vocabulary only if at least one of the following succeeds.

### 8.1 A closure theorem

Derive, from a minimal and clearly stated category of relational structures, a nontrivial criterion under which residue forces enlargement and recursion yields self-representational closure.

A strong result would separate return, fixed point, consistency, and identity-generating closure.

### 8.2 A necessity theorem for the order-four structure

Show that explicit minimal assumptions imply a complex or quaternionic generator with $J^2=-I$, rather than choosing that algebra because it realizes the desired cycle.

Failure would also be informative: it would demote order four from a structural necessity to one realization among many.

### 8.3 A canonical route from comparison to geometry

Construct a divergence, norm, or other comparator-induced object from which a metric or geometric structure follows canonically. Information geometry offers mature tools for judging whether such a route is substantive.

### 8.4 A clock theorem

Define admissible rate comparisons and prove when they generate a consistent temporal ordering and synchronization across subsystems.

### 8.5 A Navier–Stokes discriminator

Produce a quantity or inequality that distinguishes known regular and singular/model trajectories using independently computed PDE terms, and that is not merely an algebraic repackaging of already measured variables.

This is currently the most experimentally accessible route.

---

## 9. Suggested collaboration interfaces

For a **mathematician in category theory or algebra**, the key question is whether closure, residue, and self-recognition can be formalized without importing the geometry they are meant to generate.

For a **mathematical physicist working on foundations**, the natural comparison is with operational reconstructions and relational observables: which primitives can genuinely be removed, and which reappear implicitly?

For a **geometer or information theorist**, the problem is whether comparison induces a canonical divergence/metric and whether "new dimension" can be defined by rank, information capacity, or another invariant criterion.

For a **fluid dynamicist**, the concrete work is immediate: evaluate the material decomposition using instantaneous PDE terms, pressure Hessian, viscous tilting, and vortex-line geometry on the same trajectories and benchmarks.

For a **PDE analyst**, the decisive question is whether the growth-coordinate transverse law can generate a nontrivial estimate. Without such an estimate, the NS branch remains a diagnostic framework rather than a regularity mechanism.

---

## 10. Deliberate non-identifications

For clarity, the repository does not presently identify:

- relational closure with a quantum state;
- residue with entropy or energy;
- self-reference with consciousness;
- the order-four algebra with spacetime dimension;
- $2\pi$ periodicity with a derivation of physical $\pi$;
- the spectral radius $R_i$ with a physical particle radius;
- a relational rate with the speed of light in incompressible flow;
- low material turning with regularity;
- a vortex with a particle;
- a benchmark blowup mechanism with the program's ontology.

These non-identifications are not rhetorical caution. They define the places where actual derivations are still required.

---

## 11. Research program in one academic paragraph

The Relational Geometry Program can be viewed as an attempt to construct a dependency-respecting theory of distinguishability: relations generate comparisons; comparisons may leave irreducible residue; persistent residue motivates enlargement of representational capacity; recursion permits self-reference; sufficiently nontrivial self-reference may define closure and identity; algebraic realizations then test whether dimensionality, orientation, periodicity, and rate relations can emerge without being presupposed. Established relational, operational, structural, categorical, and information-geometric frameworks provide natural mathematical comparison classes. Navier–Stokes provides a physical laboratory in which the abstract language becomes testable through exact material equations for vorticity growth and reorientation. The program's scientific value therefore depends not on verbal similarity to these neighboring theories but on whether it can produce necessary theorems, new invariants, discriminating bounds, or successful falsifiable bridges.

---

## References and comparison sources

### Relational and structural perspectives

1. C. Rovelli, **Relational Quantum Mechanics**, *International Journal of Theoretical Physics* 35 (1996), 1637–1678. arXiv:quant-ph/9609002.
2. C. Rovelli, **Partial observables**, *Physical Review D* 65 (2002), 124013. DOI: 10.1103/PhysRevD.65.124013.
3. J. B. Barbour and B. Bertotti, **Mach's Principle and the Structure of Dynamical Theories**, *Proceedings of the Royal Society A* 382 (1982), 295–306.
4. J. Ladyman and D. Ross, *Every Thing Must Go: Metaphysics Naturalized*, Oxford University Press, 2007. See also the Stanford Encyclopedia of Philosophy entry **Structural Realism** for an overview of the debate.

### Operational and informational reconstruction

5. L. Hardy, **Quantum Theory From Five Reasonable Axioms**, arXiv:quant-ph/0101012 (2001).
6. G. Chiribella, G. M. D'Ariano, and P. Perinotti, **Informational derivation of quantum theory**, *Physical Review A* 84 (2011), 012311. DOI: 10.1103/PhysRevA.84.012311.
7. G. Chiribella, G. M. D'Ariano, and P. Perinotti, **Probabilistic theories with purification**, *Physical Review A* 81 (2010), 062348. DOI: 10.1103/PhysRevA.81.062348.

### Self-reference and information geometry

8. F. W. Lawvere, **Diagonal arguments and cartesian closed categories**, in *Category Theory, Homology Theory and Their Applications II*, Lecture Notes in Mathematics 92, Springer, 1969.
9. F. Nielsen, **An Elementary Introduction to Information Geometry**, *Entropy* 22 (2020), 1100. DOI: 10.3390/e22101100.
10. S.-I. Amari, **Information Geometry**, *International Statistical Review* 89 (2021), 250–273. DOI: 10.1111/insr.12464.

### Vorticity geometry and Navier–Stokes

11. P. Constantin and C. Fefferman, **Direction of vorticity and the problem of global regularity for the Navier–Stokes equations**, *Indiana University Mathematics Journal* 42 (1993), 775–789. DOI: 10.1512/iumj.1993.42.42034.
12. H. Beirão da Veiga and L. C. Berselli, **On the regularizing effect of the vorticity direction in incompressible viscous flows**, *Differential and Integral Equations* 15 (2002), 345–356. DOI: 10.57262/die/1356060864.
13. J. D. Gibbon, D. D. Holm, R. M. Kerr, and I. Roulstone, **Quaternions and particle dynamics in the Euler fluid equations**, *Nonlinearity* 19 (2006), 1969–1983. DOI: 10.1088/0951-7715/19/8/011.
14. M. Holzner, M. Guala, B. Lüthi, A. Liberzon, N. Nikitin, W. Kinzelbach, and A. Tsinober, **Viscous tilting and production of vorticity in homogeneous turbulence**, *Physics of Fluids* 22 (2010), 061701. DOI: 10.1063/1.3442477.
15. D. Buaria, J. M. Lawson, and M. Wilczek, **Twisting vortex lines regularize Navier–Stokes turbulence**, *Science Advances* 10 (2024), eado1969. DOI: 10.1126/sciadv.ado1969.
16. B. J. Cantwell, **Exact solution of a restricted Euler equation for the velocity-gradient tensor**, *Physics of Fluids A* 4 (1992), 782–793.
17. K. Ohkitani, **A Survey on a Class of Exact Solutions of the Navier–Stokes Equations and a Model for Turbulence**, *Publ. RIMS* 40 (2004), 1267–1290. DOI: 10.2977/PRIMS/1145475447.
18. Z. Grujić, **On Decay of the Local Mean Oscillations of the Vorticity Direction in Critical Navier–Stokes Flows**, arXiv:2609.05720 (2026).

### External adversarial benchmark

19. OpenAI, **Finite Time Blowup for Navier–Stokes**, public manuscript and associated Lean formalization, September 2026. The repository treats this as an announced external result under ongoing independent evaluation and uses it only as an adversarial benchmark.

---

## Repository cross-links

- Conceptual core: [`relational_geometry_core.es.md`](relational_geometry_core.es.md)
- Formal comparator: [`../02_formal_core/comparator_and_residue.md`](../02_formal_core/comparator_and_residue.md)
- Order-four realization: [`../02_formal_core/order_four_operator.md`](../02_formal_core/order_four_operator.md)
- Second-order dynamics: [`../02_formal_core/second_order_dynamics.md`](../02_formal_core/second_order_dynamics.md)
- Navier–Stokes manuscript: [`../03_navier_stokes/manuscript.md`](../03_navier_stokes/manuscript.md)
- Results register: [`../04_results/RESULTS_REGISTER.md`](../04_results/RESULTS_REGISTER.md)
- NO-GO register: [`../04_results/NO_GO_REGISTER.md`](../04_results/NO_GO_REGISTER.md)
- Open problems: [`../04_results/OPEN_PROBLEMS.md`](../04_results/OPEN_PROBLEMS.md)
