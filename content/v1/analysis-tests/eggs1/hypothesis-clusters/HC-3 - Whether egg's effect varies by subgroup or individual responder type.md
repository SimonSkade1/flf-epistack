---
type: hypothesis-cluster
id: HC-3
hypotheses:
  - "[[H-6 - Two eggs-day does not worsen cardiovascular risk factors in people with type 2 diabetes or prediabetes]]"
  - "[[H-7 - A stable, lifestyle-independent subset of hypo-responders exists for whom dietary cholesterol raises serum cholesterol little]]"
  - "[[H-13 - Egg's effect is essentially homogeneous across people with no stable protected subgroup or responder class]]"
exclusivity: "The members answer whether egg's effect is heterogeneous across people: a specific vulnerable subgroup (diabetics) is in fact NOT harmed (H-6), an intrinsic hypo/hyper-responder trait partitions individuals (H-7), or the effect is essentially homogeneous (residual H-13). STRAINED: H-6 (subgroup safety) and H-7 (responder trait) are two different axes of heterogeneity and could co-hold - see body."
exhaustive_by_construction: false
independence: "Whether the effect varies across people factorizes from its population-average direction (HC-2) and surrogate magnitude (HC-1): heterogeneity can exist around any mean."
depends_on: []
question: "Does egg / dietary-cholesterol's health effect vary systematically across subgroups or individuals, or is it essentially homogeneous?"
relevance: "The 'for whom' arm of the main question - who, if anyone, is differentially helped or harmed."
---
![[H-6 - Two eggs-day does not worsen cardiovascular risk factors in people with type 2 diabetes or prediabetes]]
![[H-7 - A stable, lifestyle-independent subset of hypo-responders exists for whom dietary cholesterol raises serum cholesterol little]]
![[H-13 - Egg's effect is essentially homogeneous across people with no stable protected subgroup or responder class]]

Carving: the heterogeneity / "for whom" hypotheses. **Mutual-exclusivity strain (flagged, secondary):** H-6 concerns a named vulnerable subgroup (T2D / prediabetes) not being harmed, while H-7 concerns an intrinsic individual responder trait; these are distinct heterogeneity axes and are not strictly exclusive - both can be true at once. I kept them as one cluster (both answer "the effect is not uniform, and here is a specific way it varies") against the residual H-13 (essentially homogeneous), accepting mild non-exclusivity rather than splitting into two thin two-member clusters under the fast-test time cap. A cleaner production carve would likely be two clusters: subgroup-vulnerability (diabetics) and responder-heterogeneity (hypo/hyper-responders). Non-exhaustive, so residual H-13 covers the homogeneous case.

## Prior

```python
# HC-3 prior - does egg's effect vary across people? Members in HC-3.hypotheses order:
# [H-6 T2D/prediabetes subgroup not harmed, H-7 intrinsic hypo/hyper-responder trait, H-13 residual: homogeneous].
# Inputs: outside view on heterogeneity claims in nutrition. `no_observation_arguments.py --cluster HC-3`
# returned NONE, so no argument moved a number here.
# Evidence partition (rule 5): NO inbound edge is marked used_for_prior. All five (E-9, E-10, E-11, E-12, E-13)
# are case-specific and discriminating - E-9/E-10 speak directly to the diabetic subgroup, CG-7 (E-11+E-12) to
# the responder trait, E-13 to the dose-response shape. Marking any would hand step 8 a starved to-do set and
# manufacture confidence. The prior therefore rests on reference-class reasoning alone.
#
# LIMITATION (inherited from step 4's flagged exclusivity strain, and NOT repairable here): H-6 and H-7 are two
# distinct heterogeneity axes and can co-hold; step 5 found no observation that separates them from each other
# (edges separate each from the residual H-13, but not H-6 from H-7). The weights below therefore price each
# axis against the homogeneity residual, and the H-6:H-7 split is essentially unidentified by the evidence
# layer - treat their ratio as an artifact of the carve, not as a claim. Steps 9-10 should read the pair jointly.

# H-6 - a named vulnerable subgroup (T2D/prediabetes) turns out NOT to be harmed. Reference class: claims that a
# clinically singled-out metabolic subgroup is exempt from a diet effect. Such exemptions are argued often but
# hold up under adequate testing maybe a third of the time; diabetics are also the subgroup with the strongest
# prior reason to differ, which cuts both ways (differ = could be more harmed, not exempt).
p_subgroup_axis_real = 0.45   # right if T2D status genuinely modifies egg's effect at all
p_direction_protective = 0.5  # given modification, right if the modification is "not worse" rather than "worse"
w_h6 = p_subgroup_axis_real * p_direction_protective

# H-7 - a stable, lifestyle-independent hypo/hyper-responder trait partitions individuals. Reference class:
# reproducible inter-individual response traits in nutrition (e.g. salt sensitivity, glycaemic response). Wide
# between-person spread in short trials is near-universal, but most of it is measurement noise plus diet
# adherence; the fraction that survives repeat-challenge testing as a stable trait is a minority but a real one.
p_spread_observed = 0.9       # right if between-person spread in response is large - near-certain background fact
p_spread_is_stable_trait = 0.4  # right if that spread reproduces within-person rather than being noise/adherence
w_h7 = p_spread_observed * p_spread_is_stable_trait

# H-13 residual (rule 4, own argued weight) - the effect is essentially homogeneous: no protected subgroup and
# no stable responder class, all apparent variation being noise, confounding or adherence. Also absorbs
# heterogeneity axes nobody listed (e.g. APOE genotype, gut microbiome, baseline LDL) - an unmodelled answer
# here looks like "yes it varies, but along an axis neither member names". Weighted by how often a claimed
# heterogeneity in nutrition dissolves entirely on replication, which is common.
w_h13 = 0.5                   # ~0.5 vs the two axes above; not a leftover of them

prior("HC-3", [w_h6, w_h7, w_h13])
```
