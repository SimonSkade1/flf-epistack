# Consolidated pool overview (step 1c) — egg-health case

Main question (verbatim): "Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?"

This is step 2b's entry point. It is **not** a graph node. It holds: (a) the whole live source pool as wikilinks grouped best-first by slice; (b) the deduped union of all 9 searchers' exclusions; (c) the duplicate resolutions; (d) the shared-data-basis clusters step 2 should mint `D` nodes for; (e) a pool-shape paragraph; and a closing balance/independence audit.

- **Pool minted:** S-1 … S-101 (contiguous, 101 candidate `source` nodes).
- **Live (non-duplicate) sources: 98.** Three nodes are TRUE duplicates flagged `duplicate_of` (S-56→S-25, S-71→S-48, S-79→S-53); step 2b sets those `curated:false` and moves them aside.
- `curated_target_N` = 25.

---

## (a) The live pool — best-first within topic/slice group

Ordering inherits each searcher's own quality×usefulness ranking. Duplicate-side nodes are listed in their minting slice, marked `[DUP → survivor]`; their survivors are listed (unmarked) in the slice that minted the survivor.

### Slice 1 — Western (US + European) CVD-event & mortality cohorts (HARD)
Harm-finding (dose-response harm at higher intake):
1. [[S-21 - Zhong 2019 JAMA - dietary cholesterol-egg consumption and incident CVD and mortality, 6 pooled US cohorts.md]]
2. [[S-27 - Djousse and Gaziano 2008 AJCN - egg consumption, CVD, and mortality in the Physicians Health Study.md]]
3. [[S-54 - Nettleton et al 2008 J Am Diet Assoc - egg, whole-grain, and dairy intake and incident heart failure in ARIC.md]]
4. [[S-23 - Djousse and Gaziano 2008 Circulation - egg consumption and heart failure in the Physicians Health Study.md]]
5. [[S-66 - Djousse et al 2020 Clinical Nutrition - egg consumption and coronary artery disease in the Million Veteran Program.md]]
6. [[S-76 - Al-Ramady et al 2022 Clin Nutr ESPEN - egg consumption and acute stroke in the Million Veteran Program.md]]

Null-to-protective (moderate intake, general populations):
7. [[S-19 - Drouin-Chartier 2020 BMJ - egg consumption and CVD in NHS, NHSII, HPFS.md]]
8. [[S-33 - Key et al 2019 Circulation - meat, fish, dairy, and egg consumption and ischemic heart disease in the pan-European EPIC cohort.md]]
9. [[S-45 - Larsson, Akesson and Wolk 2015 AJCN - egg consumption and heart failure, MI, and stroke in two Swedish cohorts.md]]
10. [[S-50 - Abdollahi et al 2019 AJCN - egg and cholesterol intake and incident stroke in the Kuopio Ischaemic Heart Disease Risk Factor Study.md]]
11. [[S-41 - Dawber et al 1982 AJCN - eggs, serum cholesterol, and coronary heart disease in the Framingham Study.md]]
12. [[S-38 - Zazpe et al 2011 Eur J Clin Nutr - egg consumption and risk of cardiovascular disease in the SUN Project.md]]
13. [[S-58 - Qureshi et al 2007 Med Sci Monit - regular egg consumption and stroke-CVD risk in a US national cohort.md]]

Weaker-fit / caveated:
14. [[S-78 - Crowe et al 2013 AJCN - ischemic heart disease risk in vegetarians vs nonvegetarians in EPIC-Oxford.md]] — exposure is vegetarian-vs-nonvegetarian status, not an egg gradient; weight down as indirect.

### Slice 2 — Asian + multinational CVD/mortality cohorts (HARD)
China — general population:
1. [[S-80 - China Kadoorie Biobank egg consumption and CVD (Qin 2018 Heart).md]] — protective anchor.
2. [[S-81 - China-PAR project- U-shaped egg intake vs incident CVD and mortality (Xia 2020).md]] — nonlinearity anchor.
3. [[S-86 - China Family Panel Studies nationwide cohort- egg intake frequency and mortality (Wang 2022).md]]
4. [[S-83 - Guangzhou Biobank Cohort Study egg consumption and CVD-mortality (Xu 2019).md]] — clean null.
5. [[S-85 - China Health and Nutrition Survey- habitual egg intake raises incident CVD (Yakti 2024).md]] — clearest Chinese harm signal.
6. [[S-84 - Rural China (Anhui) 14-year cohort- high egg intake and all-cause mortality (Liu 2021).md]]

Japan:
7. [[S-87 - Japan Public Health Center cohort- egg intake not linked to CHD incidence (Nakamura 2006).md]]
8. [[S-88 - NIPPON DATA80- egg consumption, cholesterol, and cause-specific mortality (Nakamura 2004).md]]

Multinational / cross-continental:
9. [[S-91 - PURE study- egg intake, blood lipids, CVD and mortality in 50 countries (Dehghan 2020).md]] — broadest null anchor.
10. [[S-93 - INTERHEART- eggs within the 'Western' dietary pattern and MI risk across 52 countries (Iqbal 2008).md]] — weakest-fit; eggs only inside a dietary-pattern factor.

