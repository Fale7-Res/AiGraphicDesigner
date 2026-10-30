# مرآة الكود التفصيلية: `evaluate_results.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `evaluate_results.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `evaluate_results.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `98` (`Lines 1–98`)
- **بصمة الملف (`SHA-256`):** `02f006773e45225d12acc2854fed434ee562bd92fb93bbaffdc170a7479ae85d`
- **الوصف التفصيلي:** # START CHANGE AGD-ML-PACKAGE | 2026-10-30T08:17:45Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `support_stats` | `function` | `Lines 17–20` | `def support_stats(target,pred,tolerance):` | رمز برمجي موثق. |
| `xy` | `function` | `Lines 22–22` | `def xy(mask):return np.argwhere(mask)[:,::-1].astype(float)+.5` | رمز برمجي موثق. |
| `samples_from_items` | `function` | `Lines 24–29` | `def samples_from_items(items):` | رمز برمجي موثق. |
| `render` | `function` | `Lines 31–33` | `def render(svg,png,w,h,scale):` | رمز برمجي موثق. |
| `evaluate` | `function` | `Lines 35–89` | `def evaluate(case):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `support_stats` — `Lines 17–20`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `17` إلى السطر `20` (`Lines 17–20`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 17–20`):**
```python
def support_stats(target,pred,tolerance):
    if not len(target) or not len(pred):return {'recall':0.,'precision':0.,'mean_target_distance_px':None,'p95_target_distance_px':None}
    a=cKDTree(pred).query(target)[0];b=cKDTree(target).query(pred)[0]
    return {'recall':float(np.mean(a<=tolerance)),'precision':float(np.mean(b<=tolerance)),'mean_target_distance_px':float(a.mean()),'p95_target_distance_px':float(np.percentile(a,95))}
```

### `xy` — `Lines 22–22`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `22` إلى السطر `22` (`Lines 22–22`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 22–22`):**
```python
def xy(mask):return np.argwhere(mask)[:,::-1].astype(float)+.5
```

### `samples_from_items` — `Lines 24–29`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `24` إلى السطر `29` (`Lines 24–29`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 24–29`):**
```python
def samples_from_items(items):
    lines=[]
    for p in items:
        curves=np.asarray(p['curves']);flat=np.concatenate([flatten(c)[:-1] for c in curves]+[curves[-1,-1:]])
        lines.append(flat)
    return lines,np.concatenate([sample_segments(p,.25) for p in lines]) if lines else np.empty((0,2))
```

### `render` — `Lines 31–33`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `31` إلى السطر `33` (`Lines 31–33`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 31–33`):**
```python
def render(svg,png,w,h,scale):
    start=time.perf_counter();subprocess.run([str(RESVG),'--width',str(w*scale),'--height',str(h*scale),str(svg),str(png)],check=True,capture_output=True,timeout=60)
    return time.perf_counter()-start
```

