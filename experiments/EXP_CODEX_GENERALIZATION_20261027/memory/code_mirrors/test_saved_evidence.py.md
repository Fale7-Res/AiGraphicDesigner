# مرآة الكود التفصيلية: `test_saved_evidence.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_saved_evidence.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_saved_evidence.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `30` (`Lines 1–30`)
- **بصمة الملف (`SHA-256`):** `89d7baf8ab01b01fd45eaebf248fab1f4521d0e68624179f5f0eeee46e8861ac`
- **الوصف التفصيلي:** """Regression checks against actual saved research evidence; never trace or render."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `SavedGeneralizationEvidenceTests` | `class` | `Lines 7–27` | `class SavedGeneralizationEvidenceTests(unittest.TestCase):` | رمز برمجي موثق. |
| `SavedGeneralizationEvidenceTests.setUpClass` | `method` | `Lines 9–10` | `def setUpClass(cls):` | رمز برمجي موثق. |
| `SavedGeneralizationEvidenceTests.test_frozen_sources_and_140_successful_candidates` | `method` | `Lines 11–12` | `def test_frozen_sources_and_140_successful_candidates(self):` | رمز برمجي موثق. |
| `SavedGeneralizationEvidenceTests.test_no_reconstruction_improvement_or_reranked_winner` | `method` | `Lines 13–14` | `def test_no_reconstruction_improvement_or_reranked_winner(self):` | رمز برمجي موثق. |
| `SavedGeneralizationEvidenceTests.test_selected_transparency_exact_at_test_dimensions` | `method` | `Lines 15–17` | `def test_selected_transparency_exact_at_test_dimensions(self):` | رمز برمجي موثق. |
| `SavedGeneralizationEvidenceTests.test_saved_metrics_and_all_svg_png_artifacts` | `method` | `Lines 18–19` | `def test_saved_metrics_and_all_svg_png_artifacts(self):` | رمز برمجي موثق. |
| `SavedGeneralizationEvidenceTests.test_saved_evidence_byte_preservation` | `method` | `Lines 20–21` | `def test_saved_evidence_byte_preservation(self):` | رمز برمجي موثق. |
| `SavedGeneralizationEvidenceTests.test_visual_sheets_decode_and_dashboard_has_all_cases` | `method` | `Lines 22–27` | `def test_visual_sheets_decode_and_dashboard_has_all_cases(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `SavedGeneralizationEvidenceTests` — `Lines 7–27`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `7` إلى السطر `27` (`Lines 7–27`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 7–27`):**
```python
class SavedGeneralizationEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=check_saved_evidence()
    def test_frozen_sources_and_140_successful_candidates(self):
        self.assertEqual(tuple(self.report[k] for k in ('case_count','independent_originals','candidates','failed_candidates')),(8,7,140,0))
    def test_no_reconstruction_improvement_or_reranked_winner(self):
        self.assertEqual(self.report['same_winner_cases'],8);self.assertFalse(self.report['reconstruction_improvement_demonstrated'])
    def test_selected_transparency_exact_at_test_dimensions(self):
        rows=[r for r in self.report['cases'] if r['has_alpha']];self.assertEqual(len(rows),3)
        for row in rows:self.assertEqual(row['alpha_max_error_0_255'],0)
    def test_saved_metrics_and_all_svg_png_artifacts(self):
        self.assertEqual(self.report['status'],'PASS');self.assertGreaterEqual(self.report['svgs_parsed_raster_free'],140);self.assertGreaterEqual(self.report['pngs_decoded'],140)
    def test_saved_evidence_byte_preservation(self):
        self.assertEqual(json.loads((ROOT/'reports/saved_artifact_inventory.json').read_text()),saved_inventory())
    def test_visual_sheets_decode_and_dashboard_has_all_cases(self):
        document=(ROOT/'reports/dashboard.html').read_text(encoding='utf-8')
        for row in self.report['cases']:self.assertIn(row['id'],document)
        sheets=list((ROOT/'reports/comparisons').glob('*.png'));self.assertGreaterEqual(len(sheets),16)
        for path in sheets:
            with Image.open(path) as im:im.load();self.assertGreater(im.width,0)
```

### `SavedGeneralizationEvidenceTests.setUpClass` — `Lines 9–10`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `10` (`Lines 9–10`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–10`):**
```python
    def setUpClass(cls):
        cls.report=check_saved_evidence()
```

### `SavedGeneralizationEvidenceTests.test_frozen_sources_and_140_successful_candidates` — `Lines 11–12`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `11` إلى السطر `12` (`Lines 11–12`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 11–12`):**
```python
    def test_frozen_sources_and_140_successful_candidates(self):
        self.assertEqual(tuple(self.report[k] for k in ('case_count','independent_originals','candidates','failed_candidates')),(8,7,140,0))
```

### `SavedGeneralizationEvidenceTests.test_no_reconstruction_improvement_or_reranked_winner` — `Lines 13–14`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `14` (`Lines 13–14`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 13–14`):**
```python
    def test_no_reconstruction_improvement_or_reranked_winner(self):
        self.assertEqual(self.report['same_winner_cases'],8);self.assertFalse(self.report['reconstruction_improvement_demonstrated'])
```

### `SavedGeneralizationEvidenceTests.test_selected_transparency_exact_at_test_dimensions` — `Lines 15–17`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `15` إلى السطر `17` (`Lines 15–17`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 15–17`):**
```python
    def test_selected_transparency_exact_at_test_dimensions(self):
        rows=[r for r in self.report['cases'] if r['has_alpha']];self.assertEqual(len(rows),3)
        for row in rows:self.assertEqual(row['alpha_max_error_0_255'],0)
```

### `SavedGeneralizationEvidenceTests.test_saved_metrics_and_all_svg_png_artifacts` — `Lines 18–19`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `19` (`Lines 18–19`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 18–19`):**
```python
    def test_saved_metrics_and_all_svg_png_artifacts(self):
        self.assertEqual(self.report['status'],'PASS');self.assertGreaterEqual(self.report['svgs_parsed_raster_free'],140);self.assertGreaterEqual(self.report['pngs_decoded'],140)
```

### `SavedGeneralizationEvidenceTests.test_saved_evidence_byte_preservation` — `Lines 20–21`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `20` إلى السطر `21` (`Lines 20–21`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 20–21`):**
```python
    def test_saved_evidence_byte_preservation(self):
        self.assertEqual(json.loads((ROOT/'reports/saved_artifact_inventory.json').read_text()),saved_inventory())
```

### `SavedGeneralizationEvidenceTests.test_visual_sheets_decode_and_dashboard_has_all_cases` — `Lines 22–27`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `22` إلى السطر `27` (`Lines 22–27`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 22–27`):**
```python
    def test_visual_sheets_decode_and_dashboard_has_all_cases(self):
        document=(ROOT/'reports/dashboard.html').read_text(encoding='utf-8')
        for row in self.report['cases']:self.assertIn(row['id'],document)
        sheets=list((ROOT/'reports/comparisons').glob('*.png'));self.assertGreaterEqual(len(sheets),16)
        for path in sheets:
            with Image.open(path) as im:im.load();self.assertGreater(im.width,0)
```
