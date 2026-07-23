# Orientation — early human-case epidemiology & geospatial clustering (searcher B)

Slice: who the earliest human cases were, where they lived/were exposed, and whether that pattern is best read as centering on the Huanan market. 11 `source` nodes written (budget: 11), ~20 sources read closely, more skimmed via citation-chasing on Google/Semantic Scholar.

## Sources by topic (best-first within each group)

**Clinical case series & the official line list**
1. [[S-13 - Li et al. 2020 NEJM — early transmission dynamics, first 425 confirmed cases]] — the largest early cohort (425 cases) and the source of the "55% vs 8.6%" market-linkage-over-time statistic.
2. [[S-9 - Huang et al. 2020 Lancet — clinical features of the first 41 hospitalized 2019-nCoV patients]] — the founding case series; also the origin of the "first case had no market link" puzzle.
3. [[S-10 - Chen et al. 2020 Lancet — 99-case single-hospital descriptive series]] — an independent single-hospital cohort giving a different (49%) market-linkage fraction, useful for bounding cohort-selection sensitivity.

**Geospatial case-clustering & the market-epicenter claim**
4. [[S-17 - Worobey et al. 2022 Science — geolocated case map naming the Huanan market the early epicenter]] — the central geospatial analysis; both viral lineages' cases fall closer to the market than a population-density-weighted null predicts.
5. [[S-18 - WHO-China joint study (2021) — early-case epidemiology and residential-location maps]] — the international team's own compilation and first maps of the case-location data Worobey 2022 later re-extracted and re-analyzed.

**The "first case" / earliest-onset dispute**
6. [[S-14 - Worobey 2021 Science — dissecting the early COVID-19 cases in Wuhan (the first-case correction)]] — corrects the presumed-first case's onset date (1 Dec → 16 Dec 2019) and identifies the market vendor (onset 11 Dec) as the actual earliest known case.

**Ascertainment-/surveillance-bias critiques of the market-clustering inference (and their rebuttals)**
7. [[S-23 - Stoyan & Chiu 2024 JRSS-A — statistical critique of the market-epicenter geospatial claim]] — the most credible (peer-reviewed, disinterested professional spatial-statisticians) methods critique of Worobey 2022's inference.
8. [[S-26 - Débarre & Worobey 2024 — reply to Stoyan & Chiu, reaffirming market centrality]] — the original authors' direct rebuttal.
9. [[S-30 - Weissman 2024 JRSS-A letter — proximity ascertainment bias in early case locations]] — a second, independent formal ascertainment-bias argument (though by an author who separately produced a lab-leak-leaning Bayesian analysis for this same case's debate record — flag for motivatedness).
10. [[S-32 - Débarre & Worobey 2024 — reply to Weissman, against systematic ascertainment bias]] — the direct rebuttal to #9.
11. [[S-36 - Zhang, Demaneuf et al. 2022 — within-market spatial critique, superspreader-not-spillover reading]] — a non-peer-reviewed, more overtly lab-leak-advocacy critique operating at finer (within-market) spatial grain than Stoyan/Chiu's city-scale analysis; lowest trust of this group but covers a angle (stall-level correlation) the peer-reviewed critiques don't.

## search_scope

WebSearch queries on: each canonical anchor by author+year+title fragment ("Worobey 2022 Science Huanan market", "Worobey 2021 Dissecting the early COVID-19 cases", "Huang et al 2020 Lancet clinical features", "Li et al 2020 NEJM 425 cases", "Stoyan Chiu Huanan market JRSS", "WHO-China joint mission report early case epidemiology annex", "Chen Wei / market vendor first case dispute", "ascertainment bias Huanan market"). Forward-citation-chased from Worobey 2022 and from Stoyan & Chiu (2024) to find the Débarre/Worobey and Weissman reply/counter-reply chain on arXiv. Metadata (citation counts, venues, DOIs, author lists) pulled via the Semantic Scholar Graph API (`api.semanticscholar.org/graph/v1/paper/...`, by DOI/arXiv id and by search) and cross-checked against arXiv abstract pages and journal pages; link resolution verified with `curl -IL`. Did not use Connected Papers/Research Rabbit (not needed given the citation-chase already converged on a small, tightly interlinked cluster).

## exclusions

1. **Erratum for Worobey 2022** (Science, DOI 10.1126/science.adp1133, 2024) — a correction notice, not an independent measurement; folded as a one-line mention into S-17's body rather than given its own node.
2. **Report of the WHO-China Joint Mission on Coronavirus Disease 2019** (the earlier, Feb 2020 report, distinct from the March 2021 "China Part" study I did mint as S-18) — read but not separately minted: its early-case content is superseded/recompiled by the 2021 report's dedicated epidemiology annex and case-location maps, which is what the geospatial analyses actually cite; minting both would have been a near-duplicate node for this slice's purposes.
3. **arXiv:2208.10106** (Stoyan & Chiu's own 2022 preprint) — not separately minted; fully superseded by its own 2024 JRSS-published version, S-23.
4. **Cohen, *Science* news, "Wuhan seafood market may not be source of novel virus spreading globally"** (Jan 2020) — excluded as secondary journalism reporting on Huang et al.'s own data (a discovery hub, not a primary measurement), despite being a notable early historical marker that market-linkage was already in doubt within weeks of the outbreak.
5. Market environmental/metagenomic swab papers, phylogenetic/dating papers, genome-structure/FCS papers, institutional/DEFUSE-adjacent documents, and wildlife-trade/host/serosurvey papers were all read where encountered via shared hubs but left unminted — out of this slice's scope by the disjointness rules (slices A, C, D, E, F respectively).

## Gaps / notes for step 2+

1. Every geospatial analysis in this literature (Worobey 2022, Stoyan & Chiu, Débarre & Worobey ×2, Weissman) ultimately re-uses the *same* underlying ~155–164-case location dataset, itself extracted from the WHO mission report's published maps (S-18) — i.e. this whole cluster shares one data basis and is not five independent lines of evidence, however many papers argue about it. Worth a single shared `data-basis` node in step 2 so correlation is handled correctly.
2. Couldn't get Semantic Scholar citation counts for S-32 and S-36 (persistent API rate-limiting mid-session, and S-36 isn't peer-reviewed/well-indexed); both recorded as `citation_count: unknown` per spec, worth a re-check if time permits.
3. The brief's phrase "the Chen Wei Dec-1 case" doesn't cleanly match a named individual in the primary literature I found: the original Dec-1(→corrected Dec-16)-onset non-market case is an unnamed accountant in Worobey 2021's own text; media coverage names the market vendor (the *earlier*-onset, market-linked case per Worobey's correction) as Wei Guixian. Flagging in case "Chen Wei" refers to a source I missed rather than a naming mix-up in the brief.
4. Did not find an independent (non-Worobey-lineage) geospatial re-analysis using a genuinely separate case-location dataset — everything traces back to the single WHO-report map extraction in point 1. If one exists (e.g. from a Chinese-language source not indexed by the tools used here), it would be a valuable addition step 2 should watch for.
