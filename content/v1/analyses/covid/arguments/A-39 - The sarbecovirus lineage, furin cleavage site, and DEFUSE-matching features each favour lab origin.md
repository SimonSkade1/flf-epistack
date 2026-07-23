---
id: A-39
type: argument
statement: "The choice of a sarbecovirus, the presence of an unusual furin cleavage site, and sequence features matching the 2018 DEFUSE proposal each independently raise the likelihood of a research-related origin over zoonosis."
source: "[[S-64 - Weissman's 'An Inconvenient Probability' Bayesian analysis]]"
locator: "Lineage / furin-cleavage-site / DEFUSE factor sections (Substack, v5.x)"
affects_observations: []
affects_hypotheses: ["[[H-43 - Research-related origin of a laboratory-manipulated virus (engineered lab leak)]]"]
status: approved
reason_if_not_false: checked
---
## Reasoning
Three virus-feature factors each condition on the specific pre-2020 research plan. (a) Sarbecovirus type: only about one of ~19 recent emerging pathogens in China was a sarbecovirus, whereas the DEFUSE/WIV program pre-specified exactly this virus category, giving L1 ~= 2.3 in favour of lab origin. (b) Furin cleavage site: SARS-CoV-2's FCS is rare or absent among natural sarbecoviruses, and its nucleotide-level features resemble patterns used in engineered constructs, matching the FCS-insertion plan written into the DEFUSE proposal - contributing roughly 2-3 logits, though with wide uncertainty. (c) Restriction-enzyme pattern: the genome's restriction-site spacing matches patterns in DEFUSE drafts and is uncommon in natural viruses, contributing roughly 1-2 logits, also uncertain. Because each is estimated conditional on the same DEFUSE plan, their uncertainties are large and they are discounted toward 1 in the combination (per the combination argument), but their central estimates all point the same way, reinforcing H-17.

## Validity
Reconstruction. Premises (assumed): (a) sarbecoviruses are ~1/19 of recent emerging pathogens in China, while the DEFUSE/WIV program pre-specified this category; (b) the FCS is rare/absent among natural sarbecoviruses and its nucleotide features resemble engineered constructs, matching DEFUSE's FCS-insertion plan; (c) the restriction-site spacing matches DEFUSE drafts and is uncommon in natural genomes. Load-bearing step: for each feature, P(feature | research plan) > P(feature | zoonosis), so each is a separate likelihood factor favouring lab.

Checked. Conditional on each stated premise, the direction is a valid likelihood inference — a feature that is common under the pre-specified research plan but rare in the natural comparison class carries LR > 1 for lab origin. The word "independently" in the statement is read charitably as "each on its own points toward lab" (not statistical independence); the body itself notes the three share DEFUSE-conditioning and are discounted toward 1 in combination, so no double-counting is asserted here — that guard lives in A-36. Probed defeaters (the RE-site pattern is not actually statistically anomalous once natural genomes are surveyed; the FCS's "engineering-like" character is disputed) attack the *truth* of premises (b)/(c), not the inferential step, and are priced at step 8. No premise-preserving defeater breaks the direction of any of the three factors. Approved.
