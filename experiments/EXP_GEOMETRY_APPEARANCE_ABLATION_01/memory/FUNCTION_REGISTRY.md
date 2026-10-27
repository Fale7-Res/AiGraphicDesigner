# السجل المركزي الموحد للدوال والكلاسات والرموز (`memory/FUNCTION_REGISTRY.md`)

> **مرجعية الكود ومستويات منع التكرار (`Source Authority & 3-Tier Deduplication Policy`):**
> 1. **المستوى الأول — تكرار الاسم المطابق (`Exact-Name Duplication`):** فحص حتمي آلي 100% يمنع وجود دالتين بنفس الاسم عبر الملفات.
> 2. **المستوى الثاني — التشابه الهيكلي للـ AST (`Structural AST Similarity`):** فحص آلي تحذيري يرصد الدوال ذات البنية الهيكلية المتطابقة للمراجعة.
> 3. **المستوى الثالث — التكرار الدلالي (`Semantic Duplication`):** **ليس آلياً بالكامل**؛ يتطلب من كل Agent قراءة عمود الوظيفة (`Purpose`) أدناه قبل كتابة أي دالة جديدة، ويخضع لتدقيق الـ Sub-Agent المراجع (`qa-reviewer-auditor`).

- **إجمالي الملفات البرمجية المفحوصة:** `4`
- **إجمالي الرموز المسجلة بالسطر (شاملة Methods وNested وArrow):** `41`
- **عدد الدوال المتطابقة الاسم غير المسموحة (`Exact-Name Duplicates`):** `0`
- **مرشحات التشابه الهيكلي (`Structural Similarity Candidates`):** `0`

## جدول جميع الدوال والكلاسات والرموز في المشروع (`Master Symbol Index`)

