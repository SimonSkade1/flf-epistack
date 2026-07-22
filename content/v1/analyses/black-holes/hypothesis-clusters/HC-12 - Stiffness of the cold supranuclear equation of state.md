---
id: HC-12
type: hypothesis-cluster
question: "What is the equation of state of cold matter at supranuclear densities?"
hypotheses:
  - "[[H-1 - Neutron-star matter has a stiff equation of state - no hyperons, bosons, or free quarks near nuclear saturation density]]"
  - "[[H-44 - The cold supranuclear equation of state is softened by exotic degrees of freedom]]"
exclusivity: "The equation of state is either stiff enough to support the most massive observed neutron stars without exotic softening or it is not; the members are a claim and its negation."
exhaustive_by_construction: true
independence: "Dense-matter QCD factorizes from the gravity-scale, monopole, and vacuum questions."
depends_on:
  - "HC-13: the neutron-star mass inferences anchoring stiffness assume general-relativistic orbital dynamics; if general relativity failed in the strong field the constraint would shift"
relevance: "Neutron-star structure underlies the neutron-star-survival leg of the cosmic-ray safety argument for both the black-hole and strangelet branches."
---
![[H-1 - Neutron-star matter has a stiff equation of state - no hyperons, bosons, or free quarks near nuclear saturation density]]
![[H-44 - The cold supranuclear equation of state is softened by exotic degrees of freedom]]

Stiff against softened for the same material. Exhaustive by construction: proposition and logical complement. A failure of the analysis — the mass measurements sharing a systematic (inclination, companion modeling) — would remove the stiffness anchor and favour the second member, which is the field's prior expectation from exotic phases.

## Prior

```python
# HC-12 prior — stiffness of the cold supranuclear EOS. Members in HC-12.hypotheses order:
# [H-1 stiff (no exotic softening, supports >=1.97 Msun), H-44 softened by exotic degrees of freedom].
# exhaustive_by_construction (step 4): the two members are a proposition and its exact logical
# complement, so there is NO residual member — rule 4 does not apply, and the softened weight below is
# the exact complementary credence of the stiff one (a correct binary identity, not a rescaling artifact).
#
# Outside view / reference class (process step 2): the population of published cold-supranuclear EOS
# models in the pre-2010 literature — deliberately taken BEFORE the two-solar-mass pulsar measurements,
# which are this cluster's case-specific discriminating evidence and are priced at step 8, not here
# (E-18 = O-1 Shapiro delay; CG-9 = E-19/E-21 = O-18/O-19 second pulsar + orbital decay). None of those
# three edges is marked used_for_prior: they discriminate, they are not base rates. The helper reports no
# no-observation arguments for HC-12 (`no_observation_arguments.py . --cluster HC-12` -> none), and the
# graph holds no base-rate observation node for this cluster, so the reference-class facts enter as
# looked-up named variables (rule 8), not as marked edges.
#
# depends_on HC-13 (rule 3, noted not repaired): the pulsar masses that would later move this cluster are
# inferred assuming general-relativistic strong-field orbital dynamics; if GR failed in the strong field
# (HC-13's softened member) the stiffness inference would shift. That is a cross-cluster dependence in the
# CASE evidence (step 8), not in this outside-view prior, so it does not enter the weights here — recorded
# in prose only, HC-13 is not imported.

# H-1 stiff — priced as a credence Fermi-decomposed over the pre-2010 model population. For this member
# to be right, dense-matter QCD must reach ~2 Msun without exotic softening: either exotics never switch
# on at neutron-star densities, or they do but residual repulsion keeps the EOS hard. This was the
# MINORITY expectation pre-2010 (the "hyperon puzzle" ran the other way), so H-1 takes the smaller share;
# I am moderately confident in the ordering (stiff < softened) and only weakly confident in the exact split.
p_exotics_onset = 0.75      # hyperon puzzle: near 2-3x nuclear saturation the neutron chemical potential
                            # exceeds the Lambda/Sigma masses, so hyperons (and kaon/quark phases) were
                            # generically expected to switch on and soften the EOS — the pre-2010 default
                            # (hyperonic models then typically gave Mmax ~< 1.5 Msun; PRL 114,092301 & refs)
p_stiff_if_exotic = 0.25    # even once exotics appear, repulsive hyperon-nucleon and three-body forces can
                            # hold Mmax >= 1.97; only a minority of pre-2010 hyperonic/quark models managed it
p_stiff_if_nucleonic = 0.85 # absent exotics, a purely nucleonic EOS almost always reaches ~2 Msun; the small
                            # deficit covers the softest nucleonic parametrizations
p_stiff = (1 - p_exotics_onset) * p_stiff_if_nucleonic + p_exotics_onset * p_stiff_if_exotic
w_stiff = p_stiff           # H-1

# H-44 softened — the field's prior expectation from exotic phases, and the anchor of the reference class:
# for it to be right, hyperons, a kaon/boson condensate, or deconfined quark matter appear at a few times
# saturation density and pull the maximum mass below the most massive observed neutron stars. Because the
# cluster is an exhaustive binary (H-44 == not-H-1), its weight is the exact complementary credence of the
# stiff branch above — the correct identity for a proposition and its negation, not a residual complement.
# I hold this as slightly the more likely member a priori, matching the pre-2010 hyperon-puzzle consensus.
w_softened = 1 - p_stiff    # H-44

prior("HC-12", [w_stiff, w_softened])
```
