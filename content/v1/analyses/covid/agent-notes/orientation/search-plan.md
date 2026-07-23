# Step-1 search plan — COVID origins (zoonosis vs lab leak)

Planner (1a) note. This file is (a) the survey/plan and (b) seven ready-to-spawn 1b searcher prompts. No `source` nodes are minted here.

Main question (verbatim): "Did SARS-CoV-2 first infect humans through natural zoonotic spillover (e.g. via the wildlife trade / Huanan Seafood Market) or through a research-related incident (a lab leak)?"

## (a) Survey / plan

### The debate's shape
Two hypothesis families: **zoonosis** (natural spillover, most likely at/near the Huanan Seafood Market via traded wildlife) vs **lab-leak / research-related** (escape from WIV or associated fieldwork/lab work, ranging from an unmodified field-collected virus to an engineered/gain-of-function construct). The case is anchored on the early-2024 $100k Rootclaim (Saar Wilf) vs Peter Miller judged debate; two judges ruled for zoonosis; six independent Bayesian analyses of the same evidence spanned ~23 orders of magnitude. So the graph must recompute a Bayesian conclusion from BOTH the primary empirical evidence AND the primary record of the debate's arguments.

### Literatures / recurring datasets that bear on the question
1. **Huanan market environmental & metagenomic sampling** — China CDC swabs (Jan–Mar 2020), which stalls were viral-RNA-positive, susceptible-species genetic material (raccoon-dog mtDNA) co-located with virus, metagenomic reanalyses. Key data base: the market environmental sample set.
2. **Early-case epidemiology & geospatial clustering** — the WHO/China early-case line list, clinical case series (first 41; 425 cases), residential/exposure geolocations, the Dec-2019 case map centered on the market, the "first case" (vendor vs Chen Wei) dispute, and ascertainment/surveillance-bias critiques. Data base: early-case line list + geolocations.
3. **Genomic phylogenetics & molecular dating** — lineage A/B two-introduction analyses, tMRCA / molecular-clock estimates, recombination, the deleted early Wuhan sequences / progenitor argument. Data base: early GISAID genome collection + phylodynamic models.
4. **Genome structure & engineering-signal arguments** — furin cleavage site (PRRA insertion, CGG-CGG codons), the BsaI/BsmBI restriction-site "synthetic fingerprint," codon/RBD features, and comparison to closest natural relatives (RaTG13, RmYN02, BANAL-52). Data base: the reference genome + closest natural relative sequences.
5. **Institutional / circumstantial records** — DEFUSE proposal, WIV research records & the offline virus database, biosafety (BSL-2) practices, Mojiang miners / RaTG13 provenance, the reported Nov-2019 sick WIV workers, and US intelligence/oversight assessments (ODNI, FBI, DOE, Senate). Data base: institutional documents & intelligence assessments.
6. **Wildlife trade, host range & serology** — wildlife on sale in Wuhan markets, host-susceptibility experiments (raccoon dogs, mink, civets, hamsters), the (largely negative) intermediate-host and animal serosurveys, human pre-Dec-2019 serosurveys, and SARS-1/MERS spillover precedent. Data base: wildlife-trade surveys + animal susceptibility/serosurvey data.
7. **The debate & Bayesian-analysis record itself** — Rootclaim analysis + response, Weissman's Bayesian analysis, judge Will and judge Eric decisions, Peter Miller's rebuttals, Scott Alexander's ACX writeup, the debate transcripts/videos, and the other Bayesian analyses in the "six spanning 23 OOM" set. Treated as primary artifacts for their OWN arguments (deliberate exception to the "no reviews as nodes" rule).

### Sides — balance
- **Zoonosis-leaning primary evidence:** slices A (market env), B (epi geospatial), F (wildlife/host/serology), plus the two-introduction result in C.
- **Lab-leak-leaning primary evidence:** slices D (genome structure/engineering), E (institutional/DEFUSE).
- **Neutral / methodological / both-sides:** slice C (phylogenetics is used by both), slice G (debate + Bayesian meta-analyses span the full range).
Every side and the methodological record are represented; no side is left to a single searcher's framing.

