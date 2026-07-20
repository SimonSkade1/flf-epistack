# Orientation — slice: epi-field-evidence (searcher 1b-A)

Slice: geographic/temporal signal of earliest human cases; Huanan market wildlife trade and environmental samples; market-vs-lab ascertainment bias; record of which early-case/sampling data China released vs withheld. 8 `source` nodes written (2 over the 6-node lean-budget target — see paragraph at bottom), 8 read properly.

## Sources by topic

**Geographic/temporal case clustering & the market-epicenter claim**
1. [[S-1 - Worobey 2022 Science - Huanan market case geolocation identifies it as the COVID-19 pandemic's early epicenter]] — the load-bearing zoonosis-side case-geolocation analysis.
2. [[S-7 - Stoyan & Chiu 2024 JRSS-A - Statistical critique of Worobey 2022's market-epicenter proof]] — direct methodological rebuttal of #1's centroid/Monte-Carlo argument, found while snowballing.

**Market wildlife trade & environmental/animal samples**
3. [[S-2 - Liu 2023 Nature - China CDC environmental and animal surveillance at the Huanan market]] — the primary raw market-swab dataset (China CDC); also the closure/disinfection-timeline source.
4. [[S-3 - Crits-Christoph, Débarre, Worobey et al. 2024 Cell - Susceptible wildlife DNA co-located with SARS-CoV-2 in Huanan market samples]] — independent Western-team reanalysis of the same raw swabs (#3's data), raccoon-dog/civet DNA co-location.
5. [[S-4 - Xiao et al. 2021 Scientific Reports - Wildlife species sold live at Wuhan markets 2017-2019]] — pre-pandemic baseline establishing the wildlife trade existed at Huanan specifically.

**Market-vs-lab ascertainment bias**
6. [[S-5 - Bloom 2021 MBE - Recovered deleted early-Wuhan sequences suggest ascertainment bias toward market-linked viruses]] — the core lab-leak-favoring critique that the market-centric earliest-case pattern may be a sampling artifact.

**Data release/withholding & the official field investigation**
7. [[S-6 - WHO-China Joint Report 2021 - Field mission epi-curve and market investigation into the origins of SARS-CoV-2]] — the only on-the-ground international mission; primary epi-curve/market-tracing data, negotiated access.
8. [[S-8 - Reuters 2021 (Dwyer) - China gave WHO team only summary data, not raw line lists, on the 174 earliest COVID-19 cases]] — names exactly what data was and wasn't released to #7's own team.

## search_scope

Started from the run's discovery hubs: fetched Scott Alexander's ACX post directly and mined it for epi-relevant citations/claims (data-withholding mentions, case-clustering references); did not separately fetch Weissman's substack or Rootclaim's blog response (time budget; the named anchors already in the brief covered this slice's ground, see gap note below), and did not attempt the Google-Drive judge decisions (per the plan's own anticipated-gap fallback, relying on ACX's quotation of them instead — not independently verified this covers everything the judges said on the epi axis).

For each of the brief's named anchor candidates: direct WebSearch to locate and verify exact title/venue/date, then WebFetch (Semantic Scholar Graph API by DOI/title where possible) to pull authors + citation_count + publicationDate in one shot; WebFetch on publisher/press-release/PMC pages where Semantic Scholar didn't resolve (paywalled DOIs, 403s on Nature/Cell direct pages worked around via the semantic-scholar API redirect and a Scripps press release respectively). One additional snowball search specifically for "critique/rebuttal of Worobey 2022" (per the brief's explicit ask) surfaced Stoyan & Chiu 2024 and a second, redundant critique in National Science Review (not noded, see exclusions). One additional targeted search for China-data-withholding reporting surfaced the Reuters/Dwyer story (confirmed wire source and exact date via a direct fetch of the Al Jazeera syndication after the original outlet's own page 403'd).

## exclusions

1. Pekar, Worobey, Wertheim et al. 2022 Science (lineage A/B molecular-clock paper) — out of scope, slice 2 (genomic/molecular-clock), per explicit boundary call in the search plan despite Worobey's overlapping authorship with this slice's S-1.
2. Andersen, Rambaut, Lipkin, Holmes & Garry 2020 "Proximal Origin" (furin cleavage site) — out of scope, slice 2.
3. Any furin-cleavage-site, RaTG13/BANAL-relatedness, DEFUSE-grant, or WIV-database material surfaced while mining the ACX post — out of scope, slice 2; not individually itemized, left for that slice's searcher.
4. Bloom, Virus Evolution 2023, "Association between SARS-CoV-2 and metagenomic content of samples from the Huanan Seafood Market" — a *third* independent reanalysis of the same raw Huanan swabs already covered by S-2 (China CDC) and S-3 (Crits-Christoph/Débarre/Worobey); recurring-dataset cap per the brief, so not noded — its critique (and Débarre's Virus Evolution 2023 rebuttal of it) is instead summarized in prose inside S-3's body.
5. "A Critical Reexamination of Recovered SARS-CoV-2 Sequencing Data" (bioRxiv 2024 / MBE 2025) — a reanalysis of the same recovered sequences Bloom 2021 (S-5) already covers; same recurring-dataset logic, summarized in prose in S-5's relevance_note rather than noded.
6. "Was Wuhan the early epicenter of the COVID-19 pandemic? — A critique," National Science Review — a second critique of Worobey 2022, redundant with S-7 (Stoyan & Chiu); skipped to avoid triple-counting rebuttals of the same paper. If step 2/3 wants a second independent critique, this is the one to chase.
7. The 3 debate videos and Weissman's/Rootclaim's full write-ups — not separately mined beyond what the brief's own anchor list already specified, given the time-pressured budget; a real coverage gap, not a considered rejection (see below).

## Slice shape and gaps

This slice's 8 sources split cleanly into the four sub-areas the brief specified, each carrying at least one item per side where the material exists: case-geolocation has a zoonosis anchor (S-1) and a direct statistical rebuttal (S-7); the market-samples cluster has two independent interpretations of one shared dataset (S-2, S-3) plus pre-pandemic background (S-4); ascertainment bias is carried by a single strong lab-leak-favoring paper (S-5) with no equally-direct zoonosis-side counterpart on that specific sub-question (the closest counter is implicit in S-1/S-2's own case/sample timelines); and the data-access question has a primary source (S-6) plus a sharper factual node on what was withheld (S-8). The clearest gap: I did not find a lab-leak-favoring source that is itself primary field/epi data (as opposed to a critique of zoonosis-side data) — every lab-leak-relevant node here is either a critique (S-7), a reanalysis-of-absence (S-5), or a documentation of withheld data (S-8) rather than an affirmative field-evidence finding, which may just reflect that essentially all the physical field evidence (market, swabs, early cases) was zoonosis-collected and zoonosis-interpreted almost by construction — the lab-leak case on this axis is necessarily more about what's missing/contested than about a competing physical dataset. Also flagging: I wrote 8 source nodes against a 6-node lean-budget target (read 8, matching that part of the budget exactly) because two explicit asks in the brief — a rebuttal of Worobey 2022's conclusions, and concrete data-withholding reporting — each turned up strong, non-redundant, on-axis material (S-7, S-8) that seemed worse to cut than to include; flagging the overage here rather than in the problem log since it's a scope/judgment call, not a pipeline defect.
