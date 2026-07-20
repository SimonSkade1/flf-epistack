---
type: source
id: S-2
source_type: journal-article
url: https://doi.org/10.1038/s41586-023-06043-2
venue: "Nature"
publication_date: 2023-04-05
citation_count: 78
citation_count_asof: 2026-07-20
field: "environmental virology / molecular epidemiology"
authors:
  - "William J. Liu"
  - "Peipei Liu"
  - "Wenwen Lei"
  - "Zhiyuan Jia"
  - "Xiaozhou He"
  - "Weifeng Shi"
  - "... (37 authors total, China CDC-led)"
  - "George F. Gao"
  - "Guizhen Wu"
found_via: "named anchor in orchestrator/search-plan brief (verify authors/venue/date); confirmed"
motivatedness: "China CDC-led (senior/corresponding authors George F. Gao, then-CDC Director-General, and Guizhen Wu); Chinese-government-affiliated authorship on a dataset whose broader release was itself a point of international friction. First circulated as a Research Square preprint in Feb 2022; the underlying raw metagenomic reads were not uploaded to GISAID until March 2023, 13 months later and only after international pressure (see this slice's Crits-Christoph/Débarre node, which reanalyzes those same reads). Treat the lag as a data-completeness/timing flag, not an assertion the reported findings are fabricated."
trust_score: 0.72
trust_reason: "Large systematic primary sampling (923 env + 457 animal swabs); raw reads independently reanalysed (S-3) and the reported positivity pattern held up — strong corroboration. Capped by the closure-then-sampling timing limit and 13-month release lag, not by any fabrication signal."
usefulness: 4.0
usefulness_reason: "Foundational multidimensional dataset (18 species, closure/sampling timeline, env-positivity map) that both zoonosis geolocation and the reanalysis build on."
method_read: "Descriptive surveillance measurement, low inferential load; animal-negative result is weak evidence given late/post-disinfection sampling."
standing: "Nature 2023, 78 cites; raw reads externally reanalysed."
angle: market-sampling
data_basis:
  - "[[D-2]]"
combined_score: 0.88
curated: true
curation_reason: "Rank 4 (0.88); foundational Huanan market environmental-swab dataset (D-2)."
extracted:
  - "[[O-1 - 74 of 923 Huanan environmental swabs SARS-CoV-2-positive, concentrated in the live-wildlife section]]"
  - "[[O-2 - No Huanan animal-origin sample (457 samples, 18 species) tested SARS-CoV-2-positive]]"
  - "[[O-3 - Huanan market closed and disinfected from 1 Jan 2020 with animal sampling only from 18 Jan]]"
  - "[[H-1 - SARS-CoV-2 first infected humans via zoonotic spillover at the Huanan market]]"
  - "[[A-1 - Post-disinfection late animal sampling means the animal-negative result cannot exclude infected animals]]"
---

**summary** - China CDC's own environmental and animal surveillance at the Huanan market: 923 environmental swabs collected from 1 January 2020 (the day the market was closed and disinfection began) and 457 samples from animal-origin material (unsold refrigerator/freezer stock, strays, a fish tank, covering 18 species) from 18 January 2020. No animal-origin sample tested SARS-CoV-2-positive, but 74 environmental swabs did (mostly concentrated in the section that sold live wildlife), including one yielding a lineage-A genome. This is also the primary documentary source for the market's closure-then-sampling timeline: closed and disinfection begun 1 Jan 2020, CDC swabbing starting the same day, animal-sample collection starting over two weeks later (18 Jan), after most live animals had already been removed.
Note for balance: because no animal tissue itself tested positive, the paper's own data cannot show an infected animal directly — the co-located-DNA argument for an infected intermediate host comes from the separate reanalysis of this same raw data (this slice's other market-swab node).

**relevance_note** - China's own primary market-surveillance dataset; establishes the closure/sampling timeline and the environmental-positivity pattern that both Worobey 2022's case-geolocation paper and the international reanalysis build on — flag as the shared data-basis for step 2 (same raw samples, independent interpretations).
