---
type: hypothesis-cluster
id: "HC-2"
question: "Did the two early lineages A and B arise from a single introduction of SARS-CoV-2 into humans, or from two or more separate introductions?"
hypotheses:
  - "[[H-5 - Early A-B diversity reflects two or more separate zoonotic introductions, not one]]"
  - "[[H-16 - SARS-CoV-2 early lineages A and B are better explained by a single introduction than by two]]"
exclusivity: "A count of the introduction events that seeded the co-circulating early lineages is either exactly one or two-or-more; the two members are these complementary cases, so at most one holds."
exhaustive_by_construction: true
independence: "The introduction count is a distinct quantity from the origin mechanism and the market's role; its prior — how many separate spillover/introduction events seeded the human epidemic — does not require fixing those. Its answer is evidentially correlated with origin (see depends_on), but the phylodynamic evidence that scores it is its own."
depends_on:
  - "[[HC-1]]: two-or-more independent introductions essentially requires a repeatable zoonotic source and is very unlikely under a single research-related leak, so P(two-or-more introductions) is strongly correlated with the natural-zoonosis member of HC-1; a single introduction is consistent with either origin. Kept separate (distinct phylodynamic evidence) rather than merged, so treat the two priors as only approximately independent."
relevance: "Two or more independent introductions would strongly favour a repeatable natural (zoonotic) source over a one-off lab leak; a single introduction is roughly neutral between the origins."
---
A genuinely separable sub-question with its own phylodynamic evidence (the two lineage-defining substitutions, the status of intermediate haplotypes, tMRCA dating, and the two-introduction Bayes factor and its post-publication correction).

![[H-5 - Early A-B diversity reflects two or more separate zoonotic introductions, not one]]

![[H-16 - SARS-CoV-2 early lineages A and B are better explained by a single introduction than by two]]

## Carving

**Exclusivity and exhaustiveness.** The members are the mutually exhaustive cases of a count (one vs two-or-more) of the events that seeded the co-circulating early lineages A and B. Every history has at least one such event, and a research-related leak lands in the single-introduction member (one leak), so `exhaustive_by_construction: true` with no residual: the count cannot be zero given a human epidemic, and "one" and "two-or-more" leave no gap. The observation-level claim that no genuine intermediate A/B haplotype circulated in humans (H-6, merged into H-5) is folded in as support for the two-introduction reading rather than kept as a third answer — it is a premise about the count, not a separate value of it.

**Analysis-failure mode.** If the phylodynamic model is misspecified the inferred count could be wrong. Two concrete failures: wrongly dismissing the lineage-connecting intermediate haplotypes as sequencing artifacts (O-5) would inflate support for two-or-more (favouring H-5); an error in the two-introduction Bayes-factor computation or its post-publication correction (O-21) — the headline evidence for separate introductions — would shift support toward the single-introduction member (H-16). Because the true count is not directly observed, a modelling failure of this kind, not a missing "third answer," is what could break the cluster.

## Prior

