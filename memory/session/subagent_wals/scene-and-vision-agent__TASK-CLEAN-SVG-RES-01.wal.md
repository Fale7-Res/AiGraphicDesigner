<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-17T16:28:48Z", "last_action": "CREATED", "last_change_id": "TASK-CLEAN-SVG-RES-01", "last_edited_at_utc": "2026-10-17T16:28:48Z", "last_editor": "scene-and-vision-agent", "tracking_started_at_utc": "2026-10-17T16:28:48Z"}
END_DOC_PROVENANCE -->
# Subagent WAL — scene-and-vision-agent — TASK-CLEAN-SVG-RES-01

**Subagent ID:** `scene-and-vision-agent`  
**Role:** Computer Vision and Generative AI Architect  
**Task ID:** `TASK-CLEAN-SVG-RES-01`  
**Timestamp:** 2026-10-17T16:30:00Z  

## 1. Context & Scope
Received research assignment from parent orchestrator for:
- Deep evaluation of the 10-Stage Semantic-Constrained Clean SVG Reconstruction Pipeline.
- Analysis of engineering weaknesses, failure modes, and best alternatives using pretrained CV/AI foundation models (SAM 2, Grounding DINO, LaMa, Depth-Anything v2, Intrinsic Decomposition).
- Resolution of similar-color multi-entity segmentation collisions (bun vs. cheese vs. potato).
- Criteria for Pure Vector vs. Hybrid Vector-Raster representation based on the real-world restaurant menu evidence (`menu faleh 17X50 01-1.pdf`).

## 2. Key Findings & Scientific Judgments
1. **10-Stage Pipeline Evaluation:**
   - Foundation models (SAM 2 / Grounding DINO) are flat segmenters lacking hierarchical parent-child ownership; require a VLM Scene Graph prior.
   - SAM 2 extracts visible masks only; LaMa fails at geometric shape extrapolation under heavy occlusion. An Amodal Contour Extrapolator (e.g. AISFormer / curvature extrapolation) is mandatory before raster infilling.
   - Intrinsic image decomposition (albedo vs. shading) is required to separate cast shadows from base object color.
   - Pure SSIM/MSE evaluation is flawed; must enforce the deterministic trio: Trimap Boundary IoU (8px), LPIPS, and Node Budget.
2. **Handling Similar Colors (Bun / Cheese / Potato):**
   - Color clustering (K-Means/Watershed) must never run globally across the image.
   - Enforce **Strict Semantic Primacy**: decompose into isolated entity alpha patches first.
   - Tag pixels with `(Entity_UUID, Component_Role, Color_Class)`; Boolean Union is strictly forbidden across different Entity UUIDs regardless of $\Delta E$.
   - Use relative depth discontinuity edges (Depth-Anything v2) to resolve ambiguous contact boundaries.
3. **Pure Vector vs. Hybrid Decision Framework (Menu Faleh Evidence):**
   - The menu evidence proves professional graphic designers use mixed-content (45 raster images + 1,400 vector paths, 0 live text).
   - High-entropy photorealistic food textures (meat, fried crust) cause "Bézier node explosion" (> 10,000 nodes) if vectorized purely, crippling Illustrator and browser DOM.
   - Formulated a 4-tier decision tree: Texture Entropy ($H > 6.2$), Semantic Class Prior (logos/text = Pure Vector; complex food/photos = Hybrid with vector clip paths), Node Budget Cap (<= 120 nodes/entity), and User Intent.
