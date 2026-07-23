---
id: S-21
type: source
source_type: dataset
url: https://www.ncbi.nlm.nih.gov/bioproject/PRJNA948658
venue: NCBI BioProject (mirrored on China National GeneBank NGDC's Genome Sequence Archive, accession CRA010170; also partially on GISAID)
publication_date: 2023-03-25
citation_count: unknown
citation_count_asof: 2026-07-23
field: genomics data repository
authors: [Chinese Center for Disease Control and Prevention]
found_via: cited as the data source in [[S-16 - Liu, Gao et al. — Surveillance of SARS-CoV-2 at the Huanan Seafood Market (Nature)]] and in the Crits-Christoph/Bloom/Débarre reanalyses
motivatedness: released by China CDC itself, over a year after the associated paper's submission and only after the data appeared (apparently inadvertently) on GISAID in Jan/Feb 2023 and was flagged by outside scientists — release was not voluntary/proactive on its original timeline.
trust_score: 0.82
trust_reason: "raw metagenomic reads independently re-analysed by adversarial groups (Bloom, Crits-Christoph, Débarre) with no fabrication claim, so read content is high-fidelity; capped because sample selection, stall attribution and completeness of the release were controlled and delayed by China CDC and are not independently verifiable"
usefulness: 4.5
usefulness_reason: "the single largest evidentiary object in the market debate (184 experiments, 176 samples, 4.6 Tbases) and the substrate every wildlife/viral co-location reanalysis in the pool depends on"
method_read: "large, verifiable, internally-consistent raw read set; read fidelity high but sampling and curation are submitter-controlled and post-closure"
standing: "national-agency dataset mirrored on NCBI/NGDC (CRA010170); re-analysed by multiple independent, partly hostile groups — strong corroboration of data content, none over sample selection"
angle: environmental-sampling
data_basis: ["[[D-1]]"]
combined_score: 1.44
curated: false
curation_reason: "Not curated (rank-departure, combined 1.44): raw-data release underlying D-1 with no analysis of its own; extraction covered by S-16 plus reanalyses S-35/S-39."
---
The raw metagenomic sequencing reads (184 SRA experiments, 176 BioSamples, ~4.6 Tbases) underlying [[S-16 - Liu, Gao et al. — Surveillance of SARS-CoV-2 at the Huanan Seafood Market (Nature)]] / [[S-15 - China CDC Research Square preprint — Huanan market environmental & animal surveillance]], submitted to NCBI 2023-03-25 (mirrored on China's NGDC GSA under CRA010170). This is the actual sequence-read data every metagenomic reanalysis in this slice (Crits-Christoph, Bloom, Débarre) operates on — none of these reanalyses used data outside what's in this release. The data's path to release is itself contested: an earlier partial version appeared on GISAID in Jun 2022 without being announced, was noticed by outside researchers in Jan/Feb 2023, prompting the fuller NCBI/NGDC release seen here.
relevance_note: the primary data substrate for essentially every other node in this slice — without this release none of the raccoon-dog/wildlife-DNA reanalyses would exist.
