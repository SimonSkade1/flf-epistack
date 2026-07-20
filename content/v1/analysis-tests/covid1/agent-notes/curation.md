# Curation (step 2b)

- **initial_count**: 17 (S-1 … S-17)
- **curated_target_N**: 5
- **curated_count**: 5 (S-2, S-4, S-11, S-12, S-15)
- **trust_baseline**: 0.5 — at the default 0.8 only S-11 cleared (1 of 17); the corpus is weak relative to 0.8, so per the corpus-fit rule the baseline was lowered to 0.5, at which 12 sources clear and the ranking discriminates. All `combined_score` values recomputed at 0.5.
- **scoring_rubric**: `trust_score` ∈ [0,1] = P(finding replicates cleanly); `usefulness` ≈1–5 log scale = how much the data moves the question if true; `combined_score = usefulness × (trust_score − 0.5)`, ≤ 0 ⇒ not curated.
- **rank_departures**: none. The top 5 by `combined_score` already cover both sides (research-related: S-15; zoonosis: S-12, S-2, S-4; neutral/foundational: S-11) and rest on 5 distinct data-bases (S-12, S-15, S-11, D-2, S-4) — no dataset monoculture. Script reported no strong skew at baseline 0.5, so no swap or unrepresented-position include was needed.
- **D-node reconciliation**: D-4 (scorer A) merged into D-1 (scorer B) — same SARS-CoV-2 reference-genome / early-GISAID dataset. S-9 `data_basis` repointed D-4 → D-1; D-4 tombstoned (`merged_into: [[D-1 …]]`) and moved to `data-bases/merged/`. D-2 (Huanan swabs) and D-3 (Worobey case-geolocation) confirmed distinct, left live.
- **generated**: 2026-07-20

## Script ranking output (baseline 0.5)

```
baseline 0.50 | 17 scored | 12 clear the baseline | cut = top 5

RANKING  (* = in the prospective cut)
    id        comb  trust   use  title
  * S-12      1.20   0.80   4.0  Temmam 2022 Nature - BANAL bat coronaviruses from La
  * S-15      1.20   0.80   4.0  DEFUSE proposal 2018 - leaked EcoHealth Alliance-WIV
  * S-11      1.05   0.85   3.0  Zhou 2020 Nature - first report of RaTG13, SARS-CoV-
  * S-2       0.88   0.72   4.0  Liu 2023 Nature - China CDC environmental and animal
  * S-4       0.84   0.80   2.8  Xiao et al. 2021 Scientific Reports - Wildlife speci
    S-5       0.63   0.68   3.5  Bloom 2021 MBE - Recovered deleted early-Wuhan seque
    S-7       0.45   0.65   3.0  Stoyan & Chiu 2024 JRSS-A - Statistical critique of
    S-13      0.45   0.60   4.5  Pekar, Worobey, Wertheim et al. 2022 Science - linea
    S-3       0.40   0.60   4.0  Crits-Christoph, Débarre, Worobey et al. 2024 Cell -
    S-9       0.40   0.60   4.0  Andersen 2020 Nature Medicine - Proximal Origin argu
    S-1       0.32   0.58   4.0  Worobey 2022 Science - Huanan market case geolocatio
    S-8       0.13   0.55   2.5  Reuters 2021 (Dwyer) - China gave WHO team only summ
    S-6       0.00   0.50   3.5  WHO-China Joint Report 2021 - Field mission epi-curv  [below baseline]
    S-16     -0.15   0.45   3.0  US House Select Subcommittee on the Coronavirus Pand  [below baseline]
    S-17     -0.25   0.40   2.5  Bostickson & Demaneuf (DRASTIC) 2021 - investigation  [below baseline]
    S-10     -0.80   0.30   4.0  Segreto & Deigin 2021 BioEssays - argues SARS-CoV-2'  [below baseline]
    S-14     -1.35   0.20   4.5  Bruttel, Washburne & VanDongen 2022 bioRxiv preprint  [below baseline]

REPRESENTATION OF THE CUT — No strong skew detected in the prospective cut.
  field: virology/genomics 2/5; biosafety-policy 1/5; environmental-virology 1/5; wildlife-trade 1/5
  angle: wildlife-survey 2/5; institutional-doc 1/5; sequence-recovery 1/5; market-sampling 1/5
  data_basis: S-12, S-15, S-11, S-4 each 1/5; D-2 1/5 (3 in pool)
```
