---
type: argument
id: "A-3"
status: corrected
reason_if_not_false: checked
statement: "Realistic epidemic simulations make the observed two-lineage / two-mutation basal topology unusual under a single introduction, so it is evidence for two or more introductions over one; but the originally reported ~0.1-0.5% frequency and Bayes factor of ~60 do not hold — a 2024 erratum corrected a code error, after which the Bayes factor is roughly an order of magnitude smaller and its direction is contested by independent reanalyses."
source: "[[S-1 - Pekar et al. 2022 — molecular epidemiology of multiple zoonotic origins of SARS-CoV-2]]"
locator: "Results, epidemic simulations and Bayes-factor calculation; Methods"
affects_observations: ["[[O-4 - Early SARS-CoV-2 split into two lineages A and B differing by two linked substitutions]]", "[[O-5 - The 20 apparent A-B intermediate genomes are low-coverage and lab-clustered]]"]
affects_hypotheses: ["[[H-5 - Early A-B diversity reflects two or more separate zoonotic introductions, not one]]"]
---
The inference: simulate SARS-CoV-2-like epidemics with FAVITES-COVID-Lite on a scale-free network of 5 million individuals using a customized SAPHIRE compartmental extension (doubling time 3.47 days, 95% HDI 1.35-5.44), generate coalescent trees, and simulate mutations along them. Under a single introduction, the most common outcome is one large basal polytomy (>=100 lineages), seen in 47.5% of runs; a topology matching the observed two-clade / two-mutation-gap structure arises in only 0.1% of runs when the ancestral haplotype is the intermediate C/C, and 0.5% when it is an ancestral lineage A or B haplotype with a large polytomy plus the two-mutation gap. Comparing the likelihood of the observed topology under one vs two introductions gives BF = 61.6 (recCA rooting) and 60.0 (unconstrained rooting).

Validity caveat (load-bearing for scoring): a 2024 erratum corrected a code error that had inflated the reported frequency of single-introduction topologies, so the corrected Bayes factor is much smaller (still nominally favoring two introductions but by roughly an order of magnitude less), and independent reanalyses (Weissman, McCowan) argue the intended/corrected model actually favors a single introduction. The argument's direction is therefore genuinely contested, and its strength is model- and ascertainment-dependent (simulations cover a pre-ascertainment period that could not be empirically validated).

## Original

Realistic epidemic simulations reproduce the observed pattern of two distinct early lineages separated by two mutations (each forming a basal polytomy) in only 0.1-0.5% of runs under a single introduction, yielding a Bayes factor of about 60 in favor of two or more introductions over one.

## Validity verdict

status: corrected; reason_if_not_false: checked.

The general inferential schema is valid and elementary: if the observed topology is much rarer under a single introduction than under multiple, its likelihood ratio is evidence for multiple introductions. What fails is the specific quantitative claim baked into the statement. This is not merely a "premise is false, step is sound" case that would leave it approved: the load-bearing computational step (the simulation frequencies feeding the Bayes factor) is the very thing a 2024 erratum corrected for a code error, shrinking the reported ~0.1-0.5% / BF~60 by roughly an order of magnitude, and independent reanalyses (Weissman, McCowan) argue the corrected model can point the other way. So the "BF ~60 favors two introductions" claim does not hold as stated; only the weaker "the two-lineage/two-mutation basal topology is unusual under a single introduction and thus is evidence for multiple introductions" survives, with magnitude (and possibly sign) unresolved — the classic "proves" → "is evidence for" downgrade. Corrected the statement accordingly; step 8 must price the actual, erratum-corrected and disputed magnitude.
