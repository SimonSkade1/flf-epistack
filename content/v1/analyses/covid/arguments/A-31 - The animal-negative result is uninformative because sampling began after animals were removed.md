---
type: argument
id: "A-31"
statement: "The 0/457 animal-negative result carries almost no evidential weight against animal infection, because animal sampling began on 18 January 2020, weeks after the 1 January market closure and removal of the live susceptible wildlife, so the population that could have been infected was no longer available to sample."
source: "[[S-16 - Liu, Gao et al. — Surveillance of SARS-CoV-2 at the Huanan Seafood Market (Nature)]]"
locator: "Methods, sampling timeline; Discussion"
affects_observations: ["[[O-17 - None of 457 animal-source samples from the Huanan market tested positive for SARS-CoV-2]]"]
affects_hypotheses: ["[[H-14 - The market environmental pattern reflects wildlife-associated emergence at the Huanan market]]"]
status: approved
reason_if_not_false: checked
---
Absence of evidence is evidence of absence only when the sampling could have detected the evidence had it been present. Here the live raccoon dogs, civets and other susceptible mammals that a wildlife-spillover scenario implicates had already been cleared out before any animal swab was taken; the 457 samples were unsold frozen carcasses, strays and fish-tank water. A negative result from a population that structurally excludes the relevant animals cannot lower the probability of animal infection at the market, so this observation should not be treated as counter-evidence to wildlife emergence.

## Validity assessment — approved (checked)

Reconstruction. P1: animal sampling began 18 Jan 2020. P2: the live susceptible mammals were removed at/before the 1 Jan market closure. P3: the 457 samples were non-target material (frozen carcasses, strays, fish-tank water). Load-bearing step: a negative result drawn from a population that structurally excludes the target animals cannot lower P(animal was infected) — i.e. this is exactly the case where "absence of evidence" is not "evidence of absence," because the detection precondition (sampling the relevant population when it could still test positive) fails.

Evaluation. Conditional on the premises the step is a correct application of the likelihood condition: for a negative to be evidence against animal infection you need P(negative | animals infected) < P(negative | animals not infected), which requires the sampling to have been able to catch an infected target animal. If the targets were gone, that inequality collapses toward equality and the update is ~null. Probed undercutting defeater: residual viral RNA on frozen product from the same supply chain could carry *some* weight even after live animals were cleared — but the statement claims only "almost no" weight, which already accommodates this residual channel, so the defeater does not break the link. How much weight the 0/457 actually deserves (vs. exactly zero) is a step-8 magnitude question; the inferential direction holds.
