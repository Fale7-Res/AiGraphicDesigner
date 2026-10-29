# مرآة الكود التفصيلية: `geometry_eval.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `geometry_eval.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `geometry_eval.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `181` (`Lines 1–181`)
- **بصمة الملف (`SHA-256`):** `e1dca49a85a97c17c77ab3ff81ae566423ea594b8d042a50c8d13c92988f468f`
- **الوصف التفصيلي:** # START CHANGE AGD-ISOLATION-GEOMETRY-EVAL | 2026-10-29T06:48:34Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `label_rgb` | `function` | `Lines 14–16` | `def label_rgb(label):` | رمز برمجي موثق. |
| `flatten_cubic` | `function` | `Lines 18–27` | `def flatten_cubic(points,epsilon=.01,depth=0):` | رمز برمجي موثق. |
| `chain_points` | `function` | `Lines 29–40` | `def chain_points(ch,raw=False):` | رمز برمجي موثق. |
| `uniform_points` | `function` | `Lines 42–48` | `def uniform_points(points,step=.25):` | رمز برمجي موثق. |
| `signed_area` | `function` | `Lines 50–51` | `def signed_area(points):` | رمز برمجي موثق. |
| `ring_points` | `function` | `Lines 53–63` | `def ring_points(refs,chains):` | رمز برمجي موثق. |
| `compare_samples` | `function` | `Lines 65–70` | `def compare_samples(a,b):` | رمز برمجي موثق. |
| `svg_graph` | `function` | `Lines 72–107` | `def svg_graph(graph,raw=False,regions=False,foreground=None):` | رمز برمجي موثق. |
| `svg_graph.data` | `nested_function` | `Lines 74–87` | `def data(ch,forward=True):` | رمز برمجي موثق. |
| `evaluate` | `function` | `Lines 109–179` | `def evaluate(graph,reference=None):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `label_rgb` — `Lines 14–16`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `16` (`Lines 14–16`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 14–16`):**
```python
def label_rgb(label):
    value=(int(label)*0x9e3779)&0xffffff
    return (value>>16,(value>>8)&255,value&255)
```

### `flatten_cubic` — `Lines 18–27`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `27` (`Lines 18–27`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 18–27`):**
```python
def flatten_cubic(points,epsilon=.01,depth=0):
    p=np.asarray(points,float);v=p[3]-p[0];d=float(v@v)
    t=np.clip(((p[1:3]-p[0])@v)/d,0,1) if d else np.zeros(2)
    error=np.linalg.norm(p[1:3]-(p[0]+t[:,None]*v),axis=1).max()
    if error<=epsilon:return [p[0].tolist(),p[3].tolist()]
    if depth>=24:raise ValueError('Unresolved flattening bound; topology cannot PASS')
    a=(p[:-1]+p[1:])/2;b=(a[:-1]+a[1:])/2;c=(b[0]+b[1])/2
    left=flatten_cubic([p[0],a[0],b[0],c],epsilon,depth+1)
    right=flatten_cubic([c,b[1],a[2],p[3]],epsilon,depth+1)
    return left[:-1]+right
```

### `chain_points` — `Lines 29–40`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `29` إلى السطر `40` (`Lines 29–40`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 29–40`):**
```python
def chain_points(ch,raw=False):
    if raw:return np.asarray(ch['pixel_crack_vertices'],float)
    result=[]
    for s in ch['segments']:
        pts=flatten_cubic([s['p0'],s['p1'],s['p2'],s['p3']]) if s['type']=='C' else [s['p0'],s['p3']]
        if result and np.linalg.norm(np.asarray(result[-1])-pts[0])>1e-6:raise ValueError('Disconnected within chain')
        result.extend(pts if not result else pts[1:])
    # A native ring is exported with SVG closepath. Include that explicit
    # implied straight closure in measurement, without pinning open chains.
    if ch.get('closed') and result and np.linalg.norm(np.asarray(result[-1])-result[0])>1e-9:
        result.append(result[0])
    return np.asarray(result,float)
```

