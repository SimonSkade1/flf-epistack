---
id: A-17
type: argument
statement: "E-value analysis shows an unmeasured confounder would need to be associated with both egg intake and CVD by a risk ratio of at least ~1.43-fold to move the adjusted confidence interval to a positive association (or ~1.28-fold toward an inverse one), so only fairly strong unmeasured confounding could overturn the null."
source: "[[S-19 - Drouin-Chartier 2020 BMJ - egg consumption and CVD in NHS, NHSII, HPFS]]"
locator: "Results, E value calculation"
affects_observations: ["[[O-44 - Moderate egg intake not associated with CVD in Harvard cohorts (adjusted HR 0.93), crude 1.10 reversing to null on adjustment]]"]
affects_hypotheses: ["[[H-21 - Moderate egg intake has no causal effect on CVD risk overall]]"]
---
The E-value is the minimum strength of association, on the risk-ratio scale, that an unmeasured confounder would need with both the exposure and the outcome, beyond the measured covariates, to fully explain away an observed association or shift a confidence bound to a chosen value. Using the pooled per-egg HR 0.98 (0.92-1.04): shifting the lower bound 0.92 up to 1.01 (a positive association) requires a confounder associated with both egg intake and CVD by RR >=1.43; shifting the upper bound 1.04 down to 0.99 (an inverse association) requires RR >=1.28. Confounders of RR 1.43 are substantial relative to the diet/lifestyle confounders already adjusted, so the null is moderately robust: weak residual confounding cannot manufacture a materially positive egg-CVD association (supporting H-21). This is a bound on required confounding strength, not proof of no causation, and it depends on the point estimate sitting near the null.
