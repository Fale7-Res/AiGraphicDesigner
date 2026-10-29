# السجل المركزي الموحد للدوال والكلاسات والرموز (`memory/FUNCTION_REGISTRY.md`)

> **مرجعية الكود ومستويات منع التكرار (`Source Authority & 3-Tier Deduplication Policy`):**
> 1. **المستوى الأول — تكرار الاسم المطابق (`Exact-Name Duplication`):** فحص حتمي آلي 100% يمنع وجود دالتين بنفس الاسم عبر الملفات.
> 2. **المستوى الثاني — التشابه الهيكلي للـ AST (`Structural AST Similarity`):** فحص آلي تحذيري يرصد الدوال ذات البنية الهيكلية المتطابقة للمراجعة.
> 3. **المستوى الثالث — التكرار الدلالي (`Semantic Duplication`):** **ليس آلياً بالكامل**؛ يتطلب من كل Agent قراءة عمود الوظيفة (`Purpose`) أدناه قبل كتابة أي دالة جديدة، ويخضع لتدقيق الـ Sub-Agent المراجع (`qa-reviewer-auditor`).

- **إجمالي الملفات البرمجية المفحوصة:** `12`
- **إجمالي الرموز المسجلة بالسطر (شاملة Methods وNested وArrow):** `45`
- **عدد الدوال المتطابقة الاسم غير المسموحة (`Exact-Name Duplicates`):** `0`
- **مرشحات التشابه الهيكلي (`Structural Similarity Candidates`):** `1`

## جدول جميع الدوال والكلاسات والرموز في المشروع (`Master Symbol Index`)

