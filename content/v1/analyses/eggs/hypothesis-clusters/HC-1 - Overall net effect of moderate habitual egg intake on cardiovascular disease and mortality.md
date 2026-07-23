---
type: hypothesis-cluster
id: HC-1
hypotheses:
  - "[[H-6 - Moderate egg consumption causally lowers CVD risk in Chinese adults]]"
  - "[[H-21 - Moderate egg intake has no causal effect on CVD risk overall]]"
  - "[[H-27 - Higher dietary cholesterol - egg intake causally raises CVD and mortality risk (dose-response)]]"
  - "[[H-44 - An intermediate egg intake of about 3 to 6 per week minimizes CVD and mortality risk with harm at both lower and higher intake]]"
  - "[[H-49 - Some other overall egg-CVD relationship]]"
exclusivity: "Each names an incompatible sign or shape for the population dose-response - protective, flat, monotonically harmful, or U-shaped - so at most one can summarize the typical effect (a genuine region-flip is the separate HC-2 question and would send weight to the residual)."
exhaustive_by_construction: false
independence: "The net direction/shape is a different quantity from whether the effect varies by region (HC-2), which agent carries it (HC-5), or whether the framing is well-posed (HC-10); knowing those does not fix the base rate of the sign, so the prior factorizes with the residual absorbing the region-flip case."
depends_on:
  - "HC-2: a genuine region-flip means no single overall verdict - weight then flows to this cluster's residual H-49; only approximately independent"
  - "HC-10: if egg-health is comparator-contingent/ill-posed, a single unconditional overall verdict is undercut"
  - "HC-5: the harmful pole (H-27) bundles egg-cholesterol causality shared with the operative-exposure cluster"
question: "What is the net causal effect of moderate habitual egg intake (up to ~1 egg/day) on cardiovascular disease and all-cause mortality?"
relevance: "This is the spine of the main question's 'overall ... and at what level' clauses."
---

![[H-6 - Moderate egg consumption causally lowers CVD risk in Chinese adults]]

![[H-21 - Moderate egg intake has no causal effect on CVD risk overall]]

![[H-27 - Higher dietary cholesterol - egg intake causally raises CVD and mortality risk (dose-response)]]

![[H-44 - An intermediate egg intake of about 3 to 6 per week minimizes CVD and mortality risk with harm at both lower and higher intake]]

![[H-49 - Some other overall egg-CVD relationship]]

## Carving

The sub-question is the net causal effect of moderate habitual egg intake on hard cardiovascular and mortality endpoints, read as the typical population dose-response curve. The four named members are mutually incompatible signs/shapes of that curve: causal protection (H-6), a flat null (H-21), a monotonic dose-dependent increase (H-27), and a U-shape with a moderate optimum around 3-<6/week (H-44). H-6 and H-27 carry population tags (Chinese / US) that reflect their evidentiary base, not a scope that would let both hold at once; if the sign genuinely flips by population that is the separate modification question (HC-2), and under that scenario none of the single-verdict members is globally correct, so probability flows to the residual H-49. Non-exhaustive: the residual also covers non-monotonic shapes other than the simple U. The Kadoorie/PURE/Western-cohort and dietary-cholesterol observations discriminate these members; the same Asian evidence also informs HC-2, which is permitted because level and heterogeneity are orthogonal axes rather than two slices of one question.

## Prior

