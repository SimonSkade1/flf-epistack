---
type: hypothesis-cluster
id: HC-15
hypotheses:
  - "[[H-31 - Nutritional-cohort diet-disease associations reflect cumulative bias and cannot support causal dietary claims]]"
  - "[[H-41 - The standard critiques of nutritional-cohort epidemiology are manageable, so well-conducted cohorts can support policy-relevant causal dietary inference]]"
  - "[[H-59 - Some intermediate epistemic standing]]"
exclusivity: "At most one epistemic pole is right: cohort associations cannot carry causal weight (H-31) or well-conducted cohorts can support policy-grade causal inference (H-41)."
exhaustive_by_construction: false
independence: "Method validity is logically prior to but numerically separable from any single effect estimate - it modulates how far cohort observations move the effect clusters (through source trust and likelihoods at steps 5/8), not those clusters' base rates - so the prior factorizes and depends_on is left empty."
depends_on: []
question: "Can observational nutritional-cohort associations support causal dietary (egg-health) claims?"
relevance: "The case framing's 'how can we tell / appropriate ways of knowing' - it conditions the weight of most other clusters' evidence."
---

![[H-31 - Nutritional-cohort diet-disease associations reflect cumulative bias and cannot support causal dietary claims]]

![[H-41 - The standard critiques of nutritional-cohort epidemiology are manageable, so well-conducted cohorts can support policy-relevant causal dietary inference]]

![[H-59 - Some intermediate epistemic standing]]

## Carving

The sub-question is whether observational nutritional-cohort associations can support causal dietary claims about eggs. H-31 (reform pole) says they reflect cumulative bias - residual confounding among near-universally correlated exposures, error-laden self-report, and selective analysis - and cannot carry causal weight; H-41 (defence pole) says these are manageable design/analysis problems and that well-conducted cohorts, triangulated with mechanism and intervention trials, can support policy-grade causal inference. At most one pole is right. Residual H-59 covers the intermediate standing - weak or qualitative causal support for large effects only. This meta-question cross-cuts every cohort-based cluster, but it enters downstream through source trust and likelihoods (how much a cohort observation is allowed to move a cluster), not through the other clusters' priors; those priors therefore still factorize, so depends_on is left empty and the coupling is handled at steps 5 and 8.

## Prior

```python
# HC-15 prior — can observational nutritional-cohort associations support causal egg-health claims? Members in
# HC-15.hypotheses order: [H-31 reform pole (cannot carry causal weight); H-41 defence pole (well-conducted cohorts
# support policy-grade causal inference with high confidence); H-59 residual (intermediate — weak/qualitative causal
# support for large effects only)]. Non-exhaustive, residual last.
#
# Evidence split. The prior rests on the field-level OUTSIDE-VIEW track record, which I mark used_for_prior on three
# edges (no correlation group on any): E-97 (O-69, near-universal food-mortality significance), E-98 (O-70, cohort HRs
# imply implausible lifelong magnitudes incl. -6 yr for one egg/day), E-99 (O-71, serum beta-carotene's strong
# protective cohort association RR 0.69 excluded by RCTs — the canonical cohort->RCT reversal). These are reference-class
# facts about the reliability of the field itself, so they belong in the prior. Left UNMARKED for step 8: the
# case-specific measurement-error / confounding mechanics that argue how MANAGEABLE the biases are — E-96 (E-value vs
# small egg HRs), CG-34 (O-91/92/93 OPEN under-reporting), E-103/104 (O-100/101 non-differential error, correctable).
#
# No-observation arguments (no_observation_arguments.py --cluster HC-15), all reaching H-41 (rule 6, reasoning not a
# term): A-36 (approved) replication across differently-confounded cohorts + sensitivity bounds make residual
# confounding bounded — but its own verdict flags the surviving UNIFORM healthy-user confounder as "exactly the residual
# worry for eggs"; A-37 (corrected) triangulation is the BEST-AVAILABLE policy basis, adequate only where corroborating
# mechanism/trial evidence is itself strong — downgraded from the original "sufficient for policy"; A-38 (approved)
# reverse causation is removable by early-event exclusion / lag. Net: these show the defence position is coherent and
# partly valid, but in their approved/corrected (hedged) forms they underwrite something nearer the intermediate H-59
# than H-41's strong "high-confidence policy-grade" claim — so they lift H-41 modestly and add mass to H-59.

# H-31 reform pole — the unit weight. What must hold: nutritional-cohort diet-disease signals are almost entirely
# cumulative bias and carry no causal weight. The marked track record (O-69/O-70/O-71) supports skepticism and anchors
# this pole at parity-or-above the defence. But H-31 is an ABSOLUTE claim ("cannot support causal claims at all"), and
# the field also has genuine hits (LDL/CVD, trans-fat, folate/NTD), so skepticism does not collapse fully onto it —
# much of the track-record's force is equally consistent with the intermediate H-59.
w_reform = 1.0  # H-31 anchor: field track record (O-69/70/71, used_for_prior) warrants skepticism, but the pole is absolute

# H-41 defence pole as odds vs reform. Supported by the three approved/corrected no-observation arguments
# (manageability of confounding, triangulation, reverse causation), but its bar is the STRONG one — "high degree of
# certainty for policy" — which A-37's correction explicitly declined to grant and A-36's surviving egg-relevant
# confounder undercuts. Slightly below reform a priori: for eggs the effects are tiny (HR~1.1), the regime where
# confounding dominates and the strong defence claim is least safe.
defence_vs_reform = 0.85  # would be right if the strong policy-grade claim is a bit less likely than blanket skepticism
w_defence = defence_vs_reform * w_reform  # H-41

# H-59 residual — the intermediate standing: cohorts give real but weak/qualitative causal support, reliable only for
# large effects, not the tiny egg HRs. Its own argued weight (rule 4), not a leftover. Both poles are overstated
# absolutes, and a contested meta-methodological question typically resolves between them; the hedged/corrected
# pro-defence arguments themselves land here. So the middle carries prior mass comparable to each pole — not dominating
# it (H-59 also competes with its own likelihood at step 8), but not sanded toward zero either.
w_residual = 1.0  # ~1:1 vs the reform anchor; the most defensible single reading a priori, co-plurality with H-31

prior("HC-15", [w_reform, w_defence, w_residual])
```
