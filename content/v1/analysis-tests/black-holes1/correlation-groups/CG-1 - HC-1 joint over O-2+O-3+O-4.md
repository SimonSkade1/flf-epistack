---
type: correlation-group
id: CG-1
to: "[[HC-1 - Fate of a stable LHC black hole trapped in Earth]]"
members:
  - "[[E-2 - O-2 × HC-1 — Gyr-old neutron stars observed intact]]"
  - "[[E-3 - O-3 × HC-1 — super-LHC cosmic-ray exposure of Earth, WDs and NSs]]"
  - "[[E-4 - O-4 × HC-1 — Earth and Sun survived 4.5 Gyr of UHECR bombardment]]"
---

Joint likelihood for correlated observations O-2, O-3, O-4 (shared basis: D-1, S-5). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-1 (HC-1) — ONE joint estimate over E-2+E-3+E-4: all three observations rest on the shared
# cosmic-ray survival premise D-1 (rule 1). The whole pattern: cosmic rays far above LHC energy
# have bombarded Earth, WDs and NSs for Gyr (O-3), yet 10^8-10^9-yr-old neutron stars are intact
# (O-2) and Earth+Sun survived 4.5 Gyr (O-4). Anchored on H-2 = 1 (rule 7); members in
# HC-1.hypotheses order [H-1, H-2, H-6]. Note: the white-dwarf survival datum is the separate
# lone edge E-1/O-1, not priced here — so A-1/A-2's WD half enters E-1's block, and only their
# NS half moves numbers here.
lik_survival_H2 = 1.0   # anchor: under "no macroscopic risk" every element of the pattern is
                        # exactly what you'd see — survival is the unconditional prediction
lik_survival_H1 = 0.10  # ~0.1x H-2: under catastrophic accretion, nature already ran vastly more
                        # super-LHC collisions on these bodies (O-3), so intact Gyr-old NSs and a
                        # surviving Earth/Sun are jointly surprising. Not lower because the escape
                        # routes are real: (a) the NS bound needs cosmic rays to penetrate NS
                        # magnetospheres (O-2's own caveat; G-M call WDs the more robust case, and
                        # WDs are priced on E-1, not here); (b) O-4 only bites for charged/
                        # EM-interacting BHs — neutral ones punch through Earth/Sun relativistically
                        # (A-1 approved closes that loophole only via WD/NS stopping power, i.e.
                        # partly outside this group); (c) A-3 corrected: Earth/Sun survival is
                        # anthropically conditioned, so O-4 carries reduced weight — A-6 corrected
                        # says the observer-selection worry does NOT extend to distant NSs, so O-2
                        # keeps most of its force and dominates this number. A-2 approved (every
                        # fast-accretion scenario excluded by WD/NS survival) is why the number is
                        # this low despite the caveats.
lik_survival_H6 = 0.55  # ~0.55x H-2: residual fates (sub-catastrophic damage, unmodeled regimes)
                        # mostly leave NSs and Earth observably intact, so the pattern is fairly
                        # expected — but some residual fates (e.g. significant heating or partial
                        # consumption of NSs) would show, so below the anchor, not at it
t_survival = 0.74       # cap = min trust_score over O-2/O-3/O-4 = 0.74 (all via S-1; the anthropic
                        # and magnetosphere weaknesses are priced in lik_survival_H1 above, not
                        # docked again here — the data/astronomy itself is as reliable as step 2
                        # found S-1, so t sits at the cap)
evidence("HC-1", ["O-2", "O-3", "O-4"], [lik_survival_H1, lik_survival_H2, lik_survival_H6], t=t_survival)
```
