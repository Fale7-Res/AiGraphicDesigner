# السجل المركزي الموحد للدوال والكلاسات والرموز (`memory/FUNCTION_REGISTRY.md`)

> **مرجعية الكود ومستويات منع التكرار (`Source Authority & 3-Tier Deduplication Policy`):**
> 1. **المستوى الأول — تكرار الاسم المطابق (`Exact-Name Duplication`):** فحص حتمي آلي 100% يمنع وجود دالتين بنفس الاسم عبر الملفات.
> 2. **المستوى الثاني — التشابه الهيكلي للـ AST (`Structural AST Similarity`):** فحص آلي تحذيري يرصد الدوال ذات البنية الهيكلية المتطابقة للمراجعة.
> 3. **المستوى الثالث — التكرار الدلالي (`Semantic Duplication`):** **ليس آلياً بالكامل**؛ يتطلب من كل Agent قراءة عمود الوظيفة (`Purpose`) أدناه قبل كتابة أي دالة جديدة، ويخضع لتدقيق الـ Sub-Agent المراجع (`qa-reviewer-auditor`).

- **إجمالي الملفات البرمجية المفحوصة:** `9`
- **إجمالي الرموز المسجلة بالسطر (شاملة Methods وNested وArrow):** `51`
- **عدد الدوال المتطابقة الاسم غير المسموحة (`Exact-Name Duplicates`):** `0`
- **مرشحات التشابه الهيكلي (`Structural Similarity Candidates`):** `0`

## جدول جميع الدوال والكلاسات والرموز في المشروع (`Master Symbol Index`)

