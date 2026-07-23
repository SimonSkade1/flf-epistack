---
type: evidence-link
id: "E-19"
from: "[[O-39 - Market-associated SARS-CoV-2 genomes' tMRCA matches the global pandemic tMRCA and both lineages A and B are present in market environmental samples]]"
to: "[[HC-3 - Causal role of the Huanan Seafood Market in the emergence]]"
arguments:
  - "[[A-51 - Market-associated genomes' tMRCA equalling the global tMRCA, with both lineages present, indicates emergence at the market rather than downstream amplification]]"
---
![[O-39 - Market-associated SARS-CoV-2 genomes' tMRCA matches the global pandemic tMRCA and both lineages A and B are present in market environmental samples]]

## Why this is evidence
A downstream amplifier of prior community transmission (H-15) or an incidental venue (H-19) would carry viral diversity younger than the pandemic root; market genomes' tMRCA matching the pandemic tMRCA, with both lineages present, favors emergence at the market (H-14).

## Likelihood

```python
# E-19 (HC-3) — lone edge, one observation O-39: the market-associated genomes' tMRCA overlaps the global
# pandemic root AND both basal lineages A and B are present in market environmental samples (lineage A in
# A20). Members in HC-3.hypotheses order: [H-14 primary wildlife-spillover origin, H-15 externally-seeded
# amplifier, H-19 detection/ascertainment artifact, H-45 residual]. Anchored on H-14 = 1 (best fit); others
# priced as ratios to it (rule 7). Direction from `## Why this is evidence` + A-51 (approved, checked):
# a root-matching tMRCA with BOTH basal lineages present is the "market is at the origin" signature that a
# downstream amplifier or an incidental venue does not predict.
lik_tmrca_H14 = 1.0   # anchor: market = emergence locus is exactly what predicts market genomes at the ROOT
                      # of the tree with both basal lineages present — the modal expectation under this member
lik_tmrca_H15 = 0.35  # 0.35x: an amplifier seeded from outside would tend to coalesce AFTER the root (younger
                      # tMRCA) and carry the amplified lineage only; reproducing root-tMRCA + BOTH lineages
                      # needs an early, already-diverse external seeding — a specific coincidence. Not tiny:
                      # A-51's verdict grants that a diverse community outbreak feeding the market stays
                      # logically possible
lik_tmrca_H19 = 0.3   # 0.3x: a causally-incidental venue (positives = contamination from tested cases) has
                      # even less reason than an active amplifier to hold both basal lineages at the root —
                      # its environmental genomes would reflect later community diversity. Slightly below
                      # H-15, which at least channels virus through the market
lik_tmrca_H45 = 0.5   # residual, unconstrained (rule 3): some unlisted roles (a genuine co-spillover site,
                      # cold-chain-as-origin AT the market) fit root-tMRCA + both-lineages well, others don't
                      # — middling. Above H-15/H-19 because it includes origin-flavoured variants
t_tmrca = 0.7         # cap = trust_score(S-35) = 0.75; docked modestly for the raw-data->observation step:
                      # the tMRCA overlap rests on a molecular clock with wide (only "overlapping") 95% HPD
                      # intervals, and the lineage-A-at-market claim rests on a SINGLE environmental read (A20)
                      # whose metagenomic lineage assignment is contestable
evidence("HC-3", ["O-39"], [lik_tmrca_H14, lik_tmrca_H15, lik_tmrca_H19, lik_tmrca_H45], t=t_tmrca)
```
