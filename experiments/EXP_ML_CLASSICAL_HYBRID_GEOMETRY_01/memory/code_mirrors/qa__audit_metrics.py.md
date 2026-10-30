# مرآة الكود التفصيلية: `qa/audit_metrics.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `qa/audit_metrics.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `qa/audit_metrics.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `67` (`Lines 1–67`)
- **بصمة الملف (`SHA-256`):** `01cc30dff4a04114a4a8685346a550a992dafbca1febfb600aad9287bcedd191`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `dists` | `function` | `Lines 10–12` | `def dists(a,b):` | رمز برمجي موثق. |
| `sample` | `function` | `Lines 13–18` | `def sample(p):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `dists` — `Lines 10–12`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `10` إلى السطر `12` (`Lines 10–12`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 10–12`):**
```python
def dists(a,b):
    if not len(b):return np.full(len(a),np.inf)
    return np.concatenate([cdist(a[i:i+64],b).min(axis=1) for i in range(0,len(a),64)])
```

### `sample` — `Lines 13–18`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `18` (`Lines 13–18`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 13–18`):**
```python
def sample(p):
    output=[]
    for a,b in zip(p[:-1],p[1:]):
        n=max(1,math.ceil(float(np.linalg.norm(b-a))/.25))
        output.extend(a+(b-a)*i/n for i in range(n))
    return np.array(output+[p[-1]])
```
