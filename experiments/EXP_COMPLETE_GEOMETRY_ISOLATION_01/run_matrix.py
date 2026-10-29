# START CHANGE AGD-ISOLATION-RUN-MATRIX | 2026-10-29T06:48:34Z | CREATED | Author: root
"""Bounded execution, label hashes verified, no evaluator data read."""
import os,sys,subprocess,time,json,importlib.util
from pathlib import Path
os.environ['PYTHONDONTWRITEBYTECODE']='1'
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np
from PIL import Image
from isolation import ROOT,WORK,CASES,case_dir,dump,digest

native=WORK/'geometry_rust/target/release/agd_geometry.exe'
spec=importlib.util.spec_from_file_location('agd_existing_monitor',ROOT.parent/'EXP_VECTOR_BOTTLENECKS_20261027/safe_monitor.py')
mon=importlib.util.module_from_spec(spec);spec.loader.exec_module(mon)
logs=ROOT/'reports/execution';logs.mkdir(exist_ok=True)

def verify_resume_inputs():
    inputs=json.loads((ROOT/'inputs/manifest.json').read_text())
    for case,item in inputs.items():
        if digest(item['source'])!=item['source_sha256'] or digest(item['working'])!=item['working_sha256']:
            raise RuntimeError('Frozen source/working input changed: '+case)
    existing=[case_dir(c)/(s+'_F_'+f+'.json') for c in CASES for s in ['S_A','S_V'] for f in ['A','V']]
    existing=[p for p in existing if p.exists()]
    if existing:
        manifest=ROOT/'reports/CANDIDATE_MANIFEST.json'
        if not manifest.exists():raise RuntimeError('Existing candidates need explicit artifact validation; refusing existence-only resume')
        expected=json.loads(manifest.read_text())['files']
        for path in existing:
            if expected.get(str(path))!=digest(path):raise RuntimeError('Existing candidate hash differs: '+str(path))

def launch(command,name):
    record=mon.monitor([str(x) for x in command],logs/(name+'.log'),timeout=600,memory_mib=4096)
    dump(logs/(name+'.json'),record)
    print(name,json.dumps(record),flush=True)
    if record['returncode'] or record['termination_reason']:raise RuntimeError(name+' failed; preserve output and stop portion')
    return record

def vt_segment(case):
    out=case_dir(case);target=out/'S_V.npy'
    if target.exists():return
    rgba=np.asarray(Image.open(out/'working.png').convert('RGBA'));h,w=rgba.shape[:2]
    request=WORK/'complete_geometry_isolation'/('segment_'+case+'.json');request.parent.mkdir(parents=True,exist_ok=True)
    dump(request,{'width':w,'height':h,'rgba':rgba.ravel().tolist(),'detail':192,'min_area':0})
    response=out/'S_V_response.json';launch([native,'segment',request,response],case+'_segment_V')
    obj=json.loads(response.read_text());labels=np.asarray(obj.pop('labels'),dtype=np.uint32).reshape(h,w)
    assert labels.min()>=1
    np.save(target,labels);obj['labels_sha256']=digest(target);dump(out/'S_V_meta.json',obj)
    response.unlink() # transient duplicate label serialization; canonical NPY preserved

def vt_fit(case,seg):
    out=case_dir(case);target=out/(seg+'_F_V.json')
    if target.exists():return
    labels=np.load(out/(seg+'.npy'),allow_pickle=False);h,w=labels.shape
    request=WORK/'complete_geometry_isolation'/('fit_'+case+'_'+seg+'.json')
    dump(request,{'width':w,'height':h,'labels':labels.ravel().tolist()})
    launch([native,'fit',request,target],case+'_'+seg+'_fit_V')
    obj=json.loads(target.read_text());echo=np.asarray(obj.pop('labels'),dtype=np.uint32).reshape(h,w)
    assert np.array_equal(echo,labels),'Initializer changed labels'
    assert obj['graph_matches_exact_labels']
    obj['labels_sha256']=digest(out/(seg+'.npy'));dump(target,obj)

if __name__=='__main__':
    verify_resume_inputs()
    for case in CASES:vt_segment(case)
    launch([sys.executable,ROOT/'isolation.py','arena_batch'],'arena_batch')
    for case in CASES:
        for seg in ['S_A','S_V']:vt_fit(case,seg)

# END CHANGE AGD-ISOLATION-RUN-MATRIX | 2026-10-29T06:48:34Z | CREATED | Author: root
