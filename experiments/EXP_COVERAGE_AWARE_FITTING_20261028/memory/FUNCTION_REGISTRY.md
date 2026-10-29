# السجل المركزي الموحد للدوال والكلاسات والرموز (`memory/FUNCTION_REGISTRY.md`)

> **مرجعية الكود ومستويات منع التكرار (`Source Authority & 3-Tier Deduplication Policy`):**
> 1. **المستوى الأول — تكرار الاسم المطابق (`Exact-Name Duplication`):** فحص حتمي آلي 100% يمنع وجود دالتين بنفس الاسم عبر الملفات.
> 2. **المستوى الثاني — التشابه الهيكلي للـ AST (`Structural AST Similarity`):** فحص آلي تحذيري يرصد الدوال ذات البنية الهيكلية المتطابقة للمراجعة.
> 3. **المستوى الثالث — التكرار الدلالي (`Semantic Duplication`):** **ليس آلياً بالكامل**؛ يتطلب من كل Agent قراءة عمود الوظيفة (`Purpose`) أدناه قبل كتابة أي دالة جديدة، ويخضع لتدقيق الـ Sub-Agent المراجع (`qa-reviewer-auditor`).

- **إجمالي الملفات البرمجية المفحوصة:** `8`
- **إجمالي الرموز المسجلة بالسطر (شاملة Methods وNested وArrow):** `53`
- **عدد الدوال المتطابقة الاسم غير المسموحة (`Exact-Name Duplicates`):** `0`
- **مرشحات التشابه الهيكلي (`Structural Similarity Candidates`):** `0`

## جدول جميع الدوال والكلاسات والرموز في المشروع (`Master Symbol Index`)

