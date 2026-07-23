---
id: A-30
type: argument
statement: "Because PURE accrued over 14,000 composite events, its CI (0.89-1.04) is a precise, well-powered null rather than an underpowered non-finding: it is informative against moderate harm (upper bound ~1.04) and against benefit larger than ~11%, though a modest benefit up to ~11% remains consistent — and the bound is on random error in the observed association, not on a true causal effect if systematic bias (confounding, non-classical FFQ error) is present."
source: "[[S-91 - PURE study- egg intake, blood lipids, CVD and mortality in 50 countries (Dehghan 2020)]]"
locator: "Discussion (strengths)"
affects_observations: ["[[O-86 - In PURE one or more eggs per day not associated with composite CVD-mortality, total mortality, or major CVD]]"]
affects_hypotheses: ["[[H-37 - Moderate habitual egg intake up to one per day is neutral for CVD and mortality across income levels globally]]"]
status: corrected
reason_if_not_false: checked
---
The informativeness of a null association depends on statistical power. With 14,700 composite events in PURE (and >20,000 composite outcomes across the pooled analysis), standard errors are small: the composite HR is 0.96 with 95% CI 0.89-1.04, i.e. relative risks above ~1.04 or below ~0.89 for >=7 vs <1 egg/week are excluded. A study of this size would detect a true 10-15% change in risk with high probability, so the failure to find one bounds the true effect of moving from <1 to >=7 eggs/week to at most a few percent in either direction.

Hence this is a precise null - a near-zero effect is positively supported - rather than an underpowered non-finding that would be equally consistent with a large effect. This constrains how much the neutral hypothesis should be favoured by the data. The bound applies only to the sampled intake range (up to ~1 egg/day); the cohort has too few people eating well above 1 egg/day to say anything about higher intakes.

## Validity verdict — corrected (checked)

Reconstruction. Premises: ~14,700 composite events, HR 0.96 with 95% CI 0.89-1.04. Hidden premise: high event count → small standard error → the CI reflects genuine precision, so a narrow CI around 1.0 licenses reading the effect as near-zero rather than merely undetected. Conclusion (as stated): any material harm or benefit is unlikely.

Traced step. The power → precision core is valid: with this many events a true 10-15% harm would very likely have shown, so the null is a *precise* null, not an underpowered non-finding. But the as-stated conclusion overreaches on two points, so it is corrected to the weaker form the numbers support:
1. Asymmetry the CI ignores. CI 0.89-1.04 excludes harm above ~4% but still admits benefit up to ~11%. A "moderate benefit" of ~10% is therefore *consistent* with the data, so the symmetric "any material harm or benefit unlikely" is false on the benefit side; the body's own "at most a few percent in either direction" contradicts its stated lower bound of 0.89. The step survives only for harm (and for benefit >~11%).
2. Random vs systematic error (undercutting defeater that does not deny the premises). A narrow CI bounds *random* error only; it says nothing about systematic bias (confounding, non-classical FFQ misclassification per A-29). Granting the event count and CI, a true effect could still be masked by bias, so "material *true* harm/benefit unlikely" does not follow — only "the observed association is precisely estimated." The corrected statement restricts the claim to the observed association's random-error bound and the correct asymmetric magnitudes.

## Original

statement: "Because PURE accrued over 20,000 composite events, giving high power to detect even a modest excess risk, its confidence intervals hugging 1.0 make any material harm or benefit of moderate egg intake unlikely rather than merely undetected."
