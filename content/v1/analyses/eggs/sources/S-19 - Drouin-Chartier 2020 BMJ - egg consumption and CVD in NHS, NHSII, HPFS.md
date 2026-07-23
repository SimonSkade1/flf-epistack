---
id: S-19
type: source
source_type: journal-article
url: https://doi.org/10.1136/bmj.m513
venue: BMJ
publication_date: 2020-03-04
citation_count: 125
citation_count_asof: 2026-07-23
field: nutritional/cardiovascular epidemiology
authors: [Jean-Philippe Drouin-Chartier, Siyu Chen, Yanping Li, Amanda L Schwab, Meir J Stampfer, Frank M Sacks, Bernard Rosner, Walter C Willett, Frank B Hu, Shilpa N Bhupathiraju]
found_via: named as a target primary in the planner's slice-1 brief (Harvard NHS/NHSII/HPFS family); the paper's own updated meta-analysis section is a discovery hub (mined for other cohorts' effect sizes, not itself minted further)
motivatedness: "authors disclose non-egg industry ties outside the submitted work: Drouin-Chartier — speaker/consulting honoraria from Dairy Farmers of Canada; Li — grants from California Walnut Commission; Hu — research support from California Walnut Commission and honoraria from Metagenics/Standard Process. No egg-industry funding disclosed for this paper."
trust_score: 0.82
trust_reason: "very large pooled cohorts (5.5M person-years, 14,806 events) plus a 33-cohort meta-analysis; tight CIs around the null (HR 0.93 [0.82-1.05]; meta RR 0.98 [0.93-1.03]) — FFQ/residual confounding the main cap"
usefulness: 4.2
usefulness_reason: "largest Western null for moderate egg intake on hard CVD endpoints and the source of the US-vs-Asia heterogeneity — strongly discriminating on both the overall-effect and 'for whom (region)' questions"
method_read: "~0.8 — size and meta-analytic pooling make the null robust; healthy-user confounding and FFQ error remain, and the Asian inverse subgroup (0.92, 0.85-0.99) only marginally clears significance"
standing: "BMJ (IF ~100+), 125 citations; self-corroborating via meta-analysis of 33 cohorts; updates Hu 1999 JAMA; non-egg COI (walnut/dairy) points away from an egg-favorable bias"
angle: western-cohort
data_basis: ["[[D-7]]"]
combined_score: 0.504
curated: true
curation_reason: "Core (rank): largest Western CVD null (Harvard pooling + 33-cohort meta); Western-null anchor."
extracted:
  - "[[O-43 - Higher egg intake tracks an unhealthier diet-lifestyle pattern (more red-processed meat, smoking, BMI, T2D) in Harvard cohorts]]"
  - "[[O-44 - Moderate egg intake not associated with CVD in Harvard cohorts (adjusted HR 0.93), crude 1.10 reversing to null on adjustment]]"
  - "[[A-16 - Crude-to-adjusted reversal shows the egg-CVD association is confounded by an unhealthy-eater pattern]]"
  - "[[A-17 - E-value- confounding of RR-=1.43 would be needed to turn the egg-CVD null positive]]"
  - "[[O-45 - Significant egg x type-2-diabetes interaction on CVD in Harvard cohorts, though stratum-specific egg-CVD HRs were null]]"
  - "[[O-46 - Substituting eggs for red-processed meat or full-fat milk raised CVD risk; substituting for fish-poultry-plant proteins was neutral (Harvard)]]"
  - "[[O-47 - 33-cohort meta-analysis- no overall egg-CVD association (RR 0.98 per +1 egg-day), but I2=62.3% heterogeneity]]"
  - "[[O-48 - Egg-CVD meta-association inverse in Asian cohorts (0.92) but null in US (1.01) and Europe (1.05)]]"
  - "[[A-18 - Region-structured heterogeneity favors population effect-modification over a universal egg-CVD null]]"
  - "[[O-49 - Meta-analysis in type-2-diabetes populations- higher egg intake associated with higher CVD risk (RR 1.25-1.40)]]"
  - "[[H-21 - Moderate egg intake has no causal effect on CVD risk overall]]"
  - "[[H-22 - Region-population modifies the egg-CVD association (inverse in Asia, null in West)]]"
  - "[[H-23 - Egg's CVD impact is relative to the food it replaces (neutral vs healthy proteins, better than red-processed meat)]]"
  - "[[H-24 - Egg consumption raises CVD risk specifically in people with type 2 diabetes]]"
---
Pools three large Harvard cohorts (83,349 women, NHS 1980-2012; 90,214 women, NHS II 1991-2013; 42,055 men, HPFS 1986-2012; >5.54 million person-years, 14,806 incident CVD cases) free of CVD/T2D/cancer at baseline, and updates a meta-analysis of 33 prospective-cohort risk estimates (1,720,108 participants, 139,195 CVD events). In the pooled Harvard analysis, ≥1 egg/day was not associated with incident CVD after adjusting for updated diet/lifestyle covariates correlated with egg intake (HR 0.93, 95% CI 0.82-1.05, vs <1 egg/month). The meta-analysis likewise found no overall CVD association per +1 egg/day (RR 0.98, 0.93-1.03) and, stratified by region, a null association in US and European cohorts but an inverse (protective) association in Asian cohorts (0.92, 0.85-0.99) — the update to the classic Hu 1999 JAMA Harvard analysis, and the paper the slice-1 planner offered as alternative to it.
relevance_note: The largest, most-cited Western-cohort null result for moderate egg intake and hard CVD endpoints; also the source of the US-vs-Asia heterogeneity slice 2 is tracking.

## Methodology

Two components. (1) Cohort analysis pooling three Harvard prospective cohorts — NHS (83,349 women, 1980-2012), NHS II (90,214 women, 1991-2013), HPFS (42,055 men, 1986-2012), free of CVD/T2D/cancer at baseline; 5,540,314 person-years, 14,806 incident CVD events. Whole-egg intake assessed every 2-4 years by validated semiquantitative FFQ (deattenuated validity r≈0.77-0.80 vs weighed records); repeated measures modeled as cumulative average, allowing baseline-only and simple-update sensitivity analyses. Endpoints (nonfatal/fatal MI, fatal CHD, fatal/nonfatal stroke) physician-adjudicated from medical records, blinded to exposure. Cox models with sequential adjustment (model 1 age; model 2 +lifestyle; model 3 +co-consumed foods). E-value sensitivity analysis. Substitution modeling swaps 1 egg/day for 1 serving/day of alternative foods. (2) Updated systematic review and random-effects meta-analysis of 33 prospective-cohort risk estimates (screened from 763 studies), with prespecified subgroup meta-regression by region, sex, follow-up, cohort size, risk of bias, and diet-assessment type. The cohort observations rest on the Harvard cohorts (D-7); the meta-analytic observations rest on the pooled 33-cohort corpus (D-26).

## Results — cohort analyses

![[O-43 - Higher egg intake tracks an unhealthier diet-lifestyle pattern (more red-processed meat, smoking, BMI, T2D) in Harvard cohorts]]

![[O-44 - Moderate egg intake not associated with CVD in Harvard cohorts (adjusted HR 0.93), crude 1.10 reversing to null on adjustment]]

![[A-16 - Crude-to-adjusted reversal shows the egg-CVD association is confounded by an unhealthy-eater pattern]]

![[A-17 - E-value- confounding of RR-=1.43 would be needed to turn the egg-CVD null positive]]

![[O-45 - Significant egg x type-2-diabetes interaction on CVD in Harvard cohorts, though stratum-specific egg-CVD HRs were null]]

![[O-46 - Substituting eggs for red-processed meat or full-fat milk raised CVD risk; substituting for fish-poultry-plant proteins was neutral (Harvard)]]

## Results — systematic review and meta-analysis

![[O-47 - 33-cohort meta-analysis- no overall egg-CVD association (RR 0.98 per +1 egg-day), but I2=62.3% heterogeneity]]

![[O-48 - Egg-CVD meta-association inverse in Asian cohorts (0.92) but null in US (1.01) and Europe (1.05)]]

![[A-18 - Region-structured heterogeneity favors population effect-modification over a universal egg-CVD null]]

![[O-49 - Meta-analysis in type-2-diabetes populations- higher egg intake associated with higher CVD risk (RR 1.25-1.40)]]

## Discussion

![[H-21 - Moderate egg intake has no causal effect on CVD risk overall]]

![[H-22 - Region-population modifies the egg-CVD association (inverse in Asia, null in West)]]

![[H-23 - Egg's CVD impact is relative to the food it replaces (neutral vs healthy proteins, better than red-processed meat)]]

![[H-24 - Egg consumption raises CVD risk specifically in people with type 2 diabetes]]
