# مرآة الكود التفصيلية للإصدار: `version-01/tests/test_version.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED VERSION MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `versions/version-01/tests/test_version.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)** لهذا الإصدار. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py --version version-01`.

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tests/test_version.py`
- **الإصدار المعماري (`Architecture Version`):** `version-01`
- **إجمالي عدد الأسطر (`Total Lines`):** `87` (`Lines 1–87`)
- **بصمة الملف (`SHA-256`):** `e3a2ec0602b1f5450001b5777a45940ec4195bb4dfa50f7907aa1598d81c9bf2`
- **الوصف:** موديول برمجي تنفيذي ضمن معمارية الإصدار `version-01`.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **حوكمة الإصدار الأب (`Parent Version`)** | `version-01` | يتبع مواصفة معمارية هذا الإصدار | مراجعة تكامل الإصدار عند التعديل. |
| **الحوكمة المركزية (`Global Governance`)** | `AGENTS.md` | يخضع للدستور وقواعد منع التكرار المشتركة | التحقق الحوكمي الإلزامي. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `TestVersion01Pipeline` | `class` | `Lines 16–82` | `class TestVersion01Pipeline(unittest.TestCase):` | Test suite validating Version 01 geometry and pipeline functionality. |
| `TestVersion01Pipeline.test_point2d_euclidean_distance` | `method` | `Lines 19–23` | `def test_point2d_euclidean_distance(self) -> None:` | Verify 2D distance calculation. |
| `TestVersion01Pipeline.test_bezier_segment_evaluation` | `method` | `Lines 25–36` | `def test_bezier_segment_evaluation(self) -> None:` | Verify cubic curve evaluation at t=0, t=0.5, t=1.0. |
| `TestVersion01Pipeline.test_fit_schneider_bezier_two_points` | `method` | `Lines 38–44` | `def test_fit_schneider_bezier_two_points(self) -> None:` | Fitting two points returns exactly one cubic segment. |
| `TestVersion01Pipeline.test_pipeline_compile_clean_svg` | `method` | `Lines 46–55` | `def test_pipeline_compile_clean_svg(self) -> None:` | Verify pipeline produces valid SVG string with descriptor. |
| `TestVersion01Pipeline.test_pipeline_default_gradient_disabled` | `method` | `Lines 57–61` | `def test_pipeline_default_gradient_disabled(self) -> None:` | Verify pipeline defaults to enable_gradients=False to protect baseline fidelity. |
| `TestVersion01Pipeline.test_bezier_segment_and_node_accounting` | `method` | `Lines 63–82` | `def test_bezier_segment_and_node_accounting(self) -> None:` | Verify distinction between cubic segments (C), on-curve anchor nodes, and control handles. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `TestVersion01Pipeline` — `Lines 16–82`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `82` (`Lines 16–82`)
- **الوظيفة:** Test suite validating Version 01 geometry and pipeline functionality.
- **الكود الفعلي (`Lines 16–82`):**
```python
class TestVersion01Pipeline(unittest.TestCase):
    """Test suite validating Version 01 geometry and pipeline functionality."""

    def test_point2d_euclidean_distance(self) -> None:
        """Verify 2D distance calculation."""
        p1 = Point2D(0.0, 0.0)
        p2 = Point2D(3.0, 4.0)
        self.assertAlmostEqual(p1.distance_to(p2), 5.0)

    def test_bezier_segment_evaluation(self) -> None:
        """Verify cubic curve evaluation at t=0, t=0.5, t=1.0."""
        p0 = Point2D(0.0, 0.0)
        p1 = Point2D(0.0, 10.0)
        p2 = Point2D(10.0, 10.0)
        p3 = Point2D(10.0, 0.0)
        seg = BezierSegment(p0, p1, p2, p3)
        self.assertEqual(seg.evaluate(0.0), p0)
        self.assertEqual(seg.evaluate(1.0), p3)
        mid = seg.evaluate(0.5)
        self.assertAlmostEqual(mid.x, 5.0)
        self.assertAlmostEqual(mid.y, 7.5)

    def test_fit_schneider_bezier_two_points(self) -> None:
        """Fitting two points returns exactly one cubic segment."""
        pts = [Point2D(0.0, 0.0), Point2D(100.0, 100.0)]
        segments = fit_schneider_bezier(pts)
        self.assertEqual(len(segments), 1)
        self.assertEqual(segments[0].p0, pts[0])
        self.assertEqual(segments[0].p3, pts[1])

    def test_pipeline_compile_clean_svg(self) -> None:
        """Verify pipeline produces valid SVG string with descriptor."""
        pipeline = SequentialPipeline(error_tolerance_px=1.5, max_nodes_per_path=36)
        contour = [(10.0, 10.0), (50.0, 10.0), (50.0, 50.0), (10.0, 50.0)]
        layer = pipeline.process_polygon_contour(contour, layer_id="layer_01", label="shield_base", fill_hex="#FF5733")
        svg = pipeline.compile_clean_svg([layer])
        self.assertIn("<svg", svg)
        self.assertIn("version-01", svg)
        self.assertIn('id="layer_01"', svg)
        self.assertIn('fill="#FF5733"', svg)

    def test_pipeline_default_gradient_disabled(self) -> None:
        """Verify pipeline defaults to enable_gradients=False to protect baseline fidelity."""
        pipeline = SequentialPipeline()
        self.assertFalse(pipeline.enable_gradients)
        self.assertEqual(pipeline.seed, 0)

    def test_bezier_segment_and_node_accounting(self) -> None:
        """Verify distinction between cubic segments (C), on-curve anchor nodes, and control handles."""
        p0 = Point2D(0.0, 0.0)
        p1 = Point2D(10.0, 0.0)
        p2 = Point2D(10.0, 10.0)
        p3 = Point2D(0.0, 10.0)
        seg1 = BezierSegment(p0, Point2D(3.0, 0.0), Point2D(7.0, 0.0), p1)
        seg2 = BezierSegment(p1, Point2D(10.0, 3.0), Point2D(10.0, 7.0), p2)
        seg3 = BezierSegment(p2, Point2D(7.0, 10.0), Point2D(3.0, 10.0), p3)
        seg4 = BezierSegment(p3, Point2D(0.0, 7.0), Point2D(0.0, 3.0), p0)
        subpath = [seg1, seg2, seg3, seg4]
        # In a closed loop of K cubic segments:
        k_segments = len(subpath)
        on_curve_anchors = k_segments
        off_curve_handles = k_segments * 2
        total_defining_points = on_curve_anchors + off_curve_handles
        self.assertEqual(k_segments, 4)
        self.assertEqual(on_curve_anchors, 4)
        self.assertEqual(off_curve_handles, 8)
        self.assertEqual(total_defining_points, 12)
