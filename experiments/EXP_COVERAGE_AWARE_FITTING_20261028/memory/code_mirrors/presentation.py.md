# مرآة الكود التفصيلية: `presentation.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `presentation.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `presentation.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `151` (`Lines 1–151`)
- **بصمة الملف (`SHA-256`):** `fc33bdf15948f4d07a29fc2b2792a13281918fd902be54666ea531d0660587fd`
- **الوصف التفصيلي:** """Owner-review visuals from completed coverage-aware results; no fitting or tracing."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `rgb_on` | `function` | `Lines 14–16` | `def rgb_on(image,background='white'):` | رمز برمجي موثق. |
| `number` | `function` | `Lines 18–20` | `def number(value,decimals=6):` | رمز برمجي موثق. |
| `three_background_error` | `function` | `Lines 22–29` | `def three_background_error(source,predicted):` | Float composited three-background residual, matching driver's local-error policy. |
| `choose_boxes` | `function` | `Lines 31–41` | `def choose_boxes(source,predicted,case):` | Worst complete 24px tile plus preregistered thin-feature box or center. |
| `native_sheets` | `function` | `Lines 43–63` | `def native_sheets(case,result,folder):` | Package saved actual PNG renders with source, alpha and visible error maps. |
| `actual_zoom_sheets` | `function` | `Lines 65–82` | `def actual_zoom_sheets(case,folder,images,conditions):` | Actual SVG viewport renders at 1x/4x/16x, never upscaled SVG screenshots. |
| `metric_table` | `function` | `Lines 84–91` | `def metric_table(result,background):` | رمز برمجي موثق. |
| `build_presentation` | `function` | `Lines 93–127` | `def build_presentation():` | Require all nine results complete; refuse to replace presentation evidence. |
| `add_flat_comparisons` | `function` | `Lines 130–144` | `def add_flat_comparisons():` | Add explicit flat-pair negatives without repeating any vector rendering. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `rgb_on` — `Lines 14–16`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `16` (`Lines 14–16`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 14–16`):**
```python
def rgb_on(image,background='white'):
    rgba=image.convert('RGBA')
    return Image.alpha_composite(Image.new('RGBA',rgba.size,(*BACKGROUND_COLORS[background],255)),rgba).convert('RGB')
```

### `number` — `Lines 18–20`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `20` (`Lines 18–20`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 18–20`):**
```python
def number(value,decimals=6):
    if value is None:return 'exact / undefined'
    return f'{value:.{decimals}f}' if isinstance(value,(float,int)) else html.escape(str(value))
```

### `three_background_error` — `Lines 22–29`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `22` إلى السطر `29` (`Lines 22–29`)
- **الوظيفة:** Float composited three-background residual, matching driver's local-error policy.
- **الكود الفعلي (`Lines 22–29`):**
```python
def three_background_error(source,predicted):
    """Float composited three-background residual, matching driver's local-error policy."""
    a=np.asarray(source.convert('RGBA'),dtype=float);b=np.asarray(predicted.convert('RGBA'),dtype=float)
    aa=a[:,:,3:4]/255;ba=b[:,:,3:4]/255;ap=a[:,:,:3]*aa;bp=b[:,:,:3]*ba
    errors=[]
    for color in BACKGROUND_COLORS.values():
        bg=np.array(color);errors.append(((bp+(1-ba)*bg)-(ap+(1-aa)*bg))**2)
    return np.mean(np.mean(errors,axis=0),axis=2)
```

### `choose_boxes` — `Lines 31–41`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `31` إلى السطر `41` (`Lines 31–41`)
- **الوظيفة:** Worst complete 24px tile plus preregistered thin-feature box or center.
- **الكود الفعلي (`Lines 31–41`):**
```python
def choose_boxes(source,predicted,case):
    """Worst complete 24px tile plus preregistered thin-feature box or center."""
    w,h=source.size;edge=min(24,w,h);error=three_background_error(source,predicted)
    xs=sorted(set(range(0,w-edge+1,edge))|{w-edge});ys=sorted(set(range(0,h-edge+1,edge))|{h-edge})
    score,x,y=max((float(error[y:y+edge,x:x+edge].mean()),x,y) for y in ys for x in xs)
    fixture=case.get('fixture',{});thin=fixture.get('thin_regions',[])
    if thin:
        bx,by,bw,bh=thin[0]['critical_box'];cx,cy=bx+bw/2,by+bh/2;name='thin_feature'
    else:cx,cy=w/2,h/2;name='center_detail'
    x2=int(np.clip(round(cx-edge/2),0,w-edge));y2=int(np.clip(round(cy-edge/2),0,h-edge))
    return [('worst_C_error',[x,y,edge,edge]),(name,[x2,y2,edge,edge])]
