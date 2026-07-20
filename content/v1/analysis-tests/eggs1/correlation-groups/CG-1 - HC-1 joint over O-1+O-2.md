---
type: correlation-group
id: CG-1
to: "[[HC-1 - Magnitude and mechanism of egg's effect on atherogenic blood lipids]]"
members:
  - "[[E-1 - O-1 × HC-1 — one egg-day raised LDL-C 12% and ApoB 9%]]"
  - "[[E-2 - O-2 × HC-1 — lipid effect confined to LDL-ApoB, HDL and TG unchanged]]"
---

Joint likelihood for correlated observations O-1, O-2 (shared basis: S-12). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-1 (HC-1) - ONE joint estimate over E-1 + E-2: O-1 and O-2 are two readouts of the same lipid
# panel in the same 17-subject Sacks 1984 crossover (shared data basis S-12), so they are priced as
# one pattern (rule 1), not as two witnesses. The pattern judged whole: at a very LOW baseline
# cholesterol intake (97 -> 418 mg/d), one egg/day for 3 weeks raised LDL-C 12% and ApoB 9%, while
# HDL-C, ApoA-I, ApoA-II, VLDL-C and TG did not move. Two features carry the discrimination: the
# SIZE of the LDL/ApoB rise, and its CONFINEMENT to the atherogenic fraction.
# A-1 (approved) is what lets the rise be read as caused by the egg at all; its own caveat is that
# a low-baseline vegetarian sample may show a larger fractional response than omnivores - which is
# precisely the thing H-8 predicts, so A-1 lifts H-8 rather than H-1.
# Anchored on H-1 = 1; the rest are ratios to it (rule 7).

lik_sacks_H1 = 1.0    # anchor: H-1 (large, CVD-relevant ApoB rise) predicts this pattern almost
                      # exactly - a double-digit LDL/ApoB rise from a single egg, isolated to the
                      # atherogenic particles. Nothing here is surprising under H-1.

lik_sacks_H8 = 0.85   # 0.85x as expected as under H-1. H-8 (real but saturating) predicts a small
                      # effect AT HIGH habitual intake; this experiment sits at 97 mg/d, the steep
                      # part of the curve, where H-8 predicts a LARGE fractional rise too. So the
                      # magnitude barely separates H-1 from H-8 in this study - the small markdown
                      # is only that 12% is at the upper end even of a steep-segment prediction.
                      # H-8 is equally silent-and-compatible on O-2's fraction confinement.

lik_sacks_H5 = 0.15   # 0.15x. H-5 (egg-matrix cholesterol poorly absorbed) predicts a much smaller
                      # plasma response than this at ANY baseline - a +12% LDL from ~320 mg/d extra
                      # is roughly what good absorption plus partial hepatic compensation gives.
                      # Not near zero: N=17 leaves room for the point estimate to overshoot a truly
                      # small effect, and lacto-vegetarian gut adaptation could raise absorption
                      # atypically. H-5 is near-silent on O-2, so O-2 adds little against it.

lik_sacks_H11 = 0.3   # 0.3x. Residual is unconstrained and could accommodate a 12% LDL rise, but
                      # O-2 bites here specifically: the main non-listed characterizations in play
                      # are "no material atherogenic-lipid effect" and "the effect runs through HDL
                      # functionality / particle size / TG rather than LDL-ApoB mass", and both are
                      # disfavoured by a clean isolated LDL-ApoB move with HDL, ApoA and TG flat.
                      # Kept well above zero (rule 3) - some unlisted mechanism could still produce
                      # an ApoB-only rise, and I do not know that none could.

t_sacks = 0.68        # cap = trust_score of S-12 = 0.78 (both observations, same source). Docked
                      # modestly below the cap for what sits between the raw panel and the stated
                      # observation: N=17 makes both the 12%/9% point estimates and, more sharply,
                      # the "unchanged" null in O-2 low-powered - underpowered nulls on HDL/ApoA/TG
                      # can read as confinement when a real smaller effect exists; and 1984 apoB
                      # immunoassays are less standardized than modern ones.

evidence("HC-1", ["O-1", "O-2"], [lik_sacks_H1, lik_sacks_H5, lik_sacks_H8, lik_sacks_H11], t=t_sacks)
```
