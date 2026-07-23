---
type: correlation-group
id: CG-30
to: "[[HC-10 - Intrinsic versus comparator-background-diet contingency of egg-health (is the verdict well-posed)]]"
members:
  - "[[E-88 - O-39 x HC-10 — removing eggs vs healthy proteins lowers CVD]]"
  - "[[E-89 - O-40 x HC-10 — removing eggs vs healthy proteins lowers mortality]]"
  - "[[E-90 - O-41 x HC-10 — egg-removal depends on comparator, eggs rank near processed meat]]"
---

Joint likelihood for correlated observations O-39, O-40, O-41 (shared basis: D-1). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-30 (HC-10) — ONE joint estimate over E-88+E-89+E-90: O-39/O-40/O-41 all from the Lifetime Risk Pooling
# Project substitution analysis D-1 / S-89 (rule 1). One pattern: isocalorically replacing 1 serving/day of eggs
# with nuts/legumes/whole grains/fish lowers CVD 15-21% (O-39) and with nuts/fish/poultry/whole grains/legumes
# lowers all-cause mortality 11-22% (O-40), while the effect depends on the comparator — eggs->processed meat
# gives no reduction and eggs->unprocessed red meat still lowers risk, placing eggs near processed meat at the
# bottom (O-41). Members in HC-10.hypotheses order [H-17, H-18, H-23, H-38, H-57]. The pattern reads as a stable
# low rank for eggs; anchored on H-17 = 1 (rule 7).
lik_sub_H17 = 1.0   # anchor: a fixed intrinsic low rank predicts exactly this — removing eggs for almost any
                    # healthier protein helps, removing for equally-unhealthy processed meat does not, eggs at bottom
lik_sub_H18 = 0.7   # ~0.7x: O-41's comparator-dependent sign supports comparator-contingency (A-13 approved:
                    # a substitution HR is definitionally comparator-relative, identifying no unconditional egg
                    # effect), but the CONSISTENT removal benefit across many comparators (O-39/O-40) reads as a
                    # stable fixed rank, which "no fixed effect" fits a little worse than H-17
lik_sub_H23 = 0.2   # ~0.2x: directly contradicted — removing eggs even for fish/poultry/plant lowers risk (eggs
                    # NOT neutral vs those, against H-23), and eggs rank near/at processed meat with
                    # egg->unprocessed-red-meat still beneficial (against H-23's "eggs preferable to red meat")
lik_sub_H38 = 0.5   # ~0.5x middling: a single-region (US) substitution pattern does not engage H-38's
                    # background-diet / geographic mechanism; mild consistency at most (eggs look harmful in a
                    # Western population), no specific prediction of this substitution structure
lik_sub_H57 = 0.6   # ~0.6x: a partly-intrinsic / partly-contingent hybrid fits naturally — a stable low rank
                    # (intrinsic-like) PLUS comparator-dependence (contingent-like) — so the residual reads
                    # slightly above its usual middling (A-14 approved notes the per-day benefit reaches only the
                    # ~8% high-intake minority, a magnitude caveat not a member-discrimination one)
t_sub = 0.62        # cap = trust_score(S-89) = 0.62 (O-39/O-40/O-41 all via S-89). At cap: substitution HRs are
                    # model-derived like all such analyses but faithfully reported; the comparator-relativity (A-13)
                    # and population-relevance (A-14) points are interpretation, not data-reliability weaknesses
evidence("HC-10", ["O-39", "O-40", "O-41"], [lik_sub_H17, lik_sub_H18, lik_sub_H23, lik_sub_H38, lik_sub_H57], t=t_sub)
```
