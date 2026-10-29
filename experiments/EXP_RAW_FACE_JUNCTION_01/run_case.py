# START CHANGE AGD-RAWFACE-RUN-CASE | 2026-10-29T12:20:15Z | CREATED | Author: root
"""Fixed-label raw-representation isolation; evaluator data never enters guards."""
from pathlib import Path
import os,sys,json,shutil,time,hashlib
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1';sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
OLD=ROOT.parent/'EXP_THIN_STRUCTURE_TOPOLOGY_01'
WORK=Path(os.environ.get('AGD_ISOLATION_WORK',r'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work'))
sys.path[:0]=[str(OLD),str(WORK/'geometry-deps'),str(ROOT.parent/'EXP_COMPLETE_GEOMETRY_ISOLATION_01')]
from isolation import dump,digest
from face_cycles import decompose
from geometry_eval import svg_graph
from analyze_matrix import render,RESVG
from track_b import initialize_safe
import numpy as np
from PIL import Image
import subprocess

def destination(case):
    return (WORK/'raw_face_junction/external_results' if case=='fine_features' else ROOT/'results')/case

def execute(case):
    pins=json.loads((ROOT/'BASELINE_PINS.json').read_text(encoding='utf-8'))['cases'][case]
    for item in pins.values():assert digest(item['path'])==item['sha256']
    for name,value in json.loads((ROOT/'FREEZE.json').read_text(encoding='utf-8'))['files'].items():assert digest(ROOT/name)==value
    out=destination(case);out.mkdir(parents=True,exist_ok=False)
    started=time.monotonic();cpu=time.process_time()
    for old,new in [('baseline.json','O.json'),('baseline_labels.npy','labels.npy'),('working.png','working.png'),('B.json','B.json')]:shutil.copy2(pins[old]['path'],out/new)
    original=json.loads((out/'O.json').read_text(encoding='utf-8'));candidate,audit=decompose(original);dump(out/'R.json',candidate);dump(out/'R_audit.json',audit)
    checks=[]
    for name,g in [('O',original),('R',candidate)]:
        for raw in [True,False]:
            stem=name+('_raw_regions' if raw else '_fitted_regions');svg=out/(stem+'.svg');svg.write_text(svg_graph(g,raw=raw,regions=True),encoding='utf-8')
            for scale in ([1,8] if raw else [8]):
                png=out/(stem+f'_{scale}x.png')
                subprocess.run([str(RESVG),'--width',str(g['width']*scale),'--height',str(g['height']*scale),str(svg),str(png)],check=True,capture_output=True,timeout=60)
    for raw,scale in [(True,1),(True,8),(False,8)]:
        stem='_raw_regions' if raw else '_fitted_regions';a=np.asarray(Image.open(out/('O'+stem+f'_{scale}x.png')).convert('RGBA'));b=np.asarray(Image.open(out/('R'+stem+f'_{scale}x.png')).convert('RGBA'))
        checks.append({'raw':raw,'scale':scale,'different_rgba_pixels':int(np.sum(np.any(a!=b,axis=-1))),'equal':bool(np.array_equal(a,b))})
    gate=all(x['equal'] for x in checks) and not audit['rejections']
    dump(out/'MATCHED_CONTROLS.json',{'checks':checks,'RB_permitted':gate,'labels_sha256':digest(out/'labels.npy'),'no_parameter_tuning':True})
    if gate:
        corrected,guard=initialize_safe(candidate);dump(out/'RB.json',corrected);dump(out/'RB_audit.json',guard)
    else:dump(out/'RB_SKIPPED.json',{'reason':'Frozen representation equivalence gate failed; no guard bypass or altered segmentation'})
    dump(out/'CONSTRUCTION_RESOURCES.json',{'wall_seconds':time.monotonic()-started,'process_cpu_seconds':time.process_time()-cpu,'case':case,'RB_executed':gate,'labels_sha256':digest(out/'labels.npy')})

if __name__=='__main__':execute(sys.argv[1])

# END CHANGE AGD-RAWFACE-RUN-CASE | 2026-10-29T12:20:15Z | CREATED | Author: root
