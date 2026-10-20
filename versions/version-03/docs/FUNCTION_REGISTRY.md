# السجل الموحد للدوال والكلاسات للإصدار `version-03` (`FUNCTION_REGISTRY.md`)

> **مرجعية الكود ومستويات منع التكرار الخاصة بالإصدار (`Version Source Authority & Deduplication Policy`):**
> 1. **المستوى الأول — تكرار الاسم المطابق (`Exact-Name Duplication`):** فحص حتمي آلي يمنع وجود دالتين بنفس الاسم عبر ملفات الإصدار `version-03`.
> 2. **المستوى الثاني — التشابه الهيكلي للـ AST (`Structural AST Similarity`):** فحص آلي تحذيري يرصد الدوال ذات البنية المتطابقة داخل الإصدار.
> 3. **المستوى الثالث — التكرار الدلالي (`Semantic Duplication`):** تدقيق مهندس الإصدار والمراجع المستقل لمنع إعادة اختراع الوظائف المتاحة.

- **معرف الإصدار المعماري (`Version ID`):** `version-03`
- **إجمالي الملفات البرمجية المفحوصة في الإصدار:** `3`
- **إجمالي الرموز المسجلة بالسطر:** `17`
- **عدد الدوال المتطابقة الاسم غير المسموحة:** `0`
- **مرشحات التشابه الهيكلي:** `0`

## جدول جميع الدوال والكلاسات والرموز في الإصدار (`Version Symbol Index`)

| اسم الرمز (`Symbol`) | النوع (`Kind`) | الملف المالك (`Owner File`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة (`Purpose`) | مرآة الكود التفصيلية (`Code Mirror`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TypographicPoint` | `class` | `src/geometry/bezier.py` | `Lines 12–20` | `class TypographicPoint:` | Represents a contour point on a glyph or typographic path. | [src/geometry/bezier.py.md](CODE_MIRRORS/src/geometry/bezier.py.md) |
| `TypographicPoint.distance_to` | `method` | `src/geometry/bezier.py` | `Lines 18–20` | `def distance_to(self, other: "TypographicPoint") -> float:` | Compute Euclidean distance to another point. | [src/geometry/bezier.py.md](CODE_MIRRORS/src/geometry/bezier.py.md) |
| `CalligraphicBezierSegment` | `class` | `src/geometry/bezier.py` | `Lines 24–33` | `class CalligraphicBezierSegment:` | Cubic Bézier segment optimized for calligraphic curvature. | [src/geometry/bezier.py.md](CODE_MIRRORS/src/geometry/bezier.py.md) |
| `CalligraphicBezierSegment.to_svg_cubic_path` | `method` | `src/geometry/bezier.py` | `Lines 31–33` | `def to_svg_cubic_path(self) -> str:` | Format as standard SVG C command. | [src/geometry/bezier.py.md](CODE_MIRRORS/src/geometry/bezier.py.md) |
| `fit_typographic_bezier` | `function` | `src/geometry/bezier.py` | `Lines 36–58` | `def fit_typographic_bezier(points: list[TypographicPoint], error_tolerance_px: float = 1.0) -> list[CalligraphicBezierSegment]:` | Fit typographic contour points into cubic Bézier segments preserving corner sharpness. | [src/geometry/bezier.py.md](CODE_MIRRORS/src/geometry/bezier.py.md) |
| `DualPathTypographyLayer` | `class` | `src/pipeline.py` | `Lines 17–46` | `class DualPathTypographyLayer:` | Represents a typographic layer with dual-path visual and editable representations. | [src/pipeline.py.md](CODE_MIRRORS/src/pipeline.py.md) |
| `DualPathTypographyLayer.render_exact_outline_svg` | `method` | `src/pipeline.py` | `Lines 27–36` | `def render_exact_outline_svg(self) -> str:` | Render Path 1: exact Bézier outlines. | [src/pipeline.py.md](CODE_MIRRORS/src/pipeline.py.md) |
| `DualPathTypographyLayer.render_editable_text_svg` | `method` | `src/pipeline.py` | `Lines 38–46` | `def render_editable_text_svg(self, x: float = 100.0, y: float = 100.0) -> str:` | Render Path 2: editable text SVG element. | [src/pipeline.py.md](CODE_MIRRORS/src/pipeline.py.md) |
| `DualPathTypographyPipeline` | `class` | `src/pipeline.py` | `Lines 49–90` | `class DualPathTypographyPipeline:` | Version 03 pipeline combining latent attention decomposition and dual-path typography. | [src/pipeline.py.md](CODE_MIRRORS/src/pipeline.py.md) |
| `DualPathTypographyPipeline.__init__` | `method` | `src/pipeline.py` | `Lines 52–53` | `def __init__(self, default_font_fallback: str = "Cairo") -> None:` | رمز برمجي موثق للإصدار. | [src/pipeline.py.md](CODE_MIRRORS/src/pipeline.py.md) |
| `DualPathTypographyPipeline.create_typography_layer` | `method` | `src/pipeline.py` | `Lines 55–74` | `def create_typography_layer(` | Construct a dual-path typography layer. | [src/pipeline.py.md](CODE_MIRRORS/src/pipeline.py.md) |
| `DualPathTypographyPipeline.export_dual_path_svg` | `method` | `src/pipeline.py` | `Lines 76–90` | `def export_dual_path_svg(self, layers: list[DualPathTypographyLayer], width: int = 2048, height: int = 2048) -> str:` | Compile SVG document containing both vector outline and editable text layers. | [src/pipeline.py.md](CODE_MIRRORS/src/pipeline.py.md) |
| `TestVersion03Pipeline` | `class` | `tests/test_version.py` | `Lines 16–64` | `class TestVersion03Pipeline(unittest.TestCase):` | Test suite validating Version 03 typography and dual-path output. | [tests/test_version.py.md](CODE_MIRRORS/tests/test_version.py.md) |
| `TestVersion03Pipeline.test_typographic_point_corner_flag` | `method` | `tests/test_version.py` | `Lines 19–24` | `def test_typographic_point_corner_flag(self) -> None:` | Verify typographic point corner flag preservation. | [tests/test_version.py.md](CODE_MIRRORS/tests/test_version.py.md) |
| `TestVersion03Pipeline.test_calligraphic_bezier_segment_output` | `method` | `tests/test_version.py` | `Lines 26–33` | `def test_calligraphic_bezier_segment_output(self) -> None:` | Verify calligraphic segment SVG output. | [tests/test_version.py.md](CODE_MIRRORS/tests/test_version.py.md) |
| `TestVersion03Pipeline.test_fit_typographic_bezier_with_corners` | `method` | `tests/test_version.py` | `Lines 35–45` | `def test_fit_typographic_bezier_with_corners(self) -> None:` | Verify corner breakpoints split segments cleanly. | [tests/test_version.py.md](CODE_MIRRORS/tests/test_version.py.md) |
| `TestVersion03Pipeline.test_dual_path_pipeline_export` | `method` | `tests/test_version.py` | `Lines 47–64` | `def test_dual_path_pipeline_export(self) -> None:` | Verify dual path SVG contains both outline and editable text nodes. | [tests/test_version.py.md](CODE_MIRRORS/tests/test_version.py.md) |
