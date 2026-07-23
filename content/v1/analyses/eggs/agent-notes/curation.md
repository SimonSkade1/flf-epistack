# Curation note (step 2b) — egg-health case

- **initial_count:** 101 (`source` nodes S-1…S-101, contiguous)
- **live_count:** 98 (three TRUE duplicates flagged `duplicate_of`: S-56→S-25, S-71→S-48, S-79→S-53)
- **curated_target_N:** 25 (soft; coverage + quality first)
- **curated_count:** 28
- **generated:** 2026-07-23

## trust_baseline

**0.70** (set by the orchestrator; not lowered further here).

Rationale: the cut normally uses baseline 0.8, and the spec says to lower it as a corpus-fit knob when little clears it. Here the reduction is kept deliberately minimal — only 0.10 below default, **not** the 0.5–0.6 corpus-fit drop the spec would otherwise license — so that "curated" still means genuinely reliable data (the `trust_score` each source carries is what downstream Bayesian steps rest on). At 0.70, the strong tier (feeding/metabolic-ward + methodology sources up to ~0.85, plus the best nutrition-epi cohorts ~0.72–0.82) ranks cleanly and 24 sources clear the baseline, yielding ~25 by rank before coverage adjustments. `combined_score = usefulness · (trust_score − 0.70)` is written on all 101 sources.

Comparability: the ten 2a scorers' slices were checked against the consolidated overview and read as mutually consistent (nutrition-epi ~0.5–0.72; feeding/metabolic-ward + methodology up to ~0.85). No slice was systematically high or low, so **no trust rescore was applied** — scores are kept as scored. Trust was never deflated to fit the cut.

## scoring_rubric

- `trust_score ∈ [0,1]`: probability the key finding survives a clean well-powered replication with a similar effect — judged from design/statistics/corroboration, never from whether the conclusion is believable or surprising. Carried downstream as each source's data-reliability.
- `usefulness ~1–5` (log scale): how much the data would move the main question *if true*.
- Cut key: `combined_score = usefulness · (trust_score − 0.70)`; `≤ 0 ⇒ below baseline`. Ranking is arithmetic; departures are coverage/skew decisions logged below.

## D-node reconciliation (job 1, done before the cut)

