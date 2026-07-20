---
type: source
id: S-5
source_type: journal-article
url: https://doi.org/10.1093/molbev/msab246
venue: "Molecular Biology and Evolution"
publication_date: 2021-12
citation_count: 34
citation_count_asof: 2026-07-20
field: "computational virology / bioinformatics"
authors:
  - "Jesse D. Bloom"
found_via: "named anchor in orchestrator/search-plan brief (verify exact venue; confirmed MBE, first posted as bioRxiv preprint June 2021); confirmed by direct search"
motivatedness: "Bloom (Fred Hutchinson Cancer Center, HHMI-funded academic virologist) has been publicly vocal that the market-centric case narrative is not conclusively established and has argued the lab-leak hypothesis deserves serious consideration; no industry ties; not affiliated with either institution implicated in the lab-leak hypothesis (WIV/EcoHealth)."
trust_score: 0.68
trust_reason: "The data-recovery step is transparent and reproducible (files pulled from Google Cloud, method fully described); the factual sequence findings are solid. Capped because the ascertainment-bias inference is contested by a 2025 reexamination arguing the collection dates undercut the undersampling claim."
usefulness: 3.5
usefulness_reason: "Attacks a key confounder (was the market-clustering pattern an ascertainment artefact?); moderately surprising and bears directly on the load-bearing early-case timeline."
method_read: "Reconstruction reproducible; the mutation-frequency comparison is real but the sample is small (45 partial genomes) and the interpretive step is disputed."
standing: "MBE 2021, 34 cites; single well-regarded author; drew a 2025 reexamination pushing back."
angle: sequence-recovery
data_basis:
  - "[[S-5]]"
combined_score: 0.63
curated: false
curation_reason: "Cleared baseline (0.63) but below top-5 cut."
---

**summary** - A Wuhan University team had deposited, then in June 2020 requested deletion of, 241 sequencing runs (project PRJNA612766) from NCBI's Sequence Read Archive; NCBI deleted rather than merely hid the files. Bloom recovered the deleted files from Google Cloud storage (by reconstructing archived download URLs) and reconstructed partial genomes for 45 early-epidemic samples collected in Wuhan in January 2020. These recovered sequences carried the C29095T mutation and were less likely to carry the T8782C/C28144T mutation pair (which defines the market-linked "lineage B") than the sequences reported in the WHO-China joint report — i.e., they were genetically closer to bat-coronavirus relatives than the heavily-studied market-associated samples. Bloom argues this shows the published/market-associated sequence set does not capture the full viral diversity that was already circulating in Wuhan in January 2020, i.e. an ascertainment bias toward market-associated viruses in what got sequenced, sampled, and reported.

**relevance_note** - The core ascertainment-bias critique of the market-centric case/sequence timeline that both Worobey 2022 and the WHO report rely on: argues the "earliest known cases/sequences cluster at the market" pattern may partly reflect what got reported and retained, not the true index-case pattern. A 2025 bioRxiv/MBE reexamination (not separately noded, since it reanalyzes these same recovered sequences) pushes back, arguing the recovered sequences' collection date (30 January 2020) was actually later than hundreds of other published sequences and that Wuhan-exposure history was common across early samples generally, so the single family cluster Bloom highlights doesn't establish broader undersampling.