```

### `native_sheets` — `Lines 43–63`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `43` إلى السطر `63` (`Lines 43–63`)
- **الوظيفة:** Package saved actual PNG renders with source, alpha and visible error maps.
- **الكود الفعلي (`Lines 43–63`):**
```python
def native_sheets(case,result,folder):
    """Package saved actual PNG renders with source, alpha and visible error maps."""
    saved=ROOT/'results'/case['id'];source=Image.open(saved/'source.png').convert('RGBA')
    conditions=[key for key in ('pixel','Agrad','B','C','truth') if key in result['conditions']]
    images={'source':source}|{key:Image.open(saved/key/'render.png').convert('RGBA') for key in conditions}
    w,h=source.size;column=max(w,180);labels=['source']+conditions
    for bg in BACKGROUND_COLORS:
        board=Image.new('RGB',(len(labels)*column,h+44),'white');draw=ImageDraw.Draw(board)
        for i,key in enumerate(labels):
            draw.text((i*column+5,6),LABELS[key],fill='black');draw.text((i*column+5,22),bg+' / saved actual render' if key!='source' else bg+' / source raster',fill='black')
            board.paste(rgb_on(images[key],bg),(i*column,42))
        board.save(folder/f'comparison_{bg}.png')
        error_board=Image.new('RGB',(len(conditions)*column,h+30),'white');ed=ImageDraw.Draw(error_board);ref=np.asarray(rgb_on(source,bg),dtype=float)
        for i,key in enumerate(conditions):
            delta=np.abs(ref-np.asarray(rgb_on(images[key],bg),dtype=float));heat=Image.fromarray(np.uint8(np.clip(delta*6,0,255)))
            ed.text((i*column+4,6),key+' absolute RGB error x6',fill='black');error_board.paste(heat,(i*column,28))
        error_board.save(folder/f'errors_{bg}.png')
    alpha=Image.new('RGB',(len(labels)*column,h+30),'white');ad=ImageDraw.Draw(alpha)
    for i,key in enumerate(labels):ad.text((i*column+4,6),key+' actual alpha',fill='black');alpha.paste(images[key].getchannel('A').convert('RGB'),(i*column,28))
    alpha.save(folder/'alpha.png')
    return images,conditions
```

### `actual_zoom_sheets` — `Lines 65–82`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `65` إلى السطر `82` (`Lines 65–82`)
- **الوظيفة:** Actual SVG viewport renders at 1x/4x/16x, never upscaled SVG screenshots.
- **الكود الفعلي (`Lines 65–82`):**
```python
def actual_zoom_sheets(case,folder,images,conditions):
    """Actual SVG viewport renders at 1x/4x/16x, never upscaled SVG screenshots."""
    saved=ROOT/'results'/case['id'];measurements=[];boxes=choose_boxes(images['source'],images['C'],case)
    for name,box in boxes:
        x,y,w,h=box
        for scale in (1,4,16):
            labels=['source']+conditions;board=Image.new('RGB',(len(labels)*w*scale,h*scale+28),'white');draw=ImageDraw.Draw(board)
            reference=rgb_on(images['source']).crop((x,y,x+w,y+h)).resize((w*scale,h*scale),Image.Resampling.NEAREST)
            board.paste(reference,(0,28));draw.text((1,6),'S NN',fill='black')
            for i,key in enumerate(conditions,1):
                svg=folder/f'{name}_{key}_{scale}x.svg'
                timing=inherited.crop_svg(saved/key/'output.svg',svg,box,scale)
                with Image.open(svg.with_suffix('.png')) as actual:image=rgb_on(actual)
                board.paste(image,(i*w*scale,28));draw.text((i*w*scale+1,6),SHORT[key],fill='black')
                measurements.append({'name':name,'box':box,'scale':scale,'condition':key,'actual_vector_viewport_render':True,'render':timing})
            board.save(folder/f'{name}_{scale}x.png')
    (folder/'zooms.json').write_text(json.dumps({'boxes':boxes,'measurements':measurements,'source_crop':'Nearest-neighbor source sample display; not high-resolution ground truth'},indent=2),encoding='utf-8')
    return boxes
