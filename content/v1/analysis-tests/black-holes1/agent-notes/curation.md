# Curation notes (step 2b)

- initial_count: 23
- curated_target_N: 5
- curated_count: 5
- trust_baseline: 0.6 - theory/argument-heavy corpus, trust caps ~0.85-0.90; default 0.8 leaves only a 0.05-0.10 band so usefulness is swamped and the ranking degenerates to raw trust (it curated two low-usefulness high-trust items, S-19/S-20). 0.6 restores a usefulness-driven ordering while still cutting the weak tail.
- scoring_rubric: trust_score = P(finding survives clean replication / expert scrutiny), [0,1]; usefulness = log-scale ~1-5 of how much the data moves the question if true; combined_score = usefulness x (trust_score - baseline).
- D-node reconciliation: no-op; only D-1 exists (scorer 2 minted none), no duplicates.

## Final cut
S-14, S-5, S-13, S-1, S-23.

## rank_departures
- S-1 (0.59, rank 7) included over S-21 (0.70, rank 5): S-1 is the strongest affirmative astrophysical safety argument and the only curated source resting on D-1 / cosmic-ray-survival - the empirical hinge the question asks about. Script flagged D-1 and cosmic-ray-survival as shut out of the cut; this swap fixes both.
- S-21 dropped: risk-methodology critique redundant with retained S-23 (which attacks the same empirical backbone more specifically).

## Accepted skew
None outstanding after the swap. S-5 (raw spectrum) and S-1 (argument resting partly on S-5/D-1) are mildly correlated but sit at different layers (data vs safety argument); acceptable given coverage need.

## Script ranking (baseline 0.6)
```
baseline 0.60 | 23 scored | 18 clear the baseline | cut = top 5

RANKING  (* = in the prospective cut)
    id        comb  trust   use  title
  * S-14      1.12   0.85   4.5  Hawking 1975 - Particle creation by black holes
  * S-5       0.90   0.90   3.0  Measurement of the cosmic-ray energy spectrum using 
  * S-13      0.88   0.85   3.5  Arkani-Hamed, Dimopoulos and Dvali 1998 - The hierar
  * S-23      0.80   0.80   4.0  Is a doomsday catastrophe likely - the observer-sele
  * S-21      0.70   0.80   3.5  Probing the Improbable - risk-argument flaw ceiling 
    S-11      0.60   0.75   4.0  Dimopoulos and Landsberg 2001 - Black Holes at the L
    S-1       0.59   0.74   4.2  Astrophysical implications of hypothetical stable Te
    S-15      0.55   0.82   2.5  Meade and Randall 2008 - Black holes and quantum gra
    S-3       0.53   0.79   2.8  Review of speculative disaster scenarios at RHIC
    S-12      0.51   0.75   3.4  Giddings and Thomas 2002 - High-energy colliders as 
    S-8       0.50   0.80   2.5  Search for stable strange quark matter in lunar soil
    S-20      0.50   0.85   2.0  LA-602 (1946) - Ignition of the Atmosphere with Nucl
    S-10      0.44   0.82   2.0  Spectropolarimetric survey of hydrogen-rich white dw
    S-19      0.42   0.88   1.5  Sancho v. U.S. Department of Energy - the Wagner-San
    S-2       0.40   0.76   2.5  How stable is our vacuum (Hut and Rees 1983)
    S-4       0.31   0.74   2.2  Will relativistic heavy-ion colliders destroy our pl
    S-22      0.30   0.72   2.5  A critical look at risk assessments for global catas
    S-7       0.10   0.63   3.3  LSAG 2008 - Review of the Safety of LHC Collisions
    S-17      0.00   0.60   3.0  Comments on claimed risk from metastable black holes  [below baseline]
    S-9      -0.09   0.55   1.8  Blaizot et al. 2003 - Study of Potentially Dangerous  [below baseline]
    S-6      -0.30   0.40   1.5  CERN FAQ - Will CERN generate a black hole  [below baseline]
    S-16     -0.80   0.40   4.0  Potential catastrophic risk from metastable quantum   [below baseline]
    S-18     -1.68   0.12   3.5  Rössler's Abraham-solution critique of LHC black-hol  [below baseline]

REPRESENTATION OF THE CUT
```

- generated: 2026-07-20
