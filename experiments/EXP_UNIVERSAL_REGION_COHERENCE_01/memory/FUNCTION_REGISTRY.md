# السجل المركزي الموحد للدوال والكلاسات والرموز (`memory/FUNCTION_REGISTRY.md`)

> **مرجعية الكود ومستويات منع التكرار (`Source Authority & 3-Tier Deduplication Policy`):**
> 1. **المستوى الأول — تكرار الاسم المطابق (`Exact-Name Duplication`):** فحص حتمي آلي 100% يمنع وجود دالتين بنفس الاسم عبر الملفات.
> 2. **المستوى الثاني — التشابه الهيكلي للـ AST (`Structural AST Similarity`):** فحص آلي تحذيري يرصد الدوال ذات البنية الهيكلية المتطابقة للمراجعة.
> 3. **المستوى الثالث — التكرار الدلالي (`Semantic Duplication`):** **ليس آلياً بالكامل**؛ يتطلب من كل Agent قراءة عمود الوظيفة (`Purpose`) أدناه قبل كتابة أي دالة جديدة، ويخضع لتدقيق الـ Sub-Agent المراجع (`qa-reviewer-auditor`).

- **إجمالي الملفات البرمجية المفحوصة:** `21`
- **إجمالي الرموز المسجلة بالسطر (شاملة Methods وNested وArrow):** `66`
- **عدد الدوال المتطابقة الاسم غير المسموحة (`Exact-Name Duplicates`):** `0`
- **مرشحات التشابه الهيكلي (`Structural Similarity Candidates`):** `3`

## جدول جميع الدوال والكلاسات والرموز في المشروع (`Master Symbol Index`)

