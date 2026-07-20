# Orientation — slice: cohorts-hard-endpoints

Slice: observational/epidemiological cohort (± nested case-control) studies in GENERAL adult populations, hard endpoints (incident CVD: CHD/stroke/heart failure; all-cause or cause-specific mortality), vs habitual egg intake. 7 sources minted, one primary per cohort family, spread across 7 distinct families and 4 regions (US ×3, global-multinational ×1, East Asia ×2, Europe ×1).

## Sources by finding direction

**Harm-leaning (higher intake → higher risk)**

1. [[S-7 - Zhong 2019 JAMA - Dietary cholesterol and egg intake linked to higher incident CVD and mortality in 6 pooled US cohorts]] — 6-cohort NHLBI Lifetime Risk Pooling Project (ARIC, CARDIA, Framingham Heart/Offspring, Jackson Heart, MESA), n=29,615, dose-dependent harm on both incident CVD and all-cause mortality. The headline anti-egg anchor; 225 citations.
2. [[S-14 - Djoussé 2008 Physicians Health Study - Egg consumption linked to higher mortality, especially in diabetics]] — 21,327 male US physicians; null on incident MI/stroke but mortality rises with intake, ~2x stronger in the diabetic subgroup.

**Null (no significant association)**

3. [[S-9 - Drouin-Chartier 2020 BMJ - Egg intake not associated with CVD risk in NHS-NHSII-HPFS, updated meta-analysis]] — Harvard NHS/NHSII/HPFS, n=215,618, largest/most current US cohort analysis in the slice; ≥1 egg/day not associated with incident CVD after full adjustment. Direct counterweight to Zhong 2019 from a comparably rigorous pooled design.
4. [[S-11 - Dehghan 2020 PURE - Egg intake not associated with blood lipids, CVD, or mortality across 50 countries]] — PURE (146,011, 21 countries) + ONTARGET/TRANSCEND (31,544); no significant association with lipids, mortality, or CVD events; the most geographically diverse (incl. low/middle-income countries) evidence in the slice.

**Protective or mixed/nonlinear**

5. [[S-13 - Qin 2018 Heart - Daily egg consumption associated with lower CVD risk in China Kadoorie Biobank]] — 0.5M-adult Chinese cohort (largest single cohort in the slice); daily egg consumption associated with 11-26% *lower* risk across CVD/IHD/major-coronary-event/stroke endpoints, clean dose-response. Central protective-direction anchor.
6. [[S-16 - Key 2019 Circulation - Egg intake modestly inversely associated with ischemic heart disease in EPIC]] — pan-European EPIC, n=409,885, 9 countries; eggs modestly inverse (HR 0.93/20g/day) but the association becomes nonsignificant after a reverse-causation sensitivity check — weaker/more fragile than Qin's.
7. [[S-18 - Nakamura 2004 NIPPON DATA80 - Egg consumption and a U-shaped mortality relationship in a Japanese national cohort]] — smaller (n≈9,263) Japanese national cohort; U-shaped rather than monotonic — both very-low and very-high egg intake carry higher mortality than ~1/day. Smallest N and oldest of the seven, but a useful nonlinearity flag.

Balance check: 2 harm / 2 null / 3 protective-or-nonlinear — matches the brief's requirement not to let either side dominate, and covers both of its named anchors on each side (Zhong + Djoussé for harm; PURE + Harvard-null + a China-Kadoorie/Japan pair on the other side).

## search_scope