### Slice 3 — Egg intake vs incident type-2 diabetes, observational (HARD)
US cohorts — risk elevated:
1. [[S-4 - Drouin-Chartier 2020 AJCN - egg consumption and T2D in Harvard NHS-NHS II-HPFS pooling + updated meta-analysis.md]] — best-documented statement of the US/Asia/Europe region-interaction.
2. [[S-1 - Djoussé 2009 Diabetes Care - egg consumption and T2D in Physicians' Health Study and Women's Health Study.md]] — founding US primary.
3. [[S-6 - Djoussé 2016 Clinical Nutrition - egg consumption and T2D among African Americans, Jackson Heart Study.md]]

European — null/weak:
4. [[S-8 - Wallin 2016 Diabetologia - egg consumption and T2D in the Cohort of Swedish Men + updated dose-response meta-analysis.md]]

Asian — null/inverse (+ one counter-example):
5. [[S-9 - Kurotani 2014 BJN - cholesterol and egg intakes and T2D risk, Japan Public Health Center-based Prospective Study.md]]
6. [[S-11 - Lee & Kim 2018 Nutrition Research and Practice - egg consumption and lower T2D risk in Korean men, KoGES.md]]
7. [[S-13 - Wang, Li and Shi 2020 BJN - higher egg consumption and increased diabetes risk, China Health and Nutrition Survey.md]] — the Asian counter-example (China, elevated).

Diabetic-subgroup CVD/mortality interaction (thread ii):
8. [[S-14 - Jang 2018 Nutrition and Diabetes - egg consumption and CVD risk interacting with T2DM status, KoGES Ansung-Ansan.md]] — HR 2.81 in diabetics.
9. [[S-16 - Trichopoulou 2006 J Intern Med - diet, physical activity and mortality among diabetic adults in a Greek population cohort.md]] — diabetics-only, adverse.
10. [[S-17 - Díez-Espino 2017 Clinical Nutrition - egg consumption and CVD by diabetic status, PREDIMED.md]] — no interaction (tempering counter-example).

### Slice 4 — Dietary-cholesterol → serum lipids: feeding RCTs in healthy adults (SURROGATE)
Foundational metabolic-ward dose-response (Keys/Hegsted/Mattson tradition):
1. [[S-49 - Keys, Anderson & Grande 1965 Metabolism — foundational metabolic-ward dietary-cholesterol dose-response equation.md]]
2. [[S-56 - McNamara et al. 1987 JCI — heterogeneity of cholesterol homeostasis and compensatory absorption-synthesis.md]] `[DUP → S-25]`
3. [[S-52 - Mattson, Erickson & Kligman 1972 AJCN — Procter & Gamble metabolic-ward dietary-cholesterol dose-response.md]]
4. [[S-63 - Quintao, Grundy & Ahrens 1971 JLR — dietary cholesterol and regulation of total body cholesterol pool.md]]

Clear LDL/ApoB rise (anti-egg / mechanism-confirming):
5. [[S-35 - Sacks 1984 Lancet — egg feeding raises LDL and ApoB in free-living lacto-vegetarians.md]]
6. [[S-42 - Ginsberg 1994 Arterioscler Thromb — dose-response of dietary cholesterol-egg feeding on lipoproteins in healthy young men.md]]
7. [[S-44 - Ginsberg 1995 ATVB — dietary cholesterol-egg dose-response raises both LDL and HDL in healthy young women.md]]

Whole-egg HDL-up / LDL-neutral (pro-egg / null; mostly Fernandez-lab):
8. [[S-71 - DiMarco et al. 2017 Lipids — dose-escalation egg RCT- HDL up, LDL unchanged, TMAO unchanged in healthy adults.md]] `[DUP → S-48]`
9. [[S-67 - Mutungi et al. 2008 J Nutr — egg-derived cholesterol raises HDL in carbohydrate-restricted overweight men.md]]
10. [[S-79 - Greene et al. 2006 Nutrition & Metabolism — egg feeding shifts LDL-HDL particle characteristics and raises plasma carotenoids in an elderly population.md]] `[DUP → S-53]`

Null / comparator-dependent:
11. [[S-75 - Kim & Campbell 2018 Nutrients — dietary cholesterol from whole eggs is poorly absorbed, no acute rise in plasma cholesterol.md]]
12. [[S-77 - Vorster et al. 1992 AJCN — egg intake does not change plasma lipoprotein or coagulation profiles (South African trial).md]]
13. [[S-73 - Njike et al. 2010 Nutrition Journal — daily egg consumption in hyperlipidemic adults, lipids and endothelial function.md]]
14. [[S-82 - Katz et al. 2005 Int J Cardiol — egg vs. oatmeal crossover trial- endothelial function and lipids unaffected by eggs.md]]

