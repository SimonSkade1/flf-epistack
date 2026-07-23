---
id: A-31
type: argument
statement: "Because higher egg intake produced no rise in LDL or total cholesterol (and lower blood pressure), the dietary-cholesterol-to-lipids-to-CVD pathway that motivates limiting eggs is not engaged here, so the null clinical result is mechanistically coherent rather than a harm masked by confounding."
source: "[[S-91 - PURE study- egg intake, blood lipids, CVD and mortality in 50 countries (Dehghan 2020)]]"
locator: "Discussion (competing factors)"
affects_observations: ["[[O-85 - Higher egg intake not associated with adverse blood lipids and associated with slightly lower blood pressure in PURE]]"]
affects_hypotheses: ["[[H-37 - Moderate habitual egg intake up to one per day is neutral for CVD and mortality across income levels globally]]"]
status: approved
reason_if_not_false: checked
---
The prior reason to expect harm from eggs is the causal chain: egg cholesterol -> higher serum LDL / total cholesterol -> higher CVD risk. In this dataset the first link is absent: across egg categories, total cholesterol, LDL-C, HDL-C, TC:HDL and ApoB:ApoA1 are flat (P-trend >0.20) and blood pressure is slightly lower at higher intake.

If the mediating lipid change does not occur, the causal model predicts no downstream clinical harm, so the observed null on CVD and mortality is exactly what that mechanism would produce. This makes it less plausible that the clinical null merely reflects a true harm cancelled by unmeasured confounding, because the proposed harm mechanism itself is not operating. The authors note additionally that egg phospholipids raise HDL, which can offset any small LDL effect. This coherence inference links the lipid observation to the clinical null and supports taking the null at face value rather than as a confounding artefact.

## Validity verdict — approved (checked)

Reconstruction. Premise: across egg categories, serum lipids are flat (TC, LDL-C, HDL-C, TC:HDL, ApoB:ApoA1, P-trend >0.20) and BP slightly lower (O-85). Prior harm model: egg cholesterol → ↑LDL/TC → ↑CVD. Conclusion: with the first link absent, the null CVD/mortality result is what this mechanism predicts (mechanistic coherence), making it *less* plausible that the null masks a true harm cancelled by confounding.

Traced step. Two moves. (1) If the mediating lipid change is absent, the stated causal model predicts no downstream harm, so a null clinical result is expected rather than surprising — valid within that model. (2) The coherence move: a "harm masked by confounding" story requires a live harm pathway; the *main a-priori* pathway (lipids) being idle removes the most-expected such pathway, so the confounding-masked-harm hypothesis loses some prior — modestly, not decisively. Probed defeater: "eggs could harm via non-lipid pathways (e.g. TMAO/choline), so absence of the lipid pathway doesn't remove all harm." This does not undercut, because the statement is explicitly scoped to "the *main* a-priori pathway" and claims only "less plausible," not "impossible." A second candidate defeater — the flat lipids are themselves cross-sectional/observational and could be a confounding artefact — would, if the premise were false, weaken the first link; but validity is judged conditional on the premise (lipids genuinely flat), under which the step holds. Appropriately scoped and hedged; step holds as stated.
