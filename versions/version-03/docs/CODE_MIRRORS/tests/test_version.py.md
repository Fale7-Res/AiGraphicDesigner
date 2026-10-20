# مرآة الكود التفصيلية للإصدار: `version-03/tests/test_version.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED VERSION MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `versions/version-03/tests/test_version.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)** لهذا الإصدار. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py --version version-03`.

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tests/test_version.py`
- **الإصدار المعماري (`Architecture Version`):** `version-03`
- **إجمالي عدد الأسطر (`Total Lines`):** `69` (`Lines 1–69`)
- **بصمة الملف (`SHA-256`):** `ec269fa5432f4afe5c5e69431aa61f6b167da36aeafa9ee442f49c562bb8f0b6`
- **الوصف:** موديول برمجي تنفيذي ضمن معمارية الإصدار `version-03`.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **حوكمة الإصدار الأب (`Parent Version`)** | `version-03` | يتبع مواصفة معمارية هذا الإصدار | مراجعة تكامل الإصدار عند التعديل. |
| **الحوكمة المركزية (`Global Governance`)** | `AGENTS.md` | يخضع للدستور وقواعد منع التكرار المشتركة | التحقق الحوكمي الإلزامي. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `TestVersion03Pipeline` | `class` | `Lines 16–64` | `class TestVersion03Pipeline(unittest.TestCase):` | Test suite validating Version 03 typography and dual-path output. |
| `TestVersion03Pipeline.test_typographic_point_corner_flag` | `method` | `Lines 19–24` | `def test_typographic_point_corner_flag(self) -> None:` | Verify typographic point corner flag preservation. |
| `TestVersion03Pipeline.test_calligraphic_bezier_segment_output` | `method` | `Lines 26–33` | `def test_calligraphic_bezier_segment_output(self) -> None:` | Verify calligraphic segment SVG output. |
| `TestVersion03Pipeline.test_fit_typographic_bezier_with_corners` | `method` | `Lines 35–45` | `def test_fit_typographic_bezier_with_corners(self) -> None:` | Verify corner breakpoints split segments cleanly. |
| `TestVersion03Pipeline.test_dual_path_pipeline_export` | `method` | `Lines 47–64` | `def test_dual_path_pipeline_export(self) -> None:` | Verify dual path SVG contains both outline and editable text nodes. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `TestVersion03Pipeline` — `Lines 16–64`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `64` (`Lines 16–64`)
- **الوظيفة:** Test suite validating Version 03 typography and dual-path output.
- **الكود الفعلي (`Lines 16–64`):**
```python
class TestVersion03Pipeline(unittest.TestCase):
    """Test suite validating Version 03 typography and dual-path output."""

    def test_typographic_point_corner_flag(self) -> None:
        """Verify typographic point corner flag preservation."""
        p = TypographicPoint(10.0, 20.0, is_corner=True)
        self.assertTrue(p.is_corner)
        p2 = TypographicPoint(13.0, 24.0)
        self.assertAlmostEqual(p.distance_to(p2), 5.0)

    def test_calligraphic_bezier_segment_output(self) -> None:
        """Verify calligraphic segment SVG output."""
        p0 = TypographicPoint(0.0, 0.0)
        p1 = TypographicPoint(10.0, 5.0)
        p2 = TypographicPoint(20.0, 5.0)
        p3 = TypographicPoint(30.0, 0.0)
        seg = CalligraphicBezierSegment(p0, p1, p2, p3)
        self.assertIn("C 10.00 5.00, 20.00 5.00, 30.00 0.00", seg.to_svg_cubic_path())

    def test_fit_typographic_bezier_with_corners(self) -> None:
        """Verify corner breakpoints split segments cleanly."""
        points = [
            TypographicPoint(0.0, 0.0),
            TypographicPoint(50.0, 0.0, is_corner=True),
            TypographicPoint(100.0, 50.0),
        ]
        segments = fit_typographic_bezier(points)
        self.assertEqual(len(segments), 2)
        self.assertEqual(segments[0].p0, points[0])
        self.assertEqual(segments[1].p3, points[2])

    def test_dual_path_pipeline_export(self) -> None:
        """Verify dual path SVG contains both outline and editable text nodes."""
        pipeline = DualPathTypographyPipeline(default_font_fallback="Amiri")
        contour = [(0.0, 0.0), (20.0, 0.0), (40.0, 20.0), (0.0, 20.0)]
        layer = pipeline.create_typography_layer(
            layer_id="logo_text",
            text="تصميم ذكي",
            font_family="Amiri",
            contour_points=contour,
            fill_hex="#222222",
        )
        svg = pipeline.export_dual_path_svg([layer])
        self.assertIn("<svg", svg)
        self.assertIn("version-03", svg)
        self.assertIn('id="visual_outlines_layer"', svg)
        self.assertIn('id="editable_text_layer"', svg)
        self.assertIn('direction="rtl"', svg)
        self.assertIn("تصميم ذكي", svg)
