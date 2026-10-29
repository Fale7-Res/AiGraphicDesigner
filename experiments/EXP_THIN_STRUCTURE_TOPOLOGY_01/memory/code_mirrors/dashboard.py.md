# مرآة الكود التفصيلية: `dashboard.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `dashboard.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `dashboard.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `78` (`Lines 1–78`)
- **بصمة الملف (`SHA-256`):** `65d4584eed6e4ef4db1e4d6a25c75789be4f60bbd1a79a99e69090a75cffd700`
- **الوصف التفصيلي:** # START CHANGE AGD-THIN-DASHBOARD | 2026-10-29T08:39:37Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `package` | `function` | `Lines 13–74` | `def package():` | رمز برمجي موثق. |
| `package.picture` | `nested_function` | `Lines 18–19` | `def picture(base,name,label,link=None):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `package` — `Lines 13–74`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `74` (`Lines 13–74`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 13–74`):**
```python
def package():
    body=['<h1>Thin-structure discovery × topology-safe initialization</h1><p class="warning">Experimental geometry, NOT_ACCEPTED; architecture NOT_APPROVED. No new appearance engine. All conditions and failures remain visible.</p>',
      '<p><a href="REPORT.md">Technical report</a> · <a href="protocol.json">Frozen protocol</a> · <a href="reports/SUMMARY.json">Full results</a></p>']
    body.append('<p><b>Negative results:</b> fine-feature fragmentation remains; Shield crown recovery is not demonstrated. B repairs three K01 and two Arabic rings without establishing complete geometry. Combined conditions were skipped under frozen rules.</p>')
    body.append('<nav>'+ ' · '.join(f'<a href="#{c}">{c}</a>' for c in CASES)+'</nav>')
    def picture(base,name,label,link=None):
        return f'<figure><a href="{base}/{link or name}"><img loading="lazy" src="{base}/{name}" alt="{html.escape(label)}"></a><figcaption>{html.escape(label)}</figcaption></figure>'
    for case in CASES:
        out=destination(case);base=out.as_uri() if case=='fine_features' else 'results/'+case
        conditions=[n for n in ['baseline','A','B','AB'] if (out/(n+'_metrics.json')).exists()]
        body.append(f'<section id="{case}"><h2>{case}</h2><div class="grid">')
        body.append(picture(base,'working.png','Original opaque working raster'))
        old=inherited_case_dir(case)
        if (old/'pixel_reference.svg').exists():
            import shutil
            for suffix in ['svg','png']:shutil.copy2(old/('pixel_reference.'+suffix),out/('pixel_reference.'+suffix))
            body.append(picture(base,'pixel_reference.png','Strongest saved pixel-equivalent reference','pixel_reference.svg'))
        body.append('</div>')
        if case=='A01_shield':body.append('<p>Dedicated complete crown comparison. Tips/lobes/flanks/ornament/both band edges must be reviewed individually. Inherited1.2–2px annotation uncertainty cannot certify1px accuracy.</p>')
        if case=='G06_arabic':body.append('<p>Inspect counter, isolated marks, thin stems and connections. Raster-derived topology proxy is not independent font-outline truth.</p>')
        body.append('<div class="grid">')
        body.append(picture(base,'A_bridge_locations.png','Accepted source-supported connectors: red; endpoints: blue. No marks means no accepted connector.'))
        for evidence in sorted(out.glob('A_evidence_*.png')):
            if 'endpoint' not in evidence.stem:body.append(picture(base,evidence.name,'Source discovery evidence: '+evidence.stem))
        body.append('</div><table><tr><th>Condition</th><th>Collapsed rings</th><th>Invalid rings</th><th>Crossings</th><th>Known IoU</th><th>Status</th></tr>')
        for name in conditions:
            m=json.loads((out/(name+'_metrics.json')).read_text(encoding='utf-8'))
            iou=m.get('known_geometry',{}).get('foreground_iou');iou=f'{iou:.6f}' if iou is not None else 'not independentGT'
            body.append(f'<tr><td>{name}</td><td>{m["raw_nonzero_fit_degenerate_rings"]}</td><td>{m["invalid_fit_rings"]}</td><td>{m["crossing_or_overlap_pairs"]}</td><td>{iou}</td><td>{m["geometry_acceptance"]}</td></tr>')
        body.append('</table><h3>Full drawing, raw boundary and segmentation</h3><div class="grid">')
        for name in conditions:
            labels=np.load(out/(name+'_labels.npy'),allow_pickle=False);palette=np.array([label_rgb(i) for i in range(int(labels.max())+1)],dtype=np.uint8);Image.fromarray(palette[labels]).save(out/(name+'_labels.png'))
            body.append(picture(base,name+'_labels.png',name+' region labels, arbitrary colors'))
            body.append(picture(base,name+'_raw.png',name+' raw cracks',name+'_raw.svg'))
            body.append(picture(base,name+'_curves.png',name+' fitted curves',name+'_curves.svg'))
        body.append('</div>')
        x,y,w,h=DETAIL[case]
        for scale in [1,4,16]:
            body.append(f'<details {"open" if scale==4 else ""}><summary>True SVG detail at{scale}×</summary><div class="grid">')
            for name in conditions:
                root=ET.parse(out/(name+'_curves.svg')).getroot();root.set('viewBox',f'{x} {y} {w} {h}');root.set('width',str(w*scale));root.set('height',str(h*scale))
                path=out/(name+f'_review_{scale}x.svg');path.write_text(ET.tostring(root,encoding='unicode'),encoding='utf-8');render(path,path.with_suffix('.png'))
                body.append(picture(base,path.with_suffix('.png').name,name+' actualSVG detail',path.name))
            body.append('</div></details>')
        body.append('<h3>Local diagnostic overlays and errors</h3><p>Red=raw cracks, cyan=fitted geometry. Raster background is inspection guidance, not an exported vector underlay.</p><div class="grid">')
        for name in conditions:
            g=json.loads((out/(name+'.json')).read_text(encoding='utf-8'));raw=ET.fromstring(svg_graph(g,raw=True));fit=ET.fromstring(svg_graph(g))
            for tree,color in [(raw,'#ef3340'),(fit,'#00a4c7')]:
                for node in tree:node.set('stroke',color);node.set('stroke-width','.55')
            for node in fit:raw.append(copy.deepcopy(node))
            path=out/(name+'_overlay.svg');path.write_text(ET.tostring(raw,encoding='unicode'),encoding='utf-8');render(path,path.with_suffix('.png'))
            im=Image.open(out/'working.png').convert('RGBA');im.alpha_composite(Image.open(path.with_suffix('.png')).convert('RGBA'));im.convert('RGB').save(out/(name+'_source_overlay.png'))
            body.append(picture(base,name+'_source_overlay.png',name+' source overlay',name+'_overlay.svg'))
            if (out/(name+'_known_error.png')).exists():body.append(picture(base,name+'_known_error.png',name+' independent known-mask error',name+'_foreground.svg'))
        body.append('</div></section>')
        body.append('<h3>Short-chain mechanism: raw / original / guarded</h3><p>Accepted changes where present; otherwise rejected proposal group remains unchanged. Local support is not a complete-artwork certificate.</p><div class="grid">')
        for name in ['raw','original','safe']:
            path=out/('B_mechanism_'+name+'.png')
            if path.exists():body.append(picture(base,path.name,'B mechanism '+name,path.with_suffix('.svg').name))
        body.append('</div>')
    css='body{font:16px system-ui;margin:24px;background:#eee;color:#142132}.warning{padding:18px;background:#fff0bf}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px}figure{margin:0;padding:8px;background:white;border:1px solid #bcd}img{max-width:100%;background:white}figcaption{font-size:13px;margin:8px}section{border-top:3px solid #789;margin-top:32px}td,th{padding:7px;border:1px solid #abc}table{background:white;border-collapse:collapse}summary{cursor:pointer;padding:15px}'
    (ROOT/'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Thin structure geometry review</title><style>'+css+'</style>'+''.join(body)+'</html>',encoding='utf-8')
```

### `package.picture` — `Lines 18–19`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `19` (`Lines 18–19`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 18–19`):**
```python
    def picture(base,name,label,link=None):
        return f'<figure><a href="{base}/{link or name}"><img loading="lazy" src="{base}/{name}" alt="{html.escape(label)}"></a><figcaption>{html.escape(label)}</figcaption></figure>'
```
