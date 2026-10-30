# مرآة الكود التفصيلية: `qa/audit_intersections.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `qa/audit_intersections.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `qa/audit_intersections.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `38` (`Lines 1–38`)
- **بصمة الملف (`SHA-256`):** `8ba5cf7eb1d8d90902279302aaa3638f7ed847d2d0cb17daa5b0557ed7dd7d53`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `line` | `function` | `Lines 11–21` | `def line(chain):` | رمز برمجي موثق. |
| `defects` | `function` | `Lines 22–28` | `def defects(g):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `line` — `Lines 11–21`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `11` إلى السطر `21` (`Lines 11–21`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 11–21`):**
```python
def line(chain):
    out=[];u=np.linspace(0,1,129)[:,None]
    for seg in chain['segments']:
        if seg['type']=='L':p=np.asarray([seg['p0'],seg['p3']],float)
        else:
            a,b,c,d=[np.asarray(seg[k]) for k in ('p0','p1','p2','p3')]
            p=(1-u)**3*a+3*(1-u)**2*u*b+3*(1-u)*u*u*c+u**3*d
            p[0]=a;p[-1]=d
        out.extend(p if not out else p[1:])
    if chain.get('closed') and np.linalg.norm(np.asarray(out[-1])-out[0])>0:out.append(out[0])
    return LineString(out)
```

### `defects` — `Lines 22–28`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `22` إلى السطر `28` (`Lines 22–28`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 22–28`):**
```python
def defects(g):
    ids=[c['id'] for c in g['chains']];lines=[line(c) for c in g['chains']];tree=STRtree(lines);pairs=set()
    for i,a in enumerate(lines):
        for j in tree.query(a):
            j=int(j)
            if j>i and (a.crosses(lines[j]) or a.overlaps(lines[j])):pairs.add(tuple(sorted((ids[i],ids[j]))))
    return pairs
```