```

### `TestVersion01Pipeline.test_point2d_euclidean_distance` — `Lines 19–23`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `19` إلى السطر `23` (`Lines 19–23`)
- **الوظيفة:** Verify 2D distance calculation.
- **الكود الفعلي (`Lines 19–23`):**
```python
    def test_point2d_euclidean_distance(self) -> None:
        """Verify 2D distance calculation."""
        p1 = Point2D(0.0, 0.0)
        p2 = Point2D(3.0, 4.0)
        self.assertAlmostEqual(p1.distance_to(p2), 5.0)
```

### `TestVersion01Pipeline.test_bezier_segment_evaluation` — `Lines 25–36`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `25` إلى السطر `36` (`Lines 25–36`)
- **الوظيفة:** Verify cubic curve evaluation at t=0, t=0.5, t=1.0.
- **الكود الفعلي (`Lines 25–36`):**
```python
    def test_bezier_segment_evaluation(self) -> None:
        """Verify cubic curve evaluation at t=0, t=0.5, t=1.0."""
        p0 = Point2D(0.0, 0.0)
        p1 = Point2D(0.0, 10.0)
        p2 = Point2D(10.0, 10.0)
        p3 = Point2D(10.0, 0.0)
        seg = BezierSegment(p0, p1, p2, p3)
        self.assertEqual(seg.evaluate(0.0), p0)
        self.assertEqual(seg.evaluate(1.0), p3)
        mid = seg.evaluate(0.5)
        self.assertAlmostEqual(mid.x, 5.0)
        self.assertAlmostEqual(mid.y, 7.5)
