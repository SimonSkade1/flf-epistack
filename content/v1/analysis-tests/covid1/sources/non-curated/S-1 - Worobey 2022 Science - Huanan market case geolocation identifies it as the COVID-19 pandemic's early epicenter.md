---
type: source
id: S-1
source_type: journal-article
url: https://doi.org/10.1126/science.abp8715
venue: "Science"
publication_date: 2022-07-26
citation_count: 297
citation_count_asof: 2026-07-20
field: "epidemiology (spatial / phylogeographic)"
authors:
  - "Michael Worobey"
  - "Joshua I. Levy"
  - "Lorena Malpica Serrano"
  - "Alexander Crits-Christoph"
  - "Jonathan E. Pekar"
  - "Stephen A. Goldstein"
  - "Angela L. Rasmussen"
  - "Moritz U. G. Kraemer"
  - "Chris Newman"
  - "Marion P. G. Koopmans"
  - "Marc A. Suchard"
  - "Joel O. Wertheim"
  - "Philippe Lemey"
  - "David L. Robertson"
  - "Robert F. Garry"
  - "Edward C. Holmes"
  - "Andrew Rambaut"
  - "Kristian G. Andersen"
found_via: "named anchor in orchestrator/search-plan brief; confirmed by direct search"
motivatedness: "Several co-authors (Worobey, Andersen, Holmes, Rambaut, Garry) also co-authored the 2020 'Proximal Origin' commentary and have been publicly vocal zoonosis proponents in the wider debate this run is seeded from (including the ACX/Rootclaim exchange). No industry ties apparent. Science issued a 2024 erratum (doi.org/10.1126/science.adp1133) correcting a distance-calculation error in the case-location data; the authors say it does not change the conclusion, but it is a real acknowledged error in the underlying analysis."
trust_score: 0.58
trust_reason: "Peer-reviewed Science, heavily scrutinised, but underlying case-location data is indirectly assembled (ascertainment-bias risk per S-5), the centroid-as-origin/Monte-Carlo method is contested (S-7), and a 2024 erratum corrected a distance error in the data."
usefulness: 4.0
usefulness_reason: "Load-bearing, multidimensional (cases + environmental swabs + spatial), directly discriminates market-epicenter if true."
method_read: "Spatial clustering signal on swabs is robust; case-clustering inference depends on how cases were ascertained and on a disputed null."
standing: "Science 2022, 297 cites; central zoonosis-side paper, but method openly challenged (Stoyan & Chiu) and an erratum issued."
angle: geolocation
data_basis:
  - "[[D-3]]"
  - "[[D-2]]"
combined_score: 0.32
curated: false
curation_reason: "Cleared baseline (0.32) but below top-5 cut."
---

**summary** - Case-geolocation analysis of the Huanan market's role in the pandemic's start. Assembled case-location data for the ~155 Dec-2019 COVID-19 cases lacking a known epidemiological link to each other (combining the original WHO-mission data with additional geolocations obtained via other channels, since Chinese authorities did not release a full raw line list — see this slice's other nodes on data access), plus the market's own SARS-CoV-2-positive environmental swab locations. Finds both the human cases and the positive swabs are spatially centered on, and significantly closer to, the Huanan market than chance would predict, with the highest swab-positivity concentrated in the section selling live mammals. Concludes the market was the pandemic's "early epicenter" while explicitly stating there is "insufficient evidence to define upstream events" (i.e., it does not itself identify an infected animal or a supply chain).

**relevance_note** - The single most-cited primary case-geolocation analysis anchoring the market-centric zoonosis case; its compiled case-location dataset is itself reused across the later literature (flag for step 2's data-basis linking) rather than being independently re-derived each time.
