# مرآة الكود التفصيلية: `src/test_refine.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `src/test_refine.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `src/test_refine.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `26` (`Lines 1–26`)
- **بصمة الملف (`SHA-256`):** `3b83f7d50c5e4bed9b019bc4bc58474adc0c853cbafe888e6f71ed6fdc443ea6`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `RefitTests` | `class` | `Lines 9–22` | `class RefitTests(unittest.TestCase):` | رمز برمجي موثق. |
| `RefitTests.test_visible_support_refit_exact_on_overlapping_flat_regions` | `method` | `Lines 10–18` | `def test_visible_support_refit_exact_on_overlapping_flat_regions(self):` | رمز برمجي موثق. |
| `RefitTests.test_refuses_spline_and_opacity` | `method` | `Lines 19–22` | `def test_refuses_spline_and_opacity(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `RefitTests` — `Lines 9–22`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `22` (`Lines 9–22`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–22`):**
```python
class RefitTests(unittest.TestCase):
    def test_visible_support_refit_exact_on_overlapping_flat_regions(self):
        with tempfile.TemporaryDirectory() as directory:
            d=Path(directory);a=np.zeros((16,16,3),np.uint8);a[:]=[200,40,20];a[4:12,4:12]=[20,180,40];Image.fromarray(a).save(d/'source.png')
            svg=f'<svg xmlns="{NS}" width="16" height="16"><path d="M0 0 L16 0 L16 16 L0 16 Z" fill="#808080"/><path d="M4 4 L12 4 L12 12 L4 12 Z" fill="#000000"/></svg>'
            (d/'source.svg').write_text(svg);r=refine(d/'source.png',d/'source.svg',{'mode':'pixel'},d/'out')
            self.assertTrue(r['conditions']['visible_color_refit']['metrics']['identical'])
            self.assertEqual(r['ownership_audit']['ambiguous_pixels'],0)
            original=ET.fromstring(svg);refitted=ET.parse(d/'out/visible_color_refit.svg').getroot()
            self.assertEqual([p.get('d') for p in original],[p.get('d') for p in refitted])
    def test_refuses_spline_and_opacity(self):
        root=ET.fromstring(f'<svg xmlns="{NS}"><path d="M0 0L1 0L1 1Z" fill="#123456" opacity=".5"/></svg>')
        with self.assertRaises(ValueError):inspect_pixel_document(root,{'mode':'spline'})
        with self.assertRaises(ValueError):inspect_pixel_document(root,{'mode':'pixel'})
```

### `RefitTests.test_visible_support_refit_exact_on_overlapping_flat_regions` — `Lines 10–18`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `10` إلى السطر `18` (`Lines 10–18`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 10–18`):**
```python
    def test_visible_support_refit_exact_on_overlapping_flat_regions(self):
        with tempfile.TemporaryDirectory() as directory:
            d=Path(directory);a=np.zeros((16,16,3),np.uint8);a[:]=[200,40,20];a[4:12,4:12]=[20,180,40];Image.fromarray(a).save(d/'source.png')
            svg=f'<svg xmlns="{NS}" width="16" height="16"><path d="M0 0 L16 0 L16 16 L0 16 Z" fill="#808080"/><path d="M4 4 L12 4 L12 12 L4 12 Z" fill="#000000"/></svg>'
            (d/'source.svg').write_text(svg);r=refine(d/'source.png',d/'source.svg',{'mode':'pixel'},d/'out')
            self.assertTrue(r['conditions']['visible_color_refit']['metrics']['identical'])
            self.assertEqual(r['ownership_audit']['ambiguous_pixels'],0)
            original=ET.fromstring(svg);refitted=ET.parse(d/'out/visible_color_refit.svg').getroot()
            self.assertEqual([p.get('d') for p in original],[p.get('d') for p in refitted])
```

### `RefitTests.test_refuses_spline_and_opacity` — `Lines 19–22`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `19` إلى السطر `22` (`Lines 19–22`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 19–22`):**
```python
    def test_refuses_spline_and_opacity(self):
        root=ET.fromstring(f'<svg xmlns="{NS}"><path d="M0 0L1 0L1 1Z" fill="#123456" opacity=".5"/></svg>')
        with self.assertRaises(ValueError):inspect_pixel_document(root,{'mode':'spline'})
        with self.assertRaises(ValueError):inspect_pixel_document(root,{'mode':'pixel'})
```
