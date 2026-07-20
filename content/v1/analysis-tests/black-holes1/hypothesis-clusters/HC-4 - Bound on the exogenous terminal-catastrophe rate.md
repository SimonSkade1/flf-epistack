---
type: hypothesis-cluster
id: HC-4
hypotheses:
  - "[[H-5 - The exogenous terminal-catastrophe rate is below about 1 per Gyr at 99.9 percent confidence]]"
  - "[[H-10 - The exogenous terminal-catastrophe rate is not bounded below 1 per Gyr]]"
exclusivity: "The Tegmark-Bostrom bound either holds at the stated confidence or it does not."
exhaustive_by_construction: true
independence: "An empirical bound from planet-formation-time statistics; its truth does not shift the base rates of the gravity-scale, evaporation, or accretion questions (and it covers exogenous events only, not anthropogenic collider operation)."
depends_on: []
question: "Is the exogenous terminal-catastrophe rate bounded below ~1 per Gyr at high confidence?"
relevance: "Backstop leg of the safety case: bounds nature-triggered analogues of collider catastrophes, but only exogenous ones — it does not directly bound risks whose rate humans change."
---
![[H-5 - The exogenous terminal-catastrophe rate is below about 1 per Gyr at 99.9 percent confidence]]
![[H-10 - The exogenous terminal-catastrophe rate is not bounded below 1 per Gyr]]

Exhaustive by construction: H-10 is the logical negation of H-5. Failure mode of the analysis: the planet-formation-time distribution model underlying the bound could be wrong — that failure would favour H-10.

## Prior

```python
# HC-4 prior — does the Tegmark-Bostrom exogenous-catastrophe bound hold? Members in HC-4.hypotheses
# order: [H-5 bound holds (<~1/Gyr at 99.9%), H-10 not so bounded]. Exhaustive by construction
# (H-10 = ¬H-5), so no residual member (rule 4 does not apply).
# Evidence partition: the cluster's single inbound edge, [[E-6 - O-10 × HC-4 — Earth's formation date is
# typical, not early]], carries the case-specific discriminating datum (Earth's actual typicality within
# the formation-time distribution) — that is exactly what step 8 must price, so it is left UNMARKED and
# nothing here is marked used_for_prior. The prior instead prices the validity of the bound's modeling
# hinges, i.e. P(a T-B-style typicality inference is sound), before conditioning on the datum itself.
# No-observation argument [[A-6 - Observer selection makes naive survival-based risk bounds uninformative]]
# (corrected/checked, rule 6): its corrected statement kills naive survival-based bounds for bodies whose
# survival is a precondition for our existence, but explicitly exempts comparisons among surviving
# observers — the formation-time method's whole design. So A-6 removes the anthropic defeater as a
# failure mode here rather than adding a discount; it is why no extra "anthropic-error" factor appears.

# H-5 — the bound holds at the stated confidence. True iff all three hinges named on the node hold:
# the adopted planet-formation-time distribution, uncorrelatedness of the catastrophe process, and the
# statistical derivation. Reference class: published astrophysical-statistics bounds resting on a
# semi-empirical population model. Not covered: whether the datum itself is typical (step 8's job).
# Confidence: moderate — the product is deliberately near even odds because the 99.9%-c.l. claim leans
# on distribution tails that the population model constrains only loosely.
# Habitable-planet formation-history models (Lineweaver-type) agree on the broad shape (formation spread
# over many Gyr, peak well before Earth), which the typicality test mainly needs; but a 99.9% claim also
# uses tail behaviour, where such models are weakly constrained — hence well below 1 but above a coin flip.
p_dist_model = 0.7
# Exogenous candidates (nearby GRB/supernova, local bubble nucleation) are plausibly Poisson-like in
# space-time, which the derivation needs; correlated mechanisms (light-cone-spanning vacuum decay) only
# partly fit, though T-B treat the light-cone case separately — so a modest discount, not a large one.
p_uncorrelated = 0.8
# The derivation is a short exponential-tilt/typicality computation with little room for technical error
# in a peer-reviewed Nature paper; residual chance of a subtle statistical mistake.
p_derivation = 0.9
w_H5 = p_dist_model * p_uncorrelated * p_derivation

# H-10 — logical negation of H-5: the bound fails if ANY hinge above fails. As the complement of a single
# estimated probability this is an arithmetic identity (rule 1), not a residual (the cluster is
# exhaustive_by_construction). Concretely: a wrong formation-time model is the dominant route in, per the
# failure mode named on this cluster.
w_H10 = 1 - w_H5

prior("HC-4", [w_H5, w_H10])
```
