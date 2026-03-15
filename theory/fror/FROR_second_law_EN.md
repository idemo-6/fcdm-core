# FROR / Λ‑Phy

## Second Law of Thermodynamics (Computational Formulation)

### Final draft

------------------------------------------------------------------------

# 1. Computational ontology

The universe is modeled as a single closed λ‑term.

**PrimeMover** --- a closed λ‑term representing the total system.

Dynamics are defined as a sequence of β‑reductions.

PrimeMover →β M₁ →β M₂ →β ...

Let

Σ --- total number of β steps executed.

Σ can be interpreted as the **absolute computational age of the
universe**.

------------------------------------------------------------------------

# 2. Reachable state space

Define

Ω(Σ)

as the number of distinct λ‑terms reachable from the PrimeMover after
exactly Σ β‑reductions **along physically realizable trajectories**.

Physically realizable means:

-   executable by an observer with finite memory
-   executable with polynomially bounded computational resources

Thus Ω(Σ) is not the full λ‑calculus reachability set, but the subset
consistent with physical resource constraints.

------------------------------------------------------------------------

# 3. Defect entropy

Define **defect entropy**:

S_defect(Σ) = ln Ω(Σ)

This is the computational analogue of thermodynamic entropy.

It measures the logarithm of the number of physically reachable
computational states.

------------------------------------------------------------------------

# 4. Energetic constraint

Each β‑reduction or information erasure requires energy according to the
Landauer principle:

E ≥ k_B T ln 2

Thus each computational step has a non‑zero physical cost.

------------------------------------------------------------------------

# 5. Theorem (Second Law of Thermodynamics)

For any closed subsystem of the PrimeMover and any physically realizable
sequence of β‑reductions:

ΔS_defect ≥ 0

Equality is possible only for reversible computations that:

-   store the complete reduction history
-   require memory and computation polynomial in Σ.

------------------------------------------------------------------------

# 6. Proof sketch

1.  At step Σ → Σ+1 the system transitions to a neighboring λ‑term.
2.  Returning to the exact previous state requires choosing the unique
    inverse path among all outgoing β edges.
3.  Typical λ‑terms have multiple β‑redexes; the branching factor is
    statistically \> 1.
4.  Without stored history, identifying the correct inverse path
    requires exponential search.
5.  Exponential search implies exponential Landauer cost, which is
    physically infeasible for systems with finite resources.

Therefore physically realizable processes follow trajectories for which

Ω(Σ+1) ≥ Ω(Σ)

which implies

ΔS_defect ≥ 0.

------------------------------------------------------------------------

# 7. Observer model

Define an observer as

O = (M_O, Σ_O, π_O)

where

M_O --- finite memory

Σ_O --- available computational budget

π_O --- coarse‑graining strategy.

------------------------------------------------------------------------

# 8. Observation and symmetry breaking

Consider N alternative β‑trajectories from a state M:

paths(M) = {p₁, p₂, ..., p_N}

If the observer memory is limited:

K = \|states(M_O)\| \< N

then the observer cannot distinguish all trajectories.

The coarse‑graining map

π_O : {p₁ ... p_N} → {P₁ ... P_K}

collapses multiple trajectories into equivalence classes.

Observation corresponds to recording one class P\*.

This breaks symmetry between the alternative trajectories.

------------------------------------------------------------------------

# 9. Emergence of irreversibility

Reversing the observation requires either:

-   erasing stored information (Landauer cost)
-   reconstructing discarded trajectories (exponential search)

Both operations are physically inequivalent to the original state.

Thus observation creates effective irreversibility.

------------------------------------------------------------------------

# 10. Consequences

### Arrow of time

Observation → symmetry breaking → irreversible update.

### Entropy growth

For physically realizable processes

ΔS_defect ≥ 0.

### Resource dependence

The second law arises from **finite computational resources**, not from
statistical assumptions alone.

------------------------------------------------------------------------

# 11. Relation to FROR

In FROR notation:

τ = Σ c(σ_t , σ\_{t+1})

where

τ --- accumulated cost of irreversible distinctions.

Thus

τ ∝ S_defect

Time and entropy correspond to the accumulated cost of irreversible
informational events.

------------------------------------------------------------------------

# 12. Summary

The second law of thermodynamics emerges as a consequence of:

-   branching computational trajectories
-   finite memory of observers
-   energetic cost of information processing.

Any physical system with finite resources necessarily exhibits
non‑decreasing defect entropy.
