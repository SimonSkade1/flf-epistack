---
type: hypothesis-cluster
id: HC-11
hypotheses:
  - "[[H-10 - Early stepwise egg introduction causally prevents egg allergy in high-risk infants]]"
  - "[[H-46 - Early egg introduction does not causally prevent allergy]]"
exclusivity: "Either early introduction induces tolerance and causally prevents allergy (H-10) or it is merely safe/tolerated with the reduced incidence non-causal (H-46); exactly one holds."
exhaustive_by_construction: true
independence: "Allergy prevention is an immunological channel unrelated to the cardiometabolic and TMAO clusters; its prior is independent."
depends_on: []
question: "Does early controlled egg introduction causally prevent egg allergy in high-risk (eczema) infants?"
relevance: "A 'what else to pay attention to' benefit channel - a rare hard-endpoint RCT in the corpus."
---

![[H-10 - Early stepwise egg introduction causally prevents egg allergy in high-risk infants]]

![[H-46 - Early egg introduction does not causally prevent allergy]]

## Carving

The sub-question is whether early controlled egg introduction causally prevents egg allergy in high-risk eczema infants. Two exhaustive answers: a true tolerogenic prevention effect (H-10) or no causal prevention - safe and tolerated, but the reduced incidence is not itself the causal effect (H-46, constructed). One or the other holds, so exhaustive_by_construction is set and no residual is needed. Analysis-failure mode: if the trial's large risk reduction (confirmed egg allergy 8% versus 38%) were driven by differential dropout of already-reacting infants or by the concurrent eczema-control co-intervention rather than by induced oral tolerance, the analysis would favour H-10 when H-46 is correct - the failure favours the constructed null. H-46 is minted as the complement no curated paper states.

## Prior

```python
# HC-11 prior -- does early controlled egg introduction CAUSALLY prevent egg allergy in high-risk (eczema) infants?
# Members in HC-11.hypotheses order:
#   [H-10 early stepwise heated-egg introduction CAUSALLY prevents egg allergy (induced oral tolerance),
#    H-46 early introduction is safe/tolerated but does NOT causally prevent allergy (the reduced incidence is
#         non-causal: differential dropout of already-reacting infants, the concurrent eczema co-intervention,
#         or protocol-bound non-generalizability)].
# exhaustive_by_construction: true, exactly 2 members, NO residual (rule 4 does not apply).
# No no-observation arguments exist for this cluster (no_observation_arguments.py --cluster HC-11 -> none).
# Evidence split: NO inbound edge is marked used_for_prior. Both edges are the PETIT trial itself -- the
# confirmed-allergy 8% vs 38% result (O-20, E-5) and the acute-reaction/admission pattern that bounds the dropout
# artefact (O-21, E-7), together CG-31 -- and both DISCRIMINATE H-10 vs H-46, so they are left for step 8. The
# prior rests on the OUTSIDE VIEW from the broader early-allergen-introduction literature (independent of PETIT,
# which postdates the meta-analysis cited below), before the PETIT result is read.

# H-10 -- causal tolerance induction. Reference class: the post-LEAP early-introduction paradigm. LEAP (peanut)
# showed an ~81% relative reduction in peanut allergy with early introduction (Du Toit et al., NEJM 2015), and a
# meta-analysis of early EGG introduction found a protective effect on egg allergy at moderate certainty.
egg_meta_rr = 0.56   # RR 0.56 (95% CI 0.36-0.87) for egg allergy with egg introduction at 4-6 mo, moderate certainty; per Ierodiakonou et al., JAMA 2016 (pre-PETIT, independent of O-20)
# An RR<1 whose CI excludes 1 is moderate-certainty evidence the effect is real, but "moderate certainty" plus a
# mixed egg-trial base (several null/complicated egg-introduction RCTs, and real reaction-at-introduction risk)
# leaves genuine doubt whether the meta-analytic effect is causal tolerance induction vs artefact/non-generalizable.
p_causal_given_metaeffect = 0.62   # credence the protective egg-introduction signal reflects genuine causal tolerance induction in high-risk infants (H-10)
w_causal = p_causal_given_metaeffect   # H-10

# H-46 -- safe but non-causal. Argued on its OWN terms (not as 1 - w_causal) so a skeptic can override it
# independently: base rate that a moderate-certainty prevention signal for a high-risk-only protocol proves
# artefactual (differential dropout of already-reacting infants) or fails to generalize beyond the
# eczema-controlled regimen. Kept non-trivial by the mixed egg-introduction replications.
p_noncausal = 0.40   # own estimate of the artefactual / non-generalizable pole (H-46)
w_noncausal = p_noncausal   # H-46

prior("HC-11", [w_causal, w_noncausal])
```