### Slice 5 — Inter-individual lipid-response variation: responders + ApoE genotype (SURROGATE)
(i) Hyper/hypo-responder classification & physiology:
1. [[S-22 - Katan and Beynen 1986 - Existence of consistent hypo- and hyperresponders to dietary cholesterol in man.md]]
2. [[S-25 - McNamara et al 1987 - Heterogeneity of cholesterol homeostasis in man.md]] — **survivor** of the McNamara-1987 duplicate.
3. [[S-74 - Kern 1991 NEJM - Normal plasma cholesterol in an 88-year-old man who eats 25 eggs a day, mechanisms of adaptation.md]]
4. [[S-55 - Missimer, DiMarco and Fernandez 2019 Curr Dev Nutr - Egg-derived dietary cholesterol response, distinct lipoprotein profiles, carotenoids and choline unaffected.md]]
5. [[S-30 - Herron et al 2003 J Nutr - Men classified as hypo- or hyperresponders exhibit differences in lipoprotein metabolism.md]]
6. [[S-32 - Herron et al 2002 J Am Coll Nutr - Pre-menopausal women hypo- or hyperresponders do not alter LDL-HDL ratio.md]]
7. [[S-53 - Greene et al 2006 Nutr Metab - Plasma LDL and HDL characteristics and carotenoid content positively influenced by egg consumption in an elderly population.md]] — **survivor** of the Greene-2006 duplicate.
8. [[S-36 - Herron et al 2004 Metabolism - High cholesterol intake yields less atherogenic LDL particles independent of response classification.md]]

(ii) ApoE genotype modifier (a real 3-way disagreement — do not average away):
9. [[S-62 - Weggemans, Zock, Ordovas, Pedro-Botet and Katan 2001 Atherosclerosis - ApoE genotype and response of serum cholesterol to dietary fat, cholesterol and cafestol.md]] — largest pool (n=395), null for cholesterol-specific effect.
10. [[S-65 - Sarkkinen et al 1998 AJCN - Effect of apolipoprotein E polymorphism on serum lipid response to dietary fat and dietary cholesterol.md]] — E4/4 most responsive (contradicts S-62).
11. [[S-70 - Lopez-Miranda et al 1994 J Lipid Res - Effect of apolipoprotein E phenotype on diet-induced lowering of plasma LDL cholesterol.md]] — effect in men, not women.

(iii) Other genetic/absorption modifiers:
12. [[S-72 - Herron et al 2006 J Nutr - The ABCG5 polymorphism contributes to individual responses to dietary cholesterol and carotenoids in eggs.md]]
(S-74 and S-25 cross-listed from (i) as absorption/synthesis-phenotype evidence.)

### Slice 6 — Egg RCTs in diabetic / prediabetic / metabolic-syndrome populations (MIXED)
DIABEGG (core "high egg is safe in T2D" anchor):
1. [[S-26 - DIABEGG 3-month RCT — high-egg vs low-egg diet in prediabetes-T2D (Fuller 2015).md]]
2. [[S-31 - DIABEGG weight-loss and 12-month follow-up phase in T2D (Fuller 2018).md]] — shares DIABEGG cohort with S-26.

Other T2D/prediabetes RCTs — null-to-beneficial:
3. [[S-37 - Energy-restricted high-protein diet with eggs vs lean meat in T2D-IGT (Pearce 2011).md]]
4. [[S-34 - One egg-day vs oatmeal breakfast crossover trial in T2D (Ballesteros 2015).md]]
5. [[S-46 - One egg-day vs egg substitute in pre--type-2-diabetes, glycemic outcomes (Pourafshar 2018).md]]

Metabolic-syndrome-defined whole-egg RCTs (Fernandez lab):
6. [[S-43 - Whole egg vs egg substitute in carbohydrate-restricted diet, metabolic syndrome (Blesso 2013).md]]
7. [[S-64 - Eggs plus spinach in a plant-based diet, metabolic syndrome (Thomas 2022).md]]

Eggs in plant-based diet, at-risk-for-T2D:
8. [[S-61 - Eggs in plant-based diets, cardiometabolic risk in adults at risk of T2D (Njike 2021).md]]

Independent (non-Western, non-industry) replication:
9. [[S-51 - Selenium-enriched vs zeaxanthin-enriched eggs in T2D, China (Niu 2026).md]]

Anti-egg counterweight (the one mixed result):
10. [[S-57 - Substituting eggs for high-carbohydrate breakfast foods, at-risk-for-T2D (Maki 2020).md]] — adverse LDL-C signal (not glycemic).

### Slice 7 — Choline → TMAO pathway (MIXED; mechanism independent of the lipid pathway)
Foundational mechanism + TMAO-predicts-events (all Hazen-lab, Cleveland Clinic):
1. [[S-28 - Gut flora metabolism of phosphatidylcholine promotes cardiovascular disease (Wang et al. 2011, Nature).md]]
2. [[S-29 - Intestinal microbial metabolism of phosphatidylcholine and cardiovascular risk (Tang et al. 2013, NEJM).md]]
3. [[S-40 - Gut microbial metabolite TMAO enhances platelet hyperreactivity and thrombosis risk (Zhu et al. 2016, Cell).md]]
4. [[S-39 - Intestinal microbiota metabolism of L-carnitine, a nutrient in red meat, promotes atherosclerosis (Koeth et al. 2013, Nature Medicine).md]] — carnitine route (not egg-specific), context.

Does eating eggs actually raise TMAO (feeding studies):
5. [[S-47 - Effect of egg ingestion on trimethylamine-N-oxide production in humans- a randomized, controlled, dose-response study (Miller et al. 2014, AJCN).md]] — yes, acutely/postprandially.
6. [[S-48 - Intake of up to 3 eggs-day increases HDL cholesterol and plasma choline while plasma TMAO is unchanged in a healthy population (DiMarco et al. 2017, Lipids).md]] — **survivor** of the DiMarco-2017 duplicate; chronic, fasting TMAO unchanged.
7. [[S-59 - Effects of egg consumption and choline supplementation on plasma choline and TMAO in a young population (Lemos et al. 2018, J Am Coll Nutr).md]]
8. [[S-60 - Dietary choline supplements, but not eggs, raise fasting TMAO levels in participants with normal renal function- a randomized clinical trial (Wilcox et al. 2021, Am J Med).md]] — against-own-hypothesis Hazen-lab RCT.

