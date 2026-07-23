# Step 1 — Search plan (planner 1a) — egg-health case

Main question (verbatim): "Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?"

FLF scope/intent (framing, NOT the question): "Are eggs good to eat? Bad to eat? Great in moderation? How can we tell? Does it vary across people, and what predicts this? What else should we be paying attention to here?" — the framing explicitly pushes beyond the CVD default (the "what else" and "appropriate ways of knowing" clauses), so the pool must cover non-CVD endpoints and the methodology of the evidence, not only heart-disease cohorts.

curated_target_N = 25. Step-1 totals across all searchers: **~100 `source` notes written, ~200 primaries read properly**, far more skimmed via meta-analyses / systematic reviews / reference lists. 9 searchers below; budgets sum exactly to 100 write / 200 read.

---

## 1. Debate map — literatures, sides, recurring datasets

The question decomposes along two axes that also become the natural cluster boundaries downstream: **endpoint type** (surrogate biomarkers vs hard clinical events) and **which population/mechanism**. Keep surrogate-endpoint evidence (blood lipids, TMAO) and hard-endpoint evidence (CVD events, mortality, incident diabetes) in *separate* slices — downstream clustering must not merge them.

### The literatures that bear on it
1. **Observational cohorts on hard endpoints (CVD events + all-cause/cause-specific mortality).** The backbone for "overall." Large prospective cohorts + their dose-response meta-analyses.
2. **Egg intake vs incident type-2 diabetes.** A distinct endpoint with a striking, replicated **US-vs-Asia heterogeneity**: US cohorts find egg→T2D risk elevated, Asian cohorts find null/inverse. Also the diabetic-subgroup CVD interaction (egg appears worse for CVD in people who already have diabetes).
3. **Dietary-cholesterol → serum lipids (the mechanism, SURROGATE endpoint).** Controlled-feeding / metabolic-ward RCTs measuring LDL-C, ApoB, HDL, total:HDL. Core fact: dietary cholesterol raises serum LDL, but with diminishing returns, partial homeostatic down-regulation of endogenous synthesis, a parallel HDL rise, and large inter-individual spread.
4. **Inter-individual variation in the lipid response** — hyper- vs hypo-responders, ApoE genotype (ApoE4 carriers respond more), other genetic/absorption modifiers. This is the mechanistic answer to "for whom."
5. **Egg RCTs in clinical/metabolic populations** — type-2 diabetics, prediabetes, metabolic syndrome (glycemic/lipid/cardiometabolic outcomes).
6. **The choline → TMAO pathway** — egg phosphatidylcholine → gut-microbiome-generated trimethylamine → hepatic TMAO → proposed pro-atherogenic/thrombotic effect. A mechanism genuinely *independent* of the lipid pathway, with its own biomarker data and its own pro/anti tension (choline is also an essential nutrient — see slice 8).
7. **Egg nutrition beyond CVD** — nutrient composition, satiety and weight/body-composition, choline adequacy & neurodevelopment (pregnancy/infants), lutein/zeaxanthin & eye health, high-quality protein & muscle (elderly/sarcopenia), egg allergy & early introduction, foodborne (Salmonella) risk. This is the "what else should we be paying attention to" slice.
8. **Substitution analyses + confounding / healthy-user-bias critiques + nutritional-epidemiology methodology.** The "how can we tell / appropriate ways of knowing" layer the framing foregrounds: what you replace eggs *with* changes the sign; residual confounding and healthy-user bias in FFQ-based cohorts; measurement-error and memory-based-recall critiques; GRADE-style re-appraisals.

### Sides of the debate
- **Harmful (at higher intake / in subgroups):** Zhong 2019 (6 US pooled cohorts), Physicians'/Women's Health (Djoussé), Weggemans 2001 (lipid meta), the US egg→T2D cohorts, the diabetic-subgroup CVD interaction, the TMAO literature (Wang 2011, Tang 2013), the dietary-cholesterol→LDL feeding tradition (Sacks 1984 found LDL rose; Ginsberg; Hegsted/Keys equations).
- **Neutral / null:** Harvard NHS/HPFS (Hu 1999; Drouin-Chartier 2020), PURE (Dehghan 2020, 50 countries), most updated CVD meta-analyses at moderate intake, homeostatic-compensation feeding studies.
- **Beneficial / protective (or protective in context):** China Kadoorie Biobank (Qin 2018, ~0.5M, *lower* CVD at daily intake), Asian T2D nulls/inverse, HDL-raising and satiety/weight-loss RCTs, choline-adequacy and lutein benefits, high-quality protein for the elderly, hypo-responder existence meaning population means overstate harm.

