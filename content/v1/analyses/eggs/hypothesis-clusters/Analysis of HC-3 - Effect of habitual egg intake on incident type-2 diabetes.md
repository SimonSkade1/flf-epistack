---
type: cluster-review
cluster: "[[HC-3 - Effect of habitual egg intake on incident type-2 diabetes]]"
---
#### What the analysis says

Does habitual egg intake causally raise incident type-2 diabetes, and how uniform is that across regions? Three members: `[[H-8 - Egg-T2D association is region-population-dependent - positive in US, null in Europe, null-to-inverse in Asia]]` (a real region-dependent causal effect), `[[H-9 - US egg-T2D association reflects residual confounding by the co-consumed Western dietary pattern, not a causal egg effect]]` (uniform null; the US-positive signal is confounding), and residual `[[H-51 - Some other egg-T2D structure]]` (a uniform modest effect in every region). The prior already made confounding the modal reading of a weak single-food association (RR ~1.1-1.2): [0.298, 0.540, 0.162]. The posterior [0.215, 0.723, 0.062] hardens that — H-9 to 0.723, H-8 down, the uniform-effect residual squeezed to 0.062.

One joint observation does all of it (`[[CG-8 - HC-3 joint over O-17+O-31+O-29+O-18+O-43+O-19+O-15]]`, anchored H-9=1.0, H-8=0.45, H-51=0.25, t=0.75). The pattern read whole: a US 1.18 (I2=0%) / non-US 0.97 gradient with Europe null and Asia inverse; the association concentrating at low diet quality (O-18); eggs co-occurring with the Western basket (O-43); substitution benefit only versus prudent foods, none versus other animal proteins (O-19); and a sex-fragile US signal null in men (O-15). Confounding predicts the whole of this; region-dependent causation predicts only the bare gradient.

#### What the model may not capture

The discrimination is entirely indirect. The block itself notes the bare gradient (O-17/O-31/O-29) does not separate H-8 from H-9 — H-9's 2.3x edge comes wholly from the within-population features (diet-quality modification, substitution signature, sex-fragility), read as confounding fingerprints. But those same features are compatible with a small real effect riding on top of confounding; the model treats them as near-decisive for pure null. The two listed members may also not be cleanly exclusive: "small uniform causal effect largely masked by variable confounding" is neither H-8 (region-dependent) nor a true null, and is closer to residual H-51, which the arithmetic drove to 0.062.

Is the answer on the list? Two unlisted candidates — reverse causation (incipient dysglycemia changing egg intake) and eggs as a marker of ultra-processed co-consumption — both masquerade as H-9's confounding rather than form a distinct member, so their consequence is low: they land in the same "not causal" place H-9 already occupies. That is why the comfortable-looking 0.723 is probably not hiding much out-of-model risk here.

#### What would help

Mendelian-randomization or genetic-instrument estimates of egg intake on incident T2D — *exists, unread* (would most directly separate causation from confounding and is the single highest-value item). A within-region analysis stratified on diet quality that tests whether the egg signal survives full dietary-pattern adjustment — *exists, unread*. A mechanism for the Asian inverse association (is it eggs, or the prudent-diet context they mark?) — *unclear*.

#### Confusions and contradictions

Little that is irreducible — the pattern is internally coherent under confounding. The one genuine tension is the US I2=0%: the positive association is highly consistent across US cohorts, which H-8 explains cleanly as real effect modification, whereas H-9 must attribute that tight consistency to uniformly-strong US confounding — a softer story that the model nonetheless favours on base rates. Whether homogeneous within-region positivity is better read as a real effect than as consistent confounding is the live question the posterior settles by prior weight rather than by evidence that cleanly discriminates.
