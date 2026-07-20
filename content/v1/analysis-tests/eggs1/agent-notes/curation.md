# Curation note — step 2b

- initial_count: 20 scored sources (S-1..S-20)
- curated_target_N: 10
- curated_count: 10
- trust_baseline: 0.55 — weak nutrition corpus (most trust_score < 0.8, capped by small-n surrogate RCTs, FFQ error, and industry funding); the default 0.8 would clear almost nothing, so 0.55 is set as a corpus-fit floor. 18/20 clear it; 2 fall below (S-6, S-2).
- scoring_rubric: trust_score ∈ [0,1] = P(finding survives clean replication, from method/statistics not conclusion); usefulness ~1–5 log scale = how much the data moves the question if true. combined_score = usefulness × (trust_score − 0.55); ≤ 0 ⇒ not curated.

## D-node reconciliation
PHS was minted twice (D-4 from S-4, D-9 from S-14) = same dataset. Merge already in place: survivor D-4, D-9 moved to data-bases/merged/ with `merged_into: [[D-4]]`, S-14 `data_basis` points to [[D-4 - Physicians' Health Study (PHS) cohort|D-4]]. No source references D-9. No other live D-pair duplicates.

## Comparability
Two 2a slices, trust numbers comparable (no systematic high/low offset), no blatant outlier rescored. Angle vocab differed slightly between scorers (`feeding-rct-lipids`/`feeding-rct-mechanism` vs `rct-surrogate`) but maps cleanly onto surrogate-RCT vs hard-endpoint; left as-is for the test run.

## The cut
Curated (10): S-11, S-8, S-16, S-13, S-9, S-12, S-1, S-14, S-5, S-19.
- Design mix: 5 hard-endpoint cohort (S-11, S-16, S-13, S-9, S-14) + 5 surrogate RCT/feeding (S-8, S-12, S-1, S-5, S-19).
- Data-basis spread: all 10 rest on distinct bases (D-7, S-8, D-10, D-8, D-1/D-2/D-3, S-12, S-1, D-4, S-5, S-19) — no shared basis inside the cut, full independence.

## rank_departures
- S-19 in / S-10 out (only skew swap): the natural top-10 shut out the `feeding-rct-mechanism` angle (0/3) — the LDL-C-mismeasurement / cholesterol-absorption hypothesis. Swapped the marginal cut member S-10 (0.30, controlled-feeding-doseresponse, an angle already held by S-8) for S-19 (0.25, mechanism, self-linked). Trades 0.05 ranking for a distinct method; preserves 5/5 design mix and data-basis independence.
- Accepted skew: `cohort-hard-endpoint` at 5/10 (flagged >40%) is retained — it is the design class that most directly answers a habitual-consumption health-outcome question, and the 5 cohorts are mutually independent datasets, so no false-confidence risk.

## Script ranking output
```
baseline 0.55 | 20 scored | 18 clear the baseline | cut = top 10
  * S-11   1.00  0.80  4.0  Dehghan 2020 PURE
  * S-8    0.90  0.80  3.6  Keys metabolic-ward dose-response
  * S-16   0.70  0.75  3.5  Key 2019 EPIC
  * S-13   0.60  0.70  4.0  Qin 2018 CKB
  * S-9    0.60  0.70  4.0  Drouin-Chartier 2020 BMJ
  * S-12   0.57  0.78  2.5  Ingestion of egg raises LDL (Lancet 1984)
  * S-1    0.48  0.70  3.2  DIABEGG RCT
  * S-14   0.46  0.68  3.5  Djoussé 2008 PHS
  * S-5    0.43  0.68  3.3  Katan responders
  * S-10   0.30  0.65  3.0  Ginsberg dose-response  [SWAPPED OUT]
    S-19   0.25  0.65  2.5  whole-egg cholesterol absorption  [SWAPPED IN]
    S-7    0.20  0.60  4.0  Zhong 2019 JAMA
    S-18   0.17  0.60  3.5  Nakamura NIPPON DATA80
    S-4    0.17  0.60  3.5  egg->T2D dose-response
    S-3    0.16  0.60  3.3  NHS diabetic cohort
    S-17   0.15  0.60  3.0  HDL function/antioxidants
    S-20   0.15  0.60  3.0  hyperlipidemic FMD RCT
    S-15   0.12  0.60  2.5  low-carb HDL feeding
    S-6   -0.16  0.50  3.2  ApoE polymorphism  [below baseline]
    S-2   -0.26  0.42  2.0  egg vs oatmeal  [below baseline]
Skew flags: cohort-hard-endpoint (accepted), feeding-rct-mechanism shut-out (fixed by S-19 swap).
data_basis: every basis 1/10 — no data-basis skew.
```

- generated: 2026-07-20
