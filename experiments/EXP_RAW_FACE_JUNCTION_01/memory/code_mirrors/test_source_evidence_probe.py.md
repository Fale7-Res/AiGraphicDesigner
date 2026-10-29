# مرآة الكود التفصيلية: `test_source_evidence_probe.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_source_evidence_probe.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_source_evidence_probe.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `42` (`Lines 1–42`)
- **بصمة الملف (`SHA-256`):** `3121b3b2e7fabe392f213c0dfa1e351da8b8c0c2147cdd292b0a6aeebe7b4855`
- **الوصف التفصيلي:** # START CHANGE AGD-RAWFACE-TEST-SOURCE-EVIDENCE-PROBE | 2026-10-29T12:20:15Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `EvidenceTests` | `class` | `Lines 8–36` | `class EvidenceTests(unittest.TestCase):` | رمز برمجي موثق. |
| `EvidenceTests.test_constant_has_no_edges_or_ridges` | `method` | `Lines 9–13` | `def test_constant_has_no_edges_or_ridges(self):` | رمز برمجي موثق. |
| `EvidenceTests.test_empty_support_does_not_create_corner_evidence` | `method` | `Lines 15–16` | `def test_empty_support_does_not_create_corner_evidence(self):` | رمز برمجي موثق. |
| `EvidenceTests.test_deterministic_nonmutating_source_only` | `method` | `Lines 18–31` | `def test_deterministic_nonmutating_source_only(self):` | رمز برمجي موثق. |
| `EvidenceTests.test_rejects_ambiguous_float_or_rgba_input` | `method` | `Lines 33–36` | `def test_rejects_ambiguous_float_or_rgba_input(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `EvidenceTests` — `Lines 8–36`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `8` إلى السطر `36` (`Lines 8–36`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 8–36`):**
```python
class EvidenceTests(unittest.TestCase):
    def test_constant_has_no_edges_or_ridges(self):
        arrays, meta = extract(np.full((24, 30, 3), 127, np.uint8))
        self.assertEqual(meta['persistent_edge_pixels'], 0)
        self.assertEqual(meta['ridge_maxima'], {'dark': 0.0, 'light': 0.0})
        self.assertFalse(arrays['persistent_edges'].any())

    def test_empty_support_does_not_create_corner_evidence(self):
        self.assertFalse(_near(np.zeros((5, 5), bool), 1.0).any())

    def test_deterministic_nonmutating_source_only(self):
        source = np.full((32, 32, 3), 240, np.uint8)
        source[5:27, 12:15] = [10, 10, 10]
        snapshot = source.copy()
        first, metadata = extract(source)
        second, _ = extract(source)
        np.testing.assert_array_equal(source, snapshot)
        for key in first:
            np.testing.assert_array_equal(first[key], second[key])
            self.assertEqual(first[key].shape, source.shape[:2])
            self.assertTrue(np.isfinite(first[key]).all())
        self.assertGreater(metadata['persistent_edge_pixels'], 0)
        self.assertGreater(metadata['ridge_maxima']['dark'], 0)
        self.assertFalse(metadata['config']['output_is_reconstructed_geometry'])

    def test_rejects_ambiguous_float_or_rgba_input(self):
        for source in [np.zeros((4, 4, 3)), np.zeros((4, 4, 4), np.uint8)]:
            with self.assertRaises(ValueError):
                extract(source)
```

### `EvidenceTests.test_constant_has_no_edges_or_ridges` — `Lines 9–13`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `13` (`Lines 9–13`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–13`):**
```python
    def test_constant_has_no_edges_or_ridges(self):
        arrays, meta = extract(np.full((24, 30, 3), 127, np.uint8))
        self.assertEqual(meta['persistent_edge_pixels'], 0)
        self.assertEqual(meta['ridge_maxima'], {'dark': 0.0, 'light': 0.0})
        self.assertFalse(arrays['persistent_edges'].any())
```

### `EvidenceTests.test_empty_support_does_not_create_corner_evidence` — `Lines 15–16`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `15` إلى السطر `16` (`Lines 15–16`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 15–16`):**
```python
    def test_empty_support_does_not_create_corner_evidence(self):
        self.assertFalse(_near(np.zeros((5, 5), bool), 1.0).any())
```

### `EvidenceTests.test_deterministic_nonmutating_source_only` — `Lines 18–31`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `31` (`Lines 18–31`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 18–31`):**
```python
    def test_deterministic_nonmutating_source_only(self):
        source = np.full((32, 32, 3), 240, np.uint8)
        source[5:27, 12:15] = [10, 10, 10]
        snapshot = source.copy()
        first, metadata = extract(source)
        second, _ = extract(source)
        np.testing.assert_array_equal(source, snapshot)
        for key in first:
            np.testing.assert_array_equal(first[key], second[key])
            self.assertEqual(first[key].shape, source.shape[:2])
            self.assertTrue(np.isfinite(first[key]).all())
        self.assertGreater(metadata['persistent_edge_pixels'], 0)
        self.assertGreater(metadata['ridge_maxima']['dark'], 0)
        self.assertFalse(metadata['config']['output_is_reconstructed_geometry'])
```

### `EvidenceTests.test_rejects_ambiguous_float_or_rgba_input` — `Lines 33–36`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `33` إلى السطر `36` (`Lines 33–36`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 33–36`):**
```python
    def test_rejects_ambiguous_float_or_rgba_input(self):
        for source in [np.zeros((4, 4, 3)), np.zeros((4, 4, 4), np.uint8)]:
            with self.assertRaises(ValueError):
                extract(source)
```
