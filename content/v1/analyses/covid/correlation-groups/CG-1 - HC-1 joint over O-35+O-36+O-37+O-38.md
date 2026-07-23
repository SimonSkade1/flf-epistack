---
type: correlation-group
id: CG-1
to: "[[HC-1 - Origin of SARS-CoV-2 — natural zoonosis vs research-related incident]]"
members:
  - "[[E-49 - O-35 × HC-1 — WIV a designated executing partner in DEFUSE]]"
  - "[[E-50 - O-36 × HC-1 — DEFUSE planned chimeras and hACE2-mouse testing]]"
  - "[[E-51 - O-37 × HC-1 — DEFUSE proposed inserting furin cleavage sites]]"
  - "[[E-52 - O-38 × HC-1 — DEFUSE planned chimeric-spike work]]"
---

Joint likelihood for correlated observations O-35, O-36, O-37, O-38 (shared basis: S-65). Step 8 writes the single `## Likelihood` block here; the member edges point back via `group`.

## Likelihood

```python
# CG-1 (HC-1) — ONE joint estimate over members E-49+E-50+E-51+E-52: all four observations (O-35 the DEFUSE
# consortium with WIV as an executing partner; O-36 chimera + hACE2-mouse plan; O-37 furin/human-specific
# cleavage-site insertion; O-38 chimeric-spike work) are extracted from the single DEFUSE proposal document
# S-65 (rule 1 — one witness; if the document is misread, all four are misread together). Judged as ONE
# pattern: in March 2018 the EcoHealth/WIV/UNC consortium, in the outbreak's own city, put in writing exactly
# the manipulations later debated in SARS-CoV-2's genome. This is a document about a PLAN, not evidence the
# plan was executed (A-47), so it LIFTS the engineered member over natural zoonosis but is bounded to "raises,
# cannot confirm" — a means-motive-opportunity update (A-46), not an observation of the virus itself. Anchored
# on H-43 = 1 (the member the whole pattern best fits); the rest priced as ratios to it (rule 7). Not
# double-counted with the prior: HC-1's prior explicitly excluded the DEFUSE feature-match (A-39 -> E-49/E-51)
# as belonging to this step-8 edge.

lik_defuse_H43 = 1.0   # anchor: engineered lab leak at these institutions is the only member for which the
                       # document is more than coincidence — the same institutional capability/intent that
                       # would build the construct is what wrote the plan (common cause). A-46 MMO update:
                       # documented intent (the furin/cleavage-site plan) + means (Baric's reverse-engineering
                       # track record, WIV sampling) + opportunity (WIV's own city, 20 months prior). Does NOT
                       # observe the genome — that evidence lives on the genome edges — so it raises, not confirms.

lik_defuse_H42 = 0.6   # 0.6x as expected as under H-43: H-42 (leak of an UNMODIFIED field-collected virus) is
                       # genuinely lifted by O-35 — DEFUSE documents an active WIV program sampling and handling
                       # exactly this bat-SARSr-CoV family, which is the collection/handling route H-42 posits.
                       # But the engineering-specific content (O-36/O-37/O-38) is not predicted by an unmodified
                       # virus, so H-42 earns the research-proximity lift only, well below the engineered member.
                       # ~1.4x over H-41. Confidence moderate — the split rests on which observations discriminate.

lik_defuse_H41 = 0.42  # 0.42x: under pure natural zoonosis with no research role, a specific matching plan
                       # existing in the outbreak city ~2yr prior is a coincidence, so the MMO update (A-46)
                       # penalises H-41 relative to the research members. BOUNDED, not extreme (A-47 caps the
                       # force): EcoHealth/WIV were the world's dominant bat-CoV labs, so a matching aggressive-
                       # work proposal near a natural southern-China / Wuhan-hub emergence is not astronomically
                       # unlikely; and the document is a REJECTED proposal, chimera work slated for UNC, on
                       # SARS-1-related WIV1/SHC014 backbones outside SARS-CoV-2's lineage — hence ~2.4x, not 10x.

lik_defuse_H44 = 0.55  # 0.55x: unlisted/hybrid origin, unconstrained — a middling value near H-42 (rule 3).
                       # Some residual histories involve these institutions (raising the document's
                       # expectedness), others do not; the residual neither strongly predicts nor forbids the
                       # pattern. Not set near 0 (would assert no unlisted origin could coincide with such a
                       # plan, which I don't know) nor near 1.

t_defuse = 0.90        # cap = trust_score of S-65 = 0.90 (the min over {O-35,O-36,O-37,O-38}; all four carry
                       # data_basis S-65). No dock: authenticity is very high (DRASTIC leak, DARPA-confirmed
                       # receipt+rejection, never disputed by EcoHealth) and the facts are documentary and
                       # directly checkable; the degraded-OCR quotes are reconciled to the widely-circulated
                       # verbatim text, and O-38's 'GoF-exempt' framing is EcoHealth advocacy but the
                       # observation is only that they ASSERTED it, which is faithful. So t sits at the cap.

evidence("HC-1", ["O-35", "O-36", "O-37", "O-38"], [lik_defuse_H41, lik_defuse_H42, lik_defuse_H43, lik_defuse_H44], t=t_defuse)
```
