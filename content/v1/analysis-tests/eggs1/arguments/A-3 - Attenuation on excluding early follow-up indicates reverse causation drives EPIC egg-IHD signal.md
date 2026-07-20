---
type: argument
id: "A-3"
statement: "The disappearance of the inverse egg-IHD association after excluding the first 4 years of follow-up is evidence that reverse causation contributes to the weak protective signal, and is consistent with a near-null true effect, but does not establish it."
source: "[[S-16]]"
locator: "Results (sensitivity analysis); Discussion"
affects_observations:
  - "[[O-9]]"
  - "[[O-10]]"
affects_hypotheses:
  - "[[H-4]]"
status: corrected
reason_if_not_false: checked
---

## reasoning
Reverse causation in nutritional cohorts arises when subclinical disease present at baseline changes behaviour: people with early undiagnosed illness eat fewer eggs (or are advised to), so low egg intake is a marker of pre-existing disease that then produces events early in follow-up, manufacturing a spurious inverse association. Excluding the first 4 years removes those early events (and thus the baseline-sick individuals' influence). That the HR 0.93/20g signal attenuates to nonsignificance under this exclusion is the diagnostic signature of reverse causation rather than a robust protective effect; a genuine causal protection would persist. Hence the reliable EPIC reading is essentially neutral for eggs.

## Step 6 verdict
**corrected / checked.** Reconstruction: premise = HR 0.93/20g attenuates to nonsignificance when the first 4 years are excluded; conclusion as stated = reverse causation drives the signal and the true effect is near-null. Hidden premise: attenuation under early-exclusion is uniquely explained by reverse causation. Undercutting defeaters that survive: (1) dropping 4 years of events cuts case count and therefore power, so loss of *significance* is expected even under a constant true HR — the point estimate's movement, not its p-value, is what would carry the argument, and 'attenuates to nonsignificance' conflates the two; (2) a single baseline FFQ becomes progressively less valid as exposure measurement over longer follow-up, biasing later-period estimates toward the null independently of reverse causation; (3) a genuine short-latency effect would also concentrate in early follow-up. Each of these breaks the reason-conclusion link without denying the premise. The weaker evidential conclusion — reverse causation contributes, and near-null is consistent with the data — is immune, so the statement is corrected to that.

## Original
The disappearance of the inverse egg-IHD association after excluding the first 4 years of follow-up indicates the weak protective signal is driven by reverse causation, leaving a near-null true effect.