### `uniform_points` — `Lines 42–48`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `42` إلى السطر `48` (`Lines 42–48`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 42–48`):**
```python
def uniform_points(points,step=.25):
    p=np.asarray(points,float)
    if len(p)<2:return p
    dist=np.linalg.norm(np.diff(p,axis=0),axis=1);cum=np.r_[0,np.cumsum(dist)]
    if cum[-1]==0:return p[:1]
    at=np.arange(0,cum[-1],step);at=np.r_[at,cum[-1]]
    return np.column_stack([np.interp(at,cum,p[:,axis]) for axis in range(2)])
```

### `signed_area` — `Lines 50–51`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `50` إلى السطر `51` (`Lines 50–51`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 50–51`):**
```python
def signed_area(points):
    p=np.asarray(points,float);return float(np.sum(p[:,0]*np.roll(p[:,1],-1)-p[:,1]*np.roll(p[:,0],-1))/2)
```

### `ring_points` — `Lines 53–63`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `53` إلى السطر `63` (`Lines 53–63`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 53–63`):**
```python
def ring_points(refs,chains):
    result=[];gap=0.
    for r in refs:
        p=chains[r['chain']]
        if not r['forward']:p=p[::-1]
        if not len(p):continue
        if result:gap=max(gap,float(np.linalg.norm(np.asarray(result[-1])-p[0])))
        # Preserve a discontinuity rather than silently deleting its evidence.
        result.extend(p.tolist() if not result or np.linalg.norm(np.asarray(result[-1])-p[0])>1e-6 else p[1:].tolist())
    if result:gap=max(gap,float(np.linalg.norm(np.asarray(result[-1])-result[0])))
    return np.asarray(result),gap
```

### `compare_samples` — `Lines 65–70`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `65` إلى السطر `70` (`Lines 65–70`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 65–70`):**
```python
def compare_samples(a,b):
    if len(a)==0 or len(b)==0:return {'status':'MISSING_EVIDENCE'}
    da=cKDTree(b).query(a)[0];db=cKDTree(a).query(b)[0];ds=np.r_[da,db]
    return {'symmetric_mean_px':float(ds.mean()),'symmetric_p95_px':float(np.quantile(ds,.95)),
      'directed_a_to_b_mean_px':float(da.mean()),'a_recall_at_0_5px':float(np.mean(da<=.5)),
      'a_recall_at_1px':float(np.mean(da<=1)),'b_precision_at_1px':float(np.mean(db<=1))}
```

### `svg_graph` — `Lines 72–107`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `72` إلى السطر `107` (`Lines 72–107`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 72–107`):**
```python
def svg_graph(graph,raw=False,regions=False,foreground=None):
    chains={c['id']:c for c in graph['chains']};parts=[]
    def data(ch,forward=True):
        if raw:
            p=ch['pixel_crack_vertices'];p=p if forward else p[::-1]
            return 'M'+ ' L'.join(f'{x:.6g},{y:.6g}' for x,y in p)
        seg=ch['segments'] if forward else list(reversed(ch['segments']))
        tokens=[]
        for s in seg:
            p0=s['p0'] if forward else s['p3'];p3=s['p3'] if forward else s['p0']
            if not tokens:tokens.append(f'M{p0[0]:.8g},{p0[1]:.8g}')
            if s['type']=='C':
                p1=s['p1'] if forward else s['p2'];p2=s['p2'] if forward else s['p1']
                tokens.append('C'+','.join(f'{v:.8g}' for p in [p1,p2,p3] for v in p))
            else:tokens.append(f'L{p3[0]:.8g},{p3[1]:.8g}')
        return ' '.join(tokens)+(' Z' if ch.get('closed') else '')
    if regions:
        for label,loops in graph['faces'].items():
            if int(label)==0:continue
            if foreground is not None and int(label) not in foreground:continue
            ds=[]
            for refs in loops:
                txt=''
                for i,r in enumerate(refs):
                    t=data(chains[r['chain']],r['forward'])
                    if i:t=' '.join(t.split(' ')[1:]) if not raw else t.replace('M','L',1)
                    txt+=t+' '
                ds.append(txt+' Z')
            rgb=label_rgb(label)
            color='black' if foreground is not None else '#%02x%02x%02x'%rgb
            parts.append(f'<path data-region="{label}" fill="{color}" fill-rule="evenodd" d="{" ".join(ds)}"/>')
    else:
        for ch in graph['chains']:
            color='#607d8b' if 0 in ch['adjacent_face_labels'] else '#111827'
            parts.append(f'<path data-chain="{ch["id"]}" d="{data(ch)}" fill="none" stroke="{color}" stroke-width="0.35"/>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{graph["width"]}" height="{graph["height"]}" viewBox="0 0 {graph["width"]} {graph["height"]}">'+''.join(parts)+'</svg>'
```