| اسم الرمز (`Symbol`) | النوع (`Kind`) | الملف المالك (`Owner File`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة (`Purpose`) | مرآة الكود التفصيلية (`Code Mirror`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `paths_for_case` | `function` | `bottlenecks.py` | `Lines 19–23` | `def paths_for_case(case):` | Check frozen saved sources without modifying any historical experiment. | [bottlenecks.py.md](code_mirrors/bottlenecks.py.md) |
| `visible_geometry` | `function` | `bottlenecks.py` | `Lines 25–60` | `def visible_geometry(svg,source,folder):` | Native pixel-center visibility area of RGB micro-paths; masks excluded explicitly. | [bottlenecks.py.md](code_mirrors/bottlenecks.py.md) |
| `spatial_error_partition` | `function` | `bottlenecks.py` | `Lines 62–69` | `def spatial_error_partition(source,render,band):` | Disjoint spatial error accounting; expressly not causal/additive bottleneck attribution. | [bottlenecks.py.md](code_mirrors/bottlenecks.py.md) |
| `evaluate_and_record` | `function` | `bottlenecks.py` | `Lines 71–74` | `def evaluate_and_record(source,svg,folder,band=None):` | رمز برمجي موثق. | [bottlenecks.py.md](code_mirrors/bottlenecks.py.md) |
| `run_granularity` | `function` | `bottlenecks.py` | `Lines 76–134` | `def run_granularity(case):` | رمز برمجي موثق. | [bottlenecks.py.md](code_mirrors/bottlenecks.py.md) |
| `comparisons` | `function` | `bottlenecks.py` | `Lines 136–178` | `def comparisons():` | Every granularity and worst residual shown; no favorable case filtering. | [bottlenecks.py.md](code_mirrors/bottlenecks.py.md) |
| `corrected_case` | `function` | `correct_bottlenecks.py` | `Lines 12–40` | `def corrected_case(case):` | رمز برمجي موثق. | [correct_bottlenecks.py.md](code_mirrors/correct_bottlenecks.py.md) |
| `corrected_case.signature` | `nested_function` | `correct_bottlenecks.py` | `Lines 25–28` | `def signature(root):` | رمز برمجي موثق. | [correct_bottlenecks.py.md](code_mirrors/correct_bottlenecks.py.md) |
| `rgb_paths` | `function` | `coverage.py` | `Lines 21–28` | `def rgb_paths(root):` | Exclude all geometry inside defs, masks and clipping constructions. | [coverage.py.md](code_mirrors/coverage.py.md) |
| `rgb_paths.visit` | `nested_function` | `coverage.py` | `Lines 24–27` | `def visit(node,excluded=False):` | رمز برمجي موثق. | [coverage.py.md](code_mirrors/coverage.py.md) |
| `correct_coverage` | `function` | `coverage.py` | `Lines 30–47` | `def correct_coverage(input_svg,output_svg,width=.25):` | Add narrow matching-paint strokes without altering d, order, topology or masks. | [coverage.py.md](code_mirrors/coverage.py.md) |
| `write_svg` | `function` | `coverage.py` | `Lines 49–51` | `def write_svg(path,root):` | رمز برمجي موثق. | [coverage.py.md](code_mirrors/coverage.py.md) |
| `render_alpha` | `function` | `coverage.py` | `Lines 53–56` | `def render_alpha(svg,png,scale=1):` | رمز برمجي موثق. | [coverage.py.md](code_mirrors/coverage.py.md) |
| `coverage_versions` | `function` | `coverage.py` | `Lines 58–90` | `def coverage_versions(svg,folder):` | Paint each region white; compound fill is a winding diagnostic, NOT Boolean union. | [coverage.py.md](code_mirrors/coverage.py.md) |
| `alpha_summary` | `function` | `coverage.py` | `Lines 92–106` | `def alpha_summary(separate,reference,scale=1):` | Measure coverage loss in reference-opaque interiors and exterior changes. | [coverage.py.md](code_mirrors/coverage.py.md) |
| `save_alpha_heat` | `function` | `coverage.py` | `Lines 108–112` | `def save_alpha_heat(alpha,reference,path):` | رمز برمجي موثق. | [coverage.py.md](code_mirrors/coverage.py.md) |
| `run_exact_controls` | `function` | `coverage.py` | `Lines 114–154` | `def run_exact_controls():` | Two exact known partitions, plus a real-gap negative and exterior-stroke control. | [coverage.py.md](code_mirrors/coverage.py.md) |
| `sampled_region_coverage` | `function` | `coverage.py` | `Lines 156–175` | `def sampled_region_coverage(svg,folder,scale=4,max_regions=128):` | Independent per-region thresholded alpha occupancy; samples, not analytic topology. | [coverage.py.md](code_mirrors/coverage.py.md) |
| `run_real_cases` | `function` | `coverage.py` | `Lines 177–209` | `def run_real_cases():` | رمز برمجي موثق. | [coverage.py.md](code_mirrors/coverage.py.md) |
| `finalize_real_visuals` | `function` | `coverage.py` | `Lines 211–236` | `def finalize_real_visuals(results):` | Export actual region IDs and 4x vector renders, retaining expansion negatives. | [coverage.py.md](code_mirrors/coverage.py.md) |
| `build_coverage_index` | `function` | `coverage.py` | `Lines 238–257` | `def build_coverage_index():` | Small self-contained overview; preserve real failures as prominently as gains. | [coverage.py.md](code_mirrors/coverage.py.md) |
| `digest` | `function` | `oracle.py` | `Lines 23–24` | `def digest(path):` | رمز برمجي موثق. | [oracle.py.md](code_mirrors/oracle.py.md) |
| `load_historical` | `function` | `oracle.py` | `Lines 27–34` | `def load_historical(repo):` | رمز برمجي موثق. | [oracle.py.md](code_mirrors/oracle.py.md) |
| `flat_initialization` | `function` | `oracle.py` | `Lines 37–53` | `def flat_initialization(source, destination):` | Remove original gradient paint only, preserving source geometry and solid paint. | [oracle.py.md](code_mirrors/oracle.py.md) |
| `_write_json` | `function` | `oracle.py` | `Lines 56–57` | `def _write_json(path, data):` | رمز برمجي موثق. | [oracle.py.md](code_mirrors/oracle.py.md) |
| `gradient_metadata` | `function` | `oracle.py` | `Lines 61–62` | `def gradient_metadata(root):` | رمز برمجي موثق. | [oracle.py.md](code_mirrors/oracle.py.md) |
| `finish_diagnostics` | `function` | `oracle.py` | `Lines 64–94` | `def finish_diagnostics(repo, output):` | Read-only fit analysis and actual vector-render visual/ground-truth checks. | [oracle.py.md](code_mirrors/oracle.py.md) |
| `run_oracle` | `function` | `oracle.py` | `Lines 97–152` | `def run_oracle(repo, output):` | رمز برمجي موثق. | [oracle.py.md](code_mirrors/oracle.py.md) |
| `verify_inventory` | `function` | `run_cycle.py` | `Lines 8–14` | `def verify_inventory(path):` | رمز برمجي موثق. | [run_cycle.py.md](code_mirrors/run_cycle.py.md) |
| `artifact_inventory` | `function` | `run_cycle.py` | `Lines 16–21` | `def artifact_inventory(target):` | رمز برمجي موثق. | [run_cycle.py.md](code_mirrors/run_cycle.py.md) |
| `run_bounded` | `function` | `run_cycle.py` | `Lines 23–27` | `def run_bounded(name,args,timeout):` | رمز برمجي موثق. | [run_cycle.py.md](code_mirrors/run_cycle.py.md) |
| `oracle_dashboard` | `function` | `run_cycle.py` | `Lines 29–35` | `def oracle_dashboard():` | رمز برمجي موثق. | [run_cycle.py.md](code_mirrors/run_cycle.py.md) |
| `monitor` | `function` | `safe_monitor.py` | `Lines 7–44` | `def monitor(command,log,timeout=900,memory_mib=4096):` | رمز برمجي موثق. | [safe_monitor.py.md](code_mirrors/safe_monitor.py.md) |
| `BottleneckTests` | `class` | `test_bottlenecks.py` | `Lines 11–69` | `class BottleneckTests(unittest.TestCase):` | رمز برمجي موثق. | [test_bottlenecks.py.md](code_mirrors/test_bottlenecks.py.md) |
| `BottleneckTests.test_complete_frozen_suite_and_native_metrics` | `method` | `test_bottlenecks.py` | `Lines 12–22` | `def test_complete_frozen_suite_and_native_metrics(self):` | رمز برمجي موثق. | [test_bottlenecks.py.md](code_mirrors/test_bottlenecks.py.md) |
| `BottleneckTests.test_geometry_held_across_fits_and_gradient_safety` | `method` | `test_bottlenecks.py` | `Lines 23–32` | `def test_geometry_held_across_fits_and_gradient_safety(self):` | رمز برمجي موثق. | [test_bottlenecks.py.md](code_mirrors/test_bottlenecks.py.md) |
| `BottleneckTests.test_correction_pairing_and_unchanged_underlying_paths` | `method` | `test_bottlenecks.py` | `Lines 33–42` | `def test_correction_pairing_and_unchanged_underlying_paths(self):` | رمز برمجي موثق. | [test_bottlenecks.py.md](code_mirrors/test_bottlenecks.py.md) |
| `BottleneckTests.test_visibility_does_not_hide_tiny_regions_or_count_occlusion` | `method` | `test_bottlenecks.py` | `Lines 43–51` | `def test_visibility_does_not_hide_tiny_regions_or_count_occlusion(self):` | رمز برمجي موثق. | [test_bottlenecks.py.md](code_mirrors/test_bottlenecks.py.md) |
| `BottleneckTests.test_monitor_timeout_is_bounded_and_reported` | `method` | `test_bottlenecks.py` | `Lines 52–56` | `def test_monitor_timeout_is_bounded_and_reported(self):` | رمز برمجي موثق. | [test_bottlenecks.py.md](code_mirrors/test_bottlenecks.py.md) |
| `BottleneckTests.test_cycle_inventory_rejects_missing_and_modified_artifacts` | `method` | `test_bottlenecks.py` | `Lines 57–69` | `def test_cycle_inventory_rejects_missing_and_modified_artifacts(self):` | رمز برمجي موثق. | [test_bottlenecks.py.md](code_mirrors/test_bottlenecks.py.md) |
| `CoverageTests` | `class` | `test_coverage.py` | `Lines 8–46` | `class CoverageTests(unittest.TestCase):` | رمز برمجي موثق. | [test_coverage.py.md](code_mirrors/test_coverage.py.md) |
| `CoverageTests.test_exact_partition_aa_seam_differs_from_known_union` | `method` | `test_coverage.py` | `Lines 9–15` | `def test_exact_partition_aa_seam_differs_from_known_union(self):` | رمز برمجي موثق. | [test_coverage.py.md](code_mirrors/test_coverage.py.md) |
| `CoverageTests.test_real_gap_negative_not_declared_repaired` | `method` | `test_coverage.py` | `Lines 16–19` | `def test_real_gap_negative_not_declared_repaired(self):` | رمز برمجي موثق. | [test_coverage.py.md](code_mirrors/test_coverage.py.md) |
| `CoverageTests.test_exterior_stroke_changes_known_silhouette` | `method` | `test_coverage.py` | `Lines 20–22` | `def test_exterior_stroke_changes_known_silhouette(self):` | رمز برمجي موثق. | [test_coverage.py.md](code_mirrors/test_coverage.py.md) |
| `CoverageTests.test_mask_and_path_geometry_untouched_gradient_paint_reused` | `method` | `test_coverage.py` | `Lines 23–31` | `def test_mask_and_path_geometry_untouched_gradient_paint_reused(self):` | رمز برمجي موثق. | [test_coverage.py.md](code_mirrors/test_coverage.py.md) |
| `CoverageTests.test_out_of_scope_stroke_width_refused` | `method` | `test_coverage.py` | `Lines 32–33` | `def test_out_of_scope_stroke_width_refused(self):` | رمز برمجي موثق. | [test_coverage.py.md](code_mirrors/test_coverage.py.md) |
| `CoverageTests.test_nonempty_run_targets_refused` | `method` | `test_coverage.py` | `Lines 34–46` | `def test_nonempty_run_targets_refused(self):` | رمز برمجي موثق. | [test_coverage.py.md](code_mirrors/test_coverage.py.md) |
| `OracleTests` | `class` | `test_oracle.py` | `Lines 13–63` | `class OracleTests(unittest.TestCase):` | رمز برمجي موثق. | [test_oracle.py.md](code_mirrors/test_oracle.py.md) |
| `OracleTests.test_saved_oracle_artifact_geometry_and_gradient_limits` | `method` | `test_oracle.py` | `Lines 14–30` | `def test_saved_oracle_artifact_geometry_and_gradient_limits(self):` | رمز برمجي موثق. | [test_oracle.py.md](code_mirrors/test_oracle.py.md) |
| `OracleTests.test_saved_native_mse_matches_actual_render` | `method` | `test_oracle.py` | `Lines 32–48` | `def test_saved_native_mse_matches_actual_render(self):` | رمز برمجي موثق. | [test_oracle.py.md](code_mirrors/test_oracle.py.md) |
| `OracleTests.test_init_preserves_every_geometry_attribute_and_solid_paint` | `method` | `test_oracle.py` | `Lines 50–63` | `def test_init_preserves_every_geometry_attribute_and_solid_paint(self):` | رمز برمجي موثق. | [test_oracle.py.md](code_mirrors/test_oracle.py.md) |
