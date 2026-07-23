---
id: S-23
type: source
source_type: journal-article
url: https://doi.org/10.1093/jrsssa/qnad139
venue: "Journal of the Royal Statistical Society Series A: Statistics in Society"
publication_date: 2024-01-16
citation_count: 4
citation_count_asof: 2026-07-23
field: spatial statistics
authors: [Dietrich Stoyan, Sung Nok Chiu]
found_via: canonical anchor (step-01 search-plan for this slice); preprint predecessor arXiv:2208.10106 (2022)
motivatedness: professional spatial statisticians (TU Bergakademie Freiberg; Hong Kong Baptist University) with no apparent prior stake in the origins debate; framed as a pure methods critique
trust_score: 0.72
trust_reason: "sound spatial-statistics reasoning from established statisticians with no origins stake in a top venue (JRSS-A) — the Monte-Carlo null mismatch (rejecting a population-density null is not evidence of market origin) and the unjustified centroid-as-origin premise are genuine; discounted because the conclusion is directly contested by Débarre & Worobey's reply and the critique removes support rather than establishing an alternative"
usefulness: 3.5
usefulness_reason: "attacks the inferential core of the flagship market-epicenter geospatial paper; if it holds, a key zoonosis spatial pillar loses force"
method_read: "identifies a real null-hypothesis mismatch in Worobey's Monte Carlo test and an unjustified centroid=origin assumption; rigorous, but asserts no alternative origin"
standing: "JRSS-A (top statistics venue); authors are established spatial statisticians with low motivatedness; directly rebutted by Débarre & Worobey (S-26), so the conclusion is contested; 4 citations"
angle: case-geospatial
data_basis: ["[[D-2]]"]
combined_score: 0.77
curated: true
curation_reason: "Curated: Stoyan & Chiu geospatial critique (JRSS-A), highest-trust ascertainment/geospatial critique of the market-epicenter claim; rebuttal pole on D-2."
extracted:
  - "[[O-3 - The 155-case December-2019 dataset is incomplete and coarse (vs ~257 documented cases, no onset dates, shared addresses)]]"
  - "[[O-1 - Recomputed Monte Carlo p-values for the market as case center are marginal and weaken toward non-significance as the case sample shrinks]]"
  - "[[O-2 - Bootstrap places the market at the edge of the case-centroid cloud with Wanda Plaza an equally admissible center]]"
  - "[[A-1 - Rejecting a population-density (non-contagious) null cannot single out the market as the origin]]"
  - "[[A-2 - The geometric center of early cases is not a justified estimator of the epidemic origin (centrality does not imply causality)]]"
---
A formal statistical critique, by two spatial-statistics researchers, of the geospatial method in Worobey et al. 2022. Argues (a) that using the centroid of early-case locations (or a similarly simple constructed point) as a proxy for an epidemic's true point of origin is statistically unjustified — there is no theory establishing that correspondence — and (b) that the Monte Carlo procedure Worobey et al. used to conclude no other location could be the origin is methodologically flawed (wrong reference distribution/multiple-comparisons handling). Concludes the "market was the epicenter" claim does not follow from the geospatial data as analyzed, without asserting an alternative origin.

relevance_note: the canonical formal-statistics rebuttal of the market geospatial-clustering claim, targeting Worobey 2022's core inferential step directly.

## Data and limitations (Section 2)

![[O-3 - The 155-case December-2019 dataset is incomplete and coarse (vs ~257 documented cases, no onset dates, shared addresses)]]

## Results (Section 3)

![[O-1 - Recomputed Monte Carlo p-values for the market as case center are marginal and weaken toward non-significance as the case sample shrinks]]

![[O-2 - Bootstrap places the market at the edge of the case-centroid cloud with Wanda Plaza an equally admissible center]]

## Arguments (Sections 3-4)

![[A-1 - Rejecting a population-density (non-contagious) null cannot single out the market as the origin]]

![[A-2 - The geometric center of early cases is not a justified estimator of the epidemic origin (centrality does not imply causality)]]
