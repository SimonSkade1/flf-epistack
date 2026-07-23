---
id: S-58
type: source
source_type: journal-article
url: https://doi.org/10.1016/j.cell.2020.08.012
venue: Cell
publication_date: 2020-09-03 (Cell 182(5):1295-1310.e20)
citation_count: 27
citation_count_asof: 2026-07-23
field: structural biology / deep mutational scanning
authors: [Tyler N. Starr, Allison J. Greaney, Sarah K. Hilton, Daniel Ellis, Katharine H.D. Crawford, Adam S. Dingens, "et al.", Jesse D. Bloom]
found_via: keyword search ("RBD ACE2 binding deep mutational scanning")
motivatedness: none known
trust_score: 0.9
trust_reason: Landmark yeast-display DMS covering ~all ~3,800 single RBD mutants in duplicate libraries, quantitative ACE2-affinity + expression readouts, fully open data/code, now a field-standard reference dataset.
usefulness: 3
usefulness_reason: Direct experimental test that WT RBD is not an optimized ACE2 binder — discriminates against a "rationally designed" story (though not serial passage).
method_read: Complete single-mutant scan, replicate libraries, internally validated affinity measurements; very low room for bias.
standing: Cell; heavily reused (Addgene library, public GitHub) and independently built upon across the field.
angle: wet-lab-experiment
data_basis: ["[[S-58]]"]
combined_score: 1.2
curated: false
curation_reason: "Not curated (rank-departure, combined 1.20): Starr RBD deep-mutational-scanning; the RBD-optimization argument is carried by S-46; peripheral to origin."
---
Uses yeast-display deep mutational scanning to measure the effect of essentially every possible single amino-acid substitution in the SARS-CoV-2 RBD on folding/expression and on ACE2-binding affinity. Finds the wild-type RBD sits well below the measured fitness ceiling — many single mutations further increase ACE2 affinity — i.e. SARS-CoV-2's RBD is not a computationally optimized binder, an independent experimental test of a "rationally designed for human ACE2" story (though it does not address non-computational routes such as serial passage/directed evolution).
relevance_note: the direct experimental test of Andersen et al.'s "RBD is not predicted optimal" claim, run independently of any origin-debate framing.
