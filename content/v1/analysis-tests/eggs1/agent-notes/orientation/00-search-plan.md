# Step 1 — Search plan (planner 1a)

Main question: "Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?"

## Literature survey (what bears on this, and the sides)

The debate splits cleanly along the three FLF-seeded design types, which also happen to be the natural cluster boundaries downstream (surrogate vs hard endpoints must NOT be merged):

1. **Mechanism / surrogate-endpoint (dietary cholesterol → blood LDL/ApoB).** Controlled-feeding and metabolic-ward studies and short RCTs measuring *blood lipids*, not events. Core fact: dietary cholesterol raises serum LDL, but with diminishing returns, partial homeostatic compensation (down-regulated endogenous synthesis), a parallel HDL rise, and large inter-individual spread. Pro-egg signal: null/small LDL effect, HDL up, ApoB unchanged (Sacks; several Fernandez-lab RCTs). Anti-egg signal: measurable LDL/ApoB rise per unit dietary cholesterol (Ginsberg; the Keys/Hegsted/Weggemans feeding-study tradition). Endpoint type = SURROGATE.
2. **Observational cohorts on hard endpoints (CVD events + all-cause mortality) in general populations.** The backbone for "overall." Anti-egg: Zhong 2019 (6 pooled US cohorts) and Physicians' Health Study (Djoussé) find higher CVD/mortality at high intake. Null/pro-egg: Harvard NHS/HPFS (Hu 1999; Drouin-Chartier 2020), PURE (50 countries), China Kadoorie Biobank (0.5M, *lower* CVD), Japanese cohorts. Endpoint type = HARD.
3. **Heterogeneity: subgroup / dose / responder variation.** Answers "for whom" and "at what level." Type-2 diabetics: observational subgroups suggest harm, yet RCTs in diabetics (DIABEGG, Fuller; Ballesteros) show 2 eggs/day is safe — a real pro/anti tension. Dose-response above ~1 egg/day (threshold vs linear). Inter-individual variation: hyper- vs hypo-responders (Katan; Herron/Fernandez) and ApoE genotype (ApoE4 carriers respond more). Endpoint type = MIXED (record per source).

