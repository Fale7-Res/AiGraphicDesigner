# مرآة الكود التفصيلية: `qa/check_saved_svg_semantics.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `qa/check_saved_svg_semantics.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `qa/check_saved_svg_semantics.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `57` (`Lines 1–57`)
- **بصمة الملف (`SHA-256`):** `3d4655b40a33243ae600989897952c92f233ab02849d70a9681e95fa6de1244e`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `interp` | `function` | `Lines 9–19` | `def interp(data):` | رمز برمجي موثق. |
| `expected` | `function` | `Lines 20–30` | `def expected(chain,raw,forward):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `interp` — `Lines 9–19`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `19` (`Lines 9–19`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–19`):**
```python
def interp(data):
    pen=RecordingPen();parse_path(data,pen);p=o=None;segments=[]
    for cmd,args in pen.value:
        if cmd=='moveTo':p=o=args[0]
        elif cmd=='lineTo':segments.append(('L',p,args[0]));p=args[0]
        elif cmd=='curveTo':segments.append(('C',p,*args));p=args[-1]
        elif cmd=='closePath':
            if p!=o:segments.append(('L',p,o))
            p=o
        elif cmd!='endPath':raise AssertionError(cmd)
    return segments
```

### `expected` — `Lines 20–30`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `20` إلى السطر `30` (`Lines 20–30`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 20–30`):**
```python
def expected(chain,raw,forward):
    if raw:
        pts=list(map(tuple,chain['pixel_crack_vertices']));out=[('L',a,b) for a,b in zip(pts[:-1],pts[1:])]
    else:
        out=[]
        for s in chain['segments']:
            keys=('p0','p1','p2','p3') if s['type']=='C' else ('p0','p3')
            out.append((s['type'],*(tuple(s[k]) for k in keys)))
    if chain.get('closed') and out[-1][-1]!=out[0][1]:out.append(('L',out[-1][-1],out[0][1]))
    if not forward:out=[(s[0],*reversed(s[1:])) for s in reversed(out)]
    return out
```
