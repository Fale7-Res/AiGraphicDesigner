# السجل المركزي الموحد للدوال والكلاسات والرموز (`memory/FUNCTION_REGISTRY.md`)

> **مرجعية الكود ومستويات منع التكرار (`Source Authority & 3-Tier Deduplication Policy`):**
> 1. **المستوى الأول — تكرار الاسم المطابق (`Exact-Name Duplication`):** فحص حتمي آلي 100% يمنع وجود دالتين بنفس الاسم عبر الملفات.
> 2. **المستوى الثاني — التشابه الهيكلي للـ AST (`Structural AST Similarity`):** فحص آلي تحذيري يرصد الدوال ذات البنية الهيكلية المتطابقة للمراجعة.
> 3. **المستوى الثالث — التكرار الدلالي (`Semantic Duplication`):** **ليس آلياً بالكامل**؛ يتطلب من كل Agent قراءة عمود الوظيفة (`Purpose`) أدناه قبل كتابة أي دالة جديدة، ويخضع لتدقيق الـ Sub-Agent المراجع (`qa-reviewer-auditor`).

- **إجمالي الملفات البرمجية المفحوصة:** `15`
- **إجمالي الرموز المسجلة بالسطر (شاملة Methods وNested وArrow):** `32`
- **عدد الدوال المتطابقة الاسم غير المسموحة (`Exact-Name Duplicates`):** `0`
- **مرشحات التشابه الهيكلي (`Structural Similarity Candidates`):** `1`

## جدول جميع الدوال والكلاسات والرموز في المشروع (`Master Symbol Index`)

