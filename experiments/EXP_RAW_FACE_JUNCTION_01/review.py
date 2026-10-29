# START CHANGE AGD-RAWFACE-REVIEW | 2026-10-29T12:39:51Z | CREATED | Author: root
"""Owner review of saved geometry and separate source evidence; no reconstruction."""
from run_case import ROOT,OLD,WORK,destination,dump
import json,copy,html,shutil
from xml.etree import ElementTree as ET
import numpy as np
from PIL import Image,ImageDraw
from geometry_eval import svg_graph,label_rgb,ring_points,chain_points
from analyze_matrix import render

DETAIL={'fine_features':(0,0,128,96),'G06_arabic':(100,60,110,180),'A01_shield':(118,65,136,100),'K01_linear_corner_hole':(20,20,100,100)}

def build():
    body=['<h1>Raw-face / junction validity isolation</h1><p class="warn">Geometry NOT_ACCEPTED · Architecture NOT_APPROVED. Representation repair did not recover missing artwork. Three follow-on fitting tests were STOPPED by the frozen fitted-export equivalence gate.</p>',
    '<p><a href="REPORT.md">Full report</a> · <a href="protocol.json">Frozen protocol</a> · <a href="reports/SUMMARY.json">Metrics</a> · <a href="reports/QA_FINAL_REVIEW.md">Independent QA</a></p>',
    '<p>O = saved original; R = same curves and labels, decomposed face walks; B = saved previous guard; RB = unchanged guard after R, executed only on K01. Region colors are diagnostic IDs, not appearance reconstruction.</p>']
    def pic(base,name,label,link=None):return f'<figure><a href="{base}/{link or name}"><img loading="lazy" src="{base}/{name}" alt="{html.escape(label)}"></a><figcaption>{html.escape(label)}</figcaption></figure>'
    for case in json.loads((ROOT/'protocol.json').read_text())['cases']:
        out=destination(case);base=out.as_uri() if case=='fine_features' else 'results/'+case;names=[n for n in ['O','R','B','RB'] if (out/(n+'_metrics.json')).exists()]
        rgb=Image.open(out/'working.png').convert('RGB');labels=np.load(out/'labels.npy',allow_pickle=False);palette=np.array([label_rgb(i) for i in range(int(labels.max())+1)],np.uint8);Image.fromarray(palette[labels]).save(out/'frozen_labels.png')
        body.append(f'<section id="{case}"><h2>{case}</h2><div class="grid">'+pic(base,'working.png','Original raster')+pic(base,'frozen_labels.png','Frozen segmentation: unchanged in every condition'))
        old=(WORK/'thin_structure_topology/external_results' if case=='fine_features' else OLD/'results')/case
        if (old/'pixel_reference.svg').exists():
            for ext in ['svg','png']:shutil.copy2(old/('pixel_reference.'+ext),out/('pixel_reference.'+ext))
            body.append(pic(base,'pixel_reference.png','Saved pixel-equivalent fidelity reference; not final geometry','pixel_reference.svg'))
        body.append('</div><table><tr><th>Condition</th><th>Ring denominator</th><th>Invalid raw / fit</th><th>Collapsed</th><th>Cross/overlap</th></tr>')
        for n in names:
            m=json.loads((out/(n+'_metrics.json')).read_text());body.append(f'<tr><td>{n}</td><td>{len(m["rings"])}</td><td>{m["invalid_raw_rings"]} / {m["invalid_fit_rings"]}</td><td>{m["raw_nonzero_fit_degenerate_rings"]}</td><td>{m["crossing_or_overlap_pairs"]}</td></tr>')
        body.append('</table><p>Splitting changes ring denominators. More/fewer collapsed rings do not by themselves mean geometry was lost/recovered.</p><div class="grid">')
        for n in names:
            body.append(pic(base,n+'_raw.png',n+' raw chain boundaries',n+'_raw.svg'))
            body.append(pic(base,n+'_curves.png',n+' actual fitted curves',n+'_curves.svg'))
        body.append('</div>')
        if case=='A01_shield':body.append('<h3>Complete crown, ornament, tips, valleys and both band edges</h3><p>All O/R boundary curves are identical. No crown recovery. Frame/material boundaries appear in the full drawing. Inherited1.2–2px evaluator uncertainty cannot certify1px crown correctness.</p>')
        if case=='G06_arabic':body.append('<p>Inspect counters, stems, isolated marks and junctions. Region-fill differences are export dependent; source-threshold IoU is not independent font-outline correctness.</p>')
        x,y,w,h=DETAIL[case];rgb.crop((x,y,x+w,y+h)).resize((w*4,h*4),Image.Resampling.NEAREST).save(out/'source_detail_pixels_4x.png')
        body.append('<div class="grid">'+pic(base,'source_detail_pixels_4x.png','Raster detail pixels, not high-resolution contour truth')+'</div>')
        for scale in [1,4,16]:
            body.append(f'<details {"open" if scale==4 else ""}><summary>True SVG detail render {scale}×</summary><div class="grid">')
            for n in names:
                tree=ET.parse(out/(n+'_curves.svg')).getroot();tree.set('viewBox',f'{x} {y} {w} {h}');tree.set('width',str(w*scale));tree.set('height',str(h*scale));p=out/(n+f'_review_{scale}x.svg');p.write_text(ET.tostring(tree,encoding='unicode'),encoding='utf-8');render(p,p.with_suffix('.png'))
                body.append(pic(base,p.with_suffix('.png').name,n+' actual SVG geometry',p.name))
            body.append('</div></details>')
        # Source-backed overlays stay raster diagnostics, never exported underlays.
        body.append('<h3>Internal geometry overlay</h3><div class="grid">')
        for n in names:
            tree=ET.parse(out/(n+'_curves.svg')).getroot()
            for e in tree:e.set('stroke','#00cddd');e.set('stroke-width','.55')
            p=out/(n+'_cyan.svg');p.write_text(ET.tostring(tree,encoding='unicode'),encoding='utf-8');render(p,p.with_suffix('.png'));im=rgb.convert('RGBA');im.alpha_composite(Image.open(p.with_suffix('.png')).convert('RGBA'));im.convert('RGB').save(out/(n+'_source_overlay.png'))
            body.append(pic(base,n+'_source_overlay.png',n+' source comparison; raster is inspection only',n+'_curves.svg'))
        body.append('</div><h3>Face / junction and exporter diagnostics</h3>')
        audit=json.loads((out/'R_audit.json').read_text());affected=[row for row in audit['mapping'] if row['splits']]
        if affected:
            body.append('<div class="grid">')
            focus=affected[0];original=json.loads((out/'O.json').read_text());rearranged=json.loads((out/'R.json').read_text());lookup={c['id']:chain_points(c,True) for c in original['chains']}
            for name,g,indices in [('O',original,[focus['original_ring']]),('R',rearranged,focus['new_ring_indices'])]:
                paths=[];allpts=[]
                for j,index in enumerate(indices):
                    pts,_=ring_points(g['faces'][focus['face']][index],lookup);allpts.extend(pts.tolist());d='M'+' L'.join(f'{p[0]},{p[1]}' for p in pts)+' Z';color=['#e32a3a','#0077cc','#1a9d45','#a020a0'][j%4];paths.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width=".35"/>')
                pts=np.array(allpts);lo=pts.min(0)-2;hi=pts.max(0)+2;p=out/(name+'_affected_raw_walk.svg');p.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="640" height="400" viewBox="{lo[0]} {lo[1]} {hi[0]-lo[0]} {hi[1]-lo[1]}">'+''.join(paths)+'</svg>',encoding='utf-8');render(p,p.with_suffix('.png'));body.append(pic(base,p.with_suffix('.png').name,name+' affected raw walk / decomposed cycles, exact same edges',p.name))
            body.append('</div>')
        a=np.asarray(Image.open(out/'O_fitted_regions_8x.png').convert('RGBA'));b=np.asarray(Image.open(out/'R_fitted_regions_8x.png').convert('RGBA'));diff=np.any(a!=b,axis=-1);im=np.full((*diff.shape,3),255,np.uint8);im[diff]=(235,0,70);Image.fromarray(im).save(out/'fitted_export_difference_8x.png')
        body.append('<div class="grid">'+pic(base,'fitted_export_difference_8x.png','Red = changed fitted region-ID render due compound-export behavior, not newly fitted curves'))
        for n in ['O','R']:body.append(pic(base,n+'_fitted_regions_8x.png',n+' inherited region-ID exporter at8x',n+'_fitted_regions.svg'))
        body.append('</div><h3>Independent source-only feasibility probe</h3><p>Cyan = persistent source edge near raw cracks. Magenta = farther than2px. Ridge maps normalized for display only. Evidence is not recovered structure; it includes shading and texture.</p><div class="grid">')
        for p in ['evidence_vs_raw_overlay.png','ridge_dark_DISPLAY_ONLY.png','ridge_light_DISPLAY_ONLY.png']:body.append(pic(base,'source_probe/'+p,p))
        body.append('</div></section>')
    css='body{font:16px system-ui;margin:24px;background:#edf1f4;color:#142132}.warn{padding:18px;background:#ffe7b2}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}figure{margin:0;background:white;padding:10px;border:1px solid #abc}img{max-width:100%;background:white}figcaption{font-size:13px}section{border-top:3px solid #789;margin-top:35px}td,th{border:1px solid #abc;padding:8px}table{border-collapse:collapse;background:white}summary{padding:15px;cursor:pointer}'
    (ROOT/'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Raw-face geometry isolation</title><style>'+css+'</style>'+''.join(body)+'</html>',encoding='utf-8')

if __name__=='__main__':build()

# END CHANGE AGD-RAWFACE-REVIEW | 2026-10-29T12:39:51Z | CREATED | Author: root
