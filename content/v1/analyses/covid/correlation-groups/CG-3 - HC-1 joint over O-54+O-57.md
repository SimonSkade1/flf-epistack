---
type: correlation-group
id: CG-3
to: "[[HC-1 - Origin of SARS-CoV-2 — natural zoonosis vs research-related incident]]"
members:
  - "[[E-60 - O-54 × HC-1 — SARS-CoV-1 natural market spillover precedent]]"
  - "[[E-61 - O-57 × HC-1 — natural stepwise human-adaptation of a sarbecovirus]]"
---

Joint likelihood for correlated observations O-54, O-57 (shared basis: S-44). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-3 (HC-1) — ONE joint estimate over members E-60 + E-61: both observations rest on S-44 (Kan et al.
# 2005), so they are one witness (rule 1). Members in HC-1.hypotheses order:
# [H-41 natural zoonosis, H-42 unmodified-collection lab leak, H-43 engineered lab leak, H-44 residual].
# The pattern judged whole: SARS-CoV-1 (2004) demonstrably emerged via a LIVE-ANIMAL-MARKET zoonosis —
# 91/91 civets + 15/15 raccoon dogs positive at Xinyuan with a farm-negative within-owner control locating
# infection at the market (O-54, A-56 approved), and a graded 0 -> 2-7 -> 16-27 SNV ladder from an
# animal-borne prototype toward the human epidemic genotype documenting natural stepwise human-adaptation
# of a sarbecovirus AT the market (O-57, A-57 approved). This is a PRECEDENT / base rate: the exact
# wildlife-market spillover-plus-in-market-adaptation mechanism has already happened once for a sarbecovirus
# in China. A demonstrated natural-market pathway is more expected under, and more consonant with, the
# natural-zoonosis hypothesis for SARS-CoV-2 than under the lab members. Modest magnitude — a single
# precedent about a DIFFERENT virus, so it tilts, it does not decide. Arguments A-56/A-57 set direction
# (which member the precedent favours and that natural adaptation needs no lab), not a multiplicative term
# (rule 5). Anchored on H-41 = 1; other members priced as ratios to it (rule 7).
lik_precedent_H41 = 1.0   # anchor: a real, demonstrated natural live-market sarbecovirus emergence with
                          # in-market adaptation is exactly the world H-41 describes — the observation is
                          # most consonant with, and most expected under, natural market spillover.
lik_precedent_H42 = 0.85  # ~0.85x: H-42 SHARES H-41's natural, unmodified virus, so O-57's demonstration
                          # that human-adaptation happens naturally is fully compatible with it and does
                          # not discriminate; only O-54's market-amplification/location signal points modestly
                          # away from a research-collection route toward an ordinary market route. Close to
                          # the anchor, slightly below.
lik_precedent_H43 = 0.65  # ~0.65x: the member the precedent cuts against most. O-57's graded natural
                          # SNV ladder directly rebuts the premise central to engineered H-43 that a
                          # sarbecovirus's human-adaptation required laboratory manipulation, and a
                          # demonstrated natural-market pathway makes the engineered story relatively less
                          # needed. Held modest (not lower) — one precedent, about SARS-CoV-1 not SARS-CoV-2.
lik_precedent_H44 = 0.8   # ~0.8x: unlisted/hybrid origin, unconstrained — a natural-market sarbecovirus
                          # precedent neither predicts nor forbids it. Middling, near the anchor; lower
                          # would assert an unlisted origin makes such a precedent surprising, which I don't know.
t_precedent = 0.86        # cap = trust_score of S-44 = 0.86 (both O-54, O-57 via S-44), taken at the cap:
                          # the raw data are a large-n clean binary market/farm contrast plus tabulated SNV
                          # counts. The softer dN/dS "adaptation" inference lives in A-57's hedged reading,
                          # which enters as direction only, so it caps t but does not force a markdown below it.
evidence("HC-1", ["O-54", "O-57"], [lik_precedent_H41, lik_precedent_H42, lik_precedent_H43, lik_precedent_H44], t=t_precedent)
```
