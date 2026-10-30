# مرآة الكود التفصيلية: `qa/audit_masks.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `qa/audit_masks.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `qa/audit_masks.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `36` (`Lines 1–36`)
- **بصمة الملف (`SHA-256`):** `d142c534c8e95b0412d11c6af78e85cc3c9cea3f740287c4d41def9d001dd5ff`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `topo` | `function` | `Lines 11–14` | `def topo(mask):` | رمز برمجي موثق. |
| `stats` | `function` | `Lines 15–16` | `def stats(truth,pred):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `topo` — `Lines 11–14`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `11` إلى السطر `14` (`Lines 11–14`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 11–14`):**
```python
def topo(mask):
    components=ndi.label(mask)[1]
    holes=ndi.label(ndi.binary_fill_holes(mask)&~mask)[1]
    return {'components_4_connected':int(components),'holes_4_connected':int(holes)}
```

### `stats` — `Lines 15–16`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `15` إلى السطر `16` (`Lines 15–16`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 15–16`):**
```python
def stats(truth,pred):
    return {'iou':float((truth&pred).sum()/(truth|pred).sum()),'pred_topology':topo(pred),'truth_topology':topo(truth)}
```
