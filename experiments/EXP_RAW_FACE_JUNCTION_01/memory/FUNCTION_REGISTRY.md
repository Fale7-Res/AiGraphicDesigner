# السجل المركزي الموحد للدوال والكلاسات والرموز (`memory/FUNCTION_REGISTRY.md`)

> **مرجعية الكود ومستويات منع التكرار (`Source Authority & 3-Tier Deduplication Policy`):**
> 1. **المستوى الأول — تكرار الاسم المطابق (`Exact-Name Duplication`):** فحص حتمي آلي 100% يمنع وجود دالتين بنفس الاسم عبر الملفات.
> 2. **المستوى الثاني — التشابه الهيكلي للـ AST (`Structural AST Similarity`):** فحص آلي تحذيري يرصد الدوال ذات البنية الهيكلية المتطابقة للمراجعة.
> 3. **المستوى الثالث — التكرار الدلالي (`Semantic Duplication`):** **ليس آلياً بالكامل**؛ يتطلب من كل Agent قراءة عمود الوظيفة (`Purpose`) أدناه قبل كتابة أي دالة جديدة، ويخضع لتدقيق الـ Sub-Agent المراجع (`qa-reviewer-auditor`).

- **إجمالي الملفات البرمجية المفحوصة:** `10`
- **إجمالي الرموز المسجلة بالسطر (شاملة Methods وNested وArrow):** `23`
- **عدد الدوال المتطابقة الاسم غير المسموحة (`Exact-Name Duplicates`):** `0`
- **مرشحات التشابه الهيكلي (`Structural Similarity Candidates`):** `0`

## جدول جميع الدوال والكلاسات والرموز في المشروع (`Master Symbol Index`)

