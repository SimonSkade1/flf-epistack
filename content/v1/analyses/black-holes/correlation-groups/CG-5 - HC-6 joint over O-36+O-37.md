---
type: correlation-group
id: CG-5
to: "[[HC-6 - Origin of the UHECR spectral structure]]"
members:
  - "[[E-16 - O-36 × HC-6 — HiRes 5.3-sigma suppression]]"
  - "[[E-17 - O-37 × HC-6 — E-half matches GZK prediction]]"
---

Joint likelihood for correlated observations O-36, O-37 (shared basis: D-9). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-5 (HC-6) — ONE joint estimate over members E-16 + E-17: both observations are derived from the SAME
# HiRes monocular spectra (source S-60, instrument D-9), so they are one witness, not two (rule 1). The
# pattern judged whole: a 5.3-sigma flux suppression with the break at log10 E = 19.75±0.04 (O-36) AND the
# integral-spectrum E_1/2 = 10^(19.73±0.07) eV landing on the parameter-insensitive proton-GZK prediction
# 10^19.76 eV (O-37). Members in HC-6.hypotheses order [H-9 GZK extragalactic-proton propagation, H-12
# He/CNO source-rigidity-maximum, H-21 heavy-Galactic-to-light-extragalactic transition at the dip, H-37
# residual]. Anchored on H-9 = 1; others priced as ratios to it (rule 7).

lik_supp_H9 = 1.0   # anchor: H-9 is the ONLY member predicting BOTH halves at once — a suppression AND
                    # its location + E_1/2 at exactly the parameter-free GZK-proton scale. This whole
                    # pattern is what H-9 forces, so it is maximally expected here.
lik_supp_H12 = 0.35  # 0.35x: a He/CNO account with a narrow source rigidity maximum readily produces a
                     # steepening (O-36's existence fits), but as a SOURCE property its energy has no
                     # reason to land on the GZK value, so the E_1/2 match (O-37) is a coincidence under
                     # it. Not crushed: per A-23 (corrected) the E_1/2 test is evidence FOR the proton-GZK
                     # break, not an identification of it — it discriminates against source-spectrum
                     # explanations but a heavy-composition photodisintegration suppression can still sit
                     # near a similar energy, so H-12 keeps a moderate fit rather than near-zero.
lik_supp_H21 = 0.8   # 0.8x: above the ~10^18.5 eV dip H-21 makes the flux light extragalactic (protonic),
                     # which itself undergoes GZK losses — so it predicts a suppression and E_1/2 near the
                     # GZK scale almost as well as H-9. These two observations barely separate H-21 from
                     # H-9 (their discriminating power vs H-21 lives at the dip, not here); only slightly
                     # below the anchor for H-21's less-clean high-energy proton purity.
lik_supp_H37 = 0.3   # 0.3x: unlisted/exotic/instrumental cause, unconstrained — the instrumental branch
                     # predicts NO break at all, and no unlisted cause has a reason to reproduce a break at
                     # the exact GZK energy with a matching parameter-free E_1/2. Slightly below middling
                     # for that specific double coincidence; not near zero, since an exotic top-down source
                     # could mimic a cutoff (rule 3).
t_hires = 0.7        # cap = min trust_score over {O-36, O-37} = 0.8 (both via S-60). Docked below it: the
                     # load-bearing discriminator is the ABSOLUTE-energy match of the break and E_1/2 to
                     # the GZK scale, but D-9 carries a ~17% energy-scale systematic (fluorescence-yield /
                     # calibration / aperture-MC) common to both observations — it shifts break-location
                     # and E_1/2 together, so the shared witness could move the match without the
                     # per-observation error bars flagging it.
evidence("HC-6", ["O-36", "O-37"], [lik_supp_H9, lik_supp_H12, lik_supp_H21, lik_supp_H37], t=t_hires)
```
