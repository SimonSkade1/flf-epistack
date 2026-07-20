---
type: hypothesis-cluster
id: HC-1
hypotheses:
  - "[[H-1 - Habitual whole-egg intake raises atherogenic LDL-ApoB and thereby CVD risk]]"
  - "[[H-5 - Poor bioavailability of egg cholesterol explains its weak effect on plasma cholesterol]]"
  - "[[H-8 - Dietary cholesterol's effect on serum cholesterol is real but saturating, small at high habitual intakes]]"
  - "[[H-11 - Egg's effect on atherogenic blood lipids is characterized in some way not listed above]]"
exclusivity: "The members answer one dimension - how large egg / dietary-cholesterol's effect on atherogenic blood lipids is - so at most one characterization dominates: a large, CVD-relevant ApoB rise (H-1) vs a small rise that saturates at high intake (H-8) vs a small rise because egg-matrix cholesterol is poorly absorbed (H-5)."
exhaustive_by_construction: false
independence: "The size of the surrogate-lipid effect factorizes from the direction of the hard-endpoint effect: a real ApoB rise can coexist with a null on mortality, so knowing the lipid magnitude does not fix the hard-endpoint base rate."
depends_on: []
question: "How large is habitual egg / dietary-cholesterol's effect on atherogenic blood lipids, and by what mechanism?"
relevance: "The surrogate-endpoint arm of the main question: whether eggs move atherogenic lipids enough to plausibly matter."
---
![[H-1 - Habitual whole-egg intake raises atherogenic LDL-ApoB and thereby CVD risk]]
![[H-5 - Poor bioavailability of egg cholesterol explains its weak effect on plasma cholesterol]]
![[H-8 - Dietary cholesterol's effect on serum cholesterol is real but saturating, small at high habitual intakes]]
![[H-11 - Egg's effect on atherogenic blood lipids is characterized in some way not listed above]]

Carving: this cluster holds the surrogate-endpoint (blood-lipid / ApoB) hypotheses, kept separate from the hard-endpoint direction cluster because a real lipid effect alongside a null on mortality is a key finding, not a contradiction. Members are graded by magnitude of the atherogenic-lipid effect. Exclusivity is on the dominant characterization; H-5 and H-8 both predict a *small* net lipid effect but attribute it to different mechanisms (poor absorption vs a saturating dose-response), so they overlap somewhat as magnitude answers - accepted here as two distinct mechanism-refinements of the "small effect" branch rather than merged, since a mechanism observation (e.g. absorption studies vs dose-response curves) discriminates them. Non-exhaustive, so residual H-11 covers "no effect" or a non-ApoB pathway.

## Prior

```python
# HC-1 prior - magnitude and mechanism of egg's effect on atherogenic blood lipids.
# Members in HC-1.hypotheses order: [H-1 large CVD-relevant ApoB rise, H-5 poor bioavailability,
# H-8 real but saturating, H-11 residual].
# Evidence selection (rule 5): every inbound edge (E-1..E-8) is case-specific and discriminating -
# E-1/E-2 are the crossover's own lipid readout, E-3/E-4 are H-5's defining absorption claims,
# E-5/E-8 are dose-level nulls, E-7 is H-8's defining curve shape, E-6 is a direct test of H-8's
# habitual-intake corollary. None is a reference-class base rate, so NO edge is marked
# used_for_prior: true and the whole set is left for step 8. The prior rests instead on outside-view
# lipid physiology (cholesterol absorption fractions, hepatic downregulation) that is not in the graph.
# `no_observation_arguments.py --cluster HC-1` returns none, so rule 6 contributes nothing here.

# H-8 real-but-saturating - the anchor. What would have to be true: dietary cholesterol genuinely
# raises serum LDL, but hepatic synthesis downregulation plus a bounded fractional absorption flatten
# the curve, so the marginal egg does little at Western baseline intakes. Reference class: nearly every
# absorbed-nutrient / feedback-regulated pathway in human physiology (iron, calcium, cholesterol
# itself) shows a saturating rather than linear dose-response. Highest confidence of the four.
w_saturating = 1.0

# H-1 large CVD-relevant rise, as odds vs the anchor. Would need the dose-response to stay steep across
# the habitual range with no meaningful homeostatic compensation. Fractional cholesterol absorption is
# roughly 0.5 and hepatic synthesis compensates a large part of what is absorbed, which caps how much a
# ~200 mg/d increment can move ApoB; a strictly non-saturating account has to argue that cap away.
odds_no_saturation = 0.45   # ~1 : 2.2 against the saturating account, given the compensation physiology
w_large_rise = odds_no_saturation * w_saturating

# H-5 poor bioavailability. Would need egg-matrix cholesterol specifically to be absorbed much worse
# than cholesterol from other foods - a stronger, more specific claim than "the effect is small", and
# one that competes with saturation for the same explanandum. Egg cholesterol is free (unesterified)
# and in a phospholipid emulsion, i.e. a form that is if anything absorbed well, so the mechanism is
# a priori the less likely of the two small-effect routes.
odds_matrix_vs_saturation = 0.35   # ~1 : 3 against saturation as the explanation of a small effect
w_poor_bioavail = odds_matrix_vs_saturation * w_saturating

# H-11 residual (rule 4) - the true characterization is none of the above: e.g. no atherogenic-lipid
# effect at all, or an effect running through particle size / oxidized-LDL / HDL functionality rather
# than LDL-ApoB mass, or a TMAO-mediated route with lipids as a bystander. Weighted by how often, in
# contested nutrition-mechanism questions, the eventual accepted mechanism sits outside the menu the
# field was arguing over - uncommon but far from negligible. Own argued weight, not a leftover.
w_residual = 0.22   # ~1 : 4.5 vs the anchor; ~11% of the normalised mass

prior("HC-1", [w_large_rise, w_poor_bioavail, w_saturating, w_residual])
```
