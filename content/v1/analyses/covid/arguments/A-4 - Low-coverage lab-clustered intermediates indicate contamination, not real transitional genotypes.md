---
type: argument
id: "A-4"
status: approved
reason_if_not_false: checked
statement: "Because genomes with about 10x or lower coverage at the diagnostic sites and lineage-specific shared rare mutations are the recognized signature of cross-contamination or bioinformatic error rather than true biological variants, the 20 apparent A/B intermediate genomes provide no evidence of a genuine within-human A-to-B transition."
source: "[[S-1 - Pekar et al. 2022 — molecular epidemiology of multiple zoonotic origins of SARS-CoV-2]]"
locator: "Results, intermediate-haplotype analysis"
affects_observations: ["[[O-5 - The 20 apparent A-B intermediate genomes are low-coverage and lab-clustered]]"]
affects_hypotheses: ["[[H-5 - Early A-B diversity reflects two or more separate zoonotic introductions, not one]]"]
---
General methodological principle: true low-frequency circulating variants are not expected to co-occur preferentially with lab-specific rare mutations nor to sit at positions with borderline read depth; contamination and assembly artifacts do exactly that. Since all 20 intermediate genomes exhibit at least one of these tells (>=10x-or-worse coverage at 8782/28144, same-lab shared rare mutations), they should be discounted as evidence for a circulating C/C or T/T intermediate. Removing them removes the principal genomic support for a single introduction whose descendants mutated into A and B within humans, so the two-mutation gap must instead be bridged across the human-population boundary — i.e. by separate introductions.

## Validity verdict

status: approved; reason_if_not_false: checked.

The statement's conclusion is the negative claim that these 20 genomes provide no evidence of a genuine within-human A-to-B intermediate. Reconstructed step: (premise) true low-frequency circulating variants are not expected to preferentially co-occur with lab-specific rare mutations or sit at borderline read depth, whereas contamination/assembly artifacts produce exactly that pattern; (premise) all 20 intermediates carry at least one such tell; (therefore) each of the 20 is better explained as artifact than as a real intermediate, so they do not support a circulating C/C or T/T genotype. Traced myself: conditional on the premise that these features are the recognized artifact signature and that all 20 exhibit one, an artifact explanation screens off the intermediate signal, so the collection provides no independent evidential support for a real transition. Probed the obvious defeater — a genuine variant that merely happens to be low-coverage — but the premise (co-occurrence with lab-specific shared mutations, not just low depth) is what defeats it, and it is granted here. The statement stops at "no evidence of a genuine within-human transition"; the further body leap to "therefore separate introductions" is not part of the claim being scored (and would have its own unsampled-intermediate defeater). As scoped, the inference holds.
