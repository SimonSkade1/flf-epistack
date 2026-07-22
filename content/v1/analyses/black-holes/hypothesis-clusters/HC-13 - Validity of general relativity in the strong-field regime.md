---
id: HC-13
type: hypothesis-cluster
question: "Does general relativity correctly describe gravity in the strong-field regime of massive neutron stars?"
hypotheses:
  - "[[H-13 - General relativity correctly describes gravity and gravitational radiation even in the strong-field regime of a 2-solar-mass neutron star]]"
  - "[[H-45 - General relativity fails in the strong-field regime of massive neutron stars]]"
exclusivity: "Either general relativity remains accurate at these binding energies or significant deviations appear; the members are a claim and its negation."
exhaustive_by_construction: true
independence: "Strong-field gravitation at stellar scales factorizes from the short-distance quantum-gravity clusters to the accuracy any member needs — the proposed short-distance modifications leave stellar-scale dynamics untouched."
depends_on: []
relevance: "The astrophysical safety arguments read neutron-star survival through general-relativistic models; their evidential force presupposes this cluster's first member."
---
![[H-13 - General relativity correctly describes gravity and gravitational radiation even in the strong-field regime of a 2-solar-mass neutron star]]
![[H-45 - General relativity fails in the strong-field regime of massive neutron stars]]

Validity against deviation in the regime the safety arguments use. Exhaustive by construction: proposition and logical complement. A failure of the analysis — e.g. the orbital-decay test being insensitive to the particular deviation realized in nature — would favour the second member.

## Prior

```python
# HC-13 prior — validity of general relativity in the strong-field regime of massive neutron stars.
# Members in HC-13.hypotheses order: [H-13 GR valid, H-45 GR fails].
# exhaustive_by_construction: true -> no residual member (rule 4 does not apply). The two members are a
# proposition and its negation, so I estimate the deviation probability p_fail directly from the outside
# view and take p_valid = 1 - p_fail as an arithmetic identity (rule 1), not a residual complement.
# no_observation_arguments.py --cluster HC-13 returns none, so no argument reasoning enters here.
# The one inbound evidence-link, E-13 (PSR J0348+0432 orbital decay vs the GR prediction), is the
# case-specific discriminating measurement of THIS system — not a reference-class rate — so it is left
# unmarked for step 8. The prior therefore rests on the outside view alone.

# H-13 GR valid is the anchor and near-certain a priori; H-45 GR fails carries the small but real mass that
# a genuinely new regime deserves. What would have to be true for H-45: a long-range extra field
# (scalarization, dipolar radiation) switches on at massive-neutron-star binding energies. What the prior
# does NOT yet cover: the actual PSR J0348+0432 decay ratio, folded in at step 8. Confidence: strongly
# favouring H-13, but deliberately not crushing H-45 to zero given the regime is newly probed here.

# OUTSIDE VIEW — reference class: each previously untested regime into which GR was pushed and then held.
# Broadly independent regimes GR passed before this one: solar-system perihelion precession, light bending,
# gravitational redshift, Shapiro delay, frame-dragging (Gravity Probe B / LAGEOS), the Hulse-Taylor
# weak-field radiative test, the LIGO dynamical strong-field merger regime, and the EHT near-horizon
# black-hole-shadow regime. Counted conservatively as broadly independent successes.
k_regimes_passed = 8   # ~8 broadly independent prior regimes in which GR was newly tested and not falsified

# Laplace rule of succession: after k successes in k trials, the chance the next trial is the first failure
# is 1/(k+2). This is the base rate for "GR first fails in the next new regime probed" if strong-field NS
# gravity were just one more draw from the same urn as the earlier regimes.
p_fail_base = 1 / (k_regimes_passed + 2)   # ~0.10

# ADJUSTMENT — this regime is not a random draw. Scalar-tensor gravity predicts spontaneous scalarization
# can switch on precisely at the binding energies of massive neutron stars, and quantum-gravity / dark-energy
# motivations for a long-range extra field target exactly this scale: a specific theoretical prior that
# "if GR breaks anywhere accessible, here is a favoured place." That raises failure odds above the flat base
# rate. It would be 1 if this regime carried no extra theoretical reason to deviate.
theory_uplift = 1.6   # deviation channels (scalarization, dipolar radiation) are specifically motivated at this scale
p_fail = p_fail_base * theory_uplift   # ~0.16, the prior chance GR fails in the massive-NS strong field

w_valid = 1 - p_fail   # H-13 — arithmetic complement of the estimated deviation probability, not a residual
w_fails = p_fail       # H-45 — the constructed deviation member, priced directly by the outside view above

prior("HC-13", [w_valid, w_fails])
```
