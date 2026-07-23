---
type: hypothesis-cluster
id: HC-2
hypotheses:
  - "[[H-7 - Inverse egg-CVD association in China Kadoorie reflects healthy-user confounding not causation]]"
  - "[[H-22 - Region-population modifies the egg-CVD association (inverse in Asia, null in West)]]"
  - "[[H-50 - Some other origin of regional heterogeneity]]"
exclusivity: "Either the between-region contrast reflects a true difference in the causal effect (real modification) or it does not (the salient Asian inverse being healthy-user/residual confounding); at most one holds."
exhaustive_by_construction: false
independence: "Whether the effect is region-modified is orthogonal to its overall level (HC-1) and to the T2D question; knowing the modification status does not set the base rate of the overall sign."
depends_on:
  - "HC-1: shares the Asian directional evidence; level and modification are only approximately independent"
  - "HC-10: background-diet contingency is a candidate mechanism for the regional differences"
question: "Is the egg-CVD association genuinely modified by region/population, or is the apparent heterogeneity (above all the protective Asian signal) an artefact?"
relevance: "Answers the 'for whom (which population)' clause and gates whether an 'overall' verdict is even meaningful."
---

![[H-7 - Inverse egg-CVD association in China Kadoorie reflects healthy-user confounding not causation]]

![[H-22 - Region-population modifies the egg-CVD association (inverse in Asia, null in West)]]

![[H-50 - Some other origin of regional heterogeneity]]

## Carving

The sub-question is whether the egg-CVD association is really modified by region/population or whether the apparent heterogeneity is an artefact. H-22 asserts genuine effect-modification (inverse in Asia, null in the West); H-7 asserts the salient Asian inverse is healthy-user and residual confounding rather than a causal regional difference. Reading H-22 as a claim about a real difference in the causal effect and H-7 as that difference being spurious, at most one holds. Residual H-50 covers heterogeneity that is real but arises from something other than region - differential exposure ranges, measurement quality, or chance. This cluster is kept separate from HC-1 because level and heterogeneity are distinct axes (one can hold a neutral overall verdict while believing the effect is region-modified); the shared Asian cohort evidence discriminating in both is allowed, and the mutual premise-dependence with HC-1 is logged in depends_on. H-7 (the confounding pole) is the natural foil to H-22 and lives here rather than beside its Kadoorie counterpart H-6 (which supplies HC-1's protective pole).

## Prior

```python
# HC-2 prior — is the egg-CVD association genuinely modified by region/population, or is the apparent
# heterogeneity (above all the protective Asian signal) an artefact? Members in HC-2.hypotheses order:
# [H-7 Asian inverse is healthy-user/residual confounding, H-22 genuine region effect-modification,
#  H-50 residual: other origin (exposure-range / measurement / chance)].
# No cluster no-observation arguments exist (no_observation_arguments.py --cluster HC-2 returns none).
# Evidence split: E-132 (O-71, the serum beta-carotene protective cohort signal RR 0.69 that RCTs exclude)
# is an OUTSIDE-VIEW reference-class fact — the base rate for a salient protective observational signal
# being confounding rather than causal — so it is priced into this prior and marked used_for_prior: true
# (it belongs to no correlation group, so it stands alone). Every other inbound E edge (Kadoorie, PURE,
# KoGES, China-PAR, the cohort intake-range facts, the egg-T2D cross-outcome gradient) is case-specific and
# DISCRIMINATING and is left unmarked for step 8. Weights are relative odds.

# Base rate that a salient protective observational nutrition signal is causal rather than confounding.
# Young & Karr 2011 (Significance 8(3)) followed 52 such observational claims into 12 RCTs: 0/52 replicated,
# 5 reversed; and serum beta-carotene (E-132 / O-71, biomarker-measured RR 0.69) is fully excluded by RCTs.
# Region effect-MODIFICATION is a slightly weaker claim than a main effect, so I sit just above the 0/52
# floor rather than on it.
p_protective_causal = 0.17   # per Young & Karr 2011 (0/52) and E-132; low but non-zero for a modification claim

# H-7 — the salient Asian inverse is healthy-user / residual confounding (no real regional modification of
# the causal effect). Given the signal is most likely NOT causal, healthy-user/residual confounding is the
# leading single mechanism for a protective cohort signal (the beta-carotene template), ahead of
# exposure-range or chance.
frac_healthy_user = 0.5   # among the non-causal explanations, share that is specifically healthy-user/residual confounding of the Asian inverse
w_H7 = (1 - p_protective_causal) * frac_healthy_user

# H-22 — genuine population/region effect-modification (inverse in Asia, null in West). Requires the Asian
# signal to be causal AND for that effect to genuinely differ by region rather than be one universal
# (possibly non-linear) effect measured over different exposure ranges.
frac_region_specific = 0.55   # given a real effect, chance it is truly region-modified vs universal
w_H22 = p_protective_causal * frac_region_specific

# H-50 residual — the heterogeneity is real but arises from something other than genuine region-modification
# or healthy-user confounding of the Asian inverse: differential exposure ranges (regions sampling different
# arms of one dose-response), differential measurement quality, or chance/publication artefact. Its own
# argued weight (rule 4), set high because the exposure-range explanation is specifically well-motivated for
# this question (the salient Asian cohorts sit on the low-intake limb) and rivals the confounding account.
w_H50 = 0.38   # standalone; ~0.38 vs ~0.42 for H-7, ~43% of the mass once normalised

prior("HC-2", [w_H7, w_H22, w_H50])
```