| اسم الرمز (`Symbol`) | النوع (`Kind`) | الملف المالك (`Owner File`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة (`Purpose`) | مرآة الكود التفصيلية (`Code Mirror`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `_matrix` | `function` | `fit_appearance.py` | `Lines 28–54` | `def _matrix(transform):` | Parse affine SVG transforms; reject unknown transforms explicitly. | [fit_appearance.py.md](code_mirrors/fit_appearance.py.md) |
| `_paths` | `function` | `fit_appearance.py` | `Lines 57–67` | `def _paths(root):` | رمز برمجي موثق. | [fit_appearance.py.md](code_mirrors/fit_appearance.py.md) |
| `_paths.walk` | `nested_function` | `fit_appearance.py` | `Lines 59–65` | `def walk(node, parent):` | رمز برمجي موثق. | [fit_appearance.py.md](code_mirrors/fit_appearance.py.md) |
| `_ownership` | `function` | `fit_appearance.py` | `Lines 70–106` | `def _ownership(root, width, height, directory, timeout):` | Render unique pseudo-random RGB IDs; reject seams with local consensus. | [fit_appearance.py.md](code_mirrors/fit_appearance.py.md) |
| `_basis` | `function` | `fit_appearance.py` | `Lines 109–116` | `def _basis(t, stops):` | رمز برمجي موثق. | [fit_appearance.py.md](code_mirrors/fit_appearance.py.md) |
| `_predict` | `function` | `fit_appearance.py` | `Lines 119–127` | `def _predict(model, xy):` | رمز برمجي موثق. | [fit_appearance.py.md](code_mirrors/fit_appearance.py.md) |
| `_fit_region` | `function` | `fit_appearance.py` | `Lines 130–220` | `def _fit_region(xy, rgb, train, selection, test, deadline, weights):` | رمز برمجي موثق. | [fit_appearance.py.md](code_mirrors/fit_appearance.py.md) |
| `_fit_region.fit_model` | `nested_function` | `fit_appearance.py` | `Lines 141–166` | `def fit_model(kind, params, stops):` | رمز برمجي موثق. | [fit_appearance.py.md](code_mirrors/fit_appearance.py.md) |
| `_paint` | `function` | `fit_appearance.py` | `Lines 223–246` | `def _paint(root, models):` | رمز برمجي موثق. | [fit_appearance.py.md](code_mirrors/fit_appearance.py.md) |
| `fit_svg` | `function` | `fit_appearance.py` | `Lines 249–338` | `def fit_svg(source_png, baseline_svg, flat_svg, gradient_svg, diagnostics_path, deadline_seconds=600):` | Write C/D SVGs with identical geometry; return region fit diagnostics. | [fit_appearance.py.md](code_mirrors/fit_appearance.py.md) |
| `digest` | `function` | `run_experiment.py` | `Lines 22–23` | `def digest(path):` | رمز برمجي موثق. | [run_experiment.py.md](code_mirrors/run_experiment.py.md) |
| `save_json` | `function` | `run_experiment.py` | `Lines 25–27` | `def save_json(path,data):` | رمز برمجي موثق. | [run_experiment.py.md](code_mirrors/run_experiment.py.md) |
| `geometry_signature` | `function` | `run_experiment.py` | `Lines 29–43` | `def geometry_signature(path):` | All non-paint structure including ordering and masks; gradient definitions omitted. | [run_experiment.py.md](code_mirrors/run_experiment.py.md) |
| `geometry_signature.visit` | `nested_function` | `run_experiment.py` | `Lines 32–37` | `def visit(node):` | رمز برمجي موثق. | [run_experiment.py.md](code_mirrors/run_experiment.py.md) |
| `geometry_signature.prune` | `nested_function` | `run_experiment.py` | `Lines 39–42` | `def prune(v):` | رمز برمجي موثق. | [run_experiment.py.md](code_mirrors/run_experiment.py.md) |
| `geometry_diagnostics` | `function` | `run_experiment.py` | `Lines 45–78` | `def geometry_diagnostics(path):` | Exact Bezier bounds and segment pairing for VTracer translate-only path coordinates. | [run_experiment.py.md](code_mirrors/run_experiment.py.md) |
| `fixture_sources` | `function` | `run_experiment.py` | `Lines 80–91` | `def fixture_sources():` | Two independent analytic vector controls, not included in real-image generalization claims. | [run_experiment.py.md](code_mirrors/run_experiment.py.md) |
| `frozen_cases` | `function` | `run_experiment.py` | `Lines 93–109` | `def frozen_cases():` | رمز برمجي موثق. | [run_experiment.py.md](code_mirrors/run_experiment.py.md) |
| `appearance_metrics` | `function` | `run_experiment.py` | `Lines 111–115` | `def appearance_metrics(source,prediction):` | رمز برمجي موثق. | [run_experiment.py.md](code_mirrors/run_experiment.py.md) |
| `evaluate_condition` | `function` | `run_experiment.py` | `Lines 117–128` | `def evaluate_condition(source,svg,folder):` | Evaluate actual native SVG renders, RGBA and independent full-image spatial errors. | [run_experiment.py.md](code_mirrors/run_experiment.py.md) |
| `crop_svg` | `function` | `run_experiment.py` | `Lines 130–134` | `def crop_svg(svg,target,box,scale):` | Change only viewport, render vector geometry directly at requested zoom; no bitmap enlargement. | [run_experiment.py.md](code_mirrors/run_experiment.py.md) |
| `case_visuals` | `function` | `run_experiment.py` | `Lines 136–164` | `def case_visuals(case,out):` | رمز برمجي موثق. | [run_experiment.py.md](code_mirrors/run_experiment.py.md) |
| `known_control_geometry` | `function` | `run_experiment.py` | `Lines 166–189` | `def known_control_geometry(case,out):` | Compare known-control foreground silhouette and holes independently of fitted appearance. | [run_experiment.py.md](code_mirrors/run_experiment.py.md) |
| `known_control_geometry.holes` | `nested_function` | `run_experiment.py` | `Lines 182–184` | `def holes(mask):` | رمز برمجي موثق. | [run_experiment.py.md](code_mirrors/run_experiment.py.md) |
| `run_case` | `function` | `run_experiment.py` | `Lines 191–227` | `def run_case(case):` | رمز برمجي موثق. | [run_experiment.py.md](code_mirrors/run_experiment.py.md) |
| `build_dashboard` | `function` | `run_experiment.py` | `Lines 229–243` | `def build_dashboard():` | رمز برمجي موثق. | [run_experiment.py.md](code_mirrors/run_experiment.py.md) |
| `geometry_tree` | `function` | `test_artifacts.py` | `Lines 10–18` | `def geometry_tree(node):` | رمز برمجي موثق. | [test_artifacts.py.md](code_mirrors/test_artifacts.py.md) |
| `SavedAblationTests` | `class` | `test_artifacts.py` | `Lines 20–69` | `class SavedAblationTests(unittest.TestCase):` | رمز برمجي موثق. | [test_artifacts.py.md](code_mirrors/test_artifacts.py.md) |
| `SavedAblationTests.setUpClass` | `method` | `test_artifacts.py` | `Lines 22–24` | `def setUpClass(cls):` | رمز برمجي موثق. | [test_artifacts.py.md](code_mirrors/test_artifacts.py.md) |
| `SavedAblationTests.test_complete_frozen_suite_and_artifact_hashes` | `method` | `test_artifacts.py` | `Lines 25–31` | `def test_complete_frozen_suite_and_artifact_hashes(self):` | رمز برمجي موثق. | [test_artifacts.py.md](code_mirrors/test_artifacts.py.md) |
| `SavedAblationTests.test_strict_b_c_d_geometry_and_alpha_mask_identity` | `method` | `test_artifacts.py` | `Lines 32–36` | `def test_strict_b_c_d_geometry_and_alpha_mask_identity(self):` | رمز برمجي موثق. | [test_artifacts.py.md](code_mirrors/test_artifacts.py.md) |
| `SavedAblationTests.test_svg_safety_gradient_capacity_and_png_integrity` | `method` | `test_artifacts.py` | `Lines 37–52` | `def test_svg_safety_gradient_capacity_and_png_integrity(self):` | رمز برمجي موثق. | [test_artifacts.py.md](code_mirrors/test_artifacts.py.md) |
| `SavedAblationTests.test_saved_actual_white_mse_and_alpha` | `method` | `test_artifacts.py` | `Lines 53–62` | `def test_saved_actual_white_mse_and_alpha(self):` | رمز برمجي موثق. | [test_artifacts.py.md](code_mirrors/test_artifacts.py.md) |
| `SavedAblationTests.test_zoom_evidence_and_known_control_geometry` | `method` | `test_artifacts.py` | `Lines 63–69` | `def test_zoom_evidence_and_known_control_geometry(self):` | رمز برمجي موثق. | [test_artifacts.py.md](code_mirrors/test_artifacts.py.md) |
| `AppearanceTests` | `class` | `test_fit_appearance.py` | `Lines 18–81` | `class AppearanceTests(unittest.TestCase):` | رمز برمجي موثق. | [test_fit_appearance.py.md](code_mirrors/test_fit_appearance.py.md) |
| `AppearanceTests.test_alpha_squared_weighted_flat` | `method` | `test_fit_appearance.py` | `Lines 19–25` | `def test_alpha_squared_weighted_flat(self):` | رمز برمجي موثق. | [test_fit_appearance.py.md](code_mirrors/test_fit_appearance.py.md) |
| `AppearanceTests.test_basis_partition_and_clamp` | `method` | `test_fit_appearance.py` | `Lines 27–32` | `def test_basis_partition_and_clamp(self):` | رمز برمجي موثق. | [test_fit_appearance.py.md](code_mirrors/test_fit_appearance.py.md) |
| `AppearanceTests.test_affine_transform_order` | `method` | `test_fit_appearance.py` | `Lines 34–38` | `def test_affine_transform_order(self):` | رمز برمجي موثق. | [test_fit_appearance.py.md](code_mirrors/test_fit_appearance.py.md) |
| `AppearanceTests.test_linear_render_geometry_and_translation` | `method` | `test_fit_appearance.py` | `Lines 41–42` | `def test_linear_render_geometry_and_translation(self):` | رمز برمجي موثق. | [test_fit_appearance.py.md](code_mirrors/test_fit_appearance.py.md) |
| `AppearanceTests.test_radial_render_and_holdout` | `method` | `test_fit_appearance.py` | `Lines 45–46` | `def test_radial_render_and_holdout(self):` | رمز برمجي موثق. | [test_fit_appearance.py.md](code_mirrors/test_fit_appearance.py.md) |
| `AppearanceTests._control` | `method` | `test_fit_appearance.py` | `Lines 48–81` | `def _control(self, kind):` | رمز برمجي موثق. | [test_fit_appearance.py.md](code_mirrors/test_fit_appearance.py.md) |
