---
type: argument
id: A-5
statement: "The population-average dietary-cholesterol response overstates harm for hypo-responders and understates it for hyperresponders"
source: "[[S-5 - Characteristics of human hypo- and hyperresponders to dietary cholesterol]]"
locator: "Discussion"
affects_observations:
  - "[[O-16 - Serum-cholesterol response to dietary cholesterol is consistent within individuals across repeated trials]]"
  - "[[O-17 - Cholesterol responsiveness correlates with HDL2-total-cholesterol rise but not with habitual intake or body weight]]"
affects_hypotheses:
  - "[[H-7 - A stable, lifestyle-independent subset of hypo-responders exists for whom dietary cholesterol raises serum cholesterol little]]"
status: approved
reason_if_not_false: checked
---

## Reasoning

The feeding data show two things jointly: (1) an individual's serum-cholesterol response to dietary cholesterol is reproducible across repeated trials, so it is a stable trait rather than noise; and (2) that trait does not correlate with any observable lifestyle marker (habitual cholesterol intake, body weight). A population mean therefore blends a genuinely heterogeneous mixture of low- and high-responders. Averaging is only representative of an individual when the underlying quantity is homogeneous; here it is not, so the mean LDL/serum-cholesterol rise reported for a population systematically overstates the effect for the hypo-responder subset and understates it for the hyperresponder subset. Because the trait is unpredictable from lifestyle, one cannot ex ante assign an individual to the correct subgroup, which is exactly why a single population-average figure is a poor guide to any given person's risk.

## Step 6 verdict
**approved / checked.** Reconstruction: premises = (a) individual response is reproducible across repeated trials (stable trait), (b) the trait is uncorrelated with observable lifestyle markers; conclusion = the population mean misrepresents the response for identifiable subgroups and cannot be assigned ex ante. Load-bearing step is elementary and traced: given a genuinely heterogeneous mixture, the mean lies strictly between the subgroup means, so it necessarily overstates the effect for the low-responder subset and understates it for the high-responder subset — this follows from (a) alone, which rules out the alternative that apparent heterogeneity is measurement noise around a common value. Premise (b) is what blocks ex ante assignment; without it the conclusion 'misleading for subgroups' would still hold but the subgroups would be identifiable. Both parts of the conclusion are supported by their respective premises, and no undercutting defeater survives given (a).