### Independence axes I am balancing across
The overriding failure mode is forty re-analyses of one dataset. I slice by **distinct data base**, so parallel searchers hit genuinely independent evidence rather than the same numbers:
1. Market environmental samples (A) ≠ human early-case line list (B) — different measurements at the same location.
2. Phylogenetic/dating inference (C) ≠ genome-structure/engineering inference (D) — both read "the genome," but different analyses, comparators, and arguments; kept apart and flagged as partially correlated.
3. Documentary/institutional record (E) ≠ any wet-lab or sequence measurement.
4. Wildlife-trade/host/serology (F) is the animal-side data base, disjoint from the market swabs (A) and human cases (B).
5. The argument record (G) is disjoint from all empirical primaries — it mints debate/analysis artifacts only.

### Disjointness rules (so parallel searchers never duplicate)
- Ownership is by **data base**, not by topic keyword. A given primary belongs to exactly one slice: e.g. Crits-Christoph raccoon-dog metagenomics → A only; Worobey geospatial case-map → B only; Pekar two-introductions → C only; Andersen "Proximal Origin" / Bruttel restriction-site → D only; DEFUSE proposal → E only; Xiao wildlife-trade survey → F only; Rootclaim/Weissman/judges → G only.
- **A vs B:** A owns environmental-swab / metagenomic / species-DNA data; B owns human-case data (line list, geolocations, clinical series, first-case dispute, ascertainment-bias). Both may READ Worobey 2022 Science, but the geospatial case-map paper is B's node; env-sample papers are A's.
- **C vs D:** C owns tree topology, number of introductions, tMRCA/molecular clock, recombination, progenitor/deleted-sequence work. D owns furin cleavage site, restriction-site/synthetic-origin, codon/RBD features, and closest-natural-relative genomes. Neither mints the other's papers.
- **E vs D:** E owns the DEFUSE proposal and institutional documents as documentary records; D owns whether the genome's features (e.g. FCS matching DEFUSE plans) are natural or engineered as a sequence argument.
- **F vs A/B:** F owns animals-sold / host-susceptibility / serosurvey data; it does NOT touch the Huanan environmental swabs (A) or the human case line list (B).
- **G vs A–F:** G mints ONLY debate/analysis/Bayesian/methodology artifacts. It must NOT mint empirical primaries; it snowballs through the artifacts to surface empirical primaries but leaves minting those to A–F (and flags any it thinks a sibling missed as a gap).
- Each empirical searcher (A–F) is told to mine the debate artifacts, Scott Alexander's writeup, the judge decisions, and topical reviews as discovery hubs for primaries in ITS lane — reading a shared hub is fine; minting is lane-bounded.

### Number of searchers & budget
**7 searchers** (one per independent data base above; 7 fits the independence axes better than 6 — merging A+B or C+D would collapse genuinely distinct data bases). Step-1 totals: ~80 `source` notes written, ~160 read properly, more skimmed via reviews/reference lists. `curated_target_N` = 20; err toward breadth.

| slice | focus (data base) | write | read |
|---|---|---|---|
| A | Huanan market environmental / metagenomic samples | 12 | 24 |
| B | Early-case epidemiology & geospatial clustering | 11 | 22 |
| C | Genomic phylogenetics & molecular dating | 12 | 24 |
| D | Genome structure & engineering-signal arguments | 11 | 22 |
| E | Institutional / circumstantial records | 12 | 24 |
| F | Wildlife trade, host range & serology | 11 | 22 |
| G | Debate & Bayesian-analysis record | 11 | 22 |
| **total** | | **80** | **160** |

---

## (b) Searcher prompts (ready to spawn)

