# Orientation — SARS-CoV-2 phylogenetic & molecular-dating data base (searcher C)

Slice: inference from the early genome collection about how many times the virus entered humans, the tree topology, and when. Owns: lineage A/B two-introduction analyses, molecular-clock/tMRCA/index-case timing, recombination and phylodynamic simulations, the "which lineage came first" dispute, and the deleted-early-Wuhan-sequences / progenitor-genotype work. Does NOT own genome-structure/FCS/engineering-signal papers (slice D), market environmental samples (A), human-case epidemiology (B), institutional documents (E), or wildlife/host/serosurvey (F) — those are read as shared hubs only, never minted here.

## Sources by topic (best-first within each group)

**The two-introduction inference itself**
1. [[S-1 - Pekar et al. 2022 — molecular epidemiology of multiple zoonotic origins of SARS-CoV-2]] — the canonical result: lineage A/B topology + epidemic simulation → Bayes factor for ≥2 spillovers (corrected downward by a 2024 erratum).
2. [[S-2 - Pekar et al. 2021 — Timing the SARS-CoV-2 index case in Hubei province]] — companion timing analysis (mid-Oct–mid-Nov 2019 successful-transmission start).

**Critiques of the two-introduction Bayes factor (methodological)**
3. [[S-22 - Weissman 2026 — a fundamental Bayesian error in the multiple-introductions claim]] — most detailed rebuttal; argues corrected math favors one introduction.
4. [[S-12 - McCowan 2025 — imbalanced hypothesis-testing framework in the multiple-introductions claim]] — independent, convergent methodological critique (asymmetric test conditions).

**The excluded "intermediate" A-B genomes dispute**
5. [[S-7 - Massey et al. 2023 — Unwarranted exclusion of intermediate lineage A-B genomes]] — argues Pekar et al.'s exclusion of 20 candidate intermediate genomes was post hoc.
6. [[S-8 - Pekar et al. 2025 — reported intermediate lineage A-B genomes are instead derived]] — the zoonosis side's answer: these genomes are derived, not intermediate. Currently the end of this back-and-forth in the published record.

**Deleted-sequences / progenitor-genotype dispute**
7. [[S-3 - Kumar et al. 2021 — An evolutionary portrait of the progenitor SARS-CoV-2]] — reconstructs a "progenitor" genome 3 mutations from every sampled early-Wuhan genome, implying undetected earlier circulation.
8. [[S-4 - Bloom 2021 — Recovery of deleted deep sequencing data from the early Wuhan epidemic]] — recovers SRA-deleted early sequences, argues they support an earlier/more-bat-like progenitor.
9. [[S-11 - Débarre & Hensel 2025 — critical reexamination of the recovered SARS-CoV-2 sequencing data]] — direct rebuttal: recovered sequences' true collection date and mutational context don't support Bloom's progenitor framing.

**"Which lineage/type came first" — the earlier L/S round**
10. [[S-5 - Tang et al. 2020 — On the origin and continuing evolution of SARS-CoV-2 (L-S types)]] — the original (and much-cited) L/S two-type split, precursor framing to A/B.
11. [[S-6 - MacLean et al. 2020 — No evidence for distinct types in the evolution of SARS-CoV-2]] — methodological rebuttal (founder effects/drift explain the pattern; no functional "type"); template later critiques of A/B reuse.

**Recombination as an alternative mechanism**
12. [[S-25 - Esquivel Gomez et al. 2024 — recombination-aware phylogenetic analysis of SARS-CoV-2's origin]] — Bayesian recombination-aware reconstruction of RBD ancestry across SARS-CoV-2/RaTG13; bears on whether ACE2-binding residues need an engineered explanation, from the recombination/tree side rather than sequence-feature side (D).

## search_scope

WebSearch queries for each canonical anchor named in the brief (Pekar 2022/2021, Kumar 2021, Bloom 2021, Tang 2020) plus their DOI/venue/citation metadata; forward citation-chase ("who cites/critiques X") for each anchor via WebSearch phrasing ("critique of X", "rebuttal to X", "X error"); this surfaced the McCowan and Weissman Bayes-factor critiques, the Massey↔Pekar-2025 intermediate-genome exchange, and the Débarre&Hensel↔Bloom exchange. Metadata (author lists, dates, DOIs) pulled from publisher pages (Science, OUP journals — several science.org/mdpi pages 403'd and were substituted with PMC/PubMed/journal-search-snippet metadata instead) and citation counts from the Semantic Scholar Graph API (asof 2026-07-23) rather than Google Scholar (no direct tool access). Separately searched for a dedicated "recombination as alternative to two introductions" primary; found Esquivel Gomez et al. 2024 (RBD-ancestry recombination, methods-focused) but no paper arguing recombination specifically explains the human-outbreak A/B split as an alternative to Pekar's two-spillover claim — Pekar et al. 2022 itself addresses and rules out that alternative internally (not a separate node).

## exclusions

1. Erratum to Pekar et al. 2022 (Science, 2024, doi 10.1126/science.adl0585) — folded into S-1's summary rather than minted separately; it corrects a code bug in S-1 itself, not an independent primary.
2. "COVID Origins: Worobey et al. 2022 and Pekar et al. 2022 Retraction Request" (2024 letter to Science, multiple signatories) — a bundled documentary critique (retraction demand) rather than an empirical re-analysis; reads more like an institutional/documentary artifact than a phylogenetic primary, so left for slice E to consider rather than minted here. Flagged as a possible gap if E doesn't pick it up.
3. NBER working paper "A Bayesian Assessment of the Origins of COVID-19" (w33428) — a whole-evidence Bayesian synthesis, not specifically a phylogenetic/dating primary; belongs to slice G (debate & Bayesian-analysis record).
4. Holmes et al. 2021 Cell "The origins of SARS-CoV-2: A critical review" and similar reviews — used only as discovery hubs, never minted, per the pool rule (reviews aren't primaries).
5. Boni et al. 2020 Nat Microbiol (bat-sarbecovirus recombination ancestry) — considered for the recombination angle but judged closer to slice D's "closest natural relative" genome-structure territory (deep bat-lineage recombination history rather than the human-outbreak two-lineage question); not minted here to avoid encroaching on D's lane.

## Slice shape and gaps

~12 candidates read closely, several more skimmed (reviews, GISAID/Nextstrain discussion threads, preprint server comment sections). The slice has real depth: three genuine back-and-forth exchanges in the literature (Bayes-factor-error critiques of S-1; the excluded-intermediate-genome dispute; the deleted-sequences/progenitor dispute), plus one older resolved round (Tang vs. MacLean on L/S). I could not find a lab-leak-side paper proposing a competing quantitative phylodynamic model of its own (e.g. an explicit single-introduction-plus-lab-associated-timeline reconstruction with its own dating) — all lab-leak-side sources found are critiques of the zoonosis-side models (Massey, McCowan, Weissman) rather than a positive alternative phylogenetic reconstruction; this may be a genuine feature of the debate (the lab-leak case here is more "the zoonosis inference doesn't hold up" than "here is our own competing dating model") but step 2/3 should treat it as a possible gap rather than assume none exists. I also did not find a peer-reviewed rebuttal to Kumar et al. 2021's progenitor method itself (as opposed to Bloom's data, which Débarre & Hensel target) — only informal commentary.