### `svg_graph.data` — `Lines 74–87`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `74` إلى السطر `87` (`Lines 74–87`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 74–87`):**
```python
    def data(ch,forward=True):
        if raw:
            p=ch['pixel_crack_vertices'];p=p if forward else p[::-1]
            return 'M'+ ' L'.join(f'{x:.6g},{y:.6g}' for x,y in p)
        seg=ch['segments'] if forward else list(reversed(ch['segments']))
        tokens=[]
        for s in seg:
            p0=s['p0'] if forward else s['p3'];p3=s['p3'] if forward else s['p0']
            if not tokens:tokens.append(f'M{p0[0]:.8g},{p0[1]:.8g}')
            if s['type']=='C':
                p1=s['p1'] if forward else s['p2'];p2=s['p2'] if forward else s['p1']
                tokens.append('C'+','.join(f'{v:.8g}' for p in [p1,p2,p3] for v in p))
            else:tokens.append(f'L{p3[0]:.8g},{p3[1]:.8g}')
        return ' '.join(tokens)+(' Z' if ch.get('closed') else '')
```

### `evaluate` — `Lines 109–179`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `109` إلى السطر `179` (`Lines 109–179`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 109–179`):**
```python
def evaluate(graph,reference=None):
    chains={c['id']:chain_points(c) for c in graph['chains']}
    raw={c['id']:chain_points(c,True) for c in graph['chains']}
    rows=[];gaps=[];usage=collections.defaultdict(list);tiny_area=0.;total_area=0.
    for label,loops in graph['faces'].items():
        if int(label)==0:continue
        for ri,refs in enumerate(loops):
            for r in refs:usage[r['chain']].append(r['forward'])
            p,gap=ring_points(refs,chains);r,rgap=ring_points(refs,raw);gaps.append(gap)
            a=signed_area(p);ra=signed_area(r);poly=Polygon(p) if len(p)>=3 else None
            span=np.ptp(p,axis=0) if len(p) else np.zeros(2)
            # Ring-level bound area is a diagnostic, not visible union area.
            lattice=np.mean(np.min(np.abs(p-np.round(p)),axis=1)<.01) if len(p) else 1.
            total_area+=abs(a)
            if max(span)<=2 and lattice>=.8:tiny_area+=abs(a)
            rows.append({'face':int(label),'ring':ri,'raw_signed_area':ra,'fit_signed_area':a,
              'raw_nonzero_fit_degenerate':abs(ra)>1e-6 and abs(a)<=1e-6,
              'fit_valid_ring':bool(poly is not None and poly.is_valid and abs(a)>1e-6 and gap<=.001),
              'raw_valid_ring':bool(len(r)>=3 and Polygon(r).is_valid and abs(ra)>1e-6),
              'gap_px':gap,'bbox':span.tolist(),'lattice_fraction':float(lattice)})
    internal=[c for c in graph['chains'] if 0 not in c['adjacent_face_labels']]
    fitted_samples=np.concatenate([uniform_points(chains[c['id']]) for c in internal if len(chains[c['id']])>1])
    raw_samples=np.concatenate([uniform_points(raw[c['id']]) for c in internal if len(raw[c['id']])>1])
    displacements=[]
    for c in graph['chains']:
        if len(chains[c['id']])<2:continue
        x=compare_samples(uniform_points(raw[c['id']]),uniform_points(chains[c['id']]))
        displacements.append({'chain':c['id'],**x})
    topology_chains=[c for c in graph['chains'] if len(chains[c['id']])>=2]
    lines=[LineString(chains[c['id']]) for c in topology_chains]
    tree=STRtree(lines);pairs=[];uncertain=0;touch_failures=[]
    for i,line in enumerate(lines):
        for j in tree.query(line):
            j=int(j)
            if j<=i:continue
            other=lines[j]
            if line.crosses(other) or line.overlaps(other):pairs.append([i,j])
            elif line.touches(other):
                intersection=line.intersection(other)
                allowed=[Point(p) for p in [line.coords[0],line.coords[-1]] if any(np.linalg.norm(np.asarray(p)-q)<1e-6 for q in [other.coords[0],other.coords[-1]])]
                if not allowed or any(intersection.difference(p.buffer(1e-6)).length>1e-6 for p in allowed) and intersection.geom_type!='Point':
                    touch_failures.append([topology_chains[i]['id'],topology_chains[j]['id']])
            elif line.distance(other)<.02 and not line.touches(other):uncertain+=1
    result={'rings':rows,'chains':len(chains),'cubics':sum(s['type']=='C' for c in graph['chains'] for s in c['segments']),
      'raw_nonzero_fit_degenerate_rings':sum(r['raw_nonzero_fit_degenerate'] for r in rows),
      'invalid_fit_rings':sum(not r['fit_valid_ring'] for r in rows),'invalid_raw_rings':sum(not r['raw_valid_ring'] for r in rows),
      'max_junction_gap_px':max(gaps,default=0.),'shared_reference_failures':sum(sorted(usage[c['id']])!=[False,True] for c in internal),
      'self_intersecting_chains':sum(not x.is_simple for x in lines),'crossing_or_overlap_pairs':len(pairs),'first_crossings':pairs[:30],
      'unexpected_endpoint_interior_touches':len(touch_failures),'first_bad_touches':touch_failures[:30],
      'near_intersection_unresolved_pairs':uncertain,'raw_to_fit':compare_samples(raw_samples,fitted_samples),
      'worst_displaced_chains':sorted(displacements,key=lambda r:r.get('symmetric_p95_px',0),reverse=True)[:20],
      'ring_area_weighted_tiny_lattice_fraction':tiny_area/max(total_area,1e-9),
      'microgeometry_limit':'Ring absolute area double-counts holes; visible-area anti-mosaic requires rasterized visible faces separately.',
      'continuous_predicate_limit':'Adaptive control-hull flattening <=.01px; Shapely double predicates. Near intersections unresolved, not certified PASS.'}
    if reference:
        components=[]
        for c in reference['components']:
            ref=np.concatenate([uniform_points(p) for p in c['polylines']])
            lo=ref.min(axis=0)-2;hi=ref.max(axis=0)+2
            nearby=fitted_samples[np.all((fitted_samples>=lo)&(fitted_samples<=hi),axis=1)]
            rd=cKDTree(raw_samples).query(ref)[0];fd=cKDTree(fitted_samples).query(ref)[0]
            metrics=compare_samples(ref,nearby)
            components.append({'id':c['id'],'uncertainty_px':c['uncertainty_px'],
             'strict_gate':'NOT_ESTABLISHED_REFERENCE_UNCERTAINTY',
             'raw_recall_at_1px':float(np.mean(rd<=1)), 'fit_recall_at_1px':float(np.mean(fd<=1)),
             'raw_recall_within_annotation_band':float(np.mean(rd<=c['uncertainty_px'])),
             'fit_recall_within_annotation_band':float(np.mean(fd<=c['uncertainty_px'])),
             'local_box_all_boundaries_precision_note':'Unassigned nearby boundaries include real extra structure; not correspondence-certified precision',**metrics})
        result['critical_component_diagnostics']=components
    result['geometry_acceptance']='NOT_ACCEPTED' if result['invalid_fit_rings'] or result['shared_reference_failures'] or pairs or uncertain or touch_failures or result['self_intersecting_chains'] or result['max_junction_gap_px']>.001 else 'NOT_ESTABLISHED_ALL_GATES_NOT_CERTIFIED'
    return result
```
