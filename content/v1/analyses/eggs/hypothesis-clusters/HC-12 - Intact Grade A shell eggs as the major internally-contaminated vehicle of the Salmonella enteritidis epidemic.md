---
type: hypothesis-cluster
id: HC-12
hypotheses:
  - "[[H-11 - Trans-ovarian (internal, pre-shell) contamination, not shell contamination, drives the SE egg epidemic]]"
  - "[[H-12 - Intact Grade A shell eggs are a major vehicle of the US Salmonella enteritidis epidemic]]"
  - "[[H-58 - Some other egg-Salmonella account]]"
exclusivity: "At most one account holds: the thesis that intact Grade A eggs are the major, internally-contaminated vehicle (its route facet H-11 and magnitude facet H-12) versus the residual negation."
exhaustive_by_construction: false
independence: "Foodborne-infection vehicle status is a microbiological channel unrelated to the other clusters; its prior is independent."
depends_on: []
question: "Are intact Grade A shell eggs the major, internally (trans-ovarian) contaminated vehicle of the US Salmonella enteritidis epidemic?"
relevance: "A 'what else to pay attention to' harm channel bearing on how eggs are handled/regulated."
---

![[H-11 - Trans-ovarian (internal, pre-shell) contamination, not shell contamination, drives the SE egg epidemic]]

![[H-12 - Intact Grade A shell eggs are a major vehicle of the US Salmonella enteritidis epidemic]]

![[H-58 - Some other egg-Salmonella account]]

## Carving

The sub-question is whether intact Grade A shell eggs are the major, internally-contaminated vehicle of the US Salmonella enteritidis epidemic. H-11 supplies the contested route (internal, pre-shell trans-ovarian contamination, so handling and washing cannot control it) and H-12 the magnitude (eggs the principal vehicle). These are complementary facets of one thesis rather than rivals, and no curated observation separates route from magnitude, so they are kept together, with the residual H-58 carrying the negation - transmission dominated by external/shell contamination controllable by handling, or eggs not the principal vehicle. Non-exhaustive because the thesis's two facets could in principle split (a major vehicle but via a different route). Both facets were novel and uncertain in 1988 and have since been confirmed, so the live probability mass concentrates on the thesis; the cluster is retained mainly to carry that near-settled channel into the net-health accounting.

## Prior

```python
# HC-12 prior — are intact Grade A shell eggs the major, internally (trans-ovarian) contaminated vehicle of
# the US Salmonella enteritidis epidemic? Members in HC-12.hypotheses order:
# [H-11 internal trans-ovarian route drives it, H-12 eggs a MAJOR vehicle (magnitude), H-58 residual negation].
# Per the note, H-11 and H-12 are complementary FACETS of one thesis priced as exclusive members (route-
# emphasis vs magnitude-emphasis), with H-58 the negation. No cluster no-observation arguments exist
# (no_observation_arguments.py --cluster HC-12 returns none). All three inbound E edges (E-2/E-3/E-4 — the
# 77% Grade-A attribution, the SE-vs-other-serotype 44%/15% contrast, the 10%/0% bulk-egg culture geography)
# are the case-specific DISCRIMINATING surveillance data and form correlation group CG-32; NONE is marked
# used_for_prior (all-or-none satisfied), so step 8 prices the whole group. This is deliberately a MODEST
# outside-view prior (1988 framing, before that surveillance analysis) — the near-settled confirmation the
# note describes is delivered by step 8's strong evidence, and baking it in here would double-count.
# Weights are relative odds; the magnitude facet is the unit anchor.

# H-12 magnitude facet — eggs are a MAJOR vehicle of the SE epidemic. The more robust, less-novel half of
# the thesis: eggs were already a historically plausible Salmonella vehicle, so "eggs a leading vehicle" is
# the likeliest single characterisation if eggs are implicated at all. Unit anchor.
w_H12 = 1.0

# H-11 route facet — the operative route is internal trans-ovarian (pre-shell), so handling/washing cannot
# control it. In 1988 this was the NOVEL, surprising claim (the default assumption was external shell /
# cross-contamination of cracked or soiled eggs), so a priori it carries somewhat less weight than the
# plain magnitude claim.
route_vs_magnitude = 0.7   # H-11 : H-12 ~ 0.7 : 1 a priori (novel internal route vs the safer magnitude claim)
w_H11 = route_vs_magnitude * w_H12

# H-58 residual negation — the thesis is wrong: transmission dominated by external/shell contamination that
# handling CAN control, or eggs are not the principal vehicle (e.g. poultry meat or another route dominates).
# In 1988 this negation was close to the DEFAULT belief (intact, clean, refrigerated Grade A eggs were
# considered safe), so before the surveillance analysis it holds real prior mass. Its own argued weight
# (rule 4), not a leftover.
w_H58 = 0.85   # ~0.85 : 1 vs the magnitude anchor; ~33% of the mass once normalised, to be crushed by step 8

prior("HC-12", [w_H11, w_H12, w_H58])
```
