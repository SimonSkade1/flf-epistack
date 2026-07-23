---
id: A-10
type: argument
statement: "The T2D association appearing only in US studies (internally homogeneous at 1.18) but not in non-US studies, combined with the finding that adjusting for eggs' cholesterol and protein content did not materially change the COSM estimate, is better explained by egg intake marking the surrounding dietary pattern than by a nutrient-mediated causal effect of eggs."
source: "[[S-8 - Wallin 2016 Diabetologia - egg consumption and T2D in the Cohort of Swedish Men + updated dose-response meta-analysis]]"
locator: "Discussion"
affects_observations: ["[[O-31 - Wallin meta-analysis US-vs-non-US split - egg-T2D HR 1.18 (US, I2 0%) vs 0.97 (non-US)]]", "[[O-29 - Cohort of Swedish Men - egg intake and T2D functionally null (p-trend 0.06) with register-based outcomes]]"]
affects_hypotheses: ["[[H-13 - Egg consumption is a marker of the Western dietary pattern that drives T2D, not a causal factor]]", "[[H-14 - Egg-T2D association is positive in US populations but null in non-US (European and Japanese) populations]]"]
status: approved
reason_if_not_false: checked
---
Reasoning (A-10): Two features of the data jointly discriminate a causal from a marker interpretation. First, the candidate causal mediators of an egg effect are its cholesterol and protein content, which are constant across countries; yet in COSM, additionally adjusting the model for cholesterol and protein intake did not substantially alter the (already near-null) egg-T2D estimate. If cholesterol or protein were driving risk, controlling the association's own proposed mechanism should have moved it - it did not, arguing the residual signal is not nutrient-mediated. Second, the association is present only in US cohorts and, notably, is internally consistent there (I2 0% at HR 1.18) while absent in non-US cohorts (0.97). A universal biological effect of eggs cannot switch on only in the US; what differs is the diet eggs accompany - a Western pattern (red/processed meat, fried potatoes, high-fat dairy, sweets, refined grains) in the US versus prudent/traditional patterns where eggs are eaten in Japan. Register-based outcome ascertainment in COSM (low misclassification) makes it unlikely the non-US null is an artefact of missed cases. Taken together, egg intake behaving as a proxy for the local dietary pattern explains both the geographic on/off pattern and the mechanism-adjustment null more parsimoniously than a direct causal effect. The argument is inferential, not deductive: unmeasured effect-modification by a genuinely causal egg effect remains logically possible.

## Validity (step 6)

status: approved, reason_if_not_false: checked.

Traced both prongs. Prong 1 (mediator-adjustment): if eggs raise T2D risk *through* their cholesterol/protein content, conditioning on cholesterol and protein intake should attenuate the egg coefficient; it did not move → those specific nutrients are not the operative mediators. The step is a valid mediation inference. It is weak here (COSM is already near-null, so there is little to attenuate and the mediator test was run in a cohort showing no effect), but weakness is a matter of strength, not validity, and the statement is framed as "better explained by," not a proof. Prong 2 (geographic on/off): a universal biological mechanism cannot switch on only in US cohorts, so an I2=0% signal at 1.18 confined to the US while non-US is 0.97 points to something that co-varies with geography — the accompanying diet — rather than the egg itself.

The statement is a comparative/parsimony claim ("better explained by … than by"), and both prongs push the same way, so the evidential step holds. The obvious undercutting defeater — effect-modification of a genuinely causal egg effect by the surrounding Western diet, which would also produce a US-only signal — is explicitly acknowledged and only downgrades the argument to evidential (which it already is), not refuted. Approved as stated.
