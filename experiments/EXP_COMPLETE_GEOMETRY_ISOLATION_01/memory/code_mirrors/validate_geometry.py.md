# مرآة الكود التفصيلية: `validate_geometry.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `validate_geometry.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `validate_geometry.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `97` (`Lines 1–97`)
- **بصمة الملف (`SHA-256`):** `afd2ce2e35ea0bdb78923a5b69827cabf0e7279aa5673a486511bb21b46a800b`
- **الوصف التفصيلي:** # START CHANGE AGD-ISOLATION-VALIDATE-GEOMETRY | 2026-10-29T06:48:34Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `mask_topology` | `function` | `Lines 15–18` | `def mask_topology(mask):` | رمز برمجي موثق. |
| `mask_boundary` | `function` | `Lines 20–23` | `def mask_boundary(mask,scale=8):` | رمز برمجي موثق. |
| `known_mask_evaluation` | `function` | `Lines 25–51` | `def known_mask_evaluation(case,g,labels,reference,out,name):` | رمز برمجي موثق. |
| `visible_microgeometry` | `function` | `Lines 53–69` | `def visible_microgeometry(g,labels):` | رمز برمجي موثق. |
| `run` | `function` | `Lines 71–93` | `def run():` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `mask_topology` — `Lines 15–18`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `15` إلى السطر `18` (`Lines 15–18`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 15–18`):**
```python
def mask_topology(mask):
    _,components=ndimage.label(mask)
    inv,n=ndimage.label(~mask);edge=np.unique(np.r_[inv[0],inv[-1],inv[:,0],inv[:,-1]])
    return {'components_4_connected':int(components),'holes_4_connected':int(n-len(set(edge)-{0}))}
```

### `mask_boundary` — `Lines 20–23`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `20` إلى السطر `23` (`Lines 20–23`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 20–23`):**
```python
def mask_boundary(mask,scale=8):
    boundary=mask & ~ndimage.binary_erosion(mask)
    y,x=np.nonzero(boundary)
    return np.column_stack([(x+.5)/scale,(y+.5)/scale])
```

### `known_mask_evaluation` — `Lines 25–51`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `25` إلى السطر `51` (`Lines 25–51`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 25–51`):**
```python
def known_mask_evaluation(case,g,labels,reference,out,name):
    rgb=np.asarray(Image.open(out/'working.png').convert('RGB')).astype(float)
    srcfg=np.linalg.norm(rgb-rgb[0,0],axis=-1)>8
    ids=np.unique(labels);foreground=[int(i) for i in ids if np.mean(srcfg[labels==i])>=.5]
    # Source-only majority correspondence is evaluator diagnostic, never used
    # for construction, fitting, region deletion or winner selection.
    svg=out/(name+'_foreground.svg');svg.write_text(svg_graph(g,regions=True,foreground=set(foreground)),encoding='utf-8')
    png=out/(name+'_foreground_8x.png')
    subprocess.run([str(RESVG),'--width',str(g['width']*8),'--height',str(g['height']*8),str(svg),str(png)],check=True,timeout=60,capture_output=True)
    pred=np.asarray(Image.open(png).convert('RGBA'))[...,3]>=128
    truth=np.asarray(Image.open(reference['local_only_mask_path']).convert('L'))>=128
    assert digest(reference['local_only_mask_path'])==reference['mask_sha256']
    raw=np.repeat(np.repeat(np.isin(labels,foreground),8,axis=0),8,axis=1)
    union=np.sum(pred|truth);inter=np.sum(pred&truth)
    dist=compare_samples(mask_boundary(truth),mask_boundary(pred))
    components=[]
    for item in reference['critical_known_components']:
        x0,y0,x1,y1=item['roi'];a=truth[y0*8:y1*8,x0*8:x1*8];b=pred[y0*8:y1*8,x0*8:x1*8]
        components.append({'id':item['id'],'foreground_area_recall':float(np.sum(a&b)/max(1,np.sum(a)))})
    Image.fromarray(np.stack([truth*255,pred*255,np.zeros_like(pred)],axis=-1).astype(np.uint8)).save(out/(name+'_known_error.png'))
    result={'foreground_region_ids':foreground,'foreground_correspondence':'Fixed source RGB corner-distance>8 majority per label; not evaluator geometry used for construction',
      'reference_mask_limit':'8x truth SVG threshold mask; <=.125px sampling plus renderer antialiasing, not exact analytic-contour certification',
      'foreground_iou':float(inter/max(1,union)),'raw_foreground_iou':float(np.sum(raw&truth)/max(1,np.sum(raw|truth))),
      'thin_foreground_area_recall':float(inter/max(1,np.sum(truth))),'predicted_topology':mask_topology(pred),'truth_topology':mask_topology(truth),
      'raw_topology':mask_topology(raw),'boundary':dist,'critical_components':components,
      'geometry_gate':'NOT_ACCEPTED' if inter/max(1,union)<.97 or inter/max(1,np.sum(truth))<.95 or mask_topology(pred)!=mask_topology(truth) or dist.get('symmetric_mean_px',999)>.45 or dist.get('symmetric_p95_px',999)>1.25 else 'SUPPORTED_BUT_LIMITED_SAMPLED_MASK_ONLY'}
    return result
```

