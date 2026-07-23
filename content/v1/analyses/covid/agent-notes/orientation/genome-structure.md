# Orientation — Genome structure / engineering-signal (slice D)

Slice: whether the SARS-CoV-2 sequence itself, and its closest known natural relatives, look natural or engineered — furin cleavage site, restriction-site "synthetic fingerprint," codon usage, RBD/ACE2-binding features, and the closest natural relative genomes (RaTG13, RmYN02, BANAL).

13 `source` nodes written (budget was 11; went slightly over to cover both the two named anchor-vs-rebuttal pairs and the specific "out-of-frame insertion" sub-argument named in the brief, rather than dropping one of them). All 13 read properly (full abstract/methods, not just skimmed); several dozen more skimmed via reference lists and citing-article searches along the way (Frontiers in Microbiology's furin-diversity review, the Segreto/Deigin ↔ Tyshkovskiy/Panchin BioEssays exchange, "SARS-CoV-2 furin cleavage site was not engineered" PNAS, MSH3-homology commentary threads, "Exploring the Natural Origins of SARS-CoV-2 in the Light of Recombination," Holmes et al. 2021 "The origins of SARS-CoV-2: A critical review").

## Topics (sources best-first within each)

**The furin cleavage site (FCS) — existence, novelty, and whether it's engineered:**
1. [[S-56 - Coutard et al. 2020 — Furin-like cleavage site absent in CoV of the same clade]] — first report of the FCS and its absence in same-clade relatives; the empirical fact everything else below argues about.
2. [[S-46 - Andersen et al. 2020 — The Proximal Origin of SARS-CoV-2]] — zoonosis-side reading: novel but not diagnostic of engineering.
3. [[S-59 - Chan Zhan 2021-22 — Emergence of the Spike Furin Cleavage Site in SARS-CoV-2]] — measured "genuinely unresolved given undersampling" position from a lab-leak-sympathetic but methodologically cautious source.
4. [[S-61 - Chambers, Abdullah Sadhu 2026 — Ancestral reconstruction of the S1-S2 insertion codon frame]] — quantitative test of the specific "out-of-frame insertion" argument (~97% the insertion interrupted a codon).

**The BsaI/BsmBI restriction-site "synthetic fingerprint" (no-see-um argument):**
5. [[S-48 - Bruttel, Washburne & VanDongen 2022-23 — Endonuclease fingerprint indicates a synthetic origin]] — the anchor claim.
6. [[S-62 - Fuqing Wu 2023 — Updated analysis to reject the laboratory-engineering hypothesis]] — direct methodological rebuttal (miscalculated rarity statistic, natural relatives share the pattern).

**Closest known natural relative genomes (comparators for all of the above):**
7. [[S-49 - Zhou et al. 2020 Nature — RaTG13, a bat coronavirus of probable bat origin]] — the original, still-primary comparator genome.
8. [[S-52 - Temmam et al. 2022 Nature — BANAL Laos bat coronaviruses]] — closer in the RBD than RaTG13; ACE2-competent; lacks an FCS.
9. [[S-51 - Zhou et al. 2020 Current Biology — RmYN02 natural S1-S2 insertion]] — cited as natural precedent for spike-junction insertions.
10. [[S-55 - Deigin Segreto 2021 — SARS-CoV-2's claimed natural origin is undermined by genome-sequence issues]] — disputes the RaTG13/RmYN02 sequencing/assembly record itself (contamination reads; RmYN02 "insertion" argued to actually be a deletion).

**Whole-genome chimeric-origin argument:**
11. [[S-54 - Segreto Deigin 2021 — The genetic structure of SARS-CoV-2 does not rule out a laboratory origin]] — RaTG13 backbone + pangolin-MP789-like RBD + unexplained FCS, read as a plausible engineered chimera.

**Codon usage / genome composition:**
12. [[S-57 - Xia 2020 — Extreme genomic CpG deficiency in SARS-CoV-2]] — CpG deficiency as a natural-evolutionary (ZAP-evasion) signature, not an engineering tell.

**RBD / ACE2-binding features:**
13. [[S-58 - Starr et al. 2020 — Deep mutational scanning of the SARS-CoV-2 RBD]] — independent experimental test showing the wild-type RBD is not a computationally optimized ACE2 binder (many single mutations bind tighter), undercutting a "rationally designed for humans" story specifically (not serial-passage/directed-evolution routes).

## search_scope

Started from the anchors named in the brief (Andersen 2020, Bruttel et al. 2022/23, Zhou RaTG13/RmYN02, Temmam BANAL, Segreto & Deigin) and verified/extended each via WebSearch + targeted WebFetch. Citation counts and PMIDs cross-checked via NIH iCite (`icite.od.nih.gov/api/pubs`, batched by PMID) where available; Semantic Scholar's API was hit by a shared rate limit for most of the session (many concurrent 429s, likely from sibling searchers hitting the same endpoint) so iCite was the fallback and is the source for most `citation_count` values — note iCite counts run lower than Semantic Scholar/Google Scholar for the same paper in at least one case checked (Andersen: iCite 2754 vs. Semantic Scholar ~4327), a normal cross-database discrepancy, not a data error. Snowballed forward/backward from each anchor: read the Segreto/Deigin ↔ Tyshkovskiy/Panchin BioEssays exchange in full to find Deigin & Segreto 2021 (the RaTG13/RmYN02 sequence-quality paper); searched specifically for rebuttals to Bruttel et al. and found Fuqing Wu 2023; searched specifically for the "out-of-frame insertion" argument named in the brief and found Chambers/Abdullah/Sadhu 2026; searched codon-usage/CpG and RBD-optimality literature directly (not just via the anchors) to fill those two named sub-topics.

## exclusions

1. **Boni et al. 2020 Nature Microbiology** ("Evolutionary origins of the SARS-CoV-2 sarbecovirus lineage") — read as a shared hub; not minted. Its recombination/breakpoint analysis of the FCS region is phylogenetic-inference territory (slice C's data base), even though it touches the same genomic region.
2. **Holmes et al. 2021 "The origins of SARS-CoV-2: A critical review"** (Cell) — reviews the whole debate including genome-structure arguments; used only as a discovery hub per the step-1 "reviews aren't nodes" rule.
3. **Ambati et al. 2022 "MSH3 Homology and Potential Recombination Link to SARS-CoV-2 Furin Cleavage Site"** (Frontiers in Virology) — read in full; dropped rather than minted. It's a specific, narrow engineering-signal claim (a 19-nt FCS-flanking sequence matching a patented MSH3-reverse-complement construct) but drew a corrigendum and multiple critical commentaries questioning the BLAST methodology, and none of its ~7 authors are virologists/genome-origin specialists by primary training; judged not to clear the bar for a load-bearing primary given 3 more central items already covered the FCS-emergence sub-topic. Flagged here rather than silently dropped in case step 2 wants it back in.
4. **"Furin cleavage sites naturally occur in coronaviruses" (Wu & Zhao, 2021, Stem Cell Research)** — read; a broader coronavirus-family survey showing 86 diversified FCS occurrences (86 diversified furin cleavage sites in 24 animal hosts). Overlaps substantially with Coutard 2020 (already covers "FCS existence is not unique to SARS-CoV-2 status") and Chan & Zhan 2022 (already covers "undersampling limits conclusions"); dropped as redundant given the 11-13 budget rather than as low quality — a candidate for step 2 to pull in if it wants a third, more numerous-survey-style source on FCS diversity.
5. **Bloom 2021 "Recovery of deleted deep sequencing data..."** and the **Pekar/Kumar/Tang lineage-dating literature** — explicitly out of lane (slice C: phylogenetics/dating), not read past the abstract.
6. **The DEFUSE proposal and WIV documentary record** — explicitly out of lane (slice E: institutional/circumstantial), not pursued even though Segreto & Deigin references DEFUSE-style feasibility.

## Note on the slice

The slice splits cleanly into four sub-arguments (FCS existence/novelty, restriction-site fingerprint, closest-relative-genome comparison, codon-usage/RBD-optimality), and each sub-argument already has a real primary-vs-rebuttal pair in the literature — this made "extend + chase rebuttals both ways" straightforward rather than lopsided. The one place I could not find a clean anchor-and-rebuttal pair is the RBD/ACE2-optimality argument: Starr et al. 2020 is a strong, independent primary, but I did not find a paper that directly disputes its "not computationally optimal" reading in engineering-signal terms (as opposed to disputing serial-passage/directed-evolution routes, which Starr et al. itself doesn't address) — flagged as a gap. I also did not find any working link (only a duplicate-lineage note) between this slice's restriction-site argument and slice E's DEFUSE proposal (which reportedly proposed inserting a furin cleavage site) — that specific cross-slice tie is worth someone checking, but minting/analyzing the DEFUSE text itself is out of my lane.
