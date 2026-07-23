---
type: hypothesis-cluster
id: HC-14
hypotheses:
  - "[[H-39 - Choline is an essential nutrient for humans when dietary methionine and folate are not in excess]]"
  - "[[H-48 - Dietary choline is not an essential nutrient]]"
exclusivity: "Either dietary choline is essential when methionine/folate are adequate but not in excess (H-39) or endogenous synthesis suffices so it is not essential (H-48); exactly one holds."
exhaustive_by_construction: true
independence: "Choline essentiality is a nutritional-biochemistry fact independent of the disease-effect clusters, including the choline->TMAO clusters, which concern a harm pathway rather than essentiality; its prior is independent."
depends_on: []
question: "Is dietary choline (abundant in eggs) an essential nutrient for humans?"
relevance: "A 'what else' benefit channel - eggs as a dense source of an essential nutrient."
---

![[H-39 - Choline is an essential nutrient for humans when dietary methionine and folate are not in excess]]

![[H-48 - Dietary choline is not an essential nutrient]]

## Carving

The sub-question is whether dietary choline, of which eggs are a dense source, is an essential nutrient for humans. Two exhaustive answers: essential when methionine and folate are adequate but not in excess (H-39) or not essential because endogenous PEMT synthesis suffices (H-48, constructed). Analysis-failure mode: the depletion evidence came from a short choline-free regimen in selected men; if de novo synthesis covers ordinary requirements in normally-nourished people, the analysis would favour H-39 when H-48 holds - the failure favours the constructed null. Historically H-39 prevailed - an Adequate Intake was set in 1998 - which informs but does not fix the prior. exhaustive_by_construction is set; H-48 is minted as the complement.

## Prior

```python
# HC-14 prior — is dietary choline (dense in eggs) an essential nutrient for humans. Exhaustive by
# construction (exactly one holds; no residual, so rule 4 does not apply). Members in HC-14.hypotheses
# order: [H-39 essential when methionine/folate adequate-but-not-in-excess, H-48 not essential (PEMT
# synthesis suffices)].
# Evidence split: nothing is marked used_for_prior. The only inbound edges are the Zeisel choline-
# depletion trial (CG-33: plasma-choline fall, ALT rise, cholesterol fall) — the case-specific test the
# cluster turns on, left in full for step 8. no_observation_arguments.py --cluster HC-14 returns none. The
# prior rests on the outside view: the standing expert-consensus classification, discounted for its
# evidentiary tier and for the analysis-failure mode the carving flags (a short choline-free regimen in
# selected men favours the constructed null).

# H-39 anchor — choline is (conditionally) essential. Reference class: nutrients formally recognised as
# required by an expert body on controlled depletion-repletion evidence. The US IOM set an Adequate Intake
# for choline in 1998 (550 / 425 mg/d men/women) — a standing consensus that it is required; such
# classifications are seldom later reversed. Most confident member. What it omits: the requirement is
# conditional on methionine/folate not being in excess, and interindividual (sex, genotype) variation is
# large.
p_essential_consensus_holds = 0.82   # base rate that an expert-body essentiality judgment backed by depletion-repletion data survives
w_h39 = 1.0   # unit anchor: the established/consensus reading

# H-48 not essential, odds vs H-39. What would have to be true: endogenous PEMT synthesis plus usual
# methionine/folate covers requirements in ordinarily-nourished people, so a choline-free diet does not
# *reliably* produce deficiency. Reference class / footing: choline carries an Adequate Intake, not an RDA
# (data were insufficient for an EAR/RDA — a weaker evidentiary tier), and de novo synthesis genuinely
# covers requirements for part of the population (e.g. premenopausal women, estrogen-upregulated PEMT).
# The carving's analysis-failure mode (depletion shown only in selected men) further tilts toward this null.
# Clearly the minority reading, but with real support.
base_odds_h48 = (1 - p_essential_consensus_holds) / p_essential_consensus_holds   # odds identity from the base rate, not an estimate
caveat_inflation_h48 = 1.3   # AI-not-RDA evidentiary tier + synthesis covers part of the population + failure-mode favours the null
w_h48 = base_odds_h48 * caveat_inflation_h48 * w_h39

prior("HC-14", [w_h39, w_h48])
```
