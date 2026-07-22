---
type: correlation-group
id: CG-6
to: "[[HC-9 - Existence of a catalyzing GUT-monopole flux]]"
members:
  - "[[E-5 - O-27 × HC-9 — no solar-direction low-energy neutrino excess]]"
  - "[[E-11 - O-28 × HC-9 — flux-times-catalysis bound far below direct limits]]"
---

Joint likelihood for correlated observations O-27, O-28 (shared basis: D-6). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-6 (HC-9) — ONE joint estimate over members E-5 + E-11: both rest on the same Super-K exposure D-6
# (rule 1), so they are one witness, not two. O-27 is the raw solar-direction null (317 candidates, no
# significant 19-55 MeV excess, I90 = 166.6 cm^-2 s^-1); O-28 is A-42's inversion of that same null into
# the flux×catalysis bound. Judged as ONE pattern: "Super-K's 4.6-Gyr-averaged solar exposure sees no
# catalysis neutrinos, driving F_M·sigma_0 >8 orders below direct flux limits." Members in HC-9.hypotheses
# order [H-20 detectable catalyzing flux, H-41 no relevant flux]; exhaustive_by_construction, no residual.
# Anchored on H-41 = 1 (rule 7): the null is exactly what "no flux" predicts.

lik_solarnull_H41 = 1.0   # anchor: H-41 (no astrophysically relevant catalyzing flux) predicts precisely
                          # this null — no solar-correlated excess, any bound however deep stays empty.

lik_solarnull_H20 = 0.13  # 0.13× as expected as under H-41. H-20 is by definition the "detectable
                          # ~20-55 MeV solar neutrino flux" scenario, so most of its parameter space
                          # predicts a signal Super-K would have caught — this exact null is expected only
                          # in the sliver it cannot reach. Not tiny, because A-42/E-11's model dependence
                          # marks real escape room: capture efficiency degrades above ~10^17 GeV monopole
                          # mass, plus sub-central accumulation, weak sigma_0, low pi+ branching. The bound
                          # sits >8 orders below direct limits (probes deep into H-20), so the ratio stays
                          # small; E-11 body: discrimination "strong but not total". Conditioned strictly on
                          # H-20 — its low prior plausibility is step 7's job, not priced here.

t_solarnull = 0.9         # = cap = min trust_score over {O-27, O-28}, both via S-33 = 0.9. No dock: a large,
                          # well-characterised water-Cherenkov detector (22.5 kt, 2853 live days), and A-42
                          # is approved so the raw-null → flux-bound inversion is valid — its model
                          # dependence discriminates and so lives in lik_solarnull_H20, not in t (rule 5).
evidence("HC-9", ["O-27", "O-28"], [lik_solarnull_H20, lik_solarnull_H41], t=t_solarnull)
```
