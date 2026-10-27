# السجل المركزي الموحد للدوال والكلاسات والرموز (`memory/FUNCTION_REGISTRY.md`)

> **مرجعية الكود ومستويات منع التكرار (`Source Authority & 3-Tier Deduplication Policy`):**
> 1. **المستوى الأول — تكرار الاسم المطابق (`Exact-Name Duplication`):** فحص حتمي آلي 100% يمنع وجود دالتين بنفس الاسم عبر الملفات.
> 2. **المستوى الثاني — التشابه الهيكلي للـ AST (`Structural AST Similarity`):** فحص آلي تحذيري يرصد الدوال ذات البنية الهيكلية المتطابقة للمراجعة.
> 3. **المستوى الثالث — التكرار الدلالي (`Semantic Duplication`):** **ليس آلياً بالكامل**؛ يتطلب من كل Agent قراءة عمود الوظيفة (`Purpose`) أدناه قبل كتابة أي دالة جديدة، ويخضع لتدقيق الـ Sub-Agent المراجع (`qa-reviewer-auditor`).

- **إجمالي الملفات البرمجية المفحوصة:** `4`
- **إجمالي الرموز المسجلة بالسطر (شاملة Methods وNested وArrow):** `21`
- **عدد الدوال المتطابقة الاسم غير المسموحة (`Exact-Name Duplicates`):** `0`
- **مرشحات التشابه الهيكلي (`Structural Similarity Candidates`):** `0`

## جدول جميع الدوال والكلاسات والرموز في المشروع (`Master Symbol Index`)

| اسم الرمز (`Symbol`) | النوع (`Kind`) | الملف المالك (`Owner File`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة (`Purpose`) | مرآة الكود التفصيلية (`Code Mirror`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `fetch` | `function` | `acquire_dataset.py` | `Lines 29–32` | `def fetch(url):` | رمز برمجي موثق. | [acquire_dataset.py.md](code_mirrors/acquire_dataset.py.md) |
| `digest` | `function` | `acquire_dataset.py` | `Lines 34–35` | `def digest(data):` | رمز برمجي موثق. | [acquire_dataset.py.md](code_mirrors/acquire_dataset.py.md) |
| `alpha_info` | `function` | `acquire_dataset.py` | `Lines 37–40` | `def alpha_info(image):` | رمز برمجي موثق. | [acquire_dataset.py.md](code_mirrors/acquire_dataset.py.md) |
| `main` | `function` | `acquire_dataset.py` | `Lines 42–91` | `def main():` | رمز برمجي موثق. | [acquire_dataset.py.md](code_mirrors/acquire_dataset.py.md) |
| `saved_file_digest` | `function` | `package_evidence.py` | `Lines 13–15` | `def saved_file_digest(path):` | Read-only content digest. | [package_evidence.py.md](code_mirrors/package_evidence.py.md) |
| `saved_inventory` | `function` | `package_evidence.py` | `Lines 17–20` | `def saved_inventory():` | Freeze inherited evidence independently of packaging artifacts. | [package_evidence.py.md](code_mirrors/package_evidence.py.md) |
| `appearance` | `function` | `package_evidence.py` | `Lines 22–25` | `def appearance(image,bg):` | Apply saved evaluator's exact 8-bit sRGB compositing policy. | [package_evidence.py.md](code_mirrors/package_evidence.py.md) |
| `check_saved_evidence` | `function` | `package_evidence.py` | `Lines 27–93` | `def check_saved_evidence():` | Independently decode all artifacts and recompute selected appearance metrics. | [package_evidence.py.md](code_mirrors/package_evidence.py.md) |
| `make_visual_evidence` | `function` | `package_evidence.py` | `Lines 95–130` | `def make_visual_evidence(summary):` | Create saved-render sheets and HTML showing actual original SVG browser zoom. | [package_evidence.py.md](code_mirrors/package_evidence.py.md) |
| `package_existing_outputs` | `function` | `package_evidence.py` | `Lines 132–138` | `def package_existing_outputs():` | Check byte preservation before/after writing new reports and comparisons. | [package_evidence.py.md](code_mirrors/package_evidence.py.md) |
| `read_suite` | `function` | `runner.py` | `Lines 14–19` | `def read_suite(path):` | Load frozen case list and reject hash drift before invoking any search. | [runner.py.md](code_mirrors/runner.py.md) |
| `rgb_diagnostics` | `function` | `runner.py` | `Lines 21–27` | `def rgb_diagnostics(reference,predicted):` | Inherited metrics plus independent worst spatial-tile residual diagnostics. | [runner.py.md](code_mirrors/runner.py.md) |
| `run_generalization_case` | `function` | `runner.py` | `Lines 29–85` | `def run_generalization_case(case,manifest_hash,max_candidates=24,max_seconds=240):` | One inherited search per unseen image; new alpha selection reuses its candidates. | [runner.py.md](code_mirrors/runner.py.md) |
| `SavedGeneralizationEvidenceTests` | `class` | `test_saved_evidence.py` | `Lines 7–27` | `class SavedGeneralizationEvidenceTests(unittest.TestCase):` | رمز برمجي موثق. | [test_saved_evidence.py.md](code_mirrors/test_saved_evidence.py.md) |
| `SavedGeneralizationEvidenceTests.setUpClass` | `method` | `test_saved_evidence.py` | `Lines 9–10` | `def setUpClass(cls):` | رمز برمجي موثق. | [test_saved_evidence.py.md](code_mirrors/test_saved_evidence.py.md) |
| `SavedGeneralizationEvidenceTests.test_frozen_sources_and_140_successful_candidates` | `method` | `test_saved_evidence.py` | `Lines 11–12` | `def test_frozen_sources_and_140_successful_candidates(self):` | رمز برمجي موثق. | [test_saved_evidence.py.md](code_mirrors/test_saved_evidence.py.md) |
| `SavedGeneralizationEvidenceTests.test_no_reconstruction_improvement_or_reranked_winner` | `method` | `test_saved_evidence.py` | `Lines 13–14` | `def test_no_reconstruction_improvement_or_reranked_winner(self):` | رمز برمجي موثق. | [test_saved_evidence.py.md](code_mirrors/test_saved_evidence.py.md) |
| `SavedGeneralizationEvidenceTests.test_selected_transparency_exact_at_test_dimensions` | `method` | `test_saved_evidence.py` | `Lines 15–17` | `def test_selected_transparency_exact_at_test_dimensions(self):` | رمز برمجي موثق. | [test_saved_evidence.py.md](code_mirrors/test_saved_evidence.py.md) |
| `SavedGeneralizationEvidenceTests.test_saved_metrics_and_all_svg_png_artifacts` | `method` | `test_saved_evidence.py` | `Lines 18–19` | `def test_saved_metrics_and_all_svg_png_artifacts(self):` | رمز برمجي موثق. | [test_saved_evidence.py.md](code_mirrors/test_saved_evidence.py.md) |
| `SavedGeneralizationEvidenceTests.test_saved_evidence_byte_preservation` | `method` | `test_saved_evidence.py` | `Lines 20–21` | `def test_saved_evidence_byte_preservation(self):` | رمز برمجي موثق. | [test_saved_evidence.py.md](code_mirrors/test_saved_evidence.py.md) |
| `SavedGeneralizationEvidenceTests.test_visual_sheets_decode_and_dashboard_has_all_cases` | `method` | `test_saved_evidence.py` | `Lines 22–27` | `def test_visual_sheets_decode_and_dashboard_has_all_cases(self):` | رمز برمجي موثق. | [test_saved_evidence.py.md](code_mirrors/test_saved_evidence.py.md) |
