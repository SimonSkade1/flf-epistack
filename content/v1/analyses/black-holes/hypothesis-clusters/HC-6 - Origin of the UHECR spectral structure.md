---
id: HC-6
type: hypothesis-cluster
question: "What produces the observed structure — ankle, instep, and suppression — of the ultra-high-energy cosmic-ray spectrum?"
hypotheses:
  - "[[H-9 - The UHECR ankle and suppression are caused by GZK interactions of extragalactic protons with the CMB]]"
  - "[[H-12 - The instep and steepening reflect overlapping helium and CNO flux components with a narrow source rigidity maximum, not a few foreground sources]]"
  - "[[H-21 - The dip near 10^18.5 eV marks a transition from heavy Galactic to light extragalactic cosmic rays]]"
  - "[[H-37 - The UHECR spectral structure arises from something not listed here]]"
exclusivity: "Each member attributes the same spectral structure to a different dominant source-composition and propagation account; at most one account dominates."
exhaustive_by_construction: false
independence: "The origin of the cosmic-ray spectrum is source astrophysics, factorizing from collider microphysics and from every other cluster's base rate."
depends_on: []
relevance: "The cosmic-ray leg of the safety argument needs the above-LHC-energy flux to be real, sustained, and of known composition; these members fix what that flux is and what it is made of."
---
![[H-9 - The UHECR ankle and suppression are caused by GZK interactions of extragalactic protons with the CMB]]
![[H-12 - The instep and steepening reflect overlapping helium and CNO flux components with a narrow source rigidity maximum, not a few foreground sources]]
![[H-21 - The dip near 10^18.5 eV marks a transition from heavy Galactic to light extragalactic cosmic rays]]
![[H-37 - The UHECR spectral structure arises from something not listed here]]

One sub-question — what account of sources, composition, and propagation generates the measured spectral features — with three competing answers spanning three decades of the field: proton-dominated extragalactic flux shaped by pair-production and GZK losses; a galactic-heavy-to-extragalactic-light transition at the dip; and a mixed helium/CNO composition with a narrow source rigidity maximum on which the steepening is a source property rather than a propagation cutoff. These disagree about the composition and cause of the same features, so at most one dominates; the residual covers instrumental or exotic accounts. The spectrum, declination-independence, elongation-rate, and cutoff-shape observations are what pull the members apart.

## Prior

```python
# HC-6 prior — origin of the UHECR spectral structure (ankle, instep, suppression). Members in
# HC-6.hypotheses order: [H-9 GZK extragalactic-proton propagation, H-12 He/CNO mass components with a
# narrow source rigidity maximum, H-21 heavy-Galactic-to-light-extragalactic transition at the dip,
# H-37 residual]. Outside view only: `no_observation_arguments.py --cluster HC-6` returns none, and all
# eight inbound E edges (E-6..E-9, E-14..E-17, grouped CG-2/3/4/5) are per-instrument spectrum
# measurements that discriminate between these accounts — case-specific, so all are left unmarked for
# step 8 and none are used_for_prior here. Reference class: multi-decade debates over the dominant cause
# of a UHE cosmic-ray spectral feature, where a textbook parameter-insensitive propagation mechanism
# competes with more heavily parameterised source/composition refinements.

# H-9 GZK extragalactic-proton account — the anchor. For H-9 to dominate, the suppression and dip must be
# propagation features of a predominantly protonic extragalactic flux on the CMB. It is the oldest account
# (GZK predicted 1966) and the most parameter-insensitive (the E_1/2 test does not depend on the source
# spectral index), so within the reference class it is the default textbook expectation; take it as the
# unit weight. Does not cover the possibility that the highest-energy composition is heavy. Highest prior
# confidence, but only narrowly ahead of H-12.
w_gzk = 1.0

# H-12 He/CNO mass-component account — the modern source/composition refinement. For H-12 to dominate, the
# instep and steepening must be a source property (a narrow maximum rigidity across a numerous population
# emitting rather pure mass groups), not propagation. It is a genuine front-runner in the current field,
# but requires more to be true — a specific narrow source rigidity maximum and a particular He/CNO mixing —
# so more free parameters and more ways to be wrong than the propagation account; price it just below par
# a priori. Does not cover a few-foreground-source origin of the instep (that is a residual branch).
odds_composition_vs_gzk = 0.85   # competitive front-runner, penalised for extra model parameters vs GZK
w_composition = odds_composition_vs_gzk * w_gzk

# H-21 Galactic-to-extragalactic transition at the ~10^18.5 eV dip — for this to dominate, the flux below
# the dip must be mostly Galactic iron and the dip itself the crossover to a light extragalactic component.
# A coherent but now-minority school: most current placements of the Galactic/extragalactic transition sit
# elsewhere, the high-energy composition is not cleanly light-protonic, and its pair-production dip overlaps
# what H-9 already explains, leaving little that is distinctively its own. Downweight against both
# front-runners. Does not cover a purely extragalactic light flux across the whole range.
odds_transition_vs_gzk = 0.4     # minority interpretation of the dominant account, downweighted vs H-9/H-12
w_transition = odds_transition_vs_gzk * w_gzk

# H-37 residual — the structure's dominant cause is none of the three: a shared cross-experiment
# energy-scale artifact, an exotic top-down source population, or a propagation effect not proposed here.
# Weighted by how often, for a spectral structure confirmed by several independent techniques and
# hemispheres, the eventual dominant account falls outside a menu spanning propagation, source/composition,
# and Galactic-transition physics — uncommon, since the listed members cover the mainstream space well, but
# not negligible for a prior. Its own argued weight, not a leftover (rule 4).
w_residual = 0.25                # ~0.25:1 vs H-9; ~10% of the mass once normalised

prior("HC-6", [w_gzk, w_composition, w_transition, w_residual])
```
