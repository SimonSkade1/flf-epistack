---
type: correlation-group
id: CG-4
to: "[[HC-2 - Net direction of egg's effect on hard cardiovascular and mortality endpoints]]"
members:
  - "[[E-16 - O-6 x HC-2 - No egg-MI-stroke association in the Physicians Health Study]]"
  - "[[E-17 - O-7 x HC-2 - All-cause mortality rose with egg intake in PHS (HR 1.23)]]"
  - "[[E-18 - O-8 x HC-2 - Egg-mortality association twice as strong in diabetic PHS subgroup]]"
---

Joint likelihood for correlated observations O-6, O-7, O-8 (shared basis: D-4). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-4 (HC-2) - ONE joint estimate over E-16 + E-17 + E-18: O-6, O-7, O-8 all rest on D-4, the single PHS
# cohort (rule 1). The pattern is judged whole, as one cohort's internally-consistent result:
#   null on incident MI and stroke (O-6, 1550 MIs / 1342 strokes over ~20 y)
#   + all-cause mortality gradient (O-7, HR 1.23 for >=7/wk vs <1/wk, P-trend<0.0001)
#   + a roughly doubled association in diabetics (O-8, HR 2.01, P-interaction 0.09, exploratory).
# The pattern is: harm shows up on death but not on the cardiovascular events that would mediate it, and
# concentrates in a metabolically vulnerable subgroup. A-2 (corrected) is what governs the reading: this
# dissociation is evidence AGAINST a cardiovascular-mediated causal harm, but it does NOT select residual
# confounding over a non-CVD causal route. So O-7 must not be priced as clean support for H-3, nor as clean
# support for the null members. PHS is a healthy Western male cohort, so the scope riders do most of the
# work separating the three null members (H-4 IHD-only, H-9 healthy-Western-<=1/day, H-10 diverse-global).
# Members in HC-2.hypotheses order: [H-2, H-3, H-4, H-9, H-10, H-12]. Anchored on H-12 = 1 (rule 7).

lik_phs_H12 = 1.0
# Anchor: direction-varying effect is the only member that predicts the WHOLE pattern without strain -
# harm concentrated at the high end (>=7/wk) and in diabetics, nothing at moderate intake, and no clean
# population-wide event signal. The subgroup interaction is literally its content. Docked from being a
# runaway winner only by the exploratory status of O-8 (P-interaction 0.09).

lik_phs_H3 = 0.75
# 0.75x the anchor: H-3's defining prediction is exactly O-7 + O-8 (high intake raises all-cause mortality,
# worse in diabetics) - the best fit of any single-direction member. Held below the anchor rather than at it
# because H-3's proposed mechanism is the dietary-cholesterol -> CVD chain, and O-6's null on MI and stroke
# is the intermediate that chain should have moved. Per A-2 (corrected) this is a real cost to H-3's
# cardiovascular reading, though not fatal: a non-CVD causal route (glycaemic, or fatal-CVD not captured by
# incident events, or competing risks masking the events) reproduces the pattern under H-3 too.

lik_phs_H9 = 0.55
# 0.55x: PHS is squarely in H-9's scope (generally healthy Western adults), so this pattern is the one that
# bears most directly on it. O-6 is well predicted - a genuine null up to ~1/day should show exactly no
# MI/stroke association across 1550 MIs. O-8 is outside its scope (diabetics are not 'generally healthy'),
# so it costs H-9 nothing. What costs H-9 is O-7: >=7/wk sits right at its ~1/day cap and the mortality
# gradient is significant there, so H-9 must attribute the whole gradient to confounding or non-CVD causes.
# A-2 (corrected) makes that a live but not free move - it does not license reading the gradient as
# confounding by default. Highest of the three null members because of scope fit.

lik_phs_H4 = 0.45
# 0.45x: H-4 is scoped to ischemic heart disease, so O-6's null is well predicted and central to it, while
# O-7 and O-8 are mortality endpoints its claim does not reach - it neither predicts nor forbids them. That
# non-engagement is why it sits below H-9: two thirds of this pattern is simply outside what H-4 says, so it
# earns credit only on the O-6 third and must stay silent (i.e. unexplanatory) on the rest.

lik_phs_H10 = 0.25
# 0.25x: the worst-fitting null. H-10 claims no material effect on lipids, CVD OR mortality across diverse
# populations - an explicit population-wide mortality null, which a significant HR 1.23 gradient with
# P-trend<0.0001 and an HR 2.01 diabetic subgroup contradicts head-on. It gets credit only for O-6. Not
# lower because a single self-selected male-physician cohort with an abbreviated FFQ is exactly the kind of
# study H-10 can dismiss as confounded, and O-8 is exploratory.

lik_phs_H2 = 0.15
# 0.15x: the worst fit overall. Protection at ~1/day should have shown as FEWER MIs and strokes in a ~20 y,
# 1550-event cohort; instead O-6 is flatly null and O-7/O-8 run the wrong way. Not near zero because O-6's
# null is at least compatible with a small protective effect diluted by confounding in the opposite
# direction, and because PHS's exposure contrast is crude.

t_phs = 0.55
# Cap = min trust_score over {O-6, O-7, O-8} = 0.68 (all via S-14). Docked below the cap for weaknesses
# specific to the raw-data -> stated-observation step, not to the truth of any member: exposure is an
# abbreviated food-frequency questionnaire with no full-diet adjustment (so intake is crudely graded and
# residual confounding by overall diet pattern is unmodelled), the cohort is self-selected male US
# physicians (narrow, healthy-user selected), and O-8's subgroup result is exploratory with
# P-interaction 0.09 - i.e. the diabetic contrast is the least reliable third of the pattern being priced.
evidence("HC-2", ["O-6", "O-7", "O-8"],
         [lik_phs_H2, lik_phs_H3, lik_phs_H4, lik_phs_H9, lik_phs_H10, lik_phs_H12], t=t_phs)
```
