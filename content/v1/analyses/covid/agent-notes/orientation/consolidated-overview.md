# Consolidated pool overview — COVID origins (zoonosis vs lab leak)

Step-1 consolidator (1c) note. Not a graph node. This is step 2's (2b) entry point for pool shape: the merged, grouped, best-first view of all `source` nodes produced by the 7 blind searchers (slices A–G), with duplicates, cross-cutting caveats, the union of exclusions, and a coverage/gap map.

Main question (verbatim): "Did SARS-CoV-2 first infect humans through natural zoonotic spillover (e.g. via the wildlife trade / Huanan Seafood Market) or through a research-related incident (a lab leak)?"

## Pool summary

1. **86 `source` nodes** (S-1 … S-86), all present and well-formed.
2. **0 nodes flagged `duplicate_of`.** No two nodes are the same primary artifact. The one suspected true duplicate (S-34 / S-47, both citing the WHO-China joint report PDF) was adjudicated **distinct** — see below.
3. **0 broken cross-source wikilinks.** All 13 distinct `[[S-N …]]` cross-references in source frontmatter/bodies resolve to existing files (searchers C and D's post-lock cross-ref fixes verified clean).

### Adjudication: S-34 vs S-47 (the WHO joint report) — kept as distinct

Both cite the same document (`who-...-china-part-joint-report.pdf`, 2021-03-30), the only shared URL in the pool. But they carry **different, non-redundant data sections** mapping to **different data bases**:
- **S-47** = the market **environmental swab** round (585 samples / ~33 positive by end-Jan-2020, west/wildlife side, market disinfection, cold-chain-from-20-countries hypothesis) → slice A's **market-environmental** data basis; an earlier, smaller official precursor of the fuller China CDC campaign in S-16.
- **S-34** = the **nationwide animal surveillance** (>80,000 wildlife/livestock/poultry samples across 31 provinces, zero positive) + 457 market-animal samples negative + the report's overall probability ranking (lab "extremely unlikely") → slice F's **animal-surveillance / intermediate-host** data basis.

They report different headline numbers, and each carries load-bearing data the other lacks. Flagging S-47 → S-34 (higher-id rule) would make the animal-surveillance node the survivor and orphan slice A's market-environmental precursor — actively wrong for the pipeline. This is the same pattern as **S-18** (the report's early-case-epidemiology section, slice B), which the brief already keeps as distinct. **Divergence from the consolidator brief's prior**, which expected S-34/S-47 to be a true duplicate; recorded so it can be overridden if the report-section structure is known to differ from this reading.

### Shared-document provenance (for step 2 — not a duplicate, but not independent either)

- **S-18, S-34, S-47 are three sections of the ONE WHO-China joint report.** Treat as sharing institutional reliability and motivatedness (China-negotiated data access), so do **not** count them as three independent corroborating sources — but they carry three distinct data bases (early-case epi / animal surveillance / market environmental).

### Preprint↔published & version pairs (distinct nodes; step 2 should assign each pair a SHARED data-basis)

- **S-15** (China CDC Research Square preprint) ↔ **S-16** (Nature) — same market-surveillance campaign.
- **S-24** (Zenodo rapid report) → **S-31** (bioRxiv preprint) → **S-35** (Cell) — the three Crits-Christoph raccoon-dog versions; one underlying analysis of the China CDC metagenomic dataset.
- **S-54** and **S-55** are **two different Segreto/Deigin papers** (whole-genome chimera argument vs RaTG13/RmYN02 sequence-quality argument), NOT versions of one — keep both.
- **S-71** (Senate HELP interim, Oct 2022) and **S-72** (Muddy Waters, Apr 2023) are distinct reports (predecessor vs fuller); **S-68**/**S-69** (ODNI 2021/2023) and **S-70**/**S-83** (Judge Eric decision / his Weissman response) likewise distinct.

## Cross-cutting caveats for step 2

