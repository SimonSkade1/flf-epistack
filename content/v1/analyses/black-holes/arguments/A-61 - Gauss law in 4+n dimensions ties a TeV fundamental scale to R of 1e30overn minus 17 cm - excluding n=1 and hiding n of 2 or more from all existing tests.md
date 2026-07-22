---
id: A-61
type: argument
statement: "Gauss's law in 4+n dimensions gives V(r) ∝ 1/(M_(4+n)^(n+2) r^(n+1)) for r << R and the usual 1/r potential with M_Pl^2 ~ M_(4+n)^(2+n) R^n for r >> R; demanding M_(4+n) ~ 1 TeV and the observed M_Pl fixes R ~ 1e(30/n - 17) cm — so n=1 (R ~ 1e13 cm, solar-system scales) is empirically excluded, while for every n ≥ 2 the modification of gravity sets in below the distances probed by any 1998 experiment (n=2: R ~ 100 microns - 1 mm, exactly the range planned sub-millimeter gravity experiments would reach)."
source: "[[S-15 - Arkani-Hamed, Dimopoulos, Dvali 1998 — the ADD large-extra-dimensions model]]"
locator: "§1, eqs. (1)-(4)"
affects_observations: ["[[O-43 - As of 1998 gravity had been accurately measured only down to about a centimeter - 33 untested orders of magnitude above the Planck length]]"]
affects_hypotheses: ["[[H-30 - The hierarchy problem is solved by n of 2 or more large gravity-only extra dimensions with the true Planck scale at about a TeV]]"]
status: approved
reason_if_not_false: checked
---
Reasoning (the calculation):

1. For two masses within r << R, gravitational flux spreads through all 4+n dimensions: V(r) ~ m1 m2 / (M_(4+n)^(n+2) r^(n+1)). For r >> R flux lines cannot penetrate the compact dimensions further, giving V(r) ~ m1 m2/(M_(4+n)^(n+2) R^n r): the effective 4D coupling is M_Pl^2 ~ M_(4+n)^(2+n) R^n (eq. 3).
2. Setting M_(4+n) = m_EW ~ 1 TeV and solving for R: R ~ 1e(30/n) x 1e-17 cm x (1 TeV/m_EW)^(1+2/n) (eq. 4). n=1 → 1e13 cm: gravity would deviate from Newton at solar-system distances — excluded. n=2 → 0.1-1 mm; n=6 → ~1e-12 cm. Since gravity was untested below ~1 cm, every n ≥ 2 was consistent with all data.
3. Because the SM is measured to weak-scale distances, its fields cannot propagate in the extra dimensions and must be localized to a 4D wall of thickness ~1/m_EW; only the graviton lives in the bulk. Charge conservation still holds on the wall (massless gauge fields are localized; an escaping charge stretches a flux tube of tension ~m_EW^2 that pulls it back or breaks into charge pairs), while energy can be carried into the bulk above threshold — the sharp p_T cutoff and fireworks signatures.

## Step 6 verdict

Verdict: approved (checked). Traced: flux spreading in 4+n dimensions gives V ~ 1/(M^(n+2) r^(n+1)) for r << R; matching at r ~ R yields M_Pl^2 ~ M^(2+n) R^n; solving with M = 1 TeV reproduces R ~ 1e(30/n - 17) cm. n=1 -> 1e13 cm (solar-system-scale deviation, excluded); n=2 -> ~0.1 mm, below the ~1 cm 1998 gravity frontier (O-43), so all n >= 2 were untested. O(2pi)^n compactification-convention factors shift R by less than an order and do not touch the conclusion. The wall-localization corollary (SM fields measured to weak-scale distances must be brane-bound; charge conservation via the flux-tube argument) is coherent. Valid.
