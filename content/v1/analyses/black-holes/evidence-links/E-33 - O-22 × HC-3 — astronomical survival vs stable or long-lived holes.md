---
id: E-33
type: evidence-link
from: "[[O-22 - Earth, Sun, white dwarfs, neutron stars and the stars at large have survived billions of years of cosmic-ray bombardment]]"
to: "[[HC-3 - Nature and decay of an LHC-produced strong-gravity object]]"
arguments:
  - "[[A-24 - Nature has already run the LHC collision programme 1e31 times on bodies that still exist, bounding any collider disaster mechanism]]"
  - "[[A-25 - Cosmic-ray collisions would already have nucleated any vacuum bubble the LHC could - and a bubble expands regardless of production frame]]"
  - "[[A-26 - Dangerous magnetic monopoles are excluded - GUT monopoles are far too heavy for the LHC, and cosmic-ray-produced ones would have stopped in Earth harmlessly]]"
  - "[[A-29 - Stable black holes from cosmic rays would be charged, stop in Earth or Sun, and accumulate in billions - the absence of any effect excludes the scenario]]"
  - "[[A-30 - Even hypothetically stable neutral black holes would have destroyed observed white dwarfs and neutron stars - their survival closes the last case]]"
  - "[[A-33 - Interstellar heavy-ion collisions would have seeded stars with strangelets - the absence of strangelet-triggered stellar explosions bounds the danger with no velocity assumption]]"
---
![[O-22 - Earth, Sun, white dwarfs, neutron stars and the stars at large have survived billions of years of cosmic-ray bombardment]]

## Why this is evidence

Prompt-decay members (H-10 canonical Hawking, H-14 near-threshold states decaying on microscopic timescales) predict this survival with certainty. H-24 (stable neutral holes) does not: cosmic-ray collisions on dense stars produce the same objects, white dwarfs and neutron stars stop even neutral holes, and stopped stable holes would consume their hosts in highly visible events on timescales short against the observed Gyr ages — so the persistence of large white-dwarf and neutron-star populations is unexpected under H-24 conditional on production. The long-lifetime tail of H-7 (metastability up to years or beyond) is strained the same way, though its shorter-lived range is untouched. Stable variants inside the residual H-35 are disfavored likewise.

## Likelihood

```python
# E-33 (HC-3) — lone edge, one observation O-22 "broad astronomical survival": Earth (4.5 Gyr), the Sun, ~1e22
# stars incl. white dwarfs and neutron stars persist through Gyr of cosmic-ray exposure, and conventional
# astrophysics accounts for all detected holes. This is the COARSE, qualitative survival witness — LSAG's
# restatement of Giddings-Mangano (A-30 approved). Its real quantitative teeth against H-24 are the WD/NS
# destruction chain, which E-34/E-35 price precisely off G-M; to avoid over-counting the same physics three
# times this edge is kept milder than those. Prompt-decay members predict survival with certainty; anchor
# H-10 = 1 (rule 7). Members in HC-3.hypotheses order [H-7, H-10, H-14, H-24, H-35].
lik_surv_H7  = 0.85   # metastable: its ms-to-years bulk decays before doing astrophysical damage, so survival
                      # is nearly expected — only the long-lifetime tail (holes brought to rest, then accreting)
                      # is strained (A-30). Mild ratio just below the anchor
lik_surv_H10 = 1.0    # anchor: canonical prompt Hawking decay — objects gone in ~1e-27 s, survival certain
lik_surv_H14 = 1.0    # near-threshold stringy state also decays promptly and is astrophysically safe — survival
                      # certain, indistinguishable from H-10 on this observation
lik_surv_H24 = 0.30   # stable neutral: cosmic-ray-produced neutral holes on dense stars would destroy them in
                      # highly visible events on <<Gyr timescales (A-29, A-30), so broad survival is unexpected.
                      # Not near zero — this qualitative statement's force IS the WD/NS quantitative chain priced
                      # by E-34/E-35, and D-range escape hatches (A-49 D<=7 vs A-52 D>=8) remain open; kept coarse
                      # here to price only this edge's own increment above the sharp compact-star edges
lik_surv_H35 = 0.60   # residual: unconstrained — its stable-accreting variants are cut like H-24, but most
                      # unmodelled fates (Planck remnant, stalled evaporation, prompt-like decay) survive fine.
                      # Middling, tilted toward survival-compatible (rule 3)
t_surv = 0.82         # cap = trust_score(S-1 LSAG) = 0.82; held at cap — the persistence of Earth/Sun/stars is
                      # an uncontested, generally-known background fact with no data-pipeline weakness. The
                      # stopping/production inferential chain enters as reasoning, not as a trust dock (rule 5)
evidence("HC-3", ["O-22"], [lik_surv_H7, lik_surv_H10, lik_surv_H14, lik_surv_H24, lik_surv_H35], t=t_surv)
```
