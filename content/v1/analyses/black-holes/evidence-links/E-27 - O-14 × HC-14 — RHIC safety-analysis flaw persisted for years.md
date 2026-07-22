---
id: E-27
type: evidence-link
from: "[[O-14 - The RHIC strangelet safety analysis ran five years before its anthropic-selection flaw was found and corrected]]"
to: "[[HC-14 - Locus of the residual LHC catastrophe probability]]"
---
![[O-14 - The RHIC strangelet safety analysis ran five years before its anthropic-selection flaw was found and corrected]]

## Why this is evidence

The most direct discriminator in the corpus: a published accelerator-safety argument in precisely the class at issue (cosmic-ray/Earth-survival bounds) contained a serious unnoticed flaw — ignored anthropic observation selection — that survived peer review and years of operation before Tegmark & Bostrom corrected it. H-11 predicts flaws of this kind occur at a non-negligible rate in exactly these arguments; H-46, which holds that this argument class is robust enough for its conditional bounds to carry through undiluted, makes a documented in-class failure distinctly less expected. (That the corrected analysis still bounded the risk low is likelihood-relevant detail for the pricing step, not a reason to withhold the edge.)

## Likelihood

```python
# E-27 (HC-14) — lone edge, one observation O-14 "the RHIC strangelet safety analysis ran ~5 yr before its
# anthropic-selection flaw was found & corrected". Members in HC-14.hypotheses order [H-11, H-46];
# exhaustive_by_construction, NO residual. Price ONLY the INCREMENTAL discrimination of this one same-class
# datum: the prior already rests on E-24 (general scientific error rates ~1e-3), E-26 (Castle Bravo model
# failure) and A-2 (layering). What O-14 adds beyond those outside-view facts is a precedent inside the EXACT
# genre at issue — a pivotal cosmic-ray/Earth-survival accelerator-safety argument that carried a serious
# unnoticed flaw through ~5 yr of operation. Anchored on H-11 = 1 (rule 7).
lik_rhic_H11 = 1.0   # anchor: H-11 (argument-failure dominates the actionable P(X)) predicts flaws in exactly
                     # these arguments at a non-negligible rate — a documented in-class instance is just what it expects
lik_rhic_H46 = 0.55  # 0.55x as expected under H-46 (arguments robust, conditional bounds carry through
                     # undiluted): a serious in-class flaw persisting ~5 yr cuts against robustness. Not lower
                     # because only the same-class SPECIFICITY is new here (general error rates already priced
                     # into the prior via E-24/E-26), it is n=1, and it was self-correcting — the corrected
                     # analysis still bounded risk <1e-12/yr, the kind of layered self-repair H-46 leans on
t_rhic = 0.75        # cap = trust_score(S-44, Ord-Hillerbrand-Sandberg) = 0.8; docked slightly: the timeline
                     # is solid historical fact, but the "serious flaw" severity is the source's interpretive
                     # judgment (the corrected bound stayed benign), so how much weight the episode carries is contestable
evidence("HC-14", ["O-14"], [lik_rhic_H11, lik_rhic_H46], t=t_rhic)
```
