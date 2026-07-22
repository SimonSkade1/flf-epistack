# Curation (step 2b)

- **initial_count:** 80 `source` nodes (77 live + 3 tombstones S-47/S-76/S-77, all `duplicate_of`).
- **curated_target_N:** 25
- **curated_count:** 26 = 25 rank/swap slots + 1 logged unrepresented-position include (S-30).
- **trust_baseline:** 0.75. The corpus clusters hard at trust 0.80 (a modal band of ~9 sources) and again at 0.90 (well-scrutinised foundational theory). The default 0.80 baseline lands *on* that mode, zeroing `combined_score` for a whole band of solid, coverage-critical sources on a knife-edge (S-44 Ord, S-50 Meade-Randall, S-79 Anthropic-Shadow, S-23, S-24, S-35, S-60, S-62). Dropping to 0.75 seats the cut just below that cluster: trust still dominates the ranking, but the 0.80-band discriminates on usefulness instead of collapsing to 0. 57/80 clear 0.75 (vs ~41 at 0.80) — healthy discrimination for a 25-slot cut, not "nearly everything."
- **scoring_rubric:** `trust_score` ∈ [0,1] = P(finding replicates); `usefulness` ≈ 1–5 log scale = how much the data moves the question if true. Cut key `combined_score = usefulness × (trust_score − 0.75)`; ≤ 0 ⇒ not curated (one logged exception).

