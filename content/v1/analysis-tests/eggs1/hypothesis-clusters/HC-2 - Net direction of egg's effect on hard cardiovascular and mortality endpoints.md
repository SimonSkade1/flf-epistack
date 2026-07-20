---
type: hypothesis-cluster
id: HC-2
hypotheses:
  - "[[H-2 - Moderate egg intake around one per day is protective against CVD]]"
  - "[[H-3 - High egg intake increases all-cause mortality, especially in diabetics]]"
  - "[[H-4 - Egg intake is essentially neutral for ischemic heart disease]]"
  - "[[H-9 - Moderate habitual egg intake is not associated with increased CVD risk in generally healthy Western adults]]"
  - "[[H-10 - Egg intake has no material effect on blood lipids, CVD, or mortality across diverse global populations]]"
  - "[[H-12 - Egg's net effect on hard cardiovascular and mortality endpoints is not a single population-wide direction]]"
exclusivity: "The members answer the net direction of egg's effect on hard CVD / mortality endpoints: protective (H-2), harmful (H-3), or null (H-4, H-9, H-10). At most one direction dominates a given population. STRAINED: the three null members assert the same direction (~null), distinguished only by endpoint / population scope (IHD; healthy Western adults; diverse global populations), so they are not pairwise mutually exclusive - see body."
exhaustive_by_construction: false
independence: "The overall direction on hard endpoints factorizes from the surrogate-lipid magnitude (a lipid change need not translate into events) and from the subgroup/responder question (which is about variation, not the population-average direction)."
depends_on:
  - "HC-1: a large atherogenic-lipid effect mildly raises P(harmful direction); judged weak because the surrogate-to-event link is exactly what is contested - revisit at step 10"
