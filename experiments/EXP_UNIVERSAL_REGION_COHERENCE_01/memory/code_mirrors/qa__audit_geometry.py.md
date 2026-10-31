# مرآة الكود التفصيلية: `qa/audit_geometry.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `qa/audit_geometry.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `qa/audit_geometry.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `68` (`Lines 1–68`)
- **بصمة الملف (`SHA-256`):** `50bdf49ca1fb07c8facf67c58cb07ecd4fe6d3c12eb77ca679ec4a5171de8834`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `dense` | `function` | `Lines 17–20` | `def dense(cc):` | رمز برمجي موثق. |
| `sampled_source` | `function` | `Lines 22–27` | `def sampled_source(p):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `dense` — `Lines 17–20`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `17` إلى السطر `20` (`Lines 17–20`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 17–20`):**
```python
def dense(cc):
    u=np.linspace(0.,1.,129)[:,None]
    pieces=[(1-u)**3*c[0]+3*(1-u)**2*u*c[1]+3*(1-u)*u*u*c[2]+u**3*c[3] for c in np.asarray(cc)]
    return np.concatenate([p[:-1] for p in pieces]+[pieces[-1][-1:]])
```

### `sampled_source` — `Lines 22–27`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `22` إلى السطر `27` (`Lines 22–27`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 22–27`):**
```python
def sampled_source(p):
    out=[]
    for a,b in zip(p,p[1:]):
        count=max(1,int(np.ceil(np.linalg.norm(b-a)/.05)))
        out.extend(a+(b-a)*np.arange(count)[:,None]/count)
    return np.asarray(out+[p[-1]])
```