### `evaluate` — `Lines 35–89`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `35` إلى السطر `89` (`Lines 35–89`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 35–89`):**
```python
def evaluate(case):
    base,source=paths(case);rgb=np.asarray(Image.open(source).convert('RGB'));h,w=rgb.shape[:2]
    guides=json.loads((R/'experiments/EXP_COMPLETE_GEOMETRY_ISOLATION_01/references/shield_complete_boundary_reference.json').read_text()) if case=='A01_shield' else None
    truth=None;truth_label=None
    if case in ['fine_features','K01_linear_corner_hole']:
        references=json.loads((R/'experiments/EXP_COMPLETE_GEOMETRY_ISOLATION_01/references/known_control_reference_manifest.json').read_text())['references'];ref=next(x for x in references if x['id']==case)
        p=Path(ref['local_only_mask_path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==ref['mask_sha256']
        truth=np.asarray(Image.open(p).convert('L'))>=128;truth_label='independent source-vector8x sampled reference, not constructor input'
        # Boundary coordinates at the high-resolution raster sample centers.
        tb=truth ^ ndimage.binary_erosion(truth);target=xy(tb)/8
        thin=xy(skeletonize(truth))/8
    elif case in ['G06_arabic','H01_horse']:
        mask=np.linalg.norm(rgb.astype(float)-rgb[0,0].astype(float),axis=-1)>8
        truth=mask;target=xy(mask^ndimage.binary_erosion(mask));thin=xy(skeletonize(mask));truth_label='source-threshold proxy, not independent glyph/vector truth'
    else:target=None;thin=None
    rows=[]
    classical_sk=np.load(base/'Classical/discovery.npz')['skeleton'];classical_pts=xy(classical_sk)
    for arm in ['Classical','ML','Hybrid']:
        folder=base/arm
        if (folder/'metrics.json').exists():
            rows.append(json.loads((folder/'metrics.json').read_text()));continue
        a=json.loads((folder/'construction.json').read_text());arr=np.load(folder/'discovery.npz');pre=xy(arr['skeleton'])
        selected=[np.asarray(x['source_points_xy']) for x in a['traces'] if 'old_fit' in x]
        selected_pts=np.concatenate(selected) if selected else np.empty((0,2))
        lines,post=samples_from_items(a['accepted']);shapes=[LineString(p) for p in lines]
        tree=STRtree(shapes);pairs=[]
        for i,line in enumerate(shapes):
            for j in tree.query(line):
                j=int(j)
                if j<i and (line.crosses(shapes[j]) or line.overlaps(shapes[j])):pairs.append([j,i])
        metrics={'case':case,'arm':arm,'discovery':a['prefit'],'construction':a['postfit'],'known_reference':truth_label,'prefit_selected_points':len(selected_pts),'unintegrated':True,'geometry':'NOT_ACCEPTED','region_holes_and_connectivity':'NOT_ESTABLISHED: open edge strokes have no region ownership; skeleton topology is not glyph or object topology','actual_stroke_width_px':.35,'topology':{'self_intersecting_traces':[i for i,x in enumerate(shapes) if not x.is_simple],'mutual_crossing_or_overlap_pairs':pairs,'endpoint_and_junction_relationships':'not integrated/shared or certified'},'render_seconds':{},'render_dimensions':[w,h],'fitting_limitations':'Numerical segment-distance envelopes; not exact topology or continuous certificates.'}
        if target is not None:
            metrics['boundary_1_25px']={tag:support_stats(target,p,1.25) for tag,p in [('raw_all',pre),('raw_selected',selected_pts),('fitted',post)]}
            metrics['thin_skeleton_proximity_NOT_stroke_recovery']={tag:support_stats(thin,p,1.25) for tag,p in [('raw_all',pre),('fitted',post)]}
        metrics['classical_source_edge_agreement_proxy']={tag:support_stats(classical_pts,p,2.) for tag,p in [('raw_all',pre),('fitted',post)]}
        if guides:
            metrics['critical_guides']=[]
            for g in guides['components']+guides['appearance_only']:
                q=np.concatenate([sample_segments(np.asarray(p,float),.25) for p in g['polylines']])
                metrics['critical_guides'].append({'id':g['id'],'required':g.get('structural_boundary_required',False),'uncertainty_px':g['uncertainty_px'],'raw':support_stats(q,pre,g['uncertainty_px']),'selected':support_stats(q,selected_pts,g['uncertainty_px']),'fitted':support_stats(q,post,g['uncertainty_px']),'limit':'Approximate agent guide; no independently human-certified1px truth or semantic contour correspondence.'})
        spans=[np.ptp(p,axis=0) for p in lines];lengths=np.asarray([x.length for x in shapes]);tiny=np.asarray([max(s)<=2 for s in spans],dtype=bool);micro=np.asarray([x.length*.35 for x in shapes])
        metrics['vector']={'paths':len(shapes),'cubics':a['postfit']['cubics'],'svg_bytes':(folder/'stable.svg').stat().st_size,'tiny_bbox_le2px':int(tiny.sum()),'stroke_area_proxy_tiny_fraction':float(micro[tiny].sum()/max(micro.sum(),1e-9)),'microgeometry_limit':'length*width proxy not visible area ownership; overlaps unaccounted','half_grid_alignment_sample_fraction':float(np.mean(np.max(abs(post*2-np.round(post*2)),axis=1)<.02)) if len(post) else None,'axis_aligned_sample_length_fraction':float(sum(np.linalg.norm(np.diff(p,axis=0),axis=1)[np.min(abs(np.diff(p,axis=0)),axis=1)<1e-5].sum() for p in lines)/max(lengths.sum(),1e-9)),'closed_strokes':sum(np.array_equal(p[0],p[-1]) for p in lines),'filled_regions':0,'no_raster':True}
        # Actual renderer, full native and4x;16x is an explicit viewBox ROI.
        for scale in [1,4]:metrics['render_seconds'][f'{scale}x']=render(folder/'stable.svg',folder/f'stable_{scale}x.png',w,h,scale)
        render(folder/'old.svg',folder/'old_1x.png',w,h,1)
        roi=[115,70,145,100] if case=='A01_shield' else [w//4,h//4,min(96,w//2),min(72,h//2)]
        root=ET.parse(folder/'stable.svg').getroot();root.set('viewBox',' '.join(map(str,roi)));root.set('width',str(roi[2]));root.set('height',str(roi[3]));(folder/'detail.svg').write_text(ET.tostring(root,encoding='unicode'))
        for scale in [1,4,16]:metrics['render_seconds'][f'detail_{scale}x']=render(folder/'detail.svg',folder/f'detail_{scale}x.png',roi[2],roi[3],scale)
        paint=np.asarray(Image.open(folder/'stable_1x.png').convert('RGBA'));alpha=paint[...,3]/255.;overlay=np.rint(rgb*(1-alpha[...,None])+paint[...,:3]*alpha[...,None]).astype('uint8');Image.fromarray(overlay).save(folder/'svg_source_overlay.png')
        error=np.zeros_like(rgb);error[...,1]=arr['skeleton']*255
        if target is not None:
            idx=np.floor(target).astype(int);idx[:,0]=np.clip(idx[:,0],0,w-1);idx[:,1]=np.clip(idx[:,1],0,h-1);error[idx[:,1],idx[:,0],0]=255
        Image.fromarray(error).save(folder/'discovery_reference_overlay.png')
        (folder/'metrics.json').write_text(json.dumps(metrics,indent=2));rows.append(metrics)
    return rows
```
