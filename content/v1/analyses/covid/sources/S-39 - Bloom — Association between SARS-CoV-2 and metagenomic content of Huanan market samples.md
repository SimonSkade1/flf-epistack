---
id: S-39
type: source
source_type: journal-article
url: https://doi.org/10.1093/ve/vead050
venue: Virus Evolution
publication_date: 2023-08-24
citation_count: 12
citation_count_asof: 2026-07-23
field: computational virology
authors: [Jesse D. Bloom]
found_via: canonical anchor (brief, "Débarre and others' reanalyses")
motivatedness: Bloom has been a prominent public critic of strong claims drawn from the market environmental data (see also his role recovering deleted early Wuhan sequences arguing for missing early diversity — slice C); solo-authored, explicitly framed as a corrective to the Crits-Christoph preprint's correlational method.
trust_score: 0.78
trust_reason: "Fully reproducible Snakemake pipeline from raw reads to figures with robustness checks (Theil-Sen, date subsets) on the same public China-CDC data; the correlational read-out replicates deterministically, and disclosed biotech COIs do not affect a code-public re-analysis"
usefulness: 3.5
usefulness_reason: "Reframes the strongest zoonosis genetic evidence using the same data (viral reads track fish/human more than susceptible mammals; 1 of 14 high-raccoon-dog samples had any viral read); if true, dissolves the co-location-as-infection inference"
method_read: "Per-sample joint quantification of SARS-CoV-2 vs chordate-mitochondrial reads, Pearson on log-log with robustness checks; appropriately agnostic since a correlation on post-outbreak samples cannot prove presence or absence of animal infection"
standing: "Virus Evolution (peer-reviewed), 12 citations; public code makes it independently checkable, and it functions as the main re-analysis check on Crits-Christoph (S-31/S-35)"
angle: environmental-sampling
data_basis: ["[[D-1]]"]
combined_score: 0.98
curated: true
curation_reason: "Curated: Bloom market-metagenomic reanalysis, skeptical pole of the market dispute (viral/animal reads uncorrelated); best single Bloom source on D-1."
extracted:
  - "[[O-51 - Of 14 samples dominated by raccoon-dog mtDNA only one contained any SARS-CoV-2 read (1 of ~2.1x10^8); all six bamboo-rat-dominated samples had zero]]"
  - "[[O-50 - Across market samples SARS-CoV-2 abundance correlates most with fish and livestock mtDNA (bass, catfish, cow, carp, snakehead) and negatively with raccoon dog and bamboo rat]]"
  - "[[A-54 - SARS-CoV-2 tracking fish and livestock rather than raccoon dogs is the pattern expected from human deposition, undercutting the specific raccoon-dog-shedding claim]]"
  - "[[A-55 - Because the samples were collected a month into widespread human transmission, their viral-animal co-location is uninformative about the outbreak source in either direction]]"
---
Reanalysis of the same China CDC raw sequencing data (see [[S-21 - China CDC raw metagenomic sequencing data release — Huanan market samples (NGDC GSA - NCBI BioProject)]]) used by [[S-24 - Crits-Christoph et al. — Genetic evidence of susceptible wildlife in SARS-CoV-2-positive Huanan market samples (Zenodo report)]]. Quantifies per-sample mitochondrial-DNA read counts against SARS-CoV-2 read counts across species and finds the samples with the most SARS-CoV-2 material correlate at least as strongly with fish (catfish, largemouth bass) as with any mammal; of 14 samples with substantial raccoon-dog mtDNA, only 1 had any SARS-CoV-2 reads. Argues co-location of animal DNA and viral RNA at a market, sampled a month after human transmission was already widespread, cannot reliably indicate which animals (if any) were infected.
relevance_note: the central methodological counter to the raccoon-dog co-location claim; argues the correlational evidence is too weak/confounded to identify an infected intermediate host.

## Raccoon-dog-dominated samples and viral reads (Section 2.3)

![[O-51 - Of 14 samples dominated by raccoon-dog mtDNA only one contained any SARS-CoV-2 read (1 of ~2.1x10^8); all six bamboo-rat-dominated samples had zero]]

## Correlation of SARS-CoV-2 with species mtDNA (Section 2.4)

![[O-50 - Across market samples SARS-CoV-2 abundance correlates most with fish and livestock mtDNA (bass, catfish, cow, carp, snakehead) and negatively with raccoon dog and bamboo rat]]

![[A-54 - SARS-CoV-2 tracking fish and livestock rather than raccoon dogs is the pattern expected from human deposition, undercutting the specific raccoon-dog-shedding claim]]

## What co-location can and cannot show (Discussion)

![[A-55 - Because the samples were collected a month into widespread human transmission, their viral-animal co-location is uninformative about the outbreak source in either direction]]
