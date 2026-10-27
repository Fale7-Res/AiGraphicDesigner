"""Native candidate comparison and unchanged historical-baseline aggregation."""
# START CHANGE ADAPTIVE-DELIVERY | 2026-10-27T03:09:20Z | CREATED | Author: root
from pathlib import Path
import json,html,csv,sys
import numpy as np
from PIL import Image,ImageDraw
from scipy.ndimage import gaussian_filter
ROOT=Path(__file__).resolve().parent
OLD=ROOT.parent/'EXP_VTRACER_FIDELITY_20261024'

def review(folder):
    folder=Path(folder);r=json.loads((folder/'ranking.json').read_text());rows=r['ranked'][:5]
    if not rows:return
    original=Image.open(folder/'normalized.png').convert('RGB');a=np.array(original).astype(float);w,h=original.size;local=[];options=[]
    for row in rows:
        b=np.array(Image.open(folder/row['trial']/'render.png').convert('RGB')).astype(float);delta=a-b
        tiles=[float(np.sqrt(np.mean(t*t))) for ys in np.array_split(delta,4,axis=0) for t in np.array_split(ys,4,axis=1)]
        local.append({'trial':row['trial'],'worst_tile_rmse':max(tiles),'smooth_residual_rmse_sigma4':float(np.sqrt(np.mean(gaussian_filter(delta,(4,4,0))**2)))})
        options.append('<option value="'+row['trial']+'">'+html.escape(row['trial']+' '+row['config']['clustering']+' '+row['config']['mode'])+'</option>')
    best=Image.open(folder/'best.png').convert('RGB');Image.blend(original,best,.5).save(folder/'overlay.png')
    error=Image.fromarray(np.clip(abs(a-np.array(best))*4,0,255).astype('uint8'));error.save(folder/'error_x4.png')
    panels=[('Original',original),('Adaptive selected',best)]
    old=OLD/'best_outputs'/(folder.name+'.png')
    if old.exists():panels.append(('Previous selected VTracer',Image.open(old).convert('RGB')))
    # START CHANGE ADAPTIVE-BASELINE-PANEL | 2026-10-27T03:14:00Z | CREATED | Author: root
    baseline=OLD/'results_baselines'/folder.name/'original'/'render.png'
    if baseline.exists():panels.append(('Original V04 (recorded render)',Image.open(baseline).convert('RGB')))
    # END CHANGE ADAPTIVE-BASELINE-PANEL | 2026-10-27T03:14:00Z | CREATED | Author: root
    panels.append(('Error x4',error));sheet=Image.new('RGB',(w*len(panels),h+30),'white');draw=ImageDraw.Draw(sheet)
    for i,(label,im) in enumerate(panels):draw.text((i*w+5,8),label,fill='black');sheet.paste(im,(i*w,30))
    sheet.save(folder/'comparison.png');(folder/'local_review.json').write_text(json.dumps(local,indent=2))
    payload=json.dumps({row['trial']:{k:row[k] for k in ('config','metrics','structure','performance')} for row in rows}).replace('</','<\\/')
    page='''<!doctype html><meta charset="utf-8"><title>Native SVG comparison</title><style>body{font:16px sans-serif;margin:24px;background:#eee}#view{position:relative;display:inline-block}#over{position:absolute;left:0;top:0;opacity:.5}img{max-width:none}pre{white-space:pre-wrap}</style><h1>Native-resolution candidate review</h1><p>Actual SVG renders. Numerical ranking is not human approval.</p><select id="pick">'''+''.join(options)+'''</select><label> Candidate opacity <input id="opacity" type="range" min="0" max="100" value="50"></label> <a id="svg">SVG</a><p><a href="comparison.png">Full-size comparison</a> · <a href="error_x4.png">Error ×4</a></p><div id="view"><img src="normalized.png"><img id="over"></div><pre id="details"></pre><script>const rows='''+payload+''';function change(){let t=document.getElementById('pick').value;document.getElementById('over').src=t+'/render.png';document.getElementById('svg').href=t+'/output.svg';document.getElementById('details').textContent=JSON.stringify(rows[t],null,2)}document.getElementById('pick').onchange=change;document.getElementById('opacity').oninput=e=>document.getElementById('over').style.opacity=e.target.value/100;change();</script>'''
    (folder/'review.html').write_text(page)

