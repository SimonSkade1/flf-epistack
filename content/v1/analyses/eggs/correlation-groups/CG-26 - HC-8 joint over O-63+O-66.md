---
type: correlation-group
id: CG-26
to: "[[HC-8 - Causal status of elevated TMAO for human atherosclerosis]]"
members:
  - "[[E-72 - O-63 x HC-8 — raising TMAO ~6-fold raised platelet reactivity in humans]]"
  - "[[E-73 - O-66 x HC-8 — platelet reactivity correlates with TMAO in humans]]"
---

Joint likelihood for correlated observations O-63, O-66 (shared basis: S-60). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-26 (HC-8) — ONE joint estimate over E-72+E-73: O-63 and O-66 both from the Wilcox 2021 RCT S-60 (rule 1).
# One pattern: free choline (~411 mg/d) raised fasting TMAO ~6-fold and increased platelet responsiveness
# (O-63, interventional positive control), and platelet responsiveness correlated with TMAO across participants
# (O-66, r~0.5, P<0.0001). Members in HC-8.hypotheses order [H-15, H-16, H-45]. A human functional TMAO->platelet
# coupling is H-16's territory (elevated TMAO biologically active in humans); it favors H-16 over both the marker
# pole (H-45) and the mouse-mechanism/human-open pole (H-15, which names foam cells not platelets and leaves
# translation open). Anchored on H-16 = 1 (rule 7).
lik_plat_H16 = 1.0   # anchor: TMAO being a functionally active human CVD effector predicts exactly this
                     # interventional rise + within-cohort platelet correlation
lik_plat_H45 = 0.6   # ~0.6x: under marker-only, raising TMAO should not itself move platelet function — but E-72
                     # flags the intervention is confounded by choline acting directly (A-22 approved isolates
                     # choline FORM as the TMAO determinant but does not rule out choline's direct platelet effect),
                     # and E-73 notes the cross-sectional correlation is compatible with a shared confounder, so
                     # H-45 can still produce the pattern; a genuine coupling is only moderately more expected under H-16
lik_plat_H15 = 0.6   # ~0.6x: H-15 leaves human translation open and names the macrophage/foam-cell pathway, not
                     # platelets, so a human platelet coupling is not its specific prediction — priced level with
                     # H-45, i.e. CG-26 lifts H-16 modestly over both
t_plat = 0.72        # cap = trust_score(S-60) = 0.72. At cap: a validated far-from-threshold positive control
                     # (6-fold rise, P<0.0001) and a highly significant correlation (P<0.0001); the choline-direct
                     # confound is member discrimination (priced above), not a raw-data reliability weakness
evidence("HC-8", ["O-63", "O-66"], [lik_plat_H15, lik_plat_H16, lik_plat_H45], t=t_plat)
```
