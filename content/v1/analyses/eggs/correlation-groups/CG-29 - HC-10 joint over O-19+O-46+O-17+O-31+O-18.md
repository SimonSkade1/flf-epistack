---
type: correlation-group
id: CG-29
to: "[[HC-10 - Intrinsic versus comparator-background-diet contingency of egg-health (is the verdict well-posed)]]"
members:
  - "[[E-87 - O-19 x HC-10 — egg-removal effect comparator-dependent (T2D)]]"
  - "[[E-91 - O-46 x HC-10 — Harvard substitution eggs neutral vs healthy better than red-processed meat]]"
  - "[[E-92 - O-17 x HC-10 — egg-T2D region gradient US-Europe-Asia]]"
  - "[[E-93 - O-31 x HC-10 — egg-T2D US vs non-US split]]"
  - "[[E-95 - O-18 x HC-10 — egg-T2D interaction with background diet quality]]"
---

Joint likelihood for correlated observations O-19, O-46, O-17, O-31, O-18 (shared basis: D-7, D-9, D-25). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-29 (HC-10) — ONE joint estimate over E-87+E-91+E-92+E-93+E-95: O-19/O-46/O-17/O-31/O-18 rest on the
# overlapping Harvard / meta cohort sets D-7, D-9, D-25 (rule 1; O-17 & O-31 restate the same US/non-US split on
# shared cohorts). One pattern: the egg signal is heavily comparator- and context-dependent — egg-removal for
# T2D benefits only vs whole grains/nuts/dairy and is null vs other animal proteins (O-19); eggs neutral vs
# fish/poultry/plant and worse only than red/processed meat or full-fat milk for CVD (O-46); a US-harmful /
# Asia-protective T2D region gradient (O-17, O-31); and a stronger egg-T2D association at lower overall diet
# quality (O-18). Members in HC-10.hypotheses order [H-17 intrinsic, H-18 ill-posed, H-23 substitution-indexed,
# H-38 background-diet-indexed, H-57 residual]. The whole pattern is broad contingency, fitting H-18 best;
# anchored H-18 = 1 (rule 7).
lik_ctx_H18 = 1.0   # anchor: "no fixed egg effect, verdict comparator/context-dependent" predicts the whole
                    # pattern — the substitution swings AND the region/diet-quality gradients
lik_ctx_H17 = 0.2   # ~0.2x: a fixed intrinsic low rank is directly contradicted — eggs equivalent to
                    # poultry/fish/legumes (O-19) and neutral vs fish/poultry/plant (O-46) deny "eggs worse than
                    # those foods," and a region/diet-quality-varying sign denies a fixed property. Strongly disfavored
lik_ctx_H23 = 0.75  # ~0.75x: substitution-indexing nails O-46 (its signature) and O-19, but per E-92 a
                    # comparator-only frame does not by itself predict a between-population region split (O-17/O-31)
                    # or a diet-quality interaction (O-18), so a notch below the broad-contingency anchor
lik_ctx_H38 = 0.6   # ~0.6x: background-diet-indexing nails the region gradient (Asia-protective, O-17/O-31), but
                    # O-18's DIRECTION (more harmful at LOWER diet quality) is opposite to H-38's specific
                    # refined-carb-displacement claim (E-95), and the substitution swings are not its prediction —
                    # net moderate. A-5/A-10 (approved) read the US/diet-quality dependence as Western-pattern
                    # confounding, a contingency reading generally rather than H-38's particular direction
lik_ctx_H57 = 0.5   # ~0.5x middling (rule 3): a partly-intrinsic/partly-contingent or otherwise-characterized
                    # model accommodates the messy pattern but does not outpredict the clean contingency members here
t_ctx = 0.75        # cap = min trust_score over sources {S-4 0.78, S-19 0.82, S-8 0.75} = 0.75. At cap: large
                    # pooled cohorts / meta-analyses; the overlapping-cohort correlation is handled by this joint
                    # call, and the model-derived nature of substitution estimates is an interpretation caveat
                    # (A-6 corrected: null contrasts are consistent-with not proof-of equivalence), not a raw-data
                    # reliability weakness
evidence("HC-10", ["O-19", "O-46", "O-17", "O-31", "O-18"], [lik_ctx_H17, lik_ctx_H18, lik_ctx_H23, lik_ctx_H38, lik_ctx_H57], t=t_ctx)
```