def summarize():
    rows=[]
    for p in sorted((ROOT/'results').glob('*/ranking.json')):
        r=json.loads(p.read_text())
        if not r['ranked']:continue
        b=r['ranked'][0];m=b['metrics'];s=b['structure'];old=OLD/'best_outputs'/(p.parent.name+'.json');previous=json.loads(old.read_text()) if old.exists() else None
        rows.append({'image':p.parent.name,'split':'historical12' if previous else ('new_real' if p.parent.name.startswith(('U05','U06')) else 'new_synthetic'),'family':b['config']['clustering'],'mode':b['config']['mode'],'ssim':m['ssim'],'psnr_db':m['psnr_db'],'identical':m['identical'],'edge_f1':m['edge_f1_1_5px'],'delta_e76':m['delta_e76_mean'],'highpass_rmse':m['highpass_rmse_sigma1'],'previous_ssim':previous['metrics']['ssim'] if previous else None,'previous_psnr':previous['metrics']['psnr_db'] if previous else None,'paths':s['elements'].get('path',0),'commands':sum(s['path_commands'].values()),'bytes':s['bytes'],'tested':r['evaluated_candidates'],'failed':len(r['failed']),'search_seconds':r['search_wall_seconds'],'trace_seconds':b['performance']['trace_wall_seconds'],'render_seconds':b['performance']['render_seconds'],'worker_peak_mib':b['performance']['worker_peak_mib'],'renderer_peak_mib':b['performance']['renderer_child_peak_mib'],'stop':r['stop_reason']})
    means={}
    for split in ('historical12','new_synthetic','new_real'):
        subset=[r for r in rows if r['split']==split];means[split]={'n':len(subset)}
        for k in ('ssim','psnr_db','edge_f1','delta_e76','highpass_rmse','previous_ssim','previous_psnr','search_seconds'):
            values=[r[k] for r in subset if r[k] is not None];means[split][k]=float(np.mean(values)) if values else None
        means[split]['psnr_note']='Finite values only; exactmatches have null/infinite PSNR'
    (ROOT/'reports/summary.json').write_text(json.dumps({'rows':rows,'means':means},indent=2))
    if rows:
        with (ROOT/'reports/metrics.csv').open('w') as f:
            writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    lines=['# Native-resolution results','', '| Image | Previous SSIM | Adaptive SSIM | PSNR dB | Family | Paths | Commands | Search s |','|---|---:|---:|---:|---|---:|---:|---:|']
    for r in rows:lines.append(f"| {r['image']} | {r['previous_ssim']} | {r['ssim']:.6f} | {r['psnr_db']} | {r['family']} | {r['paths']} | {r['commands']} | {r['search_seconds']:.1f} |")
    (ROOT/'reports/RESULTS.md').write_text('\n'.join(lines)+'\n')
    links=''.join(f'<li><a href="results/{r["image"]}/review.html">{r["image"]}</a> SSIM {r["ssim"]:.6f}</li>' for r in rows)
    (ROOT/'index.html').write_text('<!doctype html><meta charset="utf-8"><title>Adaptive VTracer research</title><h1>Native render comparisons</h1><p>Research only. NOT_APPROVED.</p><ul>'+links+'</ul>');print(json.dumps(means,indent=2))

if __name__=='__main__':
    for p in ([Path(sys.argv[1])] if len(sys.argv)>1 else sorted((ROOT/'results').glob('*'))):
        if (p/'ranking.json').exists():review(p)
    if len(sys.argv)==1:summarize()
# END CHANGE ADAPTIVE-DELIVERY | 2026-10-27T03:09:20Z | CREATED | Author: root
