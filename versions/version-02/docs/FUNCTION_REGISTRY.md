# السجل الموحد للدوال والكلاسات للإصدار `version-02` (`FUNCTION_REGISTRY.md`)

> **مرجعية الكود ومستويات منع التكرار الخاصة بالإصدار (`Version Source Authority & Deduplication Policy`):**
> 1. **المستوى الأول — تكرار الاسم المطابق (`Exact-Name Duplication`):** فحص حتمي آلي يمنع وجود دالتين بنفس الاسم عبر ملفات الإصدار `version-02`.
> 2. **المستوى الثاني — التشابه الهيكلي للـ AST (`Structural AST Similarity`):** فحص آلي تحذيري يرصد الدوال ذات البنية المتطابقة داخل الإصدار.
> 3. **المستوى الثالث — التكرار الدلالي (`Semantic Duplication`):** تدقيق مهندس الإصدار والمراجع المستقل لمنع إعادة اختراع الوظائف المتاحة.

- **معرف الإصدار المعماري (`Version ID`):** `version-02`
- **إجمالي الملفات البرمجية المفحوصة في الإصدار:** `3`
- **إجمالي الرموز المسجلة بالسطر:** `19`
- **عدد الدوال المتطابقة الاسم غير المسموحة:** `0`
- **مرشحات التشابه الهيكلي:** `0`

## جدول جميع الدوال والكلاسات والرموز في الإصدار (`Version Symbol Index`)

