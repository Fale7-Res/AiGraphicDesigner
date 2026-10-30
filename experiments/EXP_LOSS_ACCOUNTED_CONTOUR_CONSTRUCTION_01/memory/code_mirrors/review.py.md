# مرآة الكود التفصيلية: `review.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `review.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `review.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `47` (`Lines 1–47`)
- **بصمة الملف (`SHA-256`):** `3b8cc26de0a218f300d9775ccdd5e2da1a91b81fd9daad02b1e9e9bdf971b62d`
- **الوصف التفصيلي:** # START CHANGE AGD-CONTOUR-CLOSURE | 2026-10-30T15:21:28Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `dashboard` | `function` | `Lines 6–42` | `def dashboard(target,include_local):` | رمز برمجي موثق. |
| `dashboard.image` | `nested_function` | `Lines 9–9` | `def image(p,title):return '<figure><a href="'+html.escape(link(p))+'"><img loading="lazy" src="'+html.escape(link(p))+'"></a><figcaption>'+html.escape(title)+'</figcaption></figure>'` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `dashboard` — `Lines 6–42`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `6` إلى السطر `42` (`Lines 6–42`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 6–42`):**
```python
def dashboard(target,include_local):
    target=Path(target);target.mkdir(parents=True,exist_ok=True);protocol=json.loads((E/'protocol.json').read_text());metrics=json.loads((E/'reports/METRICS.json').read_text());parts=[]
    link=lambda p:os.path.relpath(p,target).replace('\\','/')
    def image(p,title):return '<figure><a href="'+html.escape(link(p))+'"><img loading="lazy" src="'+html.escape(link(p))+'"></a><figcaption>'+html.escape(title)+'</figcaption></figure>'
    for case,paths in protocol['cases'].items():
        if case=='fine_features' and not include_local:
            parts.append('<section><h2>Fine Features — local-only</h2><p>Full evidence is retained in the owner-local dashboard. External fixture redistribution rights are unresolved. Its aggregate metrics and hash manifest remain public; no pass is hidden.</p></section>');continue
        source=Path(paths['source']);base=Path(paths['base']);intro='<h2>'+case+'</h2><div class="grid">'+image(source,'Frozen source raster; evidence only')
        if (source.parent/'pixel_reference.png').exists():intro+=image(source.parent/'pixel_reference.png','Saved high-fidelity pixel-equivalent reference, not desired final geometry')
        intro+='</div>'
        for arm in protocol['arms']:
            out=destination(case,arm);rr=[x for x in metrics if x['case']==case and x['arm']==arm]
            block='<h3>'+arm+' — identical frozen detection</h3><div class="grid">'+image(base/arm/'support_overlay.png','Frozen detected evidence; never rerun')+image(out/'comparison_sheet.png','Source / O saved / P partitioned / Q periodic; candidate panels are geometry ONLY')+'</div>'
            block+='<table><tr><th>Construction</th><th>Selected length retained</th><th>Raw total retained</th><th>Paths / cubics</th><th>Closed contours</th><th>Recall / precision*</th></tr>'
            for m in rr:
                b=m.get('boundary_1_25px',{}).get('fitted',{});value=f'{b["recall"]:.3f} / {b["precision"]:.3f}' if b else 'No full boundary truth'
                block+=f'<tr><td>{m["condition"]}</td><td>{m["retained_selected_length_fraction"]:.1%}</td><td>{m["retained_total_length_fraction"]:.1%}</td><td>{m["vector"]["paths"]} / {m["vector"]["cubics"]}</td><td>{len(m["topology"]["closed_loops"])}</td><td>{value}</td></tr>'
            block+='</table><p>*Known-mask or raster proxy; K01 interior material edges are outside its foreground-only mask boundary. These scores do not certify all structural contours.</p><div class="grid">'
            for condition in ['O','P','Q']:
                block+=image(out/(condition+'_1x.png'),condition+' actual native SVG render')+image(out/(condition+'_detail_16x.png'),condition+' actual16×SVG detail render')
            block+='</div>'
            block+='<div class="grid">'+image(out/'P_loss_overlay.png','P raster loss diagnostic: accepted green, excluded/rejected red. Not exported artwork.')+image(out/'Q_loss_overlay.png','Q raster loss diagnostic; any missing loop remains failed.')+'</div>'
            for condition in ['O','P','Q']:
                block+='<p>'+condition+': <a href="'+link(out/(condition+'.svg'))+'">full SVG</a> · <a href="'+link(out/(condition+'_4x.png'))+'">true full4×render</a> · <a href="'+link(out/(condition+'_detail.svg'))+'">detail SVG</a> · <a href="'+link(out/(condition+'_detail_4x.png'))+'">detail4×</a> · <a href="'+link(out/(condition+'_metrics.json'))+'">metrics</a>'
                if condition!='O':block+=' · <a href="'+link(out/(condition+'_loss_ledger.csv'))+'">per-interval loss CSV</a> · <a href="'+link(out/(condition+'.json'))+'">all controls/rejections</a>'
                block+='</p>'
            if case=='A01_shield':
                block+='<h4>Dedicated entire-crown comparison</h4><p>True16×SVG crop covers tips, valleys, ornament and both bands. Outer silhouette recovery does NOT establish complete crown artwork. Guides remain uncertain by1.2–2px.</p><table><tr><th>Guide</th><th>Raw / selected</th><th>O</th><th>P</th><th>Q</th></tr>'
                for i,g in enumerate(rr[0]['critical_guides']):block+='<tr><td>'+g['id']+'</td><td>'+f'{g["raw"]["recall"]:.3f} / {g["selected"]["recall"]:.3f}'+'</td>'+''.join(f'<td>{m["critical_guides"][i]["fitted"]["recall"]:.3f}</td>' for m in rr)+'</tr>'
                block+='</table>'
            if case=='K01_linear_corner_hole':block+='<p class="warn">O is empty. P/Q recover three closed contours, but the quadrilateral is decoration, not automatically a hole. Staircase jitter remains. This is contour construction evidence, not accepted professional regions.</p><p>Cap-only diagnostic remains EMPTY: increasing the old fitter cap64→512 alone still rejects allthree traces. <a href="'+link(out/'CAP512.svg')+'">actual diagnostic SVG</a> · <a href="'+link(out/'CAP512.json')+'">frozen diagnostic results</a></p>'
            if case=='G06_arabic' and arm=='Classical':block+='<p class="warn">Q rejects one periodic modification and loses one closed loop. P retains all seven detected closed loops. Neither proves independent glyph/counter truth.</p>'
            intro+='<article>'+block+'</article>'
        parts.append('<section>'+intro+'</section>')
    head='''<!doctype html><html lang="en"><meta charset="utf-8"><title>Loss-accounted contour construction</title><style>body{font:16px system-ui;background:#f1f4f6;color:#17232b;margin:24px}section,article{background:white;padding:18px;margin:20px 0}article{border:1px solid #cbd2d9}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}figure{margin:0}img{max-width:100%;max-height:380px;object-fit:contain;background:white}figcaption{font-size:14px}table{border-collapse:collapse;font-size:14px}th,td{padding:6px;border:1px solid #aaa}.warn{color:#a22;font-weight:bold}a{color:#045aa1}</style><h1>Loss-accounted contour construction</h1><p class="warn">Geometry NOT_ACCEPTED · Architecture NOT_APPROVED · No appearance reconstruction</p><p>Saved O vs partitioned P vs periodic Q, across Classical/ML/Hybrid frozen evidence. No detector inference, new models or changed thresholds. Every raw trace edge is accounted for; short and top128 exclusions remain explicit.</p><p>P restores major Arabic/K01 contour support. Shield crown remains incomplete. Q is not consistently better and loses one Arabic closed loop. Retained pixel-scale staircases and lighting traces remain visible; no professional vector acceptance is claimed.</p><p>All geometry panels are true SVG renders. Source/evidence/loss overlays are explicitly diagnostics. Closed strokes are not completed filled regions.16×views rerender an SVGviewBox and are not enlarged sourcepixels.</p>'''
    navigation='<p><a href="'+link(E/'REPORT.md')+'">Technical report</a> · <a href="'+link(E/'protocol.json')+'">Frozen protocol</a> · <a href="'+link(E/'reports/METRICS.json')+'">Full metrics</a></p>'
    (target/'review.html').write_text(head+navigation+''.join(parts)+'</html>',encoding='utf-8')
```

### `dashboard.image` — `Lines 9–9`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `9` (`Lines 9–9`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–9`):**
```python
    def image(p,title):return '<figure><a href="'+html.escape(link(p))+'"><img loading="lazy" src="'+html.escape(link(p))+'"></a><figcaption>'+html.escape(title)+'</figcaption></figure>'
```
