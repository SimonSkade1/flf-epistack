---
id: S-61
type: source
source_type: journal-article
url: https://doi.org/10.1093/ve/veag015
venue: Virus Evolution
publication_date: 2026 (Virus Evol 12(1):veag015)
citation_count: unknown
citation_count_asof: 2026-07-23
field: molecular evolution / computational biology
authors: [Michael James Chambers, Mudabir Abdullah, Meru J. Sadhu]
found_via: keyword search ("furin cleavage site out-of-frame insertion ancestral sequence reconstruction")
motivatedness: none known
trust_score: 0.7
trust_reason: peer-reviewed (Virus Evolution 2026); two independent reconstruction methods (Treetime + IQ-TREE2 GTR+F+G+I) converge, 95% CI reported, R code/data on Zenodo, no COI; capped by single deep-event ASR being model/partition-dependent and no independent replication yet.
usefulness: 3.0
usefulness_reason: quantitative test of the named "out-of-frame insertion" argument; moderately discriminating, but the authors themselves note it does not preclude natural host-RNA templating.
method_read: ASR on 31 sarbecovirus genomes gives 97.1% (CI 94.2-99.3%) that the FCS insertion disrupted an ancestral serine codon; reproducible pipeline, but the CI is within-model and likely understates recombination-partition/model-choice uncertainty.
standing: Virus Evolution (peer-reviewed, IF ~5), 2026, citations unknown (recent); transparent with public code but not yet independently reproduced.
angle: genome-origin-argument
data_basis:
  - "[[D-5 - SARS-CoV-2 reference genome and closest natural relatives]]"
combined_score: 0.6
curated: false
curation_reason: "Not curated: Chambers insertion-codon-frame rebuttal, niche; genome-argument represented."
---
Uses ancestral-sequence reconstruction across sarbecoviruses to test whether the 12-nucleotide insertion producing SARS-CoV-2's furin cleavage site fell cleanly between codons (as template-switching recombination would tend to) or interrupted one. Finds ~97% probability the insertion disrupted a serine codon in the reconstructed ancestral sequence, which the authors argue sits more comfortably with certain insertion/mutational mechanisms than with a clean natural recombination breakpoint.
relevance_note: the primary quantitative test of the "out-of-frame insertion" argument named explicitly in this slice's brief.
