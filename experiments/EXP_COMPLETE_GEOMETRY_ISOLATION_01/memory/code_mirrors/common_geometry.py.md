# مرآة الكود التفصيلية: `common_geometry.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `common_geometry.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `common_geometry.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `35` (`Lines 1–35`)
- **بصمة الملف (`SHA-256`):** `ab9b9c2ed428c971068d5abd1650d62f2ddd54f5f88993f6f5036a977ad968bc`
- **الوصف التفصيلي:** # START CHANGE AGD-ISOLATION-COMMON-GEOMETRY | 2026-10-29T06:48:34Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `signature` | `function` | `Lines 6–9` | `def signature(ch):` | رمز برمجي موثق. |
| `normalize_to_common_faces` | `function` | `Lines 11–33` | `def normalize_to_common_faces(common,candidate):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `signature` — `Lines 6–9`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `6` إلى السطر `9` (`Lines 6–9`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 6–9`):**
```python
def signature(ch):
    pts=ch['pixel_crack_vertices']
    edges=frozenset(tuple(sorted((tuple(a),tuple(b)))) for a,b in zip(pts,pts[1:]))
    return tuple(sorted(ch['adjacent_face_labels'])),edges
```

### `normalize_to_common_faces` — `Lines 11–33`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `11` إلى السطر `33` (`Lines 11–33`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 11–33`):**
```python
def normalize_to_common_faces(common,candidate):
    lookup={signature(c):c for c in candidate['chains']}
    if len(lookup)!=len(candidate['chains']):raise ValueError('Ambiguous chain edge signatures')
    obj=copy.deepcopy(common);maps=[]
    for chain in obj['chains']:
        native=lookup.pop(signature(chain))
        a=chain['pixel_crack_vertices'];b=native['pixel_crack_vertices']
        directed_a={(tuple(x),tuple(y)) for x,y in zip(a,a[1:])}
        directed_b={(tuple(x),tuple(y)) for x,y in zip(b,b[1:])}
        same=directed_a==directed_b
        if not same and directed_a!={(y,x) for x,y in directed_b}:raise ValueError('Inconsistent raw orientation')
        seg=copy.deepcopy(native['segments'])
        if not same:
            seg=seg[::-1]
            for s in seg:
                s['p0'],s['p3']=s['p3'],s['p0']
                if s['type']=='C':s['p1'],s['p2']=s['p2'],s['p1']
        chain['segments']=seg
        chain['closed']=native.get('closed',False)
        maps.append({'common_chain':chain['id'],'native_chain':native['id'],'reversed':not same})
    if lookup:raise ValueError('Extra native geometry')
    obj['normalization']={'policy':'Common raw Arena face references, exact unit-edge chain matching, native curve reversal only; coordinates/control points unchanged','chain_mapping':maps}
    return obj
```
