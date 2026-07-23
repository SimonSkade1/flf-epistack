---
id: A-18
type: argument
status: corrected
reason_if_not_false: checked
statement: "The pooled null (I2=62.3%) masks region-specific estimates whose heterogeneity is largely explained by geography (Asia inverse 0.92, US null 1.01, Europe null 1.05), so the data are poorly described by a single homogeneous effect and are consistent with population/dietary-context effect-modification — but region-correlated cohort artifacts (measurement, background diet, confounding, healthcare) explain the same structure equally well, so modification is suggested, not favoured over a null-plus-differential-bias account."
source: "[[S-19 - Drouin-Chartier 2020 BMJ - egg consumption and CVD in NHS, NHSII, HPFS]]"
locator: "Discussion, heterogeneity"
affects_observations: ["[[O-48 - Egg-CVD meta-association inverse in Asian cohorts (0.92) but null in US (1.01) and Europe (1.05)]]"]
affects_hypotheses: ["[[H-22 - Region-population modifies the egg-CVD association (inverse in Asia, null in West)]]"]
---
A pooled RR near 1.0 can arise two ways: eggs truly have no effect anywhere, or opposing region-specific effects average out. The meta-analysis shows substantial heterogeneity (I2=62.3%), and prespecified meta-regression finds geographic region to be its main source (P for interaction=0.07): the Asian estimate is significantly inverse (0.92, 0.85-0.99) while the US (1.01) and European (1.05) estimates are null, with much lower within-US heterogeneity (I2=30.8%). A homogeneous-null model does not predict this structured between-region divergence, whereas effect-modification by population/dietary context does (e.g. eggs co-consumed with vegetables/rice in Asian diets versus bacon/processed meat in Western diets, or displacing different baseline foods), supporting H-22. The interaction P=0.07 is not conventionally significant, so the modification is suggested rather than established, and region is confounded with numerous cohort-level differences (measurement, background diet, healthcare) beyond diet culture per se.

## Validity assessment (step 6)

Traced step: I2=62.3% with region as the main prespecified heterogeneity source does show the data are not well described by a homogeneous effect (a true null everywhere with only sampling variation gives I2 ~= 0). But the argument's dichotomy is effect-modification vs "universal null," and the load-bearing move to genuine population/dietary effect-modification requires the hidden premise that the region-structured divergence is causal rather than artefactual. Undercutting defeater that survives without denying any premise: a true universal null combined with region-correlated differential bias (FFQ measurement, background-diet confounding, healthcare, cohort design — all of which co-vary with geography) reproduces exactly the same structured heterogeneity. The argument itself concedes this ("region is confounded with numerous cohort-level differences"). So the evidence favours "not a single homogeneous data-generating process," not specifically effect-modification over a null-plus-differential-bias account. Weaker claim that survives: the structured heterogeneity is inconsistent with a clean homogeneous null and is consistent with (suggestive of, given P=0.07) population effect-modification. corrected / checked.

## Original

statement: "The pooled null (I2=62.3%) masks region-specific estimates whose heterogeneity is largely explained by geography (Asia inverse 0.92, US null 1.01, Europe null 1.05), so the data are better described by population/dietary-context effect-modification than by a single universal null effect."
