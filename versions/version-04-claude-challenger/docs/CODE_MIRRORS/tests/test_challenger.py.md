# مرآة الكود التفصيلية للإصدار: `version-04-claude-challenger/tests/test_challenger.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED VERSION MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `versions/version-04-claude-challenger/tests/test_challenger.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)** لهذا الإصدار. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py --version version-04-claude-challenger`.

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tests/test_challenger.py`
- **الإصدار المعماري (`Architecture Version`):** `version-04-claude-challenger`
- **إجمالي عدد الأسطر (`Total Lines`):** `62` (`Lines 1–62`)
- **بصمة الملف (`SHA-256`):** `9a9aa69263e39463cb9d6cd38979f04b9a2646a26493dd25bfe9cd4a0df54f20`
- **الوصف:** موديول برمجي تنفيذي ضمن معمارية الإصدار `version-04-claude-challenger`.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **حوكمة الإصدار الأب (`Parent Version`)** | `version-04-claude-challenger` | يتبع مواصفة معمارية هذا الإصدار | مراجعة تكامل الإصدار عند التعديل. |
| **الحوكمة المركزية (`Global Governance`)** | `AGENTS.md` | يخضع للدستور وقواعد منع التكرار المشتركة | التحقق الحوكمي الإلزامي. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `ChallengerTests` | `class` | `Lines 16–58` | `class ChallengerTests(unittest.TestCase):` | رمز برمجي موثق للإصدار. |
| `ChallengerTests.test_surface_output_stays_within_leaf_budget_and_contains_no_raster` | `method` | `Lines 17–26` | `def test_surface_output_stays_within_leaf_budget_and_contains_no_raster(self):` | رمز برمجي موثق للإصدار. |
| `ChallengerTests.test_constant_image_is_valid_svg_and_has_no_gradient_need` | `method` | `Lines 28–34` | `def test_constant_image_is_valid_svg_and_has_no_gradient_need(self):` | رمز برمجي موثق للإصدار. |
| `ChallengerTests.test_edge_residual_is_explicit_vector_hybrid` | `method` | `Lines 36–48` | `def test_edge_residual_is_explicit_vector_hybrid(self):` | رمز برمجي موثق للإصدار. |
| `ChallengerTests.test_edge_residual_is_deterministic` | `method` | `Lines 50–58` | `def test_edge_residual_is_deterministic(self):` | رمز برمجي موثق للإصدار. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `ChallengerTests` — `Lines 16–58`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `58` (`Lines 16–58`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 16–58`):**
```python
class ChallengerTests(unittest.TestCase):
    def test_surface_output_stays_within_leaf_budget_and_contains_no_raster(self):
        rgb = np.zeros((32, 48, 3), dtype=np.uint8)
        rgb[:] = (238, 240, 242)
        rgb[5:26, 9:37] = (20, 60, 90)
        svg, meta = AdaptiveVectorSurface(Config(max_cells=180)).vectorize(rgb)
        root = ET.fromstring(svg)
        self.assertEqual(root.tag.rsplit('}', 1)[-1], 'svg')
        self.assertLessEqual(meta['leaf_cells'], 180)
        self.assertEqual(len(root.findall('.//svg:rect', SVG_NS)), meta['rectangles'])
        self.assertEqual(root.findall('.//svg:image', SVG_NS), [])

    def test_constant_image_is_valid_svg_and_has_no_gradient_need(self):
        rgb = np.full((24, 24, 3), (128, 128, 128), dtype=np.uint8)
        svg, meta = AdaptiveVectorSurface(Config(max_cells=40)).vectorize(rgb)
        root = ET.fromstring(svg)
        self.assertEqual(len(root.findall('.//svg:rect', SVG_NS)), 1)
        self.assertEqual(meta['linear_gradients'], 0)
        self.assertIn('#808080', svg.lower())

    def test_edge_residual_is_explicit_vector_hybrid(self):
        rgb = np.zeros((30, 30, 3), dtype=np.uint8)
        rgb[:] = (245, 245, 245)
        rgb[8:22, 7:23] = (200, 20, 30)
        base, _ = AdaptiveVectorSurface(Config(max_cells=120)).vectorize(rgb)
        hybrid, edge = add_edge_residual_layer(base, rgb, dilation=1, color_bits=5)
        root = ET.fromstring(hybrid)
        self.assertIn('Hybrid vector-only representation', hybrid)
        self.assertIn('edge-band-residuals', hybrid)
        self.assertGreater(edge['edge_residual_pixels'], 0)
        self.assertEqual(edge['embedded_raster_images'], 0)
        self.assertEqual(root.findall('.//svg:image', SVG_NS), [])
        self.assertGreater(len(root.findall('.//svg:path', SVG_NS)), 0)

    def test_edge_residual_is_deterministic(self):
        yy, xx = np.indices((25, 31))
        rgb = np.stack([xx * 7 % 256, yy * 9 % 256, (xx + yy) * 5 % 256], axis=2).astype(np.uint8)
        base1, _ = AdaptiveVectorSurface(Config(max_cells=90)).vectorize(rgb)
        base2, _ = AdaptiveVectorSurface(Config(max_cells=90)).vectorize(rgb)
        out1, meta1 = add_edge_residual_layer(base1, rgb)
        out2, meta2 = add_edge_residual_layer(base2, rgb)
        self.assertEqual(out1, out2)
        self.assertEqual(meta1, meta2)
```

