---
id: S-1
type: source
source_type: journal-article
url: https://www.science.org/doi/10.1126/science.abp8337
venue: Science
publication_date: 2022-07-26
citation_count: 187
citation_count_asof: 2026-07-23
field: molecular epidemiology / phylodynamics
authors: [Jonathan E. Pekar, Andrew Magee, Edyth Parker, Niema Moshiri, Katherine Izhikevich, Jennifer L. Havens, Karthik Gangavarapu, Lorena Mariana Malpica Serrano, Alexander Crits-Christoph, Nathaniel L. Matteson, Mark Zeller, Joshua I. Levy, Jade C. Wang, Scott Hughes, Jungmin Lee, Heedo Park, Man-Seong Park, Katherine Zi Yan Ching, Raymond Tzer Pin Lin, Mohd Noor Mat Isa, Yusuf Muhammad Noor, Tetyana I. Vasylyeva, Robert F. Garry, Edward C. Holmes, Andrew Rambaut, Marc A. Suchard, Kristian G. Andersen, Michael Worobey, Joel O. Wertheim]
found_via: search-plan canonical anchor
motivatedness: several co-authors (Andersen, Holmes, Rambaut, Worobey) are also authors of "The Proximal Origin of SARS-CoV-2" and other zoonosis-supporting work, and have documented private communications (later FOIA'd) minimizing the lab-leak hypothesis early in the pandemic — a standing pro-zoonosis lean to weigh.
refuted: 
duplicate_of: 
trust_score: 0.6
trust_reason: Science with public code/data, but the load-bearing Bayes factor was cut ~1 order of magnitude by a 2023 erratum (code error) and independent reanalysis (Weissman) argues the intended model favors one introduction — the headline effect size did not hold up robustly
usefulness: 4.5
usefulness_reason: 787-genome plus large-simulation reconstruction; if the two-introduction result is true it strongly disfavors a single lab introduction — the central discriminating genomic argument
method_read: BEAST phylodynamics plus FAVITES epidemic simulation with rejection sampling; heavily model- and ascertainment-dependent, and one code fix materially moved the headline Bayes factor
standing: Science, 187 cites; carries a 2023 erratum and an active reanalysis dispute (Massey, Weissman, McCowan); the two-introduction count is not independently corroborated
angle: phylodynamics
data_basis: ["[[D-3]]"]
combined_score: 0.45
curated: true
curation_reason: "Curated (below rank-cut, contested-central): Pekar two-introduction phylodynamics, flagship pro-zoonosis molecular-dating inference and primary D-3 (GISAID) representative; one pole of the phylo dispute."
extracted: ["[[O-4 - Early SARS-CoV-2 split into two lineages A and B differing by two linked substitutions]]", "[[O-5 - The 20 apparent A-B intermediate genomes are low-coverage and lab-clustered]]", "[[H-6 - The A-B intermediate haplotypes did not genuinely circulate in humans]]", "[[A-4 - Low-coverage lab-clustered intermediates indicate contamination, not real transitional genotypes]]", "[[O-6 - Molecular-clock dating places tMRCA in mid-December 2019 and lineage B primary infection around 18 Nov 2019]]", "[[A-3 - Single introduction almost never reproduces the two-lineage two-mutation topology, favoring two or more introductions]]", "[[H-7 - No substantial cryptic human circulation of SARS-CoV-2 before December 2019]]", "[[H-5 - Early A-B diversity reflects two or more separate zoonotic introductions, not one]]", "[[A-5 - Both lineages spread without within-human adaptation, implying a pre-adapted animal reservoir]]"]
---
The canonical two-introduction paper. Reconstructs the phylogenetic network of the ~2 early SARS-CoV-2 lineages (A and B, differing at two linked positions) from genomes collected before March 2020, then uses coalescent-based epidemic simulations to ask how often a single introduction would be expected to generate the observed topology plus case-count/diversity pattern versus two independent introductions. Concludes lineage B likely entered humans around 18 Nov 2019 (23 Oct–8 Dec range) with lineage A's introduction following within weeks, favoring (Bayes factor) at least two zoonotic spillovers over one. A 2024 erratum corrected a code error in the Bayes-factor calculation (it had overestimated support for multiple introductions); the corrected number still nominally favors two introductions but is much smaller, and this correction itself became the anchor for several later critiques (Weissman, McCowan) arguing the true corrected number favors one introduction.

relevance_note: the load-bearing quantitative case that the phylogenetic/genomic record alone supports (at least) two independent zoonotic spillovers rather than one lab-associated introduction.

## Results — early genomic structure
![[O-4 - Early SARS-CoV-2 split into two lineages A and B differing by two linked substitutions]]
![[O-5 - The 20 apparent A-B intermediate genomes are low-coverage and lab-clustered]]
![[H-6 - The A-B intermediate haplotypes did not genuinely circulate in humans]]
![[A-4 - Low-coverage lab-clustered intermediates indicate contamination, not real transitional genotypes]]

## Results — molecular dating
![[O-6 - Molecular-clock dating places tMRCA in mid-December 2019 and lineage B primary infection around 18 Nov 2019]]

## Results — epidemic simulations
![[A-3 - Single introduction almost never reproduces the two-lineage two-mutation topology, favoring two or more introductions]]
![[H-7 - No substantial cryptic human circulation of SARS-CoV-2 before December 2019]]

## Discussion
![[H-5 - Early A-B diversity reflects two or more separate zoonotic introductions, not one]]
![[A-5 - Both lineages spread without within-human adaptation, implying a pre-adapted animal reservoir]]