| اسم الرمز (`Symbol`) | النوع (`Kind`) | الملف المالك (`Owner File`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة (`Purpose`) | مرآة الكود التفصيلية (`Code Mirror`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `make_geometry_review` | `function` | `build_review.py` | `Lines 9–47` | `def make_geometry_review():` | رمز برمجي موثق. | [build_review.py.md](code_mirrors/build_review.py.md) |
| `make_geometry_review.dashboard` | `nested_function` | `build_review.py` | `Lines 18–46` | `def dashboard(owner):` | رمز برمجي موثق. | [build_review.py.md](code_mirrors/build_review.py.md) |
| `polyline` | `function` | `coherence_refine.py` | `Lines 24–26` | `def polyline(curves):` | رمز برمجي موثق. | [coherence_refine.py.md](code_mirrors/coherence_refine.py.md) |
| `curve_quality` | `function` | `coherence_refine.py` | `Lines 29–55` | `def curve_quality(curves):` | Derivative/curvature are diagnostics, separate from pathcount/span proxies. | [coherence_refine.py.md](code_mirrors/coherence_refine.py.md) |
| `_unit` | `function` | `coherence_refine.py` | `Lines 58–60` | `def _unit(vector):` | رمز برمجي موثق. | [coherence_refine.py.md](code_mirrors/coherence_refine.py.md) |
| `_least_square` | `function` | `coherence_refine.py` | `Lines 63–80` | `def _least_square(points,left,right):` | Nonnegative endpoint handle scalars keep the inherited tangent directions. | [coherence_refine.py.md](code_mirrors/coherence_refine.py.md) |
| `_piecewise` | `function` | `coherence_refine.py` | `Lines 83–103` | `def _piecewise(points,left,right,deadline,depth=0):` | رمز برمجي موثق. | [coherence_refine.py.md](code_mirrors/coherence_refine.py.md) |
| `_proposal` | `function` | `coherence_refine.py` | `Lines 106–128` | `def _proposal(item,points,deadline):` | رمز برمجي موثق. | [coherence_refine.py.md](code_mirrors/coherence_refine.py.md) |
| `refine` | `function` | `coherence_refine.py` | `Lines 131–180` | `def refine(items,originaltraces):` | Return unchanged-schema items plus exhaustive chain decision audit. | [coherence_refine.py.md](code_mirrors/coherence_refine.py.md) |
| `combined_worker` | `function` | `combined_control.py` | `Lines 11–23` | `def combined_worker():` | رمز برمجي موثق. | [combined_control.py.md](code_mirrors/combined_control.py.md) |
| `evaluate_universal_case` | `function` | `evaluate_universal.py` | `Lines 14–59` | `def evaluate_universal_case(case):` | رمز برمجي موثق. | [evaluate_universal.py.md](code_mirrors/evaluate_universal.py.md) |
| `evaluate_all_universal` | `function` | `evaluate_universal.py` | `Lines 61–73` | `def evaluate_all_universal():` | رمز برمجي موثق. | [evaluate_universal.py.md](code_mirrors/evaluate_universal.py.md) |
| `endpoint_graph_stats` | `function` | `graph_diagnostic.py` | `Lines 5–13` | `def endpoint_graph_stats(paths):` | رمز برمجي موثق. | [graph_diagnostic.py.md](code_mirrors/graph_diagnostic.py.md) |
| `endpoint_graph_stats.find` | `nested_function` | `graph_diagnostic.py` | `Lines 7–10` | `def find(a):` | رمز برمجي موثق. | [graph_diagnostic.py.md](code_mirrors/graph_diagnostic.py.md) |
| `graph_diagnostic` | `function` | `graph_diagnostic.py` | `Lines 14–21` | `def graph_diagnostic():` | رمز برمجي موثق. | [graph_diagnostic.py.md](code_mirrors/graph_diagnostic.py.md) |
| `launch_universal` | `function` | `launch.py` | `Lines 6–21` | `def launch_universal():` | رمز برمجي موثق. | [launch.py.md](code_mirrors/launch.py.md) |
| `check` | `function` | `qa/audit_candidates.py` | `Lines 22–24` | `def check(ok, message):` | رمز برمجي موثق. | [qa__audit_candidates.py.md](code_mirrors/qa__audit_candidates.py.md) |
| `sampled` | `function` | `qa/audit_candidates.py` | `Lines 26–29` | `def sampled(curves, count=65):` | رمز برمجي موثق. | [qa__audit_candidates.py.md](code_mirrors/qa__audit_candidates.py.md) |
| `parse_svg` | `function` | `qa/audit_candidates.py` | `Lines 31–64` | `def parse_svg(path, expected=None):` | رمز برمجي موثق. | [qa__audit_candidates.py.md](code_mirrors/qa__audit_candidates.py.md) |
| `Links` | `class` | `qa/audit_delivery.py` | `Lines 12–16` | `class Links(HTMLParser):` | رمز برمجي موثق. | [qa__audit_delivery.py.md](code_mirrors/qa__audit_delivery.py.md) |
| `Links.__init__` | `method` | `qa/audit_delivery.py` | `Lines 13–13` | `def __init__(self):super().__init__();self.links=[]` | رمز برمجي موثق. | [qa__audit_delivery.py.md](code_mirrors/qa__audit_delivery.py.md) |
| `Links.handle_starttag` | `method` | `qa/audit_delivery.py` | `Lines 14–16` | `def handle_starttag(self,tag,attrs):` | رمز برمجي موثق. | [qa__audit_delivery.py.md](code_mirrors/qa__audit_delivery.py.md) |
| `dense` | `function` | `qa/audit_geometry.py` | `Lines 17–20` | `def dense(cc):` | رمز برمجي موثق. | [qa__audit_geometry.py.md](code_mirrors/qa__audit_geometry.py.md) |
| `sampled_source` | `function` | `qa/audit_geometry.py` | `Lines 22–27` | `def sampled_source(p):` | رمز برمجي موثق. | [qa__audit_geometry.py.md](code_mirrors/qa__audit_geometry.py.md) |
| `dense_region_curve_samples` | `function` | `qa/audit_regions.py` | `Lines 15–18` | `def dense_region_curve_samples(curves):` | رمز برمجي موثق. | [qa__audit_regions.py.md](code_mirrors/qa__audit_regions.py.md) |
| `_flat` | `function` | `region_integration.py` | `Lines 16–28` | `def _flat(c, tolerance=.005, depth=0, deadline=None):` | رمز برمجي موثق. | [region_integration.py.md](code_mirrors/region_integration.py.md) |
| `_points` | `function` | `region_integration.py` | `Lines 31–34` | `def _points(curves,deadline=None):` | رمز برمجي موثق. | [region_integration.py.md](code_mirrors/region_integration.py.md) |
| `_angle` | `function` | `region_integration.py` | `Lines 37–42` | `def _angle(curves,forward):` | رمز برمجي موثق. | [region_integration.py.md](code_mirrors/region_integration.py.md) |
| `_area` | `function` | `region_integration.py` | `Lines 45–45` | `def _area(p):return float(np.sum(p[:-1,0]*p[1:,1]-p[1:,0]*p[:-1,1])/2)` | رمز برمجي موثق. | [region_integration.py.md](code_mirrors/region_integration.py.md) |
| `_reverse` | `function` | `region_integration.py` | `Lines 48–48` | `def _reverse(refs):return [dict(chain=r['chain'],forward=not r['forward']) for r in refs[::-1]]` | رمز برمجي موثق. | [region_integration.py.md](code_mirrors/region_integration.py.md) |
| `integrate` | `function` | `region_integration.py` | `Lines 51–168` | `def integrate(items,width,height,rgb):` | Return graph,audit. Items remain unchanged; graph chains preserve all inputs. | [region_integration.py.md](code_mirrors/region_integration.py.md) |
| `separate_region_scope` | `function` | `region_scope_metrics.py` | `Lines 9–23` | `def separate_region_scope():` | رمز برمجي موثق. | [region_scope_metrics.py.md](code_mirrors/region_scope_metrics.py.md) |
| `bundle` | `function` | `test_coherence.py` | `Lines 15–18` | `def bundle(points,tid=0):` | رمز برمجي موثق. | [test_coherence.py.md](code_mirrors/test_coherence.py.md) |
| `CoherenceTests` | `class` | `test_coherence.py` | `Lines 21–60` | `class CoherenceTests(unittest.TestCase):` | رمز برمجي موثق. | [test_coherence.py.md](code_mirrors/test_coherence.py.md) |
| `CoherenceTests.assert_anchors` | `method` | `test_coherence.py` | `Lines 22–26` | `def assert_anchors(self,before,after):` | رمز برمجي موثق. | [test_coherence.py.md](code_mirrors/test_coherence.py.md) |
| `CoherenceTests.test_circle` | `method` | `test_coherence.py` | `Lines 27–32` | `def test_circle(self):` | رمز برمجي موثق. | [test_coherence.py.md](code_mirrors/test_coherence.py.md) |
| `CoherenceTests.test_jaggy_staircase` | `method` | `test_coherence.py` | `Lines 33–38` | `def test_jaggy_staircase(self):` | رمز برمجي موثق. | [test_coherence.py.md](code_mirrors/test_coherence.py.md) |
| `CoherenceTests.test_thin_L_corner` | `method` | `test_coherence.py` | `Lines 39–43` | `def test_thin_L_corner(self):` | رمز برمجي موثق. | [test_coherence.py.md](code_mirrors/test_coherence.py.md) |
| `CoherenceTests.test_shared_junction` | `method` | `test_coherence.py` | `Lines 44–48` | `def test_shared_junction(self):` | رمز برمجي موثق. | [test_coherence.py.md](code_mirrors/test_coherence.py.md) |
| `CoherenceTests.test_closed_hole_nesting` | `method` | `test_coherence.py` | `Lines 49–54` | `def test_closed_hole_nesting(self):` | رمز برمجي موثق. | [test_coherence.py.md](code_mirrors/test_coherence.py.md) |
| `CoherenceTests.test_missing_provenance_explicit_rollback` | `method` | `test_coherence.py` | `Lines 55–57` | `def test_missing_provenance_explicit_rollback(self):` | رمز برمجي موثق. | [test_coherence.py.md](code_mirrors/test_coherence.py.md) |
| `CoherenceTests.test_quality_is_separate` | `method` | `test_coherence.py` | `Lines 58–60` | `def test_quality_is_separate(self):` | رمز برمجي موثق. | [test_coherence.py.md](code_mirrors/test_coherence.py.md) |
| `line` | `function` | `test_region_integration.py` | `Lines 15–17` | `def line(a,b):` | رمز برمجي موثق. | [test_region_integration.py.md](code_mirrors/test_region_integration.py.md) |
| `path` | `function` | `test_region_integration.py` | `Lines 20–20` | `def path(points):return {'curves':[line(a,b) for a,b in zip(points,points[1:])]}` | رمز برمجي موثق. | [test_region_integration.py.md](code_mirrors/test_region_integration.py.md) |
| `square` | `function` | `test_region_integration.py` | `Lines 23–23` | `def square(x,y,s):return path([(x,y),(x+s,y),(x+s,y+s),(x,y+s),(x,y)])` | رمز برمجي موثق. | [test_region_integration.py.md](code_mirrors/test_region_integration.py.md) |
| `RegionTests` | `class` | `test_region_integration.py` | `Lines 26–111` | `class RegionTests(unittest.TestCase):` | رمز برمجي موثق. | [test_region_integration.py.md](code_mirrors/test_region_integration.py.md) |
| `RegionTests.run_case` | `method` | `test_region_integration.py` | `Lines 27–32` | `def run_case(self,items):` | رمز برمجي موثق. | [test_region_integration.py.md](code_mirrors/test_region_integration.py.md) |
| `RegionTests.test_single_square_closed` | `method` | `test_region_integration.py` | `Lines 34–37` | `def test_single_square_closed(self):` | رمز برمجي موثق. | [test_region_integration.py.md](code_mirrors/test_region_integration.py.md) |
| `RegionTests.test_open_stroke_preserved` | `method` | `test_region_integration.py` | `Lines 39–42` | `def test_open_stroke_preserved(self):` | رمز برمجي موثق. | [test_region_integration.py.md](code_mirrors/test_region_integration.py.md) |
| `RegionTests.test_shared_junction_square` | `method` | `test_region_integration.py` | `Lines 44–49` | `def test_shared_junction_square(self):` | رمز برمجي موثق. | [test_region_integration.py.md](code_mirrors/test_region_integration.py.md) |
| `RegionTests.test_hole_and_interior_island_all_atomic` | `method` | `test_region_integration.py` | `Lines 51–56` | `def test_hole_and_interior_island_all_atomic(self):` | رمز برمجي موثق. | [test_region_integration.py.md](code_mirrors/test_region_integration.py.md) |
| `RegionTests.test_dangling_t_no_invented_region` | `method` | `test_region_integration.py` | `Lines 58–60` | `def test_dangling_t_no_invented_region(self):` | رمز برمجي موثق. | [test_region_integration.py.md](code_mirrors/test_region_integration.py.md) |
| `RegionTests.test_crossing_rejected_not_deleted` | `method` | `test_region_integration.py` | `Lines 62–65` | `def test_crossing_rejected_not_deleted(self):` | رمز برمجي موثق. | [test_region_integration.py.md](code_mirrors/test_region_integration.py.md) |
| `RegionTests.test_tangent_ambiguity_rejected` | `method` | `test_region_integration.py` | `Lines 67–69` | `def test_tangent_ambiguity_rejected(self):` | رمز برمجي موثق. | [test_region_integration.py.md](code_mirrors/test_region_integration.py.md) |
| `RegionTests.test_exact_no_snapping` | `method` | `test_region_integration.py` | `Lines 71–73` | `def test_exact_no_snapping(self):` | رمز برمجي موثق. | [test_region_integration.py.md](code_mirrors/test_region_integration.py.md) |
| `RegionTests.test_numerical_selfintersection_rejected` | `method` | `test_region_integration.py` | `Lines 75–77` | `def test_numerical_selfintersection_rejected(self):` | رمز برمجي موثق. | [test_region_integration.py.md](code_mirrors/test_region_integration.py.md) |
| `RegionTests.test_curved_loop_exact_cubics` | `method` | `test_region_integration.py` | `Lines 79–85` | `def test_curved_loop_exact_cubics(self):` | رمز برمجي موثق. | [test_region_integration.py.md](code_mirrors/test_region_integration.py.md) |
| `RegionTests.test_collinear_overshoot_not_flattened_to_chord` | `method` | `test_region_integration.py` | `Lines 87–95` | `def test_collinear_overshoot_not_flattened_to_chord(self):` | رمز برمجي موثق. | [test_region_integration.py.md](code_mirrors/test_region_integration.py.md) |
| `RegionTests.test_real_resvg_nested_atomic_faces_1_4_16` | `method` | `test_region_integration.py` | `Lines 97–111` | `def test_real_resvg_nested_atomic_faces_1_4_16(self):` | رمز برمجي موثق. | [test_region_integration.py.md](code_mirrors/test_region_integration.py.md) |
| `SelectionTests` | `class` | `test_selection.py` | `Lines 5–13` | `class SelectionTests(unittest.TestCase):` | رمز برمجي موثق. | [test_selection.py.md](code_mirrors/test_selection.py.md) |
| `SelectionTests.test_deterministic_and_no_mutation` | `method` | `test_selection.py` | `Lines 6–10` | `def test_deterministic_and_no_mutation(self):` | رمز برمجي موثق. | [test_selection.py.md](code_mirrors/test_selection.py.md) |
| `SelectionTests.test_closure_is_source_only` | `method` | `test_selection.py` | `Lines 11–13` | `def test_closure_is_source_only(self):` | رمز برمجي موثق. | [test_selection.py.md](code_mirrors/test_selection.py.md) |
| `output_folder` | `function` | `universal_run.py` | `Lines 23–24` | `def output_folder(case):` | رمز برمجي موثق. | [universal_run.py.md](code_mirrors/universal_run.py.md) |
| `selection_rank` | `function` | `universal_run.py` | `Lines 26–44` | `def selection_rank(traces,rgb):` | Fixed score, all source features only; no length term or image identifiers. | [universal_run.py.md](code_mirrors/universal_run.py.md) |
| `new_classical` | `function` | `universal_run.py` | `Lines 46–59` | `def new_classical(rgb):` | رمز برمجي موثق. | [universal_run.py.md](code_mirrors/universal_run.py.md) |
| `run_universal_case` | `function` | `universal_run.py` | `Lines 61–78` | `def run_universal_case(case):` | رمز برمجي موثق. | [universal_run.py.md](code_mirrors/universal_run.py.md) |
