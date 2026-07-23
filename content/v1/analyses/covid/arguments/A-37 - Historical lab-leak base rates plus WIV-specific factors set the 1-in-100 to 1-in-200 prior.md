---
id: A-37
type: argument
statement: "Pre-COVID lab-accident base rates combined with WIV-specific risk factors and the roughly 50% chance DEFUSE-type work was active justify a prior of about 1/100 to 1/200 for a research-related 2019 origin."
source: "[[S-64 - Weissman's 'An Inconvenient Probability' Bayesian analysis]]"
locator: "Prior / base-rate section (Substack, v5.x)"
affects_observations: []
affects_hypotheses: ["[[H-18 - The prior probability of a research-related pandemic origin in 2019 is on the order of 1 in 100 to 1 in 200]]","[[H-43 - Research-related origin of a laboratory-manipulated virus (engineered lab leak)]]"]
status: approved
reason_if_not_false: checked
---
## Reasoning
Literature estimates put the probability of a major human-transmissible leak at roughly 0.2-1% per year per relevant BSL-3 laboratory. WIV-specific factors raise concern: SARS-related coronavirus work was conducted partly at BSL-2 (inadequate for gain-of-function on such viruses), and State-Department cables had warned of safety deficiencies. Conditional on DEFUSE-type work actually proceeding, Weissman puts P0if(2019,LL) ~= 1/100. Multiplying by an estimated ~50% probability that the work actually occurred (DEFUSE was formally rejected by DARPA, but subsequent Chinese-Academy funding and Shi Zhengli's non-denial keep the probability substantial) gives P0(2019,LL) ~= 1/200, i.e. starting prior odds around 1/70 favouring zoonosis. He flags these as 'obviously very rough', possibly off by a factor of ~10. This base-rate estimate is the L0 term feeding the combination in H-17.

## Validity
Reconstruction. Premises: per-lab-per-year leak base rate ≈ 0.2–1%; WIV concentrated the relevant SARSr-CoV work (partly at BSL-2, with warned safety deficiencies); conditional on DEFUSE-type work proceeding, P0if(2019,LL) ≈ 1/100; and ≈50% probability the work actually occurred. Load-bearing step: a law-of-total-probability composition, P0(2019,LL) ≈ P(LL | work)·P(work) ≈ (1/100)·(1/2) ≈ 1/200, giving a prior in the 1/100–1/200 band.

Checked. The arithmetic is elementary and correct (1/100 × 0.5 = 1/200; the 1/100–1/200 range spans the work-conditional and work-marginal figures). The composition is a valid total-probability step and is if anything conservative, since it drops the (small) no-DEFUSE leak path rather than inflating the estimate. No completion-by-force: the inputs are granted premises, and no undercutting defeater breaks the link from these inputs to an order-1/100–1/200 prior. Whether the base rate and the 50% figure are *true* is a premise-truth matter priced at step 7 (and Weissman himself flags them "obviously very rough," possibly off by ~10×); that does not touch the validity of the inference. Approved.