**Recurring cohorts (independence hazard).** Cohort papers heavily re-analyse a few datasets: NHS/NHSII/HPFS (Harvard), the US pooled set (ARIC, CARDIA, Framingham Offspring, Jackson Heart, MESA — Zhong's Lifetime Risk Pooling Project), PURE, EPIC, China Kadoorie Biobank, UK Biobank, Physicians'/Women's Health Study, Japan (JACC/JPHC), Korea (KoGES/KNHANES), Rotterdam, SUN. Slice 2 must spread across *distinct* cohort families, one primary per family — not N re-analyses of NHS.

**Motivatedness hazard.** The egg industry (American Egg Board / Egg Nutrition Center) funds a large share of pro-egg work — much of the Fernandez lab, several egg RCTs, and the Alexander 2016 meta-analysis. Searchers must set `motivatedness` when funding/COI is disclosed. This is recorded as data, not used to discount now.

**Primary-only rule.** Reviews/meta-analyses are discovery hubs (mine their reference lists via `found_via`), never their own `source` node.

## Slice division (3 independent slices, ~20 notes total)

| slice | owns | endpoint | writes |
|---|---|---|---|
| **1 mechanism-surrogate** | feeding/RCT lipid studies in general/healthy adults | SURROGATE | 7 |
| **2 cohorts-hard-endpoints** | observational cohorts, general populations, distinct cohort families | HARD | 7 |
| **3 heterogeneity-subgroup-dose** | T2D (incl. RCTs-in-diabetics), dose-response, responder/genotype variation | MIXED | 6 |

**Crisp non-overlap boundaries** (designed so parallel searchers rarely collide):
1. Divider between 1 and 2 is *endpoint type*: blood lipids → slice 1; CVD events/mortality → slice 2.
2. Divider between 1 and 3 is *population/purpose*: an egg RCT in healthy adults → slice 1; an egg RCT in diabetics, or any study whose headline is responder/genotype heterogeneity → slice 3.
3. Divider between 2 and 3: slice 2 owns every *general-population* cohort event paper — **even if** it also reports a diabetic subgroup (e.g. Hu 1999, Zhong 2019). Slice 3 does NOT re-mint those; it takes RCTs-in-diabetics, dedicated diabetic-cohort analyses, dose-response-focused primaries, and responder/ApoE primaries.
4. If a searcher finds a paper that clearly belongs to another slice, they **leave it** (log as an exclusion "out of scope — slice X"), not mint it — avoids cross-slice duplicates while running in parallel.

**Balance baked in:** each slice prompt names concrete pro-egg AND anti-egg anchors and requires the searcher not to let one side dominate.

## Balance/independence self-check for this plan
- All three design types covered (1/2/3 = a/b/c). ✔
- Surrogate (slice 1) and hard (slice 2) endpoints kept in separate slices; slice 3 tags endpoint per source. ✔
- Pro and anti anchors named on every slice. ✔
- Slice 2 aimed at ≥6 distinct cohort families, one primary each. ✔
- Reviews/meta-analyses used only as hubs. ✔

---

# SEARCHER PROMPTS (spawn each as-is; orchestrator appends the TEST-RUN NOTICE)

## Searcher-prompt 1b-A (slice: mechanism-surrogate)

Read .claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set.
Analysis directory: projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/eggs1
Main question (verbatim): "Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?"
Your slice: **mechanism-surrogate** — controlled-feeding / metabolic-ward studies and short RCTs in general or healthy adults that measure the response of BLOOD LIPIDS (LDL-C, ApoB, HDL, total:HDL ratio, lipoprotein particles) to dietary cholesterol / egg intake. This is the surrogate-endpoint, mechanistic evidence. You MUST NOT touch the other two slices: **slice 2 cohorts-hard-endpoints** (observational CVD-event / mortality cohorts) and **slice 3 heterogeneity-subgroup-dose** (RCTs specifically in type-2 diabetics, dose-response-focused papers, and hyper-/hypo-responder or ApoE-genotype studies). Rule of thumb: if the outcome is a blood lipid measured in general/healthy adults → yours; if the outcome is a clinical event → slice 2; if the study population is diabetics or its headline is responder/genotype variation → slice 3. Keep balance: mint BOTH studies showing a measurable LDL/ApoB rise from dietary cholesterol (e.g. the Ginsberg controlled-feeding and Keys/Hegsted/Weggemans feeding tradition) AND studies showing null LDL / HDL-up / no-ApoB-change (e.g. Sacks NEJM egg-feeding; Fernandez-lab whole-egg RCTs) — do not let one side dominate. Record endpoint = surrogate and set `motivatedness` whenever egg-industry (American Egg Board / Egg Nutrition Center) or similar funding/COI is disclosed (common in this slice). Discovery hubs to mine for primaries (do NOT node them): Clarke 1997 BMJ metabolic-ward meta-analysis, Weggemans 2001 AJCN dietary-cholesterol meta-analysis, Berger 2015 AJCN, and McNamara / Vincent dietary-cholesterol reviews — harvest their reference lists. Seed primaries to check (not exhaustive; snowball out): Ginsberg 1994/1995 (controlled feeding, healthy men), Sacks 1984 NEJM (eggs in vegetarians), Blesso/DiMarco/Mutungi Fernandez-lab whole-egg RCTs, Njike 2010 (daily egg, lipids/endothelial), Kim & Campbell 2018 crossover.
Budget: write 7 source notes; read properly ~7 sources (lean on the meta-analyses above to skim many candidates cheaply).
Mint every source node with:
  python3 .claude/skills/flf-epistack/scripts/create_node.py "projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/eggs1" --type source --title "..."
Never hand-pick an id, and do not spawn subagents.
Finish by writing your own orientation note in agent-notes/orientation/mechanism-surrogate.md (per the mode file's spec: sources as wikilinks under topic headings best-first, plus search_scope, exclusions, and a short slice paragraph).
Return: the S-ids you created, any gaps you hit, and a 1-line-per-source list.

## Searcher-prompt 1b-B (slice: cohorts-hard-endpoints)

Read .claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set.
Analysis directory: projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/eggs1
Main question (verbatim): "Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?"
Your slice: **cohorts-hard-endpoints** — observational / epidemiological cohort (and nested case-control) studies in GENERAL adult populations reporting HARD endpoints: incident CVD (CHD, stroke, heart failure) and all-cause or cause-specific mortality, versus habitual egg intake. You MUST NOT touch the other two slices: **slice 1 mechanism-surrogate** (blood-lipid / ApoB response studies) and **slice 3 heterogeneity-subgroup-dose** (RCTs in diabetics, dose-response-focused primaries, responder/ApoE studies). You OWN every general-population cohort event paper even if it also reports a diabetic subgroup (e.g. Hu 1999, Zhong 2019) — slice 3 will not re-mint those. **Independence is the priority here:** cohort papers re-analyse a few datasets, so spread across ≥6 DISTINCT cohort families and mint at most one primary per family — do NOT take multiple re-analyses of the same cohort. Target families (pick the most informative primary in each): Harvard NHS/NHSII/HPFS (Drouin-Chartier 2020 BMJ, or Hu 1999 JAMA), US pooled set / Zhong 2019 JAMA (ARIC+CARDIA+Framingham Offspring+Jackson Heart+MESA), PURE (Dehghan 2020, 50 countries), China Kadoorie Biobank (Qin 2018 Heart, 0.5M), EPIC (find the EPIC egg–CVD/mortality primary), UK Biobank, Physicians' / Women's Health Study (Djoussé 2008), Japan JACC/JPHC, plus optionally Korea (KoGES/KNHANES), Rotterdam, or SUN. Keep balance: include BOTH harm-finding cohorts (Zhong 2019, Djoussé/Physicians') AND null-or-protective cohorts (PURE, China Kadoorie's lower-risk finding, Harvard's null, Japanese nulls) — do not let one side dominate. Record endpoint = hard, capture citation counts (these are highly-cited), and set `motivatedness` where funding/COI is disclosed. Discovery hubs to mine (do NOT node them): Rong 2013 BMJ, Drouin-Chartier 2020 BMJ meta portion, Shin 2013 AJCN, Krittanawong 2021 and Godos 2021 dose meta-analyses, Alexander 2016 (egg-industry-funded — note it) — harvest their reference lists to reach the distinct-cohort primaries.
Budget: write 7 source notes; read properly ~7 sources (lean on the meta-analyses above to skim many candidates cheaply).
Mint every source node with:
  python3 .claude/skills/flf-epistack/scripts/create_node.py "projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/eggs1" --type source --title "..."
Never hand-pick an id, and do not spawn subagents.
Finish by writing your own orientation note in agent-notes/orientation/cohorts-hard-endpoints.md (per the mode file's spec: sources as wikilinks under topic headings best-first, plus search_scope, exclusions, and a short slice paragraph).
Return: the S-ids you created, any gaps you hit, and a 1-line-per-source list.

## Searcher-prompt 1b-C (slice: heterogeneity-subgroup-dose)

Read .claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set.
Analysis directory: projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/eggs1
Main question (verbatim): "Is habitual egg consumption net beneficial, harmful, or neutral for human health — overall, for whom, and at what level of intake?"
Your slice: **heterogeneity-subgroup-dose** — evidence on FOR WHOM and AT WHAT LEVEL: (i) type-2 diabetics, especially RCTs in diabetics (DIABEGG/Fuller; Ballesteros one-egg-a-day in T2D) and dedicated diabetic-cohort analyses; (ii) dose-response above ~1 egg/day (threshold vs linear per-egg risk); (iii) inter-individual variation — hyper- vs hypo-responders to dietary cholesterol (Katan 1987; Herron/Fernandez responder-classification studies) and ApoE genotype (ApoE4 carriers). You MUST NOT touch the other two slices: **slice 1 mechanism-surrogate** (general-population blood-lipid RCTs) and **slice 2 cohorts-hard-endpoints** (general-population CVD/mortality cohorts). Do NOT re-mint general-population cohort papers that merely include a diabetic subgroup (Hu 1999, Zhong 2019 belong to slice 2); take diabetes-SPECIFIC primaries instead. Your slice spans BOTH endpoint types — record per source whether its outcome is surrogate (lipids/glycemia) or hard (events), so downstream clustering can separate them. Keep balance: include BOTH pro-egg heterogeneity findings (DIABEGG showing 2 eggs/day safe in T2D; existence of hypo-responders meaning population means overstate harm) AND anti-egg ones (diabetic subgroups/cohorts showing elevated risk; hyper-responders and ApoE4 carriers with large LDL rises) — do not let one side dominate. Set `motivatedness` for egg-industry funding, which is common in the diabetic-RCT and responder literature (Fernandez lab / Egg Nutrition Center). Discovery hubs to mine (do NOT node them): Tamez 2016 and Wallin egg-and-diabetes meta-analyses, Fernandez responder reviews, Ordovas ApoE reviews, and the dose-response meta-analyses (Godos 2021) — harvest their reference lists for primaries.
Budget: write 6 source notes; read properly ~6 sources (lean on the meta-analyses above to skim many candidates cheaply).
Mint every source node with:
  python3 .claude/skills/flf-epistack/scripts/create_node.py "projects/create a useful aligning (AI-)macroagents agenda/Participate in FLF competition/analysis-tests/eggs1" --type source --title "..."
Never hand-pick an id, and do not spawn subagents.
Finish by writing your own orientation note in agent-notes/orientation/heterogeneity-subgroup-dose.md (per the mode file's spec: sources as wikilinks under topic headings best-first, plus search_scope, exclusions, and a short slice paragraph).
Return: the S-ids you created, any gaps you hit, and a 1-line-per-source list.