Parallel 2a scorers minted duplicate `data-basis` nodes for the same dataset. Merged by dataset identity (survivor = lowest id; every source's `data_basis` repointed to the survivor; merged nodes moved to `data-bases/merged/`, none deleted):

| merged | → survivor | dataset | repointed source |
|---|---|---|---|
| D-5 | D-2 | Physicians' Health Study | S-1 |
| D-19 | D-7 | Harvard NHS/NHSII/HPFS | S-19 |
| D-23 | D-9 | Cohort of Swedish Men | S-45 |
| D-17 | D-12 | China Health & Nutrition Survey | S-13 |
| D-18 | D-13 | EPIC | S-16 |
| D-15 | D-11 | Million Veteran Program | S-66 |

Result: 18 live D nodes (down from 24), each with ≥1 inbound `data_basis`, no two live D nodes representing the same dataset, and no lingering references to a merged id. All other D nodes are singletons and were left as-is (D-1 LRPP, D-3 DIABEGG, D-4 Cleveland GeneBank, D-6 WHS, D-8 Jackson Heart, D-10 JPHC, D-14 China Kadoorie, D-16 KoGES, D-20 PREDIMED, D-21 SUN, D-22 Ginsberg, D-24 Swedish Mammography).

**Fernandez / UConn feeding-lab cluster (correlated, NOT merged):** S-30, S-32, S-36, S-72, S-55 (responder subject-pool series) and same-lab distinct-cohort trials S-48, S-53, S-43, S-64, S-59, S-67 are distinct trials sharing lab/PI/protocol and mostly Egg Nutrition Center / American Egg Board funding. They keep self-links (`[[S-N]]`), not a shared D — but step 5 should treat them as **correlated on lab practice + COI** (already in `motivatedness`). Only one member (S-67 Mutungi) is curated, so the concentration does not enter the cut; the rest are non-curated.

## angle normalization (before the skew check)

Scorer-introduced variants were collapsed to one consistent 15-tag set (`curation_select.py` groups on `angle`): `egg-diabetic-subgroup → diabetic-interaction` (S-14, S-16, S-17); `allergy-rct`/`allergy-epi → allergy` (S-15, S-18); `global-cohort → asian-cohort` (S-91 PURE, folded into the non-Western/multinational cohort bucket); `dietary-pattern → asian-cohort` for the multinational MI cohort (S-93 INTERHEART) and `→ methodology-critique` for the confounding-demonstration (S-101 MESA dietary-pattern). Final vocabulary: western-cohort, asian-cohort, egg-T2D-cohort, diabetic-interaction, feeding-rct-lipids, responder-genotype, egg-rct-clinical, tmao-mechanism, tmao-null, nutrition-benefit, foodborne-harm, allergy, methodology-critique, methodology-defence, substitution.

## The cut

Coverage-first, because the question is contested and multi-sided. Core = the 24 sources with `combined_score > 0` (trust > 0.70). Of these, 16 were kept and 8 were dropped (feeding-rct-lipids and methodology-critique each capped at ~3–4 curated; plus two same-position redundancies). 12 below-baseline sources were added as logged coverage-includes so that every contested position carries ≥1 curated source. Final skew: **no `angle` exceeds 3 curated members and no `data_basis` exceeds 2** — well under the ~4 ceiling; the script reports no strong skew on the pool. Curated stay in `sources/`; the 73 non-curated (3 duplicates + 8 skew/redundancy trims + 62 below-baseline) moved to `sources/non-curated/`. Nothing deleted, no id renumbered.

### Final curated set (28), by position

1. Western CVD harm — **S-21** (coverage)
2. Western CVD null — **S-19** (core); global null **S-91** (core)
3. Asian/multinational protective — **S-80** (coverage); multinational null **S-91** (core)
4. Asian within-region heterogeneity (U-shape, "at what level") — **S-81** (coverage)
5. egg-T2D US-elevated — **S-4** (core)
6. egg-T2D null/inverse — **S-8** European (core), **S-9** Asian/Japan (coverage)
7. Diabetic-subgroup CVD interaction — **S-14** (coverage)
8. Lipid feeding LDL-up mechanism — **S-49**, **S-42** (core)
9. Lipid feeding HDL-up (pro-egg) — **S-67** (coverage)
10. Responder hypo/hyper — **S-25** (core)
11. ApoE genotype ("for whom") — **S-62** (coverage)
12. Egg RCT in diabetics (safe, interventional) — **S-26** (coverage)
13. Egg RCT adverse counterweight — **S-57** (coverage)
14. TMAO harm — **S-28**, **S-47** (core)
15. TMAO null-from-eggs — **S-60** (core)
16. Beyond-CVD benefit (choline essentiality) — **S-7** (core)
17. Allergy — **S-15** prevention RCT, **S-18** prevalence (core)
18. Foodborne — **S-20** (core)
19. Methodology critique — **S-99** (measurement), **S-94** (confounding), **S-95** (reform viewpoint) (S-99/S-94 core, S-95 coverage)
20. Methodology defence — **S-100** (coverage)
21. Substitution — **S-89** (coverage), plus **S-57** (substitution-angle)

Angle distribution (all ≤3): egg-T2D-cohort 3, feeding-rct-lipids 3, asian-cohort 3, methodology-critique 3, allergy 2, western-cohort 2, responder-genotype 2, tmao-mechanism 2, substitution 2; diabetic-interaction / methodology-defence / foodborne-harm / egg-rct-clinical / tmao-null / nutrition-benefit 1 each.
Shared data_basis in the cut (correlated pairs step 5 must not double-count): **D-7** = S-4 + S-19 (Harvard cohorts); **D-1** = S-21 + S-89 (Zhong 6-cohort pool). Everything else is a unique D or a self-link.

### coverage_includes (12; each `combined_score ≤ 0`, trust kept as scored)

This is a deliberate, documented extension of the cut's single-exception default: covering a contested multi-sided question needs several. Each keeps its low `trust_score` so downstream steps still discount it.

| id | trust | combined | position / reason |
|---|---|---|---|
| S-21 | 0.57 | −0.52 | Western CVD harm anchor (Zhong 6-cohort dose-response) — no harm-direction Western source is core |
| S-80 | 0.60 | −0.38 | Asian protective anchor (China Kadoorie) — protective verdict-direction otherwise unrepresented |
| S-81 | 0.68 | −0.08 | Asian within-region U-shape (China-PAR) — only nonlinearity source, the "at what level" clause |
| S-9 | 0.65 | −0.13 | egg-T2D Asian null (JPHC) — Asian pole of the first-class US-vs-Asia axis |
| S-14 | 0.55 | −0.48 | diabetic-subgroup CVD interaction (Jang, HR 2.81) — "for whom (diabetics)" |
| S-26 | 0.70 | 0.00 | DIABEGG RCT — sole interventional "high-egg safe in T2D" anchor |
| S-57 | 0.62 | −0.23 | Maki adverse-LDL substitution — the one counterweight to the null-to-beneficial egg-RCT slice |
| S-62 | 0.60 | −0.32 | Weggemans ApoE null (largest pool) — the "for whom (genotype)" disagreement |
| S-67 | 0.55 | −0.41 | Mutungi whole-egg-raises-HDL — pro-egg lipid side otherwise absent (Fernandez/ENC-AEB COI) |
| S-89 | 0.62 | −0.30 | Zhong substitution analysis — substitution position otherwise unrepresented (shares D-1 with S-21) |
| S-95 | 0.60 | −0.30 | Ioannidis "nutritional-epi needs reform" — the meta-level critique viewpoint explicitly required |
| S-100 | 0.62 | −0.22 | Satija defence of nutritional-epi — balances the critique cluster |

### rank_departures

**Coverage-includes added out of rank (below-baseline):** S-21, S-80, S-81, S-9, S-14, S-26, S-57, S-62, S-67, S-89, S-95, S-100 (see table above).

**Core (combined > 0) dropped from the rank-cut:**
- S-1 (0.06) — redundant with S-4 on the US-elevated egg→T2D position (same direction); dropped for coverage room.
- S-45 (0.07) — redundant with S-19 on the Western-null position; dropped for coverage room.
- S-35 (0.25) — feeding-rct-lipids skew cap; Sacks LDL-rise redundant with kept Keys/Ginsberg.
- S-44 (0.20) — feeding-rct-lipids skew cap; shares D-22 (Ginsberg) with kept S-42, dropped for independence.
- S-52 (0.41) — feeding-rct-lipids skew cap; Mattson metabolic-ward dose-response redundant with kept Keys equation.
- S-90 (0.45) — methodology-critique skew cap; substitution-caution overlaps kept substitution (S-89) and critique set.
- S-97 (0.34) — methodology-critique skew cap; cookbook-test data-dredging critique overlaps kept OPEN/E-value/Ioannidis.
- S-98 (0.05) — methodology-critique skew cap; GRADE red-meat template carries no egg data.

**Skew consciously accepted:** none outstanding. The two capped angles (feeding-rct-lipids, methodology-critique) are trimmed to 3 curated each; no angle > 3 and no data_basis > 2 in the final cut, so `curation_select.py` reports no strong skew. The `field` dimension is dominated by nutrition/epidemiology sub-labels — inherent to the question, not a correctable skew. The only correlated pairs (D-7, D-1) are intentional and handed to step 5 via shared D-node identity.

## step1_corrections

Factual errors the 2a scorers found in step-1 summaries (so step 3 reads the paper, not the wrong summary). For the three that ended up curated, a one-line `**Correction (2a read):**` was appended to the node body (additive):

1. **S-9 Kurotani 2014 (JPHC)** — NULL egg→T2D in both sexes. The "40% lower risk in men" was a mis-summary; the inverse OR was for **dietary cholesterol in postmenopausal women**, not eggs. *(appended — curated)*
2. **S-42 Ginsberg 1994** — a 20-man, 8-week crossover feeding **0/1/2/4 eggs/day (128–858 mg cholesterol/d)**, not a "P:S-ratio 0/750/1500 mg" design. *(appended — curated)*
3. **S-47 Miller 2014** — an **n=6** within-subject dose-response (0/1/2/4/6 yolks), not a larger-n trial. *(appended — curated)*
4. **S-16 Trichopoulou 2006** — the egg-specific HR is secondary-sourced (via the DMSO diabetic-CVD review), not the paper's headline endpoint. *(recorded only — non-curated)*
5. **S-92 Djoussé 2021** — a 9-US-cohort pooling (not Harvard-dominant); self-linked, and shares MESA with S-101. *(recorded only — non-curated)*

## curation_select.py output (baseline 0.70, target-n 25) — pasted

```
baseline 0.70 | 101 scored | 24 clear the baseline | cut = top 25

RANKING  (* = in the prospective cut)
    id        comb  trust   use  title
  * S-19      0.50   0.82   4.2  Drouin-Chartier 2020 BMJ - egg consumption and CVD i
  * S-99      0.50   0.85   3.3  The OPEN study- how much self-reported diet data act
  * S-49      0.48   0.85   3.2  Keys, Anderson & Grande 1965 Metabolism — foundation
  * S-20      0.46   0.83   3.5  St Louis 1988 - Emergence of grade A eggs as a major
  * S-90      0.45   0.85   3.0  Why substitution analysis in nutritional epidemiolog
  * S-52      0.41   0.85   2.7  Mattson, Erickson & Kligman 1972 AJCN — Procter & Ga
  * S-15      0.40   0.80   4.0  Natsume 2017 - PETIT trial- two-step egg introductio
    S-56      0.36   0.82   3.0  McNamara et al. 1987 JCI — heterogeneity of choleste  [duplicate]
  * S-42      0.34   0.82   2.8  Ginsberg 1994 Arterioscler Thromb — dose-response of
  * S-97      0.34   0.82   2.8  The cookbook test- almost every ingredient is 'linke
  * S-94      0.33   0.83   2.5  The E-value- how much unmeasured confounding would i
  * S-4       0.32   0.78   4.0  Drouin-Chartier 2020 AJCN - egg consumption and T2D
  * S-91      0.32   0.78   4.0  PURE study- egg intake, blood lipids, CVD and mortal
  * S-35      0.25   0.80   2.5  Sacks 1984 Lancet — egg feeding raises LDL and ApoB
  * S-18      0.20   0.78   2.5  Eggesbo 2001 - Population-based prevalence of egg al
  * S-44      0.20   0.78   2.5  Ginsberg 1995 ATVB — dietary cholesterol-egg dose-re
  * S-8       0.18   0.75   3.5  Wallin 2016 Diabetologia - egg consumption and T2D i
  * S-28      0.09   0.72   4.3  Gut flora metabolism of phosphatidylcholine promotes
  * S-47      0.08   0.73   2.8  Effect of egg ingestion on trimethylamine-N-oxide pr
  * S-25      0.07   0.72   3.3  McNamara et al 1987 - Heterogeneity of cholesterol h
  * S-45      0.07   0.72   3.3  Larsson, Akesson and Wolk 2015 AJCN - egg consumptio
  * S-60      0.06   0.72   3.2  Dietary choline supplements, but not eggs, raise fas
  * S-1       0.06   0.72   3.0  Djoussé 2009 Diabetes Care - egg consumption and T2D
  * S-7       0.05   0.72   2.5  Zeisel 1991 - Choline, an essential nutrient for hum
  * S-98      0.05   0.72   2.3  GRADE-ing red-meat RCT evidence as a template for re
    S-26      0.00   0.70   3.5  DIABEGG 3-month RCT — high-egg vs low-egg diet in pr  [below baseline]
    S-22      0.00   0.70   3.3  Katan and Beynen 1986 - Existence of consistent hypo  [below baseline]
    S-31      0.00   0.70   2.8  DIABEGG weight-loss and 12-month follow-up phase in   [below baseline]
    S-68      0.00   0.70   3.4  TMAO response to animal source foods varies among he  [below baseline]
    S-87      0.00   0.70   3.3  Japan Public Health Center cohort- egg intake not li  [below baseline]
    S-92      0.00   0.70   3.5  Egg-diabetes-CHD risk after adjusting for overall di  [below baseline]
    S-63     -0.06   0.68   2.8  Quintao, Grundy & Ahrens 1971 JLR — dietary choleste  [below baseline]
    S-39     -0.06   0.68   3.0  Intestinal microbiota metabolism of L-carnitine, a n  [below baseline]
    S-83     -0.06   0.68   3.0  Guangzhou Biobank Cohort Study egg consumption and C  [below baseline]
    S-40     -0.06   0.68   3.2  Gut microbial metabolite TMAO enhances platelet hype  [below baseline]
    S-48     -0.06   0.68   3.2  Intake of up to 3 eggs-day increases HDL cholesterol  [below baseline]
    S-81     -0.08   0.68   4.0  China-PAR project- U-shaped egg intake vs incident C  [below baseline]
    S-29     -0.08   0.68   4.0  Intestinal microbial metabolism of phosphatidylcholi  [below baseline]
    S-78     -0.09   0.65   1.8  Crowe et al 2013 AJCN - ischemic heart disease risk   [below baseline]
    S-9      -0.13   0.65   2.6  Kurotani 2014 BJN - cholesterol and egg intakes and   [below baseline]
    S-17     -0.15   0.65   3.0  Díez-Espino 2017 Clinical Nutrition - egg consumptio  [below baseline]
    S-33     -0.19   0.65   3.8  Key et al 2019 Circulation - meat, fish, dairy, and   [below baseline]
    S-101    -0.21   0.62   2.6  Eggs load onto the same 'Western' dietary pattern as  [below baseline]
    S-100    -0.22   0.62   2.7  In defence of nutritional epidemiology's methods and  [below baseline]
    S-93     -0.22   0.60   2.2  INTERHEART- eggs within the 'Western' dietary patter  [below baseline]
    S-32     -0.23   0.60   2.3  Herron et al 2002 J Am Coll Nutr - Pre-menopausal wo  [below baseline]
    S-41     -0.23   0.60   2.3  Dawber et al 1982 AJCN - eggs, serum cholesterol, an  [below baseline]
    S-57     -0.23   0.62   2.9  Substituting eggs for high-carbohydrate breakfast fo  [below baseline]
    S-50     -0.24   0.62   3.0  Abdollahi et al 2019 AJCN - egg and cholesterol inta  [below baseline]
    S-11     -0.25   0.60   2.5  Lee & Kim 2018 Nutrition Research and Practice - egg  [below baseline]
    S-12     -0.25   0.60   2.5  van Vliet 2017 - Whole eggs versus egg whites and po  [below baseline]
    S-53     -0.26   0.60   2.6  Greene et al 2006 Nutr Metab - Plasma LDL and HDL ch  [below baseline]
    S-10     -0.27   0.60   2.7  Vishwanathan 2009 - Egg yolks increase macular pigme  [below baseline]
    S-54     -0.27   0.60   2.7  Nettleton et al 2008 J Am Diet Assoc - egg, whole-gr  [below baseline]
    S-69     -0.27   0.62   3.4  TMAO is associated with mortality- impact of modestl  [below baseline]
    S-58     -0.28   0.60   2.8  Qureshi et al 2007 Med Sci Monit - regular egg consu  [below baseline]
    S-2      -0.30   0.55   2.0  Vander Wal 2005 - Short-term effect of eggs on satie  [below baseline]
    S-95     -0.30   0.60   3.0  The case that nutritional-epidemiology cohort method  [below baseline]
    S-89     -0.30   0.62   3.8  Substitution analysis- replacing eggs with other pro  [below baseline]
    S-62     -0.32   0.60   3.2  Weggemans, Zock, Ordovas, Pedro-Botet and Katan 2001  [below baseline]
    S-51     -0.33   0.55   2.2  Selenium-enriched vs zeaxanthin-enriched eggs in T2D  [below baseline]
    S-36     -0.34   0.55   2.3  Herron et al 2004 Metabolism - High cholesterol inta  [below baseline]
    S-59     -0.34   0.55   2.3  Effects of egg consumption and choline supplementati  [below baseline]
    S-24     -0.35   0.60   3.5  USDA-FSIS Salmonella Enteritidis risk assessment for  [below baseline]
    S-82     -0.36   0.58   3.0  Katz et al. 2005 Int J Cardiol — egg vs. oatmeal cro  [below baseline]
    S-61     -0.37   0.55   2.5  Eggs in plant-based diets, cardiometabolic risk in a  [below baseline]
    S-80     -0.38   0.60   3.8  China Kadoorie Biobank egg consumption and CVD (Qin   [below baseline]
    S-66     -0.38   0.58   3.2  Djousse et al 2020 Clinical Nutrition - egg consumpt  [below baseline]
    S-6      -0.39   0.55   2.6  Djoussé 2016 Clinical Nutrition - egg consumption an  [below baseline]
    S-34     -0.40   0.50   2.0  One egg-day vs oatmeal breakfast crossover trial in   [below baseline]
    S-38     -0.40   0.50   2.0  Zazpe et al 2011 Eur J Clin Nutr - egg consumption a  [below baseline]
    S-55     -0.40   0.50   2.0  Missimer, DiMarco and Fernandez 2019 Curr Dev Nutr -  [below baseline]
    S-67     -0.40   0.55   2.7  Mutungi et al. 2008 J Nutr — egg-derived cholesterol  [below baseline]
    S-30     -0.42   0.55   2.8  Herron et al 2003 J Nutr - Men classified as hypo- o  [below baseline]
    S-74     -0.42   0.55   2.8  Kern 1991 NEJM - Normal plasma cholesterol in an 88-  [below baseline]
    S-70     -0.43   0.55   2.9  Lopez-Miranda et al 1994 J Lipid Res - Effect of apo  [below baseline]
    S-73     -0.43   0.55   2.9  Njike et al. 2010 Nutrition Journal — daily egg cons  [below baseline]
    S-13     -0.45   0.55   3.0  Wang, Li and Shi 2020 BJN - higher egg consumption a  [below baseline]
    S-43     -0.45   0.55   3.0  Whole egg vs egg substitute in carbohydrate-restrict  [below baseline]
    S-88     -0.45   0.55   3.0  NIPPON DATA80- egg consumption, cholesterol, and cau  [below baseline]
    S-75     -0.45   0.52   2.5  Kim & Campbell 2018 Nutrients — dietary cholesterol   [below baseline]
    S-14     -0.48   0.55   3.2  Jang 2018 Nutrition and Diabetes - egg consumption a  [below baseline]
    S-84     -0.48   0.55   3.2  Rural China (Anhui) 14-year cohort- high egg intake   [below baseline]
    S-64     -0.48   0.50   2.4  Eggs plus spinach in a plant-based diet, metabolic s  [below baseline]
    S-27     -0.49   0.55   3.3  Djousse and Gaziano 2008 AJCN - egg consumption, CVD  [below baseline]
    S-76     -0.49   0.55   3.3  Al-Ramady et al 2022 Clin Nutr ESPEN - egg consumpti  [below baseline]
    S-86     -0.50   0.52   2.8  China Family Panel Studies nationwide cohort- egg in  [below baseline]
    S-37     -0.52   0.50   2.6  Energy-restricted high-protein diet with eggs vs lea  [below baseline]
    S-21     -0.52   0.57   4.0  Zhong 2019 JAMA - dietary cholesterol-egg consumptio  [below baseline]
    S-46     -0.54   0.50   2.7  One egg-day vs egg substitute in pre--type-2-diabete  [below baseline]
    S-77     -0.54   0.50   2.7  Vorster et al. 1992 AJCN — egg intake does not chang  [below baseline]
    S-16     -0.56   0.50   2.8  Trichopoulou 2006 J Intern Med - diet, physical acti  [below baseline]
    S-79     -0.56   0.50   2.8  Greene et al. 2006 Nutrition & Metabolism — egg feed  [below baseline]
    S-85     -0.58   0.52   3.2  China Health and Nutrition Survey- habitual egg inta  [below baseline]
    S-71     -0.59   0.48   2.7  DiMarco et al. 2017 Lipids — dose-escalation egg RCT  [below baseline]
    S-65     -0.66   0.48   3.0  Sarkkinen et al 1998 AJCN - Effect of apolipoprotein  [below baseline]
    S-3      -0.67   0.45   2.7  Vander Wal 2008 - Egg breakfast enhances weight loss  [below baseline]
    S-23     -0.70   0.42   2.5  Djousse and Gaziano 2008 Circulation - egg consumpti  [below baseline]
    S-96     -0.87   0.40   2.9  The 'fatal flaws' case against food-frequency-questi  [below baseline]
    S-5      -0.92   0.42   3.3  Caudill 2018 - Maternal choline supplementation impr  [below baseline]
    S-72     -0.95   0.36   2.8  Herron et al 2006 J Nutr - The ABCG5 polymorphism co  [below baseline]

REPRESENTATION OF THE CUT
  angle:
    methodology-critique              5/24 of cut, 5 in pool
    feeding-rct-lipids                5/24 of cut, 5 in pool
    egg-T2D-cohort                    3/24 of cut, 3 in pool
    western-cohort                    2/24 of cut, 2 in pool
    allergy                           2/24 of cut, 2 in pool
    tmao-mechanism                    2/24 of cut, 2 in pool
    foodborne-harm                    1/24 of cut, 1 in pool
    asian-cohort                      1/24 of cut, 1 in pool
    responder-genotype                1/24 of cut, 1 in pool
    tmao-null                         1/24 of cut, 1 in pool
    nutrition-benefit                 1/24 of cut, 1 in pool
  data_basis:
    unknown                           3/24 of cut, 3 in pool
    D-22                              2/24 of cut, 2 in pool
    (remaining values 1/24 each)

  No strong skew detected in the prospective cut.
```

Note: the pasted ranking is the script's pure-rank prospective cut (top-24 that clear baseline 0.70). The **applied** cut departs from it per the coverage-first mandate above — 8 of those 24 were trimmed (skew caps + two redundancies) and 12 below-baseline coverage-includes were added — giving the final 28. The script's angle skew flags (feeding-rct-lipids 5, methodology-critique 5) are resolved in the applied cut, where each is trimmed to 3.