1. Started from the orchestrator's `00-search-plan.md`, which already named specific target papers per cohort family (Harvard NHS/NHSII/HPFS, US-pooled/Zhong 2019, PURE/Dehghan 2020, China Kadoorie/Qin 2018, Physicians'/Djoussé 2008) — went directly to targeted WebSearch queries for each named paper rather than first mining the listed discovery hubs' reference lists (Rong 2013, Shin 2013, Krittanawong 2021, Godos 2021, Alexander 2016). This is a deliberate shortcut given the target-run's time pressure: the hubs would very likely have surfaced the same primaries the brief already named. Net effect: reference-list snowballing from those five hubs specifically was **not** done; if the real run wants more coverage beyond the 7 named families, that snowball is still owed.
2. Targeted WebSearch per family for the two families the brief left unnamed: "EPIC study egg consumption cardiovascular disease mortality," then "Key 2019 Circulation EPIC" once the paper surfaced; "Japan JACC/JPHC egg consumption mortality," which surfaced NIPPON DATA80 as a cleaner dedicated primary than JACC/JPHC itself.
3. Also searched "UK Biobank egg consumption cardiovascular disease mortality" (no clean dedicated primary found — see exclusions) and "Guangzhou Biobank egg consumption" (found a usable but redundant-with-budget Chinese alternative).
4. Metadata/verification: Europe PMC REST API (`ebi.ac.uk/europepmc/webservices/rest/search`, title and PMID lookups, `resultType=core`) for citation counts (asof 2026-07-20), DOIs, journal/year, author lists, and abstracts — Semantic Scholar's API was tried first but rate-limited (HTTP 429) throughout, so I switched to Europe PMC, which worked cleanly. WebFetch on PMC full-text pages for funding/COI statements on the 3 most load-bearing sources (Zhong 2019, Drouin-Chartier 2020, Qin 2018); the other 4 got a lower-confidence best-effort motivatedness note rather than a full-text pull, given the read budget.

## exclusions

1. Qin et al., "Regarding associations of egg consumption with cardiovascular disease..." (PMID 30309864) — a response/commentary letter on S-13, not primary data; excluded as non-primary.
2. Guangzhou Biobank Cohort Study (Zhang/Xu et al., Eur J Nutr 2019; 28,024 participants, null finding) — a genuine distinct Chinese cohort, found and skimmed, but dropped for budget: China Kadoorie Biobank already fills the "Chinese cohort" slot at far larger N (0.5M vs 28k). Good candidate to add in a production run for extra China-side replication.
3. Nakamura et al. 2018 Eur J Clin Nutr ("Re-evaluation... in Japanese women") and Nakamura et al. 2006 BJN (JPHC study, CHD incidence) — alternative Japan-family primaries, found via search; excluded as redundant with NIPPON DATA80 (already the slice's Japan representative; one primary per family).
4. Japan Collaborative Cohort (JACC) dairy/animal-food dietary-pattern paper — examines food patterns broadly, doesn't isolate egg intake as its own exposure; out of scope.
5. SUN Project (Zazpe et al., Eur J Clin Nutr 2011, "Egg consumption and risk of cardiovascular disease in the SUN Project") — a named-optional family in the brief; surfaced incidentally in another search but not pursued/read, budget already committed to the higher-priority named families.
6. Korea (KoGES/KNHANES) and Rotterdam Study — named-optional families in the brief; not actively searched, same reason as #5.
7. Nothing from this slice was found to clearly belong to slice 1 (mechanism-surrogate) or slice 3 (heterogeneity-subgroup-dose) during search, so no cross-slice hand-offs were needed.

## Slice paragraph

7 sources, 7 distinct cohort families, no re-analysis of the same cohort minted twice. Shape: 3 US (Harvard NHS/NHSII/HPFS null; NHLBI 6-cohort pooled harm; Physicians' Health Study harm-in-mortality), 1 global-multinational (PURE, null, 50 countries), 2 East Asian (China Kadoorie protective at 0.5M; Japan NIPPON DATA80 U-shaped at ~9k), 1 European (EPIC, weakly/fragile-protective). This hits essentially every named target family from the brief except UK Biobank: searched specifically but could not find a UK Biobank paper that isolates egg intake as its own hard-endpoint exposure (only broader dietary-pattern analyses that fold eggs into a pattern score) — a real gap, not a considered drop, flag it if a production run wants that family too. The slice as it stands already carries the debate's real shape: the harm signal is largely a US-cohort (and specifically a dietary-cholesterol-adjustment-sensitive) phenomenon, while the largest non-US cohorts (China Kadoorie at 0.5M, PURE at 146k+31k across 50 countries) are null-to-protective — a pattern worth flagging for step 3/4 as a candidate moderator (region / baseline diet) rather than pure noise.
