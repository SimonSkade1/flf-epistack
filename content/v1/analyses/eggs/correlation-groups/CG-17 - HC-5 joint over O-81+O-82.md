---
type: correlation-group
id: CG-17
to: "[[HC-5 - Operative exposure behind the egg-cardiovascular association]]"
members:
  - "[[E-118 - O-81 x HC-5 — cholesterol response is genotype-invariant, unlike fat]]"
  - "[[E-119 - O-82 x HC-5 — genotype modulates the fat response but not cholesterol]]"
---

Joint likelihood for correlated observations O-81, O-82 (shared basis: S-62). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-17 (HC-5) — ONE joint estimate over E-118 + E-119: both rest on S-62 (Weggemans 2001 pooled reanalysis),
# so priced together (rule 1). Members [H-3, H-26, H-54]. Joint pattern: the LDL-C response to dietary
# cholesterol was genotype-invariant and small (O-81), while the saturated-fat response was genotype-modulated,
# larger in APOE E4 carriers (O-82). A modifiable fat response but none for cholesterol marks fat as the more
# potent lever. Anchored on H-3 = 1.0. A-28 (approved) tempers strength: the fat genotype effect is small, CI crosses zero.
lik_genotype_H3 = 1.0   # anchor: a genotype-modulated (biologically real) fat response alongside a flat
                        # cholesterol response is what H-3 (fat the larger determinant) predicts.
lik_genotype_H26 = 0.6  # 0.6x: a small, genotype-invariant cholesterol response sits awkwardly with H-26's
                        # cholesterol-as-operative-lever, but only modestly — H-26 concerns the population-mean
                        # exposure, not genotype modification, and A-28 shows the discriminating fat effect
                        # (0.08 mmol/L, CI -0.01 to 0.18) is small and not statistically robust.
lik_genotype_H54 = 0.65 # 0.65x middling: a fat-vs-cholesterol genotype contrast is largely orthogonal to whether
                        # the operative exposure is a non-cholesterol component or confounding; set slightly above
                        # H-26 only because it is neutral rather than mildly demoted (rule 3).
t_genotype = 0.6        # cap = trust over {O-81, O-82} = S-62 0.6. Held at cap: O-81 is depth-limited (abstract +
                        # step-2 summary, full text paywalled), but the quoted genotype comparisons are the
                        # observation; retrospective genotyping / pooled reanalysis are design features already in the score.
evidence("HC-5", ["O-81", "O-82"], [lik_genotype_H3, lik_genotype_H26, lik_genotype_H54], t=t_genotype)
```
