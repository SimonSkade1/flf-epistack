---
type: hypothesis-cluster
id: HC-6
hypotheses:
  - "[[H-20 - In dysglycemic adults, replacing high-carb breakfast foods with eggs modestly worsens LDL-C]]"
  - "[[H-34 - Egg-derived dietary cholesterol raises fasting LDL-total cholesterol linearly, roughly +1.4-1.5 mg-dL per 100 mg]]"
  - "[[H-40 - Whole eggs on a carbohydrate-restricted diet produce a net-favorable-neutral lipid response (HDL up, LDL-HDL preserved) even in hyper-absorbers]]"
  - "[[H-53 - Some other egg lipid-profile effect]]"
exclusivity: "Read as the single best characterization of the net lipid effect, at most one holds - a rise in atherogenic lipids (absolute per H-34 or comparator-relative per H-20) versus a net-neutral-to-HDL-favourable response (H-40)."
exhaustive_by_construction: false
independence: "The biomarker lipid effect is a distinct quantity from hard-endpoint CVD (HC-1) and from operative-exposure attribution (HC-5); its prior stands alone, with the responder-variance link to HC-7 noted."
depends_on:
  - "HC-7: this cluster's mean lipid effect and HC-7's response spread are the same trait's first two moments"
question: "What is the net effect of adding egg or egg-derived cholesterol on the atherogenic blood-lipid profile in controlled feeding?"
relevance: "The mechanistic biomarker layer under the CVD verdict - the classic reason eggs were deemed harmful."
---

![[H-20 - In dysglycemic adults, replacing high-carb breakfast foods with eggs modestly worsens LDL-C]]

![[H-34 - Egg-derived dietary cholesterol raises fasting LDL-total cholesterol linearly, roughly +1.4-1.5 mg-dL per 100 mg]]

![[H-40 - Whole eggs on a carbohydrate-restricted diet produce a net-favorable-neutral lipid response (HDL up, LDL-HDL preserved) even in hyper-absorbers]]

![[H-53 - Some other egg lipid-profile effect]]

## Carving

The sub-question is the net effect of egg/egg-cholesterol on the atherogenic blood-lipid profile in controlled feeding. Members range from a modest linear LDL and apoB rise per unit dietary cholesterol (H-34), through a small comparator-relative LDL worsening when eggs displace high-carbohydrate foods in dysglycemic adults (H-20), to a net-neutral-to-favourable response - HDL up, LDL and the LDL:HDL ratio preserved even in hyper-absorbers - on a carbohydrate-restricted background (H-40). Read as the best single characterization of the net lipid effect, at most one holds; H-34 and H-20 sit on the 'raises atherogenic lipids' side at different grains (absolute dose-response versus comparator-relative small effect) and are discriminated by different observations, while H-40's context-dependence - a low-carbohydrate background independently raising HDL - is the live confound against it. Residual H-53 covers particle-quality-only or subgroup-confined effects. H-20 lives here rather than in HC-4 because its LDL endpoint co-holds with its trial-mate H-19's glycemic finding and so cannot be an exclusive co-member there. The mean-versus-spread relationship to HC-7 is noted in depends_on.

## Prior

```python
# HC-6 prior — net effect of egg / egg-cholesterol on the atherogenic blood-lipid profile in controlled
# feeding. Members in HC-6.hypotheses order:
# [H-20 comparator-relative LDL worsening in dysglycemia, H-34 linear absolute LDL/apoB rise,
#  H-40 net-neutral-to-HDL-favourable on a carb-restricted background, H-53 residual].
# Evidence split: the one base-rate fact this step rests on is O-28 — serum cholesterol rises with dietary
# cholesterol in controlled metabolic-ward feeding, the general Keys-era dose-response (E-17, now marked
# used_for_prior: true, so step 8 skips it). Every egg-specific trial — the Ginsberg quantification
# (CG-21), the prediabetes-RCT nulls (CG-19), the eggs-vs-high-carb contrast (CG-20), the 4-egg null
# (E-20), the Mutungi carb-restricted HDL rise (CG-22) — is left unmarked; it discriminates and is priced
# at step 8. no_observation_arguments.py --cluster HC-6 returns none, so no argument moved a number here.

# H-34 anchor — an absolute, dose-dependent LDL/apoB rise as the single best characterization of the net
# effect. What must hold: the general dose-response (O-28) dominates the net lipid effect and is borne by
# LDL/apoB, not HDL. Reference class: controlled metabolic-ward dietary-cholesterol feeding, the classic
# mechanism behind the "eggs are harmful" verdict. Omits: magnitude in older / hyper-responder /
# different-background populations. Most confident of the four as the default reading, because the
# outside-view dose-response is established and positive.
w_h34 = 1.0   # unit anchor: the mechanistic default characterization

# H-40 net-neutral-to-HDL-favourable, odds vs H-34. What must hold: homeostatic down-regulation of
# endogenous synthesis blunts the dietary-cholesterol effect to neutral AND eggs specifically raise HDL.
# Reference class: whole-egg feeding on a carbohydrate-restricted background. Confound it omits: the
# low-carb background independently raises HDL, and the source lab (Fernandez) is egg-industry funded — so
# the *favourable* half is fragile even where the *neutral* half is plausible. Second-most likely:
# neutrality is common but the HDL-up spin is confounded, so below H-34.
odds_neutral_fav_vs_rise = 0.60   # net-neutral-to-favourable somewhat less likely a priori than an absolute rise
w_h40 = odds_neutral_fav_vs_rise * w_h34

# H-20 comparator-relative worsening in dysglycemic adults, odds vs H-34. What must hold: eggs displace
# higher-carb breakfast foods and leave a *smaller LDL decrease* (not an absolute rise) in a metabolic-
# syndrome/prediabetes population. Reference class: isocaloric breakfast-substitution trials in dysglycemia.
# Omits/weakness: the least general characterization (comparator- and population-specific) and the trial is
# fragile (n=30, p~0.02 uncorrected, LDL fell absolutely on both arms). Below H-40 because as "the single
# best characterization of the net effect" a comparator-only story is narrow.
odds_comparator_vs_rise = 0.40   # narrow, fragile comparator-relative effect: below both the rise and the neutral reading
w_h20 = odds_comparator_vs_rise * w_h34

# H-53 residual — some other lipid effect the three listed members cannot express: an effect confined to
# LDL particle quality (size/oxidation with bulk LDL-C flat) or to a specific subgroup (e.g. ApoE4
# hyper-responders). Its own argued weight (rule 4), not a leftover: uncommon because the three members
# already span the sign of the net bulk-lipid effect, but real given the particle-quality channel.
odds_other = 0.23   # ~0.23 : 1 vs the unit anchor; ~10% of the mass once normalised
w_h53 = odds_other

prior("HC-6", [w_h20, w_h34, w_h40, w_h53])
```
