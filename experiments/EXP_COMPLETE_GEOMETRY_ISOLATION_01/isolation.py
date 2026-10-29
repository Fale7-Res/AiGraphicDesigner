"""Research-only fixed-label isolation harness. Never reads evaluator annotations.

External Arena source remains outside this repository; no rights grant assumed.
"""
# START CHANGE AGD-ISOLATION-HARNESS | 2026-10-29T06:51:24Z | EDITED | Author: root
from pathlib import Path
import argparse, hashlib, importlib.util, json, os, sys, time, types
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
WORK = Path(os.environ.get('AGD_ISOLATION_WORK', r'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work'))
EXTERNAL = WORK/'arena_review/geometry_only_v2'
LOCAL = WORK/'complete_geometry_isolation'
CASES = {
 'A01_shield': REPO/'experiments/EXP_VECTOR_BOTTLENECKS_20261027/results/granularity/A01_shield/source.png',
 'G07_tux': REPO/'experiments/EXP_GEOMETRY_APPEARANCE_ABLATION_01/results/G07_tux/source.png',
 'G06_arabic': REPO/'experiments/EXP_VECTOR_BOTTLENECKS_20261027/results/granularity/G06_arabic/source.png',
 'G05_chelsea_nativecrop': REPO/'experiments/EXP_VECTOR_BOTTLENECKS_20261027/results/granularity/G05_chelsea_nativecrop/source.png',
 'fine_features': EXTERNAL/'inputs/synthetic/fine_features.png',
 'K01_linear_corner_hole': REPO/'experiments/EXP_VECTOR_BOTTLENECKS_20261027/results/oracle/K01_linear_corner_hole/source.png',
}

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def dump(path, obj):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,indent=2,allow_nan=False),encoding='utf-8')

def case_dir(case):
    # Unknown-rights independent fixture and derived artwork are local-only.
    return (LOCAL/'external_results' if case=='fine_features' else ROOT/'results')/case

def prepare():
    manifest={}
    for case,src in CASES.items():
        out=case_dir(case); out.mkdir(parents=True,exist_ok=True)
        rgba=Image.open(src).convert('RGBA')
        bg=Image.new('RGBA',rgba.size,'white'); bg.alpha_composite(rgba)
        working=out/'working.png'; bg.convert('RGB').save(working)
        manifest[case]={'source':str(src),'source_sha256':digest(src),'working':str(working),
          'working_sha256':digest(working),'size':list(rgba.size),
          'source_alpha_min':int(np.asarray(rgba)[...,3].min()),
          'pixels_unchanged':bool(np.array_equal(np.asarray(rgba)[...,:3],np.asarray(bg)[...,:3])),
          'rights':'external owner ZIP, not redistributed' if case=='fine_features' else 'existing repository input'}
    dump(ROOT/'inputs/manifest.json',manifest)
    return manifest

def arena_modules():
    sys.path.insert(0,str(WORK/'geometry-deps'))
    # Legacy imports CairoSVG at module load. This geometry-only wrapper denies
    # that renderer explicitly; none of the called graph/fit functions need it.
    stub=types.ModuleType('cairosvg')
    def denied(*a,**k): raise RuntimeError('Appearance/rendering forbidden in external geometry worker')
    stub.svg2png=denied; sys.modules['cairosvg']=stub
    package='agd_external_arena'
    spec=importlib.util.spec_from_file_location(package,EXTERNAL/'src/__init__.py',submodule_search_locations=[str(EXTERNAL/'src')])
    module=importlib.util.module_from_spec(spec);sys.modules[package]=module;spec.loader.exec_module(module)
    from importlib import import_module
    mods=[import_module(package+'.'+name) for name in ['segment','graph','fit']]
    hashes={str(p.relative_to(EXTERNAL)):digest(p) for p in list((EXTERNAL/'src').glob('*.py'))+[EXTERNAL/'historical/legacy_penvector.py']}
    return (*mods,hashes)

def worker(case,stage,segmentation):
    out=case_dir(case); image=out/'working.png'
    if stage=='segment':
        sm,gm,fm,hashes=arena_modules()
        if case in ('A01_shield','fine_features'):
            saved=EXTERNAL/('outputs/shield' if case=='A01_shield' else 'outputs/fine_features')/'labels.npy'
            original=EXTERNAL/('inputs/shield.png' if case=='A01_shield' else 'inputs/synthetic/fine_features.png')
            if not np.array_equal(np.asarray(Image.open(original).convert('RGB')),np.asarray(Image.open(image))):
                raise ValueError('Saved labels do not match common working pixels')
            labels=np.load(saved,allow_pickle=False); meta={'saved_labels':str(saved),'sha256':digest(saved)}
        else:
            _,labels,_,_,meta=sm.segment_image(image,method='felzenszwalb',scale=400,min_area=12,max_regions=1500)
        if labels.ndim!=2 or labels.min()<1: raise ValueError('Inside labels must be positive; zero reserved for exterior')
        np.save(out/'S_A.npy',labels.astype(np.uint32))
        dump(out/'S_A_meta.json',{'segmentation':meta,'external_source_hashes':hashes})
    elif stage=='arena_fit':
        sm,gm,fm,hashes=arena_modules(); labels=np.load(out/(segmentation+'.npy'),allow_pickle=False)
        graph=gm.construct(labels); raw=gm.serialize(graph,labels.shape[1],labels.shape[0])
        dump(out/(segmentation+'_raw_arena.json'),raw)
        stats=fm.initialize(graph,labels.shape[1],labels.shape[0],tolerance=.8,smooth=1.)
        fitted=gm.serialize(graph,labels.shape[1],labels.shape[0])
        fitted['stats']=stats;fitted['labels_sha256']=digest(out/(segmentation+'.npy'))
        dump(out/(segmentation+'_F_A.json'),fitted)
    else: raise ValueError(stage)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('action',choices=['prepare','worker','arena_batch']);p.add_argument('--case');p.add_argument('--stage');p.add_argument('--segmentation',default='S_A');a=p.parse_args()
    if a.action=='prepare':prepare()
    elif a.action=='arena_batch':
        import psutil,platform
        records=[]
        for case in CASES:
            for stage,seg in [('segment','S_A'),('arena_fit','S_A'),('arena_fit','S_V')]:
                target=case_dir(case)/(('S_A.npy') if stage=='segment' else seg+'_F_A.json')
                if target.exists():continue
                start=time.monotonic();cpu=time.process_time()
                worker(case,stage,seg)
                row={'case':case,'stage':stage,'segmentation':seg,'wall_seconds':time.monotonic()-start,'cpu_seconds':time.process_time()-cpu,'rss_mib_at_end':psutil.Process().memory_info().rss/1024**2}
                records.append(row);dump(ROOT/'reports/arena_execution.json',{'python':platform.python_version(),'records':records})
                print(json.dumps(row),flush=True)
    else:worker(a.case,a.stage,a.segmentation)
# END CHANGE AGD-ISOLATION-HARNESS | 2026-10-29T06:51:24Z | EDITED | Author: root
