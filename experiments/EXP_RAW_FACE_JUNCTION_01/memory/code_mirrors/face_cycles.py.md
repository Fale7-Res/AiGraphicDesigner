# مرآة الكود التفصيلية: `face_cycles.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `face_cycles.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `face_cycles.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `62` (`Lines 1–62`)
- **بصمة الملف (`SHA-256`):** `26ff3fd76bb5401b367aaa569f3ecfb2996c489fe4474e81648cafb63bbae6b4`
- **الوصف التفصيلي:** # START CHANGE AGD-RAWFACE-FACE-CYCLES | 2026-10-29T12:20:15Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `directed_occurrences` | `function` | `Lines 9–10` | `def directed_occurrences(faces):` | رمز برمجي موثق. |
| `split_closed_walk` | `function` | `Lines 12–32` | `def split_closed_walk(refs,raw,max_splits=8192):` | Partition only at exact repeated chain endpoints; retain every occurrence. |
| `decompose` | `function` | `Lines 34–60` | `def decompose(graph):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `directed_occurrences` — `Lines 9–10`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `10` (`Lines 9–10`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–10`):**
```python
def directed_occurrences(faces):
    return {str(face):collections.Counter((int(ref['chain']),bool(ref['forward'])) for ring in rings for ref in ring) for face,rings in faces.items()}
```

### `split_closed_walk` — `Lines 12–32`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `12` إلى السطر `32` (`Lines 12–32`)
- **الوظيفة:** Partition only at exact repeated chain endpoints; retain every occurrence.
- **الكود الفعلي (`Lines 12–32`):**
```python
def split_closed_walk(refs,raw,max_splits=8192):
    """Partition only at exact repeated chain endpoints; retain every occurrence."""
    pending=[copy.deepcopy(refs)];result=[];splits=0
    while pending:
        walk=pending.pop();nodes=[];ends=[]
        if not walk:raise ValueError('Empty walk cannot be silently deleted')
        for ref in walk:
            p=raw[ref['chain']];p=p if ref['forward'] else p[::-1]
            if len(p)<2:raise ValueError('Unsupported raw chain')
            nodes.append(tuple(p[0]));ends.append(tuple(p[-1]))
        if any(ends[i]!=nodes[(i+1)%len(nodes)] for i in range(len(nodes))):raise ValueError('Open endpoint walk')
        seen={};cut=None
        for j,node in enumerate(nodes):
            if node in seen:cut=(seen[node],j);break
            seen[node]=j
        if cut is None:result.append(walk);continue
        i,j=cut;splits+=1
        if splits>max_splits:raise ValueError('Frozen split budget exceeded')
        # Two closed walks, no geometry inserted, removed, reordered internally.
        pending.extend([walk[:i]+walk[j:],walk[i:j]])
    return result,splits
```

### `decompose` — `Lines 34–60`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `34` إلى السطر `60` (`Lines 34–60`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 34–60`):**
```python
def decompose(graph):
    original=copy.deepcopy(graph);result=copy.deepcopy(graph)
    raw={c['id']:chain_points(c,True) for c in graph['chains']}
    mapping=[];rejections=[];splits_total=0
    for face,rings in graph['faces'].items():
        new=[]
        for ri,refs in enumerate(rings):
            start=len(new);pts,gap=ring_points(refs,raw);before=Polygon(pts)
            try:
                pieces,splits=split_closed_walk(refs,raw,8192-splits_total)
                sums=sum(signed_area(ring_points(x,raw)[0]) for x in pieces)
                if abs(sums-signed_area(pts))>1e-9:raise ValueError('Signed area changed')
                if collections.Counter((x['chain'],x['forward']) for x in refs)!=collections.Counter((x['chain'],x['forward']) for q in pieces for x in q):raise ValueError('Directed occurrences changed')
            except ValueError as exc:
                pieces=[copy.deepcopy(refs)];splits=0;rejections.append({'face':face,'ring':ri,'reason':str(exc)})
            new.extend(pieces);splits_total+=splits
            records=[]
            for part in pieces:
                p,g=ring_points(part,raw);poly=Polygon(p)
                records.append({'raw_signed_area':signed_area(p),'raw_valid':bool(poly.is_valid and abs(signed_area(p))>1e-6 and g<=.001),'reason':explain_validity(poly),'refs':len(part)})
            mapping.append({'face':face,'original_ring':ri,'new_ring_indices':list(range(start,len(new))),'raw_area_before':signed_area(pts),'raw_valid_before':bool(before.is_valid and abs(signed_area(pts))>1e-6 and gap<=.001),'validity_reason_before':explain_validity(before),'splits':splits,'parts':records})
        result['faces'][face]=new
    assert result['chains']==original['chains']
    assert directed_occurrences(original['faces'])==directed_occurrences(result['faces'])
    assert {k:v for k,v in result.items() if k!='faces'}=={k:v for k,v in original.items() if k!='faces'}
    audit={'method':'exact repeated chain-endpoint walk decomposition','mapping':mapping,'splits':splits_total,'rejections':rejections,'all_non_face_fields_unchanged':True,'directed_occurrences_unchanged':True,'geometry_moved':False,'labels_changed':False,'limitations':['Point contacts remain physical point contacts; no connectivity repair','Simple rings are not a globally valid filled MultiPolygon proof','No raw internal-chain splitting or pruning of zero-area cycles','Ring count denominators change; do not infer completeness from counts']}
    return result,audit
```
