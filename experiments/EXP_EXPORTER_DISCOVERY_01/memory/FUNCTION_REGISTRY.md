# السجل المركزي الموحد للدوال والكلاسات والرموز (`memory/FUNCTION_REGISTRY.md`)

> **مرجعية الكود ومستويات منع التكرار (`Source Authority & 3-Tier Deduplication Policy`):**
> 1. **المستوى الأول — تكرار الاسم المطابق (`Exact-Name Duplication`):** فحص حتمي آلي 100% يمنع وجود دالتين بنفس الاسم عبر الملفات.
> 2. **المستوى الثاني — التشابه الهيكلي للـ AST (`Structural AST Similarity`):** فحص آلي تحذيري يرصد الدوال ذات البنية الهيكلية المتطابقة للمراجعة.
> 3. **المستوى الثالث — التكرار الدلالي (`Semantic Duplication`):** **ليس آلياً بالكامل**؛ يتطلب من كل Agent قراءة عمود الوظيفة (`Purpose`) أدناه قبل كتابة أي دالة جديدة، ويخضع لتدقيق الـ Sub-Agent المراجع (`qa-reviewer-auditor`).

- **إجمالي الملفات البرمجية المفحوصة:** `16`
- **إجمالي الرموز المسجلة بالسطر (شاملة Methods وNested وArrow):** `68`
- **عدد الدوال المتطابقة الاسم غير المسموحة (`Exact-Name Duplicates`):** `0`
- **مرشحات التشابه الهيكلي (`Structural Similarity Candidates`):** `3`

## جدول جميع الدوال والكلاسات والرموز في المشروع (`Master Symbol Index`)

