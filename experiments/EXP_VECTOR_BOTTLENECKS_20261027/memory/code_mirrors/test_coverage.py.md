# مرآة الكود التفصيلية: `test_coverage.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_coverage.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_coverage.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `49` (`Lines 1–49`)
- **بصمة الملف (`SHA-256`):** `9a3fce6be2ffe21af541658014ed515c12ecaf4ac80a16ca0f446e46d4b43fc0`
- **الوصف التفصيلي:** """Coverage diagnostics and reversible stroke invariants; no new searches."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `CoverageTests` | `class` | `Lines 8–46` | `class CoverageTests(unittest.TestCase):` | رمز برمجي موثق. |
| `CoverageTests.test_exact_partition_aa_seam_differs_from_known_union` | `method` | `Lines 9–15` | `def test_exact_partition_aa_seam_differs_from_known_union(self):` | رمز برمجي موثق. |
| `CoverageTests.test_real_gap_negative_not_declared_repaired` | `method` | `Lines 16–19` | `def test_real_gap_negative_not_declared_repaired(self):` | رمز برمجي موثق. |
| `CoverageTests.test_exterior_stroke_changes_known_silhouette` | `method` | `Lines 20–22` | `def test_exterior_stroke_changes_known_silhouette(self):` | رمز برمجي موثق. |
| `CoverageTests.test_mask_and_path_geometry_untouched_gradient_paint_reused` | `method` | `Lines 23–31` | `def test_mask_and_path_geometry_untouched_gradient_paint_reused(self):` | رمز برمجي موثق. |
| `CoverageTests.test_out_of_scope_stroke_width_refused` | `method` | `Lines 32–33` | `def test_out_of_scope_stroke_width_refused(self):` | رمز برمجي موثق. |
| `CoverageTests.test_nonempty_run_targets_refused` | `method` | `Lines 34–46` | `def test_nonempty_run_targets_refused(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `CoverageTests` — `Lines 8–46`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `8` إلى السطر `46` (`Lines 8–46`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 8–46`):**
```python
class CoverageTests(unittest.TestCase):
    def test_exact_partition_aa_seam_differs_from_known_union(self):
        results=json.loads((ROOT/'results/coverage/controls/results.json').read_text())
        for name in ('diagonal','curved'):
            row=results[name]['coverage']
            self.assertGreater(row['separate_1x']['interior_alpha_deficit_pixels'],0)
            self.assertEqual(row['compound_1x']['interior_alpha_deficit_pixels'],0)
            self.assertGreaterEqual(row['separate_1x']['coverage_deficit_source_pixel_equivalents'],row['stroke025_1x']['coverage_deficit_source_pixel_equivalents'])
    def test_real_gap_negative_not_declared_repaired(self):
        row=json.loads((ROOT/'results/coverage/controls/results.json').read_text())['genuine_gap']['coverage']
        self.assertGreater(row['compound_1x']['coverage_deficit_source_pixel_equivalents'],0)
        self.assertGreater(row['stroke025_1x']['coverage_deficit_source_pixel_equivalents'],0)
    def test_exterior_stroke_changes_known_silhouette(self):
        row=json.loads((ROOT/'results/coverage/controls/results.json').read_text())['exterior']['coverage']['4x']
        self.assertGreater(row['coverage_excess_source_pixel_equivalents'],0)
    def test_mask_and_path_geometry_untouched_gradient_paint_reused(self):
        source=f'<svg xmlns="{SVG}" width="8" height="8"><defs><mask id="m"><path fill="white" d="M0 0H8V8H0Z"/></mask><linearGradient id="g"/></defs><g mask="url(#m)"><path fill="url(#g)" d="M1 1H7V7H1Z"/></g></svg>'
        with tempfile.TemporaryDirectory() as tmp:
            a=Path(tmp)/'a.svg';b=Path(tmp)/'b.svg';a.write_text(source)
            before=ET.parse(a).getroot();correct_coverage(a,b);after=ET.parse(b).getroot()
            self.assertEqual(ET.tostring(next(before.iter(f'{{{SVG}}}mask'))),ET.tostring(next(after.iter(f'{{{SVG}}}mask'))))
            self.assertEqual([p.get('d') for p in rgb_paths(before)],[p.get('d') for p in rgb_paths(after)])
            self.assertEqual(rgb_paths(after)[0].get('stroke'),'url(#g)')
            self.assertEqual(a.read_text(),source)
    def test_out_of_scope_stroke_width_refused(self):
        with self.assertRaises(ValueError):correct_coverage('missing.svg','unused.svg',width=2)
    def test_nonempty_run_targets_refused(self):
        previous=coverage_module.ROOT
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'results/coverage/controls').mkdir(parents=True)
            (root/'results/coverage/controls/preserved.txt').write_text('keep')
            coverage_module.ROOT=root
            try:
                with self.assertRaises(FileExistsError):coverage_module.run_exact_controls()
                (root/'results/coverage/A01_shield').mkdir()
                (root/'results/coverage/A01_shield/preserved.txt').write_text('keep')
                with self.assertRaises(FileExistsError):coverage_module.run_real_cases()
                self.assertEqual((root/'results/coverage/A01_shield/preserved.txt').read_text(),'keep')
            finally:coverage_module.ROOT=previous
```

### `CoverageTests.test_exact_partition_aa_seam_differs_from_known_union` — `Lines 9–15`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `15` (`Lines 9–15`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–15`):**
```python
    def test_exact_partition_aa_seam_differs_from_known_union(self):
        results=json.loads((ROOT/'results/coverage/controls/results.json').read_text())
        for name in ('diagonal','curved'):
            row=results[name]['coverage']
            self.assertGreater(row['separate_1x']['interior_alpha_deficit_pixels'],0)
            self.assertEqual(row['compound_1x']['interior_alpha_deficit_pixels'],0)
            self.assertGreaterEqual(row['separate_1x']['coverage_deficit_source_pixel_equivalents'],row['stroke025_1x']['coverage_deficit_source_pixel_equivalents'])
```

### `CoverageTests.test_real_gap_negative_not_declared_repaired` — `Lines 16–19`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `19` (`Lines 16–19`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 16–19`):**
```python
    def test_real_gap_negative_not_declared_repaired(self):
        row=json.loads((ROOT/'results/coverage/controls/results.json').read_text())['genuine_gap']['coverage']
        self.assertGreater(row['compound_1x']['coverage_deficit_source_pixel_equivalents'],0)
        self.assertGreater(row['stroke025_1x']['coverage_deficit_source_pixel_equivalents'],0)
```

### `CoverageTests.test_exterior_stroke_changes_known_silhouette` — `Lines 20–22`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `20` إلى السطر `22` (`Lines 20–22`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 20–22`):**
```python
    def test_exterior_stroke_changes_known_silhouette(self):
        row=json.loads((ROOT/'results/coverage/controls/results.json').read_text())['exterior']['coverage']['4x']
        self.assertGreater(row['coverage_excess_source_pixel_equivalents'],0)
```

### `CoverageTests.test_mask_and_path_geometry_untouched_gradient_paint_reused` — `Lines 23–31`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `23` إلى السطر `31` (`Lines 23–31`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 23–31`):**
```python
    def test_mask_and_path_geometry_untouched_gradient_paint_reused(self):
        source=f'<svg xmlns="{SVG}" width="8" height="8"><defs><mask id="m"><path fill="white" d="M0 0H8V8H0Z"/></mask><linearGradient id="g"/></defs><g mask="url(#m)"><path fill="url(#g)" d="M1 1H7V7H1Z"/></g></svg>'
        with tempfile.TemporaryDirectory() as tmp:
            a=Path(tmp)/'a.svg';b=Path(tmp)/'b.svg';a.write_text(source)
            before=ET.parse(a).getroot();correct_coverage(a,b);after=ET.parse(b).getroot()
            self.assertEqual(ET.tostring(next(before.iter(f'{{{SVG}}}mask'))),ET.tostring(next(after.iter(f'{{{SVG}}}mask'))))
            self.assertEqual([p.get('d') for p in rgb_paths(before)],[p.get('d') for p in rgb_paths(after)])
            self.assertEqual(rgb_paths(after)[0].get('stroke'),'url(#g)')
            self.assertEqual(a.read_text(),source)
```

### `CoverageTests.test_out_of_scope_stroke_width_refused` — `Lines 32–33`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `32` إلى السطر `33` (`Lines 32–33`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 32–33`):**
```python
    def test_out_of_scope_stroke_width_refused(self):
        with self.assertRaises(ValueError):correct_coverage('missing.svg','unused.svg',width=2)
```

### `CoverageTests.test_nonempty_run_targets_refused` — `Lines 34–46`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `34` إلى السطر `46` (`Lines 34–46`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 34–46`):**
```python
    def test_nonempty_run_targets_refused(self):
        previous=coverage_module.ROOT
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'results/coverage/controls').mkdir(parents=True)
            (root/'results/coverage/controls/preserved.txt').write_text('keep')
            coverage_module.ROOT=root
            try:
                with self.assertRaises(FileExistsError):coverage_module.run_exact_controls()
                (root/'results/coverage/A01_shield').mkdir()
                (root/'results/coverage/A01_shield/preserved.txt').write_text('keep')
                with self.assertRaises(FileExistsError):coverage_module.run_real_cases()
                self.assertEqual((root/'results/coverage/A01_shield/preserved.txt').read_text(),'keep')
            finally:coverage_module.ROOT=previous
```
