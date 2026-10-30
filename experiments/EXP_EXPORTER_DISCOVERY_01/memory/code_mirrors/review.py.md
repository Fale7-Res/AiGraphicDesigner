# مرآة الكود التفصيلية: `review.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `review.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `review.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `61` (`Lines 1–61`)
- **بصمة الملف (`SHA-256`):** `20532d2833d16e29532662c7586880db1893a34288589ecefc28fee5f32238f6`
- **الوصف التفصيلي:** # START CHANGE AGD-EXPORT-REVIEW | 2026-10-29T22:12:25Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `build` | `function` | `Lines 12–57` | `def build():` | رمز برمجي موثق. |
| `build.pic` | `nested_function` | `Lines 16–16` | `def pic(base,name,label,link=None):return f'<figure><a href="{base}/{link or name}"><img loading="lazy" src="{base}/{name}" alt="{html.escape(label)}"></a><figcaption>{html.escape(label)}</figcaption></figure>'` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `build` — `Lines 12–57`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `12` إلى السطر `57` (`Lines 12–57`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 12–57`):**
```python
def build():
    body=['<h1>SVG correctness → matched fitting → source-driven strokes</h1><p class="warn">Geometry NOT_ACCEPTED · Architecture NOT_APPROVED. Exporter correctness and local safety gains do not establish complete artwork. Fine discovery accepted0; Arabic hypothetical union deteriorates. Failures remain visible.</p>',
    '<p><a href="REPORT.md">Technical report</a> · <a href="protocol.json">Frozen protocol</a> · <a href="reports/QA_FINAL_REVIEW.md">Independent QA</a> · <a href="reports/NEXT_MILESTONE_ML.md">Classical / pretrained ML / hybrid recommendation</a></p>',
    '<p>O original frozen graph; R decomposed face walks; B previous guard; RB unchanged guard after R; A previous endpoint discovery. All are newly serialized correctly. C is separate source-only stroke proposals, not shared-graph integration.</p>']
    def pic(base,name,label,link=None):return f'<figure><a href="{base}/{link or name}"><img loading="lazy" src="{base}/{name}" alt="{html.escape(label)}"></a><figcaption>{html.escape(label)}</figcaption></figure>'
    for case in json.loads((ROOT/'protocol.json').read_text())['phase_b']['cases']:
        out=destination(case);base=out.as_uri() if case=='fine_features' else 'results/'+case;rgb=Image.open(out/'working.png').convert('RGB');w,h=rgb.size
        labels=np.load(out/'labels.npy',allow_pickle=False);palette=np.array([label_rgb(i) for i in range(int(labels.max())+1)],np.uint8);Image.fromarray(palette[labels]).save(out/'labels.png')
        body.append(f'<section id="{case}"><h2>{case}</h2><div class="grid">'+pic(base,'working.png','Original raster')+pic(base,'labels.png','Frozen segmentation: phase B unchanged'))
        old=(WORK/'thin_structure_topology/external_results' if case=='fine_features' else THIN/'results')/case
        if (old/'pixel_reference.svg').exists():
            for ext in ['svg','png']:shutil.copy2(old/('pixel_reference.'+ext),out/('pixel_reference.'+ext))
            body.append(pic(base,'pixel_reference.png','Saved pixel-equivalent fidelity reference, not final geometry','pixel_reference.svg'))
        body.append('</div><h3>Exporter correction at identical geometry</h3><div class="grid">'+pic(base,'O_legacy_regions.png','Historical compound-region export at8x: affected','O_legacy_regions.svg')+pic(base,'O_regions_8x.png','Corrected export at8x: same controls and labels','O_regions.svg')+pic(base,'R_regions_8x.png','Corrected decomposed export: equivalent','R_regions.svg')+'</div>')
        names=[n for n in ['O','A','B','R','RB'] if (out/(n+'_metrics.json')).exists()];body.append('<table><tr><th>Condition</th><th>Ring count</th><th>Invalid fit</th><th>Collapsed</th><th>Cross/overlap</th></tr>')
        for n in names:
            m=json.loads((out/(n+'_metrics.json')).read_text());body.append(f'<tr><td>{n}</td><td>{len(m["rings"])}</td><td>{m["invalid_fit_rings"]}</td><td>{m["raw_nonzero_fit_degenerate_rings"]}</td><td>{m["crossing_or_overlap_pairs"]}</td></tr>')
        body.append('</table><p>Ring denominators change after decomposition. Fewer invalid rings are not a complete-reconstruction pass.</p><div class="grid">')
        for n in ['O','R','RB']:body.append(pic(base,n+'_curves.png',n+' actual curve drawing',n+'_curves.svg'))
        body.append('</div>')
        if case=='A01_shield':body.append('<h3>Dedicated crown: tips, valleys, ornament, upper/lower band</h3><p>Also inspect frame and red/gold interfaces in the full drawing. Approximate1.2–2px guides do not certify1pxaccuracy; sparse Cstrokes do not reconstruct the crown.</p>')
        if case=='G06_arabic':body.append('<p>Actual counters, stems and connections must be inspected. Source-threshold counts are not independent glyph-outline truth; hypothetical union harms the proxy.</p>')
        c=json.loads((out/'discovery/proposals.json').read_text());m=json.loads((out/'discovery/METRICS.json').read_text());body.append(f'<h3>Source-driven proposal experiment</h3><p>Acceptedsourceproposals: {len(c["accepted"])}; rejectedchains: {len(c["rejected"])}. Shared-graph integration: NOT ESTABLISHED. Candidate confidence is a contrast heuristic.</p>')
        proposals=Image.open(out/'discovery/proposals_native.png').convert('RGBA');over=rgb.convert('RGBA');over.alpha_composite(proposals);over.convert('RGB').save(out/'discovery/source_proposals_overlay.png')
        rejected=rgb.copy();d=ImageDraw.Draw(rejected)
        for p in c['rejected']:
            if len(p['source_points_xy'])>=2:d.line([tuple(q) for q in p['source_points_xy']],fill='#eb3344',width=1)
        rejected.save(out/'discovery/rejected_source_traces.png')
        body.append('<div class="grid">'+pic(base,'discovery/proposals_native.png','Actual cubic stroke proposals only','discovery/proposals.svg')+pic(base,'discovery/source_proposals_overlay.png','Proposals over source: inspection PNG only','discovery/proposals.svg')+pic(base,'discovery/rejected_source_traces.png','Red source traces rejected by frozen checks; not exported fallback geometry')+'</div>')
        x,y,cw,ch=DETAIL[case];rgb.crop((x,y,x+cw,y+ch)).resize((cw*4,ch*4),Image.Resampling.NEAREST).save(out/'source_detail_pixels_4x.png');body.append('<div class="grid">'+pic(base,'source_detail_pixels_4x.png','Enlarged raster pixels, not high-resolution contour truth')+'</div>')
        combined=ET.parse(out/'O_curves.svg').getroot();new=ET.parse(out/'discovery/proposals.svg').getroot()
        for e in new:combined.append(copy.deepcopy(e))
        p=out/'discovery/overlay_geometry.svg';p.write_text(ET.tostring(combined,encoding='unicode'),encoding='utf-8')
        for scale in [1,4,16]:
            body.append(f'<details {"open" if scale==4 else ""}><summary>True SVG detail {scale}×</summary><div class="grid">')
            for n,path in [('O',out/'O_curves.svg'),('RB',out/'RB_curves.svg'),('C proposals',out/'discovery/proposals.svg'),('O + C unintegrated overlay',p)]:
                tree=ET.parse(path).getroot();tree.set('viewBox',f'{x} {y} {cw} {ch}');tree.set('width',str(cw*scale));tree.set('height',str(ch*scale));target=out/('review_'+n.replace(' ','_').replace('+','plus')+f'_{scale}x.svg');target.write_text(ET.tostring(tree,encoding='unicode'),encoding='utf-8');render_size(target,target.with_suffix('.png'),cw,ch,scale);body.append(pic(base,target.with_suffix('.png').name,n+' actual SVG detail',target.name))
            body.append('</div></details>')
        body.append('<h3>Errors and topology warnings</h3><p>Red/green masks show truth/prediction only where independent controls exist; Arabic is a source proxy. Painted union is not safely integrated topology.</p><div class="grid">')
        for n in ['O','RB']:
            if (out/(n+'_known_error.png')).exists():body.append(pic(base,n+'_known_error.png',n+' known-vector error'))
        for name in ['proposal_only_error.png','hypothetical_union_error.png','hypothetical_union.png']:
            if (out/'discovery'/name).exists():body.append(pic(base,'discovery/'+name,name,'discovery/hypothetical_union.svg' if name=='hypothetical_union.png' else None))
        body.append('</div></section>')
    css='body{font:16px system-ui;margin:24px;background:#edf1f4;color:#142132}.warn{padding:18px;background:#ffe7b2}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px}figure{margin:0;background:white;padding:10px;border:1px solid #abc}img{max-width:100%;background:white}figcaption{font-size:13px}section{border-top:3px solid #789;margin-top:30px}td,th{padding:8px;border:1px solid #abc}table{border-collapse:collapse;background:white}summary{padding:15px;cursor:pointer}'
    (ROOT/'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Exporter and geometry discovery</title><style>'+css+'</style>'+''.join(body)+'</html>',encoding='utf-8')
```

### `build.pic` — `Lines 16–16`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `16` (`Lines 16–16`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 16–16`):**
```python
    def pic(base,name,label,link=None):return f'<figure><a href="{base}/{link or name}"><img loading="lazy" src="{base}/{name}" alt="{html.escape(label)}"></a><figcaption>{html.escape(label)}</figcaption></figure>'
```
