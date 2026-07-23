---
id: A-6
type: argument
statement: "That swapping eggs for whole grains, nuts or dairy lowers modelled T2D risk while swapping eggs for other animal proteins (meat, poultry, fish) shows no significant change is consistent with eggs being no more diabetogenic than the animal-food class they belong to, and supports (without establishing) the association being driven by the broader dietary pattern rather than something specific to eggs."
source: "[[S-4 - Drouin-Chartier 2020 AJCN - egg consumption and T2D in Harvard NHS-NHS II-HPFS pooling + updated meta-analysis]]"
locator: "Results/Discussion; substitution analysis"
affects_observations: ["[[O-19 - Substituting eggs with whole grains, nuts, yogurt or reduced-fat dairy lowers modelled T2D risk; other animal proteins no change]]"]
affects_hypotheses: ["[[H-9 - US egg-T2D association reflects residual confounding by the co-consumed Western dietary pattern, not a causal egg effect]]"]
status: corrected
reason_if_not_false: checked
---
Reasoning (A-6): Substitution modelling holds total energy fixed and asks what happens when one food displaces another, so the sign of each contrast reveals eggs' rank relative to the substitute rather than an absolute effect. Two facts constrain the interpretation. (a) Replacing eggs with plant foods (whole grains, nuts) or dairy (yogurt, reduced-fat milk) lowers modelled risk by ~9-19% - but this is expected because those foods are themselves inversely associated with T2D, so a lower-risk result follows from the substitute's benefit, not necessarily from eggs' harm. (b) Replacing eggs with red/processed meat, poultry, fish or unprocessed meat produces no significant change - i.e. within the animal-food class, eggs are interchangeable with other animal proteins for T2D risk. If eggs carried a specific diabetogenic property (e.g. via cholesterol) beyond being an animal food eaten in a Western pattern, swapping them for other animal proteins should still move risk; it does not. The pattern therefore locates eggs as one member of an animal-food/Western-pattern cluster rather than a distinctive cause, supporting the confounding-by-pattern reading. Caveat: substitution estimates are model-derived, not observed behaviour, and inherit the same residual confounding as the primary analysis.

## Validity (step 6)

status: corrected | reason_if_not_false: checked

Traced the step. The load-bearing move is: an egg->other-animal-protein substitution shows "no significant change" => eggs are no more diabetogenic than the animal-food class => eggs are a marker rather than a distinctive cause. Two links, of which the first has an undercutting defeater. "No significant change" is a failure to reject the null, not evidence of equivalence: a non-significant substitution contrast is equally produced by a genuinely underpowered comparison as by true equivalence, so "does not => eggs are no more diabetogenic (implies)" over-reads. Absence of evidence of a difference is not evidence of no difference. Hence the deductive "implies" fails; the weaker evidential form immune to the defeater - the null contrast is *consistent with*, and mildly supportive of, eggs-as-animal-food-marker - does hold, since equivalence remains one live reading of a null point estimate and it coheres with the confounding hypothesis. Note also the plant/dairy arm is correctly self-neutralised in the body (the risk drop there is attributed to the substitute's own inverse association, so it carries no weight for eggs' harm), leaving the whole inference resting on the animal-protein null. Corrected: "implies eggs are no more diabetogenic" -> "is consistent with eggs being no more diabetogenic"; the downstream "supports the broader-pattern reading" is retained as evidential, not probative. A second, non-fatal caveat (already in the body) is that substitution estimates are model-derived and inherit the primary analysis's residual confounding - this bears on premise truth (priced later), not on the corrected step.

## Original

statement: "That swapping eggs for whole grains, nuts or dairy lowers modelled T2D risk while swapping eggs for other animal proteins (meat, poultry, fish) does not implies eggs are no more diabetogenic than the animal-food class they belong to, consistent with the association being driven by the broader dietary pattern rather than something specific to eggs."
