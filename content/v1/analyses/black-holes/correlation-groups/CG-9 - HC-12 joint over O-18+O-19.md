---
type: correlation-group
id: CG-9
to: "[[HC-12 - Stiffness of the cold supranuclear equation of state]]"
members:
  - "[[E-19 - O-18 × HC-12 — second two-solar-mass pulsar by an independent method]]"
  - "[[E-21 - O-19 × HC-12 — orbital decay corroborates the two-solar-mass value independently of white-dwarf models]]"
---

Joint likelihood for correlated observations O-18, O-19 (shared basis: S-80). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-9 (HC-12) — ONE joint estimate over members E-19 + E-21: both observations rest on S-80
# (Antoniadis+ 2013 on PSR J0348+0432), so they are one witness (rule 1). Members in HC-12.hypotheses
# order [H-1 stiff, H-44 softened] — exhaustive binary, no residual (rule 3 n/a). The pattern judged
# whole: a second ~2 Msun pulsar (2.01±0.04) measured by WD spectroscopy+timing rather than Shapiro
# delay (O-18), AND its GR orbital-decay Pb-dot(obs)/Pb-dot(GR)=1.05±0.18 (O-19), which cross-checks
# that mass by a channel that BYPASSES the WD-atmosphere/cooling-model step (E-21). Anchored H-1 = 1;
# H-44 built from the crux P(2.01 observed | softened) times a decay-corroboration factor (rule 7).
# A-22 (approved, E-21) enters only as reasoning — it confirms GR holds in this strong field, so the
# mass inference is not escapable via GR-failure; being an HC-13 argument it does not move these numbers.

lik_pulsar_H1 = 1.0            # anchor: H-1 (stiff, Mmax >= ~2 Msun) predicts massive NS are real and
                              # reproducible across methods, so a second 2.01 Msun pulsar by a DIFFERENT
                              # systematic (WD models, not inclination) plus GR-consistent orbital decay
                              # is exactly what stiff EOS expects — both halves of the pattern fully fit

p_mass_artifact_H44 = 0.22    # CRUX: P(2.01+/-0.04 observed | softened EOS). Under H-44 the true Mmax
                              # falls below ~2 Msun, so O-18 must be an artifact of the one model-dependent
                              # link — WD atmospheres/cooling tracks (O-18 body). Not negligible (WD models
                              # are a genuine systematic) but a 2% measurement is rarely inflated by the
                              # required ~0.1-0.3 Msun, and the paper argues the thin-envelope escape needs
                              # fine-tuning + an implausible ~20 Myr cooling age

f_decay_corroboration_H44 = 0.5  # O-19 multiplies the artifact story down: the GR decay prediction is
                              # computed from the spectroscopic masses and the observed decay agrees
                              # (E-21), bypassing the WD step — under a materially lower true mass the
                              # predicted decay would generically shift off the observed value. Only ~0.5,
                              # not tiny: the +/-18% precision (mass via decay is ~2.07 +0.20/-0.21) is a
                              # loose independent constraint, so the coincidence H-44 needs is not extreme

lik_pulsar_H44 = p_mass_artifact_H44 * f_decay_corroboration_H44  # ~0.11: joint pattern ~9x less
                              # expected under softened than stiff — a strong but non-extreme corroborating
                              # update from this second (not primary) mass, priced independently of J1614

t_j0348 = 0.92                # cap = min trust_score over {O-18, O-19} = 0.92 (both via S-80, "strongest
                              # reliability tier": +/-2% mass by two independent channels on a clean system).
                              # Held at cap: the raw spectroscopy/timing data are high-quality; the WD-model
                              # dependence is a truth/systematic issue already priced in lik (rule 5), so
                              # docking t for it would double-count

evidence("HC-12", ["O-18", "O-19"], [lik_pulsar_H1, lik_pulsar_H44], t=t_j0348)
```