| اسم الرمز (`Symbol`) | النوع (`Kind`) | الملف المالك (`Owner File`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة (`Purpose`) | مرآة الكود التفصيلية (`Code Mirror`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `directed_occurrences` | `function` | `face_cycles.py` | `Lines 9–10` | `def directed_occurrences(faces):` | رمز برمجي موثق. | [face_cycles.py.md](code_mirrors/face_cycles.py.md) |
| `split_closed_walk` | `function` | `face_cycles.py` | `Lines 12–32` | `def split_closed_walk(refs,raw,max_splits=8192):` | Partition only at exact repeated chain endpoints; retain every occurrence. | [face_cycles.py.md](code_mirrors/face_cycles.py.md) |
| `decompose` | `function` | `face_cycles.py` | `Lines 34–60` | `def decompose(graph):` | رمز برمجي موثق. | [face_cycles.py.md](code_mirrors/face_cycles.py.md) |
| `measure` | `function` | `measure_results.py` | `Lines 14–49` | `def measure():` | رمز برمجي موثق. | [measure_results.py.md](code_mirrors/measure_results.py.md) |
| `occurrence` | `function` | `qa/check_outputs.py` | `Lines 12–12` | `def occurrence(g):return {f:collections.Counter((r['chain'],r['forward']) for w in rings for r in w) for f,rings in g['faces'].items()}` | رمز برمجي موثق. | [qa__check_outputs.py.md](code_mirrors/qa__check_outputs.py.md) |
| `build` | `function` | `review.py` | `Lines 13–69` | `def build():` | رمز برمجي موثق. | [review.py.md](code_mirrors/review.py.md) |
| `build.pic` | `nested_function` | `review.py` | `Lines 17–17` | `def pic(base,name,label,link=None):return f'<figure><a href="{base}/{link or name}"><img loading="lazy" src="{base}/{name}" alt="{html.escape(label)}"></a><figcaption>{html.escape(label)}</figcaption></figure>'` | رمز برمجي موثق. | [review.py.md](code_mirrors/review.py.md) |
| `destination` | `function` | `run_case.py` | `Lines 19–20` | `def destination(case):` | رمز برمجي موثق. | [run_case.py.md](code_mirrors/run_case.py.md) |
| `execute` | `function` | `run_case.py` | `Lines 22–45` | `def execute(case):` | رمز برمجي موثق. | [run_case.py.md](code_mirrors/run_case.py.md) |
| `_near` | `function` | `source_evidence_probe.py` | `Lines 31–36` | `def _near(mask: np.ndarray, radius: float) -> np.ndarray:` | رمز برمجي موثق. | [source_evidence_probe.py.md](code_mirrors/source_evidence_probe.py.md) |
| `extract` | `function` | `source_evidence_probe.py` | `Lines 39–94` | `def extract(rgb: np.ndarray) -> tuple[dict[str, np.ndarray], dict]:` | Extract fixed maps from native uint8 RGB. Never infer region ownership. | [source_evidence_probe.py.md](code_mirrors/source_evidence_probe.py.md) |
| `save` | `function` | `source_evidence_probe.py` | `Lines 97–120` | `def save(rgb_path: str | Path, output_dir: str | Path) -> None:` | CLI wrapper reads only source image and writes immutable evidence maps. | [source_evidence_probe.py.md](code_mirrors/source_evidence_probe.py.md) |
| `FaceWalkTests` | `class` | `test_face_cycles.py` | `Lines 6–23` | `class FaceWalkTests(unittest.TestCase):` | رمز برمجي موثق. | [test_face_cycles.py.md](code_mirrors/test_face_cycles.py.md) |
| `FaceWalkTests.test_pinched_triangles_preserve_every_directed_reference` | `method` | `test_face_cycles.py` | `Lines 7–12` | `def test_pinched_triangles_preserve_every_directed_reference(self):` | رمز برمجي موثق. | [test_face_cycles.py.md](code_mirrors/test_face_cycles.py.md) |
| `FaceWalkTests.test_no_silent_open_walk_fix` | `method` | `test_face_cycles.py` | `Lines 13–14` | `def test_no_silent_open_walk_fix(self):` | رمز برمجي موثق. | [test_face_cycles.py.md](code_mirrors/test_face_cycles.py.md) |
| `FaceWalkTests.test_reversed_references_and_hole_winding_not_reoriented` | `method` | `test_face_cycles.py` | `Lines 15–17` | `def test_reversed_references_and_hole_winding_not_reoriented(self):` | رمز برمجي موثق. | [test_face_cycles.py.md](code_mirrors/test_face_cycles.py.md) |
| `FaceWalkTests.test_degenerate_cycle_is_retained_not_pruned` | `method` | `test_face_cycles.py` | `Lines 18–20` | `def test_degenerate_cycle_is_retained_not_pruned(self):` | رمز برمجي موثق. | [test_face_cycles.py.md](code_mirrors/test_face_cycles.py.md) |
| `FaceWalkTests.test_budget_is_fail_closed` | `method` | `test_face_cycles.py` | `Lines 21–23` | `def test_budget_is_fail_closed(self):` | رمز برمجي موثق. | [test_face_cycles.py.md](code_mirrors/test_face_cycles.py.md) |
| `EvidenceTests` | `class` | `test_source_evidence_probe.py` | `Lines 8–36` | `class EvidenceTests(unittest.TestCase):` | رمز برمجي موثق. | [test_source_evidence_probe.py.md](code_mirrors/test_source_evidence_probe.py.md) |
| `EvidenceTests.test_constant_has_no_edges_or_ridges` | `method` | `test_source_evidence_probe.py` | `Lines 9–13` | `def test_constant_has_no_edges_or_ridges(self):` | رمز برمجي موثق. | [test_source_evidence_probe.py.md](code_mirrors/test_source_evidence_probe.py.md) |
| `EvidenceTests.test_empty_support_does_not_create_corner_evidence` | `method` | `test_source_evidence_probe.py` | `Lines 15–16` | `def test_empty_support_does_not_create_corner_evidence(self):` | رمز برمجي موثق. | [test_source_evidence_probe.py.md](code_mirrors/test_source_evidence_probe.py.md) |
| `EvidenceTests.test_deterministic_nonmutating_source_only` | `method` | `test_source_evidence_probe.py` | `Lines 18–31` | `def test_deterministic_nonmutating_source_only(self):` | رمز برمجي موثق. | [test_source_evidence_probe.py.md](code_mirrors/test_source_evidence_probe.py.md) |
| `EvidenceTests.test_rejects_ambiguous_float_or_rgba_input` | `method` | `test_source_evidence_probe.py` | `Lines 33–36` | `def test_rejects_ambiguous_float_or_rgba_input(self):` | رمز برمجي موثق. | [test_source_evidence_probe.py.md](code_mirrors/test_source_evidence_probe.py.md) |