question: "What is the net direction of habitual egg intake's effect on hard cardiovascular / mortality endpoints?"
relevance: "The hard-endpoint arm of the main question - the outcome (events / mortality) that ultimately settles net benefit / harm."
---
![[H-2 - Moderate egg intake around one per day is protective against CVD]]
![[H-3 - High egg intake increases all-cause mortality, especially in diabetics]]
![[H-4 - Egg intake is essentially neutral for ischemic heart disease]]
![[H-9 - Moderate habitual egg intake is not associated with increased CVD risk in generally healthy Western adults]]
![[H-10 - Egg intake has no material effect on blood lipids, CVD, or mortality across diverse global populations]]
![[H-12 - Egg's net effect on hard cardiovascular and mortality endpoints is not a single population-wide direction]]

Carving: the hard-endpoint (CVD-event / mortality) hypotheses, kept separate from the surrogate-lipid cluster per the run's steering. The clean exclusive dimension is direction: protective vs harmful vs null. H-2 and H-3 are the protective and harmful poles. **Mutual-exclusivity strain (flagged):** H-4, H-9 and H-10 all assert a ~null direction and were kept as separate members by 4a because their riders differ (H-4 restricts to ischemic heart disease and attributes the weak inverse signal to reverse causation; H-9 restricts to generally healthy Western adults up to ~1/day; H-10 spans low/middle/high-income populations and also covers lipids). They are therefore scope-refinements of a single "null" answer, not three competing answers - within one cluster they overlap (all could co-hold). Handling: I kept all three as members (no merging is 4b's remit, and 4a deemed them discriminable by scope), and treat the exclusivity as holding across the *direction poles* (protective / harmful / null) while explicitly recording that the three null variants are non-exclusive among themselves. Step 5 will link observations to each by its scope rider; step 7 priors on the three should be read as a partition of the null mass by population, not as independent rivals. Residual H-12 covers a direction-varying (J-shaped / non-monotonic) effect that no single-direction member captures.

## Prior

```python
# HC-2 prior - net direction of egg's effect on hard CVD / mortality endpoints. Members in HC-2.hypotheses
# order: [H-2 protective, H-3 harmful, H-4 null-IHD/reverse-causation, H-9 null-healthy-Western-<=1/day,
# H-10 null-diverse-global, H-12 residual (direction varies)].
# Inputs: outside view on nutritional epidemiology of single foods. `no_observation_arguments.py --cluster HC-2`
# returned none. NO inbound E edge was marked used_for_prior: true - E-14..E-23 are all case-specific cohort
# results (CKB, PHS, EPIC, Harvard pooled, PURE) that discriminate between the members, so all ten are left
# whole for step 8.
#
# STRUCTURE (rule 2 prose, cluster-wide): H-4, H-9 and H-10 are not three independent rivals - they are a
# partition of the single "null" answer by scope rider (IHD + reverse-causation reading; generally healthy
# Western adults up to ~1/day; diverse global populations incl. low/middle-income). Pricing each at full
# strength against H-2/H-3 would triple-count the null branch and mechanically bury the directional members.
# So: price the null BRANCH as one quantity, then split that branch mass across the three by how plausible
# each one's scope rider is as the way the null actually holds. The branch total is the meaningful number;
# the internal split is a scope judgement and is the weakest part of this block.

# --- Null branch (H-4 + H-9 + H-10 together) ---
# What would have to be true: habitual egg intake, at ordinary levels, has no material causal effect on hard
# endpoints, and the observed inverse/positive associations are confounding or reverse causation. Reference
# class: single common foods eaten at ordinary doses, studied in observational cohorts, where the mechanistic
# story runs through a surrogate (here dietary cholesterol -> LDL). In that class the honest population-average
# answer is far more often "no detectable effect on events" than a demonstrated direction. This is the anchor.
w_null_branch = 1.0

# Split of the branch by scope plausibility (shares of the branch, not independent estimates).
# H-9's rider is the least demanding: it only claims a null in generally healthy Western adults up to ~1/day -
# the narrowest, best-covered scope, and the one hardest to be wrong about.
share_h9 = 0.45
# H-4's rider adds a mechanism claim (the weak apparent inverse IS reverse causation) on top of an IHD-only
# null. More content than H-9, so less likely to hold exactly, but the reverse-causation reading is a common
# and well-supported failure mode in diet cohorts.
share_h4 = 0.30
# H-10 is the strongest of the three: a null across diverse global populations INCLUDING low/middle-income,
# and on lipids too. Broad-scope universal nulls in nutrition usually break somewhere (baseline intake and
# background diet differ enormously between, say, rural China and the US), so it gets the smallest share.
share_h10 = 0.25
w_h4  = w_null_branch * share_h4
w_h9  = w_null_branch * share_h9
w_h10 = w_null_branch * share_h10

# --- H-2 protective (moderate intake ~1/day protective against CVD) ---
# What would have to be true: eggs displace worse foods or supply something causally protective, strongly
# enough to show as fewer hard events. Odds against the null branch. Priors here are set by how often, in this
# reference class, a nutrient-dense whole food turns out to be genuinely protective on hard endpoints rather
# than only apparently so via healthy-user confounding - uncommon, and eggs are not a food with an established
# protective mechanism at the event level. Does not cover population-specific protection (that is H-12).
odds_protective_vs_null = 0.22
w_protective = w_null_branch * odds_protective_vs_null

# --- H-3 harmful (high intake raises all-cause mortality, especially in diabetics) ---
# What would have to be true: the dietary-cholesterol -> LDL -> events chain carries through at habitual doses.
# Slightly lower than H-2 as a population-wide claim, because H-3's most credible content (the diabetic excess)
# is a subgroup claim that H-12 expresses better; as a whole-population mortality direction it is a strong ask.
odds_harmful_vs_null = 0.18
w_harmful = w_null_branch * odds_harmful_vs_null

# --- H-12 residual: no single population-wide direction (J-shape / effect-modification) ---
# Concretely: null or protective at low-to-moderate intake in low-baseline-intake populations, harmful at high
# intake or in diabetics/hyperresponders - so no single member's direction is right. Own argued weight (rule 4):
# in nutrition questions that have stayed contested for decades across large well-powered cohorts with
# conflicting signs, "the direction is not one number" is a live and fairly common resolution, so this is priced
# well above a token residual. It also absorbs answers nobody here modelled (e.g. the effect is entirely about
# what eggs displace, not eggs).
odds_varies_vs_null = 0.35
w_varies = w_null_branch * odds_varies_vs_null

prior("HC-2", [w_protective, w_harmful, w_h4, w_h9, w_h10, w_varies])
```
