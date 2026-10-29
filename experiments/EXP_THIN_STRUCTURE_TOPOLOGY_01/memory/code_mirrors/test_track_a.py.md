# مرآة الكود التفصيلية: `test_track_a.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_track_a.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_track_a.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `44` (`Lines 1–44`)
- **بصمة الملف (`SHA-256`):** `0ac5669ad98399ce262e244bbcce0d6d663b0f11ee4a9b087e5e9cc0bf69d23d`
- **الوصف التفصيلي:** """Abstract Track A controls; no research benchmark/GT input."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `line_control` | `function` | `Lines 7–11` | `def line_control(supported=True):` | رمز برمجي موثق. |
| `TrackATests` | `class` | `Lines 13–41` | `class TrackATests(unittest.TestCase):` | رمز برمجي موثق. |
| `TrackATests.test_supported_missing_label_connector` | `method` | `Lines 14–18` | `def test_supported_missing_label_connector(self):` | رمز برمجي موثق. |
| `TrackATests.test_blank_gap_rejected_no_global_fallback` | `method` | `Lines 19–22` | `def test_blank_gap_rejected_no_global_fallback(self):` | رمز برمجي موثق. |
| `TrackATests.test_determinism_and_input_immutability` | `method` | `Lines 23–26` | `def test_determinism_and_input_immutability(self):` | رمز برمجي موثق. |
| `TrackATests.test_parallel_offset_features_not_joined` | `method` | `Lines 27–30` | `def test_parallel_offset_features_not_joined(self):` | رمز برمجي موثق. |
| `TrackATests.test_adjacent_tonal_regions_not_globally_merged` | `method` | `Lines 31–34` | `def test_adjacent_tonal_regions_not_globally_merged(self):` | رمز برمجي موثق. |
| `TrackATests.test_pair_budget_and_convex_mixture` | `method` | `Lines 35–41` | `def test_pair_budget_and_convex_mixture(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `line_control` — `Lines 7–11`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `7` إلى السطر `11` (`Lines 7–11`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 7–11`):**
```python
def line_control(supported=True):
    rgb=np.full((21,41,3),255,np.uint8);labels=np.ones((21,41),np.uint32)
    rgb[10,5:35]=[24,30,40];labels[10,5:15]=2;labels[10,17:35]=3
    if not supported:rgb[10,15:17]=255
    return rgb,labels
```

### `TrackATests` — `Lines 13–41`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `41` (`Lines 13–41`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 13–41`):**
```python
class TrackATests(unittest.TestCase):
    def test_supported_missing_label_connector(self):
        rgb,labels=line_control();out,audit,evidence=discover(rgb,labels)
        self.assertEqual(audit['accepted_bridges'],1);self.assertEqual(audit['connector_pixels'],2)
        self.assertEqual(out[10,5],out[10,34]);self.assertEqual(audit['output_regions'],2)
        self.assertEqual(int(evidence['connector_mask'].sum()),2)
    def test_blank_gap_rejected_no_global_fallback(self):
        rgb,labels=line_control(False);out,audit,_=discover(rgb,labels)
        np.testing.assert_array_equal(out,labels);self.assertEqual(audit['accepted_bridges'],0)
        self.assertEqual(audit['status'],'UNCHANGED_NO_CONFIDENT_PROPOSAL')
    def test_determinism_and_input_immutability(self):
        rgb,labels=line_control();original=labels.copy();r1,a1,e1=discover(rgb,labels);r2,a2,e2=discover(rgb,labels)
        np.testing.assert_array_equal(labels,original);np.testing.assert_array_equal(r1,r2)
        self.assertEqual(a1['bridges'],a2['bridges']);np.testing.assert_array_equal(e1['connector_mask'],e2['connector_mask'])
    def test_parallel_offset_features_not_joined(self):
        rgb=np.full((24,40,3),255,np.uint8);labels=np.ones((24,40),np.uint32)
        rgb[8,4:15]=20;labels[8,4:15]=2;rgb[12,17:30]=20;labels[12,17:30]=3
        out,audit,_=discover(rgb,labels);self.assertEqual(audit['accepted_bridges'],0);np.testing.assert_array_equal(out,labels)
    def test_adjacent_tonal_regions_not_globally_merged(self):
        rgb=np.full((21,41,3),255,np.uint8);labels=np.ones((21,41),np.uint32)
        rgb[10,5:35]=20;labels[10,5:20]=2;labels[10,20:35]=3
        out,audit,_=discover(rgb,labels);self.assertEqual(audit['accepted_bridges'],0);np.testing.assert_array_equal(out,labels)
    def test_pair_budget_and_convex_mixture(self):
        rgb,labels=line_control();out,audit,_=discover(rgb,labels,{'max_endpoint_pairs':0})
        self.assertEqual(audit['endpoint_pairs_tested'],0);self.assertGreater(audit['endpoint_pairs_truncated'],0)
        np.testing.assert_array_equal(out,labels)
        _,audit,_=discover(rgb,labels)
        for bridge in audit['bridges']:
            self.assertGreaterEqual(bridge['min_mixture_fraction'],0);self.assertLessEqual(bridge['mean_mixture_fraction'],1)
```

### `TrackATests.test_supported_missing_label_connector` — `Lines 14–18`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `18` (`Lines 14–18`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 14–18`):**
```python
    def test_supported_missing_label_connector(self):
        rgb,labels=line_control();out,audit,evidence=discover(rgb,labels)
        self.assertEqual(audit['accepted_bridges'],1);self.assertEqual(audit['connector_pixels'],2)
        self.assertEqual(out[10,5],out[10,34]);self.assertEqual(audit['output_regions'],2)
        self.assertEqual(int(evidence['connector_mask'].sum()),2)
```

### `TrackATests.test_blank_gap_rejected_no_global_fallback` — `Lines 19–22`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `19` إلى السطر `22` (`Lines 19–22`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 19–22`):**
```python
    def test_blank_gap_rejected_no_global_fallback(self):
        rgb,labels=line_control(False);out,audit,_=discover(rgb,labels)
        np.testing.assert_array_equal(out,labels);self.assertEqual(audit['accepted_bridges'],0)
        self.assertEqual(audit['status'],'UNCHANGED_NO_CONFIDENT_PROPOSAL')
```

### `TrackATests.test_determinism_and_input_immutability` — `Lines 23–26`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `23` إلى السطر `26` (`Lines 23–26`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 23–26`):**
```python
    def test_determinism_and_input_immutability(self):
        rgb,labels=line_control();original=labels.copy();r1,a1,e1=discover(rgb,labels);r2,a2,e2=discover(rgb,labels)
        np.testing.assert_array_equal(labels,original);np.testing.assert_array_equal(r1,r2)
        self.assertEqual(a1['bridges'],a2['bridges']);np.testing.assert_array_equal(e1['connector_mask'],e2['connector_mask'])
```

### `TrackATests.test_parallel_offset_features_not_joined` — `Lines 27–30`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `27` إلى السطر `30` (`Lines 27–30`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 27–30`):**
```python
    def test_parallel_offset_features_not_joined(self):
        rgb=np.full((24,40,3),255,np.uint8);labels=np.ones((24,40),np.uint32)
        rgb[8,4:15]=20;labels[8,4:15]=2;rgb[12,17:30]=20;labels[12,17:30]=3
        out,audit,_=discover(rgb,labels);self.assertEqual(audit['accepted_bridges'],0);np.testing.assert_array_equal(out,labels)
```

### `TrackATests.test_adjacent_tonal_regions_not_globally_merged` — `Lines 31–34`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `31` إلى السطر `34` (`Lines 31–34`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 31–34`):**
```python
    def test_adjacent_tonal_regions_not_globally_merged(self):
        rgb=np.full((21,41,3),255,np.uint8);labels=np.ones((21,41),np.uint32)
        rgb[10,5:35]=20;labels[10,5:20]=2;labels[10,20:35]=3
        out,audit,_=discover(rgb,labels);self.assertEqual(audit['accepted_bridges'],0);np.testing.assert_array_equal(out,labels)
```

### `TrackATests.test_pair_budget_and_convex_mixture` — `Lines 35–41`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `35` إلى السطر `41` (`Lines 35–41`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 35–41`):**
```python
    def test_pair_budget_and_convex_mixture(self):
        rgb,labels=line_control();out,audit,_=discover(rgb,labels,{'max_endpoint_pairs':0})
        self.assertEqual(audit['endpoint_pairs_tested'],0);self.assertGreater(audit['endpoint_pairs_truncated'],0)
        np.testing.assert_array_equal(out,labels)
        _,audit,_=discover(rgb,labels)
        for bridge in audit['bridges']:
            self.assertGreaterEqual(bridge['min_mixture_fraction'],0);self.assertLessEqual(bridge['mean_mixture_fraction'],1)
```
