# مرآة الكود التفصيلية: `analyze_matrix.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `analyze_matrix.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `analyze_matrix.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `90` (`Lines 1–90`)
- **بصمة الملف (`SHA-256`):** `cae247ade1c982631705dcee5914aa853bd57f12db621e6f071e3fd08503bf3e`
- **الوصف التفصيلي:** # START CHANGE AGD-ISOLATION-ANALYZE-MATRIX | 2026-10-29T06:48:34Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `render` | `function` | `Lines 15–18` | `def render(svg,png):` | رمز برمجي موثق. |
| `edge_dictionary` | `function` | `Lines 20–29` | `def edge_dictionary(g):` | رمز برمجي موثق. |
| `region_center_check` | `function` | `Lines 31–37` | `def region_center_check(svg,labels,target):` | رمز برمجي موثق. |
| `analyze` | `function` | `Lines 39–86` | `def analyze():` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `render` — `Lines 15–18`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `15` إلى السطر `18` (`Lines 15–18`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 15–18`):**
```python
def render(svg,png):
    t=time.monotonic();p=subprocess.run([str(RESVG),str(svg),str(png)],capture_output=True,timeout=60)
    if p.returncode:raise RuntimeError(p.stderr.decode(errors='replace'))
    return time.monotonic()-t
```

### `edge_dictionary` — `Lines 20–29`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `20` إلى السطر `29` (`Lines 20–29`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 20–29`):**
```python
def edge_dictionary(g):
    edges={}
    for ch in g['chains']:
        pair=tuple(sorted(ch['adjacent_face_labels']))
        pts=ch['pixel_crack_vertices']
        for a,b in zip(pts,pts[1:]):
            key=tuple(sorted((tuple(a),tuple(b))))
            if key in edges:raise ValueError('Duplicate raw crack')
            edges[key]=pair
    return edges
```

### `region_center_check` — `Lines 31–37`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `31` إلى السطر `37` (`Lines 31–37`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 31–37`):**
```python
def region_center_check(svg,labels,target):
    # Native raw polygon SVG covers exactly pixel squares: color at centers must
    # equal deterministic label paint; no antialias boundary samples are used.
    render(svg,target);rgb=np.asarray(Image.open(target).convert('RGB'))
    expected=np.stack([labels*97%200+30,labels*57%200+30,labels*137%200+30],axis=-1).astype(np.uint8)
    wrong=np.any(rgb!=expected,axis=-1)
    return {'pixels_wrong_region_id_color':int(wrong.sum()),'pixels':int(wrong.size)}
```

### `analyze` — `Lines 39–86`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `39` إلى السطر `86` (`Lines 39–86`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 39–86`):**
```python
def analyze():
    ref=json.loads((ROOT/'references/shield_complete_boundary_reference.json').read_text())
    freeze=json.loads((ROOT/'references/FREEZE.json').read_text())
    for path,data in freeze['files'].items():assert digest(ROOT/'references'/path)==data['sha256']
    rows=[];integrity=[]
    for case in CASES:
        out=case_dir(case);w,h=Image.open(out/'working.png').size
        for seg in ['S_A','S_V']:
            labels=np.load(out/(seg+'.npy'),allow_pickle=False)
            a=json.loads((out/(seg+'_F_A.json')).read_text());v=json.loads((out/(seg+'_F_V.json')).read_text())
            assert a['labels_sha256']==v['labels_sha256']==digest(out/(seg+'.npy'))
            ea=edge_dictionary(a);ev=edge_dictionary(v)
            match=ea==ev
            checks={}
            for init,g in [('F_A',a),('F_V',v)]:
                rawsvg=out/(seg+'_'+init+'_raw_regions.svg');rawsvg.write_text(svg_graph(g,raw=True,regions=True),encoding='utf-8')
                checks[init]=region_center_check(rawsvg,labels,out/(seg+'_'+init+'_raw_regions.png'))
            integrity.append({'case':case,'segmentation':seg,'labels_sha256':digest(out/(seg+'.npy')),
                'exact_raw_unit_edge_and_adjacency_match':match,'raw_region_fill_checks':checks,
                'raw_edges_A':len(ea),'raw_edges_V':len(ev),'graph_equivalence':match and all(x['pixels_wrong_region_id_color']==0 for x in checks.values())})
            rgb=np.stack([labels*97%200+30,labels*57%200+30,labels*137%200+30],axis=-1).astype(np.uint8)
            Image.fromarray(rgb).save(out/(seg+'_labels.png'))
            for init,g in [('F_A',a),('F_V',v)]:
                name=seg+'_'+init;start=time.monotonic()
                metrics=evaluate(g,ref if case=='A01_shield' else None)
                metrics['analysis_wall_seconds']=time.monotonic()-start
                metrics['case']=case;metrics['condition']=name
                metrics['candidate_sha256']=digest(out/(name+'.json'))
                metrics['regions']=int(np.unique(labels).size)
                metrics['raw_graph_equivalence']=integrity[-1]['graph_equivalence']
                renders={}
                for suffix,raw,regions in [('curves',False,False),('raw',True,False),('regions',False,True)]:
                    svg=out/(name+'_'+suffix+'.svg');svg.write_text(svg_graph(g,raw=raw,regions=regions),encoding='utf-8')
                    renders[suffix]=render(svg,out/(name+'_'+suffix+'.png'))
                # True vector viewport renders, never enlarged PNG evidence.
                import xml.etree.ElementTree as ET
                tree=ET.fromstring((out/(name+'_curves.svg')).read_text())
                x,y,cw,ch=ZOOMS[case];cw=min(cw,w-x);ch=min(ch,h-y)
                for scale in [1,4,16]:
                    tree.set('viewBox',f'{x} {y} {cw} {ch}');tree.set('width',str(cw*scale));tree.set('height',str(ch*scale))
                    path=out/(name+f'_detail_{scale}x.svg');path.write_text(ET.tostring(tree,encoding='unicode'),encoding='utf-8')
                    renders[f'detail_{scale}x']=render(path,path.with_suffix('.png'))
                metrics['render_wall_seconds']=renders
                dump(out/(name+'_metrics.json'),metrics)
                brief={k:metrics[k] for k in ['case','condition','regions','chains','cubics','raw_nonzero_fit_degenerate_rings','invalid_fit_rings','invalid_raw_rings','max_junction_gap_px','shared_reference_failures','self_intersecting_chains','crossing_or_overlap_pairs','unexpected_endpoint_interior_touches','near_intersection_unresolved_pairs','ring_area_weighted_tiny_lattice_fraction','geometry_acceptance','raw_graph_equivalence','raw_to_fit']}
                rows.append(brief);dump(ROOT/'reports/metrics_summary.json',rows);dump(ROOT/'reports/graph_integrity.json',integrity)
                print(json.dumps(brief),flush=True)
    return rows
```
