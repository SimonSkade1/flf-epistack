---
type: correlation-group
id: CG-11
to: "[[HC-1 - Origin of SARS-CoV-2 — natural zoonosis vs research-related incident]]"
members:
  - "[[E-39 - O-68 × HC-1 — closest full-genome relative is a wild bat virus]]"
  - "[[E-40 - O-69 × HC-1 — wild BANAL RBDs match hACE2-contact residues]]"
  - "[[E-41 - O-70 × HC-1 — wild BANAL RBDs out-bind early SARS-CoV-2]]"
  - "[[E-42 - O-71 × HC-1 — wild unmodified bat virus infects human cells]]"
  - "[[E-43 - O-72 × HC-1 — no BANAL relative has a furin site]]"
  - "[[E-44 - O-73 × HC-1 — natural recombinant mosaic of wild bat sarbecoviruses]]"
---

Joint likelihood for correlated observations O-68, O-69, O-70, O-71, O-72, O-73 (shared basis: S-52). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-11 (HC-1) — ONE joint estimate over member edges E-39..E-44. All six observations rest on the SINGLE
# source S-52 (Temmam 2022, the BANAL discovery), so they are ONE correlated witness (rule 1): if BANAL were
# misidentified or its assays flawed, all six fail together — pricing them as six independent edges would
# re-count the same study six times. Members in HC-1.hypotheses order:
# [H-41 natural zoonosis, H-42 unmodified-collection leak, H-43 engineered lab leak, H-44 residual].
# H-41 and H-42 BOTH have a NATURAL genome, so this natural-relative picture gives them EQUAL likelihood; the
# whole group discriminates only H-43 (engineered) vs {H-41,H-42}. Anchored on the natural-genome bloc = 1
# (rule 7a); H-43 and residual priced as ratios to it.
#
# The pattern judged as ONE witness: a wild bat sarbecovirus 96.8% identical to SARS-CoV-2 (O-68) whose RBD
# already matches 15-16/17 hACE2-contact residues (O-69), out-binds early SARS-CoV-2 ~3x (O-70), enters and
# replicates in human cells unmodified (O-71), and whose backbone+RBD assemble by natural recombination among
# sympatric wild bat viruses (O-73) — the ONE feature the closest relatives don't bridge being the furin
# site (O-72).

lik_banal_H41 = 1.0            # anchor, natural-genome member: the whole picture is exactly what a natural
                              # origin predicts — human-capable sarbecoviruses already circulate and
                              # recombine in wild bats with no lab step needed (A-65, A-66 approved). Best fit.
lik_banal_H42 = lik_banal_H41  # EQUAL to H-41 by construction: H-42 also has a NATURAL genome, so a
                              # natural-relative / no-adaptation picture predicts it identically. The genome
                              # cannot separate the two natural-virus members; only the human-introduction
                              # ROUTE (priced in the prior / other clusters), not this evidence, does.
lik_banal_H43 = 0.5           # 0.5x the natural bloc — moderately, NOT the ~5x the six independent edges
                              # implied. Under an ENGINEERED origin the strong natural-relative +
                              # no-lab-adaptation-needed picture is surprising: natural RBDs already out-bind
                              # SARS-CoV-2 (O-69/O-70/O-71 undercut the "RBD optimised in the lab" premise,
                              # A-65) and the RBD fragment nests cleanly in the wild bat clade rather than
                              # looking grafted (O-73 vs the chimera reading, A-66). Only PARTLY discounted:
                              # H-43 still assumes a natural backbone, and O-72 (no furin in any relative) is
                              # CONSISTENT with / mildly favours a separate lab insertion (A-67: route stays
                              # open), which offsets most of the tilt. Net ~2:1 for the natural bloc as one
                              # witness.
lik_banal_H44 = 0.7           # residual, unconstrained: middling (rule 3). Many unlisted histories (e.g. a
                              # lab-modified virus later spilling naturally) still carry a natural genome and
                              # would fit these natural relatives, so it sits nearer the natural bloc than
                              # H-43 but predicts nothing sharply; not pushed to an extreme.
t_banal = 0.80               # cap = trust_score(S-52) = 0.85, inherited by all six observations. Docked
                              # slightly for the model-dependence of the recombination inference (O-73 rests
                              # on GARD breakpoint detection); the direct assays behind O-68..O-72 (genome
                              # identity, SPR affinity, pseudovirus entry, live-virus recovery) are
                              # multi-method and convergent, so the dock is small.
evidence("HC-1", ["O-68", "O-69", "O-70", "O-71", "O-72", "O-73"],
         [lik_banal_H41, lik_banal_H42, lik_banal_H43, lik_banal_H44], t=t_banal)
```