## Curated set (26), by leg of the safety case
1. Institutional/safety-review: S-1, S-3
2. Production premise (extra-dim models + production theory): S-15, S-17, S-19, S-50
3. Evaporation (foundations + dissent): S-36, S-40, S-72, S-59
4. Astro survival / accretion / compact-star data: S-37, S-51, S-66, S-80, S-33
5. Cosmic-ray flux (4 independent instruments): S-75 (Auger), S-71 (TA), S-60 (HiRes), S-43 (Fly's Eye)
6. Alternative mechanisms: S-16, S-20 (vacuum decay), S-31 (monopole null-search), S-13 (strangelet)
7. Critics / risk-methodology / physics-dissent: S-44, S-30
8. Anthropic / observation-selection: S-79

## rank_departures (every swap + the include)
Prospective rank-25 (script, baseline 0.75, duplicates excluded): S-36,75,15,71,66,59,40,67,33,72,80,31,16,19,20,3,51,69,43,34,37,45,1,17,78.

Swaps applied by hand (5 out / 5 in) + 1 include:
- **−S-67 (rank 8) / +S-60:** S-67 is a 2nd Auger paper (D-2), correlated with curated S-75; swapped for HiRes S-60 (D-9) so the load-bearing cosmic-ray leg spans 4 *independent* instruments rather than 2 Auger + TA + Fly's Eye. Data-basis independence per spec point 3.
- **−S-69 (rank 18) / +S-44:** S-69 rests on the *identical* 215k-event Auger 2020 dataset as S-67 (PRD/PRL companion) — not independent evidence. Slot goes to S-44 (Ord et al., combined 0.20), the only risk-methodology critic clearing baseline and the source most directly answering the question's "what does it hinge on"; the critics side was entirely absent from the rank-25.
- **−S-34 (rank 19) / +S-13:** S-34 (Hawking 1974 letter) reports the same result as curated S-36 (Hawking 1975) — maximally correlated. Slot goes to S-13 (De Rujula–Glashow, combined 0.20) to seat the strangelet "other proposed mechanism" leg (shut out of the rank-25).
- **−S-45 (rank 22) / +S-50:** evaporation-theory already carries Hawking (S-36) + Page ×2 (S-40, S-72); dropped the surplus greybody paper to seat S-50 (Meade-Randall, combined 0.18), which fills the shut-out production-theory leg and carries the key hinge argument (LHC objects may be sub-semiclassical, so the Hawking-evaporation calc may not apply).
- **−S-78 (rank 25) / +S-79:** same anthropic-selection angle; S-79 ("Anthropic Shadow") applies the observation-selection correction with collider catastrophes as an explicit example class (load-bearing per orientation), more on-topic than S-78's general catastrophe-rate bound.
- **+S-30 (include, combined −1.58 ≤ 0):** the one sanctioned unrepresented-position include. Plaga is the sole peer-engaged primary arguing an LHC black hole could be dangerous (metastable scenario, rebutted by S-42); trust 0.30 (a checkable ~10²³ dimensional error) keeps every observation it emits heavily discounted downstream, but the adversarial "not put to rest on physics grounds" position now has a primary node for steps 3/6. (Dissent is also carried by S-59 evaporation-soft-spot and S-44 methodology; this add makes the physics-catastrophe claim itself explicit.)

## Accepted skews (Check 7)
The final cut still shows two angle/field shut-outs, both consciously accepted:
- **monopole-catalysis-theory (S-26/27/29) / field "particle physics / grand unification":** the monopole risk is represented by its two curated *empirical* nulls — S-31 (MoEDAL) and S-33 (Super-K). The Rubakov–Callan catalysis theory papers are the mechanism those searches test, not independent safety evidence; leaving them as the exclusion record is correct.
- **No data_basis over-representation remains:** after the Auger de-correlation, D-2 holds 1/26 of the cut (S-75); the largest angle clusters are evaporation-theory (4) and cosmic-ray-flux (4), both 15% ≪ 40%.

## D-node reconciliation (merges/retirements → data-bases/merged/, move-never-delete)
- **D-11 → D-2** (both Pierre Auger; survivor lowest id). Repointed S-64, S-67, S-69.
- **D-12 → D-9** (both HiRes). Repointed S-63.
- **D-7 retired → decomposed into [[D-10 - Sloan Digital Sky Survey spectroscopic dataset]], [[S-66 - Demorest et al. 2010 — Shapiro delay measurement of a two-solar-mass neutron star]], [[S-70 - Hansen et al. 2007 — Cooling of white dwarfs and the age of the globular cluster NGC 6397]], [[S-80 - Antoniadis et al. 2013, A Massive Pulsar in a Compact Relativistic Binary]]:** D-7 was a pre-existing grab-bag ("compact-star survival"). Repointed its sole referrer S-37 at the concrete member datasets so step 5 sees G&M's astro bound as correlated with the census papers (S-61 via D-10, S-66, S-70, S-80) that supply its empirical anchor, rather than hidden behind an orphan node. S-42 unchanged (→ S-37).
- Confirmed distinct (not merged): D-13 (original Fly's Eye) ≠ D-9/D-12 (HiRes); D-3 (TA), D-8 (AGASA) unique. D-14 (master cosmic-ray *flux spectrum*) kept separate from the instrument nodes D-2/3/8/9/13 by design — it is the shared basis capturing correlation among the four safety reviews (S-1/2/3/4), which rest on the aggregate spectrum, not one instrument.
- Merged/retired D nodes are tombstones (0 inbound by design, `merged_into`/`retired_into` pointer); Check-8's "≥1 inbound / no two live same dataset" applies to the 10 live D nodes, all of which are referenced.

## Defect fixes (would have broken step 3 locators)
- **S-50:** url corrected from arXiv:0802.2218 (Kanti lecture notes, wrong paper) → arXiv:0708.3017 (Meade & Randall, "Black Holes and Quantum Gravity at the LHC," JHEP 0805:003). Body/scores already described the correct paper; venue arXiv id also fixed.
- **S-74:** recorded url hep-ph/0507138 resolves to Koch, **Bleicher, Hossenfelder** 2005 "Black Hole **Remnants** at the LHC" (JHEP 0510:053) — a remnant-signature paper, NOT the "event-generator cross-sections" paper the immutable filename claims. Realigned authors, venue, body, angle (evaporation-theory) and scores (0.6 / 2.6) to the actual paper; url kept (it is correct for that paper); filename immutable, mismatch flagged in `motivatedness`.

## Script ranking output (baseline 0.75, --target-n 25)
```
baseline 0.75 | 80 scored | 57 clear the baseline | cut = top 25

RANKING  (* = in the prospective cut)
    id        comb  trust   use  title
  * S-36      0.60   0.90   4.0  Hawking 1975 — Particle Creation by Black Holes
  * S-75      0.54   0.90   3.6  Pierre Auger Collaboration 2025- spectrum across dec
  * S-15      0.53   0.90   3.5  Arkani-Hamed, Dimopoulos, Dvali 1998 — the ADD large
  * S-71      0.53   0.90   3.5  Abu-Zayyad et al. 2013- Telescope Array surface-dete
  * S-66      0.50   0.90   3.3  Demorest et al. 2010 — Shapiro delay measurement of
  * S-59      0.48   0.90   3.2  Unruh 1976 — Notes on black-hole evaporation
  * S-40      0.47   0.88   3.6  Page 1976 — Particle emission rates (nonrotating)
  * S-67      0.46   0.88   3.5  Aab et al. 2020 (PRL)- Auger spectral features
  * S-33      0.42   0.90   2.8  Super-Kamiokande 2012, GUT monopole search
  * S-72      0.42   0.90   2.8  Page 1976 — Particle emission rates II (rotating)
  * S-80      0.41   0.92   2.4  Antoniadis et al. 2013, Massive Pulsar
  * S-31      0.39   0.90   2.6  MoEDAL 2019, monopole trapping-detector search
  * S-16      0.38   0.90   2.5  Coleman & De Luccia 1980, vacuum decay + gravity
  * S-19      0.38   0.90   2.5  Randall, Sundrum 1999 — RS1
  * S-20      0.35   0.85   3.5  Degrassi et al. 2012, Higgs/vacuum stability NNLO
  * S-3       0.35   0.85   3.5  Busza, Jaffe, Sandweiss, Wilczek- RHIC review
    S-76      0.35   0.85   3.5  [duplicate of S-3]
  * S-51      0.35   0.90   2.3  Bondi 1952 — spherical accretion
  * S-69      0.33   0.88   2.5  Aab et al. 2020 (PRD)- Auger spectrum [identical dataset to S-67]
  * S-43      0.30   0.85   3.0  Bird et al. 1994- Fly's Eye spectrum
  * S-34      0.30   0.85   3.0  Hawking 1974 — Black hole explosions [= S-36 result]
  * S-37      0.29   0.82   4.2  Giddings & Mangano 2008 — astro implications
  * S-45      0.28   0.85   2.8  Harris, Kanti 2003 — (4+n)-D Hawking radiation
  * S-1       0.28   0.82   4.0  LSAG report- Safety of LHC Collisions
  * S-17      0.26   0.88   2.0  Antoniadis et al. 1998 — mm-to-fermi dimensions
  * S-78      0.26   0.82   3.7  Bostrom & Tegmark 2005, doomsday-catastrophe bound
    S-14      0.26   0.92   1.5  Coleman 1977, fate of the false vacuum
    S-22      0.25   0.85   2.5  Buttazzo et al. 2013, Higgs near-criticality
    S-46      0.25   0.85   2.5  Bird et al. 1995- 'Oh-My-God' event
    S-64      0.24   0.83   3.0  Abraham et al. 2008- Auger flux suppression
    S-21      0.23   0.90   1.5  Randall, Sundrum 1999 — RS2
    S-73      0.21   0.82   3.0  Auger-TA 2020- combined UHECR spectrum
    S-44      0.20   0.80   4.0  Ord, Hillerbrand, Sandberg- Probing the Improbable
    S-13      0.20   0.85   2.0  De Rujula & Glashow 1984- Nuclearites
    S-7       0.20   0.85   2.0  Konopinski, Marvin, Teller- LA-602
    S-57      0.19   0.85   1.9  Unruh 1976 — absorption cross section
    S-41      0.18   0.83   2.3  Linsley 1963- first >10^20 eV cosmic ray
    S-18      0.18   0.85   1.8  Turner & Wilczek 1982, vacuum metastable
    S-79      0.18   0.80   3.5  Ćirković, Sandberg & Bostrom 2010- Anthropic Shadow
    S-28      0.18   0.80   3.5  Dimopoulos, Landsberg 2001 — Black Holes at the LHC
    S-50      0.18   0.80   3.5  Meade, Randall 2008 — BH & Quantum Gravity at LHC
    S-60      0.17   0.80   3.4  Abbasi et al. 2008- HiRes GZK suppression
    S-61      0.16   0.82   2.3  Kepler et al. 2007 — SDSS WD mass distribution
    S-62      0.15   0.80   3.0  Jacobson 1991 — evaporation & ultrashort distances
    S-23      0.14   0.80   2.8  Isidori et al. 2007, gravitational corrections
    S-63      0.14   0.80   2.8  Abbasi et al. 2008-09- HiRes monocular flux
    S-26      0.14   0.82   2.0  Rubakov 1981, monopoles & proton decay
    S-38      0.14   0.82   2.0  Bekenstein 1973 — Black Holes and Entropy
    S-70      0.13   0.80   2.6  Hansen et al. 2007 — WD cooling / NGC 6397 age
    S-27      0.13   0.82   1.8  Callan 1982, disappearing dyons
    S-29      0.13   0.82   1.8  Callan 1982, dyon-fermion dynamics
    S-10      0.11   0.78   3.5  Koch, Bleicher, Stöcker- exclusion of BH scenarios
    S-47      0.11   0.78   3.5  [duplicate of S-10]
    S-24      0.10   0.80   2.0  Argyres et al. 1998 — BHs & sub-mm dimensions
    S-32      0.09   0.78   3.0  Giddings, Thomas 2002 — BH factories
    S-8       0.09   0.78   3.0  Witten 1984, cosmic separation of phases
    S-35      0.08   0.80   1.5  Wagner & Sancho v. DOE- LHC injunction
    S-2       0.03   0.76   2.5  CERN-2003-001- heavy-ion dangerous-events study
    S-9       0.03   0.76   2.5  Farhi & Jaffe 1984, strange matter
    S-12      0.00   0.75   2.5  strange-quark-matter search in lunar soil
    S-39      0.00   0.75   3.6  Kent- critical look at GCR risk assessments
    S-42      0.00   0.75   2.5  Giddings & Mangano 2008 — reply to Plaga
    S-48      0.00   0.75   2.0  Johnson- The Black Hole Case
    S-4      -0.03   0.74   3.0  Dar, De Rújula, Heinz- RHIC destroy planet?
    S-77     -0.03   0.74   3.0  [duplicate of S-4]
    S-6      -0.10   0.70   2.0  CERN SPC- endorsement of LSAG
    S-11     -0.13   0.70   2.5  STAR strangelet search at RHIC
    S-54     -0.13   0.70   2.6  Calogero- might a lab experiment destroy Earth
    S-58     -0.22   0.65   2.2  Posner- Catastrophe (accelerator chapter)
    S-52     -0.38   0.55   1.9  Hayashida et al. 2000- AGASA event list
    S-53     -0.39   0.60   2.6  Casadio, Harms 2000 — evaporation + extra dims
    S-74     -0.39   0.60   2.6  Koch, Bleicher, Hossenfelder 2005 — BH remnants [defect-fixed]
    S-5      -0.45   0.45   1.5  CERN FAQ- Will CERN generate a black hole
    S-49     -0.45   0.60   3.0  Takeda et al. 1998- AGASA beyond GZK
    S-68     -0.45   0.60   3.0  MacGibbon 1987 — Planck-mass relics
    S-56     -0.51   0.60   3.4  Helfer 2003 — Do black holes radiate
    S-55     -0.70   0.50   2.8  Takeda et al. 2003- AGASA spectrum
    S-65     -1.28   0.35   3.2  Belinski 1995 — No Hawking radiation
    S-30     -1.57   0.30   3.5  Plaga- catastrophic risk from metastable BHs [coverage include]
    S-25     -1.68   0.08   2.5  Rössler- Schwarzschild/CERN mini-BH risk

Prospective-cut skew flags (script, on the rank-25): angle production-theory /
strangelet-theory / monopole-catalysis-theory shut out; field GUT shut out.
All resolved or consciously accepted by the hand-swaps above.
```

- **generated:** 2026-07-21