### `ChallengerTests.test_surface_output_stays_within_leaf_budget_and_contains_no_raster` — `Lines 17–26`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `17` إلى السطر `26` (`Lines 17–26`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 17–26`):**
```python
    def test_surface_output_stays_within_leaf_budget_and_contains_no_raster(self):
        rgb = np.zeros((32, 48, 3), dtype=np.uint8)
        rgb[:] = (238, 240, 242)
        rgb[5:26, 9:37] = (20, 60, 90)
        svg, meta = AdaptiveVectorSurface(Config(max_cells=180)).vectorize(rgb)
        root = ET.fromstring(svg)
        self.assertEqual(root.tag.rsplit('}', 1)[-1], 'svg')
        self.assertLessEqual(meta['leaf_cells'], 180)
        self.assertEqual(len(root.findall('.//svg:rect', SVG_NS)), meta['rectangles'])
        self.assertEqual(root.findall('.//svg:image', SVG_NS), [])
```

### `ChallengerTests.test_constant_image_is_valid_svg_and_has_no_gradient_need` — `Lines 28–34`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `28` إلى السطر `34` (`Lines 28–34`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 28–34`):**
```python
    def test_constant_image_is_valid_svg_and_has_no_gradient_need(self):
        rgb = np.full((24, 24, 3), (128, 128, 128), dtype=np.uint8)
        svg, meta = AdaptiveVectorSurface(Config(max_cells=40)).vectorize(rgb)
        root = ET.fromstring(svg)
        self.assertEqual(len(root.findall('.//svg:rect', SVG_NS)), 1)
        self.assertEqual(meta['linear_gradients'], 0)
        self.assertIn('#808080', svg.lower())
```

### `ChallengerTests.test_edge_residual_is_explicit_vector_hybrid` — `Lines 36–48`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `36` إلى السطر `48` (`Lines 36–48`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 36–48`):**
```python
    def test_edge_residual_is_explicit_vector_hybrid(self):
        rgb = np.zeros((30, 30, 3), dtype=np.uint8)
        rgb[:] = (245, 245, 245)
        rgb[8:22, 7:23] = (200, 20, 30)
        base, _ = AdaptiveVectorSurface(Config(max_cells=120)).vectorize(rgb)
        hybrid, edge = add_edge_residual_layer(base, rgb, dilation=1, color_bits=5)
        root = ET.fromstring(hybrid)
        self.assertIn('Hybrid vector-only representation', hybrid)
        self.assertIn('edge-band-residuals', hybrid)
        self.assertGreater(edge['edge_residual_pixels'], 0)
        self.assertEqual(edge['embedded_raster_images'], 0)
        self.assertEqual(root.findall('.//svg:image', SVG_NS), [])
        self.assertGreater(len(root.findall('.//svg:path', SVG_NS)), 0)
```

### `ChallengerTests.test_edge_residual_is_deterministic` — `Lines 50–58`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `50` إلى السطر `58` (`Lines 50–58`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 50–58`):**
```python
    def test_edge_residual_is_deterministic(self):
        yy, xx = np.indices((25, 31))
        rgb = np.stack([xx * 7 % 256, yy * 9 % 256, (xx + yy) * 5 % 256], axis=2).astype(np.uint8)
        base1, _ = AdaptiveVectorSurface(Config(max_cells=90)).vectorize(rgb)
        base2, _ = AdaptiveVectorSurface(Config(max_cells=90)).vectorize(rgb)
        out1, meta1 = add_edge_residual_layer(base1, rgb)
        out2, meta2 = add_edge_residual_layer(base2, rgb)
        self.assertEqual(out1, out2)
        self.assertEqual(meta1, meta2)
```