Skeptical side (marker-not-cause / relative-dose):
9. [[S-68 - TMAO response to animal source foods varies among healthy young men and is influenced by their gut microbiota composition (Cho et al. 2016-2017, Mol Nutr Food Res).md]] — fish raises TMAO 46-62x more than eggs.
10. [[S-69 - TMAO is associated with mortality- impact of modestly impaired renal function (Gruppen et al. 2017, Scientific Reports).md]] — association largely explained by eGFR.

### Slice 8 — Egg nutrition beyond CVD (MIXED)
Satiety & weight/body-composition:
1. [[S-3 - Vander Wal 2008 - Egg breakfast enhances weight loss.md]]
2. [[S-2 - Vander Wal 2005 - Short-term effect of eggs on satiety in overweight and obese subjects.md]]

Choline as a beneficial essential nutrient:
3. [[S-5 - Caudill 2018 - Maternal choline supplementation improves infant information processing speed.md]]
4. [[S-7 - Zeisel 1991 - Choline, an essential nutrient for humans.md]]

Lutein/zeaxanthin & eye health:
5. [[S-10 - Vishwanathan 2009 - Egg yolks increase macular pigment in statin users with low baseline pigment.md]]

High-quality protein & muscle:
6. [[S-12 - van Vliet 2017 - Whole eggs versus egg whites and postexercise muscle protein synthesis.md]]

Egg allergy & early introduction:
7. [[S-15 - Natsume 2017 - PETIT trial- two-step egg introduction prevents egg allergy in high-risk infants.md]]
8. [[S-18 - Eggesbo 2001 - Population-based prevalence of egg allergy in young children.md]]

Foodborne / Salmonella risk:
9. [[S-20 - St Louis 1988 - Emergence of grade A eggs as a major source of Salmonella enteritidis infections.md]]
10. [[S-24 - USDA-FSIS Salmonella Enteritidis risk assessment for shell eggs and egg products.md]]

### Slice 9 — Substitution + confounding / healthy-user bias + methodology (META)
Substitution analyses:
1. [[S-89 - Substitution analysis- replacing eggs with other protein foods and CVD-mortality risk.md]] — Zhong 2021 IJE; shares Zhong-2019 6-cohort data.
2. [[S-90 - Why substitution analysis in nutritional epidemiology needs caution.md]]

Confounding / healthy-user bias:
3. [[S-92 - Egg-diabetes-CHD risk after adjusting for overall diet quality.md]] — Djoussé 2021 9-cohort pooling.
4. [[S-94 - The E-value- how much unmeasured confounding would it take to explain away an association.md]]
5. [[S-101 - Eggs load onto the same 'Western' dietary pattern as red and processed meat in MESA.md]]