### `visible_microgeometry` — `Lines 53–69`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `53` إلى السطر `69` (`Lines 53–69`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 53–69`):**
```python
def visible_microgeometry(g,labels):
    # Conservative region-area bound from unchanged source ownership. Separate
    # fitted bbox/contour test; no blanket ROI exemptions are applied.
    by_id={c['id']:c for c in g['chains']};records=[]
    for label,loops in g['faces'].items():
        pts=[]
        for refs in loops:
            for r in refs:pts.extend(chain_points(by_id[r['chain']]).tolist())
        p=np.asarray(pts);samples=np.concatenate([uniform_points(chain_points(by_id[r['chain']])) for loop in loops for r in loop])
        lattice=float(np.mean(np.min(np.abs(samples-np.round(samples)),axis=1)<=.01)) if len(samples) else 1.
        records.append({'label':int(label),'owned_source_pixels':int(np.sum(labels==int(label))),'span_px':np.ptp(p,axis=0).tolist(),'lattice_fraction':lattice})
    scales={}
    for scale in [1,2,4]:
        area=sum(r['owned_source_pixels'] for r in records if max(r['span_px'])<=scale and r['lattice_fraction']>=.8)
        scales[str(scale)]={'source_ownership_area_fraction':area/labels.size,'pixels':area}
    return {'scales_px':scales,'regions':records,'automatic_2px_alarm':scales['2']['source_ownership_area_fraction']>=.1,
      'limit':'Uses exact source-label owned area, not fitted overlap-occluded visible area. Conservative source-support diagnostic; visible-area gate remains NOT_ESTABLISHED on invalid fitted arrangements. No ROI blanket exemption.'}
```

### `run` — `Lines 71–93`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `71` إلى السطر `93` (`Lines 71–93`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 71–93`):**
```python
def run():
    reference=json.loads((ROOT/'references/shield_complete_boundary_reference.json').read_text())
    known={x['id']:x for x in json.loads((ROOT/'references/known_control_reference_manifest.json').read_text())['references']}
    rows=[]
    for case in CASES:
        out=case_dir(case)
        for seg in ['S_A','S_V']:
            labels=np.load(out/(seg+'.npy'),allow_pickle=False)
            common=json.loads((out/(seg+'_F_A.json')).read_text())
            for init in ['F_A','F_V']:
                name=seg+'_'+init;g=json.loads((out/(name+'.json')).read_text())
                normalized=normalize_to_common_faces(common,g)
                dump(out/(name+'_common_faces.json'),normalized)
                m=evaluate(normalized,reference if case=='A01_shield' else None)
                m['common_faces']=True;m['candidate_original_sha256']=digest(out/(name+'.json'))
                m['microgeometry']=visible_microgeometry(normalized,labels)
                if case in known:m['known_geometry']=known_mask_evaluation(case,normalized,labels,known[case],out,name)
                dump(out/(name+'_common_metrics.json'),m)
                row={'case':case,'condition':name,**{k:m[k] for k in ['chains','cubics','raw_nonzero_fit_degenerate_rings','invalid_fit_rings','invalid_raw_rings','max_junction_gap_px','shared_reference_failures','self_intersecting_chains','crossing_or_overlap_pairs','near_intersection_unresolved_pairs','geometry_acceptance','raw_to_fit']}}
                if 'known_geometry'in m:row['known_geometry']=m['known_geometry']
                rows.append(row);dump(ROOT/'reports/common_face_summary.json',rows)
                print(json.dumps(row),flush=True)
    return rows
```
