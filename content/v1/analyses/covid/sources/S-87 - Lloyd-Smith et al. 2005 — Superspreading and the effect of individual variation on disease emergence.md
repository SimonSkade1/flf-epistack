---
id: S-87
type: source
source_type: journal-article
url: https://doi.org/10.1038/nature04153
venue: Nature
publication_date: 2005-11-17
citation_count: 2590
citation_count_asof: 2026-07-23
field: theoretical epidemiology / disease ecology
authors: [James O. Lloyd-Smith, Sebastian J. Schreiber, P. Ekkehard Kopp, Wayne M. Getz]
found_via: keyword search "superspreading individual variation disease emergence" while surveying the base-rate/venue-amplification gap
motivatedness: none apparent; academic modelling paper, no stake in the COVID-origins debate
trust_score: 0.9
trust_reason: foundational compound-Poisson/negative-binomial superspreading framework fit to contact-tracing data from ~8-10 diseases; the k dispersion result has been re-derived and reproduced across hundreds of later studies — independent-corroboration signal is strong
usefulness: 2.5
usefulness_reason: the quantitative basis for "first visible cluster is where a rare superspreading event hit, not where spillover occurred" — underlies but does not itself address the Wuhan market-ascertainment argument
method_read: rigorous statistical model, multiple diseases, clearly supports its claim; a well-established general result
standing: Nature, 2,590 citations, foundational and heavily reused across outbreak epidemiology
angle: base-rate-precedent
data_basis: ["[[S-87]]"]
combined_score: 1.0
curated: true
curation_reason: "Curated: Lloyd-Smith superspreading, quantitative foundation of the base-rate/ascertainment argument (first-detected cluster set by chance superspreading, not origin); self-basis."
extracted: ["[[O-23 - Individual infectiousness is highly overdispersed across eight directly-transmitted diseases; SARS dispersion k approx 0.16]]", "[[A-41 - With overdispersed infectiousness, chance superspreader placement, not average R0 or spillover location, governs whether and where a pathogen first cluster appears]]"]
---
Fits a compound-Poisson transmission model (individual reproduction number drawn from a gamma distribution, dispersion parameter k) to contact-tracing data from 8 directly-transmitted human diseases (SARS-1, measles, smallpox, pneumonic plague, etc.), showing infectiousness is highly right-skewed: the great majority of cases transmit to few or no others while a small minority ("superspreaders") generate large, explosive clusters. Formalizes a rigorous statistical definition of a superspreading event (transmission exceeding the 99th percentile of a Poisson(R0) expectation) and shows individual-level heterogeneity, not average R0, governs whether/where an emerging pathogen's first visible cluster appears.

relevance_note: the foundational quantitative primary behind "venue-amplification" reasoning — a pathogen's first visible cluster size and location is driven by whichever contact network a rare superspreading event happens to hit, independent of where true spillover occurred; underlies (but does not itself address) the market-specific ascertainment-bias argument in this case.

## Extracted (structured summary)

### Empirical overdispersion
![[O-23 - Individual infectiousness is highly overdispersed across eight directly-transmitted diseases; SARS dispersion k approx 0.16]]

### Branching-process consequence
![[A-41 - With overdispersed infectiousness, chance superspreader placement, not average R0 or spillover location, governs whether and where a pathogen first cluster appears]]
