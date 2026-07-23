# Curation note — step 2 (2b) — COVID origins

- **initial_count:** 91 (`S-1` … `S-91`, all primary sources from step 1)
- **curated_target_N:** 20
- **curated_count:** 23 (+3 over target; every extra is a logged both-sides / coverage / independent-basis include, below)
- **trust_baseline:** **0.50** — see reasoning below
- **scoring_rubric:** `trust_score` ∈ [0,1] = P(key finding replicates cleanly), from method/statistics/corroboration only (never from believing the conclusion); `usefulness` ≈ 1–5 log scale = how much the data would move the question *if true*. Cut key `combined_score = usefulness × (trust_score − baseline)`; ≤ 0 ⇒ not curated except logged contested-question includes.
- **generated:** 2026-07-23

## Baseline reasoning (the key judgment)

The default baseline **0.8** is wrong for this corpus. The evidence the debate actually turns on — Pekar two-introduction phylodynamics (0.60), Worobey geospatial (0.55), the Crits-Christoph/Bloom market re-analyses (0.68–0.78), Andersen *Proximal Origin* (0.50), Bruttel synthetic-fingerprint (0.25), the Bayesian analyses (0.30–0.57) — is **inherently mid-to-low trust because it is contested and mutually rebutted**, not because the data collection was sloppy. At baseline 0.8 the cut would keep only high-trust wet-lab animal-susceptibility studies, SARS/MERS precedents and documentary records, and drop the entire contested middle — a biased, non-representative set that answers a different question than the one asked.