1. **Citation counts come from three different indexes and are NOT comparable across nodes.** Slices A/B/C used Semantic Scholar; F used OpenAlex; D used NIH **iCite (systematically lower** — e.g. Andersen 2020: iCite 2754 vs Semantic Scholar ~4327). E/G nodes are mostly government/debate documents with `citation_count: unknown`. **Do not read a low or `unknown` count as a data-reliability signal** — it is a cross-database/indexing artifact or a non-indexed document type.
2. **Attribution fix:** the "Muddy Waters" report (S-72) and its predecessor (S-71) are **Senate HELP Committee** (Health, Education, Labor & Pensions) minority/GOP staff products — **not HSGAC**, as the planner's brief said. HSGAC (Rand Paul) runs a separate ongoing investigation with no comparable stable report as of step 1.
3. **Shared data bases within slices** (so correlation isn't double-counted):
   - B geospatial cluster — S-17, S-18, S-23, S-26, S-30, S-32, S-36 — all re-use the **same ~155–164-case location dataset** extracted from the WHO report maps (S-18). One shared data basis, not seven independent lines.
   - A raccoon-dog dispute — S-24/S-31/S-35 (Crits-Christoph), S-39/S-43 (Bloom), S-42 (Débarre), S-53 (Nickels letter) — all operate on the **single released China CDC metagenomic dataset (S-21)**. One shared data basis.
4. **`refuted`/`duplicate_of` fields** are pre-populated (blank or filled) on the slice-C phylo nodes; the filled `refuted` notes (S-3, S-4, S-5, S-7) record live in-literature rebuttals, not pipeline deletions.
5. **Side-balance confirmed.** The lab-leak side is represented by **positive** evidence, not only critiques of zoonosis papers: genome (S-48 synthetic fingerprint, S-54/S-55 chimera + sequence-quality, S-59 FCS emergence), institutional (S-65/S-66 DEFUSE, S-68/S-69/S-84 IC assessments, S-71/S-72/S-85 oversight reports, S-74 State Dept, S-81 FOIA, S-82 DRASTIC, S-75/S-77 Mojiang/RaTG13, S-78 cables), and independent Bayesian replication (S-60 Rootclaim ~89% lab, S-64 Weissman lab-favoring, S-86 Levin NBER 14,900:1 lab).

## Sources by slice (best-first within each group)

### A — Huanan market environmental / metagenomic samples (12)
*Primary sampling campaign & its data:* [[S-16 - Liu, Gao et al. — Surveillance of SARS-CoV-2 at the Huanan Seafood Market (Nature)]] · [[S-15 - China CDC Research Square preprint — Huanan market environmental & animal surveillance]] (preprint of S-16) · [[S-21 - China CDC raw metagenomic sequencing data release — Huanan market samples (NGDC GSA - NCBI BioProject)]] (the dataset every reanalysis below uses).
*Raccoon-dog / susceptible-wildlife co-location dispute (all on S-21):* [[S-35 - Crits-Christoph et al. — Genetic tracing of market wildlife and viruses at the epicenter of the COVID-19 pandemic (Cell)]] · [[S-31 - Crits-Christoph et al. — Genetic tracing of market wildlife and viruses at the epicenter of the COVID-19 pandemic (bioRxiv preprint)]] · [[S-24 - Crits-Christoph et al. — Genetic evidence of susceptible wildlife in SARS-CoV-2-positive Huanan market samples (Zenodo report)]] · [[S-39 - Bloom — Association between SARS-CoV-2 and metagenomic content of Huanan market samples]] · [[S-42 - Débarre — What we can and cannot learn from SARS-CoV-2 and animals in metagenomic samples from the Huanan market]] · [[S-43 - Bloom — Importance of quantifying the number of viral reads in metagenomic sequencing of Huanan market samples]] · [[S-53 - Nickels et al. — open letter requesting retraction of Crits-Christoph et al. 2024 (Cell)]].
*Official record:* [[S-47 - WHO-China joint mission report — animal and environment (Huanan market) section]] (market-env section of the WHO report; precursor to S-16) · [[S-50 - WHO SAGO statement on newly released China CDC metagenomics data from Huanan market]].

### B — Early-case epidemiology & geospatial clustering (11)
*Clinical case series & official line list:* [[S-13 - Li et al. 2020 NEJM — early transmission dynamics, first 425 confirmed cases]] · [[S-9 - Huang et al. 2020 Lancet — clinical features of the first 41 hospitalized 2019-nCoV patients]] · [[S-10 - Chen et al. 2020 Lancet — 99-case single-hospital descriptive series]].
*Geospatial case-clustering / market-epicenter claim:* [[S-17 - Worobey et al. 2022 Science — geolocated case map naming the Huanan market the early epicenter]] · [[S-18 - WHO-China joint study (2021) — early-case epidemiology and residential-location maps]] (early-case section of the WHO report; supplies the shared case-location dataset).
*"First case" / earliest-onset dispute:* [[S-14 - Worobey 2021 Science — dissecting the early COVID-19 cases in Wuhan (the first-case correction)]].
*Ascertainment-/surveillance-bias critiques & rebuttals:* [[S-23 - Stoyan & Chiu 2024 JRSS-A — statistical critique of the market-epicenter geospatial claim]] · [[S-26 - Débarre & Worobey 2024 — reply to Stoyan & Chiu, reaffirming market centrality]] · [[S-30 - Weissman 2024 JRSS-A letter — proximity ascertainment bias in early case locations]] · [[S-32 - Débarre & Worobey 2024 — reply to Weissman, against systematic ascertainment bias]] · [[S-36 - Zhang, Demaneuf et al. 2022 — within-market spatial critique, superspreader-not-spillover reading]].

### C — Genomic phylogenetics & molecular dating (12)
*Two-introduction inference:* [[S-1 - Pekar et al. 2022 — molecular epidemiology of multiple zoonotic origins of SARS-CoV-2]] · [[S-2 - Pekar et al. 2021 — Timing the SARS-CoV-2 index case in Hubei province]].
*Bayes-factor critiques (methodological):* [[S-22 - Weissman 2026 — a fundamental Bayesian error in the multiple-introductions claim]] · [[S-12 - McCowan 2025 — imbalanced hypothesis-testing framework in the multiple-introductions claim]].
*Excluded "intermediate" A-B genomes dispute:* [[S-7 - Massey et al. 2023 — Unwarranted exclusion of intermediate lineage A-B genomes]] (`refuted` by S-8) · [[S-8 - Pekar et al. 2025 — reported intermediate lineage A-B genomes are instead derived]].
*Deleted-sequences / progenitor dispute:* [[S-3 - Kumar et al. 2021 — An evolutionary portrait of the progenitor SARS-CoV-2]] (`refuted` partially by S-4/S-11) · [[S-4 - Bloom 2021 — Recovery of deleted deep sequencing data from the early Wuhan epidemic]] (`refuted` by S-11) · [[S-11 - Débarre & Hensel 2025 — critical reexamination of the recovered SARS-CoV-2 sequencing data]].
*Earlier L/S round:* [[S-5 - Tang et al. 2020 — On the origin and continuing evolution of SARS-CoV-2 (L-S types)]] (`refuted` by S-6) · [[S-6 - MacLean et al. 2020 — No evidence for distinct types in the evolution of SARS-CoV-2]].
*Recombination alternative:* [[S-25 - Esquivel Gomez et al. 2024 — recombination-aware phylogenetic analysis of SARS-CoV-2's origin]].

### D — Genome structure & engineering-signal (13)
*Furin cleavage site — existence, novelty, engineering:* [[S-56 - Coutard et al. 2020 — Furin-like cleavage site absent in CoV of the same clade]] · [[S-46 - Andersen et al. 2020 — The Proximal Origin of SARS-CoV-2]] · [[S-59 - Chan Zhan 2021-22 — Emergence of the Spike Furin Cleavage Site in SARS-CoV-2]] · [[S-61 - Chambers, Abdullah Sadhu 2026 — Ancestral reconstruction of the S1-S2 insertion codon frame]].
*Restriction-site "synthetic fingerprint":* [[S-48 - Bruttel, Washburne & VanDongen 2022-23 — Endonuclease fingerprint indicates a synthetic origin]] · [[S-62 - Fuqing Wu 2023 — Updated analysis to reject the laboratory-engineering hypothesis]].
*Closest natural relative genomes:* [[S-49 - Zhou et al. 2020 Nature — RaTG13, a bat coronavirus of probable bat origin]] · [[S-52 - Temmam et al. 2022 Nature — BANAL Laos bat coronaviruses]] · [[S-51 - Zhou et al. 2020 Current Biology — RmYN02 natural S1-S2 insertion]] · [[S-55 - Deigin Segreto 2021 — SARS-CoV-2's claimed natural origin is undermined by genome-sequence issues]].
*Whole-genome chimeric-origin argument:* [[S-54 - Segreto Deigin 2021 — The genetic structure of SARS-CoV-2 does not rule out a laboratory origin]].
*Codon usage / composition:* [[S-57 - Xia 2020 — Extreme genomic CpG deficiency in SARS-CoV-2]].
*RBD / ACE2-binding features:* [[S-58 - Starr et al. 2020 — Deep mutational scanning of the SARS-CoV-2 RBD]].

### E — Institutional / circumstantial records (14)
*DEFUSE proposal episode:* [[S-65 - Project DEFUSE proposal (EcoHealth Alliance to DARPA, 2018)]] · [[S-66 - DARPA's internal rejection review of the DEFUSE proposal]].
*US intelligence-community assessments:* [[S-68 - ODNI declassified Updated Assessment on COVID-19 Origins (Aug 2021)]] · [[S-84 - FBI and DOE 2023 agency-confidence positions on a lab-associated origin]] · [[S-69 - ODNI Report on Potential Links Between WIV and COVID-19 Origins (June 2023)]].
*Congressional oversight:* [[S-85 - House Select Subcommittee staff report on EcoHealth Alliance and WIV funding (May 2024)]] · [[S-72 - Muddy Waters- The Origins of COVID-19 (Senate HELP GOP staff report, Apr 2023)]] (Senate **HELP**, not HSGAC) · [[S-71 - Senate HELP Committee minority interim report on COVID-19 origins (Oct 2022)]].
*WIV research records:* [[S-77 - Nature addendum disclosing RaTG13's identity with the Mojiang mine sample RaBtCoV-4991]] · [[S-82 - DRASTIC investigation into the WIV pathogen databases taken offline in Sept 2019]].
*Federal funding oversight:* [[S-81 - FOIA-released NIAID-EcoHealth Alliance gain-of-function correspondence and grant records]].
*Biosafety / diplomatic:* [[S-78 - Washington Post report on 2018 State Department cables warning of WIV biosafety issues]].
*Mojiang miners clinical record:* [[S-75 - Li Xu's master's thesis on the 2012 Mojiang miners' pneumonia cases]].
*State Department claims:* [[S-74 - State Department Fact Sheet- Activity at the Wuhan Institute of Virology (Jan 2021)]].

### F — Wildlife trade, host range & serology (13)
*Wildlife on sale at Wuhan markets:* [[S-19 - Xiao et al. 2021 — animal sales from Wuhan wet markets pre-pandemic]].
*Host-susceptibility / experimental infection:* [[S-20 - Freuling et al. 2020 — raccoon dog experimental SARS-CoV-2 infection]] · [[S-27 - Oreshkova et al. 2020 — SARS-CoV-2 outbreak on Dutch mink farms]] · [[S-29 - Shi et al. 2020 — susceptibility of ferrets, cats, dogs and other domesticated animals to SARS-CoV-2]] · [[S-28 - Sia et al. 2020 — pathogenesis and transmission of SARS-CoV-2 in golden hamsters]] · [[S-33 - Damas et al. 2020 — comparative-structural ACE2 host-range prediction for SARS-CoV-2]].
*Intermediate-host search / animal surveillance (largely negative):* [[S-34 - WHO-China joint report 2021 — animal and environmental sampling section]] (nationwide + market-animal surveillance section of the WHO report) · [[S-37 - Deng et al. 2020 — 35-species serosurvey excludes intermediate hosts]] · [[S-40 - Xiao K. et al. 2020 — isolation of SARS-CoV-2-related coronavirus from Malayan pangolins]].
*Human serosurveys (pre-Dec-2019):* [[S-38 - Chang et al. 2022 — Wuhan blood-donor serosurvey, September-December 2019]].
*SARS-1 / MERS spillover precedent:* [[S-41 - Guan et al. 2003 — SARS-CoV-like viruses isolated from market civets, southern China]] · [[S-44 - Kan et al. 2005 — SARS-CoV-like virus in market civets vs farmed civets]] · [[S-45 - Reusken et al. 2013 — MERS-CoV neutralising antibodies in dromedary camels]].

### G — Debate & Bayesian-analysis record (11)
*The two debaters' primary cases:* [[S-60 - Rootclaim's main COVID-19 origins analysis]] · [[S-73 - Peter Miller's written case against the lab-leak theory]].
*Debate record & judges' decisions:* [[S-70 - Judge Eric Stansifer's written decision]] · [[S-67 - Judge Will van Treuren's written decision]] · [[S-76 - The Rootclaim vs. Peter Miller COVID-origins debate, video record]].
*"Six analyses spanning 23 OOM" synthesis:* [[S-79 - Scott Alexander's ACX review of the Rootclaim debate]] · [[S-63 - Rootclaim's response to Scott Alexander's ACX review]] · [[S-80 - Daniel Filan's Bayesian analysis of COVID origins]].
*Independent analyses outside the "six" + methodological cross-examination:* [[S-64 - Weissman's 'An Inconvenient Probability' Bayesian analysis]] · [[S-83 - Judge Eric Stansifer's response to Michael Weissman]] · [[S-86 - Levin's NBER Bayesian assessment of COVID-19 origins]].

## Union of exclusions (all searchers)

*Considered and dropped at ingestion — a reader can tell these from gaps.*

**Superseded / redundant versions:** Pekar 2022 erratum (folded into S-1); Worobey 2022 erratum (folded into S-17); Stoyan & Chiu 2022 preprint arXiv:2208.10106 (superseded by S-23); earlier Feb-2020 WHO-China Joint Mission report (superseded by S-18); House Select Subcommittee Dec-2024 ~520pp final report (restates S-85); Scribd/ResearchGate/Newsweek DEFUSE copies (duplicate hosting of S-65/S-66); Rootclaim "debate results" blog post (folded into S-76); Judge Will's spreadsheet, video summaries, Scott's blank calculator template (raw artifacts under minted prose).

**Out of lane (owned by a sibling slice, read as shared hub):** for A — Worobey 2022 / WHO early-case annex (B), Xiao 2021 + susceptibility studies (F), Débarre & Worobey arXiv:2403.05859 (B); for D — Boni et al. 2020 (C), Bloom/Pekar/Kumar/Tang dating (C), DEFUSE text (E); for C — NBER Bayesian synthesis (G, = S-86); for F/B — market env/metagenomic + phylo + genome + institutional papers each left to their owner slice.

**Reviews / secondary syntheses (not primaries, per pool rule):** Holmes et al. 2021 Cell "critical review"; Alina Chan & Matt Ridley "Viral" (book); Cohen 2020 Science news; Andrew Gelman blog commentary (incl. his Levin critique); DARPA's 2021 public denial statement; GAO-23-105406 (generic pandemic-origin tech, not COVID-specific).

**Judged below the bar / redundant primaries:** Ambati et al. 2022 MSH3-homology FCS claim (corrigendum + methodology critiques; FCS sub-topic already covered); Wu & Zhao 2021 FCS-diversity survey (redundant with S-56/S-59); Dong & Hiscox 2023 (human BAL sequences, not market swabs); Courtier-Orgogozo & de Ribera 2022 (within-market human-to-human transmission argument, not a sampling record); Lam et al. 2020 pangolin CoV (overlaps S-40); Tu 2004 / Song 2005 civet SARS-1 (precedent covered by S-41/S-44); Haagmans 2013 MERS camel (covered by S-45); structural SARS-1 civet-ACE2 papers (superseded by S-33 for SARS-CoV-2).

**Not-part-of-scope debate artifacts:** Quay & Muller and Demaneuf & de Maistre Bayesian analyses (checked — NOT part of the debate's "six," not engaged by any of them; a wider-genre gap, see below); Peter Daszak's aside estimate + Good Judgment Project sub-study (informal, inside S-79); Yuri Deigin's technical claims (genome-structure, slice D); Senate HSGAC "Reading Room" (ongoing, no stable report).

## Coverage & gap map (audit vs search-plan)

**Well-covered / deep (no top-up needed):** A (market env — data trunk + 3-round reanalysis dispute); B (epi/geospatial — but note all 7 nodes share ONE case-location dataset; node count ≠ independent lines); C (two-introduction + three live rebuttal exchanges); D (each of 4 sub-arguments has a primary+rebuttal pair); E (14 nodes, complete against the anchor list); F (5 sub-questions covered); G (the "six" pinned down + Weissman + Levin replication). **DEFUSE confirmed in pool** (S-65 proposal, S-66 DARPA rejection) — the D↔E tie (S-54/S-55/S-48's engineering argument ↔ DEFUSE's proposed FCS insertion) is a cross-slice link for step 3/5, not a source gap.

**Gaps (see my return message for the real-vs-structural judgment and top-up suggestions):**
1. **Base-rate primary** for "a novel pathogen's first-detected cluster centers on a market/venue regardless of true origin" (leaned on by Rootclaim/Weissman/judge Eric). **Not covered by any A/B/F node** — the SARS-1/MERS precedent nodes (S-41/S-44/S-45) show market *amplification of a true zoonosis*, not the null. Likely a **real** gap.
2. **A:** no China/Chinese-academic rebuttal to Bloom/Nickels (all reanalyses Western-authored) — possible real gap (Chinese-language search not done) or structural (China CDC hasn't publicly engaged).
3. **C:** no lab-leak-side *positive* phylodynamic/dating model (all lab-leak phylo sources are critiques); no rebuttal of Kumar's progenitor *method* — likely **structural** (debate asymmetry).
4. **F:** no SARS-CoV-2 civet-challenge study (structural — apparently never done); no post-2021 farmed-wildlife serosurvey responding to the market-metagenomics controversy (borderline real).
5. **E:** no public WIV internal biosafety/incident records — **structural** (China has not released them); a trust-scoring asymmetry, unfixable by search.