| اسم الرمز (`Symbol`) | النوع (`Kind`) | الملف المالك (`Owner File`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة (`Purpose`) | مرآة الكود التفصيلية (`Code Mirror`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `audit` | `function` | `audit_results.py` | `Lines 9–74` | `def audit():` | رمز برمجي موثق. | [audit_results.py.md](code_mirrors/audit_results.py.md) |
| `_historical` | `function` | `coverage_fitter.py` | `Lines 27–40` | `def _historical():` | رمز برمجي موثق. | [coverage_fitter.py.md](code_mirrors/coverage_fitter.py.md) |
| `_json` | `function` | `coverage_fitter.py` | `Lines 43–44` | `def _json(path, data):` | رمز برمجي موثق. | [coverage_fitter.py.md](code_mirrors/coverage_fitter.py.md) |
| `_hash` | `function` | `coverage_fitter.py` | `Lines 47–48` | `def _hash(path):` | رمز برمجي موثق. | [coverage_fitter.py.md](code_mirrors/coverage_fitter.py.md) |
| `_shape_signature` | `function` | `coverage_fitter.py` | `Lines 51–66` | `def _shape_signature(root):` | Ignore only visible-path RGB paint and gradient definitions; retain masks. | [coverage_fitter.py.md](code_mirrors/coverage_fitter.py.md) |
| `_shape_signature.visit` | `nested_function` | `coverage_fitter.py` | `Lines 54–65` | `def visit(node, inside_mask=False):` | رمز برمجي موثق. | [coverage_fitter.py.md](code_mirrors/coverage_fitter.py.md) |
| `_visible_gradient_ids` | `function` | `coverage_fitter.py` | `Lines 69–94` | `def _visible_gradient_ids(root):` | رمز برمجي موثق. | [coverage_fitter.py.md](code_mirrors/coverage_fitter.py.md) |
| `_visible_gradient_ids.visit` | `nested_function` | `coverage_fitter.py` | `Lines 71–75` | `def visit(node):` | رمز برمجي موثق. | [coverage_fitter.py.md](code_mirrors/coverage_fitter.py.md) |
| `_render` | `function` | `coverage_fitter.py` | `Lines 97–102` | `def _render(root, svg, png):` | رمز برمجي موثق. | [coverage_fitter.py.md](code_mirrors/coverage_fitter.py.md) |
| `_paint_probe` | `function` | `coverage_fitter.py` | `Lines 105–114` | `def _paint_probe(root, colors, old):` | رمز برمجي موثق. | [coverage_fitter.py.md](code_mirrors/coverage_fitter.py.md) |
| `build_maps` | `function` | `coverage_fitter.py` | `Lines 117–194` | `def build_maps(baseline_svg, folder):` | Measure per-path effective visibility; preserve full-scene opacity and masks. | [coverage_fitter.py.md](code_mirrors/coverage_fitter.py.md) |
| `_color` | `function` | `coverage_fitter.py` | `Lines 197–200` | `def _color(value):` | رمز برمجي موثق. | [coverage_fitter.py.md](code_mirrors/coverage_fitter.py.md) |
| `_models` | `function` | `coverage_fitter.py` | `Lines 203–230` | `def _models(root, old):` | رمز برمجي موثق. | [coverage_fitter.py.md](code_mirrors/coverage_fitter.py.md) |
| `_write_models` | `function` | `coverage_fitter.py` | `Lines 233–247` | `def _write_models(root, models, target, old):` | رمز برمجي موثق. | [coverage_fitter.py.md](code_mirrors/coverage_fitter.py.md) |
| `fit_case` | `function` | `coverage_fitter.py` | `Lines 250–356` | `def fit_case(source_png, baseline_flat_svg, baseline_gradient_svg, maps_folder,` | Fit flat and same-capacity gradient paint using full-scene linear coefficients. | [coverage_fitter.py.md](code_mirrors/coverage_fitter.py.md) |
| `fit_case.error` | `nested_function` | `coverage_fitter.py` | `Lines 270–270` | `def error(pred, mask):return float(np.mean((pred[mask]-target[mask])**2))` | رمز برمجي موثق. | [coverage_fitter.py.md](code_mirrors/coverage_fitter.py.md) |
| `fit_case.predict_models` | `nested_function` | `coverage_fitter.py` | `Lines 294–299` | `def predict_models(models):` | رمز برمجي موثق. | [coverage_fitter.py.md](code_mirrors/coverage_fitter.py.md) |
| `fixture_specs` | `function` | `fixtures.py` | `Lines 14–51` | `def fixture_specs():` | Ground truth uses <=7 paint paths, no bitmap/grid, <=4 equally spaced stops. | [fixtures.py.md](code_mirrors/fixtures.py.md) |
| `freeze_fixtures` | `function` | `fixtures.py` | `Lines 53–91` | `def freeze_fixtures():` | Write all fixture inputs before fitting; refuse nonempty generation targets. | [fixtures.py.md](code_mirrors/fixtures.py.md) |
| `rgb_on` | `function` | `presentation.py` | `Lines 14–16` | `def rgb_on(image,background='white'):` | رمز برمجي موثق. | [presentation.py.md](code_mirrors/presentation.py.md) |
| `number` | `function` | `presentation.py` | `Lines 18–20` | `def number(value,decimals=6):` | رمز برمجي موثق. | [presentation.py.md](code_mirrors/presentation.py.md) |
| `three_background_error` | `function` | `presentation.py` | `Lines 22–29` | `def three_background_error(source,predicted):` | Float composited three-background residual, matching driver's local-error policy. | [presentation.py.md](code_mirrors/presentation.py.md) |
| `choose_boxes` | `function` | `presentation.py` | `Lines 31–41` | `def choose_boxes(source,predicted,case):` | Worst complete 24px tile plus preregistered thin-feature box or center. | [presentation.py.md](code_mirrors/presentation.py.md) |
| `native_sheets` | `function` | `presentation.py` | `Lines 43–63` | `def native_sheets(case,result,folder):` | Package saved actual PNG renders with source, alpha and visible error maps. | [presentation.py.md](code_mirrors/presentation.py.md) |
| `actual_zoom_sheets` | `function` | `presentation.py` | `Lines 65–82` | `def actual_zoom_sheets(case,folder,images,conditions):` | Actual SVG viewport renders at 1x/4x/16x, never upscaled SVG screenshots. | [presentation.py.md](code_mirrors/presentation.py.md) |
| `metric_table` | `function` | `presentation.py` | `Lines 84–91` | `def metric_table(result,background):` | رمز برمجي موثق. | [presentation.py.md](code_mirrors/presentation.py.md) |
| `build_presentation` | `function` | `presentation.py` | `Lines 93–127` | `def build_presentation():` | Require all nine results complete; refuse to replace presentation evidence. | [presentation.py.md](code_mirrors/presentation.py.md) |
| `add_flat_comparisons` | `function` | `presentation.py` | `Lines 130–144` | `def add_flat_comparisons():` | Add explicit flat-pair negatives without repeating any vector rendering. | [presentation.py.md](code_mirrors/presentation.py.md) |
| `save` | `function` | `research.py` | `Lines 17–19` | `def save(path,data):` | رمز برمجي موثق. | [research.py.md](code_mirrors/research.py.md) |
| `sha` | `function` | `research.py` | `Lines 20–20` | `def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()` | رمز برمجي موثق. | [research.py.md](code_mirrors/research.py.md) |
| `prepare` | `function` | `research.py` | `Lines 21–44` | `def prepare():` | رمز برمجي موثق. | [research.py.md](code_mirrors/research.py.md) |
| `transplant` | `function` | `research.py` | `Lines 45–56` | `def transplant(template,fitted,target):` | رمز برمجي موثق. | [research.py.md](code_mirrors/research.py.md) |
| `old_fit` | `function` | `research.py` | `Lines 57–57` | `def old_fit():return new._historical()` | رمز برمجي موثق. | [research.py.md](code_mirrors/research.py.md) |
| `fixture_baseline` | `function` | `research.py` | `Lines 58–80` | `def fixture_baseline(c,out):` | رمز برمجي موثق. | [research.py.md](code_mirrors/research.py.md) |
| `evaluate_extra` | `function` | `research.py` | `Lines 81–105` | `def evaluate_extra(source,png,maps,reference):` | رمز برمجي موثق. | [research.py.md](code_mirrors/research.py.md) |
| `evaluate_extra.mean` | `nested_function` | `research.py` | `Lines 95–95` | `def mean(mask):return float(err[mask].mean()) if mask.any() else None` | رمز برمجي موثق. | [research.py.md](code_mirrors/research.py.md) |
| `run` | `function` | `research.py` | `Lines 106–148` | `def run(c):` | رمز برمجي موثق. | [research.py.md](code_mirrors/research.py.md) |
| `main` | `function` | `research.py` | `Lines 149–160` | `def main():` | رمز برمجي موثق. | [research.py.md](code_mirrors/research.py.md) |
| `FitterTests` | `class` | `test_fitter.py` | `Lines 15–66` | `class FitterTests(unittest.TestCase):` | رمز برمجي موثق. | [test_fitter.py.md](code_mirrors/test_fitter.py.md) |
| `FitterTests._fixture` | `method` | `test_fitter.py` | `Lines 16–28` | `def _fixture(self, folder, alpha=False):` | رمز برمجي موثق. | [test_fitter.py.md](code_mirrors/test_fitter.py.md) |
| `FitterTests.test_source_over_coefficients_recover_thin_support` | `method` | `test_fitter.py` | `Lines 30–44` | `def test_source_over_coefficients_recover_thin_support(self):` | رمز برمجي موثق. | [test_fitter.py.md](code_mirrors/test_fitter.py.md) |
| `FitterTests.test_joint_fit_preserves_soft_alpha_gradient_and_improves_render` | `method` | `test_fitter.py` | `Lines 46–66` | `def test_joint_fit_preserves_soft_alpha_gradient_and_improves_render(self):` | رمز برمجي موثق. | [test_fitter.py.md](code_mirrors/test_fitter.py.md) |
| `AnalyticFixtureTests` | `class` | `test_fixtures.py` | `Lines 9–54` | `class AnalyticFixtureTests(unittest.TestCase):` | رمز برمجي موثق. | [test_fixtures.py.md](code_mirrors/test_fixtures.py.md) |
| `AnalyticFixtureTests.setUpClass` | `method` | `test_fixtures.py` | `Lines 11–12` | `def setUpClass(cls):` | رمز برمجي موثق. | [test_fixtures.py.md](code_mirrors/test_fixtures.py.md) |
| `AnalyticFixtureTests.test_two_small_frozen_controls_and_reference_reuse` | `method` | `test_fixtures.py` | `Lines 13–21` | `def test_two_small_frozen_controls_and_reference_reuse(self):` | رمز برمجي موثق. | [test_fixtures.py.md](code_mirrors/test_fixtures.py.md) |
| `AnalyticFixtureTests.test_frozen_hashes_and_real_png_decoding` | `method` | `test_fixtures.py` | `Lines 22–28` | `def test_frozen_hashes_and_real_png_decoding(self):` | رمز برمجي موثق. | [test_fixtures.py.md](code_mirrors/test_fixtures.py.md) |
| `AnalyticFixtureTests.test_no_raster_or_dense_grid_and_same_initial_geometry` | `method` | `test_fixtures.py` | `Lines 29–35` | `def test_no_raster_or_dense_grid_and_same_initial_geometry(self):` | رمز برمجي موثق. | [test_fixtures.py.md](code_mirrors/test_fixtures.py.md) |
| `AnalyticFixtureTests.test_gradient_stop_family_and_subpixel_features` | `method` | `test_fixtures.py` | `Lines 36–41` | `def test_gradient_stop_family_and_subpixel_features(self):` | رمز برمجي موثق. | [test_fixtures.py.md](code_mirrors/test_fixtures.py.md) |
| `AnalyticFixtureTests.test_soft_alpha_is_actual_vector_mask_and_visible_in_render` | `method` | `test_fixtures.py` | `Lines 42–46` | `def test_soft_alpha_is_actual_vector_mask_and_visible_in_render(self):` | رمز برمجي موثق. | [test_fixtures.py.md](code_mirrors/test_fixtures.py.md) |
| `AnalyticFixtureTests.test_nonempty_freeze_target_refused` | `method` | `test_fixtures.py` | `Lines 47–54` | `def test_nonempty_freeze_target_refused(self):` | رمز برمجي موثق. | [test_fixtures.py.md](code_mirrors/test_fixtures.py.md) |
| `ResearchTests` | `class` | `test_research.py` | `Lines 6–19` | `class ResearchTests(unittest.TestCase):` | رمز برمجي موثق. | [test_research.py.md](code_mirrors/test_research.py.md) |
| `ResearchTests.test_balanced_background_objective` | `method` | `test_research.py` | `Lines 7–13` | `def test_balanced_background_objective(self):` | رمز برمجي موثق. | [test_research.py.md](code_mirrors/test_research.py.md) |
| `ResearchTests.test_manifest_capacity_and_no_search` | `method` | `test_research.py` | `Lines 14–19` | `def test_manifest_capacity_and_no_search(self):` | رمز برمجي موثق. | [test_research.py.md](code_mirrors/test_research.py.md) |
