# مرآة الكود التفصيلية للإصدار: `version-02/tests/test_version.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED VERSION MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `versions/version-02/tests/test_version.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)** لهذا الإصدار. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py --version version-02`.

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tests/test_version.py`
- **الإصدار المعماري (`Architecture Version`):** `version-02`
- **إجمالي عدد الأسطر (`Total Lines`):** `68` (`Lines 1–68`)
- **بصمة الملف (`SHA-256`):** `e6a1074951eb01afb87772e6dcb7e2c1031ca9db7a4088fc7a64b3c4fe1ec435`
- **الوصف:** موديول برمجي تنفيذي ضمن معمارية الإصدار `version-02`.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **حوكمة الإصدار الأب (`Parent Version`)** | `version-02` | يتبع مواصفة معمارية هذا الإصدار | مراجعة تكامل الإصدار عند التعديل. |
| **الحوكمة المركزية (`Global Governance`)** | `AGENTS.md` | يخضع للدستور وقواعد منع التكرار المشتركة | التحقق الحوكمي الإلزامي. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `TestVersion02Pipeline` | `class` | `Lines 16–63` | `class TestVersion02Pipeline(unittest.TestCase):` | Test suite validating Version 02 Scene Graph and clean SVG output. |
| `TestVersion02Pipeline.test_vector_point_distance` | `method` | `Lines 19–23` | `def test_vector_point_distance(self) -> None:` | Verify vector point distance metric. |
| `TestVersion02Pipeline.test_optimized_bezier_segment_handles` | `method` | `Lines 25–33` | `def test_optimized_bezier_segment_handles(self) -> None:` | Verify optimized Bézier segment handles formatting. |
| `TestVersion02Pipeline.test_fit_smooth_curve_node_budget` | `method` | `Lines 35–39` | `def test_fit_smooth_curve_node_budget(self) -> None:` | Verify node count respects budget. |
| `TestVersion02Pipeline.test_pipeline_semantic_group_with_clippath` | `method` | `Lines 41–63` | `def test_pipeline_semantic_group_with_clippath(self) -> None:` | Verify semantic group SVG generation contains <clipPath> and base/shadow elements. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `TestVersion02Pipeline` — `Lines 16–63`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `63` (`Lines 16–63`)
- **الوظيفة:** Test suite validating Version 02 Scene Graph and clean SVG output.
- **الكود الفعلي (`Lines 16–63`):**
```python
class TestVersion02Pipeline(unittest.TestCase):
    """Test suite validating Version 02 Scene Graph and clean SVG output."""

    def test_vector_point_distance(self) -> None:
        """Verify vector point distance metric."""
        p1 = VectorPoint(10.0, 20.0)
        p2 = VectorPoint(13.0, 24.0)
        self.assertAlmostEqual(p1.distance_to(p2), 5.0)

    def test_optimized_bezier_segment_handles(self) -> None:
        """Verify optimized Bézier segment handles formatting."""
        p0 = VectorPoint(0.0, 0.0)
        h_out = VectorPoint(5.0, 10.0)
        h_in = VectorPoint(15.0, 10.0)
        p3 = VectorPoint(20.0, 0.0)
        seg = OptimizedBezierSegment(anchor_start=p0, handle_out=h_out, handle_in=h_in, anchor_end=p3)
        cmd = seg.to_svg_cubic_command()
        self.assertIn("C 5.00 10.00, 15.00 10.00, 20.00 0.00", cmd)

    def test_fit_smooth_curve_node_budget(self) -> None:
        """Verify node count respects budget."""
        points = [VectorPoint(float(i), float(i % 10)) for i in range(100)]
        segs = fit_smooth_curve(points, max_nodes=20)
        self.assertLessEqual(len(segs), 25)

    def test_pipeline_semantic_group_with_clippath(self) -> None:
        """Verify semantic group SVG generation contains <clipPath> and base/shadow elements."""
        pipeline = HierarchicalSceneGraphPipeline(max_nodes_budget=36)
        base_pts = [(0.0, 0.0), (100.0, 0.0), (100.0, 100.0), (0.0, 100.0)]
        shadow_pts = [(50.0, 50.0), (100.0, 50.0), (100.0, 100.0), (50.0, 100.0)]
        group = pipeline.create_semantic_group(
            group_id="fries_pack",
            label="fries",
            base_points=base_pts,
            base_color_hex="#FFAA00",
            shadow_points=shadow_pts,
            shadow_color_hex="#994400",
            shadow_opacity=0.4,
        )
        svg_group = group.to_svg_group()
        self.assertIn('<g id="fries_pack"', svg_group)
        self.assertIn('<clipPath id="clip_fries_pack">', svg_group)
        self.assertIn('clip-path="url(#clip_fries_pack)"', svg_group)
        self.assertIn('opacity="0.40"', svg_group)

        full_svg = pipeline.export_scene_graph_svg([group])
        self.assertIn("<svg", full_svg)
        self.assertIn("version-02", full_svg)
