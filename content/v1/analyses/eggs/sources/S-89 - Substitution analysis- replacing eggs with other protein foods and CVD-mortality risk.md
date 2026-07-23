---
id: S-89
type: source
source_type: journal-article
url: https://doi.org/10.1093/ije/dyaa205
venue: International Journal of Epidemiology
publication_date: "2021"
citation_count: 45
citation_count_asof: 2026-07-23
field: nutritional epidemiology (cardiovascular)
authors: [Zhong VW, Allen NB, Greenland P, "et al."]
found_via: "citation-chase from Zhong VW et al 2019 JAMA (same underlying pooled US cohort family, slice 1) + PubMed keyword search"
motivatedness: "unknown; academic pooled-cohort consortium (Lifetime Risk Pooling Project), no industry funding found"
trust_score: 0.62
trust_reason: Large pooled cohorts (29682, 6 US studies); the qualitative demonstration that the egg "effect" flips sign/size with the comparator is near-structural and robust, but the specific substitution HRs rest on the modeling assumptions S-90 warns are reference-dependent and on observational confounding.
usefulness: 3.8
usefulness_reason: Shows comparator-dependence within a single dataset (eggs vs fish/nuts/legumes/grains vs red meat) — the core insight that dissolves the naive "eggs good/bad" framing; large, multi-food, and a US-cohort angle in an Asian-heavy slice.
method_read: Well-powered pooled cohort but substitution coefficients are model-contingent; direction robust, magnitudes soft — ~0.62.
standing: Int J Epidemiology, 45 citations; shares the Lifetime Risk Pooling Project basis with Zhong 2019 JAMA (S-21), so not independent of that finding.
angle: substitution
data_basis: [[D-1]]
combined_score: -0.304
curated: true
curation_reason: "Coverage-include (combined<=0, trust 0.62): Zhong substitution analysis; substitution position otherwise unrepresented. Shares D-1 with S-21 (correlated). Position: substitution."
extracted: ["[[O-39 - Replacing one serving per day of eggs with nuts, legumes, whole grains or fish lowers incident CVD by 15-21 percent]]", "[[O-40 - Replacing one serving per day of eggs with nuts, fish, poultry or whole grains lowers all-cause mortality by 11-22 percent]]", "[[O-41 - Sign and size of the egg-removal effect depend on the comparator food; eggs rank near processed meat]]", "[[O-42 - Only 8 percent of participants ate at least one egg serving per day in the pooled US cohorts]]", "[[H-17 - Eggs are a relatively unhealthy protein source; benefit comes from replacing eggs with plant or fish protein]]", "[[A-13 - Isocaloric substitution algebra makes the egg effect the difference of two food coefficients, so no unconditional egg effect is identified]]", "[[H-18 - The egg-health effect is a property of the comparator not of eggs alone, so eggs good-or-bad is ill-posed]]", "[[A-14 - Full-serving-per-day substitution benefits apply only to the small high-intake minority, so population impact of cutting eggs is smaller]]"]
---
Uses the pooled ~29,700-participant Lifetime Risk Pooling Project (6 US cohorts) to model isocaloric substitution of one serving of one animal-protein food for another, estimating the resulting change in incident CVD and all-cause mortality risk. The same substitution matrix compares eggs against every other protein food as reference, so the sign and size of the "egg effect" is shown, within one paper, to depend on the comparator.

## Methodology
Pooled analysis of 29,682 US adults from six prospective cohorts (ARIC, CARDIA, CHS, Framingham Heart + Offspring, MESA; baseline visits 1985-2002), individual-participant-data harmonized. 6,963 incident CVD events and 8,875 deaths over median 19.0 y (max 31.3 y) follow-up to 31 Aug 2016. Excluded: baseline CVD, extreme energy (<500 or >6000 kcal/day), missing data. Baseline diet only, by validated diet history/FFQ harmonized across cohorts. One serving = one whole egg, 85 g other meats, 28 g nuts, half cup legumes, one slice whole-grain bread. Substitution model Y = a*F1 + b*F2 + covariates with all eight protein foods entered together and total constrained, so the substitution effect is the coefficient contrast exp(b-a); a quadratic term added for processed meat (non-monotonic). Cohort-stratified cause-specific hazard models (incident CVD, competing risks) and proportional hazards (mortality). Covariates: age, sex, race/ethnicity, education, total energy, smoking status + pack-years, physical-activity z-score, alcohol, hormone therapy, modified aHEI-2010 (protein components removed); blood pressure, cholesterol, glucose, BMI excluded as mediators. 30-year absolute risk differences via bootstrap (500 samples). No subgroup analyses (prior work found no consistent interactions).

## Results
![[O-39 - Replacing one serving per day of eggs with nuts, legumes, whole grains or fish lowers incident CVD by 15-21 percent]]
![[O-40 - Replacing one serving per day of eggs with nuts, fish, poultry or whole grains lowers all-cause mortality by 11-22 percent]]
![[O-41 - Sign and size of the egg-removal effect depend on the comparator food; eggs rank near processed meat]]
![[O-42 - Only 8 percent of participants ate at least one egg serving per day in the pooled US cohorts]]

## Interpretation
![[H-17 - Eggs are a relatively unhealthy protein source; benefit comes from replacing eggs with plant or fish protein]]
![[A-13 - Isocaloric substitution algebra makes the egg effect the difference of two food coefficients, so no unconditional egg effect is identified]]
![[H-18 - The egg-health effect is a property of the comparator not of eggs alone, so eggs good-or-bad is ill-posed]]
![[A-14 - Full-serving-per-day substitution benefits apply only to the small high-intake minority, so population impact of cutting eggs is smaller]]

relevance_note: Direct primary demonstrating the comparator-dependence of the egg-health association — the core epistemic claim of this slice's substitution thread.