```

### `TestVersion03Pipeline.test_typographic_point_corner_flag` — `Lines 19–24`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `19` إلى السطر `24` (`Lines 19–24`)
- **الوظيفة:** Verify typographic point corner flag preservation.
- **الكود الفعلي (`Lines 19–24`):**
```python
    def test_typographic_point_corner_flag(self) -> None:
        """Verify typographic point corner flag preservation."""
        p = TypographicPoint(10.0, 20.0, is_corner=True)
        self.assertTrue(p.is_corner)
        p2 = TypographicPoint(13.0, 24.0)
        self.assertAlmostEqual(p.distance_to(p2), 5.0)
```

### `TestVersion03Pipeline.test_calligraphic_bezier_segment_output` — `Lines 26–33`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `26` إلى السطر `33` (`Lines 26–33`)
- **الوظيفة:** Verify calligraphic segment SVG output.
- **الكود الفعلي (`Lines 26–33`):**
```python
    def test_calligraphic_bezier_segment_output(self) -> None:
        """Verify calligraphic segment SVG output."""
        p0 = TypographicPoint(0.0, 0.0)
        p1 = TypographicPoint(10.0, 5.0)
        p2 = TypographicPoint(20.0, 5.0)
        p3 = TypographicPoint(30.0, 0.0)
        seg = CalligraphicBezierSegment(p0, p1, p2, p3)
        self.assertIn("C 10.00 5.00, 20.00 5.00, 30.00 0.00", seg.to_svg_cubic_path())
```

### `TestVersion03Pipeline.test_fit_typographic_bezier_with_corners` — `Lines 35–45`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `35` إلى السطر `45` (`Lines 35–45`)
- **الوظيفة:** Verify corner breakpoints split segments cleanly.
- **الكود الفعلي (`Lines 35–45`):**
```python
    def test_fit_typographic_bezier_with_corners(self) -> None:
        """Verify corner breakpoints split segments cleanly."""
        points = [
            TypographicPoint(0.0, 0.0),
            TypographicPoint(50.0, 0.0, is_corner=True),
            TypographicPoint(100.0, 50.0),
        ]
        segments = fit_typographic_bezier(points)
        self.assertEqual(len(segments), 2)
        self.assertEqual(segments[0].p0, points[0])
        self.assertEqual(segments[1].p3, points[2])
```

### `TestVersion03Pipeline.test_dual_path_pipeline_export` — `Lines 47–64`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `47` إلى السطر `64` (`Lines 47–64`)
- **الوظيفة:** Verify dual path SVG contains both outline and editable text nodes.
- **الكود الفعلي (`Lines 47–64`):**
```python
    def test_dual_path_pipeline_export(self) -> None:
        """Verify dual path SVG contains both outline and editable text nodes."""
        pipeline = DualPathTypographyPipeline(default_font_fallback="Amiri")
        contour = [(0.0, 0.0), (20.0, 0.0), (40.0, 20.0), (0.0, 20.0)]
        layer = pipeline.create_typography_layer(
            layer_id="logo_text",
            text="تصميم ذكي",
            font_family="Amiri",
            contour_points=contour,
            fill_hex="#222222",
        )
        svg = pipeline.export_dual_path_svg([layer])
        self.assertIn("<svg", svg)
        self.assertIn("version-03", svg)
        self.assertIn('id="visual_outlines_layer"', svg)
        self.assertIn('id="editable_text_layer"', svg)
        self.assertIn('direction="rtl"', svg)
        self.assertIn("تصميم ذكي", svg)
```