Nutritional-epidemiology methodology as position artifacts (5 critical + 1 defence + 1 template):
6. [[S-95 - The case that nutritional-epidemiology cohort methods need radical reform.md]] — Ioannidis 2018.
7. [[S-99 - The OPEN study- how much self-reported diet data actually misreports intake.md]]
8. [[S-97 - The cookbook test- almost every ingredient is 'linked' to cancer risk.md]]
9. [[S-96 - The 'fatal flaws' case against food-frequency-questionnaire dietary data.md]]
10. [[S-100 - In defence of nutritional epidemiology's methods and policy role.md]] — the balancing defence.
11. [[S-98 - GRADE-ing red-meat RCT evidence as a template for reappraising dietary guidance.md]] — NutriRECS template (no egg data).

---

## (b) Union of exclusions (deduped across all 9 searchers)

Grouped by reason. "Reconciled" = a paper one slice recorded as excluded that another slice actually minted (so it IS in the live pool — no gap).

**Reconciled cross-slice hand-offs (no gap):**
1. Djoussé et al. 2021 Clin Nutr (9-US-cohort pooling, diet-quality-adjusted) — excluded by slices 1 & 3 as a slice-3/boundary case; **minted by slice 9 as S-92**.
2. Jang 2018 KoGES Ansung-Ansan (CVD × T2DM interaction) — excluded by slice 2 as slice-3 territory; **minted by slice 3 as S-14**.
3. Blesso 2013 (whole egg in metabolic syndrome) — excluded by slice 4 as slice-6 territory; **minted by slice 6 as S-43**.
4. Njike 2010 Nutrition Journal (hyperlipidemic adults) — excluded by slice 6 as slice-4 territory; **minted by slice 4 as S-73**.
5. DiMarco 2017 TMAO co-headline — slice 4 minted it (as S-71) for lipids, slice 7 minted it (as S-48) for TMAO → **TRUE duplicate, resolved below (survivor S-48).**

**Discovery-hub reviews / meta-analyses (mined for primaries, never minted — correct):**
6. Rong 2013 BMJ; Drouin-Chartier 2020 BMJ meta portion; Shin 2013 AJCN; Krittanawong 2021; Godos 2021; Alexander 2016 (egg-industry-funded); Xu 2019 & Godos 2021 region-stratified metas (slice 1/2).
7. Tamez 2016 BJN; Wallin/Li 2013; Shin 2013; the DMSO egg-CVD-in-diabetics review (slice 3).
8. Clarke 1997 BMJ; Weggemans 2001 AJCN; Berger 2015 AJCN; Vincent 2019 AJCN; Rouhani 2018 JACN (slice 4).
9. Fernandez 2006 & 2012; Ordovas ApoE reviews; Herron/Fernandez responder reviews; Griffin reviews (slice 5).
10. Richard 2017 Can J Diabetes and other egg-RCT-in-T2D systematic reviews (slice 6).
11. Heianza 2017 JAHA; Schiattarella 2017 EHJ; Zeisel/Warrier choline-TMAO reviews; Klatt & Caudill skeptical commentary (slice 7).
12. Egg-satiety reviews; Wallace 2018 / Zeisel choline reviews; AREDS/lutein reviews; DIAAS protein-quality reviews; EFSA/CDC Salmonella reports (slice 8).
13. Ioannidis/Trepanowski commentaries; NutriRECS/2019-Annals companion papers (slice 9).

**Wrong design / out of scope:**
14. Radzevičienė & Ostrauskas 2012 (Lithuania, case-control); Ni 2020 (Hangzhou, cross-sectional); Shi 2011 (Jiangsu, repeated cross-sectional) — not prospective cohorts (slice 3).
15. Jeon/Kim/Yun 2025 KNHANES (cross-sectional, modelled risk-score outcome); HEXA Korea metabolic-syndrome paper (surrogate/prevalent endpoint) (slice 2).
16. Mesas 2022 EVIDENT II (cross-sectional FFQ nested in an RCT) (slice 6).
17. Guo 2017 Eur J Nutr (Caerphilly+NDNS, UK) — Western, slice-1 territory, not re-flagged (slice 2).
18. Moreno/Lopez-Miranda 2004; Katan/van Gastel 1988 Trappist study — dietary-FAT (not cholesterol) manipulation (slice 5).
19. Herron 2006 J Nutr carotenoid-prediction paper — reads as slice-8 (lutein) not slice-5 (slice 5).
20. AJCN 2025 egg/SFA-LDL paper; Ma 2022 Chinese cholesterol-balance — mean-effect feeding, slice-4 territory (slice 5).
21. China-PAR/ChinaMUCA/InterASIA "genetic-susceptibility CAD" paper — Asian, slice-2 territory (slice 1); note a *different* China-PAR paper (Xia 2020) is minted as S-81.

**Shared-cohort, deliberately not re-minted (independence — see cluster list):**
22. Hu FB 1999 JAMA (Harvard NHS/HPFS) — superseded by S-19 (same 3 cohorts) (slice 1).
23. Pan 2023 Nutrients (China Kadoorie Qingdao sub-cohort) — same cohort as S-80; sex-differential finding worth extracting downstream (slice 2).
24. Ke Wang 2022 NMCD (CFPS, CVD) — same CFPS cohort as S-86 (slice 2).
25. NIPPON DATA80 re-evaluation 2017 (extended follow-up, women) — same cohort as S-88 (slice 2).
26. Wang Z 2014 EHJ (choline/betaine prognostic) — same Cleveland-Clinic GeneBank cohort as S-29/S-40 (slice 7).
27. Blesso 2013 J Clin Lipidol / Njike diet-quality companion / Thomas 2022 Nutrients companion — same trials as S-43 / S-61 / S-64 (slice 6).
28. Greene 2005 J Nutr companion — probable-overlap with the Greene 2006 paper; **NOT** the same artifact as the minted Greene 2006 (S-53/S-79) — a genuinely separate paper, left out (slice 4).

**Redundant primaries dropped for budget (legit top-up candidates, not gaps):**
29. Flynn 1979 AJCN (null egg-cholesterol classic) — redundant with S-77/S-82 (slice 4).
30. Ratliff 2010; Fallaize 2013 (satiety) — redundant with Vander Wal S-2/S-3 (slice 8).
31. Chung 2004 / Handelman / Kelly buttermilk-MPOD — lutein-bioavailability-only, superseded by S-10 (slice 8).
32. Perkin 2016 NEJM (EAT egg arm, ITT null) & Palmer 2013 (STAR, stopped early) — informative allergy contrast cases (slice 8).
33. Djoussé 2010 CHS (elderly US egg-T2D, underpowered) — natural 11th slice-3 pick (slice 3).
34. Zhu C ~2019/2021 (postmenopausal whole-egg TMAO null) — independent population, budget-cut (slice 7).
35. Wallace & Fulgoni 2016 (NHANES choline-adequacy, ~10.8% meet AI) — strong "choline adequacy" candidate, budget-cut (slice 8).

**Genuine gaps / not found within budget (see audit):**
36. Rotterdam Study; UK Biobank standalone Western egg-vs-hard-endpoint primary — searched, none found (slice 1).
37. EPIC-InterAct standalone egg-T2D primary; Tehran Lipid & Glucose Study egg-T2D; dedicated China Kadoorie egg-T2D — none isolatable (slice 3).
38. WHI 2022 AJCN (eggs/cholesterol/choline/betaine & diabetes) — located but 403-blocked, unread (slice 3).
39. Korea general-population hard-endpoint CVD/mortality cohort; South & Southeast Asia standalone egg-CVD cohorts; Taiwan/Singapore egg-specific hard-endpoint papers — none found (slice 2).
40. NPC1L1-polymorphism-and-egg-response primary; the Gylling/Miettinen ApoE absorption/synthesis J Lipid Res paper (strongest slice-5 near-miss); a "Rho" responder paper (unidentifiable) (slice 5).
41. A clean Mendelian-randomization TMAO-causality primary (skeptical thread) (slice 7).
42. An elderly/sarcopenia whole-egg-vs-alternative-protein MPS/lean-mass RCT — only young-men data (S-12) found (slice 8).
43. Virtanen/Kuopio egg-specific substitution primary; a post-2018 rebuttal answering Ioannidis specifically; an egg-specific E-value application — none found (slice 9).

---

## (c) Duplicate resolutions (job 1)

All three suspected pairs are **TRUE duplicates**, each verified by identical DOI + author list + design (not merely similar findings). A full DOI scan of all 101 nodes found **exactly these three** duplicate-DOI pairs and no others; PubMed-URL and other nodes are all distinct artifacts. Survivor = lower id; higher id flagged `duplicate_of` + a body merge note, both files retained for step 2b.

| Pair | Survivor (kept) | Duplicate (flagged) | Same artifact — evidence |
|------|-----------------|---------------------|--------------------------|
| McNamara 1987 | **S-25** (slice 5) | S-56 (slice 4) | DOI 10.1172/JCI113013, J Clin Invest 1987, McNamara/Kolb/Parker/Batwin/Samuel/Brown/Ahrens; 75×12-wk metabolic-ward periods, ~69% compensate. |
| DiMarco 2017 | **S-48** (slice 7) | S-71 (slice 4) | DOI 10.1007/s11745-017-4230-9, Lipids 2017, DiMarco et al.; 0-3 eggs/day dose-escalation, HDL up / LDL flat / TMAO unchanged. Exactly the 4/7-boundary double-mint the planner flagged. |
| Greene 2006 | **S-53** (slice 5) | S-79 (slice 4) | DOI 10.1186/1743-7075-3-6, Nutrition & Metabolism (London) 2006, Greene/Waters/Clark/Contois/Fernandez; 42 elderly, 3 eggs/day vs cholesterol-free substitute, 30-day crossover. (Verified same DOI despite the planner's caution about a *separate* Greene 2005 J Nutr paper, which was not minted.) |

Minor metadata drift between duplicate members (first-name transcription variants — "Diana/Dominic DiMarco", "Colleen/Christine Greene" — and citation-count differences) is scrivener error on the same artifact, not evidence of two papers; the survivors carry the more standard author strings. Step 2 should reconcile metadata onto the survivor.

---

## (d) Shared-data-basis clusters (job 2) — mint `D` nodes; do NOT merge

These papers are **distinct artifacts** that re-use the same underlying dataset or come from the same lab; they must stay separate nodes but be linked to a common `data-basis` (`D`) node so step 5 does not double-count correlated evidence and step 2 sets `data_basis` correctly.

**Direct shared-cohort clusters (same participants/dataset, ≥2 live nodes):**
1. **Lifetime Risk Pooling Project (6 US cohorts: ARIC, CARDIA, CHS, Framingham Offspring, Jackson Heart, MESA):** S-21 (Zhong 2019, CVD/mortality) + S-89 (Zhong 2021, substitution). *Partial constituent overlap:* S-54 (ARIC standalone HF), S-101 (MESA dietary-pattern), and S-6 (Jackson Heart T2D) each re-analyse ONE constituent cohort of this pool — genuinely separate analyses but not fully independent of S-21/S-89. Flag as partial-overlap.
2. **Physicians' Health Study (PHS-I):** S-23 (heart failure) + S-27 (CVD/mortality) + S-1 (PHS-men arm of the egg→T2D analysis). *Women's Health Study* underlies the other arm of S-1 (no other WHS node).
3. **Million Veteran Program (MVP):** S-66 (CAD) + S-76 (acute stroke).
4. **Cleveland-Clinic GeneBank angiography cohort (Hazen lab):** S-29 (Tang 2013, 4,007-pt MACE) + S-40 (Zhu 2016, same cohort). S-28 (Wang 2011) uses a related earlier Cleveland-Clinic human cohort. See cluster (E) for the broader lab/COI grouping.
5. **DIABEGG trial cohort (Fuller):** S-26 (3-month) + S-31 (12-month follow-up phase).
6. **Cohort of Swedish Men (COSM; Wolk/Larsson group):** S-8 (T2D) + S-45 (CVD; S-45 also adds the Swedish Mammography Cohort for its women).
7. **China Health and Nutrition Survey (CHNS):** S-13 (T2D) + S-85 (incident CVD).
8. **Japan Public Health Center-based Prospective Study (JPHC):** S-9 (T2D) + S-87 (CHD).
9. **KoGES umbrella (Korean Genome & Epidemiology Study):** S-11 (general-population T2D) + S-14 (Ansung-Ansan sub-cohort, CVD × T2D). Likely distinct sub-cohorts under one umbrella — treat as partial overlap.
10. **EPIC umbrella (nested/overlapping sub-cohorts):** S-33 (pan-European EPIC IHD) ⊇ S-78 (EPIC-Oxford UK arm) and S-16 (EPIC-Greece diabetics). Sub-cohort participants are subsets of pan-European EPIC — partial overlap; verify person-level overlap at step 2.
11. **Ginsberg Columbia dose-response program:** S-42 (men, 1994) + S-44 (women, 1995) — companion trials, one investigator/protocol, distinct participants.

**Same-lab / investigator correlation clusters (distinct datasets; correlate for step 5 + motivatedness, NOT shared participants):**
A. **Fernandez / UConn egg-feeding lab — the single biggest correlation concentration in the pool.** Responder-classification subject-pool series likely sharing/overlapping participants: S-30, S-32, S-36, S-72, S-55. Same lab, distinct cohorts: S-48 (DiMarco), S-53 (Greene elderly), S-43 (Blesso metabolic syndrome), S-64 (Thomas), S-59 (Lemos). A large share of the pro-egg lipid / responder / metabolic evidence — and most "whole-egg raises HDL / benign hyperresponse" claims — traces to this one lab, much of it Egg Nutrition Center / American Egg Board funded. Step 5 must treat these as correlated on lab-level practice and COI, not as independent confirmations.
B. **Djoussé research group (Harvard/VA):** S-1, S-6, S-23, S-27, S-66, S-76, S-92 — one senior author (Luc Djoussé) spanning PHS, WHS, Jackson Heart, MVP, and the 9-cohort pooling. Cohort data are genuinely distinct, but this is one analytic team, not seven.
C. **Yale-Griffin Prevention Research Center (Katz/Njike):** S-73 (Njike 2010), S-82 (Katz 2005), S-61 (Njike 2021) — same group, CDC-funded (no egg-industry COI), distinct trials.
D. **Wolk/Larsson Swedish group:** S-8, S-45 (also shares the COSM cohort, cluster 6).
E. **Hazen / Cleveland-Clinic TMAO lab, with a shared TMAO-diagnostic patent/royalty COI:** S-28, S-29, S-39, S-40, S-60. S-28's motivatedness field explicitly flags this COI across the whole set. S-60 (Wilcox 2021) is an *interventional* RCT (not the GeneBank cohort) and reports against the lab's own harm hypothesis — same lab, distinct data.
F. **Nakamura Japanese group:** S-87 (JPHC) + S-88 (NIPPON DATA80) — same lead author, genuinely different cohorts.

**Explicitly NOT shared (confirm, so step 2 does not over-merge):**
- **S-54 (Nettleton ARIC 2008) vs S-101 (Nettleton MESA 2009)** — DIFFERENT cohorts (ARIC ≠ MESA), same lead author only. Both stand as independent data. (Each does partially overlap the Zhong pool via its own constituent cohort — see cluster 1.)

---

## (e) Pool-shape summary

98 live sources spread across the 9 planned slices with no slice thinner than 8 live nodes. The empirical hard-endpoint backbone is strong and genuinely multi-population: ~11 distinct Western cohort families (slice 1) and ~10 non-Western/multinational families (slice 2), with the US-vs-Asia heterogeneity present as a first-class axis in both the CVD (slices 1/2) and diabetes (slice 3) literatures. Both mechanistic pathways are independently populated — the lipid pathway across slices 4 (mean dose-response, 11 live nodes) and 5 (responder/ApoE variation, 12 nodes), and the TMAO pathway in slice 7 (10 nodes) — and the mechanism side carries its own internal disagreements (ApoE 3-way split; acute-vs-chronic and food-vs-supplement TMAO). Observational (slice 3) and interventional (slice 6) diabetes evidence are both present. The methodology/epistemics slice (9, 11 nodes) and the beyond-CVD slice (8, 10 nodes) both filled well, giving the "how can we tell" and "what else" clauses of the FLF framing real coverage. All three verdict directions (harm, neutral, beneficial) appear in multiple slices. The main structural cautions carried forward: a heavy Fernandez/UConn-lab and Djoussé-group concentration behind large parts of the pro-egg-mechanism and US-cohort evidence respectively (a correlation, not a gap), a China-dominated Asian leg (Korea and South/SE Asia absent), and a slice-6 that is one-sided toward null-to-beneficial because no adverse-glycemic egg RCT appears to exist.

---

## Audit — balance + independence vs planner 1a's plan (job 4)

### Balance (all three sides represented, each in ≥2 slices)
1. **Harm side — well represented.** Slice 1 (Zhong S-21, Djoussé/PHS S-23/S-27, ARIC/Nettleton S-54, MVP S-66/S-76); slice 2 (CHNS harm S-85, rural Anhui S-84, NIPPON women-specific S-88); slice 3 (US egg→T2D S-1/S-4/S-6, China S-13, diabetic-interaction S-14/S-16); slice 4 (Sacks S-35, Ginsberg LDL-rise S-42/S-44); slice 7 (TMAO harm pathway S-28/S-29/S-40); slice 8 (Salmonella S-20/S-24, allergy base-rate S-18).
2. **Neutral/null — well represented.** Slice 1 (Harvard S-19, EPIC S-33, Swedish S-45, KIHD S-50, Framingham S-41, SUN S-38, NHANES S-58); slice 2 (PURE S-91, JPHC S-87, Guangzhou S-83); slice 3 (Swedish S-8, PREDIMED-interaction-null S-17); slice 4 (Vorster S-77, Katz S-82, Kim & Campbell S-75); slice 6 (DIABEGG S-26/S-31); slice 7 (eggs-don't-raise-TMAO S-48/S-59/S-60, skeptical S-68/S-69).
3. **Beneficial/protective — well represented.** Slice 2 (Kadoorie protective S-80, China-PAR moderate-best S-81, CFPS S-86); slice 3 (Asian inverse S-9/S-11); slice 4 (HDL-up S-67, S-48); slice 5 (hypo-responder existence, benign hyperresponse); slice 6 (favorable glycemic/lipid S-34/S-37/S-43/S-46/S-51/S-61/S-64); slice 8 (satiety/weight S-2/S-3, choline-neuro S-5/S-7, lutein S-10, protein S-12, PETIT allergy prevention S-15).
**Verdict: balance intact.** No side is thin or confined to a single slice.

### Independence axes (vs the plan's guarantees)
4. **≥6 distinct Western cohort families (slice 1): MET (≈11).** Harvard NHS/NHSII/HPFS; the 6-US-cohort pool; PHS; pan-European EPIC; EPIC-Oxford; SUN; Framingham; COSM+SMC; KIHD; NHANES-I; MVP. Caveats: 4 of 14 slice-1 nodes are Djoussé-group (both PHS + both MVP) — authorship-correlated, distinct data; and the pool's constituent ARIC/MESA re-appear in S-54/S-101. Still ≥6 genuinely independent families. **Not thin.**
5. **Several distinct non-Western families (slice 2): MET but China-skewed.** 6 Chinese families (Kadoorie, China-PAR, CFPS, Guangzhou, CHNS, rural Anhui) + 2 Japanese (JPHC, NIPPON DATA80) + 2 multinational (PURE, INTERHEART). Korea has NO general-population hard-endpoint cohort in the pool (its one CVD paper, S-14, is the diabetic-interaction paper that correctly sits in slice 3); South & Southeast Asia are absent as standalone cohorts. The US-vs-Asia contrast axis is intact via China + Japan + PURE, but rests disproportionately on China. **Borderline: geographically thin outside China, not thin in count.**
6. **Lipid pathway (4/5) AND TMAO pathway (7) both present as independent bases: MET.** Lipid: 11 live slice-4 + 12 slice-5 nodes. TMAO: 10 slice-7 nodes. Independent measurement pathways, each internally contested. **Not thin.**
7. **Observational (3) vs interventional (6) diabetes both present: MET.** 10 observational + 10 interventional. Caveat: slice 6 is one-sided toward null-to-beneficial (only S-57/Maki is even a partial counterweight; no RCT with an adverse *glycemic* signal was found despite active search) — an accurate reflection of the literature, not a pool gap. **Not thin.**
8. **Methodology (9) non-thin: MET (11 live, over budget).** Both critics (S-95/S-96/S-97/S-98/S-99) and an explicit defence (S-100) present, plus substitution (S-89/S-90) and confounding tools (S-92/S-94/S-101). The planner's worry that slice 9 might underfill did not materialise. **Not thin.**
9. **Beyond-CVD (8) non-thin: MET (10 live).** Six threads, mixed valence (6 benefit / 2 Salmonella-harm / 2 allergy-split). Minor internal thinness: single lutein node, single protein node, and the protein evidence is young-men-only (no elderly/sarcopenia RCT). **Not thin overall.**
10. **Responder/ApoE (5): MET (12 live, over budget).** The planner's worry it might be a small literature did not bind. The ApoE sub-thread is the smallest (3 nodes) but carries a load-bearing 3-way disagreement rather than being padded. **Not thin.**

### Top-up verdict
**No axis is empty or below its plan-stated independence bar; no top-up searcher round is required for pool validity.** The pool clears every balance and independence guarantee in section 71-79 of the plan.

One **optional, low-priority** top-up is defensible if step 2 wants to harden a specific claim:
- **Geographic breadth of the Asian leg (slice 2):** a targeted search for a Korean general-population hard-endpoint CVD/mortality cohort and any South/Southeast-Asian standalone egg-CVD cohort, to make the US-vs-Asia contrast robust to a "this is really just China + Japan" critique. Two independent searchers already judged these to be likely genuine evidence gaps rather than search misses, so expected yield is low — hence optional, not required.

Two items are **step-5 correlation flags, not gaps** (record, do not top up):
- The **Fernandez/UConn-lab concentration** (cluster A) behind most whole-egg-HDL/responder/metabolic-syndrome pro-egg results — searchers 4 and 5 both looked for and failed to find an independent non-Fernandez whole-egg-HDL-up trial. Non-Fernandez pro/null trials do exist in the pool (Yale-Griffin S-73/S-82, Vorster S-77, Kim & Campbell S-75, DIABEGG, Ballesteros S-34, Pourafshar S-46, Niu S-51), so the pro-egg side is not solely one lab — but the specific "whole-egg raises HDL" claim is lab-concentrated.
- The **Djoussé-group concentration** (cluster B) behind 4 of 14 slice-1 nodes and much of slice-3's US signal.
