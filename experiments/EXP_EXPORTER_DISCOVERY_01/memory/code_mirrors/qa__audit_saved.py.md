# مرآة الكود التفصيلية: `qa/audit_saved.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `qa/audit_saved.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `qa/audit_saved.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `76` (`Lines 1–76`)
- **بصمة الملف (`SHA-256`):** `5194ce0899f5b68657c7d9b963868f06a24e970d3e2906c9cd6f154f5e62cec8`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `load` | `function` | `Lines 12–12` | `def load(p):return json.loads(Path(p).read_text(encoding='utf-8'))` | رمز برمجي موثق. |
| `directed` | `function` | `Lines 13–13` | `def directed(g):return {f:collections.Counter((r['chain'],r['forward']) for ring in loops for r in ring) for f,loops in g['faces'].items()}` | رمز برمجي موثق. |
| `cross` | `function` | `Lines 14–14` | `def cross(a,b):return float(a[0]*b[1]-a[1]*b[0])` | رمز برمجي موثق. |
| `open_area` | `function` | `Lines 15–15` | `def open_area(points):return .5*sum(cross(a,b) for a,b in zip(points[:-1],points[1:]))` | رمز برمجي موثق. |
| `curve_area` | `function` | `Lines 17–22` | `def curve_area(s):` | رمز برمجي موثق. |
| `collapsed` | `function` | `Lines 23–38` | `def collapsed(g):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `load` — `Lines 12–12`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `12` إلى السطر `12` (`Lines 12–12`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 12–12`):**
```python
def load(p):return json.loads(Path(p).read_text(encoding='utf-8'))
```

### `directed` — `Lines 13–13`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `13` (`Lines 13–13`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 13–13`):**
```python
def directed(g):return {f:collections.Counter((r['chain'],r['forward']) for ring in loops for r in ring) for f,loops in g['faces'].items()}
```

### `cross` — `Lines 14–14`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `14` (`Lines 14–14`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 14–14`):**
```python
def cross(a,b):return float(a[0]*b[1]-a[1]*b[0])
```

### `open_area` — `Lines 15–15`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `15` إلى السطر `15` (`Lines 15–15`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 15–15`):**
```python
def open_area(points):return .5*sum(cross(a,b) for a,b in zip(points[:-1],points[1:]))
```

### `curve_area` — `Lines 17–22`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `17` إلى السطر `22` (`Lines 17–22`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 17–22`):**
```python
def curve_area(s):
    if s['type']=='L':return cross(s['p0'],s['p3'])/2
    a,b,c,d=[np.asarray(s[k]) for k in ('p0','p1','p2','p3')];u=t[:,None]
    p=(1-u)**3*a+3*(1-u)**2*u*b+3*(1-u)*u*u*c+u**3*d
    v=3*((1-u)**2*(b-a)+2*(1-u)*u*(c-b)+u*u*(d-c))
    return float(np.sum(weights*(p[:,0]*v[:,1]-p[:,1]*v[:,0]))/2)
```

### `collapsed` — `Lines 23–38`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `23` إلى السطر `38` (`Lines 23–38`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 23–38`):**
```python
def collapsed(g):
    lookup={c['id']:c for c in g['chains']};total=0;rings=0
    for face,loops in g['faces'].items():
        if int(face)==0:continue
        for refs in loops:
            rawarea=fitarea=0.;rings+=1
            for ref in refs:
                c=lookup[ref['chain']];sign=1 if ref['forward'] else -1
                pts=c['pixel_crack_vertices'];rv=open_area(pts)
                if c.get('closed'):rv+=cross(pts[-1],pts[0])/2
                rawarea+=sign*rv
                value=sum(curve_area(s) for s in c['segments'])
                if c.get('closed') and c['segments']:value+=cross(c['segments'][-1]['p3'],c['segments'][0]['p0'])/2
                fitarea+=sign*value
            total+=abs(rawarea)>1e-6 and abs(fitarea)<=1e-6
    return {'rings':rings,'raw_nonzero_fit_zero':int(total)}
```
