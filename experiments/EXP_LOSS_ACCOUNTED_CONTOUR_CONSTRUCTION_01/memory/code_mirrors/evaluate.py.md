# مرآة الكود التفصيلية: `evaluate.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `evaluate.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `evaluate.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `145` (`Lines 1–145`)
- **بصمة الملف (`SHA-256`):** `db388172b890d3cde04a54986dbdd8b300f484d07f515f7bdef4b87e181c57cb`
- **الوصف التفصيلي:** # START CHANGE AGD-CONTOUR-CLOSURE | 2026-10-30T15:21:28Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `topology_diagnostics` | `function` | `Lines 18–46` | `def topology_diagnostics(items,raws):` | رمز برمجي موثق. |
| `references` | `function` | `Lines 48–63` | `def references(case,source):` | رمز برمجي موثق. |
| `micro_diagnostics` | `function` | `Lines 65–71` | `def micro_diagnostics(items):` | رمز برمجي موثق. |
| `evaluate_arm` | `function` | `Lines 73–136` | `def evaluate_arm(case,arm):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `topology_diagnostics` — `Lines 18–46`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `46` (`Lines 18–46`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 18–46`):**
```python
def topology_diagnostics(items,raws):
    lines=[LineString(flattened(np.asarray(i['curves']))) for i in items];tree=STRtree(lines)
    mutual=[];new=[];touch=[];selfbad=[];loops=[];endpoints=collections.Counter();loop_polygons=[]
    for i,(item,line) in enumerate(zip(items,lines)):
        raw=LineString(np.asarray(raws[item['trace_id']]['source_points_xy']));p=np.asarray(item['curves'])
        endpoints[tuple(p[0,0])]+=1;endpoints[tuple(p[-1,-1])]+=1
        if not line.is_simple:selfbad.append(i)
        for j in tree.query(line):
            j=int(j)
            if j>=i:continue
            if line.crosses(lines[j]) or line.overlaps(lines[j]):
                mutual.append([j,i]);other=LineString(raws[items[j]['trace_id']]['source_points_xy'])
                if line.crosses(lines[j]) and not raw.crosses(other) or line.overlaps(lines[j]) and not raw.overlaps(other):new.append([j,i])
            elif line.intersects(lines[j]):touch.append([j,i])
        if np.array_equal(p[0,0],p[-1,-1]):
            source=np.asarray(raw.coords);fitted=np.asarray(line.coords);a=signed_area(source);b=signed_area(fitted);rawpoly=Polygon(source);fitpoly=Polygon(fitted)
            overlap=float(rawpoly.intersection(fitpoly).area/max(rawpoly.union(fitpoly).area,1e-9)) if rawpoly.is_valid and fitpoly.is_valid else None
            loops.append({'trace_id':item['trace_id'],'raw_signed_area_px2':a,'fitted_signed_area_px2':b,'winding_preserved':bool(a*b>0),'source_polygon_fit_iou':overlap,'is_simple':bool(line.is_simple),'closed_exactly':True,'limits':'SourcepolygonIoU is raw-evidence fit, not independent artwork/region/holetruth'})
            if rawpoly.is_valid and fitpoly.is_valid:loop_polygons.append((item['trace_id'],rawpoly,fitpoly))
    source_ends=collections.Counter()
    for trace in raws.values():
        q=np.asarray(trace['source_points_xy']);source_ends[tuple(q[0])]+=1;source_ends[tuple(q[-1])]+=1
    sourcejunctions={k:v for k,v in source_ends.items() if v>=3}
    nesting=[]
    for i,(tid,a,b) in enumerate(loop_polygons):
        for oid,c,d in loop_polygons[:i]:
            relation=lambda x,y:'contains' if x.contains(y) else 'within' if x.within(y) else 'disjoint' if x.disjoint(y) else 'touches' if x.touches(y) else 'overlap'
            before,after=relation(a,c),relation(b,d);nesting.append({'trace_pair':[tid,oid],'source_relation':before,'fitted_relation':after,'preserved':before==after})
    return {'self_intersecting_paths':selfbad,'proper_cross_or_overlap_pairs':mutual,'new_cross_or_overlap_pairs_vs_same_raw_pair':new,'touch_pairs_including_shared_junctions':touch,'closed_loops':loops,'valid_closed_loop_nesting':nesting,'source_endpoint_junctions':len(sourcejunctions),'complete_incidence_junctions_retained':sum(endpoints[k]>=v for k,v in sourcejunctions.items()),'reference_junction_definition':'degree>=3 from frozen trace endpoints, not semantic artworktruth','new_endpoint_junctions':sum(v>=3 and k not in sourcejunctions for k,v in endpoints.items()),'closed_regions_and_holes':'NOT_ESTABLISHED; independent curve/contour closure and nesting is not filledfaceownership'}
```