| اسم الرمز (`Symbol`) | النوع (`Kind`) | الملف المالك (`Owner File`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة (`Purpose`) | مرآة الكود التفصيلية (`Code Mirror`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `VectorPoint` | `class` | `src/geometry/bezier.py` | `Lines 12–19` | `class VectorPoint:` | Represents a 2D position vector in canvas coordinate space. | [src/geometry/bezier.py.md](CODE_MIRRORS/src/geometry/bezier.py.md) |
| `VectorPoint.distance_to` | `method` | `src/geometry/bezier.py` | `Lines 17–19` | `def distance_to(self, other: "VectorPoint") -> float:` | Compute Euclidean distance to another point. | [src/geometry/bezier.py.md](CODE_MIRRORS/src/geometry/bezier.py.md) |
| `OptimizedBezierSegment` | `class` | `src/geometry/bezier.py` | `Lines 23–45` | `class OptimizedBezierSegment:` | Cubic Bézier segment with explicit in/out pen tool handles. | [src/geometry/bezier.py.md](CODE_MIRRORS/src/geometry/bezier.py.md) |
| `OptimizedBezierSegment.evaluate_at` | `method` | `src/geometry/bezier.py` | `Lines 30–41` | `def evaluate_at(self, t: float) -> VectorPoint:` | Evaluate the cubic curve at parameter t in [0.0, 1.0]. | [src/geometry/bezier.py.md](CODE_MIRRORS/src/geometry/bezier.py.md) |
| `OptimizedBezierSegment.to_svg_cubic_command` | `method` | `src/geometry/bezier.py` | `Lines 43–45` | `def to_svg_cubic_command(self) -> str:` | Format as standard SVG C command. | [src/geometry/bezier.py.md](CODE_MIRRORS/src/geometry/bezier.py.md) |
| `fit_smooth_curve` | `function` | `src/geometry/bezier.py` | `Lines 48–71` | `def fit_smooth_curve(points: list[VectorPoint], max_nodes: int = 36) -> list[OptimizedBezierSegment]:` | Fit a series of points into smooth cubic Bézier segments enforcing maximum node budget. | [src/geometry/bezier.py.md](CODE_MIRRORS/src/geometry/bezier.py.md) |
| `SemanticPathElement` | `class` | `src/pipeline.py` | `Lines 16–32` | `class SemanticPathElement:` | Represents a discrete path component (base, shadow, highlight) in a group. | [src/pipeline.py.md](CODE_MIRRORS/src/pipeline.py.md) |
| `SemanticPathElement.render_d_attribute` | `method` | `src/pipeline.py` | `Lines 23–32` | `def render_d_attribute(self) -> str:` | Render d attribute path string. | [src/pipeline.py.md](CODE_MIRRORS/src/pipeline.py.md) |
| `SemanticObjectGroup` | `class` | `src/pipeline.py` | `Lines 36–72` | `class SemanticObjectGroup:` | Represents a grouped design object containing base, shadow, and clipPath. | [src/pipeline.py.md](CODE_MIRRORS/src/pipeline.py.md) |
| `SemanticObjectGroup.to_svg_group` | `method` | `src/pipeline.py` | `Lines 45–72` | `def to_svg_group(self) -> str:` | Render this semantic object as an SVG <g> with non-destructive clipping. | [src/pipeline.py.md](CODE_MIRRORS/src/pipeline.py.md) |
| `HierarchicalSceneGraphPipeline` | `class` | `src/pipeline.py` | `Lines 75–124` | `class HierarchicalSceneGraphPipeline:` | Version 02 hierarchical scene graph pipeline. | [src/pipeline.py.md](CODE_MIRRORS/src/pipeline.py.md) |
| `HierarchicalSceneGraphPipeline.__init__` | `method` | `src/pipeline.py` | `Lines 78–79` | `def __init__(self, max_nodes_budget: int = 36) -> None:` | رمز برمجي موثق للإصدار. | [src/pipeline.py.md](CODE_MIRRORS/src/pipeline.py.md) |
| `HierarchicalSceneGraphPipeline.create_semantic_group` | `method` | `src/pipeline.py` | `Lines 81–113` | `def create_semantic_group(` | Create an optimized semantic object group with base and clipped shadow. | [src/pipeline.py.md](CODE_MIRRORS/src/pipeline.py.md) |
| `HierarchicalSceneGraphPipeline.export_scene_graph_svg` | `method` | `src/pipeline.py` | `Lines 115–124` | `def export_scene_graph_svg(self, groups: list[SemanticObjectGroup], width: int = 2048, height: int = 2048) -> str:` | Export all semantic groups into a high-fidelity Clean SVG document. | [src/pipeline.py.md](CODE_MIRRORS/src/pipeline.py.md) |
| `TestVersion02Pipeline` | `class` | `tests/test_version.py` | `Lines 16–63` | `class TestVersion02Pipeline(unittest.TestCase):` | Test suite validating Version 02 Scene Graph and clean SVG output. | [tests/test_version.py.md](CODE_MIRRORS/tests/test_version.py.md) |
| `TestVersion02Pipeline.test_vector_point_distance` | `method` | `tests/test_version.py` | `Lines 19–23` | `def test_vector_point_distance(self) -> None:` | Verify vector point distance metric. | [tests/test_version.py.md](CODE_MIRRORS/tests/test_version.py.md) |
| `TestVersion02Pipeline.test_optimized_bezier_segment_handles` | `method` | `tests/test_version.py` | `Lines 25–33` | `def test_optimized_bezier_segment_handles(self) -> None:` | Verify optimized Bézier segment handles formatting. | [tests/test_version.py.md](CODE_MIRRORS/tests/test_version.py.md) |
| `TestVersion02Pipeline.test_fit_smooth_curve_node_budget` | `method` | `tests/test_version.py` | `Lines 35–39` | `def test_fit_smooth_curve_node_budget(self) -> None:` | Verify node count respects budget. | [tests/test_version.py.md](CODE_MIRRORS/tests/test_version.py.md) |
| `TestVersion02Pipeline.test_pipeline_semantic_group_with_clippath` | `method` | `tests/test_version.py` | `Lines 41–63` | `def test_pipeline_semantic_group_with_clippath(self) -> None:` | Verify semantic group SVG generation contains <clipPath> and base/shadow elements. | [tests/test_version.py.md](CODE_MIRRORS/tests/test_version.py.md) |