```

### `TestVersion02Pipeline.test_vector_point_distance` — `Lines 19–23`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `19` إلى السطر `23` (`Lines 19–23`)
- **الوظيفة:** Verify vector point distance metric.
- **الكود الفعلي (`Lines 19–23`):**
```python
    def test_vector_point_distance(self) -> None:
        """Verify vector point distance metric."""
        p1 = VectorPoint(10.0, 20.0)
        p2 = VectorPoint(13.0, 24.0)
        self.assertAlmostEqual(p1.distance_to(p2), 5.0)
```

### `TestVersion02Pipeline.test_optimized_bezier_segment_handles` — `Lines 25–33`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `25` إلى السطر `33` (`Lines 25–33`)
- **الوظيفة:** Verify optimized Bézier segment handles formatting.
- **الكود الفعلي (`Lines 25–33`):**
```python
    def test_optimized_bezier_segment_handles(self) -> None:
        """Verify optimized Bézier segment handles formatting."""
        p0 = VectorPoint(0.0, 0.0)
        h_out = VectorPoint(5.0, 10.0)
        h_in = VectorPoint(15.0, 10.0)
        p3 = VectorPoint(20.0, 0.0)
        seg = OptimizedBezierSegment(anchor_start=p0, handle_out=h_out, handle_in=h_in, anchor_end=p3)
        cmd = seg.to_svg_cubic_command()
        self.assertIn("C 5.00 10.00, 15.00 10.00, 20.00 0.00", cmd)
```

### `TestVersion02Pipeline.test_fit_smooth_curve_node_budget` — `Lines 35–39`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `35` إلى السطر `39` (`Lines 35–39`)
- **الوظيفة:** Verify node count respects budget.
- **الكود الفعلي (`Lines 35–39`):**
```python
    def test_fit_smooth_curve_node_budget(self) -> None:
        """Verify node count respects budget."""
        points = [VectorPoint(float(i), float(i % 10)) for i in range(100)]
        segs = fit_smooth_curve(points, max_nodes=20)
        self.assertLessEqual(len(segs), 25)
```

### `TestVersion02Pipeline.test_pipeline_semantic_group_with_clippath` — `Lines 41–63`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `41` إلى السطر `63` (`Lines 41–63`)
- **الوظيفة:** Verify semantic group SVG generation contains <clipPath> and base/shadow elements.
- **الكود الفعلي (`Lines 41–63`):**
```python
    def test_pipeline_semantic_group_with_clippath(self) -> None:
        """Verify semantic group SVG generation contains <clipPath> and base/shadow elements."""
        pipeline = HierarchicalSceneGraphPipeline(max_nodes_budget=36)
        base_pts = [(0.0, 0.0), (100.0, 0.0), (100.0, 100.0), (0.0, 100.0)]
        shadow_pts = [(50.0, 50.0), (100.0, 50.0), (100.0, 100.0), (50.0, 100.0)]
        group = pipeline.create_semantic_group(
            group_id="fries_pack",
            label="fries",
            base_points=base_pts,
            base_color_hex="#FFAA00",
            shadow_points=shadow_pts,
            shadow_color_hex="#994400",
            shadow_opacity=0.4,
        )
        svg_group = group.to_svg_group()
        self.assertIn('<g id="fries_pack"', svg_group)
        self.assertIn('<clipPath id="clip_fries_pack">', svg_group)
        self.assertIn('clip-path="url(#clip_fries_pack)"', svg_group)
        self.assertIn('opacity="0.40"', svg_group)

        full_svg = pipeline.export_scene_graph_svg([group])
        self.assertIn("<svg", full_svg)
        self.assertIn("version-02", full_svg)
```
