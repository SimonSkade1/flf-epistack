---
id: HC-7
type: hypothesis-cluster
question: "Is bulk strange quark matter absolutely stable at zero external pressure?"
hypotheses:
  - "[[H-28 - Strange quark matter may be absolutely stable in bulk at zero external pressure]]"
  - "[[H-39 - Bulk strange quark matter is not absolutely stable at zero external pressure]]"
exclusivity: "Either up-down-strange quark matter is the true ground state of baryonic matter at zero pressure or it is not; the members are a claim and its negation."
exhaustive_by_construction: true
independence: "Strange-matter stability is dense-QCD physics, factorizing from the gravity-scale, monopole, vacuum, and astrophysical clusters."
depends_on: []
relevance: "The strangelet disaster scenario — the main non-black-hole mechanism in the main question — is live only if bulk strange matter is stable."
---
![[H-28 - Strange quark matter may be absolutely stable in bulk at zero external pressure]]
![[H-39 - Bulk strange quark matter is not absolutely stable at zero external pressure]]

Witten's conjecture against its negation. Exhaustive by construction: proposition and logical complement, no residual needed. A failure of the analysis would look like the corpus's stability discussions all resting on the same bag-model idealizations while terrestrial, astrophysical, and accelerator searches were each insensitive for a shared unnoticed reason; such a failure would favour the first member (stability remaining live despite the null searches).

## Prior

```python
# HC-7 prior — is bulk strange quark matter absolutely stable at zero external pressure? Members in
# HC-7.hypotheses order: [H-28 stable in bulk, H-39 not stable]. exhaustive_by_construction: a proposition
# and its logical negation, so there is NO residual member (rule 4 does not apply).
# Inputs: an outside view over long-standing, internally-consistent-but-unconfirmed exotic ground-state
# conjectures, plus the cluster's no-observation arguments from
# `no_observation_arguments.py <analysis-dir> --cluster HC-7` (A-56, A-65, both approved) used as reasoning
# only, never as a term. The two inbound E edges — E-2 (fifteen years of null strange-matter searches) and
# E-3 (STAR strangelet null at RHIC) — are case-specific discriminating null searches, NOT base rates, so
# neither is priced into this prior; both are left unmarked for step 8.

# H-39 not-stable — the anchor. Outside-view default: Witten's strange-matter conjecture (proposed 1984,
# ~42 years standing) has neither a first-principles proof nor an empirical confirmation, and the mainstream
# prior for an unconfirmed exotic ground state is that it is not the true ground state. This member needs no
# special mechanism to be true — ordinary nuclei being the ground state is the null world. Take it as unit weight.
# Most confident of the two: it is favoured both by the base rate and by the accumulated (here unpriced) nulls.
w_unstable = 1.0

# H-28 stable — for this to be right, up-down-strange quark matter must be absolutely stable in bulk at zero
# pressure despite ordinary nuclei being metastable against decaying into it. Priced as odds against H-39 from
# an outside view, then nudged by the two arguments. Reference class: decades-old, QCD-consistent but
# unconfirmed conjectures that some exotic configuration is the true ground state of matter.
# Outside view: base rate that such a conjecture turns out realized. Most drift toward "not realized" as null
# searches accumulate, but a real minority survive, and strange-matter stability is excluded by no
# first-principles QCD result — so this is well above zero, not a fringe possibility.
p_base_exotic_true = 0.30   # ~30% of long-standing, consistent-but-unconfirmed exotic ground-state claims prove real
# Adjustment factor (<1). The stability window has narrowed over 40 years (the viable bag-model / coupling
# region shrank under hypernuclear and lattice input) without closing. A-56 (approved) argues the *dangerous*
# strangelet scenario dies at producibility and at the positive-charge requirement, but explicitly leaves bulk
# stability — its condition (1) — open, so it barely lowers H-28 here. A-65 (approved) notes Earth's long
# nuclearite-exposure history without conversion, a weak further downward nudge on realized bulk stability.
# Net: a mild discount, not a kill; the discriminating nulls that could sharpen it are step 8's job.
f_window = 0.85
odds_stable = (p_base_exotic_true / (1 - p_base_exotic_true)) * f_window   # identity, not an estimate
w_stable = odds_stable * w_unstable   # H-28

prior("HC-7", [w_stable, w_unstable])
```

