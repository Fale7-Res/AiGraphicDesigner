<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-17T08:10:55Z", "last_action": "EDITED", "last_change_id": "TASK-P0-ARCH-REVIEW", "last_edited_at_utc": "2026-10-17T09:32:29Z", "last_editor": "scene-and-vision-agent", "tracking_started_at_utc": "2026-10-17T08:10:55Z"}
END_DOC_PROVENANCE -->
# Subagent WAL — scene-and-vision-agent — TASK-P0-ARCH-REVIEW

**Subagent ID:** `scene-and-vision-agent`  
**Role:** Computer Vision and Generative AI Architect  
**Task ID:** `TASK-P0-ARCH-REVIEW`  
**Timestamp:** 2026-10-17T08:12:00Z  

## 1. Context & Scope
Received instruction from parent orchestrator to conduct an independent, unvarnished architectural critique of:
- `docs/product/OWNER_ORIGINAL_VISION.md` (read in full, lines 1–13)
- `docs/architecture/VISION_REQUIREMENTS_ANALYSIS.md`
- `docs/architecture/ARCHITECTURE_OPTIONS.md`
- `docs/architecture/SPECIALIST_REVIEWS.md`
- `docs/architecture/DESIGN_IR_PROPOSAL.md`
- `docs/architecture/FEASIBILITY_RESEARCH_PLAN.md`
- `docs/architecture/RISK_REGISTER.md`
- `docs/architecture/ARCHITECTURE_DEBATE_AND_CONFLICTS.md`

## 2. Key Findings & Independent Judgments
1. **Vision Fidelity & Gaps:**
   - Mode 1 (Generation): The owner envisions pre-planning layers, generating the full image, and then generating the layers with the same specifications. Generating individual layers from scratch via diffusion prompts causes severe visual drift; the system must decompose the approved preview image amodally instead of re-generating layers independently.
   - Mode 2 (Magic Layers): Global top-down segmentation (SAM 2) is technically superior to the owner's bottom-up wire-tracing, but this architectural departure must be made transparent to the owner.
   - Mode 3 (Editing): Shadow decoupling is critical; shadows must live inside the object group (`<g id="Potato">`) as semi-transparent vector patches, while underlying bread must have unshadowed amodal reconstruction.
2. **SAM 2 + Grounding DINO Blind Spots:**
   - Contact shadows & ambient occlusion are frequently lumped into the object or background. SAM 2 lacks intrinsic lighting decomposition. A dedicated shadow extraction step is mandatory.
   - Translucent & feathered edges (sauces, crusts) require Alpha Matting (e.g. ViTMatte) rather than binary sigmoid thresholding.
   - Text & glyph boundaries are distorted if passed through standard SAM 2.
3. **LaMa Amodal Inpainting Reality:**
   - LaMa is excellent for background texture completion, but fails at semantic shape reconstruction under heavy occlusion (> 40%). It produces blurry boundaries that create wavy, chaotic Bézier paths when vectorized.
   - Solution: Adopt Geometry-First Amodal Completion (predicting closed Bézier boundary first, or using Amodal Mask Completion like AmodalSAM/AISFormer), with LaMa used strictly for internal texture fill.
4. **Demands on Vector & Canvas Specialists:**
   - Vector: Shared-boundary topology snapping to eliminate micro-gaps; bridging disconnected shadow patches into a single cohesive `<path>`; gradient mesh simplification to linear/radial gradients.
   - Canvas: WebGL/multi-layer composition to maintain 60 FPS during 50% opacity slider overlay; strict JSON mutation contracts to prevent raster/vector desynchronization; RTL and Arabic shaping without FOUT.
5. **Readiness & Experiments:**
   - Overall confidence in Hybrid Architecture: High (85-90%).
   - Confidence in vanilla SAM 2 + LaMa without enhancements: Low (30%).
   - Required enhancements to `EXP-01` and `EXP-03`, plus new shadow decomposition validation.

## 3. [DEBATE-ROUND-01] Peer Challenge Response — Vector Fitting Tolerance & Node Budget
- **Opposing Proposal:** `vector-and-typography-agent` proposes Schneider Bézier tolerance ε = 2.0 px (CPU < 25ms) and node ceilings (32 for base paths, 16 for shadows/highlights).
- **Vision Architect Assessment:**
  1. *Conditional agreement on Macro-Geometry:* Approved for large, smooth entities (buns, shields, broad shadows) where 2.0px filters binary mask quantization noise.
  2. *Severe objection on Micro-Features & High-Frequency Details:* Catastrophic for sesame seeds (~8x14px) and frilly lettuce edges (`A02`, `A03`). At ε = 2.0px, an 8px sesame seed suffers 25–50% geometric distortion, and high-frequency lettuce ruffles are clipped flat.
  3. *Trimap Boundary IoU (8px) Degradation:* Systematic 2.0px smoothing cuts ruffles, degrading Trimap Boundary IoU from > 0.90 to < 0.82.
  4. *Demanded Reciprocal Constraints:*
     - **Scale-Aware Dynamic Epsilon:** ε = 2.0px for macro-shapes (nodes <= 32), but ε = 0.8px for micro-features (sesame seeds, leaf frills) with node budget <= 8–12.
     - **Corner / Curvature Extrema Preservation:** Lock C0/G0 sharp points (sesame tips) before curve fitting.
     - **Amodal Under-lap Guarantee:** 1.5px dilation on lower Z-index layers to prevent 2.0px shrinkage from creating white hairline cracks between adjacent shapes.

