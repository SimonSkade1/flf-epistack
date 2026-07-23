---
id: S-17
type: source
source_type: journal-article
url: https://doi.org/10.1126/science.abp8715
venue: Science
publication_date: 2022-07-26
citation_count: 299
citation_count_asof: 2026-07-23
field: genomic epidemiology / spatial statistics
authors: [Michael Worobey, Joshua I. Levy, Lorena Malpica Serrano, Alexander Crits-Christoph, Jonathan E. Pekar, Stephen A. Goldstein, Angela L. Rasmussen, Moritz U.G. Kraemer, Chris Newman, Marion P.G. Koopmans, Marc A. Suchard, Joel O. Wertheim, Philippe Lemey, David L. Robertson, Robert F. Garry, Edward C. Holmes, Andrew Rambaut, Kristian G. Andersen]
found_via: canonical anchor (step-01 search-plan for this slice)
motivatedness: Worobey and Andersen (corresponding authors) are established zoonosis-hypothesis proponents (Andersen co-authored "Proximal Origin"); treat the paper's inferential framing with that in mind — this is exactly the paper Stoyan/Chiu and Weissman target with methods critiques
trust_score: 0.55
trust_reason: "Science, 299 citations, but the discriminating result rests on small lineage-confirmed subsets (n=2 and n=11), near-threshold p-values (0.034 / 0.017), an ascertainment-biased case set, and a null-model choice that drew a 2024 erratum and live statistical critiques (Stoyan-Chiu, Weissman) — the clustering is real but the specific inference is contested."
usefulness: 4.3
usefulness_reason: "The core geospatial epicenter analysis — if both lineages independently cluster near the market as claimed, strongly favors market-centered emergence; directly separates the leading hypotheses."
method_read: "Geolocated 155/164 Dec-2019 Wuhan-resident cases from WHO-report maps; tested Haversine distance-to-market against 1,000 population-density-weighted (WorldPop) random draws. Lineage B (n=11) median 8.30 km p=0.017; lineage A (n=2) 2.31 km p=0.034 — small n, near-threshold, resting on ascertainment-biased case locations; 2024 erratum (correction, not retraction) on the null generation."
standing: "Science; 299 citations; high-profile; methods directly critiqued in-pool by Stoyan & Chiu and Weissman; erratum issued Mar 2024; corresponding authors are named zoonosis proponents."
angle: case-geospatial
data_basis: ["[[D-2]]", "[[D-1]]"]
combined_score: 0.215
curated: true
curation_reason: "Curated via contested-question exception (combined 0.22, low trust 0.55): Worobey geospatial market-epicenter, the central pro-zoonosis geospatial evidence; low trust reflects ascertainment concerns and keeps discounting it downstream."
extracted: ["[[O-30 - December-2019 Wuhan cases were significantly closer to the Huanan market than a population-weighted null]]", "[[O-31 - Both lineage A and lineage B early cases cluster near the Huanan market]]", "[[A-43 - Both lineages independently centering on the market points to the market as the common emergence locus]]", "[[O-32 - Market-unlinked December cases lived even closer to the market than market-linked cases]]", "[[A-44 - Market-unlinked cases clustering on the market argues the signal is not mere market-link ascertainment]]", "[[O-33 - Positive market environmental samples concentrated at a single live-mammal vendor stall]]", "[[A-45 - Positive samples localizing to a live-mammal stall ties earliest contamination to the wildlife trade]]", "[[H-21 - The Huanan market was the early epicenter of the pandemic via the live-wildlife trade]]"]
---
Extracts latitude/longitude for 155 of 164 Wuhan-resident December-2019 cases from maps in the WHO mission report, then tests their spatial distribution against a population-density-weighted null (Haversine distance to market vs. 1,000 age/density-matched random draws from worldpop.org data). Finds lineage-B cases (n=11, median distance 8.30 km, p=0.017) and the two earliest-known lineage-A cases (2.31 km, p=0.034; and a case adjacent to a hotel within ~500 m of the market) are significantly closer to the Huanan market than chance predicts, for both viral lineages independently. Separately documents live SARS-CoV-2-susceptible mammals (raccoon dogs among them) sold at the market with environmental-sample positives concentrated in the same stalls, and concludes the market was the pandemic's early epicenter via the wildlife trade. Subject to a 2024 erratum (correction, not retraction).

relevance_note: the primary geospatial case-clustering analysis the "market epicenter" claim rests on; the direct target of the Stoyan/Chiu statistical critique and the Weissman ascertainment-bias critique in this same slice.

## Results — case geography
![[O-30 - December-2019 Wuhan cases were significantly closer to the Huanan market than a population-weighted null]]
![[O-31 - Both lineage A and lineage B early cases cluster near the Huanan market]]
![[A-43 - Both lineages independently centering on the market points to the market as the common emergence locus]]
![[O-32 - Market-unlinked December cases lived even closer to the market than market-linked cases]]
![[A-44 - Market-unlinked cases clustering on the market argues the signal is not mere market-link ascertainment]]

## Results — market environmental mapping
![[O-33 - Positive market environmental samples concentrated at a single live-mammal vendor stall]]
![[A-45 - Positive samples localizing to a live-mammal stall ties earliest contamination to the wildlife trade]]

## Discussion
![[H-21 - The Huanan market was the early epicenter of the pandemic via the live-wildlife trade]]