### Searcher A — Huanan market environmental / metagenomic samples

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/covid
Main question (verbatim): "Did SARS-CoV-2 first infect humans through natural zoonotic spillover (e.g. via the wildlife trade / Huanan Seafood Market) or through a research-related incident (a lab leak)?"
Your slice: The Huanan Seafood Market ENVIRONMENTAL & METAGENOMIC sampling data base — the primary record of what was physically sampled at the market. Covers: China CDC environmental swabs (Jan–Mar 2020), which stalls/sewage/surfaces were SARS-CoV-2-positive, the spatial distribution of positives within the market, susceptible-species genetic material (esp. raccoon-dog and other wildlife mtDNA) co-located with viral RNA, viral lineages recovered from the swabs, and metagenomic reanalyses of the released sequencing data. Canonical anchors to find, verify metadata, and snowball from (non-exhaustive — extend and chase references/critiques both ways): Liu/Gao et al. China CDC market surveillance paper (Nature 2023, and its 2022 Research Square preprint); Crits-Christoph et al. raccoon-dog / susceptible-wildlife metagenomics (Cell 2024 / 2023 preprint); the WHO-China joint report environmental-sampling annex; Débarre and others' reanalyses of the market metagenomic data; any China CDC data releases (GSA/NGDC). You MUST NOT mint: human early-case line-list / geolocation / clinical-series papers or the market geospatial case-map (Worobey 2022 Science) — those are slice B's; phylogenetic/dating papers (slice C); genome-engineering/FCS papers (slice D); wildlife-trade-survey / host-susceptibility / serosurvey papers (slice F). You may READ shared hubs (Scott Alexander's writeup, judge decisions, reviews) to find primaries, but only mint market-environmental-data primaries.
Budget: write 12 `source` notes; read 24 sources properly; skim more via reviews/reference lists.
Mint every source node by piping markdown on stdin (body carries {{ID}}; title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/covid --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents. Use WebSearch/WebFetch (load them via ToolSearch) to find real sources with resolving URLs and real metadata (venue, date, citation count + asof, field).
Finish by writing your own orientation note `agent-notes/orientation/market-environmental.md` per the step-01 spec (your sources as wikilinks under topic headings, best-first; search_scope; exclusions; ~1 paragraph on the slice).
Return: the S-ids you created, the orientation-note path, and any gaps you hit.
```

### Searcher B — Early-case epidemiology & geospatial clustering

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/covid
Main question (verbatim): "Did SARS-CoV-2 first infect humans through natural zoonotic spillover (e.g. via the wildlife trade / Huanan Seafood Market) or through a research-related incident (a lab leak)?"
Your slice: The EARLY HUMAN-CASE epidemiology & geospatial data base — who the earliest cases were, where they lived and were exposed, and how the case cluster maps onto the market. Covers: the WHO-China early-case line list; clinical case series of the first patients (e.g. Huang et al. Lancet first 41 cases; Li et al. NEJM 425 cases); the residential/exposure geolocation analysis and Dec-2019 case map centered on the Huanan market (Worobey 2022 Science "early epicenter"); the "first case" / earliest-onset dispute (market vendor vs the Chen Wei Dec-1 case, Worobey 2021 Science); and the ascertainment-/surveillance-bias critiques of the market-clustering inference. Canonical anchors to find, verify, and snowball from (extend + chase critiques both ways): Worobey et al. 2022 Science (case geolocations); Worobey 2021 Science "Dissecting the early COVID-19 cases in Wuhan"; Huang et al. 2020 Lancet; Li et al. 2020 NEJM; the WHO-China joint mission report early-case section; surveillance-bias critiques (e.g. Stoyan/Chiu, and lab-leak-side rebuttals of the geospatial claim). You MUST NOT mint: market ENVIRONMENTAL/metagenomic swab papers (slice A); molecular-phylogenetic/dating papers such as Pekar (slice C); genome-structure/FCS papers (slice D); institutional documents (slice E); wildlife-trade/host/serosurvey papers (slice F). You may READ shared hubs to find primaries, but only mint human-case epidemiology/geospatial primaries.
Budget: write 11 `source` notes; read 22 sources properly; skim more via reviews/reference lists.
Mint every source node by piping markdown on stdin (body carries {{ID}}; title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/covid --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents. Use WebSearch/WebFetch (load them via ToolSearch) to find real sources with resolving URLs and real metadata (venue, date, citation count + asof, field).
Finish by writing your own orientation note `agent-notes/orientation/early-case-epidemiology.md` per the step-01 spec (your sources as wikilinks under topic headings, best-first; search_scope; exclusions; ~1 paragraph on the slice).
Return: the S-ids you created, the orientation-note path, and any gaps you hit.
```

### Searcher C — Genomic phylogenetics & molecular dating

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/covid
Main question (verbatim): "Did SARS-CoV-2 first infect humans through natural zoonotic spillover (e.g. via the wildlife trade / Huanan Seafood Market) or through a research-related incident (a lab leak)?"
Your slice: The SARS-CoV-2 PHYLOGENETIC & MOLECULAR-DATING data base — inference from the early genome collection about how many times the virus entered humans, the tree topology, and when. Covers: the lineage A / lineage B two-introduction analyses; molecular-clock / tMRCA and index-case timing estimates; recombination and phylodynamic simulations; the "which lineage came first" dispute; and the deleted-early-Wuhan-sequences / progenitor-genotype work. Canonical anchors to find, verify, and snowball from (extend + chase critiques both ways): Pekar et al. 2022 Science "molecular epidemiology of multiple zoonotic origins"; Pekar et al. 2021 Science "Timing the SARS-CoV-2 index case"; Kumar et al. 2021 MBE progenitor analysis; Bloom 2021 "Recovery of deleted deep sequencing data..."; Tang et al. 2020 (L/S types); and lab-leak-side / methodological critiques of the two-introduction inference (e.g. Bloom, Kumar, Stoyan). You MUST NOT mint: genome-structure / furin-cleavage-site / restriction-site / closest-natural-relative-sequence papers (slice D — even though those also read "the genome"); market environmental (A) or human-case epidemiology (B) papers; institutional documents (E); wildlife/host/serosurvey papers (F). You may READ shared hubs to find primaries, but only mint phylogenetics/dating primaries.
Budget: write 12 `source` notes; read 24 sources properly; skim more via reviews/reference lists.
Mint every source node by piping markdown on stdin (body carries {{ID}}; title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/covid --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents. Use WebSearch/WebFetch (load them via ToolSearch) to find real sources with resolving URLs and real metadata (venue, date, citation count + asof, field).
Finish by writing your own orientation note `agent-notes/orientation/phylogenetics-dating.md` per the step-01 spec (your sources as wikilinks under topic headings, best-first; search_scope; exclusions; ~1 paragraph on the slice).
Return: the S-ids you created, the orientation-note path, and any gaps you hit.
```

### Searcher D — Genome structure & engineering-signal arguments

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/covid
Main question (verbatim): "Did SARS-CoV-2 first infect humans through natural zoonotic spillover (e.g. via the wildlife trade / Huanan Seafood Market) or through a research-related incident (a lab leak)?"
Your slice: The GENOME-STRUCTURE / ENGINEERING-SIGNAL data base — whether the SARS-CoV-2 sequence itself and its closest natural relatives look natural or engineered. Covers: the furin cleavage site (PRRA insertion, CGG-CGG arginine codons, out-of-frame insertion arguments); the BsaI/BsmBI restriction-site "synthetic fingerprint" / seamless-ligation ("no-see-um") argument; codon usage, RBD/ACE2-binding features; and comparison to the closest known natural relatives (RaTG13, RmYN02, BANAL-52/-236 Laos bat CoVs). Canonical anchors to find, verify, and snowball from (extend + chase rebuttals both ways): Andersen et al. 2020 Nature Medicine "The Proximal Origin of SARS-CoV-2" (the zoonosis-side genome argument); Bruttel, Washburne & Nordlund 2022 "Endonuclease fingerprint indicates a synthetic origin"; Zhou et al. 2020 Nature (RaTG13); Zhou et al. 2020 (RmYN02); Temmam et al. 2022 Nature (BANAL bat CoVs); Segreto & Deigin lab-origin hypothesis; and rebuttals to the synthetic-fingerprint claim. You MUST NOT mint: phylogenetics/dating/two-introduction papers (slice C); the DEFUSE proposal or other institutional DOCUMENTS (slice E — you own the sequence argument, not the grant record); market environmental (A), human-case (B), or wildlife/host/serosurvey (F) papers. You may READ shared hubs to find primaries, but only mint genome-structure/engineering-signal primaries.
Budget: write 11 `source` notes; read 22 sources properly; skim more via reviews/reference lists.
Mint every source node by piping markdown on stdin (body carries {{ID}}; title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/covid --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents. Use WebSearch/WebFetch (load them via ToolSearch) to find real sources with resolving URLs and real metadata (venue, date, citation count + asof, field).
Finish by writing your own orientation note `agent-notes/orientation/genome-structure.md` per the step-01 spec (your sources as wikilinks under topic headings, best-first; search_scope; exclusions; ~1 paragraph on the slice).
Return: the S-ids you created, the orientation-note path, and any gaps you hit.
```

### Searcher E — Institutional / circumstantial records

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/covid
Main question (verbatim): "Did SARS-CoV-2 first infect humans through natural zoonotic spillover (e.g. via the wildlife trade / Huanan Seafood Market) or through a research-related incident (a lab leak)?"
Your slice: The INSTITUTIONAL / CIRCUMSTANTIAL documentary record — the primary documents about WIV/EcoHealth research and about official investigations. Covers: the DEFUSE proposal (DARPA/EcoHealth/WIV, 2018) as a primary document; WIV research records, Shi Zhengli's coronavirus work, and the WIV virus database taken offline (Sept 2019); biosafety / BSL-2 practice records; the Mojiang miners (2012) and RaTG13 provenance; the reported Nov-2019 sick WIV workers (State Dept fact sheet); and US intelligence / oversight assessments (ODNI declassified assessment, FBI and DOE positions, Senate HSGAC/ interim reports, GAO). Canonical anchors to find, verify, and snowball from (extend + chase both sides' readings): the leaked DEFUSE proposal text; the 2021/2023 ODNI assessment on COVID-19 origins; the Senate HSGAC "Muddy Waters" report; State Dept Jan-2021 fact sheet; DRASTIC-surfaced documents; primary reporting/FOIA releases of EcoHealth-WIV grant records. Treat these as primary DOCUMENTS (records), not as reviews. You MUST NOT mint: the genome-structure/FCS/engineering SEQUENCE arguments (slice D — you own the documentary record, not the molecular claim); market env (A), human-case (B), phylogenetics (C), or wildlife/host/serosurvey (F) papers; and NOT the Rootclaim/Weissman/judge/Scott-Alexander debate artifacts (slice G). You may READ shared hubs to find primaries, but only mint institutional/documentary primaries.
Budget: write 12 `source` notes; read 24 sources properly; skim more via reviews/reference lists.
Mint every source node by piping markdown on stdin (body carries {{ID}}; title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/covid --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents. Use WebSearch/WebFetch (load them via ToolSearch) to find real sources with resolving URLs and real metadata (venue, date, citation count + asof, field).
Finish by writing your own orientation note `agent-notes/orientation/institutional-records.md` per the step-01 spec (your sources as wikilinks under topic headings, best-first; search_scope; exclusions; ~1 paragraph on the slice).
Return: the S-ids you created, the orientation-note path, and any gaps you hit.
```

### Searcher F — Wildlife trade, host range & serology

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/covid
Main question (verbatim): "Did SARS-CoV-2 first infect humans through natural zoonotic spillover (e.g. via the wildlife trade / Huanan Seafood Market) or through a research-related incident (a lab leak)?"
Your slice: The WILDLIFE-TRADE / HOST-RANGE / SEROLOGY data base — the animal side of the spillover question. Covers: what live wildlife was on sale in Wuhan markets before the pandemic (esp. raccoon dogs and other susceptible species); host-susceptibility / experimental-infection studies (raccoon dogs, mink, civets, hamsters, cats); the intermediate-host search and its (largely negative) animal-surveillance results; human pre-Dec-2019 serosurveys (incl. disputed early-antibody claims); farmed-wildlife serosurveys; and the SARS-1 / MERS spillover precedent (civet, dromedary camel; market-amplification pattern). Canonical anchors to find, verify, and snowball from (extend + chase both ways): Xiao et al. 2021 Sci Reports "Animal sales from Wuhan wet markets..."; raccoon-dog / mink susceptibility studies (e.g. Freuling et al.); China's farmed-wildlife and market-animal surveys; the WHO-China joint report animal-sampling section; SARS-1 civet intermediate-host papers (Guan et al. 2003). You MUST NOT mint: the Huanan ENVIRONMENTAL swab / metagenomic papers (slice A — you own animals-sold and susceptibility/serosurvey data, not the market surface swabs); human early-case epidemiology (B); phylogenetics (C); genome-structure (D); institutional documents (E); debate artifacts (G). You may READ shared hubs to find primaries, but only mint wildlife-trade/host/serology primaries.
Budget: write 11 `source` notes; read 22 sources properly; skim more via reviews/reference lists.
Mint every source node by piping markdown on stdin (body carries {{ID}}; title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/covid --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents. Use WebSearch/WebFetch (load them via ToolSearch) to find real sources with resolving URLs and real metadata (venue, date, citation count + asof, field).
Finish by writing your own orientation note `agent-notes/orientation/wildlife-host-serology.md` per the step-01 spec (your sources as wikilinks under topic headings, best-first; search_scope; exclusions; ~1 paragraph on the slice).
Return: the S-ids you created, the orientation-note path, and any gaps you hit.
```

### Searcher G — Debate & Bayesian-analysis record

```
Read /home/simonskade/workspace/.claude/skills/flf-epistack/steps/step-01-find-sources.md — it is your full instruction set.
Analysis directory: /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/covid
Main question (verbatim): "Did SARS-CoV-2 first infect humans through natural zoonotic spillover (e.g. via the wildlife trade / Huanan Seafood Market) or through a research-related incident (a lab leak)?"
Your slice: The DEBATE & BAYESIAN-ANALYSIS record — the primary artifacts of the reasoning itself. IMPORTANT exception to the step-01 "no reviews as nodes" rule: for THIS slice, mint each debate/analysis artifact as a `source` because it is the primary record of ITS OWN argument (set motivatedness/agenda accordingly). Covers: the Rootclaim COVID-origins analysis and Rootclaim's response to Scott Alexander (https://blog.rootclaim.com/covid-origins-debate-response-to-scott-alexander/); Michael Weissman's Bayesian analysis "An Inconvenient Probability" (https://michaelweissman.substack.com/p/an-inconvenient-probability-v57); judge Will's decision (https://drive.google.com/file/d/1YhmkYB32RpGsXvQTsX4xZ0Yul1wiwh8Z/view) and judge Eric's decision (https://drive.google.com/file/d/1aHlhPd-16EOabzXhiajT5PBm3uVCAG3T/view); Peter Miller's rebuttals / debate materials; Scott Alexander's ACX writeup (https://www.astralcodexten.com/p/practically-a-book-review-rootclaim); the three debate videos (https://www.youtube.com/watch?v=Y1vaooTKHCM , https://www.youtube.com/watch?v=KdORmvU8MLI , https://www.youtube.com/watch?v=d1dbfoK8nSE) and any transcripts; and the OTHER Bayesian analyses in the "six independent analyses spanning ~23 orders of magnitude" set (find and identify them — candidates include Weissman, Rootclaim/Wilf, and other named Bayesian estimates such as Quay & Muller, Chan/Ridley-adjacent, Demaneuf/de Maistre; verify which six the case refers to). Also include primary methodological/prior-setting pieces that argue how to weight this evidence. You MUST NOT mint empirical primaries — market env (A), human-case epi (B), phylogenetics (C), genome-structure (D), institutional documents (E), wildlife/host/serology (F). Snowball THROUGH these artifacts to surface empirical primaries, but leave minting those to the sibling slices; if you think a key empirical primary is uncovered, record it as a gap in your orientation note.
Budget: write 11 `source` notes; read 22 sources properly; skim more via reviews/reference lists.
Mint every source node by piping markdown on stdin (body carries {{ID}}; title never does):
  cat <<'EOF' | python3 /home/simonskade/workspace/.claude/skills/flf-epistack/scripts/create_node.py /home/simonskade/workspace/external-projects/flf-epistack/content/v1/analyses/covid --type source --title "Descriptive title, no id"
  ---
  id: {{ID}}
  type: source
  ...
  ---
  body
  EOF
Never hand-pick an id, and do not spawn subagents. Use WebSearch/WebFetch (load them via ToolSearch) to find real sources with resolving URLs and real metadata (venue, date, citation count + asof, field).
Finish by writing your own orientation note `agent-notes/orientation/debate-bayesian-record.md` per the step-01 spec (your sources as wikilinks under topic headings, best-first; search_scope; exclusions; ~1 paragraph on the slice).
Return: the S-ids you created, the orientation-note path, and any gaps you hit.
```
