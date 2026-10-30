# START CHANGE AGD-ML-PACKAGE | 2026-10-30T08:17:45Z | CREATED | Author: root
from construct_geometry import R,E,W,paths
from pathlib import Path
import json,html,shutil,os
from PIL import Image,ImageDraw,ImageOps
import numpy as np

def image_link(path,label):
    return '<figure><a href="'+html.escape(path)+'"><img loading="lazy" src="'+html.escape(path)+'"></a><figcaption>'+html.escape(label)+'</figcaption></figure>'

def make_review(target,local_delivery=False):
    target=Path(target);target.mkdir(parents=True,exist_ok=True)
    rows=json.loads((E/'reports/METRICS.json').read_text());cases=list(dict.fromkeys(x['case'] for x in rows));sections=[]
    link=lambda p:os.path.relpath(p,target).replace('\\','/')
    for case in cases:
        base,source=paths(case);rgb=Image.open(source).convert('RGB');w,h=rgb.size
        if case=='fine_features' and not local_delivery:
            sections.append('<section><h2>fine_features — local-only evidence</h2><p>Rights for the supplied Arena fixture are unresolved. Metrics below remain disclosed; SVGs and renders are available in the local owner dashboard. No fixture/derivative images are redistributed in Git.</p></section>');continue
        cards=image_link(link(source),'Source raster — reference evidence, no final appearance fitting')
        inp=source.parent
        if (inp/'O_curves.svg').exists():cards+=image_link(link(inp/'O_curves.svg'),'Inherited corrected-export geometry, unchanged')
        if (inp/'pixel_reference.png').exists():cards+=image_link(link(inp/'pixel_reference.png'),'Saved high-fidelity pixel-equivalent reference; not desired geometry')
        if (inp/'labels.png').exists():cards+=image_link(link(inp/'labels.png'),'Frozen segmentation visualization')
        cards+=image_link(link(base/'ML/sigmoid.png'),'Raw DexiNed sigmoid; heatmap is NOT vector reconstruction')
        table=[];sheets=[('Source',rgb)]
        for arm in ['Classical','ML','Hybrid']:
            folder=base/arm;m=next(x for x in rows if x['case']==case and x['arm']==arm)
            cards+=image_link(link(folder/'support_overlay.png'),arm+' pre-fit evidence on source')
            cards+=image_link(link(folder/'stable_1x.png'),arm+' actual SVG render 1×; diagnostic .35px strokes')
            cards+=image_link(link(folder/'detail_16x.png'),arm+' true SVG detail render 16×')
            cards+='<p><a href="'+link(folder/'stable.svg')+'">'+arm+' full SVG</a> · <a href="'+link(folder/'old.svg')+'">old fitter SVG</a> · <a href="'+link(folder/'stable_4x.png')+'">full 4×</a> · <a href="'+link(folder/'detail_4x.png')+'">detail 4×</a> · <a href="'+link(folder/'detail.svg')+'">detail SVG</a> · <a href="'+link(folder/'construction.json')+'">all accepted/rejected traces</a> · <a href="'+link(folder/'metrics.json')+'">metrics</a></p>'
            b=m.get('boundary_1_25px',{});raw=b.get('raw_all',{}).get('recall');fit=b.get('fitted',{}).get('recall')
            table.append(f'<tr><td>{arm}</td><td>{m["discovery"]["components8"]}</td><td>{m["vector"]["paths"]}</td><td>{m["vector"]["cubics"]}</td><td>{raw}</td><td>{fit}</td></tr>')
            rgba=Image.open(folder/'stable_1x.png').convert('RGBA');white=Image.new('RGBA',rgba.size,'white');white.alpha_composite(rgba)
            sheets.append((arm+' geometry ONLY',white.convert('RGB')))
        sheet=Image.new('RGB',(4*370,320),'white');draw=ImageDraw.Draw(sheet)
        for i,(label,img) in enumerate(sheets):
            draw.text((i*370+8,8),label,fill='black');thumb=ImageOps.contain(img,(354,280));sheet.paste(thumb,(i*370+8,32))
        sheet.save(base/'comparison_sheet.png');cards+=image_link(link(base/'comparison_sheet.png'),'Source versus actual geometry ONLY; missing regions remain visible')
        special=''
        if case=='A01_shield':
            special='<h3>Entire crown: tips, valleys, ornament, flanks and bands</h3><p>16× panes render viewBox115,70,145,100 directly from SVG. No enlarged raster is used as proof of geometry. All candidates remain incomplete; no strict1px claim from uncertain guides.</p><table><tr><th>Critical guide</th><th>CV raw→fit</th><th>ML raw→fit</th><th>Hybrid raw→fit</th></tr>'
            rr=[x for x in rows if x['case']==case]
            for i,g in enumerate(rr[0]['critical_guides']):
                special+='<tr><td>'+g['id']+'</td>'+''.join(f'<td>{a["critical_guides"][i]["raw"]["recall"]:.3f} → {a["critical_guides"][i]["fitted"]["recall"]:.3f}</td>' for a in rr)+'</tr>'
            special+='</table><p>Guide proximity is evidence support, not semantic region correspondence; appearance-only guide rows are not required structural boundaries.</p>'
        if case=='K01_linear_corner_hole':special+='<p class="bad">All candidate SVGs are EMPTY. Raw boundaries were detected; downstream fitting rejected every whole contour. This is a mandatory control failure, not a successful low-complexity SVG.</p>'
        sections.append('<section><h2>'+case+'</h2><table><tr><th>Arm</th><th>Skeleton components (not regions)</th><th>Paths</th><th>Cubics</th><th>Raw boundary recall</th><th>Fitted recall</th></tr>'+''.join(table)+'</table>'+special+'<div class="grid">'+cards+'</div></section>')
    if local_delivery:
        f=W/'ml_geometry/fitting_control/replication'
        sections.append('<section><h2>Independent frozen-trace fitting control</h2><p>Same two previously rejected source traces; unchanged0.6px numerical gate. New fitter accepts both with36/37cubics versus31/36. This repairs overshoot only; correct four-component geometry remains NOT_ESTABLISHED.</p><div class="grid">'+image_link(link(f/'old_rejected_4x.png'),'Old rejected geometry, true4×SVG render')+image_link(link(f/'new_control_4x.png'),'New bounded fitter, true4×SVG render')+image_link(link(f/'overlay_16x.png'),'Old/new/raw diagnostic overlay, actual16×SVG render')+'</div><a href="'+link(f/'new_control.svg')+'">new SVG</a> · <a href="'+link(f/'old_rejected.svg')+'">old rejected SVG</a></section>')
    header='''<!doctype html><html lang="en"><meta charset="utf-8"><title>Classical CV vs pretrained ML vs hybrid geometry</title><style>body{font:16px system-ui;margin:24px;background:#f4f6f8;color:#18212a}section{background:white;padding:18px;margin:24px 0}table{border-collapse:collapse;font-size:14px}td,th{border:1px solid #bbb;padding:6px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:18px}figure{margin:0}img{max-width:100%;max-height:360px;object-fit:contain;background:white}figcaption{font-size:14px}.bad{color:#a80000;font-weight:bold}</style><h1>Geometry research: Classical CV / DexiNed / Hybrid</h1><p class="bad">Geometry NOT_ACCEPTED · Architecture NOT_APPROVED · No appearance reconstruction</p><p>NO overall winner. DexiNed256 runs locally but loses important Shield/Arabic detail; hybrid is not consistently better. Common curve construction discards long contours. K01 is an explicit failure.</p><p>512px inference exceeded1.5GiB and stopped; one256px resource fallback was frozen before its inference outputs. SAM2.1 is SKIPPED_RESOURCE by feasibility screening, not measured failure. No training, paid API, or source upload.</p><p>Classical native resolution vs learned256 is the deployable resource comparison, not equal-resolution network superiority. Display strokes are actually0.35px, differing from protocol0.7; geometry/support metrics use centerlines separately. Thin/reference proxies do not prove holes/region ownership.</p>'''
    (target/'review.html').write_text(header+''.join(sections)+'</html>',encoding='utf-8')

if __name__=='__main__':
    make_review(E)
    make_review(Path.cwd()/'outputs/ml_geometry_review',True)

# END CHANGE AGD-ML-PACKAGE | 2026-10-30T08:17:45Z | CREATED | Author: root
