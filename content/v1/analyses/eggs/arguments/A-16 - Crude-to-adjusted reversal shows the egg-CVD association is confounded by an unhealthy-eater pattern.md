---
id: A-16
type: argument
status: approved
reason_if_not_false: checked
statement: "The crude age-adjusted egg-CVD association (HR 1.10) reversing to null (0.93) only after adjustment for co-consumed foods and lifestyle shows the raw association is confounded by an unhealthy dietary/lifestyle pattern; the same correlation structure means residual confounding could still bias the adjusted estimate in either direction."
source: "[[S-19 - Drouin-Chartier 2020 BMJ - egg consumption and CVD in NHS, NHSII, HPFS]]"
locator: "Results, Table 1; Discussion"
affects_observations: ["[[O-44 - Moderate egg intake not associated with CVD in Harvard cohorts (adjusted HR 0.93), crude 1.10 reversing to null on adjustment]]", "[[O-43 - Higher egg intake tracks an unhealthier diet-lifestyle pattern (more red-processed meat, smoking, BMI, T2D) in Harvard cohorts]]"]
affects_hypotheses: ["[[H-21 - Moderate egg intake has no causal effect on CVD risk overall]]"]
---
Higher egg eaters differ systematically (O-43): higher BMI, more smoking, more red/processed meat, refined grains, sugar-sweetened beverages, and more prevalent type 2 diabetes -- a cluster of established CVD risk factors. Under age-only adjustment this cluster loads onto egg intake, producing the modest positive crude HR 1.10. Sequentially adjusting for these lifestyle and dietary covariates removes the shared variance and the estimate falls to 0.93 (null). That the estimate moves this much with adjustment is direct evidence the crude association is confounded rather than causal, supporting the adjusted null as the better causal estimate (H-21). The caveat runs the other way too: adjustment removes only measured confounding, and the same 'unhealthy eater' cluster (or imperfectly measured versions of the adjusted variables) could leave residual confounding biasing the adjusted 0.93 -- direction not guaranteed. So the reversal both licenses the null and flags its residual-confounding uncertainty.

## Validity assessment (step 6)

Traced step: adjusting for a cluster of measured covariates that are (a) correlated with egg intake and (b) established CVD risk factors, and watching the crude 1.10 collapse to 0.93, directly demonstrates that measured confounding produced the crude signal — this is confounding shown, not inferred to an unobservable. Candidate undercutting defeater: over-adjustment, i.e. some adjusted variables (BMI, T2D) could be mediators/downstream of the egg-containing diet, so part of the shift blocks a real causal path rather than removing confounding. It survives only partially: the pattern also contains unambiguous non-mediators (smoking, red/processed meat, refined grains, SSB — not caused by eating eggs), which carry the bulk of the reversal, so "the crude association is confounded by an unhealthy-eater pattern" holds even after discounting the mediator-adjustable subset. The statement's bidirectional residual-confounding caveat is already correct. approved / checked.