I verified this empirically: the naive top-20 at **baseline 0.50** already shuts out case-geospatial, phylodynamics, genome-origin-argument, bayesian-synthesis, intel-assessment, and data-bases D-5 and D-6 (see the script's REPRESENTATION block at the bottom). Raising to 0.55 would additionally push Worobey (S-17, 0.55) and the WHO animal-surveillance (S-34, 0.55) below the line and create *more* forced exceptions; lowering further would let low-reliability material clear on rank. **0.50 sits just below the pool trust median (~0.60)**, so solidly-reliable sources (trust ≥ ~0.6) clear on rank while the contested-but-central sources (0.25–0.55) enter as explicitly-logged both-sides/coverage exceptions whose unchanged low `trust_score` keeps discounting them in every downstream Bayesian step. Inclusion ≠ endorsement.

## Data-basis reconciliation (D-merges)

Two duplicate pairs minted by blind parallel 2a scorers were merged (survivor = lowest id; absorbed node tombstoned with `merged_into` and moved to `data-bases/merged/`):

1. **D-9 → D-5** ("SARS-CoV-2 reference genome and closest natural relatives"). Repointed S-56, S-57, S-59 from `[[D-9]]` to `[[D-5]]`. D-5 (was `url: unknown`) adopted D-9's reference-genome URL (NC_045512.2) and its comparative-genomics bias note.
2. **D-7 → D-6** ("US intelligence-community COVID-origins assessments"). D-7 had zero inbound links; D-6 (was `url: unknown`) adopted D-7's ODNI URL. No source repoint needed.

Market-metagenomics cluster verified to converge on **D-1**: S-15/S-16/S-21, Crits-Christoph S-24/S-31/S-35, Bloom S-39/S-42/S-43, WHO/SAGO S-47/S-50 all carry `[[D-1]]` (S-31/S-35 additionally carry D-3 for the genome-tracing facet, S-47 additionally D-10 as a report section — accurate secondary correlation, kept). After repoints, **every `data_basis` link resolves** and all six live D-nodes (D-1, D-2, D-3, D-5, D-6, D-10) have ≥1 inbound link.

## Angle-vocabulary normalization (comparability across the 9 slices)

Scorer slices used comparable trust/usefulness numbers — the spread is content-driven (wet-lab animal studies & epidemiological precedents genuinely high; opinion/debate/institutional documents genuinely low), not scorer drift, so **no wholesale rescore**. Angle tags were folded into one consistent vocabulary so the skew check groups cleanly:

1. `molecular-dating` (S-2) → `phylodynamics`.
2. `epidemiological-precedent` split by argumentative structure: **zoonosis-precedent** (S-41/44/45 — market/farm amplification of a *true* zoonosis) vs **base-rate-precedent** (S-87/88/89/90 — first-detected cluster *disconnected* from true origin). These are argumentatively opposite (topup note flags this) and must not group together.
3. `genome-origin-argument` created for the engineering-signal debate (S-46, S-48, S-54, S-55, S-56, S-57, S-59, S-61, S-62), folding the coined `base-rate-argument` (S-54/S-59) and separating this contested cluster from neutral comparative genomics (`sequence-analysis`: progenitor/deleted-sequence/lineage/relative-characterization).

## Curated set (23) — id : one-line why

Zoonosis object-level: **S-16** China CDC market data (Nature, primary D-1) · **S-35** Crits-Christoph raccoon-dog reanalysis (Cell, pro-zoonosis D-1 pole) · **S-39** Bloom market reanalysis (skeptical D-1 pole) · **S-17** Worobey geospatial market-epicenter (central geospatial claim) · **S-1** Pekar two-introduction phylodynamics (primary D-3) · **S-13** Li NEJM early transmission/line-list (best D-2 early-case) · **S-19** wildlife-on-sale at Wuhan markets · **S-27** Dutch mink natural outbreak (host-susceptibility rep) · **S-52** BANAL-52 closest natural relative (pro-natural genome) · **S-44** SARS market-civet precedent · **S-34** WHO nationwide animal surveillance (sole D-10; intermediate-host-negative line).

Contested rebuttal / lab-leak object-level: **S-23** Stoyan geospatial critique (best-trust critique pole) · **S-22** Weissman phylo Bayesian-error critique · **S-46** Andersen *Proximal Origin* (anti-engineering genome pole, D-5) · **S-48** Bruttel synthetic fingerprint (strongest lab-engineering source, D-5) · **S-54** Segreto/Deigin chimera (best 'genome suggests lab' source) · **S-65** DEFUSE proposal (key institutional lab record, top rank) · **S-84** FBI/DOE IC lab-associated positions (best-trust intel, sole D-6).

Base-rate / debate synthesis: **S-87** Lloyd-Smith superspreading (base-rate foundation) · **S-88** Ebola-1976 detected-cluster≠origin precedent · **S-60** Rootclaim ~89%-lab Bayesian case · **S-64** Weissman 'Inconvenient Probability' (independent lab-leaning Bayesian) · **S-70** Judge Eric decision (zoonosis-leaning adjudication).

## rank_departures

**A. Curated despite `combined_score ≤ 0`** (sanctioned contested-question / debate-artifact exceptions; low trust keeps discounting downstream, inclusion ≠ endorsement):
- **S-22** (0.00) — phylo-critique rebuttal pole; only high-trust rebuttal of Pekar.
- **S-46** (0.00) — the central genome anti-engineering argument; D-5 anchor.
- **S-54** (−0.30) — best single 'genome structure suggests lab origin' source.
- **S-64** (−0.26) — independent lab-leaning Bayesian analysis.
- **S-60** (−0.60) — the debate's primary lab-leaning synthesis (Rootclaim).
- **S-48** (−1.00) — single strongest lab-engineering (synthetic-fingerprint) source.

**B. Curated with positive `combined_score` but below the naive top-20** (coverage/independence beats a marginal ranking point):
- **S-84** (0.55) intel-assessment + sole D-6 · **S-23** (0.77) geospatial-critique pole on D-2 · **S-1** (0.45) primary phylodynamics/D-3 · **S-70** (0.20) judge decision · **S-17** (0.22) central geospatial claim · **S-34** (0.15) sole D-10 + intermediate-host line.

**C. Non-curated despite ranking in/near the naive top-20** (dropped for redundancy / superseded-version / basis-dedup, each covered by a curated peer):
- **S-21** (1.44) raw-data release → analysis covered by S-16/S-35/S-39 (all D-1).
- **S-58** (1.20) RBD deep-mutational-scanning → peripheral; RBD-optimization argument in S-46.
- **S-41** (1.14) SARS-civet → redundant with curated S-44.
- **S-49** (1.05) RaTG13 characterization → natural-relatives via S-52.
- **S-9** (1.05) clinical-41 → early-clinical via S-13.
- **S-29** (1.05) / **S-28** (1.00) / **S-20** (0.84) susceptibility studies → host-susceptibility via S-27.
- **S-45** (1.00) MERS-camel → second zoonosis-precedent, S-44 is the representative.
- **S-81** (0.93) FOIA GOF records / **S-85** (0.84) House report → institutional lab-leak via S-65.
- **S-56** (0.88) FCS-absent fact → carried within S-46/S-48; genome cut kept to three.
- **S-66** (0.88) DARPA DEFUSE-review → same institutional episode as S-65.
- **S-31** (0.80) / **S-24** (0.72) → superseded Crits-Christoph versions, S-35 (Cell) curated.
- **S-90** (0.77) HIV base-rate → base-rate cluster via S-87/S-88.
- **S-77** (0.70) RaTG13/Mojiang addendum → institutional via S-65; D-5 kept to two.
- Positive-combined sources below ~0.7 (S-11, S-6, S-61, S-89, S-33, S-62, S-38, S-2, S-43, S-18, S-37, S-15, S-59, S-42, S-25, S-40, S-8, S-14, S-32, S-47, S-82, S-50, S-30, S-51, S-67, S-79, S-69, S-83, S-68) fall out naturally — their argument clusters are already represented; per-node reasons are on each file.

**Superseded version chains dropped** (best single version curated): China CDC S-15(preprint)→**S-16**(Nature); Crits-Christoph S-24(Zenodo)/S-31(bioRxiv)→**S-35**(Cell).

## Accepted skew (script flags on the *actual* 23-source cut)

No angle exceeds 13% of the cut; all six live data-bases are represented (max D-1/[] at 4/23 = 17%). Three angle shut-outs are **consciously accepted**:
1. **sequence-analysis** (0/23, 7 pool) — secondary genome sub-disputes (progenitor S-3/4/11, L/S-types S-5/6, intermediate-genomes S-7, RaTG13-characterization S-49), peripheral to the origin question; the live genome debate is represented by `genome-origin-argument` (S-46/48/54) and natural relatives by S-52.
2. **wet-lab-experiment** (0/23, 4 pool) — host-susceptibility is represented by S-27 (natural mink outbreak, `veterinary-outbreak`); the experimental-infection panels (S-20/28/29) and RBD-DMS (S-58) are redundant/peripheral.
3. **clinical-series** (0/23, 3 pool) — early-clinical is represented by S-13 (`case-linelist`, same D-2 early-case data); S-9/S-10 redundant, S-75 (Mojiang thesis) peripheral.

The naive-top-20 REPRESENTATION block below is the script's report on the *rank* cut, not on the curated set — it is the diagnostic that motivated the coverage-based departures above.

## Script ranking output (baseline 0.50, target-n 20) — pasted

```
baseline 0.50 | 91 scored | 66 clear the baseline | cut = top 20

RANKING  (* = in the prospective cut)
    id        comb  trust   use  title
  * S-65      1.52   0.90   3.8  Project DEFUSE proposal (EcoHealth Alliance to DARPA
  * S-21      1.44   0.82   4.5  China CDC raw metagenomic sequencing data release —
  * S-52      1.40   0.85   4.0  Temmam et al. 2022 Nature — BANAL Laos bat coronavir
  * S-58      1.20   0.90   3.0  Starr et al. 2020 — Deep mutational scanning of the
  * S-44      1.15   0.86   3.2  Kan et al. 2005 — SARS-CoV-like virus in market cive
  * S-41      1.14   0.88   3.0  Guan et al. 2003 — SARS-CoV-like viruses isolated fr
  * S-19      1.08   0.80   3.6  Xiao et al. 2021 — animal sales from Wuhan wet marke
  * S-49      1.05   0.80   3.5  Zhou et al. 2020 Nature — RaTG13, a bat coronavirus
  * S-9       1.05   0.80   3.5  Huang et al. 2020 Lancet — clinical features of the
  * S-27      1.05   0.85   3.0  Oreshkova et al. 2020 — SARS-CoV-2 outbreak on Dutch
  * S-29      1.05   0.85   3.0  Shi et al. 2020 — susceptibility of ferrets, cats, d
  * S-16      1.03   0.73   4.5  Liu, Gao et al. — Surveillance of SARS-CoV-2 at the
  * S-35      1.00   0.75   4.0  Crits-Christoph et al. — Genetic tracing of market w
  * S-87      1.00   0.90   2.5  Lloyd-Smith et al. 2005 — Superspreading and the eff
  * S-28      1.00   0.90   2.5  Sia et al. 2020 — pathogenesis and transmission of S
  * S-45      1.00   0.87   2.7  Reusken et al. 2013 — MERS-CoV neutralising antibodi
  * S-13      0.98   0.78   3.5  Li et al. 2020 NEJM — early transmission dynamics, f
  * S-39      0.98   0.78   3.5  Bloom — Association between SARS-CoV-2 and metagenom
  * S-88      0.98   0.85   2.8  International Commission 1978 — Ebola haemorrhagic f
  * S-81      0.93   0.87   2.5  FOIA-released NIAID-EcoHealth Alliance gain-of-funct
    S-56      0.88   0.85   2.5  Coutard et al. 2020 — Furin-like cleavage site absen
    S-66      0.88   0.85   2.5  DARPA's internal rejection review of the DEFUSE prop
    S-20      0.84   0.80   2.8  Freuling et al. 2020 — raccoon dog experimental SARS
    S-85      0.84   0.80   2.8  House Select Subcommittee staff report on EcoHealth
    S-31      0.80   0.70   4.0  Crits-Christoph et al. — Genetic tracing of market w
    S-90      0.77   0.85   2.2  Faria et al. 2014 — The early spread and epidemic ig
    S-23      0.77   0.72   3.5  Stoyan & Chiu 2024 JRSS-A — statistical critique of
    S-24      0.72   0.68   4.0  Crits-Christoph et al. — Genetic evidence of suscept
    S-10      0.70   0.78   2.5  Chen et al. 2020 Lancet — 99-case single-hospital de
    S-77      0.70   0.70   3.5  Nature addendum disclosing RaTG13's identity with th
    S-11      0.66   0.72   3.0  Débarre & Hensel 2025 — critical reexamination of th
    S-6       0.60   0.80   2.0  MacLean et al. 2020 — No evidence for distinct types
    S-61      0.60   0.70   3.0  Chambers, Abdullah Sadhu 2026 — Ancestral reconstruc
    S-89      0.59   0.72   2.7  Cowling et al. 2015 — Preliminary epidemiologic asse
    S-33      0.57   0.75   2.3  Damas et al. 2020 — comparative-structural ACE2 host
    S-62      0.57   0.72   2.6  Fuqing Wu 2023 — Updated analysis to reject the labo
    S-84      0.55   0.72   2.5  FBI and DOE 2023 agency-confidence positions on a la
    S-38      0.55   0.72   2.5  Chang et al. 2022 — Wuhan blood-donor serosurvey, Se
    S-2       0.54   0.68   3.0  Pekar et al. 2021 — Timing the SARS-CoV-2 index case
    S-1       0.45   0.60   4.5  Pekar et al. 2022 — molecular epidemiology of multip
    S-43      0.43   0.66   2.7  Bloom — Importance of quantifying the number of vira
    S-18      0.40   0.60   4.0  WHO-China joint study (2021) — early-case epidemiolo
    S-37      0.40   0.70   2.0  Deng et al. 2020 — 35-species serosurvey excludes in
    S-15      0.38   0.60   3.8  China CDC Research Square preprint — Huanan market e
    S-4       0.35   0.60   3.5  Bloom 2021 — Recovery of deleted deep sequencing dat
    S-59      0.30   0.65   2.0  Chan Zhan 2021-22 — Emergence of the Spike Furin Cle
    S-42      0.30   0.62   2.5  Débarre — What we can and cannot learn from SARS-CoV
    S-25      0.30   0.60   3.0  Esquivel Gomez et al. 2024 — recombination-aware phy
    S-40      0.30   0.60   3.0  Xiao K. et al. 2020 — isolation of SARS-CoV-2-relate
    S-8       0.30   0.60   3.0  Pekar et al. 2025 — reported intermediate lineage A-
    S-14      0.26   0.58   3.3  Worobey 2021 Science — dissecting the early COVID-19
    S-32      0.24   0.62   2.0  Débarre & Worobey 2024 — reply to Weissman, against
    S-47      0.22   0.60   2.2  WHO-China joint mission report — animal and environm
    S-17      0.22   0.55   4.3  Worobey et al. 2022 Science — geolocated case map na
    S-70      0.20   0.57   2.9  Judge Eric Stansifer's written decision
    S-82      0.20   0.60   2.0  DRASTIC investigation into the WIV pathogen database
    S-50      0.18   0.60   1.8  WHO SAGO statement on newly released China CDC metag
    S-3       0.18   0.55   3.5  Kumar et al. 2021 — An evolutionary portrait of the
    S-30      0.18   0.55   3.5  Weissman 2024 JRSS-A letter — proximity ascertainmen
    S-34      0.15   0.55   3.0  WHO-China joint report 2021 — animal and environment
    S-51      0.15   0.55   3.0  Zhou et al. 2020 Current Biology — RmYN02 natural S1
    S-67      0.14   0.55   2.8  Judge Will van Treuren's written decision
    S-79      0.13   0.55   2.5  Scott Alexander's ACX review of the Rootclaim debate
    S-69      0.10   0.55   2.0  ODNI Report on Potential Links Between WIV and COVID
    S-83      0.10   0.55   2.0  Judge Eric Stansifer's response to Michael Weissman
    S-68      0.09   0.55   1.8  ODNI declassified Updated Assessment on COVID-19 Ori
    S-22      0.00   0.50   4.0  Weissman 2026 — a fundamental Bayesian error in the   [below baseline]
    S-46      0.00   0.50   4.0  Andersen et al. 2020 — The Proximal Origin of SARS-C  [below baseline]
    S-26      0.00   0.50   3.0  Débarre & Worobey 2024 — reply to Stoyan & Chiu, rea  [below baseline]
    S-55      0.00   0.50   2.5  Deigin Segreto 2021 — SARS-CoV-2's claimed natural o  [below baseline]
    S-73      0.00   0.50   2.5  Peter Miller's written case against the lab-leak the  [below baseline]
    S-75      0.00   0.50   3.0  Li Xu's master's thesis on the 2012 Mojiang miners'   [below baseline]
    S-76      0.00   0.50   2.5  The Rootclaim vs. Peter Miller COVID-origins debate,  [below baseline]
    S-86     -0.05   0.48   2.6  Levin's NBER Bayesian assessment of COVID-19 origins  [below baseline]
    S-57     -0.12   0.45   2.5  Xia 2020 — Extreme genomic CpG deficiency in SARS-Co  [below baseline]
    S-78     -0.16   0.42   2.0  Washington Post report on 2018 State Department cabl  [below baseline]
    S-12     -0.17   0.45   3.5  McCowan 2025 — imbalanced hypothesis-testing framewo  [below baseline]
    S-91     -0.20   0.40   2.0  Chinese Embassy (US) 2021 — official rebuttal of Blo  [below baseline]
    S-36     -0.25   0.40   2.5  Zhang, Demaneuf et al. 2022 — within-market spatial   [below baseline]
    S-64     -0.26   0.42   3.2  Weissman's 'An Inconvenient Probability' Bayesian an  [below baseline]
    S-54     -0.30   0.40   3.0  Segreto Deigin 2021 — The genetic structure of SARS-  [below baseline]
    S-7      -0.30   0.40   3.0  Massey et al. 2023 — Unwarranted exclusion of interm  [below baseline]
    S-72     -0.30   0.38   2.5  Muddy Waters- The Origins of COVID-19 (Senate HELP G  [below baseline]
    S-5      -0.30   0.35   2.0  Tang et al. 2020 — On the origin and continuing evol  [below baseline]
    S-71     -0.30   0.35   2.0  Senate HELP Committee minority interim report on COV  [below baseline]
    S-80     -0.30   0.30   1.5  Daniel Filan's Bayesian analysis of COVID origins  [below baseline]
    S-53     -0.38   0.35   2.5  Nickels et al. — open letter requesting retraction o  [below baseline]
    S-63     -0.56   0.30   2.8  Rootclaim's response to Scott Alexander's ACX review  [below baseline]
    S-60     -0.60   0.30   3.0  Rootclaim's main COVID-19 origins analysis  [below baseline]
    S-74     -0.84   0.22   3.0  State Department Fact Sheet- Activity at the Wuhan I  [below baseline]
    S-48     -1.00   0.25   4.0  Bruttel, Washburne & VanDongen 2022-23 — Endonucleas  [below baseline]

REPRESENTATION OF THE (NAIVE TOP-20) CUT — diagnostic only; actual cut differs by the departures above
  angle:
    environmental-sampling            4/20 of cut, 11 in pool
    wet-lab-experiment                3/20 of cut, 4 in pool
    zoonosis-precedent                3/20 of cut, 3 in pool
    documentary-record                2/20 of cut, 7 in pool
    wildlife-survey                   2/20 of cut, 5 in pool
    base-rate-precedent               2/20 of cut, 4 in pool
    sequence-analysis                 1/20 of cut, 5 in pool
    clinical-series                   1/20 of cut, 2 in pool
    veterinary-outbreak               1/20 of cut, 1 in pool
    case-linelist                     1/20 of cut, 1 in pool
    case-geospatial                   0/20 of cut, 5 in pool  <-- shut out
    genome-origin-argument            0/20 of cut, 4 in pool  <-- shut out
    phylodynamics                     0/20 of cut, 4 in pool  <-- shut out
    bayesian-synthesis                0/20 of cut, 4 in pool  <-- shut out
    intel-assessment                  0/20 of cut, 3 in pool  <-- shut out
  data_basis (naive top-20):
    D-1 4/20 · D-3 1/20 · D-2 1/20 · D-5 0/20 (shut out) · D-6 0/20 (shut out)
```
