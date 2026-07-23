# Structure note (step 4b) — egg-health case

- **H in (step-3):** 44
- **active (paper-derived survivors, 4a):** 39
- **merged:** 5 (H-13, H-14, H-25, H-32, H-37 — in `hypotheses/merged/`)
- **dropped:** 0
- **clusters (HC):** 15
- **4b-minted structural members:** 15 (11 residual `H-49…H-59`, 4 constructed `H-45…H-48`), all `active` ⇒ **54 active H files** total, each in exactly one cluster
- **generated:** 2026-07-23

## Cluster inventory (top-level map)

Each HC is one sub-question whose members are its mutually-exclusive answers (ordered ascending-id, residual last — the frozen index for steps 7-8). `r` = residual (`step-4-residual`), `c` = constructed complement (`step-4-constructed`).

1. [[HC-1 - Overall net effect of moderate habitual egg intake on cardiovascular disease and mortality]] — What is the net causal effect (sign/shape) of moderate egg intake on CVD/mortality? — H-6 (protective), H-21 (neutral), H-27 (harmful), H-44 (U-shaped), H-49r.
2. [[HC-2 - Regional-population modification of the egg-cardiovascular association]] — Is the egg-CVD effect genuinely region-modified, or is the Asian inverse an artefact? — H-7 (confounded artefact), H-22 (real modification), H-50r.
3. [[HC-3 - Effect of habitual egg intake on incident type-2 diabetes]] — Does egg intake causally raise incident T2D, and how uniformly? — H-8 (region-dependent), H-9 (null / Western-pattern confounding), H-51r.
4. [[HC-4 - Cardiometabolic effect of eggs in people with diabetes, prediabetes, or metabolic syndrome]] — In dysglycemic people, is egg intake net-harmful, safe, or beneficial? — H-4 (RCT-safe), H-19 (glycemically favourable), H-24 (CVD harm), H-33 (harm mechanism), H-52r.
5. [[HC-5 - Operative exposure behind the egg-cardiovascular association]] — Is the operative agent egg-cholesterol or accompanying fat quality? — H-3 (fat quality dominates), H-26 (dietary cholesterol), H-54r.
6. [[HC-6 - Effect of egg-egg-cholesterol intake on the atherogenic blood-lipid profile]] — Does egg/egg-cholesterol worsen the atherogenic lipid profile? — H-20 (LDL worse vs carb), H-34 (linear LDL/apoB rise), H-40 (net-neutral/HDL-favourable), H-53r.
7. [[HC-7 - Nature of inter-individual variation in cholesterol response to dietary cholesterol]] — What is the structure of responder variation, and is it identifiable? — H-1 (discrete hypo/hyper), H-2 (feedback-buffering mechanism), H-35 (continuous trait), H-36 (ApoE non-predictive), H-55r.
8. [[HC-8 - Causal status of elevated TMAO for human atherosclerosis]] — Is TMAO itself causally atherogenic in humans? — H-15 (animal-model mechanism), H-16 (human causal), H-45c (non-causal marker). *[exhaustive]*
9. [[HC-9 - Whether habitual egg intake produces a harm-relevant TMAO elevation]] — Does egg intake raise TMAO enough to matter, and when? — H-28 (form-limited), H-29 (no fasting rise), H-30 (renal-only), H-42 (real postprandial rise), H-43 (rise benign), H-56r.
10. [[HC-10 - Intrinsic versus comparator-background-diet contingency of egg-health (is the verdict well-posed)]] — Is egg-health intrinsic or comparator/context-contingent (is the verdict well-posed)? — H-17 (intrinsically unhealthy), H-18 (ill-posed/contingent), H-23 (substitution-indexed), H-38 (background-diet-indexed), H-57r.
11. [[HC-11 - Whether early egg introduction causally prevents egg allergy in high-risk infants]] — Does early egg introduction causally prevent allergy? — H-10 (causal prevention), H-46c (no causal prevention). *[exhaustive]*
12. [[HC-12 - Intact Grade A shell eggs as the major internally-contaminated vehicle of the Salmonella enteritidis epidemic]] — Are intact Grade A eggs the major, internally-contaminated SE vehicle? — H-11 (internal route), H-12 (major vehicle), H-58r.
13. [[HC-13 - Whether eggs enhance satiety beyond their protein content]] — Do eggs boost satiety beyond protein? — H-5 (beyond protein), H-47c (protein-only). *[exhaustive]*
14. [[HC-14 - Whether dietary choline is an essential nutrient for humans]] — Is dietary choline essential for humans? — H-39 (essential), H-48c (not essential). *[exhaustive]*
15. [[HC-15 - Whether nutritional-cohort associations can support causal egg-health claims]] — Can nutritional cohorts support causal egg-health claims? — H-31 (cannot / reform), H-41 (can / defence), H-59r.

## Carving notes

1. **Two-axis CVD decomposition.** Overall sign/shape (HC-1), regional modification (HC-2), and intrinsic-vs-contingent framing (HC-10) are kept as separate orthogonal questions rather than one, with their premise-dependences logged in `depends_on` (HC-1↔HC-2, HC-1↔HC-10, HC-2↔HC-10). H-6 (protective) anchors HC-1; its Kadoorie foil H-7 (confounding) anchors HC-2 — the causal-vs-confounding contrast is expressed across the two axes, not duplicated as one partition.
2. **Task-mandated competing pairs kept inside one cluster:** H-42 vs H-29 (TMAO postprandial-rise vs fasting-null) → HC-9; H-1 vs H-35 (discrete vs continuous responder distribution) → HC-7; H-17 vs H-18/H-23 (intrinsic vs comparator-contingent) → HC-10.
3. **Same-source split by endpoint.** H-19 (glycemic) → HC-4 and H-20 (LDL) → HC-6, both from the Maki trial: their endpoints co-hold and so cannot be exclusive members of one probability space.
4. **TMAO split into exposure (HC-9) and causality (HC-8)** as genuinely different sub-questions; strong `depends_on` between them (exposure matters only if TMAO is causal). HC-8 uses an ordinal-rung reading (animal-mechanism / human-causal / marker) to stay exclusive and exhaustive.
5. **Beyond-CVD channels are separate MECE clusters** (allergy HC-11, salmonella HC-12, satiety HC-13, choline HC-14) rather than a non-exclusive grab-bag; each single-active-hypothesis channel is paired with a constructed null complement (exhaustive) — except salmonella, whose two facets (route H-11, magnitude H-12) share the thesis and take a residual negation.
6. **Meta-question (HC-15)** cross-cuts every cohort-based cluster but enters downstream via source trust / likelihoods (steps 5, 8), not via other clusters' priors, so those priors still factorize and its `depends_on` is empty.
7. **No H dropped** — all 39 active clustered. **No numbers/priors/weights** written anywhere in the HC layer (descriptive effect sizes/intakes quoted in carving prose only, mirroring the H statements).
