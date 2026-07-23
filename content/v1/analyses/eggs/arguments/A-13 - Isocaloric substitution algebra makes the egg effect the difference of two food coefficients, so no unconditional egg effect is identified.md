---
id: A-13
type: argument
statement: "Because a substitution HR is the contrast between two foods' coefficients under a constrained total, the estimated effect of eggs is definitionally comparator-relative, so this design identifies no single unconditional egg effect."
source: "[[S-89 - Substitution analysis- replacing eggs with other protein foods and CVD-mortality risk]]"
locator: "Methods (substitution model); Discussion"
affects_observations: ["[[O-41 - Sign and size of the egg-removal effect depend on the comparator food; eggs rank near processed meat]]"]
affects_hypotheses: ["[[H-18 - The egg-health effect is a property of the comparator not of eggs alone, so eggs good-or-bad is ill-posed]]"]
---
In the substitution model Y = a*F1 + b*F2 + covariates, with the total amount of protein foods held fixed, decreasing F1 by one unit while increasing F2 by one unit changes the linear predictor by (b - a). The reported substitution hazard ratio is therefore exp(b - a): the contrast between the two foods' coefficients, not an absolute coefficient for either food.

Consequently the estimated "effect of removing eggs" equals (beta_comparator - beta_eggs) and takes a different value for every comparator - near-null when the comparator is itself unhealthy (processed meat, whose coefficient is close to eggs') and strongly protective when the comparator is healthy (nuts or whole grains, with much lower coefficients). The design never contrasts eggs against a fixed baseline (e.g. total calories or "no egg"), so it cannot estimate an unconditional egg coefficient at all. The authors make the same point concretely: substituting eggs with unprocessed red meat lowers risk yet is not a healthy choice, because red meat is itself harmful.

This is an identity of the linear model, valid regardless of confounding or measurement error, and it converts the ill-posed question "are eggs good or bad" into the well-posed "eggs relative to what."
