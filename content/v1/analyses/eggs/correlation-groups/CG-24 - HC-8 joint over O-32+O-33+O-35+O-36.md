---
type: correlation-group
id: CG-24
to: "[[HC-8 - Causal status of elevated TMAO for human atherosclerosis]]"
members:
  - "[[E-59 - O-32 x HC-8 — dietary TMAO supplementation raises plaque in mice]]"
  - "[[E-67 - O-33 x HC-8 — TMAO drives macrophage foam-cell formation]]"
  - "[[E-68 - O-35 x HC-8 — suppressing gut-flora TMAO abolishes atherosclerosis]]"
  - "[[E-69 - O-36 x HC-8 — FMO3 (TMAO-generating enzyme) segregates with lesion area]]"
---

Joint likelihood for correlated observations O-32, O-33, O-35, O-36 (shared basis: S-28). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-24 (HC-8) — ONE joint estimate over E-59+E-67+E-68+E-69: O-32/O-33/O-35/O-36 all rest on S-28's own mouse
# experiments (rule 1). Judged as one pattern: the orthogonal mouse causal chain — dietary TMAO/choline raises
# aortic plaque tracking TMAO and NOT lipids (O-32), choline/TMAO upregulate macrophage scavenger receptors ->
# foam cells (O-33), antibiotic flora-suppression drops TMAO ~100x and abolishes the ~3-fold choline
# atherosclerosis (O-35), and hepatic FMO3 + an FMO3-region SNP co-segregate with lesion area and TMAO (O-36).
# A-11 (approved): these orthogonal lines establish a genuine causal choline->flora->TMAO->atherosclerosis chain
# IN MICE. Members in HC-8.hypotheses order [H-15 real mechanism/human-open, H-16 human-causal, H-45 human marker].
# Anchored on the mechanism poles = 1 (rule 7): pure mouse data cannot separate H-15 from H-16 (both posit a real
# mechanism), so they price equal; it separates the marker pole.
lik_mouse_H15 = 1.0  # anchor: the whole orthogonal mouse chain (necessity + sufficiency + host genetics,
                     # lipid-independent) is exactly H-15's claimed mechanism — fully predicted
lik_mouse_H16 = 1.0  # equal to H-15: mouse data alone cannot tell "mechanism real, human translation open" from
                     # "human-causal established"; both require the same real mechanism this chain demonstrates
lik_mouse_H45 = 0.5  # ~0.5x: a clean causal chain — especially direct TMAO supplementation reproducing plaque
                     # (sufficiency) — is ~2x more expected if TMAO is genuinely atherogenic than under marker-only.
                     # NOT lower because H-45 is a HUMAN claim: per the step brief, mouse->human translation is a
                     # member-discrimination RATIO here, not a t dock — a real mouse mechanism that fails to
                     # translate is fully available to H-45, so mouse data discriminate it only moderately. A-11
                     # closes the "mouse data is artifact" escape but not the "real in mice, marker in humans" one
t_mouse = 0.72       # cap = trust_score(S-28) = 0.72 (O-32/33/35/36 all via S-28). At cap: Wang 2011 Nature
                     # primary mouse experiments, orthogonal designs; no raw-data->observation weakness beyond what
                     # 0.72 encodes, and translation uncertainty is priced in the ratios above, not here
evidence("HC-8", ["O-32", "O-33", "O-35", "O-36"], [lik_mouse_H15, lik_mouse_H16, lik_mouse_H45], t=t_mouse)
```
