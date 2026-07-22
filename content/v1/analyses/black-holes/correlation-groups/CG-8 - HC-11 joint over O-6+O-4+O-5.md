---
type: correlation-group
id: CG-8
to: "[[HC-11 - Origin of the near-criticality of the Higgs potential]]"
members:
  - "[[E-20 - O-6 × HC-11 — lambda and its beta function both nearly vanish at the Planck scale]]"
  - "[[E-22 - O-4 × HC-11 — measured Higgs mass sits just below the absolute-stability boundary]]"
  - "[[E-23 - O-5 × HC-11 — parameters fall inside the narrow metastable wedge of the phase diagram]]"
---

Joint likelihood for correlated observations O-6, O-4, O-5 (shared basis: D-1). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-8 (HC-11) — ONE joint estimate over members E-20 + E-22 + E-23 (O-6, O-4, O-5). All three rest on the
# same measured SM parameters D-1 (top + Higgs mass world averages) via S-20 (rule 1), so they are ONE
# witness, not three: O-6 (lambda(M_Pl) and beta_lambda both near zero), O-4 (Mh ~2 sigma below the
# absolute-stability boundary) and O-5 (parameters inside the narrow metastable wedge) are three facets of a
# single fact — the measured Higgs potential sits near-critical, on the stability/metastability phase
# boundary. Priced as ONE pattern. Members in HC-11.hypotheses order [H-6 principle, H-43 coincidence];
# cluster is exhaustive_by_construction, so no residual. Anchored on H-6 = 1 (rule 7); H-43 priced as the
# ratio "how much less expected is THIS near-critical draw if it were an unforced coincidence?"
#
# THE CRUX is P(exactly-near-critical | principle) vs P(same | coincidence). Two subtleties bound how far
# this witness can carry:
#  (i) anthropic — a habitable universe needs only a vacuum that has not already decayed (long-lived); it
#      does NOT need one sitting *near the boundary*. A deep-stable vacuum is equally habitable, so anthropic
#      selection does NOT explain the proximity. The near-criticality therefore stays a genuine surprise
#      under H-43 even after conditioning on our existence — this is what lets the pattern favour H-6 at all.
#  (ii) look-elsewhere / measure — "near-critical" is a partly post-hoc target, and the prior measure over
#      (Mt, Mh) that fixes how improbable a coincident draw is, is ill-defined. This caps the update: I
#      cannot push P(near-critical | coincidence) arbitrarily low, because the size of the "surprising"
#      region is not objectively pinned.

lik_principle = 1.0   # anchor. H-6 says a dynamical/statistical attractor places the parameters on the
                      # critical line, so the whole near-critical pattern is the expected outcome. Not
                      # perfect: H-6 is a broad family and its sharpest variants (lambda(M_Pl)=0 exactly)
                      # are disfavoured at 2 sigma (E-20 nuance), leaving proximity-attractor variants
                      # intact — hence anchor at 1, not "overwhelming fit".

lik_coincidence = 0.3 # 0.3x as expected as under H-6: an unforced draw landing this close to the boundary
                      # is a priori surprising (E-22: the mass could have fallen anywhere in its range;
                      # E-23: the metastable wedge gets no special weight). Not lower, because of subtlety
                      # (ii) — the target region and parameter measure are ambiguous, so the coincidence is
                      # improbable but not extravagantly so (few-percent-of-plausible-range order). Not
                      # higher, because subtlety (i) blocks the usual anthropic escape. Net ~3x odds toward
                      # H-6 — a modest witness, matching that H-6's mechanisms are speculative with no
                      # confirmed analog (prior already shades toward the coincidence null).

t_nearcrit = 0.7      # cap = min trust_score over {O-6, O-4, O-5} = 0.85 (all via S-20). Docked below the
                      # cap for A-6 (approved): the near-criticality is a ~2-sigma verdict hinging on the
                      # top-mass input (Mt below ~171 GeV would restore lambda(M_Pl) >= 0 and dissolve the
                      # explanandum) and on assuming no new physics / Planck-threshold corrections below
                      # M_Pl. That is a specific, named weakness in the step from raw data (Mt, Mh) to the
                      # stated "near-critical" observation, so t sits below reliability, not at it.

evidence("HC-11", ["O-6", "O-4", "O-5"], [lik_principle, lik_coincidence], t=t_nearcrit)
```
