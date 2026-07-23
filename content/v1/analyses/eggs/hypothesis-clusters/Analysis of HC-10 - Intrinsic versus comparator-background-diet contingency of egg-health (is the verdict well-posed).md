---
type: cluster-review
cluster: "[[HC-10 - Intrinsic versus comparator-background-diet contingency of egg-health (is the verdict well-posed)]]"
---

#### What the analysis says

The question is whether egg-health is an intrinsic fixed property or a property of the comparator/background diet — i.e. whether an unconditional "eggs are good/bad" is even well-posed. Members: [[H-17 - Eggs are a relatively unhealthy protein source; benefit comes from replacing eggs with plant or fish protein]] (intrinsic low rank), [[H-18 - The egg-health effect is a property of the comparator not of eggs alone, so eggs good-or-bad is ill-posed]] (fully comparator-contingent), [[H-23 - Egg's CVD impact is relative to the food it replaces (neutral vs healthy proteins, better than red-processed meat)]] (substitution-indexed), [[H-38 - The health effect of eggs depends on background diet, being least harmful when displacing refined carbohydrate]], and residual [[H-57 - Some other egg-health characterization]].

The prior `[0.222, 0.267, 0.233, 0.167, 0.111]` was a pure outside view on the framing question: `contingency_vs_intrinsic = 3.0` (the field's default treats a single food's modelled effect as an isocaloric substitution quantity, so contingency is near-definitional). The posterior `[0.112, 0.443, 0.172, 0.189, 0.084]` has H-18 (ill-posed) leading, intrinsic H-17 halved. Two correlation groups pull opposite ways: CG-29 (region gradients + substitution swings across the Harvard/meta cohorts; `H18=1, H17=0.2, H23=0.75, H38=0.6`, trust 0.75) drives broad contingency and crushes intrinsic; CG-30 (Lifetime Risk Pooling: removing eggs lowers CVD 15-21% and mortality 11-22%, eggs ranking near processed meat; `H17=1, H18=0.7, H23=0.2, H38=0.5`, trust 0.62) favours a stable low rank but crushes H-23. Because CG-29 carries more observations and higher trust, H-18 wins; H-38 rises modestly on the region gradient.

#### What the model may not capture

The two CGs read the *same* Harvard-cohort family (overlapping D-1/D-7/D-9/D-25) as "no fixed effect" (CG-29) and "stable low rank" (CG-30). The model handles overlap *within* each joint call but cannot express that the two opposing pulls are not independent — H-18's lead partly rests on one dataset cut two ways.

H-18 and H-23 are barely distinct: "ill-posed without specifying the substitution" and "the effect is the difference from the displaced food" are nearly the same claim, H-18 the superset. The 0.443-vs-0.172 gap is largely a grain artifact and their exclusivity is weak.

Is the answer on the list? A partly-intrinsic/partly-contingent hybrid — a genuine cholesterol/choline load (CG-30's stable rank) *plus* substitution modulation (CG-29) — is exactly residual H-57, the natural reading if both CGs are partly right, yet it is sanded to 0.084 because H-18 absorbs the contingency mass. Deeper: the contingency members trace to Harvard substitution analyses (S-89, S-19) whose method *definitionally* yields comparator-relative estimates (A-13). "Eggs have no fixed effect" may be an artifact of modelling single foods as isocaloric substitutions — the prior's `3.0` already concedes this, so the cluster partly measures the analytic frame, not the food.

#### What would help

1. Whether H-18 and H-23 are separable at the observation level at all — *does not exist* / *unclear*.
2. A comparator-free, mechanistically-anchored egg contrast (eggs vs isocaloric-identical background on a hard endpoint) that could break the substitution tautology — *does not exist* (nutritional epi cannot produce an unconditional contrast).
3. Non-overlapping-cohort replication of the substitution rankings to de-correlate CG-29 and CG-30 — *exists, unread*.

#### Confusions and contradictions

CG-29 and CG-30 point opposite (contingent vs stable-low-rank) on overlapping data and the model prices both without resolving which the shared cohorts really support. Within CG-29, O-18's direction — eggs *more* harmful at *lower* diet quality — is the opposite of H-38's refined-carb-displacement prediction; the block flags this internal tension rather than hiding it, and it is shipped unresolved.
