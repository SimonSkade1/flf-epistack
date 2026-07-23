---
type: correlation-group
id: CG-5
to: "[[HC-2 - Number of independent introductions of SARS-CoV-2 into humans]]"
members:
  - "[[E-1 - O-4 × HC-2 — two co-dominant lineages with a clean two-mutation gap]]"
  - "[[E-2 - O-5 × HC-2 — no genuine circulating A-B intermediate haplotype]]"
  - "[[E-3 - O-6 × HC-2 — separately dated lineage A and B primary cases]]"
---

Joint likelihood for correlated observations O-4, O-5, O-6 (shared basis: D-3). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-5 (HC-2) — ONE joint estimate over members E-1 + E-2 + E-3: O-4 (two co-dominant early lineages
# A/B separated by a clean two-linked-mutation gap), O-5 (the 20 apparent A-B intermediate genomes are
# low-coverage / lab-clustered sequencing artifacts, i.e. no genuine human intermediate circulated),
# O-6 (BEAST clock dates two distinct, near-simultaneous primary infections). All three rest on the
# same S-1/Pekar D-3 basis (rule 1), so the whole two-lineage / no-intermediate / two-primaries pattern
# is judged as ONE witness — if that dataset+pipeline is wrong they fail together. Members in
# HC-2.hypotheses order [H-5 two-or-more introductions, H-16 single introduction]; no residual
# (exhaustive_by_construction: true), so a two-entry vector (rule 3 n/a). Anchored on H-5 = 1 — this
# pattern is the classic >=2-introduction signature Pekar built it to be — with H-16 priced as a ratio
# to it (rule 7).
lik_pattern_H5 = 1.0   # anchor: two-or-more introductions is the member the whole pattern signals.
                       # Separately seeded lineages need no circulating human intermediate — the
                       # two-mutation gap sits across the population boundary, matching O-5 — and two
                       # separately dated, near-simultaneous primary cases (O-6) are exactly what
                       # independent spillovers predict. Close to maximally expected under H-5.
lik_pattern_H16 = 0.45 # ~0.45x as expected under a single introduction (BF ~2.2 toward H-5). The
                       # single-introduction camp reads the two lineages as ordinary within-human
                       # diversification from one seeding, the bridging intermediate merely UNSAMPLED
                       # rather than absent: A-4 (approved) shows the 20 candidate intermediates are
                       # artifacts, which removes the POSITIVE genomic support for an in-human A->B
                       # transition but does not forbid an unsampled one; and it reads O-6's dates as one
                       # MRCA seen through a model-laden clock. Set only MODESTLY below 1, NOT at the
                       # original BF~60 (~0.017): A-3 was CORRECTED — the 2024 erratum cut the Bayes
                       # factor ~an order of magnitude (to ~6) and independent reanalyses (Weissman,
                       # McCowan) argue the corrected model can point toward one introduction, so only
                       # the weak qualitative "the two-lineage/two-mutation topology is unusual under a
                       # single introduction" survives, with magnitude and even sign contested. 0.45
                       # encodes that shrunken, direction-contested residual signal, not the headline BF.
t_pattern = 0.5        # cap = min trust_score over {O-4,O-5,O-6} = 0.6 (all via S-1/Pekar). The erratum
                       # + reanalysis dispute is ALREADY inside that 0.6 cap (S-1.trust_reason names it),
                       # so re-docking for it would double-count. Docked one further step to 0.5 for a
                       # DISTINCT observation-level weakness on the dating leg (O-6): the tMRCA and
                       # primary-case dates are rooting-dependent (recCA vs unconstrained), carry ~6-week
                       # HPDs (lineage-B primary case 23 Oct–8 Dec), and rest on a pre-ascertainment
                       # simulation window that could not be empirically validated (A-3-corrected) —
                       # a data-reliability dock, not a truth judgement.
evidence("HC-2", ["O-4", "O-5", "O-6"], [lik_pattern_H5, lik_pattern_H16], t=t_pattern)
```