```

### `TestVersion01Pipeline.test_fit_schneider_bezier_two_points` — `Lines 38–44`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `38` إلى السطر `44` (`Lines 38–44`)
- **الوظيفة:** Fitting two points returns exactly one cubic segment.
- **الكود الفعلي (`Lines 38–44`):**
```python
    def test_fit_schneider_bezier_two_points(self) -> None:
        """Fitting two points returns exactly one cubic segment."""
        pts = [Point2D(0.0, 0.0), Point2D(100.0, 100.0)]
        segments = fit_schneider_bezier(pts)
        self.assertEqual(len(segments), 1)
        self.assertEqual(segments[0].p0, pts[0])
        self.assertEqual(segments[0].p3, pts[1])
```

### `TestVersion01Pipeline.test_pipeline_compile_clean_svg` — `Lines 46–55`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `46` إلى السطر `55` (`Lines 46–55`)
- **الوظيفة:** Verify pipeline produces valid SVG string with descriptor.
- **الكود الفعلي (`Lines 46–55`):**
```python
    def test_pipeline_compile_clean_svg(self) -> None:
        """Verify pipeline produces valid SVG string with descriptor."""
        pipeline = SequentialPipeline(error_tolerance_px=1.5, max_nodes_per_path=36)
        contour = [(10.0, 10.0), (50.0, 10.0), (50.0, 50.0), (10.0, 50.0)]
        layer = pipeline.process_polygon_contour(contour, layer_id="layer_01", label="shield_base", fill_hex="#FF5733")
        svg = pipeline.compile_clean_svg([layer])
        self.assertIn("<svg", svg)
        self.assertIn("version-01", svg)
        self.assertIn('id="layer_01"', svg)
        self.assertIn('fill="#FF5733"', svg)
```

### `TestVersion01Pipeline.test_pipeline_default_gradient_disabled` — `Lines 57–61`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `57` إلى السطر `61` (`Lines 57–61`)
- **الوظيفة:** Verify pipeline defaults to enable_gradients=False to protect baseline fidelity.
- **الكود الفعلي (`Lines 57–61`):**
```python
    def test_pipeline_default_gradient_disabled(self) -> None:
        """Verify pipeline defaults to enable_gradients=False to protect baseline fidelity."""
        pipeline = SequentialPipeline()
        self.assertFalse(pipeline.enable_gradients)
        self.assertEqual(pipeline.seed, 0)
```

### `TestVersion01Pipeline.test_bezier_segment_and_node_accounting` — `Lines 63–82`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `63` إلى السطر `82` (`Lines 63–82`)
- **الوظيفة:** Verify distinction between cubic segments (C), on-curve anchor nodes, and control handles.
- **الكود الفعلي (`Lines 63–82`):**
```python
    def test_bezier_segment_and_node_accounting(self) -> None:
        """Verify distinction between cubic segments (C), on-curve anchor nodes, and control handles."""
        p0 = Point2D(0.0, 0.0)
        p1 = Point2D(10.0, 0.0)
        p2 = Point2D(10.0, 10.0)
        p3 = Point2D(0.0, 10.0)
        seg1 = BezierSegment(p0, Point2D(3.0, 0.0), Point2D(7.0, 0.0), p1)
        seg2 = BezierSegment(p1, Point2D(10.0, 3.0), Point2D(10.0, 7.0), p2)
        seg3 = BezierSegment(p2, Point2D(7.0, 10.0), Point2D(3.0, 10.0), p3)
        seg4 = BezierSegment(p3, Point2D(0.0, 7.0), Point2D(0.0, 3.0), p0)
        subpath = [seg1, seg2, seg3, seg4]
        # In a closed loop of K cubic segments:
        k_segments = len(subpath)
        on_curve_anchors = k_segments
        off_curve_handles = k_segments * 2
        total_defining_points = on_curve_anchors + off_curve_handles
        self.assertEqual(k_segments, 4)
        self.assertEqual(on_curve_anchors, 4)
        self.assertEqual(off_curve_handles, 8)
        self.assertEqual(total_defining_points, 12)
```
