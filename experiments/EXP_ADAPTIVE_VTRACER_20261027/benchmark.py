"""Frozen native-resolution suite; no filename-specific search configuration."""
# START CHANGE ADAPTIVE-SUITE | 2026-10-27T03:08:56Z | CREATED | Author: restore_execute
from pathlib import Path
import json, hashlib, argparse
from concurrent.futures import ThreadPoolExecutor,as_completed
import numpy as np
from PIL import Image,ImageDraw
from skimage import data
from optimizer import optimize,ROOT
OLD=ROOT.parent/'EXP_VTRACER_FIDELITY_20261024'

def fixtures():
    p=ROOT/'unseen';p.mkdir(exist_ok=True);manifest=[]
    y,x=np.mgrid[:192,:256];shade=np.exp(-((x-130)**2/2600+(y-120)**2/350))
    rgb=np.stack([230-70*shade+x/30,225-65*shade+y/40,215-55*shade],2).clip(0,255).astype('uint8')
    images={'U01_smooth_shadow':Image.fromarray(rgb),'U02_fine_monochrome':Image.new('RGB',(256,192),'white')}
    d=ImageDraw.Draw(images['U02_fine_monochrome'])
    for k in range(15):d.line([(10,8+k*11),(240,12+k*11)],fill='black',width=1+k%3)
    rng=np.random.default_rng(26026);images['U03_color_texture']=Image.fromarray(rng.integers(0,256,(192,256,3),dtype='uint8'))
    alpha=Image.fromarray(rgb).convert('RGBA');alpha.putalpha(Image.fromarray((x/255*255).astype('uint8')));images['U04_partial_alpha']=alpha
    images['U05_astronaut']=Image.fromarray(data.astronaut());images['U06_brick']=Image.fromarray(data.brick())
    for name,im in images.items():
        f=p/(name+'.png')
        if not f.exists():im.save(f)
        manifest.append({'id':name,'file':f.name,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'size':im.size,'alpha_policy':'white' if name=='U04_partial_alpha' else 'reject','split':'new_real' if name in ('U05_astronaut','U06_brick') else 'new_synthetic'})
    (p/'manifest.json').write_text(json.dumps({'inputs':manifest,'real_source':'scikit-image0.26 bundled data; https://scikit-image.org/docs/stable/api/skimage.data.html; astronaut NASA publicdomain, brick CC0Textures CC0; native dimensions unchanged'},indent=2))
    return manifest

def execute(item):
    source,split,alpha=item;out=ROOT/'results'/source.stem
    if (out/'ranking.json').exists():return {'id':source.stem,'status':'reused_completed'}
    r=optimize(source,out,24,720,alpha)
    return {'id':source.stem,'split':split,'tested':r['evaluated_candidates'],'stop':r['stop_reason'],'status':'ok' if r['ranked'] else 'failed','metrics':r['ranked'][0]['metrics'] if r['ranked'] else None}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--workers',type=int,default=2);a=p.parse_args()
    records=fixtures();items=[(x,'historical12','reject') for x in sorted((OLD/'inputs').glob('*.png'))]+[(ROOT/'unseen'/r['file'],r['split'],r['alpha_policy']) for r in records]
    (ROOT/'reports/protocol.json').write_text(json.dumps({'optimizer_sha256':hashlib.sha256((ROOT/'optimizer.py').read_bytes()).hexdigest(),'cases':[str(x[0]) for x in items],'max_candidates':24,'dispatch_seconds':720,'frozen_before_run':True},indent=2))
    failures=[]
    with ThreadPoolExecutor(max_workers=a.workers) as pool:
        jobs={pool.submit(execute,x):x for x in items}
        for job in as_completed(jobs):
            try:r=job.result()
            except Exception as e:r={'id':str(jobs[job][0]),'status':'failed','error':repr(e)}
            print(json.dumps(r),flush=True)
            if r['status']=='failed':failures.append(r)
    if failures:raise SystemExit(1)
# END CHANGE ADAPTIVE-SUITE | 2026-10-27T03:08:56Z | CREATED | Author: restore_execute
