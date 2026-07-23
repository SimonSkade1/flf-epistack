---
type: hypothesis-cluster
id: HC-13
hypotheses:
  - "[[H-5 - Eggs increase satiety and reduce hunger beyond their protein content]]"
  - "[[H-47 - Egg satiety is fully explained by protein content]]"
exclusivity: "Either eggs have a satiety effect beyond protein (H-5) or any greater fullness is fully explained by protein/energy (H-47); exactly one holds."
exhaustive_by_construction: true
independence: "The satiety/appetite channel is behaviorally distinct from the disease-endpoint clusters; its prior is independent."
depends_on: []
question: "Do eggs enhance satiety and appetite control beyond what their protein content explains?"
relevance: "A 'what else' weight/appetite channel bearing on the net-health verdict via body weight."
---

![[H-5 - Eggs increase satiety and reduce hunger beyond their protein content]]

![[H-47 - Egg satiety is fully explained by protein content]]

## Carving

The sub-question is whether eggs enhance satiety beyond what their protein content explains. Two exhaustive answers: an egg-specific effect beyond protein (H-5) or no effect beyond what protein and energy account for (H-47, constructed). Analysis-failure mode: unblinded subjective appetite ratings could register greater postbreakfast fullness in the high-egg arm from expectation effects or imperfect protein-matching, favouring H-5 when H-47 is correct - the failure favours the constructed null. exhaustive_by_construction is set (beyond-protein or not); H-47 is minted as the complement.

## Prior

```python
# HC-13 prior — do eggs enhance satiety beyond what their protein content explains?
# Members in HC-13.hypotheses order: [H-5 beyond-protein egg-specific satiety effect, H-47 fully explained by
# protein/energy]. exhaustive_by_construction: true — TWO members, NO residual (rule 4 does not apply).
# no_observation_arguments.py --cluster HC-13 returned none.
# EVIDENCE SPLIT: the single inbound observation O-7 (E-1) — greater postbreakfast satiety under matched protein
# in DIABEGG — is a case-specific RCT result that DISCRIMINATES the two members, so it is LEFT for step 8 and
# NOTHING is marked used_for_prior. The prior rests on outside-view appetite physiology.
# Odds anchored on the protein/energy-only member (H-47 = 1.0).

# Anchor — H-47 satiety fully explained by protein/energy. Outside view: protein is the most satiating
# macronutrient and dominates food-level satiety; eggs contain no fibre, so their fullness is largely a
# protein/energy effect. Most claimed food-SPECIFIC satiety differences shrink to null once protein and energy
# are accurately matched. So "no effect beyond protein" is the base-rate expectation and the member I favour.
w_protein_only = 1.0   # H-47 anchor: protein/energy explains food satiety once matched — the reference-class default

# H-5 beyond-protein egg-specific satiety effect. Decomposed into two judgeable factors: whether an egg-specific
# satiety channel beyond protein/energy exists at all (food-matrix, lipid, slower gastric emptying), and whether
# an apparent beyond-protein signal is real rather than an artifact of the analysis-failure mode the carving
# flags (unblinded subjective ratings + imperfect protein-matching bias appetite scores toward H-5).
p_beyond_channel = 0.50    # prob a real egg-specific satiety channel beyond protein/energy exists — modest; satiety is protein-dominated and eggs lack fibre
frac_real_not_artifact = 0.70   # given such a signal, fraction that is a true effect not an unblinded-rating / matching artifact
p_h5 = p_beyond_channel * frac_real_not_artifact   # prior prob H-5 is the true answer
odds_beyond = p_h5 / (1 - p_h5)   # odds of H-5 vs H-47 (1 - p is an identity, not an estimate)
w_beyond = odds_beyond * w_protein_only   # H-5

prior("HC-13", [w_beyond, w_protein_only])
```