```python
# HC-1 prior — net causal effect/shape of moderate habitual egg intake (up to ~1/day) on CVD & all-cause mortality.
# Members in HC-1.hypotheses order:
#   [H-6 protective (Chinese/Asian), H-21 null overall, H-27 monotonic dose-dependent harm (US),
#    H-44 U-shape with optimum 3-<6/wk, H-49 residual (no single population-average verdict)].
# no_observation_arguments.py --cluster HC-1 returned none.
# EVIDENCE SPLIT: every egg-specific cohort/meta result DISCRIMINATES these members and is LEFT for step 8 —
#   Kadoorie (CG-1), Harvard adjusted-null + its confounder structure (CG-2), 33-cohort meta + region gradient
#   (CG-3), US-pooled +half-egg/day & dietary-cholesterol dose-response (CG-4), PURE/ONTARGET (CG-5), China-PAR
#   U-shape (CG-6), KoGES whole-cohort null (E-38). ONE outside-view datum is pulled into the prior:
#   O-70 (E-52, marked used_for_prior) — Ioannidis's reference-class reductio that face-value nutritional-cohort
#   magnitudes are jointly absurd (about -6 y life-expectancy per daily egg). Its step-5 note frames it as
#   discriminating, but its content is a general "these associations are usually bias-driven not causal" fact
#   about the whole reference class, not eggs' own record — so it belongs in the prior and is not re-counted at 8.
# Odds are anchored on the null (H-21 = 1.0). depends_on: a genuine region sign-flip (HC-2) sends weight to H-49.

# Anchor — H-21 null overall. Outside view: for a single common food at moderate intake against HARD CVD /
# mortality endpoints, the base-rate outcome in nutritional epidemiology is no clinically meaningful causal
# effect (small confounded associations that do not survive as large causal effects). This is the modal answer,
# and the member I am most confident in relative to the others.
w_null = 1.0   # H-21 anchor: null is the reference-class modal outcome for a moderate single-food -> hard-endpoint question

# Reference-class deflator from O-70 (E-52, used_for_prior). If the large egg cohort HRs were lifelong-causal
# they imply absurd, mutually incompatible life-expectancy effects; the reference class of nutritional-cohort
# single-food estimates is therefore mostly bias-driven. This multiplies DOWN the a-priori odds of the two
# "large true causal effect" members (protective H-6, harmful H-27); it does not touch null/U-shape/residual.
deflate_large_causal = 0.60   # O-70: fraction to which the outside view discounts a large true single-food causal effect

# H-6 protective in Chinese/Asian adults. For this to be the typical population effect, eggs' nutrient density
# (protein, choline, carotenoids, phospholipids) would have to net-lower hard endpoints. Reference class:
# single-food "protective-against-CVD" claims are common but seldom confirmed causally (vitamin-E, beta-carotene,
# antioxidant cohort signals nulled in RCTs). Population tag narrows it further. Least confident of the four
# named shapes; omits WHY any signal is Asian-specific (that mechanism is HC-2's question).
base_odds_protect_vs_null = 0.50   # a genuine single-food protective effect on hard endpoints, before the O-70 deflation
w_protect = base_odds_protect_vs_null * deflate_large_causal * w_null   # H-6

# H-27 monotonic dose-dependent harm (US). The textbook lipid-hypothesis expectation: egg cholesterol raises
# serum cholesterol -> atherogenic -> more CVD, no threshold. Mechanistically the most "expected" non-null
# shape, so it gets the largest non-null odds before deflation — but O-70's -6 y/egg figure is exactly this
# member's face value, so the deflation bites hardest here. More confident than protective, below null.
base_odds_harm_vs_null = 0.90   # textbook monotonic harm from egg cholesterol, before the O-70 deflation
w_harm = base_odds_harm_vs_null * deflate_large_causal * w_null   # H-27

# H-44 U-shape, optimum 3-<6/wk, harm at both extremes. A specific functional form. U-shapes recur in nutrition
# but a genuine one for eggs is a narrow claim, and the low-intake harm arm is the shape most easily manufactured
# by confounding (very-low egg eaters are disproportionately poor/sick/otherwise-unhealthy). Not deflated by
# O-70 (its arm magnitudes are not the absurd-lifelong ones), but intrinsically low prior.
odds_ushape_vs_null = 0.22   # a true U-shaped dose-response, vs a confounding-driven low-end artifact
w_ushape = odds_ushape_vs_null * w_null   # H-44

# H-49 residual — its OWN argued weight (rule 4), not a leftover. An unmodelled answer here looks like: the sign
# is GENUINELY subgroup/region-dependent so no single population curve is correct (the HC-2 region-flip case,
# flagged in depends_on), or a non-monotonic shape other than the simple U (e.g. threshold/plateau). Given the
# well-known Asian-inverse vs Western-null divergence, a "no single verdict" world is a live prior.
w_residual = 0.30   # ~0.30 : 1 vs null; genuine region/subgroup sign-dependence or an unlisted shape

prior("HC-1", [w_protect, w_null, w_harm, w_ushape, w_residual])
```