| اسم الرمز (`Symbol`) | النوع (`Kind`) | الملف المالك (`Owner File`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة (`Purpose`) | مرآة الكود التفصيلية (`Code Mirror`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `image_link` | `function` | `build_review.py` | `Lines 8–9` | `def image_link(path,label):` | رمز برمجي موثق. | [build_review.py.md](code_mirrors/build_review.py.md) |
| `make_review` | `function` | `build_review.py` | `Lines 11–53` | `def make_review(target,local_delivery=False):` | رمز برمجي موثق. | [build_review.py.md](code_mirrors/build_review.py.md) |
| `paths` | `function` | `construct_geometry.py` | `Lines 21–24` | `def paths(case):` | رمز برمجي موثق. | [construct_geometry.py.md](code_mirrors/construct_geometry.py.md) |
| `chain_graph` | `function` | `construct_geometry.py` | `Lines 26–32` | `def chain_graph(curves,width,height):` | رمز برمجي موثق. | [construct_geometry.py.md](code_mirrors/construct_geometry.py.md) |
| `build` | `function` | `construct_geometry.py` | `Lines 34–73` | `def build(case):` | رمز برمجي موثق. | [construct_geometry.py.md](code_mirrors/construct_geometry.py.md) |
| `support_stats` | `function` | `evaluate_results.py` | `Lines 17–20` | `def support_stats(target,pred,tolerance):` | رمز برمجي موثق. | [evaluate_results.py.md](code_mirrors/evaluate_results.py.md) |
| `xy` | `function` | `evaluate_results.py` | `Lines 22–22` | `def xy(mask):return np.argwhere(mask)[:,::-1].astype(float)+.5` | رمز برمجي موثق. | [evaluate_results.py.md](code_mirrors/evaluate_results.py.md) |
| `samples_from_items` | `function` | `evaluate_results.py` | `Lines 24–29` | `def samples_from_items(items):` | رمز برمجي موثق. | [evaluate_results.py.md](code_mirrors/evaluate_results.py.md) |
| `render` | `function` | `evaluate_results.py` | `Lines 31–33` | `def render(svg,png,w,h,scale):` | رمز برمجي موثق. | [evaluate_results.py.md](code_mirrors/evaluate_results.py.md) |
| `evaluate` | `function` | `evaluate_results.py` | `Lines 35–89` | `def evaluate(case):` | رمز برمجي موثق. | [evaluate_results.py.md](code_mirrors/evaluate_results.py.md) |
| `infer` | `function` | `infer_dexined.py` | `Lines 13–29` | `def infer(source,weights,out):` | رمز برمجي موثق. | [infer_dexined.py.md](code_mirrors/infer_dexined.py.md) |
| `Links` | `class` | `qa/audit_final.py` | `Lines 10–14` | `class Links(HTMLParser):` | رمز برمجي موثق. | [qa__audit_final.py.md](code_mirrors/qa__audit_final.py.md) |
| `Links.__init__` | `method` | `qa/audit_final.py` | `Lines 11–11` | `def __init__(self):super().__init__();self.links=[]` | رمز برمجي موثق. | [qa__audit_final.py.md](code_mirrors/qa__audit_final.py.md) |
| `Links.handle_starttag` | `method` | `qa/audit_final.py` | `Lines 12–14` | `def handle_starttag(self,tag,attrs):` | رمز برمجي موثق. | [qa__audit_final.py.md](code_mirrors/qa__audit_final.py.md) |
| `dists` | `function` | `qa/audit_metrics.py` | `Lines 10–12` | `def dists(a,b):` | رمز برمجي موثق. | [qa__audit_metrics.py.md](code_mirrors/qa__audit_metrics.py.md) |
| `sample` | `function` | `qa/audit_metrics.py` | `Lines 13–18` | `def sample(p):` | رمز برمجي موثق. | [qa__audit_metrics.py.md](code_mirrors/qa__audit_metrics.py.md) |
| `flatten` | `function` | `stable_fit.py` | `Lines 16–30` | `def flatten(curve, epsilon=.002, depth=0):` | Adaptive control-hull distance bound, excluding unresolved recursion. | [stable_fit.py.md](code_mirrors/stable_fit.py.md) |
| `sample_segments` | `function` | `stable_fit.py` | `Lines 33–38` | `def sample_segments(points, step=.01):` | رمز برمجي موثق. | [stable_fit.py.md](code_mirrors/stable_fit.py.md) |
| `measure` | `function` | `stable_fit.py` | `Lines 41–60` | `def measure(points, curves, step=.01, epsilon=.002):` | Segment distances, never nearest sampled-vertex distances. | [stable_fit.py.md](code_mirrors/stable_fit.py.md) |
| `construct` | `function` | `stable_fit.py` | `Lines 63–81` | `def construct(vertices):` | Per-chord handles; long neighbors cannot stretch a short chord's handle. | [stable_fit.py.md](code_mirrors/stable_fit.py.md) |
| `fit` | `function` | `stable_fit.py` | `Lines 84–128` | `def fit(points, maximum_deviation=.6, maximum_segments=64):` | Frozen RDP, chord handles, <=8 rounds subdivision, no grid fallback. | [stable_fit.py.md](code_mirrors/stable_fit.py.md) |
| `MetricTests` | `class` | `test_metrics.py` | `Lines 10–29` | `class MetricTests(unittest.TestCase):` | رمز برمجي موثق. | [test_metrics.py.md](code_mirrors/test_metrics.py.md) |
| `MetricTests.test_exact_and_displaced_support` | `method` | `test_metrics.py` | `Lines 11–14` | `def test_exact_and_displaced_support(self):` | رمز برمجي موثق. | [test_metrics.py.md](code_mirrors/test_metrics.py.md) |
| `MetricTests.test_empty_support_is_failure` | `method` | `test_metrics.py` | `Lines 16–19` | `def test_empty_support_is_failure(self):` | رمز برمجي موثق. | [test_metrics.py.md](code_mirrors/test_metrics.py.md) |
| `MetricTests.test_pixel_centers_are_explicit` | `method` | `test_metrics.py` | `Lines 21–23` | `def test_pixel_centers_are_explicit(self):` | رمز برمجي موثق. | [test_metrics.py.md](code_mirrors/test_metrics.py.md) |
| `MetricTests.test_open_curve_has_no_implicit_closure` | `method` | `test_metrics.py` | `Lines 25–29` | `def test_open_curve_has_no_implicit_closure(self):` | رمز برمجي موثق. | [test_metrics.py.md](code_mirrors/test_metrics.py.md) |
| `StableFitTests` | `class` | `test_stable_fit.py` | `Lines 8–28` | `class StableFitTests(unittest.TestCase):` | رمز برمجي موثق. | [test_stable_fit.py.md](code_mirrors/test_stable_fit.py.md) |
| `StableFitTests.test_unequal_chord_cannot_create_long_short_handle` | `method` | `test_stable_fit.py` | `Lines 9–13` | `def test_unequal_chord_cannot_create_long_short_handle(self):` | رمز برمجي موثق. | [test_stable_fit.py.md](code_mirrors/test_stable_fit.py.md) |
| `StableFitTests.test_sharp_corner_preserved` | `method` | `test_stable_fit.py` | `Lines 14–19` | `def test_sharp_corner_preserved(self):` | رمز برمجي موثق. | [test_stable_fit.py.md](code_mirrors/test_stable_fit.py.md) |
| `StableFitTests.test_no_budget_fallback` | `method` | `test_stable_fit.py` | `Lines 20–23` | `def test_no_budget_fallback(self):` | رمز برمجي موثق. | [test_stable_fit.py.md](code_mirrors/test_stable_fit.py.md) |
| `StableFitTests.test_nonfinite_rejected` | `method` | `test_stable_fit.py` | `Lines 24–25` | `def test_nonfinite_rejected(self):` | رمز برمجي موثق. | [test_stable_fit.py.md](code_mirrors/test_stable_fit.py.md) |
| `StableFitTests.test_segment_distance_not_vertex_distance` | `method` | `test_stable_fit.py` | `Lines 26–28` | `def test_segment_distance_not_vertex_distance(self):` | رمز برمجي موثق. | [test_stable_fit.py.md](code_mirrors/test_stable_fit.py.md) |
