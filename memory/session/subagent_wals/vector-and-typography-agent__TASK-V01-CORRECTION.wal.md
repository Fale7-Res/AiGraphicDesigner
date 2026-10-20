<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-17T18:02:58Z", "last_action": "CREATED", "last_change_id": "TASK-V01-CORRECTION-01", "last_edited_at_utc": "2026-10-17T18:02:58Z", "last_editor": "vector-and-typography-agent", "tracking_started_at_utc": "2026-10-17T18:02:58Z"}
END_DOC_PROVENANCE -->
# Subagent WAL: Vector & Typography Specialist (`vector-and-typography-agent`)
**Task ID:** `TASK-V01-CORRECTION-01`
**Agent:** `vector-and-typography-agent`
**Timestamp:** 2026-10-17T18:05:00Z
**Status:** ACTIVE_INVESTIGATION

## 1. Visual Evidence & Image Analysis
- Inspected the 3 owner-provided diagnostic images in `versions/version-01/files from owner to antigravity/`:
  1. `A01_detailed_original_old_new_diff.png`: Confirmed dramatic improvement over old baseline (gold rim recovered, crown silhouette restored, white gaps eliminated). However, difference heatmap highlights that specular highlights and lighting gradients are stepped into flat bands, and anti-aliasing seams at boundaries remain visible.
  2. `all_12_source_vs_svg.png`: Visualizes the committed state where only A01 had Stage A improvements while A02..A12 were still on old degraded baseline with severe fragmentation and white gaps.
  3. `all_12_independently_rerun_improved_code.png`: Visualizes independent rerun of improved code across all 12 images. Confirms dramatic PSNR and SSIM leaps across all 12 images (e.g. A02 falafel jumped from 8.4 dB to 19.6 dB, A03 burger jumped from 9.8 dB to 17.8 dB, A08 coffee to 23.1 dB, A09 calligraphy to 18.8 dB). However, path counts exploded (995 on falafel, 946 on burger, 1025 on shawarma, 1056 on cake), and appearance is cel-shaded flat posterization without true smooth vector gradients.

## 2. A01 Numerical & Mathematical Discrepancy Breakdown
- **Discrepancy Cause:** 
  - `A01_v01_vector.svg` in `preliminary_visual_tests/outputs/` actually contains:
    - 139 `<path>` elements (each corresponding to a `VectorLayer` outer contour).
    - 311 `M` commands (139 outer boundary subpaths + 172 inner hole subpaths).
    - 3,368 `C` commands (cubic Bézier curve segments).
    - 39 compound paths with `fill-rule="evenodd"`.
  - The "28 paths and 848 nodes" reported in `STAGE_A_FIDELITY_REPORT.md` originated from an intermediate diagnostic run with higher area filtering/coarser clustering that was logged in text, but the committed production run used `n_colors=16, min_contour_area=2.0, error_tolerance_px=0.5, max_nodes_per_path=48`, yielding exactly 139 paths and 3,368 cubic Bézier nodes.
  - Clarified taxonomy: `VectorLayer` is the Python dataclass representing 1 outer contour + child holes; each renders to 1 SVG `<path>` tag; each subpath in `<path>` is delimited by `M...Z`; and each Bézier curve segment is 1 `C` command (requiring 1 on-curve anchor point + 2 off-curve control points = 3 coordinate pairs).

## 3. Compositing Layer Ordering & Topological Enclosure Critique
- Naive global area sort `cluster_areas.sort(key=lambda x: x[0], reverse=True)` sorts clusters by total pixel count across the whole image.
- Mathematically, global Lebesgue measure $\text{Area}(C_i)$ does not respect local topological containment $R_B \subset_{\text{enc}} R_A$.
- Counterexamples:
  1. Multi-component clusters: 1,000 tiny highlight flecks totaling 15,000 px get sorted underneath a 12,000 px solid base shape, completely erasing the highlights.
  2. Thin outer rings/frames: A ring of area 1,200 px enclosing a central badge of area 30,000 px gets sorted on top of the badge, whereas an inner cutout of a larger cluster gets buried.
  3. Arabic calligraphy & logos (A09, A10): Interior text or loops belonging to a larger cluster get drawn underneath the enclosing white/colored shape, destroying readability.
- Formal solution: Build a Topological Enclosure Poset (DAG) via bounding-box filtering and `pointPolygonTest`, then execute Kahn's topological sort to guarantee container shapes are always rendered before contained shapes.

## 4. Seam Sealing, Anti-Aliasing, and Silhouette Preservation
- OpenCV integer pixel centers create an intrinsic 1.0 px coordinate dead-zone between abutting pixel regions.
- Floating-point Bézier fitting creates subpixel curve divergence between shared boundaries, causing 25% background bleed under Porter-Duff alpha compositing.
- Naive stroke trapping (`stroke-width=1.0`) expands outward on exterior boundaries, causing silhouette bloating, rounded sharp corners, and letter stroke fattening.
- Proposed solutions:
  1. Interior-only morphological dilation with master silhouette clipping: $(M_i \oplus B_{3 \times 3}) \cap M_{\text{silhouette}}$.
  2. Base-plate underlay: Solid union silhouette placed at $z=0$ under each semantic group.
  3. Shared-edge planar map representation for mathematically identical boundary curves.