```

### `metric_table` — `Lines 84–91`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `84` إلى السطر `91` (`Lines 84–91`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 84–91`):**
```python
def metric_table(result,background):
    parts=['<table><tr><th>Condition</th><th>SSIM</th><th>PSNR dB</th><th>MSE</th><th>Worst 32px RMSE</th><th>Mean DeltaE76</th><th>Alpha MAE</th></tr>']
    for key in ('pixel','Aflat','Agrad','B','C','truth'):
        if key not in result['conditions']:continue
        row=result['conditions'][key];m=row['metrics'][background]
        values=[key,m['ssim'],m['psnr_db'],m['mse'],m.get('worst_32px_tile_rmse'),m.get('delta_e76_mean'),row.get('alpha_mae')]
        parts.append('<tr>'+''.join('<td>'+number(value)+'</td>' for value in values)+'</tr>')
    return ''.join(parts)+'</table>'
```

### `build_presentation` — `Lines 93–127`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `93` إلى السطر `127` (`Lines 93–127`)
- **الوظيفة:** Require all nine results complete; refuse to replace presentation evidence.
- **الكود الفعلي (`Lines 93–127`):**
```python
def build_presentation():
    """Require all nine results complete; refuse to replace presentation evidence."""
    manifest=json.loads((ROOT/'inputs/manifest.json').read_text(encoding='utf-8'));cases=manifest['cases']
    if len(cases)!=9:raise ValueError('Expected nine preregistered cases')
    results={}
    for case in cases:
        file=ROOT/'results'/case['id']/'result.json'
        if not file.is_file():raise FileNotFoundError('Wait for parent completion; missing '+str(file))
        result=json.loads(file.read_text(encoding='utf-8'))
        if not all(k in result['conditions'] for k in ('Aflat','Agrad','B','C')):raise ValueError('Incomplete conditions '+case['id'])
        results[case['id']]=result
    output=ROOT/'presentation'
    if output.exists() and any(output.iterdir()):raise FileExistsError('Preserve prior presentation; choose a fresh experiment/export target')
    output.mkdir(exist_ok=True)
    order=sorted(cases,key=lambda c:min(v['ssim'] for v in results[c['id']]['conditions']['C']['metrics'].values()))
    cards=[]
    for case in order:
        cid=case['id'];result=results[cid];folder=output/cid;folder.mkdir()
        images,conditions=native_sheets(case,result,folder);boxes=actual_zoom_sheets(case,folder,images,conditions)
        worst=min(v['ssim'] for v in result['conditions']['C']['metrics'].values())
        cards.append(f'<section id="{cid}"><h2>{html.escape(cid)}</h2><p>{case["kind"]}; C worst-background SSIM {worst:.9f}. Native saved renders at {images["source"].width}×{images["source"].height}.</p>')
        c=result['conditions']['C'];ag=result['conditions']['Agrad']
        cards.append('<p>Balanced float three-background MSE: Agrad '+number(ag.get('float_three_background_mse'))+' → C '+number(c.get('float_three_background_mse'))+'. Held-out periodic-pixel MSE: '+number(ag.get('heldout_float_three_background_mse'))+' → '+number(c.get('heldout_float_three_background_mse'))+'. Geometry/mask invariant is checked separately in result.json.</p>')
        cards.append('<p>'+''.join(f'<a href="results/{cid}/{key}/output.svg">{key} full SVG</a> | ' for key in ('pixel','Aflat','Agrad','B','C','truth') if key in result['conditions'])+f'<a href="results/{cid}/source.png">Prepared source</a> | <a href="results/{cid}/result.json">All metrics</a> | <a href="results/{cid}/fitting.json">Fitting diagnostics</a> | <a href="results/{cid}/coverage/maps.json">Coverage-map diagnostics</a> | <a href="results/{cid}/coverage/maps.npz">Numerical maps</a></p>')
        for bg in BACKGROUND_COLORS:
            cards.append(f'<details {"open" if bg=="white" else ""}><summary>{bg}: native comparison, amplified errors and metrics</summary><figure><img loading="lazy" src="presentation/{cid}/comparison_{bg}.png"></figure><figure><img loading="lazy" src="presentation/{cid}/errors_{bg}.png"></figure>'+metric_table(result,bg)+'</details>')
        cards.append(f'<details><summary>Actual alpha and effective-mixture boundary mask</summary><figure><img loading="lazy" src="presentation/{cid}/alpha.png"></figure><img loading="lazy" src="results/{cid}/coverage/boundary_band.png"><p>The boundary band includes translucent interiors and is not physical contour ground truth. Fixed masks can retain source-grid dependence on real RGBA cases.</p></details>')
        for name,box in boxes:
            cards.append(f'<h3>{name}: source coordinates {box}</h3>')
            for scale in (1,4,16):
                cards.append(f'<details {"open" if scale==4 else ""}><summary>Actual SVG viewport {scale}× (S NN is raster sample display)</summary><figure><img loading="lazy" src="presentation/{cid}/{name}_{scale}x.png"></figure><p>'+''.join(f'<a href="presentation/{cid}/{name}_{key}_{scale}x.svg">{SHORT[key]} cropped SVG</a> | ' for key in conditions)+'</p></details>')
        cards.append(f'<a href="presentation/{cid}/zooms.json">Crop selection and render timing/memory</a></section>')
    document='''<!doctype html><html lang="en"><meta charset="utf-8"><title>Coverage-aware fixed-geometry fitting — owner review</title><style>body{font:16px system-ui;background:#161c24;color:#eee;margin:24px;line-height:1.5}header{max-width:1100px}section{border-top:2px solid #7089a5;margin-top:40px;padding-top:20px}figure{overflow:auto;margin:12px 0}img{max-width:none}td,th{border:1px solid #596b81;padding:5px;text-align:right}table{border-collapse:collapse}a{color:#9ad3ff}summary{cursor:pointer;padding:10px;background:#242f3e}details{margin:12px 0}h3{margin-top:28px}</style><header><h1>Coverage-aware fitting: owner visual review</h1><p>Research only. Global architecture NOT_APPROVED. All nine cases are shown, sorted worst C background SSIM first. Native metrics, geometry quality, approximation to the pixel reference and cross-category generalization are separate claims. A result is not successful merely because C improves Agrad.</p><p>S: prepared source; P: strongest saved pixel fidelity reference when available; Ag: inherited interior-only adaptive fit; B: coverage-aware flat; C: coverage-aware adaptive; T: known true vector control when available. Aflat is included in full metrics and SVG links. Analytic controls are causal fixtures, not real-image generalization evidence. New fixtures have no pixel baseline.</p><p>Comparison/error PNGs use saved actual native renders. Zoom SVGs are rendered directly at 1×,4×,16× from the original vector viewport; S NN is nearest-neighbor source raster display, not high-resolution ground truth. Error maps show absolute RGB error ×6 with saturation. Crop1 is the worst C complete 24px tile by balanced float three-background MSE; crop2 uses the fixture thin-feature location or image center. Curves and path geometry remain fixed; no stroke correction was introduced here.</p></header>'''+''.join(cards)+'</html>'
    (ROOT/'index.html').write_text(document,encoding='utf-8')
    return {'cases':len(cases),'order':[c['id'] for c in order],'dashboard':str(ROOT/'index.html'),'presentation':str(output)}
```