| اسم الرمز (`Symbol`) | النوع (`Kind`) | الملف المالك (`Owner File`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة (`Purpose`) | مرآة الكود التفصيلية (`Code Mirror`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `audit` | `function` | `audit_exporter_calls.py` | `Lines 9–23` | `def audit(root):` | رمز برمجي موثق. | [audit_exporter_calls.py.md](code_mirrors/audit_exporter_calls.py.md) |
| `_sample` | `function` | `discovery_strokes.py` | `Lines 34–40` | `def _sample(field, x, y):` | رمز برمجي موثق. | [discovery_strokes.py.md](code_mirrors/discovery_strokes.py.md) |
| `_ridge_evidence` | `function` | `discovery_strokes.py` | `Lines 43–67` | `def _ridge_evidence(rgb):` | رمز برمجي موثق. | [discovery_strokes.py.md](code_mirrors/discovery_strokes.py.md) |
| `_trace` | `function` | `discovery_strokes.py` | `Lines 70–100` | `def _trace(skeleton):` | Visit undirected graph edges once; suppress redundant diagonal chords. | [discovery_strokes.py.md](code_mirrors/discovery_strokes.py.md) |
| `_trace.walk` | `nested_function` | `discovery_strokes.py` | `Lines 85–95` | `def walk(a, b):` | رمز برمجي موثق. | [discovery_strokes.py.md](code_mirrors/discovery_strokes.py.md) |
| `_resample_polyline` | `function` | `discovery_strokes.py` | `Lines 103–108` | `def _resample_polyline(points, step):` | رمز برمجي موثق. | [discovery_strokes.py.md](code_mirrors/discovery_strokes.py.md) |
| `_fit` | `function` | `discovery_strokes.py` | `Lines 111–144` | `def _fit(points):` | رمز برمجي موثق. | [discovery_strokes.py.md](code_mirrors/discovery_strokes.py.md) |
| `_width` | `function` | `discovery_strokes.py` | `Lines 147–174` | `def _width(lab, points, angle, radius):` | رمز برمجي موثق. | [discovery_strokes.py.md](code_mirrors/discovery_strokes.py.md) |
| `discover` | `function` | `discovery_strokes.py` | `Lines 177–218` | `def discover(rgb):` | رمز برمجي موثق. | [discovery_strokes.py.md](code_mirrors/discovery_strokes.py.md) |
| `svg` | `function` | `discovery_strokes.py` | `Lines 221–233` | `def svg(audit, width, height):` | رمز برمجي موثق. | [discovery_strokes.py.md](code_mirrors/discovery_strokes.py.md) |
| `save` | `function` | `discovery_strokes.py` | `Lines 236–244` | `def save(source, directory):` | رمز برمجي موثق. | [discovery_strokes.py.md](code_mirrors/discovery_strokes.py.md) |
| `mask_metrics` | `function` | `measure.py` | `Lines 20–24` | `def mask_metrics(truth,pred):` | رمز برمجي موثق. | [measure.py.md](code_mirrors/measure.py.md) |
| `proposal_samples` | `function` | `measure.py` | `Lines 26–29` | `def proposal_samples(proposal):` | رمز برمجي موثق. | [measure.py.md](code_mirrors/measure.py.md) |
| `evaluate_discovery` | `function` | `measure.py` | `Lines 31–70` | `def evaluate_discovery(case):` | رمز برمجي موثق. | [measure.py.md](code_mirrors/measure.py.md) |
| `run` | `function` | `measure.py` | `Lines 72–83` | `def run():` | رمز برمجي موثق. | [measure.py.md](code_mirrors/measure.py.md) |
| `destination` | `function` | `phase_b.py` | `Lines 17–17` | `def destination(case):return (WORK/'exporter_discovery/external_results' if case=='fine_features' else ROOT/'results')/case` | رمز برمجي موثق. | [phase_b.py.md](code_mirrors/phase_b.py.md) |
| `render_size` | `function` | `phase_b.py` | `Lines 19–20` | `def render_size(svg,png,width,height,scale=1):` | رمز برمجي موثق. | [phase_b.py.md](code_mirrors/phase_b.py.md) |
| `execute` | `function` | `phase_b.py` | `Lines 22–51` | `def execute(case):` | رمز برمجي موثق. | [phase_b.py.md](code_mirrors/phase_b.py.md) |
| `line` | `function` | `qa/audit_intersections.py` | `Lines 11–21` | `def line(chain):` | رمز برمجي موثق. | [qa__audit_intersections.py.md](code_mirrors/qa__audit_intersections.py.md) |
| `defects` | `function` | `qa/audit_intersections.py` | `Lines 22–28` | `def defects(g):` | رمز برمجي موثق. | [qa__audit_intersections.py.md](code_mirrors/qa__audit_intersections.py.md) |
| `topo` | `function` | `qa/audit_masks.py` | `Lines 11–14` | `def topo(mask):` | رمز برمجي موثق. | [qa__audit_masks.py.md](code_mirrors/qa__audit_masks.py.md) |
| `stats` | `function` | `qa/audit_masks.py` | `Lines 15–16` | `def stats(truth,pred):` | رمز برمجي موثق. | [qa__audit_masks.py.md](code_mirrors/qa__audit_masks.py.md) |
| `load` | `function` | `qa/audit_saved.py` | `Lines 12–12` | `def load(p):return json.loads(Path(p).read_text(encoding='utf-8'))` | رمز برمجي موثق. | [qa__audit_saved.py.md](code_mirrors/qa__audit_saved.py.md) |
| `directed` | `function` | `qa/audit_saved.py` | `Lines 13–13` | `def directed(g):return {f:collections.Counter((r['chain'],r['forward']) for ring in loops for r in ring) for f,loops in g['faces'].items()}` | رمز برمجي موثق. | [qa__audit_saved.py.md](code_mirrors/qa__audit_saved.py.md) |
| `cross` | `function` | `qa/audit_saved.py` | `Lines 14–14` | `def cross(a,b):return float(a[0]*b[1]-a[1]*b[0])` | رمز برمجي موثق. | [qa__audit_saved.py.md](code_mirrors/qa__audit_saved.py.md) |
| `open_area` | `function` | `qa/audit_saved.py` | `Lines 15–15` | `def open_area(points):return .5*sum(cross(a,b) for a,b in zip(points[:-1],points[1:]))` | رمز برمجي موثق. | [qa__audit_saved.py.md](code_mirrors/qa__audit_saved.py.md) |
| `curve_area` | `function` | `qa/audit_saved.py` | `Lines 17–22` | `def curve_area(s):` | رمز برمجي موثق. | [qa__audit_saved.py.md](code_mirrors/qa__audit_saved.py.md) |
| `collapsed` | `function` | `qa/audit_saved.py` | `Lines 23–38` | `def collapsed(g):` | رمز برمجي موثق. | [qa__audit_saved.py.md](code_mirrors/qa__audit_saved.py.md) |
| `interp` | `function` | `qa/check_saved_svg_semantics.py` | `Lines 9–19` | `def interp(data):` | رمز برمجي موثق. | [qa__check_saved_svg_semantics.py.md](code_mirrors/qa__check_saved_svg_semantics.py.md) |
| `expected` | `function` | `qa/check_saved_svg_semantics.py` | `Lines 20–30` | `def expected(chain,raw,forward):` | رمز برمجي موثق. | [qa__check_saved_svg_semantics.py.md](code_mirrors/qa__check_saved_svg_semantics.py.md) |
| `diagnostic` | `function` | `qa/diagnose_rejected_fit.py` | `Lines 19–96` | `def diagnostic(source_json, target):` | رمز برمجي موثق. | [qa__diagnose_rejected_fit.py.md](code_mirrors/qa__diagnose_rejected_fit.py.md) |
| `interpreted` | `function` | `qa/independent_semantics.py` | `Lines 13–24` | `def interpreted(text):` | رمز برمجي موثق. | [qa__independent_semantics.py.md](code_mirrors/qa__independent_semantics.py.md) |
| `visit` | `function` | `qa/verify_frozen.py` | `Lines 11–17` | `def visit(obj):` | رمز برمجي موثق. | [qa__verify_frozen.py.md](code_mirrors/qa__verify_frozen.py.md) |
| `build` | `function` | `review.py` | `Lines 12–57` | `def build():` | رمز برمجي موثق. | [review.py.md](code_mirrors/review.py.md) |
| `build.pic` | `nested_function` | `review.py` | `Lines 16–16` | `def pic(base,name,label,link=None):return f'<figure><a href="{base}/{link or name}"><img loading="lazy" src="{base}/{name}" alt="{html.escape(label)}"></a><figcaption>{html.escape(label)}</figcaption></figure>'` | رمز برمجي موثق. | [review.py.md](code_mirrors/review.py.md) |
| `_point` | `function` | `svg_exporter.py` | `Lines 12–15` | `def _point(value):` | رمز برمجي موثق. | [svg_exporter.py.md](code_mirrors/svg_exporter.py.md) |
| `_same` | `function` | `svg_exporter.py` | `Lines 18–19` | `def _same(a, b):` | رمز برمجي موثق. | [svg_exporter.py.md](code_mirrors/svg_exporter.py.md) |
| `chain_segments` | `function` | `svg_exporter.py` | `Lines 22–54` | `def chain_segments(chain, raw=False, forward=True):` | Return directed L/C segments, including a logical chain closure. | [svg_exporter.py.md](code_mirrors/svg_exporter.py.md) |
| `_coordinate` | `function` | `svg_exporter.py` | `Lines 57–58` | `def _coordinate(point, precision):` | رمز برمجي موثق. | [svg_exporter.py.md](code_mirrors/svg_exporter.py.md) |
| `_commands` | `function` | `svg_exporter.py` | `Lines 61–65` | `def _commands(segments, move=True, precision=17):` | رمز برمجي موثق. | [svg_exporter.py.md](code_mirrors/svg_exporter.py.md) |
| `_color` | `function` | `svg_exporter.py` | `Lines 68–70` | `def _color(label):` | رمز برمجي موثق. | [svg_exporter.py.md](code_mirrors/svg_exporter.py.md) |
| `svg_graph` | `function` | `svg_exporter.py` | `Lines 73–114` | `def svg_graph(graph, raw=False, regions=False, foreground=None, *, precision=17):` | API-compatible strict replacement for research geometry_eval.svg_graph. | [svg_exporter.py.md](code_mirrors/svg_exporter.py.md) |
| `SourceStrokeTests` | `class` | `test_discovery_strokes.py` | `Lines 8–60` | `class SourceStrokeTests(unittest.TestCase):` | رمز برمجي موثق. | [test_discovery_strokes.py.md](code_mirrors/test_discovery_strokes.py.md) |
| `SourceStrokeTests.test_uniform_has_no_candidates` | `method` | `test_discovery_strokes.py` | `Lines 9–12` | `def test_uniform_has_no_candidates(self):` | رمز برمجي موثق. | [test_discovery_strokes.py.md](code_mirrors/test_discovery_strokes.py.md) |
| `SourceStrokeTests.test_single_boundary_not_stroke` | `method` | `test_discovery_strokes.py` | `Lines 14–17` | `def test_single_boundary_not_stroke(self):` | رمز برمجي موثق. | [test_discovery_strokes.py.md](code_mirrors/test_discovery_strokes.py.md) |
| `SourceStrokeTests.test_absent_label_thin_stroke_proposal` | `method` | `test_discovery_strokes.py` | `Lines 19–27` | `def test_absent_label_thin_stroke_proposal(self):` | رمز برمجي موثق. | [test_discovery_strokes.py.md](code_mirrors/test_discovery_strokes.py.md) |
| `SourceStrokeTests.test_deterministic_geometry` | `method` | `test_discovery_strokes.py` | `Lines 29–32` | `def test_deterministic_geometry(self):` | رمز برمجي موثق. | [test_discovery_strokes.py.md](code_mirrors/test_discovery_strokes.py.md) |
| `SourceStrokeTests.test_junction_trace_edges_once` | `method` | `test_discovery_strokes.py` | `Lines 34–40` | `def test_junction_trace_edges_once(self):` | رمز برمجي موثق. | [test_discovery_strokes.py.md](code_mirrors/test_discovery_strokes.py.md) |
| `SourceStrokeTests.test_corner_fit_keeps_vertex` | `method` | `test_discovery_strokes.py` | `Lines 42–47` | `def test_corner_fit_keeps_vertex(self):` | رمز برمجي موثق. | [test_discovery_strokes.py.md](code_mirrors/test_discovery_strokes.py.md) |
| `SourceStrokeTests.test_loop_trace_closes_once` | `method` | `test_discovery_strokes.py` | `Lines 49–56` | `def test_loop_trace_closes_once(self):` | رمز برمجي موثق. | [test_discovery_strokes.py.md](code_mirrors/test_discovery_strokes.py.md) |
| `SourceStrokeTests.test_invalid_input` | `method` | `test_discovery_strokes.py` | `Lines 58–60` | `def test_invalid_input(self):` | رمز برمجي موثق. | [test_discovery_strokes.py.md](code_mirrors/test_discovery_strokes.py.md) |
| `parse_path` | `function` | `test_svg_exporter.py` | `Lines 15–47` | `def parse_path(data):` | Interpret emitted absolute M/L/C/Z without serializer helper reuse. | [test_svg_exporter.py.md](code_mirrors/test_svg_exporter.py.md) |
| `line_chain` | `function` | `test_svg_exporter.py` | `Lines 50–53` | `def line_chain(identifier, points, closed=False):` | رمز برمجي موثق. | [test_svg_exporter.py.md](code_mirrors/test_svg_exporter.py.md) |
| `graph` | `function` | `test_svg_exporter.py` | `Lines 56–57` | `def graph(chains, loops=None):` | رمز برمجي موثق. | [test_svg_exporter.py.md](code_mirrors/test_svg_exporter.py.md) |
| `ref` | `function` | `test_svg_exporter.py` | `Lines 60–61` | `def ref(identifier, forward=True):` | رمز برمجي موثق. | [test_svg_exporter.py.md](code_mirrors/test_svg_exporter.py.md) |
| `paths` | `function` | `test_svg_exporter.py` | `Lines 64–65` | `def paths(svg):` | رمز برمجي موثق. | [test_svg_exporter.py.md](code_mirrors/test_svg_exporter.py.md) |
| `svg_data` | `function` | `test_svg_exporter.py` | `Lines 68–70` | `def svg_data(data, regions=True):` | رمز برمجي موثق. | [test_svg_exporter.py.md](code_mirrors/test_svg_exporter.py.md) |
| `SemanticTests` | `class` | `test_svg_exporter.py` | `Lines 73–136` | `class SemanticTests(unittest.TestCase):` | رمز برمجي موثق. | [test_svg_exporter.py.md](code_mirrors/test_svg_exporter.py.md) |
| `SemanticTests.test_precision_control_is_explicit_and_default_roundtrips` | `method` | `test_svg_exporter.py` | `Lines 74–79` | `def test_precision_control_is_explicit_and_default_roundtrips(self):` | رمز برمجي موثق. | [test_svg_exporter.py.md](code_mirrors/test_svg_exporter.py.md) |
| `SemanticTests.test_single_open_and_closed_preserve_corners` | `method` | `test_svg_exporter.py` | `Lines 81–88` | `def test_single_open_and_closed_preserve_corners(self):` | رمز برمجي موثق. | [test_svg_exporter.py.md](code_mirrors/test_svg_exporter.py.md) |
| `SemanticTests.test_independent_subpaths_hole_nested_evenodd` | `method` | `test_svg_exporter.py` | `Lines 90–95` | `def test_independent_subpaths_hole_nested_evenodd(self):` | رمز برمجي موثق. | [test_svg_exporter.py.md](code_mirrors/test_svg_exporter.py.md) |
| `SemanticTests.test_embedded_closed_chain_has_own_explicit_closure` | `method` | `test_svg_exporter.py` | `Lines 97–104` | `def test_embedded_closed_chain_has_own_explicit_closure(self):` | رمز برمجي موثق. | [test_svg_exporter.py.md](code_mirrors/test_svg_exporter.py.md) |
| `SemanticTests.test_reverse_cubic_controls_and_implicit_closure_order` | `method` | `test_svg_exporter.py` | `Lines 106–111` | `def test_reverse_cubic_controls_and_implicit_closure_order(self):` | رمز برمجي موثق. | [test_svg_exporter.py.md](code_mirrors/test_svg_exporter.py.md) |
| `SemanticTests.test_shared_boundary_repeated_junctions_preserved` | `method` | `test_svg_exporter.py` | `Lines 113–121` | `def test_shared_boundary_repeated_junctions_preserved(self):` | رمز برمجي موثق. | [test_svg_exporter.py.md](code_mirrors/test_svg_exporter.py.md) |
| `SemanticTests.test_mixed_open_closed_and_input_immutable` | `method` | `test_svg_exporter.py` | `Lines 123–126` | `def test_mixed_open_closed_and_input_immutable(self):` | رمز برمجي موثق. | [test_svg_exporter.py.md](code_mirrors/test_svg_exporter.py.md) |
| `SemanticTests.test_fail_closed_disconnected_unsupported_nonfinite_open_face` | `method` | `test_svg_exporter.py` | `Lines 128–136` | `def test_fail_closed_disconnected_unsupported_nonfinite_open_face(self):` | رمز برمجي موثق. | [test_svg_exporter.py.md](code_mirrors/test_svg_exporter.py.md) |
| `RendererTests` | `class` | `test_svg_exporter.py` | `Lines 139–176` | `class RendererTests(unittest.TestCase):` | رمز برمجي موثق. | [test_svg_exporter.py.md](code_mirrors/test_svg_exporter.py.md) |
| `RendererTests.test_actual_resvg_known_canonical_fixtures` | `method` | `test_svg_exporter.py` | `Lines 140–176` | `def test_actual_resvg_known_canonical_fixtures(self):` | رمز برمجي موثق. | [test_svg_exporter.py.md](code_mirrors/test_svg_exporter.py.md) |
