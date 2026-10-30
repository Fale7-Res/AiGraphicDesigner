# مرآة الكود التفصيلية: `construct_geometry.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `construct_geometry.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `construct_geometry.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `77` (`Lines 1–77`)
- **بصمة الملف (`SHA-256`):** `bc972b391349754cc88e4826a2bf6f491fa7568b018350221840b8a8733194c3`
- **الوصف التفصيلي:** # START CHANGE AGD-ML-PACKAGE | 2026-10-30T08:17:45Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `paths` | `function` | `Lines 21–24` | `def paths(case):` | رمز برمجي موثق. |
| `chain_graph` | `function` | `Lines 26–32` | `def chain_graph(curves,width,height):` | رمز برمجي موثق. |
| `build` | `function` | `Lines 34–73` | `def build(case):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `paths` — `Lines 21–24`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `21` إلى السطر `24` (`Lines 21–24`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 21–24`):**
```python
def paths(case):
    base=W/'ml_geometry/local_only'/case if case=='fine_features' else E/'results'/case
    source=(W/'ml_geometry/local_only'/case if case=='fine_features' else E/'inputs'/case)/'working.png'
    return base,source
```

### `chain_graph` — `Lines 26–32`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `26` إلى السطر `32` (`Lines 26–32`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 26–32`):**
```python
def chain_graph(curves,width,height):
    chains=[]
    for i,item in enumerate(curves):
        cc=np.asarray(item['curves'])
        chains.append({'id':i,'closed':bool(np.array_equal(cc[0,0],cc[-1,-1])),'adjacent_face_labels':[1,2],
                       'segments':[dict(type='C',**{k:p.tolist() for k,p in zip(['p0','p1','p2','p3'],c)}) for c in cc]})
    return {'width':width,'height':height,'chains':chains,'faces':{}}
```

### `build` — `Lines 34–73`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `34` إلى السطر `73` (`Lines 34–73`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 34–73`):**
```python
def build(case):
    base,source=paths(case);rgb=np.asarray(Image.open(source).convert('RGB'));h,w=rgb.shape[:2]
    old=R/'experiments/EXP_RAW_FACE_JUNCTION_01/results'/case/'source_probe/source_evidence.npz'
    if case=='fine_features':old=W/'raw_face_junction/external_results/fine_features/source_probe/source_evidence.npz'
    if old.exists():classical=np.load(old)['persistent_edges'];origin=str(old)
    else:
        arrays,_=extract(rgb);classical=arrays['persistent_edges'];origin='unchanged historical extract(rgb)'
    probability=np.load(base/'ML/predictions.npz')['native_sigmoid']
    ml=apply_hysteresis_threshold(probability,.3,.5)
    near=ndimage.distance_transform_edt(~classical)<=1.5 if classical.any() else np.zeros_like(classical)
    hybrid_field=np.where(near | (probability>=.7),probability,0.)
    hybrid=apply_hysteresis_threshold(hybrid_field,.3,.5)
    for name,evidence in [('Classical',classical),('ML',ml),('Hybrid',hybrid)]:
        folder=base/name;folder.mkdir(parents=True,exist_ok=True)
        if (folder/'construction.json').exists():raise RuntimeError('Preserve existing candidates')
        started=time.monotonic();sk=skeletonize(evidence);raw,adjacency=_trace(sk)
        np.savez_compressed(folder/'discovery.npz',support=evidence,skeleton=sk)
        Image.fromarray(evidence.astype('uint8')*255).save(folder/'support.png')
        overlay=rgb.copy();overlay[sk]=(255,0,180);Image.fromarray(overlay).save(folder/'support_overlay.png')
        ranked=sorted(enumerate(raw),key=lambda z:(-np.linalg.norm(np.diff(z[1],axis=0),axis=1).sum(),z[0]))
        accepted=[];old_accepted=[];records=[];eligible=0
        for index,points in ranked:
            length=float(np.linalg.norm(np.diff(points,axis=0),axis=1).sum())
            record={'trace_id':index,'length_px':length,'source_points_xy':points.tolist()}
            if length<6:record['reason']='short_chain';records.append(record);continue
            eligible+=1
            if eligible>128:record['reason']='proposal_budget';records.append(record);continue
            if time.monotonic()-started>120:record['reason']='case_wall_budget';records.append(record);continue
            legacy,lmeta=_fit(points);record['old_fit']=lmeta
            if legacy is not None:old_accepted.append({'trace_id':index,'curves':legacy.tolist()})
            curves,meta=fit(points);record['stable_fit']=meta
            if curves is not None:
                accepted.append({'trace_id':index,'curves':curves.tolist(),'length_px':length,'fit':meta})
                record['reason']='accepted'
            else:record['reason']=meta['reason']
            records.append(record)
        for tag,items in [('old',old_accepted),('stable',accepted)]:
            graph=chain_graph(items,w,h);(folder/(tag+'.svg')).write_text(svg_graph(graph),encoding='utf-8')
        report={'case':case,'arm':name,'evidence_origin':origin if name=='Classical' else 'same DexiNed sigmoid fixed postprocessor','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'prefit':{'support_pixels':int(evidence.sum()),'density':float(evidence.mean()),'skeleton_pixels':int(sk.sum()),'components8':int(ndimage.label(sk,np.ones((3,3)))[1]),'junction_pixels':sum(len(v)>2 for v in adjacency.values()),'endpoint_pixels':sum(len(v)==1 for v in adjacency.values()),'raw_traces':len(raw),'eligible_traces':eligible},'postfit':{'old_accepted':len(old_accepted),'stable_accepted':len(accepted),'cubics':sum(len(x['curves']) for x in accepted),'rejections':dict(collections.Counter(x['reason'] for x in records if x['reason']!='accepted'))},'accepted':accepted,'traces':records,'wall_seconds':time.monotonic()-started,'integration':'Unintegrated open boundary proposals; no invented region ownership, width, holes or semantics. Complete geometry NOT_ACCEPTED.'}
        (folder/'construction.json').write_text(json.dumps(report,indent=2));print(case,name,report['prefit'],report['postfit'],report['wall_seconds'],flush=True)
```
