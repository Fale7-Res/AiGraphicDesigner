# مرآة الكود التفصيلية: `run_experiment.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `run_experiment.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `run_experiment.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `269` (`Lines 1–269`)
- **بصمة الملف (`SHA-256`):** `2080cc7f795d7ab007267be71afc51cf87ce7cf753f0baefd7fc6b308c62b984`
- **الوصف التفصيلي:** """Approved fixed-geometry SVG appearance ablation; historical artifacts read-only."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `digest` | `function` | `Lines 22–23` | `def digest(path):` | رمز برمجي موثق. |
| `save_json` | `function` | `Lines 25–27` | `def save_json(path,data):` | رمز برمجي موثق. |
| `geometry_signature` | `function` | `Lines 29–43` | `def geometry_signature(path):` | All non-paint structure including ordering and masks; gradient definitions omitted. |
| `geometry_signature.visit` | `nested_function` | `Lines 32–37` | `def visit(node):` | رمز برمجي موثق. |
| `geometry_signature.prune` | `nested_function` | `Lines 39–42` | `def prune(v):` | رمز برمجي موثق. |
| `geometry_diagnostics` | `function` | `Lines 45–78` | `def geometry_diagnostics(path):` | Exact Bezier bounds and segment pairing for VTracer translate-only path coordinates. |
| `fixture_sources` | `function` | `Lines 80–91` | `def fixture_sources():` | Two independent analytic vector controls, not included in real-image generalization claims. |
| `frozen_cases` | `function` | `Lines 93–109` | `def frozen_cases():` | رمز برمجي موثق. |
| `appearance_metrics` | `function` | `Lines 111–115` | `def appearance_metrics(source,prediction):` | رمز برمجي موثق. |
| `evaluate_condition` | `function` | `Lines 117–128` | `def evaluate_condition(source,svg,folder):` | Evaluate actual native SVG renders, RGBA and independent full-image spatial errors. |
| `crop_svg` | `function` | `Lines 130–134` | `def crop_svg(svg,target,box,scale):` | Change only viewport, render vector geometry directly at requested zoom; no bitmap enlargement. |
| `case_visuals` | `function` | `Lines 136–164` | `def case_visuals(case,out):` | رمز برمجي موثق. |
| `known_control_geometry` | `function` | `Lines 166–189` | `def known_control_geometry(case,out):` | Compare known-control foreground silhouette and holes independently of fitted appearance. |
| `known_control_geometry.holes` | `nested_function` | `Lines 182–184` | `def holes(mask):` | رمز برمجي موثق. |
| `run_case` | `function` | `Lines 191–227` | `def run_case(case):` | رمز برمجي موثق. |
| `build_dashboard` | `function` | `Lines 229–243` | `def build_dashboard():` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `digest` — `Lines 22–23`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `22` إلى السطر `23` (`Lines 22–23`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 22–23`):**
```python
def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
```

### `save_json` — `Lines 25–27`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `25` إلى السطر `27` (`Lines 25–27`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 25–27`):**
```python
def save_json(path,data):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(data,indent=2,allow_nan=False),encoding='utf-8')
```

### `geometry_signature` — `Lines 29–43`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `29` إلى السطر `43` (`Lines 29–43`)
- **الوظيفة:** All non-paint structure including ordering and masks; gradient definitions omitted.
- **الكود الفعلي (`Lines 29–43`):**
```python
def geometry_signature(path):
    """All non-paint structure including ordering and masks; gradient definitions omitted."""
    root=ET.parse(path).getroot()
    def visit(node):
        if node.tag.rsplit('}',1)[-1] in ('linearGradient','radialGradient'):return None
        attrs={k:v for k,v in node.attrib.items() if k not in ('fill','style','id','data-fit-model','data-fit-region')}
        # Masks' fill/opacity/crispEdges are explicitly included, even though RGB paint is omitted.
        if node.tag.endswith('mask'):attrs['mask_subtree']=ET.tostring(node,encoding='unicode')
        return [node.tag,attrs,[v for c in node if (v:=visit(c)) is not None]]
    # Empty gradient-only defs do not change geometry.
    def prune(v):
        v[2]=[prune(c) for c in v[2]]
        v[2]=[c for c in v[2] if not(c[0].endswith('defs') and not c[2])]
        return v
    return hashlib.sha256(json.dumps(prune(visit(root)),sort_keys=True).encode()).hexdigest()
```

### `geometry_signature.visit` — `Lines 32–37`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `32` إلى السطر `37` (`Lines 32–37`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 32–37`):**
```python
    def visit(node):
        if node.tag.rsplit('}',1)[-1] in ('linearGradient','radialGradient'):return None
        attrs={k:v for k,v in node.attrib.items() if k not in ('fill','style','id','data-fit-model','data-fit-region')}
        # Masks' fill/opacity/crispEdges are explicitly included, even though RGB paint is omitted.
        if node.tag.endswith('mask'):attrs['mask_subtree']=ET.tostring(node,encoding='unicode')
        return [node.tag,attrs,[v for c in node if (v:=visit(c)) is not None]]
```

### `geometry_signature.prune` — `Lines 39–42`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `39` إلى السطر `42` (`Lines 39–42`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 39–42`):**
```python
    def prune(v):
        v[2]=[prune(c) for c in v[2]]
        v[2]=[c for c in v[2] if not(c[0].endswith('defs') and not c[2])]
        return v
```

### `geometry_diagnostics` — `Lines 45–78`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `45` إلى السطر `78` (`Lines 45–78`)
- **الوظيفة:** Exact Bezier bounds and segment pairing for VTracer translate-only path coordinates.
- **الكود الفعلي (`Lines 45–78`):**
```python
def geometry_diagnostics(path):
    """Exact Bezier bounds and segment pairing for VTracer translate-only path coordinates."""
    root=ET.parse(path).getroot();paths=list(root.iter(f'{{{SVG}}}path'))
    masks={id(p) for m in root.iter(f'{{{SVG}}}mask') for p in m.iter(f'{{{SVG}}}path')}
    bounds=[];segments=collections.Counter();cubic=0;closed=0;lattice=0;points=0;unsupported=[]
    for p in paths:
        if id(p) in masks:continue
        d=p.get('d','');pen=BoundsPen(None);parse_path(d,pen)
        if pen.bounds:
            x0,y0,x1,y1=pen.bounds;bounds.append((x1-x0,y1-y0))
        transform=p.get('transform','');translation=re.fullmatch(r'\s*translate\(\s*([-\d.eE]+)[ ,]+([-\d.eE]+)\s*\)\s*',transform)
        if transform and not translation:unsupported.append(transform);continue
        dx,dy=map(float,translation.groups()) if translation else (0.,0.)
        rec=RecordingPen();parse_path(d,rec);position=None;origin=None
        for op,ps in rec.value:
            ps=[(round(x+dx,3),round(y+dy,3)) for x,y in ps]
            points+=len(ps);lattice+=sum(abs(x-round(x))<1e-8 and abs(y-round(y))<1e-8 for x,y in ps)
            if op=='moveTo':position=origin=ps[0];continue
            if op=='closePath':
                closed+=1
                if position!=origin:ps=[origin];op='lineTo'
                else:continue
            if op in ('lineTo','curveTo') and position is not None:
                seq=(position,*ps);segments[min(seq,tuple(reversed(seq)))]+=1
                cubic+=op=='curveTo';position=ps[-1]
    return {'rgb_paths':len(bounds),'mask_paths':len(masks),'closed_subpaths':closed,'cubic_segments':cubic,
        'rgb_paths_bounds_le_1px':sum(w<=1.0001 and h<=1.0001 for w,h in bounds),
        'rgb_paths_bounds_le_2px':sum(w<=2.0001 and h<=2.0001 for w,h in bounds),
        'median_rgb_path_bbox_max_dimension':float(np.median([max(w,h) for w,h in bounds])) if bounds else None,
        'coordinate_integer_lattice_fraction':lattice/points if points else None,
        'exact_segment_pairs_round_3dp':sum(v==2 for v in segments.values()),
        'segments_incidence_gt2':sum(v>2 for v in segments.values()),'unpaired_segments':sum(v==1 for v in segments.values()),
        'unsupported_transforms':unsupported,
        'limits':'Bounds exact for Bezier path local coordinates; tiny-path counts are not area weighted. Segment pairing is structural evidence, not a proof of nonintersection, watertight rasterization, topology correctness, or semantic coherence.'}
```

### `fixture_sources` — `Lines 80–91`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `80` إلى السطر `91` (`Lines 80–91`)
- **الوظيفة:** Two independent analytic vector controls, not included in real-image generalization claims.
- **الكود الفعلي (`Lines 80–91`):**
```python
def fixture_sources():
    """Two independent analytic vector controls, not included in real-image generalization claims."""
    directory=ROOT/'inputs';directory.mkdir(exist_ok=True)
    controls={
      'K01_linear_corner_hole':'''<svg xmlns="http://www.w3.org/2000/svg" width="192" height="160" viewBox="0 0 192 160"><defs><linearGradient id="g" gradientUnits="userSpaceOnUse" x1="12" y1="0" x2="178" y2="0"><stop offset="0" stop-color="#12365f"/><stop offset="0.45" stop-color="#559ddd"/><stop offset="1" stop-color="#d9eaff"/></linearGradient></defs><path fill="#e8e0d2" d="M0 0H192V160H0Z"/><path fill="url(#g)" fill-rule="evenodd" d="M18 20L150 12L178 58L161 140L38 144C12 115 8 56 18 20Z M69 53C46 52 46 101 71 105C101 105 102 53 69 53Z"/><path fill="#c95328" d="M118 66L169 62L154 120L112 114Z"/></svg>''',
      'K02_radial_shared_curves':'''<svg xmlns="http://www.w3.org/2000/svg" width="192" height="160" viewBox="0 0 192 160"><defs><radialGradient id="r" gradientUnits="userSpaceOnUse" cx="70" cy="55" r="101"><stop offset="0" stop-color="#fff6ad"/><stop offset="0.5" stop-color="#e4931c"/><stop offset="1" stop-color="#663209"/></radialGradient></defs><path fill="#27394c" d="M0 0H192V160H0Z"/><path fill="url(#r)" d="M22 115C6 75 25 20 80 17C129 10 171 42 173 94C135 73 103 101 99 143C64 153 32 142 22 115Z"/><path fill="#3b9d95" d="M173 94C135 73 103 101 99 143C143 145 177 124 173 94Z"/></svg>'''}
    for name,text in controls.items():
        path=directory/f'{name}.svg'
        if path.exists():assert path.read_text()==text
        else:path.write_text(text,encoding='utf-8')
        if not path.with_suffix('.png').exists():render_svg(path,path.with_suffix('.png'),192,160)
    return list(controls)
```

### `frozen_cases` — `Lines 93–109`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `93` إلى السطر `109` (`Lines 93–109`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 93–109`):**
```python
def frozen_cases():
    controls=fixture_sources();cases=[]
    win=BASE/'results/A01_shield'
    cases.append({'id':'A01_shield','source':str(win/'normalized.png'),'reference':str(win/'best.svg'),'geometry':str(win/'trial_08/output.svg'),'known_vector':False})
    for name in ['G01_coffee','G03_rocket','G05_chelsea_nativecrop','G06_arabic','G07_tux','G08_dice_alpha']:
        saved=GEN/'results'/name
        raw=GEN/'inputs'/f'{name}.png';normalized=saved/'prepared/reference_srgb_rgba.png'
        source=raw if np.array_equal(np.asarray(Image.open(raw).convert('RGBA')),np.asarray(Image.open(normalized).convert('RGBA'))) else normalized
        item={'id':name,'source':str(source),'reference':str(saved/'inherited.svg'),'geometry':str(saved/'baseline_search/trial_08/output.svg'),'known_vector':False}
        if source!=raw:item.update(original_raster_source=str(raw),original_raster_sha256=digest(raw))
        cases.append(item)
    for name in controls:cases.append({'id':name,'source':str(ROOT/'inputs'/f'{name}.png'),'known_vector':True,'ground_truth_svg':str(ROOT/'inputs'/f'{name}.svg')})
    for c in cases:
        c['source_sha256']=digest(c['source'])
        for key in ['reference','geometry','ground_truth_svg']:
            if key in c:c[key+'_sha256']=digest(c[key])
    return cases
```

### `appearance_metrics` — `Lines 111–115`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `111` إلى السطر `115` (`Lines 111–115`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 111–115`):**
```python
def appearance_metrics(source,prediction):
    a=np.asarray(source,dtype=np.uint8);b=np.asarray(prediction,dtype=np.uint8)
    m=compare(a,b)|extra_metrics(a,b);sq=(a.astype(float)-b.astype(float))**2
    tiles=[float(np.sqrt(sq[y:y+32,x:x+32].mean())) for y in range(0,len(a),32) for x in range(0,a.shape[1],32)]
    m['worst_32px_tile_rmse']=max(tiles);return m
```

### `evaluate_condition` — `Lines 117–128`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `117` إلى السطر `128` (`Lines 117–128`)
- **الوظيفة:** Evaluate actual native SVG renders, RGBA and independent full-image spatial errors.
- **الكود الفعلي (`Lines 117–128`):**
```python
def evaluate_condition(source,svg,folder):
    """Evaluate actual native SVG renders, RGBA and independent full-image spatial errors."""
    folder.mkdir(parents=True,exist_ok=True);ref=Image.open(source).convert('RGBA')
    performance=render_svg(svg,folder/'render.png',*ref.size);pred=Image.open(folder/'render.png').convert('RGBA')
    a=np.asarray(ref);b=np.asarray(pred);da=np.abs(a[:,:,3].astype(float)-b[:,:,3].astype(float))
    metrics={}
    for name,color in [('white',(255,255,255)),('black',(0,0,0)),('bluegray',(40,80,120))]:
        back=Image.new('RGBA',ref.size,(*color,255));r=Image.alpha_composite(back,ref).convert('RGB');p=Image.alpha_composite(back,pred).convert('RGB')
        metrics[name]=appearance_metrics(r,p);p.save(folder/f'{name}.png')
    premult_a=a[:,:,:3].astype(float)*a[:,:,3:4]/255;premult_b=b[:,:,:3].astype(float)*b[:,:,3:4]/255
    return {'metrics':metrics,'alpha_mae':float(da.mean()),'alpha_max_error':float(da.max()),'premultiplied_rgb_rmse':float(np.sqrt(((premult_a-premult_b)**2).mean())),
      'structure':svg_structure(svg),'geometry':geometry_diagnostics(svg),'geometry_signature':geometry_signature(svg),'render':performance,'sha256':digest(svg)}
```

### `crop_svg` — `Lines 130–134`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `130` إلى السطر `134` (`Lines 130–134`)
- **الوظيفة:** Change only viewport, render vector geometry directly at requested zoom; no bitmap enlargement.
- **الكود الفعلي (`Lines 130–134`):**
```python
def crop_svg(svg,target,box,scale):
    """Change only viewport, render vector geometry directly at requested zoom; no bitmap enlargement."""
    x,y,w,h=box;root=ET.parse(svg).getroot();root.set('viewBox',f'{x} {y} {w} {h}');root.set('width',str(w));root.set('height',str(h))
    ET.ElementTree(root).write(target,encoding='utf-8',xml_declaration=True)
    return render_svg(target,target.with_suffix('.png'),w*scale,h*scale)
```

### `case_visuals` — `Lines 136–164`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `136` إلى السطر `164` (`Lines 136–164`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 136–164`):**
```python
def case_visuals(case,out):
    ref=Image.open(out/'source.png').convert('RGBA');w,h=ref.size
    white=Image.alpha_composite(Image.new('RGBA',ref.size,'white'),ref).convert('RGB')
    conditions=['A','B','C','D'];canvas=Image.new('RGB',(w*5,h+26),'#20242b');draw=ImageDraw.Draw(canvas)
    for i,(label,im) in enumerate([('Source',white)]+[(k,Image.open(out/k/'white.png').convert('RGB')) for k in conditions]):
        draw.text((i*w+5,5),label,fill='white');canvas.paste(im,(i*w,26))
    canvas.save(out/'comparison.png')
    errors=Image.new('RGB',(w*4,h+26),'#20242b');ed=ImageDraw.Draw(errors)
    reference=np.asarray(white).astype(float)
    for i,k in enumerate(conditions):
        e=np.abs(reference-np.asarray(Image.open(out/k/'white.png')).astype(float));heat=np.uint8(np.clip(e*6,0,255));ed.text((i*w+5,5),k+' absolute RGB error x6',fill='white');errors.paste(Image.fromarray(heat),(i*w,26))
    errors.save(out/'errors.png')
    # Prespecified crops: D worst native error tile plus image center, not favorable visual selection.
    d=np.asarray(Image.open(out/'D/white.png')).astype(float);sq=((reference-d)**2).mean(axis=2)
    candidates=[(float(sq[y:y+24,x:x+24].mean()),x,y) for y in range(0,h-23,24) for x in range(0,w-23,24)]
    _,x,y=max(candidates);boxes=[('worst_error',(x,y,24,24)),('center',(max(0,w//2-12),max(0,h//2-12),24,24))]
    zooms=[]
    for name,box in boxes:
        for scale in (1,4,16):
            sheet=Image.new('RGB',(24*scale*5,24*scale+24),'#20242b');dr=ImageDraw.Draw(sheet)
            x,y,cw,ch=box;source_crop=white.crop((x,y,x+cw,y+ch)).resize((cw*scale,ch*scale),Image.Resampling.NEAREST)
            sheet.paste(source_crop,(0,24));dr.text((1,4),'Source NN',fill='white')
            for i,k in enumerate(conditions,1):
                target=out/k/f'{name}_{scale}x.svg';timing=crop_svg(out/k/'output.svg',target,box,scale)
                image=Image.open(target.with_suffix('.png')).convert('RGBA');bg=Image.new('RGBA',image.size,'white');image=Image.alpha_composite(bg,image).convert('RGB')
                sheet.paste(image,(i*cw*scale,24));dr.text((i*cw*scale+1,4),k,fill='white')
                zooms.append({'region':name,'box':list(box),'scale':scale,'condition':k,'render':timing})
            sheet.save(out/f'{name}_{scale}x.png')
    save_json(out/'zoom_measurements.json',zooms)
```

### `known_control_geometry` — `Lines 166–189`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `166` إلى السطر `189` (`Lines 166–189`)
- **الوظيفة:** Compare known-control foreground silhouette and holes independently of fitted appearance.
- **الكود الفعلي (`Lines 166–189`):**
```python
def known_control_geometry(case,out):
    """Compare known-control foreground silhouette and holes independently of fitted appearance."""
    masks=[];ref=Image.open(out/'source.png').convert('RGB');background=np.asarray(ref)[0,0].astype(float)
    for name,source in [('truth',case['ground_truth_svg']),('spline',out/'B/output.svg')]:
        root=ET.parse(source).getroot();paths=list(root.iter(f'{{{SVG}}}path'))
        for i,p in enumerate(paths):
            if name=='truth':is_background=i==0
            else:
                color=np.array(ImageColor.getrgb(p.get('fill'))).astype(float)
                is_background=float(np.linalg.norm(color-background))<3
            p.set('fill','#000000' if is_background else '#ffffff')
        target=out/f'known_silhouette_{name}.svg';ET.ElementTree(root).write(target,encoding='utf-8',xml_declaration=True)
        render_svg(target,target.with_suffix('.png'),ref.width*4,ref.height*4)
        masks.append(np.asarray(Image.open(target.with_suffix('.png')).convert('L'))>=128)
    a,b=masks;ea=a & ~binary_erosion(a);eb=b & ~binary_erosion(b)
    ab=distance_transform_edt(~eb)[ea]/4;ba=distance_transform_edt(~ea)[eb]/4
    def holes(mask):
        labs,n=label(~mask);border=set(np.concatenate((labs[0],labs[-1],labs[:,0],labs[:,-1])))
        return sum(i not in border for i in range(1,n+1))
    save_json(out/'known_geometry.json',{'foreground_iou_4x':float((a&b).sum()/(a|b).sum()),
        'boundary_truth_to_spline_mean_px':float(ab.mean()),'boundary_spline_to_truth_mean_px':float(ba.mean()),
        'boundary_truth_to_spline_p95_px':float(np.percentile(ab,95)),'boundary_spline_to_truth_p95_px':float(np.percentile(ba,95)),
        'truth_foreground_holes':holes(a),'spline_foreground_holes':holes(b),
        'method':'4x actual vector render, threshold128; known first background path vs VTracer flat regions with inherited color distance<3 from source corner background. Tests foreground union only; not a full internal-region correspondence/topology proof.'})
```

### `known_control_geometry.holes` — `Lines 182–184`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `182` إلى السطر `184` (`Lines 182–184`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 182–184`):**
```python
    def holes(mask):
        labs,n=label(~mask);border=set(np.concatenate((labs[0],labs[-1],labs[:,0],labs[:,-1])))
        return sum(i not in border for i in range(1,n+1))
```

### `run_case` — `Lines 191–227`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `191` إلى السطر `227` (`Lines 191–227`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 191–227`):**
```python
def run_case(case):
    from fit_appearance import fit_svg
    for key in ['source','reference','geometry','ground_truth_svg']:
        if key in case and digest(case[key])!=case[key+'_sha256']:raise ValueError('Frozen artifact drift: '+key)
    out=ROOT/'results'/case['id']
    if (out/'result.json').exists():
        result=json.loads((out/'result.json').read_text());assert result['source_sha256']==digest(case['source'])
        for k,row in result['conditions'].items():assert digest(out/k/'output.svg')==row['sha256']
        print('REUSE',case['id'],flush=True);return
    if out.exists() and any(out.iterdir()):raise FileExistsError('Partial evidence preserved; inspect rather than overwrite')
    out.mkdir(parents=True);start=time.perf_counter();shutil.copyfile(case['source'],out/'source.png')
    for k in 'ABCD':(out/k).mkdir()
    if case['known_vector']:
        rgb=Image.open(out/'source.png').convert('RGB');rgb.save(out/'rgb.png')
        for k,config in [('A',pilots()[6]),('B',pilots()[8])]:
            result=run_trial(out/'rgb.png',out/f'control_trace_{k}',config)
            if result['status']!='ok':raise RuntimeError(result)
            shutil.copyfile(out/f'control_trace_{k}/output.svg',out/k/'output.svg')
    else:
        shutil.copyfile(case['reference'],out/'A/output.svg');shutil.copyfile(case['geometry'],out/'B/output.svg')
    raw_b=out/'B/output.svg';fit_svg(out/'source.png',raw_b,out/'C/output.svg',out/'D/output.svg',out/'fitting.json',deadline_seconds=540)
    alpha=Image.open(out/'source.png').convert('RGBA').getchannel('A');transparent=alpha.getextrema()!=(255,255)
    if transparent:
        alpha.save(out/'source_alpha.png')
        for k in 'BCD':
            shutil.move(str(out/k/'output.svg'),str(out/k/'rgb_unmasked.svg'))
            apply_vector_alpha(out/k/'rgb_unmasked.svg',out/'source_alpha.png',out/k/'output.svg')
    results={k:evaluate_condition(out/'source.png',out/k/'output.svg',out/k) for k in 'ABCD'}
    if results['C']['geometry_signature']!=results['D']['geometry_signature']:raise AssertionError('C/D geometry drift')
    if results['B']['geometry_signature']!=results['C']['geometry_signature']:raise AssertionError('B/C geometry drift')
    if case['known_vector']:known_control_geometry(case,out)
    case_visuals(case,out)
    report={'id':case['id'],'source_sha256':digest(out/'source.png'),'conditions':results,'transparent':transparent,'known_vector':case['known_vector'],
        'wall_seconds':time.perf_counter()-start,'geometry_config':pilots()[8],'geometry_policy':'one preregistered inherited watershed128 spline/cutout geometry, no per-image settings; reuse saved trial08',
        'alpha_policy':'identical inherited vector-run alpha mask B/C/D; actual output alpha separately measured',
        'architecture':'NOT_APPROVED'}
    save_json(out/'result.json',report);print('COMPLETE',case['id'],{k:round(v['metrics']['white']['ssim'],6) for k,v in results.items()},flush=True)
```

### `build_dashboard` — `Lines 229–243`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `229` إلى السطر `243` (`Lines 229–243`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 229–243`):**
```python
def build_dashboard():
    rows=[];cards=[]
    for path in sorted((ROOT/'results').glob('*/result.json')):
        r=json.loads(path.read_text());name=r['id'];cards.append(f'<section><h2>{name}</h2><p>Source, A pixel reference, B spline, C flat, D adaptive appearance. Images shown at native pixel size; scroll horizontally. Error maps use 6x absolute RGB error.</p>')
        for key in ['comparison','errors','worst_error_4x','worst_error_16x','center_16x']:
            cards.append(f'<figure><figcaption>{key}</figcaption><img loading="lazy" src="results/{name}/{key}.png"></figure>')
        cards.append('<p>'+ ' | '.join(f'<a href="results/{name}/{k}/output.svg">{k} full SVG</a>' for k in 'ABCD')+f' | <a href="results/{name}/result.json">metrics</a> | <a href="results/{name}/fitting.json">fit diagnostics</a></p><table><tr><th>Condition</th><th>SSIM white</th><th>PSNR dB</th><th>Worst tile RMSE</th><th>RGB paths</th><th>Bytes</th></tr>')
        for k,v in r['conditions'].items():
            m=v['metrics']['white'];row={'case':name,'condition':k,'ssim':m['ssim'],'psnr_db':m['psnr_db'],'mse':m['mse'],'worst_tile_rmse':m['worst_32px_tile_rmse'],'rgb_paths':v['geometry']['rgb_paths'],'bytes':v['structure']['bytes'],'render_seconds':v['render']['render_seconds'],'alpha_mae':v['alpha_mae']};rows.append(row)
            cards.append('<tr>'+''.join(f'<td>{html.escape(str(row[x]))}</td>' for x in ['condition','ssim','psnr_db','worst_tile_rmse','rgb_paths','bytes'])+'</tr>')
        cards.append('</table></section>')
    (ROOT/'index.html').write_text('<!doctype html><meta charset="utf-8"><title>Fixed geometry appearance ablation</title><style>body{font:16px system-ui;background:#141820;color:#eee;margin:24px}section{border-top:2px solid #879;margin-top:40px}figure{overflow:auto;margin:12px 0}img{max-width:none}td,th{padding:6px;border:1px solid #678}a{color:#8cf}</style><h1>Fixed-geometry appearance ablation — owner review</h1><p>Research only; architecture NOT_APPROVED. All failures retained. Native scores do not prove coherent geometry. Pixel A is a fidelity reference, not the desired final representation. Controls are analytic fixtures, not real-world generalization evidence. C and D have identical geometry; alpha still uses inherited grid runs. Source crops are nearest-neighbor reference displays, not vector ground truth.</p>'+''.join(cards),encoding='utf-8')
    with (ROOT/'reports/metrics.csv').open('w',newline='') as stream:
        w=csv.DictWriter(stream,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    save_json(ROOT/'reports/metrics.json',rows)
```