### `references` — `Lines 48–63`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `48` إلى السطر `63` (`Lines 48–63`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 48–63`):**
```python
def references(case,source):
    rgb=np.asarray(Image.open(source).convert('RGB'));target=None;mask=None;scale=1
    if case in ['fine_features','K01_linear_corner_hole']:
        refs=json.loads((R/'experiments/EXP_COMPLETE_GEOMETRY_ISOLATION_01/references/known_control_reference_manifest.json').read_text())['references'];ref=next(x for x in refs if x['id']==case)
        file=Path(ref['local_only_mask_path']);assert hashlib.sha256(file.read_bytes()).hexdigest()==ref['mask_sha256'];mask=np.asarray(Image.open(file).convert('L'))>=128;scale=8;tag='independent8xsource-vector sampled mask'
    elif case in ['G06_arabic','H01_horse']:
        mask=np.linalg.norm(rgb.astype(float)-rgb[0,0].astype(float),axis=-1)>8;tag='source-thresholdproxy;notindependentglyph/vectortruth'
    else:tag='No independent full contour truth'
    if mask is not None:target=xy(mask^ndimage.binary_erosion(mask))/scale
    holes=[]
    if mask is not None:
        components,n=ndimage.label(ndimage.binary_fill_holes(mask)&~mask)
        for i in range(1,n+1):
            region=components==i
            holes.append(xy(region^ndimage.binary_erosion(region))/scale)
    return rgb,target,holes,tag
```

### `micro_diagnostics` — `Lines 65–71`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `65` إلى السطر `71` (`Lines 65–71`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 65–71`):**
```python
def micro_diagnostics(items):
    lengths=[];tiny=[]
    for item in items:
        for curve in np.asarray(item['curves']):
            flat=flatten(curve);lengths.append(float(np.linalg.norm(np.diff(flat,axis=0),axis=1).sum()));tiny.append(max(np.ptp(flat,axis=0))<=2)
    lengths=np.asarray(lengths);tiny=np.asarray(tiny,bool)
    return dict(tiny_cubic_span_le2px=int(tiny.sum()),tiny_cubic_length_weighted_fraction=float(lengths[tiny].sum()/max(lengths.sum(),1e-9)),median_cubic_length_px=float(np.median(lengths)) if len(lengths) else None,anti_mosaic_limit='No pixelcellsorrawfallback; shortcubicspansandremaininggridoscillationcanstillfailprofessionalgeometry. Pathbboxaloneisinsufficient.')
```