### `add_flat_comparisons` — `Lines 130–144`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `130` إلى السطر `144` (`Lines 130–144`)
- **الوظيفة:** Add explicit flat-pair negatives without repeating any vector rendering.
- **الكود الفعلي (`Lines 130–144`):**
```python
def add_flat_comparisons():
    """Add explicit flat-pair negatives without repeating any vector rendering."""
    document=(ROOT/'index.html').read_text(encoding='utf-8')
    for case in json.loads((ROOT/'inputs/manifest.json').read_text())['cases']:
        cid=case['id'];saved=ROOT/'results'/cid;folder=ROOT/'presentation'/cid
        source=rgb_on(Image.open(saved/'source.png'));a=rgb_on(Image.open(saved/'Aflat/render.png'));b=rgb_on(Image.open(saved/'B/render.png'))
        ref=np.asarray(source,dtype=float);w,h=source.size;column=max(w,180)
        pictures=[('Source',source),('Aflat interior',a),('B coverage flat',b)]
        for label,image in [('Aflat error x6',a),('B error x6',b)]:pictures.append((label,Image.fromarray(np.uint8(np.clip(np.abs(ref-np.asarray(image,dtype=float))*6,0,255)))))
        sheet=Image.new('RGB',(column*5,h+30),'white');draw=ImageDraw.Draw(sheet)
        for i,(label,image) in enumerate(pictures):draw.text((i*column+3,5),label,fill='black');sheet.paste(image,(i*column,28))
        sheet.save(folder/'flat_pair_white.png')
        heading=f'<h2>{cid}</h2>'
        if f'presentation/{cid}/flat_pair_white.png' not in document:document=document.replace(heading,heading+f'<details><summary>Flat comparison: inspect SSIM regressions as well as MSE gains</summary><figure><img loading="lazy" src="presentation/{cid}/flat_pair_white.png"></figure></details>')
    (ROOT/'index.html').write_text(document,encoding='utf-8')
```
