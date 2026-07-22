---
id: E-30
type: evidence-link
from: "[[O-23 - The Moon, unshielded by any atmosphere, has endured billions of years of cosmic-ray heavy-ion bombardment and remains ordinary matter]]"
to: "[[HC-8 - Runaway growth of a stopped negative strangelet]]"
arguments:
  - "[[A-32 - Lunar survival under billions of years of heavy-ion cosmic-ray collisions rules out dangerous strangelet production - RHIC data validate both assumptions]]"
  - "[[A-59 - Lunar persistence bounds dangerous strangelet production at p below 2e-11 - unless production is confined to exactly central rapidity]]"
---
![[O-23 - The Moon, unshielded by any atmosphere, has endured billions of years of cosmic-ray heavy-ion bombardment and remains ordinary matter]]

## Why this is evidence

H-29 predicts that any (meta)stable negative strangelet ever produced near rest in a lunar-surface heavy-ion collision and stopped in the regolith would have run away and converted the Moon to strange matter — so the Moon persisting as ordinary matter after billions of years of unshielded iron-on-iron exposure is improbable under H-29 to the degree cosmic rays could ever have made such a stopping strangelet. H-40 predicts lunar persistence regardless: growth halts before macroscopic conversion. The discrimination is real but conditional — it runs through the chance that production-plus-stopping ever occurred on the Moon (rapidity/stopping caveats live in the attached arguments), so the direction is toward H-40 with strength set by that antecedent.

## Likelihood

```python
# E-30 (HC-8) — lone edge, one observation O-23 "Moon persists as ordinary matter under heavy-ion
# cosmic-ray bombardment". Members in HC-8.hypotheses order [H-29 runaway, H-40 no-runaway];
# exhaustive_by_construction, no residual. Conditioning: HC-8 already assumes a (meta)stable negative
# strangelet exists / stops / is negative; this edge discriminates only through whether, over the lunar
# exposure, a produce-AND-stop event ever occurred and (under H-29) ran away. Anchor H-40 = 1 (rule 7).
lik_moon_H40 = 1.0   # anchor: under no-runaway the Moon persists with certainty regardless of any
                     # strangelet stopped in the regolith — the observation is guaranteed
lik_moon_H29 = 0.15  # 0.15x: under runaway, persistence requires that NO stoppable dangerous strangelet
                     # was ever produced-and-stopped in ~1e28 lunar Fe-Fe collisions. A-59 (approved):
                     # lunar survival bounds that per-collision probability < 2e-11 even with a 1e-6
                     # rapidity-suppression factor; A-32 (approved): RHIC Cu+Cu thermal and velocity data
                     # validate the two stopping assumptions. Not lower because the bound's sole escape —
                     # production ONLY at exactly central rapidity (products too fast to stop) — is NOT
                     # closed by this body. E-30's own increment is the lunar heavy-ion STOPPING channel
                     # (docked for that rapidity loophole); it is complementary to E-32's metastability
                     # loophole, not a re-count of the same "no conversion observed" logic.
t_moon = 0.82        # cap = trust_score(O-23 source S-1) = 0.82; "Moon persists as ordinary matter" is a
                     # generally-known robust fact with no dating/selection weakness — held at the cap
evidence("HC-8", ["O-23"], [lik_moon_H29, lik_moon_H40], t=t_moon)
```