### `evaluate_arm` — `Lines 73–136`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `73` إلى السطر `136` (`Lines 73–136`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 73–136`):**
```python
def evaluate_arm(case,arm):
    protocol=json.loads((E/'protocol.json').read_text());base=Path(protocol['cases'][case]['base']);source=Path(protocol['cases'][case]['source']);old=json.loads((base/arm/'construction.json').read_text());raws={x['trace_id']:x for x in old['traces']}
    out=destination(case,arm);rgb,target,holes,tag=references(case,source);h,w=rgb.shape[:2]
    rawmask=np.load(base/arm/'discovery.npz')['skeleton'];allpts=xy(rawmask)
    selected=[np.asarray(x['source_points_xy']) for x in old['traces'] if 'old_fit' in x];selectedpts=np.concatenate(selected) if selected else np.empty((0,2))
    guides=json.loads((R/'experiments/EXP_COMPLETE_GEOMETRY_ISOLATION_01/references/shield_complete_boundary_reference.json').read_text()) if case=='A01_shield' else None
    rows=[]
    for condition in ['O','P','Q']:
        if (out/(condition+'_metrics.json')).exists():
            saved=json.loads((out/(condition+'_metrics.json')).read_text())
            if 'valid_closed_loop_nesting' not in saved['topology']:
                candidate=old if condition=='O' else json.loads((out/(condition+'.json')).read_text())
                saved['topology']=topology_diagnostics(candidate['accepted'],raws)
                (out/(condition+'_metrics.json')).write_text(json.dumps(saved,indent=2))
            if 'tiny_cubic_span_le2px' not in saved['vector']:
                candidate=old if condition=='O' else json.loads((out/(condition+'.json')).read_text())
                saved['vector'].update(micro_diagnostics(candidate['accepted']))
                (out/(condition+'_metrics.json')).write_text(json.dumps(saved,indent=2))
            rows.append(saved);continue
        data=old if condition=='O' else json.loads((out/(condition+'.json')).read_text());items=data['accepted'];lines,post=samples_from_items(items)
        summary=data.get('summary',{})
        if condition=='O':
            total=sum(x['length_px'] for x in old['traces']);kept=sum(x['length_px'] for x in old['traces'] if any(p['trace_id']==x['trace_id'] for p in items));sel=sum(np.linalg.norm(np.diff(p,axis=0),axis=1).sum() for p in selected)
            summary={'raw_trace_count':len(raws),'raw_length_px':total,'selected_length_px':sel,'accepted_length_px':kept,'lost_length_px':total-kept,'output_paths':len(items),'cubics':sum(len(x['curves']) for x in items),'loss_by_reason':dict(collections.Counter(x['reason'] for x in old['traces']))}
        m={'case':case,'arm':arm,'condition':condition,'loss':summary,'retained_selected_length_fraction':summary['accepted_length_px']/max(summary['selected_length_px'],1e-9),'retained_total_length_fraction':summary['accepted_length_px']/max(summary['raw_length_px'],1e-9),'reference':tag,'geometry':'NOT_ACCEPTED','source_predictions_changed':False,'topology':topology_diagnostics(items,raws),'render_seconds':{}}
        if target is not None:
            m['boundary_1_25px']={name:support_stats(target,p,1.25) for name,p in [('raw_all',allpts),('selected',selectedpts),('fitted',post)]}
            m['hole_boundary_support_NOT_ownership']=[{'reference_hole_index':i,'fitted_all':support_stats(q,post,1.25),'closed_paths_only':support_stats(q,np.concatenate([sample_segments(p,.25) for p,item in zip(lines,items) if np.array_equal(p[0],p[-1])]) if any(np.array_equal(p[0],p[-1]) for p in lines) else np.empty((0,2)),1.25)} for i,q in enumerate(holes)]
        if guides:
            m['critical_guides']=[]
            for g in guides['components']+guides['appearance_only']:
                q=np.concatenate([sample_segments(np.asarray(p,float),.25) for p in g['polylines']])
                m['critical_guides'].append({'id':g['id'],'uncertainty_px':g['uncertainty_px'],'required':g.get('structural_boundary_required',False),'raw':support_stats(q,allpts,g['uncertainty_px']),'selected':support_stats(q,selectedpts,g['uncertainty_px']),'fitted':support_stats(q,post,g['uncertainty_px']),'limit':'Approximateagentguide;nostrict1px/humanorsemanticcorrespondencetruth'})
        spans=[np.ptp(p,axis=0) for p in lines];tiny=np.asarray([max(s)<=2 for s in spans],bool);lengths=np.asarray([LineString(p).length for p in lines]);alllength=max(lengths.sum(),1e-9)
        m['vector']={'paths':len(items),'cubics':sum(len(x['curves']) for x in items),'tiny_bbox_le2px':int(tiny.sum()),'tiny_stroke_area_proxy_fraction':float(lengths[tiny].sum()/alllength),'microgeometry':'Lengthtimesconstantwidthproxy,notactualvisiblefacearea','half_grid_fraction':float(np.mean(np.max(abs(post*2-np.round(post*2)),axis=1)<.02)) if len(post) else None,'axis_sample_length_fraction':float(sum(np.linalg.norm(np.diff(p,axis=0),axis=1)[np.min(abs(np.diff(p,axis=0)),axis=1)<1e-5].sum() for p in lines)/alllength),'svg_bytes':(out/(condition+'.svg')).stat().st_size,'filled_regions':0}
        m['vector'].update(micro_diagnostics(items))
        for scale in [1,4]:m['render_seconds'][f'{scale}x']=render(out/(condition+'.svg'),out/(condition+f'_{scale}x.png'),w,h,scale)
        roi=[115,70,145,100] if case=='A01_shield' else [w//4,h//4,min(96,w//2),min(72,h//2)]
        root=ET.parse(out/(condition+'.svg')).getroot();root.set('viewBox',' '.join(map(str,roi)));root.set('width',str(roi[2]));root.set('height',str(roi[3]));(out/(condition+'_detail.svg')).write_text(ET.tostring(root,encoding='unicode'))
        for scale in [1,4,16]:m['render_seconds'][f'detail{scale}x']=render(out/(condition+'_detail.svg'),out/(condition+f'_detail_{scale}x.png'),roi[2],roi[3],scale)
        # Loss overlay is explicitly raster evidence diagnostic, never SVG fallback.
        lossview=Image.fromarray(rgb.copy());draw=ImageDraw.Draw(lossview)
        if condition=='O':
            for trace in old['traces']:
                color=(0,150,40) if any(p['trace_id']==trace['trace_id'] for p in items) else (220,50,40)
                draw.line([tuple(v) for v in trace['source_points_xy']],fill=color,width=1)
        else:
            ledgerrows=[]
            for trace in data['traces']:
                raw=np.asarray(raws[trace['trace_id']]['source_points_xy'])
                for part in trace['ledger']:
                    color=(0,150,40) if part['status']=='accepted' else (220,50,40)
                    draw.line([tuple(v) for v in raw[part['lo']:part['hi']+1]],fill=color,width=1)
                    ledgerrows.append({'trace_id':trace['trace_id'],'old_reason':trace['old_reason'],'closed_source':trace['closed_source'],'lo':part['lo'],'hi':part['hi'],'length_px':part['length_px'],'status':part['status'],'reason':part['reason']})
            with (out/(condition+'_loss_ledger.csv')).open('w',newline='',encoding='utf-8') as f:
                writer=csv.DictWriter(f,fieldnames=list(ledgerrows[0]));writer.writeheader();writer.writerows(ledgerrows)
        lossview.save(out/(condition+'_loss_overlay.png'))
        (out/(condition+'_metrics.json')).write_text(json.dumps(m,indent=2));rows.append(m)
    sheet=Image.new('RGB',(4*370,320),'white');draw=ImageDraw.Draw(sheet)
    panels=[('Source',Image.fromarray(rgb))]
    for c in ['O','P','Q']:
        rgba=Image.open(out/(c+'_1x.png')).convert('RGBA');white=Image.new('RGBA',rgba.size,'white');white.alpha_composite(rgba);panels.append((c+' geometry ONLY',white.convert('RGB')))
    for i,(label,im) in enumerate(panels):draw.text((i*370+8,8),label,fill='black');sheet.paste(ImageOps.contain(im,(354,280)),(i*370+8,32))
    sheet.save(out/'comparison_sheet.png');return rows
```
