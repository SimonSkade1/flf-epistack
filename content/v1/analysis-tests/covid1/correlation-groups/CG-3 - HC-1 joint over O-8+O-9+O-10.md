---
type: correlation-group
id: CG-3
to: "[[HC-1 - Route of the first human SARS-CoV-2 infection]]"
members:
  - "[[E-5 - O-8 × HC-1 — closest natural relatives from Laos with a recombinant mosaic spike]]"
  - "[[E-6 - O-9 × HC-1 — a wild bat sarbecovirus already binds human ACE2]]"
  - "[[E-7 - O-10 × HC-1 — closest natural relatives lack the furin cleavage site]]"
---

Joint likelihood for correlated observations O-8, O-9, O-10 (shared basis: S-12). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-3 (HC-1) — ONE joint estimate over E-5 + E-6 + E-7: O-8, O-9 and O-10 all rest on S-12
# (Temmam 2022, the same Laos sampling campaign and the same wet-lab work-up), so they are one
# witness, not three (rule 1). The pattern is judged whole, and the whole pattern is:
#
#   "the closest known natural relatives of SARS-CoV-2 are human-cell-infectious but furin-site-free"
#
# i.e. a wild Rhinolophus clade in northern Laos that (a) is nearer SARS-CoV-2 genome-wide than
# RaTG13 with a recombinant mosaic spike, (b) already binds human ACE2 at SARS-CoV-2-like affinity
# and replicates in human cells with no passage or engineering, yet (c) carries no furin cleavage
# site at S1/S2. The two halves point opposite ways (b cuts against H-5, c is what an insertion
# account predicts), which is exactly why they must be priced as one composite and not netted off
# per observation (process 3). Members in HC-1.hypotheses order:
# [H-1 Huanan market spillover, H-5 WIV research-related incident, H-6 residual].
# Anchored on H-1 = 1; H-5 and H-6 priced as ratios to it (rule 7).

lik_banal_H1 = 1.0
# ANCHOR. Given a natural market spillover, this composite is close to what you would expect a
# reservoir survey to return. A natural route requires a wild progenitor pool that is already
# human-competent without human intervention; the survey found precisely that (96.8% identity,
# mosaic spike from ongoing recombination, human-ACE2 binding). The one part that sits awkwardly
# is the missing furin cleavage site: under H-1 the site has to have arisen naturally somewhere in
# the reservoir or in an intermediate host, and three viruses from one Laos region show no trace of
# it. That is a real cost, but a small one at this sample size — sarbecovirus sampling is sparse
# enough that absence in n=3 from one karst region is weak evidence of absence in the clade, and
# furin sites occur elsewhere in the wider betacoronavirus family. Not "1.0 because H-1 is the best
# fit" — the anchor's scale is free (rule 7); it is the reference the other two are read against.

lik_banal_H5 = 0.65
# 0.65x as expected as under H-1. Conditioning strictly on a WIV research incident being true
# (process 2 — H-5's low prior is step 7's business, not this number's), the composite splits:
#   + The furin-site half (O-10) is genuinely well predicted. If the site was inserted, its absence
#     from every close natural relative is exactly what should be found, and no coincidence is
#     needed. This is the strongest thing this group says for H-5.
#   + Close natural relatives existing at all is neutral-to-expected under H-5: a lab account needs
#     a collectable natural backbone just as much as a spillover account does.
#   - The human-ACE2/human-cell-infectivity half (O-9) is where H-5 loses ground. A-4 (approved,
#     checked) is what moves this number: an uncontrived wild isolate binding human ACE2 at
#     SARS-CoV-2-like affinity is an existential counterexample that defeats "no natural
#     human-infectious analogue exists" as a *reason* to prefer a lab origin. A-4 claims reason-
#     defeat only, not positive support for zoonosis, and concedes the furin site up front, so it
#     does not touch the O-10 half. Its effect here is to strip out the receptor-binding strand of
#     the lab case, leaving the group's pro-H-5 content resting on the furin site alone.
# Net: the composite is somewhat less expected under H-5 than under H-1, because H-5 gets one half
# right and pays for the other, whereas H-1 gets the larger half right and pays a discounted price
# on the smaller. Deliberately not far below 1 — this group is genuinely close to a wash, and a
# reader who weights the furin site more heavily than the sparse-sampling discount should re-run
# with this at or above 1.0. It is the most arguable number in the block.

lik_banal_H6 = 0.9
# 0.9x. Real and argued, not a leftover (rule 3). H-6 is a mixture whose dominant leg is natural
# (upstream supply chain, or distant spillover with silent introduction into Wuhan) plus a small
# non-WIV research leg. Its natural legs predict the composite about as well as H-1 does, and
# marginally better on one point: a Laotian/SE-Asian reservoir sits more comfortably with a
# distant-spillover route than with a Huanan-local one (E-5's "Why this is evidence" makes exactly
# this point). Its small research leg carries the same furin-site fit as H-5. Set just below the
# anchor rather than above it because the composite says nothing that discriminates a market index
# case from an upstream one, and an unconstrained member should not be rewarded for that silence.
# Middling by construction: it neither predicts nor forbids this pattern.

t_banal = 0.7
# Cap = min trust_score over {O-8, O-9, O-10} = 0.8 (all three via S-12). Docked to 0.7 for one
# named weakness in the step from raw data to the stated observations: the infectivity claim in
# O-9 is in-vitro only (binding assay plus replication in human cell lines), which is a weaker
# warrant for "human-infectious" than the observation statement's phrasing invites, and S-12 carries
# an open July 2022 Author Correction that we could not inspect line-by-line in this run. The
# genomic claims (O-8, O-10) are sequence facts and would justify sitting at the cap on their own;
# with mixed reliability inside a group, the minimum governs (process 5). Not docked further for
# n=3 viruses from one Laos region: that is a limit on what the data generalises to, which is
# already priced inside the likelihood comments above, not a defect in the measurement itself.

evidence("HC-1", ["O-8", "O-9", "O-10"], [lik_banal_H1, lik_banal_H5, lik_banal_H6], t=t_banal)
```