| اسم الرمز (`Symbol`) | النوع (`Kind`) | الملف المالك (`Owner File`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة (`Purpose`) | مرآة الكود التفصيلية (`Code Mirror`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `package` | `function` | `dashboard.py` | `Lines 13–74` | `def package():` | رمز برمجي موثق. | [dashboard.py.md](code_mirrors/dashboard.py.md) |
| `package.picture` | `nested_function` | `dashboard.py` | `Lines 18–19` | `def picture(base,name,label,link=None):` | رمز برمجي موثق. | [dashboard.py.md](code_mirrors/dashboard.py.md) |
| `main` | `function` | `evaluate_batch.py` | `Lines 7–21` | `def main():` | رمز برمجي موثق. | [evaluate_batch.py.md](code_mirrors/evaluate_batch.py.md) |
| `separation_errors` | `function` | `evaluate_study.py` | `Lines 14–23` | `def separation_errors(truth,pred):` | رمز برمجي موثق. | [evaluate_study.py.md](code_mirrors/evaluate_study.py.md) |
| `evaluate_candidate` | `function` | `evaluate_study.py` | `Lines 25–68` | `def evaluate_candidate(case,name):` | رمز برمجي موثق. | [evaluate_study.py.md](code_mirrors/evaluate_study.py.md) |
| `execute` | `function` | `run_study.py` | `Lines 8–47` | `def execute(case,condition):` | رمز برمجي موثق. | [run_study.py.md](code_mirrors/run_study.py.md) |
| `destination` | `function` | `study.py` | `Lines 13–14` | `def destination(case):` | رمز برمجي موثق. | [study.py.md](code_mirrors/study.py.md) |
| `load_baseline` | `function` | `study.py` | `Lines 16–20` | `def load_baseline(case):` | رمز برمجي موثق. | [study.py.md](code_mirrors/study.py.md) |
| `initialize_labels` | `function` | `study.py` | `Lines 22–28` | `def initialize_labels(labels):` | رمز برمجي موثق. | [study.py.md](code_mirrors/study.py.md) |
| `MeasurementSafeguards` | `class` | `test_study.py` | `Lines 7–20` | `class MeasurementSafeguards(unittest.TestCase):` | رمز برمجي موثق. | [test_study.py.md](code_mirrors/test_study.py.md) |
| `MeasurementSafeguards.test_false_join_of_two_disjoint_structures` | `method` | `test_study.py` | `Lines 8–11` | `def test_false_join_of_two_disjoint_structures(self):` | رمز برمجي موثق. | [test_study.py.md](code_mirrors/test_study.py.md) |
| `MeasurementSafeguards.test_false_split_of_one_structure` | `method` | `test_study.py` | `Lines 13–16` | `def test_false_split_of_one_structure(self):` | رمز برمجي موثق. | [test_study.py.md](code_mirrors/test_study.py.md) |
| `MeasurementSafeguards.test_empty_reference_never_passes` | `method` | `test_study.py` | `Lines 18–20` | `def test_empty_reference_never_passes(self):` | رمز برمجي موثق. | [test_study.py.md](code_mirrors/test_study.py.md) |
| `line_control` | `function` | `test_track_a.py` | `Lines 7–11` | `def line_control(supported=True):` | رمز برمجي موثق. | [test_track_a.py.md](code_mirrors/test_track_a.py.md) |
| `TrackATests` | `class` | `test_track_a.py` | `Lines 13–41` | `class TrackATests(unittest.TestCase):` | رمز برمجي موثق. | [test_track_a.py.md](code_mirrors/test_track_a.py.md) |
| `TrackATests.test_supported_missing_label_connector` | `method` | `test_track_a.py` | `Lines 14–18` | `def test_supported_missing_label_connector(self):` | رمز برمجي موثق. | [test_track_a.py.md](code_mirrors/test_track_a.py.md) |
| `TrackATests.test_blank_gap_rejected_no_global_fallback` | `method` | `test_track_a.py` | `Lines 19–22` | `def test_blank_gap_rejected_no_global_fallback(self):` | رمز برمجي موثق. | [test_track_a.py.md](code_mirrors/test_track_a.py.md) |
| `TrackATests.test_determinism_and_input_immutability` | `method` | `test_track_a.py` | `Lines 23–26` | `def test_determinism_and_input_immutability(self):` | رمز برمجي موثق. | [test_track_a.py.md](code_mirrors/test_track_a.py.md) |
| `TrackATests.test_parallel_offset_features_not_joined` | `method` | `test_track_a.py` | `Lines 27–30` | `def test_parallel_offset_features_not_joined(self):` | رمز برمجي موثق. | [test_track_a.py.md](code_mirrors/test_track_a.py.md) |
| `TrackATests.test_adjacent_tonal_regions_not_globally_merged` | `method` | `test_track_a.py` | `Lines 31–34` | `def test_adjacent_tonal_regions_not_globally_merged(self):` | رمز برمجي موثق. | [test_track_a.py.md](code_mirrors/test_track_a.py.md) |
| `TrackATests.test_pair_budget_and_convex_mixture` | `method` | `test_track_a.py` | `Lines 35–41` | `def test_pair_budget_and_convex_mixture(self):` | رمز برمجي موثق. | [test_track_a.py.md](code_mirrors/test_track_a.py.md) |
| `_line` | `function` | `test_track_b.py` | `Lines 6–6` | `def _line(a,b):return {'type':'L','p0':list(a),'p3':list(b)}` | رمز برمجي موثق. | [test_track_b.py.md](code_mirrors/test_track_b.py.md) |
| `_chain` | `function` | `test_track_b.py` | `Lines 7–9` | `def _chain(key,points,labels,collapsed=False,closed=False):` | رمز برمجي موثق. | [test_track_b.py.md](code_mirrors/test_track_b.py.md) |
| `_hole_graph` | `function` | `test_track_b.py` | `Lines 11–17` | `def _hole_graph():` | رمز برمجي موثق. | [test_track_b.py.md](code_mirrors/test_track_b.py.md) |
| `GuardTests` | `class` | `test_track_b.py` | `Lines 19–64` | `class GuardTests(unittest.TestCase):` | رمز برمجي موثق. | [test_track_b.py.md](code_mirrors/test_track_b.py.md) |
| `GuardTests.test_short_l_area_and_hole_preserved_without_grid_fallback` | `method` | `test_track_b.py` | `Lines 20–33` | `def test_short_l_area_and_hole_preserved_without_grid_fallback(self):` | رمز برمجي موثق. | [test_track_b.py.md](code_mirrors/test_track_b.py.md) |
| `GuardTests.test_shared_t_junction_endpoints_and_reversed_references_unchanged` | `method` | `test_track_b.py` | `Lines 35–47` | `def test_shared_t_junction_endpoints_and_reversed_references_unchanged(self):` | رمز برمجي موثق. | [test_track_b.py.md](code_mirrors/test_track_b.py.md) |
| `GuardTests.test_new_collision_is_rejected_and_original_retained` | `method` | `test_track_b.py` | `Lines 49–55` | `def test_new_collision_is_rejected_and_original_retained(self):` | رمز برمجي موثق. | [test_track_b.py.md](code_mirrors/test_track_b.py.md) |
| `GuardTests.test_nonunit_shape_is_not_repaired_by_grid_outline` | `method` | `test_track_b.py` | `Lines 57–64` | `def test_nonunit_shape_is_not_repaired_by_grid_outline(self):` | رمز برمجي موثق. | [test_track_b.py.md](code_mirrors/test_track_b.py.md) |
| `_region_endpoints` | `function` | `track_a.py` | `Lines 21–47` | `def _region_endpoints(labels):` | Find short-radius skeleton endpoints and inward/outward local directions. | [track_a.py.md](code_mirrors/track_a.py.md) |
| `_adjacent_pairs` | `function` | `track_a.py` | `Lines 49–54` | `def _adjacent_pairs(labels):` | رمز برمجي موثق. | [track_a.py.md](code_mirrors/track_a.py.md) |
| `_neighbor_labels` | `function` | `track_a.py` | `Lines 56–58` | `def _neighbor_labels(labels,endpoint):` | رمز برمجي موثق. | [track_a.py.md](code_mirrors/track_a.py.md) |
| `_segment_distance` | `function` | `track_a.py` | `Lines 60–63` | `def _segment_distance(xx,yy,a,b):` | رمز برمجي موثق. | [track_a.py.md](code_mirrors/track_a.py.md) |
| `_path_for_pair` | `function` | `track_a.py` | `Lines 65–110` | `def _path_for_pair(rgb_lab,labels,a,b,gap,fg,cfg):` | Bounded four-neighbor Dijkstra with a source-color mixture support gate. | [track_a.py.md](code_mirrors/track_a.py.md) |
| `discover` | `function` | `track_a.py` | `Lines 112–183` | `def discover(rgb,labels,config=None):` | Return repaired labels/audit/evidence; absent source confidence is unchanged. | [track_a.py.md](code_mirrors/track_a.py.md) |
| `discover.rejected` | `nested_function` | `track_a.py` | `Lines 131–131` | `def rejected(reason):reject[reason]=reject.get(reason,0)+1` | رمز برمجي موثق. | [track_a.py.md](code_mirrors/track_a.py.md) |
| `discover.representative` | `nested_function` | `track_a.py` | `Lines 157–159` | `def representative(a):` | رمز برمجي موثق. | [track_a.py.md](code_mirrors/track_a.py.md) |
| `_utilities` | `function` | `track_b.py` | `Lines 15–24` | `def _utilities():` | رمز برمجي موثق. | [track_b.py.md](code_mirrors/track_b.py.md) |
| `_ring_records` | `function` | `track_b.py` | `Lines 26–46` | `def _ring_records(graph,utilities,segment_area):` | رمز برمجي موثق. | [track_b.py.md](code_mirrors/track_b.py.md) |
| `_collapsed` | `function` | `track_b.py` | `Lines 48–49` | `def _collapsed(row):` | رمز برمجي موثق. | [track_b.py.md](code_mirrors/track_b.py.md) |
| `_unit_l` | `function` | `track_b.py` | `Lines 51–55` | `def _unit_l(chain):` | رمز برمجي موثق. | [track_b.py.md](code_mirrors/track_b.py.md) |
| `_chord_collapsed` | `function` | `track_b.py` | `Lines 57–64` | `def _chord_collapsed(chain):` | رمز برمجي موثق. | [track_b.py.md](code_mirrors/track_b.py.md) |
| `_pair_defects` | `function` | `track_b.py` | `Lines 66–85` | `def _pair_defects(lines,changed):` | رمز برمجي موثق. | [track_b.py.md](code_mirrors/track_b.py.md) |
| `_validate_component` | `function` | `track_b.py` | `Lines 87–113` | `def _validate_component(before,after,changed,utilities,segment_area):` | رمز برمجي موثق. | [track_b.py.md](code_mirrors/track_b.py.md) |
| `initialize_safe` | `function` | `track_b.py` | `Lines 115–159` | `def initialize_safe(graph,config=None):` | Apply only locally checked corrections; unrepaired geometry stays rejected. | [track_b.py.md](code_mirrors/track_b.py.md) |