### Recurring datasets — the INDEPENDENCE hazard
Cohort papers heavily re-analyse a handful of datasets; a pool of forty NHS re-analyses is one data point, not forty. Distinct cohort families: **NHS/NHSII/HPFS** (Harvard), the **US pooled set** (ARIC, CARDIA, CHS, Framingham Offspring, Jackson Heart, MESA — Zhong's Lifetime Risk Pooling Project), **PURE** (50 countries), **EPIC** (+EPIC-Oxford), **China Kadoorie Biobank**, **UK Biobank**, **Physicians'/Women's Health Study**, **Japan** (JACC / JPHC / NIPPON DATA), **Korea** (KoGES / KNHANES), **Rotterdam**, **SUN**, **ARIC** (also standalone), **Framingham**. The geographic split (slice 1 Western vs slice 2 Asian/multinational) is deliberately drawn so the pool contains genuinely independent populations, and so the US-vs-Asia heterogeneity is a first-class independent-data axis rather than noise. On the mechanism side, the **lipid** data basis (slices 3/4/5) and the **TMAO** data basis (slice 6) are independent measurement pathways; each is kept in its own slice.

### Motivatedness hazard
The egg industry (American Egg Board / **Egg Nutrition Center**) funds a large share of pro-egg work — much of the Fernandez lab, several whole-egg and diabetic RCTs, and some meta-analyses (e.g. Alexander 2016). Searchers MUST set `motivatedness` whenever funding/COI is disclosed. This is recorded as data, not used to discount now.

### Primary-only rule
Reviews, systematic reviews and meta-analyses are **discovery hubs** — mine their reference lists (record `found_via`), never give one its own `source` node. Named hubs to mine per slice below.

---

## 2. Slice table (disjoint slices → searcher → write/read → independent-data focus)

| # | Slice | Endpoint | Write | Read | Independent-data / balance focus |
|---|-------|----------|-------|------|----------------------------------|
| 1 | Western (US + European) CVD-event & mortality cohorts | HARD | 14 | 28 | ≥6 distinct Western cohort families; harm (Zhong, Djoussé) + null (Harvard, EPIC) |
| 2 | Asian + multinational CVD/mortality cohorts (US-vs-Asia heterogeneity) | HARD | 12 | 24 | China Kadoorie, Japan, Korea, PURE, INTERHEART — distinct non-Western populations; protective (Kadoorie) + null |
| 3 | Egg intake vs incident type-2 diabetes (observational) | HARD | 10 | 20 | US-elevated vs Asia-null cohorts as the independent-data contrast; diabetic-subgroup CVD interaction |
| 4 | Dietary-cholesterol → serum lipids: feeding RCTs in healthy adults | SURROGATE | 14 | 28 | distinct feeding trials (not re-analyses); LDL-rise (Sacks, Ginsberg) + HDL-up/null (Fernandez-lab) |
| 5 | Inter-individual lipid-response variation: responders + ApoE genotype | SURROGATE | 10 | 20 | responder-classification & genotype studies as the "for whom" mechanism |
| 6 | Egg RCTs in diabetic / prediabetic / metabolic-syndrome populations | MIXED | 10 | 20 | interventional (not observational) clinical-population trials; DIABEGG-safe + any harm signals |
| 7 | Choline → TMAO pathway (gut-microbiome / atherogenesis) | MIXED | 10 | 20 | TMAO as a data basis independent of the lipid pathway; TMAO-predicts-events + null-TMAO-from-eggs |
| 8 | Egg nutrition beyond CVD (satiety/weight, choline-neuro, lutein, protein, allergy, foodborne) | MIXED | 10 | 20 | non-CVD endpoints the framing invites; benefits + harms (Salmonella, allergy) |
| 9 | Substitution analyses + confounding / healthy-user bias + methodology critiques | META | 10 | 20 | the "how can we tell" layer; substitution primaries + methodology-position primaries |
| | **Total** | | **100** | **200** | |

**Balance baked in:** every slice prompt names concrete pro-egg AND anti-egg anchors and forbids letting one side dominate. Harm, neutral, and beneficial sides each appear in multiple slices; the critical/methodology side gets its own dedicated slice (9), and the beyond-CVD picture its own (8), so neither is ghettoised nor omitted.

**Independence baked in:** the two empirical CVD legs are split by population (1 Western vs 2 Asian/multinational); the two mechanism legs are split by biomarker (3/4/5 lipids vs 6→wait, 7 TMAO); observational-diabetes (3) is separated from interventional-diabetes (6). This is the only place pool shape is chosen — no searcher sees the pool.

### Crisp non-overlap boundaries (so parallel searchers rarely collide)
1. **1 vs 2 — geography.** US + Canada + European single-country/region cohorts → slice 1. Any East/South/Southeast-Asian cohort, and explicitly multinational cohorts spanning continents (PURE, INTERHEART, the WHO-CARDIAC-type studies) → slice 2. EPIC pan-European → slice 1; EPIC-InterAct diabetes → slice 3.
2. **1/2 vs 3 — endpoint.** If the paper's headline endpoint is **incident type-2 diabetes** → slice 3. If it is CVD events / mortality → slice 1 or 2, *even if* it also reports a diabetic subgroup (e.g. Hu 1999, Zhong 2019 stay in 1). Slice 3 does NOT re-mint those; it owns dedicated egg→T2D-incidence primaries and diabetes-specific cohort analyses.
3. **4 vs 5 — mean vs variance of the lipid response.** A feeding RCT whose headline is the **average** LDL/HDL/ApoB response in general/healthy adults → slice 4. A study whose headline is **inter-individual variation** (hyper/hypo-responder classification, ApoE- or other-genotype stratification) → slice 5.
4. **4 vs 6 — population.** Feeding/egg RCT in **general/healthy normolipidemic** adults → slice 4. Egg RCT whose population is defined by **disease** (T2D, prediabetes, metabolic syndrome) with glycemic/lipid/cardiometabolic outcomes → slice 6.
5. **6 vs 8 — trial purpose.** A disease-population RCT with cardiometabolic outcomes → slice 6. A trial whose focus is **appetite / satiety / weight / body-composition** (even in overweight subjects) → slice 8.
6. **4/5 vs 7 — biomarker.** A feeding study measuring **blood lipids** → slice 4/5. A feeding/observational study whose headline biomarker is **TMAO / choline→TMAO** → slice 7. If a single study measures both, it goes to whichever is its headline; the other slice mines it via `found_via`.
7. **7 vs 8 — the two faces of choline.** Choline as a route to **TMAO / cardiovascular harm** → slice 7. Choline as a **beneficial essential nutrient** (pregnancy, infant neurodevelopment, adequacy) → slice 8. (This split preserves a real pro/anti tension around the same nutrient.)
8. **9 vs 1/2 — analysis vs data.** Slice 9 owns **substitution-modeling** primaries (headline = "replace eggs with X") and **methodology-position** primaries (confounding/healthy-user-bias/measurement-error/GRADE critiques). Where a substitution result is just a secondary analysis inside a slice-1/2 cohort paper, slice 9 mines it via `found_via` (and may set `duplicate_of`), it does not re-mint the cohort.
9. **General rule:** if a searcher finds a paper it believes another slice owns, it records it under `found_via` / `exclusions` and does NOT mint it — this is what keeps parallel writers off duplicate sources.

### Balance/independence self-check for this plan
- All three sides represented, each in ≥2 slices; critical/methodology side has a dedicated slice (9). ✔
- Surrogate (3/4/5/7-partial) and hard (1/2/3) endpoints kept in separate slices; mixed slices (6/7/8) tag endpoint per source. ✔
- Two independent empirical CVD legs (Western vs Asian populations). ✔
- Two independent mechanism legs (lipids vs TMAO). ✔
- Observational vs interventional diabetes separated (3 vs 6). ✔
- Beyond-CVD endpoints given a dedicated slice (8), per the FLF "what else" clause. ✔
- Reviews/meta-analyses used only as hubs. ✔

---

## 3. Searcher prompts (spawn each verbatim in the fenced block; on **sonnet**)

### Searcher 1 — Western (US + European) CVD-event & mortality cohorts

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set. Your role is a 1b searcher; do NOT spawn subagents.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/eggs
Main question (verbatim): "Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?"
Your slice: Prospective observational cohort (and nested case-control) studies in GENERAL adult populations of the US, Canada, and Europe reporting HARD endpoints — incident CVD (CHD, stroke, heart failure) and all-cause or cause-specific mortality — versus habitual egg intake. INDEPENDENCE IS THE PRIORITY: cohort papers re-analyse a few datasets, so spread across ≥6 DISTINCT Western cohort families and mint at most one PRIMARY per family; do not take multiple re-analyses of the same cohort. Target families (pick the most informative primary in each): Harvard NHS/NHSII/HPFS (Drouin-Chartier 2020 BMJ, or Hu 1999 JAMA); the US pooled set / Zhong 2019 JAMA (ARIC + CARDIA + CHS + Framingham Offspring + Jackson Heart + MESA, Lifetime Risk Pooling Project); Physicians' Health Study / Women's Health Study (Djoussé — heart failure Circulation 2008, and CVD/mortality); EPIC pan-European and EPIC-Oxford; Rotterdam; ARIC standalone; Framingham standalone; SUN (Spain); UK Biobank; any Scandinavian/Finnish cohort. Keep balance: include BOTH harm-finding cohorts (Zhong 2019; Djoussé/PHS at ≥7 eggs/week) AND null-or-protective cohorts (Harvard's null; EPIC nulls). Record endpoint = hard; capture citation counts (these are highly cited); set `motivatedness` where funding/COI is disclosed.
What you must NOT touch: any Asian or explicitly multinational cohort (PURE, INTERHEART, China Kadoorie, Japan, Korea) — those are slice 2; any paper whose HEADLINE endpoint is incident type-2 diabetes — that is slice 3 (you OWN CVD/mortality cohorts even if they also report a diabetic subgroup; slice 3 will not re-mint them); feeding/lipid RCTs (slices 4/5), diabetic/metabolic RCTs (slice 6), TMAO (slice 7), non-CVD nutrition (slice 8), and substitution-modeling / methodology-critique primaries (slice 9). If you find a paper another slice owns, record it under found_via/exclusions and do not mint it.
Discovery hubs to MINE for primaries (do NOT node them): Rong 2013 BMJ dose-response meta-analysis; Drouin-Chartier 2020 BMJ meta portion; Shin 2013 AJCN; Krittanawong 2021 and Godos 2021 dose-response meta-analyses; Alexander 2016 (egg-industry-funded — note it). Harvest their reference lists to reach the distinct-cohort primaries.
Budget: write 14 `source` notes; read ~28 sources properly (lean on the meta-analyses above to skim far more cheaply).
Mint every id'd node by piping its markdown on stdin (the body carries {{ID}}; the title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/eggs --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents.
Finish by writing your own orientation note in agent-notes/orientation/western-cvd-cohorts.md (per the mode file's spec: your sources as wikilinks under topic headings, best-first within each, plus search_scope, exclusions, and a short slice paragraph).
Return: the S-ids you created, your orientation-note path (agent-notes/orientation/western-cvd-cohorts.md), gaps you hit, and a ≤10-line report (1 line per source).
```

### Searcher 2 — Asian + multinational CVD/mortality cohorts (US-vs-Asia heterogeneity)

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set. Your role is a 1b searcher; do NOT spawn subagents.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/eggs
Main question (verbatim): "Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?"
Your slice: Prospective observational cohort studies in ASIAN and explicitly MULTINATIONAL/cross-continental populations reporting HARD endpoints (incident CVD — CHD, stroke, heart failure — and all-cause/cause-specific mortality) versus habitual egg intake. This slice deliberately owns the non-Western populations so the pool contains genuinely INDEPENDENT data and captures the US-vs-Asia heterogeneity as a first-class axis. Spread across DISTINCT cohort families, one primary each: China Kadoorie Biobank (Qin 2018 Heart, ~0.5M, daily egg associated with LOWER IHD/stroke); Japan (JACC study — Nakamura; JPHC; NIPPON DATA80); Korea (KoGES / KNHANES); PURE (Dehghan 2020 AJCN, 50 countries, ~177k — null CVD/mortality); INTERHEART (case-control, 52 countries); any Chinese (besides Kadoorie), Taiwanese, Singaporean, or South-Asian cohort. Keep balance: include BOTH protective/null anchors (China Kadoorie lower risk; PURE null; Japanese nulls) AND any harm signals you find in Asian data — do not let the "eggs are fine in Asia" narrative go unchallenged. Record endpoint = hard; capture citation counts; set `motivatedness` where disclosed. Note per source how egg intake and confounding differ from Western settings (dietary pattern, SES gradient) — useful downstream for the heterogeneity question.
What you must NOT touch: US/Canadian/European single-region cohorts (slice 1); any paper whose HEADLINE endpoint is incident type-2 diabetes, including Asian T2D cohorts (slice 3); feeding/lipid RCTs (4/5), diabetic/metabolic RCTs (6), TMAO (7), non-CVD nutrition (8), substitution/methodology (9). Record others' papers under found_via/exclusions, do not mint.
Discovery hubs to MINE (do NOT node them): Rong 2013 BMJ; Xu 2019 and Godos 2021 dose-response meta-analyses (which stratify by region); the region-stratified sub-analyses inside Drouin-Chartier 2020 BMJ; any Asian-specific egg-CVD systematic review. Harvest reference lists to reach the distinct-cohort primaries.
Budget: write 12 `source` notes; read ~24 sources properly (lean on the meta-analyses above to skim far more cheaply).
Mint every id'd node by piping its markdown on stdin (the body carries {{ID}}; the title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/eggs --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents.
Finish by writing your own orientation note in agent-notes/orientation/asian-multinational-cvd-cohorts.md (sources as wikilinks under topic headings best-first, plus search_scope, exclusions, short slice paragraph).
Return: the S-ids you created, your orientation-note path (agent-notes/orientation/asian-multinational-cvd-cohorts.md), gaps you hit, and a ≤10-line report (1 line per source).
```

### Searcher 3 — Egg intake vs incident type-2 diabetes (observational)

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set. Your role is a 1b searcher; do NOT spawn subagents.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/eggs
Main question (verbatim): "Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?"
Your slice: OBSERVATIONAL evidence on egg intake and TYPE-2 DIABETES — two threads: (i) egg intake vs INCIDENT type-2 diabetes in prospective cohorts, where there is a striking replicated US-vs-Asia heterogeneity (US cohorts find risk ELEVATED; Asian cohorts find null/inverse); (ii) the diabetic-subgroup CVD interaction — dedicated analyses showing egg is associated with worse CVD/mortality in people who ALREADY have diabetes. Spread across distinct cohort families, one primary each: Physicians' Health Study (Djoussé 2009 AJCN/Diabetes Care, egg→T2D in US men — elevated); Women's Health Study (Djoussé, US women); Harvard NHS/HPFS egg→T2D analysis; EPIC-InterAct (European, ~null); China Kadoorie / Chinese cohorts egg→T2D (null/inverse); Japan/Korea egg→T2D; any Iranian (Tehran Lipid) or other cohort. For thread (ii): the diabetic-subgroup results reported as a paper's focus, and any cohort of diabetics-only. Keep balance explicit: mint BOTH the US-elevated-risk primaries AND the Asian-null/inverse primaries — the contrast IS the finding here.
What you must NOT touch: general-population CVD/mortality cohort papers even when they include a diabetic subgroup as a secondary result — those belong to slices 1/2 (mine their diabetic-subgroup numbers via found_via, do not re-mint the cohort). RCTs in diabetics (DIABEGG, Ballesteros) belong to slice 6 — leave them. Feeding/lipid RCTs (4/5), TMAO (7), non-CVD nutrition (8), substitution/methodology (9). Record others' papers under found_via/exclusions, do not mint.
Discovery hubs to MINE (do NOT node them): Djoussé's own egg-diabetes reviews; Tamez 2016 (egg & T2D meta-analysis); Wallin 2013 and Shin 2013 egg-diabetes meta-analyses; Drouin-Chartier 2020's diabetes-outcome section; any region-stratified egg-T2D systematic review. Harvest reference lists for the distinct-cohort primaries and note the region label per source.
Budget: write 10 `source` notes; read ~20 sources properly (lean on the meta-analyses above to skim far more cheaply).
Mint every id'd node by piping its markdown on stdin (the body carries {{ID}}; the title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/eggs --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents.
Finish by writing your own orientation note in agent-notes/orientation/egg-diabetes-observational.md (sources as wikilinks under topic headings best-first, plus search_scope, exclusions, short slice paragraph).
Return: the S-ids you created, your orientation-note path (agent-notes/orientation/egg-diabetes-observational.md), gaps you hit, and a ≤10-line report (1 line per source).
```

### Searcher 4 — Dietary-cholesterol → serum lipids: feeding RCTs in healthy adults

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set. Your role is a 1b searcher; do NOT spawn subagents.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/eggs
Main question (verbatim): "Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?"
Your slice: The MECHANISM at the SURROGATE endpoint — controlled-feeding / metabolic-ward studies and egg-feeding RCTs in GENERAL or HEALTHY adults measuring the response of BLOOD LIPIDS (LDL-C, ApoB, HDL-C, total:HDL ratio, lipoprotein particle number/size) to dietary cholesterol / egg intake. This is the average dose-response of the lipid pathway. INDEPENDENCE: prefer genuinely distinct feeding trials over re-analyses of one dataset. Keep balance — mint BOTH sides: (anti-egg/mechanism-confirming) Sacks 1984 Lancet (egg raised LDL in free-living subjects), Ginsberg 1994/1995 (controlled feeding of dietary cholesterol in healthy young men/women, modest LDL rise), and the Keys/Hegsted/Weggemans metabolic-ward feeding tradition; (null/pro-egg) Fernandez-lab whole-egg RCTs (Mutungi 2008, DiMarco 2017, Blesso 2013 — HDL up, ApoB unchanged, often carbohydrate-restricted), Njike 2010 (daily egg, lipids/endothelial function), Kim & Campbell 2018 crossover, and studies showing homeostatic compensation / diminishing LDL returns at higher intake. Record endpoint = surrogate. Set `motivatedness` whenever egg-industry funding (American Egg Board / Egg Nutrition Center) or similar COI is disclosed — this is common here.
What you must NOT touch: any study whose HEADLINE is inter-individual variation, hyper/hypo-responder classification, or ApoE/other genotype stratification — that is slice 5; any egg RCT whose POPULATION is diabetic / prediabetic / metabolic-syndrome — that is slice 6; any feeding study whose HEADLINE biomarker is TMAO/choline — that is slice 7; satiety/weight/body-composition trials — slice 8; hard clinical-event cohorts — slices 1/2. If a trial reports both a mean lipid effect (yours) and responder subsets, you own it only if the mean effect is its headline; else leave it to slice 5. Record others' papers under found_via/exclusions, do not mint.
Discovery hubs to MINE (do NOT node them): Clarke 1997 BMJ metabolic-ward meta-analysis; Weggemans 2001 AJCN dietary-cholesterol meta-analysis; Berger 2015 AJCN dietary-cholesterol systematic review; Vincent 2019 and McNamara dietary-cholesterol reviews; Rouhani 2018 egg-and-lipids meta-analysis. Harvest their reference lists for the primary feeding trials.
Budget: write 14 `source` notes; read ~28 sources properly (lean on the meta-analyses above to skim far more cheaply).
Mint every id'd node by piping its markdown on stdin (the body carries {{ID}}; the title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/eggs --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents.
Finish by writing your own orientation note in agent-notes/orientation/feeding-rcts-lipids-healthy.md (sources as wikilinks under topic headings best-first, plus search_scope, exclusions, short slice paragraph).
Return: the S-ids you created, your orientation-note path (agent-notes/orientation/feeding-rcts-lipids-healthy.md), gaps you hit, and a ≤10-line report (1 line per source).
```

### Searcher 5 — Inter-individual lipid-response variation: responders + ApoE genotype

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set. Your role is a 1b searcher; do NOT spawn subagents.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/eggs
Main question (verbatim): "Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?"
Your slice: The "FOR WHOM" of the lipid mechanism — inter-individual variation in the blood-lipid response to dietary cholesterol / eggs. Three threads: (i) hyper- vs hypo-responder classification and its physiology (Katan & Beynen 1987 Am J Epidemiol; McNamara 1987; Herron/Fernandez responder-classification studies 2002-2004; the finding that a large fraction of people are hypo-responders, so population means overstate individual harm); (ii) ApoE genotype as a modifier (ApoE4 carriers respond more — Ordovas; Weggemans/Zock ApoE meta-analysis; Sarkkinen); (iii) other genetic/absorption modifiers (NPC1L1, ABCG5/8, cholesterol-absorption vs synthesis phenotypes; Rho-Fernandez lipoprotein-response work). This slice is the mechanistic heterogeneity that answers who is harmed and who is not. Keep balance: hypo-responder existence is a PRO-egg consideration (means overstate harm); hyper-responders and ApoE4 carriers with large LDL rises are an ANTI-egg consideration — mint both. Record endpoint = surrogate. Set `motivatedness` for egg-industry funding (Fernandez lab / Egg Nutrition Center is common here).
What you must NOT touch: mean-effect feeding RCTs in general/healthy adults whose headline is the AVERAGE lipid response — those are slice 4 (you take a trial only when inter-individual variation / genotype IS its headline); diabetic/metabolic-population RCTs (slice 6); TMAO (slice 7); hard clinical-event cohorts (1/2); non-CVD nutrition (8); methodology (9). Record others' papers under found_via/exclusions, do not mint.
Discovery hubs to MINE (do NOT node them): Fernandez responder reviews (Fernandez 2006/2012 Curr Opin Clin Nutr); Ordovas ApoE-diet reviews; Weggemans 2001 (its ApoE stratification); Herron & Fernandez reviews; Griffin dietary-cholesterol-responsiveness reviews. Harvest reference lists for the primary responder/genotype studies.
Budget: write 10 `source` notes; read ~20 sources properly (lean on the reviews above to skim far more cheaply).
Mint every id'd node by piping its markdown on stdin (the body carries {{ID}}; the title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/eggs --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents.
Finish by writing your own orientation note in agent-notes/orientation/responders-apoe-genotype.md (sources as wikilinks under topic headings best-first, plus search_scope, exclusions, short slice paragraph).
Return: the S-ids you created, your orientation-note path (agent-notes/orientation/responders-apoe-genotype.md), gaps you hit, and a ≤10-line report (1 line per source).
```

### Searcher 6 — Egg RCTs in diabetic / prediabetic / metabolic-syndrome populations

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set. Your role is a 1b searcher; do NOT spawn subagents.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/eggs
Main question (verbatim): "Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?"
Your slice: INTERVENTIONAL evidence (randomised / controlled feeding trials) of egg intake in CLINICAL / METABOLIC populations — type-2 diabetics, prediabetes, and metabolic syndrome — with cardiometabolic outcomes (glycemic control HbA1c/fasting glucose/insulin sensitivity, blood lipids, blood pressure, inflammation, endothelial function). This is the interventional test of the observational "eggs harm diabetics" signal. Anchors: DIABEGG (Fuller KA et al. 2015 AJCN and 2018 Am J Clin Nutr — high-egg 2/day vs low-egg in T2D/prediabetes, no adverse lipid/glycemic effect); Ballesteros 2015 (one egg/day in T2D); Pearce 2011 (eggs in overweight/hyperlipidemic — weight-loss context but disease-defined); Njike egg trials in metabolic populations; any egg-in-prediabetes or egg-in-metabolic-syndrome RCT (Blesso 2013 metabolic syndrome sits at the 4/6 boundary — take it here if its population is metabolic-syndrome-defined and its outcomes are cardiometabolic). Keep balance: DIABEGG-type "2 eggs/day is safe in T2D" is the PRO-egg anchor; actively seek any RCT reporting adverse glycemic/lipid signals in diabetics as the ANTI-egg counterweight. Record endpoint per source (surrogate glycemic/lipid, or hard). Set `motivatedness` — egg-industry funding is common in this literature.
What you must NOT touch: OBSERVATIONAL egg-diabetes cohorts (slice 3); feeding/lipid RCTs in general/healthy adults (slice 4); responder/ApoE studies (slice 5); TMAO (slice 7); satiety/weight-loss trials whose focus is appetite/body-composition rather than glycemic/lipid disease outcomes (slice 8 — coordinate at the boundary: disease-population + cardiometabolic outcome = yours; appetite/weight focus = slice 8); hard-event cohorts (1/2); methodology (9). Record others' papers under found_via/exclusions, do not mint.
Discovery hubs to MINE (do NOT node them): Richard 2017 and Fuller 2015 egg-and-diabetes RCT reviews; the DIABEGG protocol/follow-up papers; Sparks egg-glycemic reviews; any Cochrane-style egg-in-T2D systematic review. Harvest reference lists for the primary trials.
Budget: write 10 `source` notes; read ~20 sources properly (lean on the reviews above to skim far more cheaply).
Mint every id'd node by piping its markdown on stdin (the body carries {{ID}}; the title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/eggs --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents.
Finish by writing your own orientation note in agent-notes/orientation/egg-rcts-diabetic-metabolic.md (sources as wikilinks under topic headings best-first, plus search_scope, exclusions, short slice paragraph).
Return: the S-ids you created, your orientation-note path (agent-notes/orientation/egg-rcts-diabetic-metabolic.md), gaps you hit, and a ≤10-line report (1 line per source).
```

### Searcher 7 — Choline → TMAO pathway (gut-microbiome / atherogenesis)

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set. Your role is a 1b searcher; do NOT spawn subagents.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/eggs
Main question (verbatim): "Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?"
Your slice: The CHOLINE → TMAO pathway as a proposed cardiovascular-harm mechanism INDEPENDENT of the blood-lipid pathway. Eggs are the largest dietary source of phosphatidylcholine; gut microbiota convert it to trimethylamine, which the liver oxidises to TMAO, proposed to be pro-atherogenic/pro-thrombotic. Three threads: (i) foundational mechanism + TMAO-predicts-events — Wang Z et al. 2011 Nature ("Gut flora metabolism of phosphatidylcholine promotes cardiovascular disease"); Tang WHW et al. 2013 NEJM ("Intestinal microbial metabolism of phosphatidylcholine and cardiovascular risk", includes an egg/choline challenge); Koeth 2013 Nature Med (carnitine, related); Zhu 2016 Cell (TMAO & platelets/thrombosis); prospective TMAO-and-events cohorts and their meta-analyses' PRIMARIES. (ii) does eating EGGS actually raise TMAO / raise risk — egg-feeding studies measuring plasma TMAO (DiMarco 2017; Miller 2014; Zhu egg-challenge; Lemos 2018 daily-egg TMAO). (iii) the SKEPTICAL side — that egg-derived TMAO rises are transient/modest, that fish raises TMAO far more without harm, that TMAO may be a marker not a cause (renal-function confounding). Keep balance: mint BOTH the harm-pathway primaries AND the skeptical primaries. Record endpoint per source (surrogate biomarker vs hard event). Set `motivatedness` where disclosed (egg-industry-funded null-TMAO studies exist; Hazen-lab has TMAO-diagnostic COI — note both directions).
What you must NOT touch: feeding studies whose HEADLINE biomarker is blood lipids (slices 4/5); choline as a beneficial nutrient / neurodevelopment / adequacy (slice 8 — you own choline ONLY as a route to TMAO/harm); egg-diabetes (3/6); hard-event egg-intake cohorts (1/2); methodology (9). If a study measures both TMAO and lipids, you own it only if TMAO is its headline. Record others' papers under found_via/exclusions, do not mint.
Discovery hubs to MINE (do NOT node them): Heianza 2017 (TMAO & CVD-events meta-analysis); Schiattarella 2017 (TMAO meta); Zeisel & Warrier reviews on choline/TMAO; any egg-TMAO systematic review. Harvest reference lists for the primary mechanistic and feeding studies.
Budget: write 10 `source` notes; read ~20 sources properly (lean on the meta-analyses above to skim far more cheaply).
Mint every id'd node by piping its markdown on stdin (the body carries {{ID}}; the title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/eggs --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents.
Finish by writing your own orientation note in agent-notes/orientation/choline-tmao-pathway.md (sources as wikilinks under topic headings best-first, plus search_scope, exclusions, short slice paragraph).
Return: the S-ids you created, your orientation-note path (agent-notes/orientation/choline-tmao-pathway.md), gaps you hit, and a ≤10-line report (1 line per source).
```

### Searcher 8 — Egg nutrition beyond CVD (satiety/weight, choline-neuro, lutein, protein, allergy, foodborne)

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set. Your role is a 1b searcher; do NOT spawn subagents.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/eggs
Main question (verbatim): "Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?"
Your slice: Everything about egg health OUTSIDE the CVD/diabetes/lipid axis — the "what else should we be paying attention to" the FLF framing invites. Cover these threads, mostly one primary each (breadth over depth): (i) SATIETY & WEIGHT/BODY-COMPOSITION — egg-breakfast satiety and weight-loss RCTs (Vander Wal 2005/2008; Ratliff 2010; Fallaize 2013); (ii) CHOLINE as an ESSENTIAL BENEFICIAL nutrient — maternal choline & infant neurodevelopment (Caudill 2018 FASEB J; Zeisel choline-essentiality; choline adequacy/AI intake data), and NAFLD/liver relevance; (iii) LUTEIN/ZEAXANTHIN & eye health — egg-yolk carotenoid bioavailability and macular/AMD outcomes (Handelman; Chung; egg-lutein intervention trials); (iv) high-quality PROTEIN & MUSCLE — egg protein/leucine and muscle-protein synthesis, elderly/sarcopenia (van Vliet 2017 whole-egg vs egg-white MPS); (v) EGG ALLERGY & early introduction (LEAP-style / EAT study egg arm; egg-allergy epidemiology); (vi) FOODBORNE / SALMONELLA risk (Salmonella Enteritidis in eggs, CDC/EFSA burden estimates) and any other harm (e.g. egg & specific-cancer signals if primary). Keep balance: this slice is where the clear BENEFITS live (satiety, choline, lutein, protein) AND concrete non-CVD HARMS (Salmonella, allergy) — mint both, don't produce an all-positive list. Record endpoint/outcome per source and its population (pregnant women, infants, elderly, general).
What you must NOT touch: any CVD/mortality or lipid or TMAO or diabetes outcome — those are slices 1-7 (in particular, choline→TMAO/harm is slice 7; you own choline only as a beneficial nutrient); substitution/methodology (slice 9). A weight-loss trial in a disease population reporting mainly glycemic/lipid outcomes belongs to slice 6 — you take the appetite/satiety/body-composition-focused trials. Record others' papers under found_via/exclusions, do not mint.
Discovery hubs to MINE (do NOT node them): egg-and-satiety reviews; Wallace 2018 and Zeisel choline-intake reviews; AREDS/lutein reviews; protein-quality/DIAAS reviews; EFSA/CDC egg-Salmonella reports; any "eggs beyond cholesterol / egg nutrient-density" review. Harvest reference lists for the primaries.
Budget: write 10 `source` notes; read ~20 sources properly (lean on the reviews above to skim far more cheaply).
Mint every id'd node by piping its markdown on stdin (the body carries {{ID}}; the title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/eggs --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents.
Finish by writing your own orientation note in agent-notes/orientation/egg-nutrition-beyond-cvd.md (sources as wikilinks under topic headings best-first, plus search_scope, exclusions, short slice paragraph).
Return: the S-ids you created, your orientation-note path (agent-notes/orientation/egg-nutrition-beyond-cvd.md), gaps you hit, and a ≤10-line report (1 line per source).
```

### Searcher 9 — Substitution analyses + confounding / healthy-user bias + methodology critiques

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set. Your role is a 1b searcher; do NOT spawn subagents.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/eggs
Main question (verbatim): "Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?"
Your slice: The "HOW CAN WE TELL / appropriate ways of knowing" layer the FLF framing foregrounds — the epistemics of the egg evidence. Three threads: (i) SUBSTITUTION ANALYSES — primaries whose HEADLINE is that the health association of eggs depends on the comparator (eggs replacing refined carbs/processed meat vs replacing other protein/unsaturated fat flips the sign): isocaloric-substitution modelling papers (e.g. the substitution analyses reported as the focus in Zhong 2019, Drouin-Chartier 2020, Virtanen; and dedicated food-substitution methodology papers). Where a substitution result is only a secondary analysis inside a slice-1/2 cohort you have already-minted elsewhere, mine it via found_via and set duplicate_of rather than re-minting the cohort. (ii) CONFOUNDING / HEALTHY-USER BIAS — papers demonstrating or quantifying residual confounding, the healthy/unhealthy-user bias in egg cohorts (egg eaters' co-behaviours — bacon, smoking, activity, SES), and negative-control/quantitative-bias analyses in nutrition epidemiology. (iii) NUTRITIONAL-EPIDEMIOLOGY METHODOLOGY as PRIMARY position artifacts — Ioannidis 2018 JAMA ("The challenge of reforming nutritional epidemiologic research"); Archer memory-based dietary-assessment critique; Schoenfeld & Ioannidis ("Is everything we eat associated with cancer?"); the NutriRECS/Zeraatkar-Johnston GRADE reappraisal approach (red-meat precedent, applied as a way-of-knowing template); FFQ measurement-error primaries. These methodology papers ARE primary artifacts of a position — mint them. Keep balance: substitution and confounding critiques cut BOTH ways (some inflate apparent harm, some inflate apparent safety) — represent both, and include at least one defence of nutritional-cohort validity, not only the critics.
What you must NOT touch: the cohort papers and feeding trials themselves (slices 1-8) — you own the analyses/critiques ABOUT them, not the underlying data papers (mine those via found_via). Record others' papers under found_via/exclusions, do not mint. NOTE: this is a METHODOLOGY slice, not an independent-data slice — many substitution results share the cohort data bases of slices 1/2, so lean on duplicate_of/found_via to keep the pool honest about that.
Discovery hubs to MINE (do NOT node them): Ioannidis and Trepanowski nutrition-methodology commentaries; the substitution-analysis sections of Zhong 2019 / Drouin-Chartier 2020; GRADE/NutriRECS working-group papers; any "confounding in nutritional epidemiology" review. Harvest reference lists for the primaries.
Budget: write 10 `source` notes; read ~20 sources properly (lean on the reviews above to skim far more cheaply).
Mint every id'd node by piping its markdown on stdin (the body carries {{ID}}; the title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/eggs --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents.
Finish by writing your own orientation note in agent-notes/orientation/substitution-confounding-methodology.md (sources as wikilinks under topic headings best-first, plus search_scope, exclusions, short slice paragraph).
Return: the S-ids you created, your orientation-note path (agent-notes/orientation/substitution-confounding-methodology.md), gaps you hit, and a ≤10-line report (1 line per source).
```

---

## 4. Notes for the consolidator (1c) / audit

- Per-searcher WRITE budgets sum to **100**; READ budgets sum to **200**. If a slice underfills, the likely shortfalls are slice 9 (some items are commentaries/position pieces, not indexed trials, and much substitution content is secondary analysis to be recorded via found_via rather than minted) and slice 5 (responder/ApoE primaries are a smaller literature than the mean-effect feeding trials).
- **Independence guarantees to audit:** (a) the Western (slice 1) vs Asian/multinational (slice 2) split should yield ≥6 distinct Western + several distinct non-Western cohort families — if the pool collapses onto NHS/HPFS re-analyses, flag it; (b) the lipid pathway (3/4/5) vs TMAO pathway (7) should both be represented as independent mechanism bases; (c) observational (3) vs interventional (6) diabetes evidence should both be present.
- **Balance to audit:** harm, neutral, and beneficial anchors each appear; the critical/methodology side (slice 9) and the beyond-CVD side (slice 8) are each covered. If either dedicated slice came back thin, spawn a top-up searcher for it.
- **De-dup watch:** Hu 1999 and Zhong 2019 are owned by slice 1 (CVD) but also report diabetic subgroups / substitution results — expect slices 3 and 9 to reference them via found_via, not re-mint. Blesso 2013 sits at the 4/6 boundary (whole-egg RCT in metabolic syndrome). DiMarco 2017 sits at the 4/7 boundary (lipids + TMAO). Check these three for accidental double-minting.
- Each searcher writes exactly one orientation note in agent-notes/orientation/, named after its slice: western-cvd-cohorts.md, asian-multinational-cvd-cohorts.md, egg-diabetes-observational.md, feeding-rcts-lipids-healthy.md, responders-apoe-genotype.md, egg-rcts-diabetic-metabolic.md, choline-tmao-pathway.md, egg-nutrition-beyond-cvd.md, substitution-confounding-methodology.md.
- Seed papers named in the prompts are anchors/leads, not a closed list, and some citations are from memory — searchers must verify metadata on the page (venue, year, citation count, funding) per the mode file's "capture metadata on the page" step.
