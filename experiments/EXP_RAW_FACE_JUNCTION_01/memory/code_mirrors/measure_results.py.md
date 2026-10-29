# مرآة الكود التفصيلية: `measure_results.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `measure_results.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `measure_results.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `53` (`Lines 1–53`)
- **بصمة الملف (`SHA-256`):** `b9aedfd0f47508de15d01f4a7870033079973493e94a5df3b20047cb79a58ae4`
- **الوصف التفصيلي:** # START CHANGE AGD-RAWFACE-MEASURE-RESULTS | 2026-10-29T12:39:51Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `measure` | `function` | `Lines 14–49` | `def measure():` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `measure` — `Lines 14–49`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `49` (`Lines 14–49`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 14–49`):**
```python
def measure():
    summary=[];cases=json.loads((ROOT/'protocol.json').read_text(encoding='utf-8'))['cases']
    for case in cases:
        out=destination(case);original=json.loads((out/'O.json').read_text(encoding='utf-8'))
        audit=json.loads((out/'R_audit.json').read_text(encoding='utf-8'));labels=np.load(out/'labels.npy',allow_pickle=False)
        junctions=[];lookup={c['id']:c for c in original['chains']}
        for row in audit['mapping']:
            if not row['splits']:continue
            refs=original['faces'][row['face']][row['original_ring']];starts=[]
            for ref in refs:
                p=lookup[ref['chain']]['pixel_crack_vertices'];starts.append(tuple(p[0] if ref['forward'] else p[-1]))
            for p,n in collections.Counter(starts).items():
                if n<2:continue
                x,y=map(int,p);block=labels[max(0,y-1):min(labels.shape[0],y+1),max(0,x-1):min(labels.shape[1],x+1)]
                junctions.append({'face':row['face'],'ring':row['original_ring'],'xy':list(p),'visits':n,'pixel_neighborhood_2x2':block.tolist(),'note':'Diagonal/pinched contact evidence, not semantic object connectivity.'})
        dump(out/'JUNCTION_DIAGNOSTICS.json',junctions)
        for name in ['O','R','B','RB']:
            if not (out/(name+'.json')).exists():continue
            shutil.copy2(out/'labels.npy',out/(name+'_labels.npy'))
            m=inherited.evaluate_candidate(case,name)
            raw_valid=sum(x['raw_valid_ring'] for x in m['rings']);fitted_valid=sum(x['fit_valid_ring'] for x in m['rings'])
            row={k:m.get(k) for k in ['case','condition','chains','cubics','invalid_raw_rings','invalid_fit_rings','raw_nonzero_fit_degenerate_rings','crossing_or_overlap_pairs','shared_reference_failures','max_junction_gap_px','near_intersection_unresolved_pairs','self_intersecting_chains','geometry_acceptance','raw_to_fit','known_geometry','arabic_source_proxy','critical_component_diagnostics','coverage','visible_microgeometry','render_wall_seconds']}
            row.update(ring_count=len(m['rings']),raw_valid_rings=raw_valid,fitted_valid_rings=fitted_valid)
            summary.append(row)
        # Probe evaluation is separate, consumes maps only after their immutable generation.
        maps=np.load(out/'source_probe/source_evidence.npz',allow_pickle=False);edge=maps['persistent_edges'];ys,xs=np.nonzero(edge);points=np.c_[xs+.5,ys+.5]
        lines=[LineString(chain_points(c,True)) for c in original['chains']];tree=STRtree(lines)
        distances=np.array([Point(p).distance(lines[int(tree.nearest(Point(p)))]) for p in points])
        absent=np.zeros(edge.shape,bool)
        if len(distances):absent[ys[distances>2],xs[distances>2]]=True
        np.save(out/'source_probe/edge_evidence_farther_than_2px.npy',absent)
        rgb=np.asarray(Image.open(out/'working.png').convert('RGB'));overlay=rgb.copy();overlay[edge]=(0,180,255);overlay[absent]=(255,0,180);Image.fromarray(overlay).save(out/'source_probe/evidence_vs_raw_overlay.png')
        md=json.loads((out/'source_probe/source_evidence.json').read_text(encoding='utf-8'))
        dump(out/'source_probe/EVALUATION_ONLY.json',{'persistent_edge_pixels':int(edge.sum()),'persistent_edge_fraction':md['persistent_edge_fraction'],'farther_than_2px_from_raw_cracks':int(absent.sum()),'fraction_of_evidence_farther_than_2px':float(absent.sum()/max(1,edge.sum())),'coordinate_convention':'Raster element[y,x] at geometric(x+.5,y+.5); raw pixel cracks use integer corners. Distance to complete raw line segments using Shapely doubles.','clutter_warning':md['clutter_warning'],'interpretation':'Unrepresented source contrast, not verified missing structural geometry. Texture, AA, illumination and noise can contribute. No discovered region, stroke or component claim.'})
        dump(ROOT/'reports/SUMMARY.json',summary)
        print(case,'measured',flush=True)
```