```python
# HC-2 prior — number of independent introductions of SARS-CoV-2 into humans. Members in
# HC-2.hypotheses order: [H-5 two-or-more introductions, H-16 exactly one introduction].
# exhaustive_by_construction: true — the count of seeding events is either 1 or >=2, so there is no
# residual: a two-entry weight vector only (rule 4 does not apply).
#
# This is the OUTSIDE-VIEW base rate for how a novel zoonotic outbreak enters humans — >=2 vs exactly
# one independent introduction — BEFORE SARS-CoV-2's own phylodynamic evidence. All five inbound edges
# (E-1..E-5: the two-lineage / two-linked-mutation topology, intermediate-haplotype status, tMRCA
# dating, and the Pekar 2022 two-introduction Bayes factor + its 2024 erratum) are case-specific
# DISCRIMINATING data, not reference-class facts, so NONE is marked used_for_prior — all are left for
# step 8. This step therefore marks no frontmatter. The cluster's one no-observation argument
# (`no_observation_arguments.py <dir> --cluster HC-2`), A-5 (approved, checked), enters below as
# reasoning weighed while choosing a number, not as a multiplicative term of its own (rule 6).
#
# depends_on (HC-2 -> HC-1): >=2 introductions essentially needs a repeatable zoonotic source and is
# very unlikely under a one-off leak, so this count is evidentially correlated with HC-1's
# natural-origin member. A per-cluster prior still factorizes; I treat that dependence as an
# approximation and do NOT import HC-1's numbers — c_repeatable below is a *general* base rate over
# emergences, deliberately kept distinct from HC-1's P(zoonosis).

# --- Reference class / shared decomposition ----------------------------------------------------------
# Reason over the two seeding scenarios a novel human-establishing emergence can fall into, then mix.
# c_repeatable: fraction of comparable emergences whose source is a repeatable reservoir kept in
# sustained human contact (wildlife-trade / farm / livestock conduit) rather than a one-off or
# non-repeatable jump. Set moderately-high but well short of certain — many novel zoonoses arrive via
# such conduits, but plenty (one-off bushmeat kills, single pandemic-flu reassortment seedings, a
# hypothetical single leak) do not. A base rate over emergences, kept separate from HC-1's origin prior.
c_repeatable = 0.6

# P(early epidemic seeded by >=2 independent SUCCESSFUL introductions | repeatable sustained-contact
# source). Anchor: SARS-CoV-1, the closest reference case. Its 2003-04 Guangdong re-emergence was FOUR
# independently-infected human cases from the market/civet reservoir, and the 2002-03 epidemic showed
# multiple independent civet-to-human introductions concentrated in market/food handlers (~80% of one
# Guangzhou market's civets seropositive) — per Kan et al. 2005 J Virol and the SARS molecular-
# epidemiology review, https://pmc.ncbi.nlm.nih.gov/articles/PMC2435571 , accessed 2026-07-23. So >=2
# is common, NOT rare, GIVEN this scenario — but even with a repeatable source one establishment often
# pre-empts a near-simultaneous second, so this stays well below certainty. Nudged UP (from ~0.35) by
# A-5 (approved, checked): if both lineages established with no within-human adaptation the progenitor
# was already human-transmissible in the reservoir, making each contact a Bernoulli trial and repeated
# successful spillovers plausible. A-5 is folded in here as reasoning, not as a separate term.
p_multi_given_repeatable = 0.45

# P(>=2 independent successful introductions | one-off / non-repeatable source). A single jump (or a
# single leak) yields one introduction by construction; >=2 would require an implausible coincidence of
# two separate one-off events in the same narrow origin window. Small but nonzero.
p_multi_given_oneoff = 0.05

# --- H-5: two or more independent introductions ------------------------------------------------------
# Holds if early A/B diversity was seeded by >=2 separate spillovers, which essentially requires a
# repeatable reservoir with sustained human contact. Reference class: coronavirus emergence via the
# wildlife trade, anchored on SARS-CoV-1's documented multiple introductions. Does NOT cover
# SARS-CoV-2's own phylodynamics (that is step-8 evidence, edges E-1..E-5). Judged the minority member
# a priori: the base rate of >=2-introduction seedings is real but below single-introduction seedings.
w_multi = c_repeatable * p_multi_given_repeatable + (1 - c_repeatable) * p_multi_given_oneoff

# --- H-16: exactly one introduction ------------------------------------------------------------------
# Holds if one spillover (or one leak) seeded the human MRCA and A/B diverged within humans. Priced from
# the SAME scenario mixture as its complement WITHIN each scenario — (1 - p_multi_*) is an arithmetic
# identity, not a fresh estimate, since the count is binary within a scenario too — so both members are
# argued from the named scenario factors rather than one being a bare complement of the OTHER member's
# weight (w_single does not reference w_multi). Favoured a priori: most documented novel emergences that
# establish sustained human transmission trace to a single introduction, because establishing
# transmission is itself rare and doing it twice near-simultaneously is rarer. More confident in this
# member than in H-5.
w_single = c_repeatable * (1 - p_multi_given_repeatable) + (1 - c_repeatable) * (1 - p_multi_given_oneoff)

prior("HC-2", [w_multi, w_single])
```
