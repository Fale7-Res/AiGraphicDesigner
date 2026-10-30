# START CHANGE AGD-ML-PACKAGE | 2026-10-30T08:17:45Z | CREATED | Author: root
"""Frozen common evidence-to-open-curve control. No evaluator imports."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
import sys,json,time,hashlib,shutil,collections
R=Path(os.environ.get('AGD_REPO',r'C:\Users\Mohamed\Desktop\AiGraphicDesigner'))
E=R/'experiments/EXP_ML_CLASSICAL_HYBRID_GEOMETRY_01';W=Path(os.environ.get('AGD_WORK',str(Path.cwd()/'work')))
sys.path[:0]=[str(R/'experiments/EXP_EXPORTER_DISCOVERY_01'),str(R/'experiments/EXP_RAW_FACE_JUNCTION_01'),str(W/'ml_geometry/fitting_control'),str(W/'geometry-deps')]
import numpy as np
from PIL import Image
from scipy import ndimage
from skimage.filters import apply_hysteresis_threshold
from skimage.morphology import skeletonize
from discovery_strokes import _trace,_fit
from source_evidence_probe import extract
from svg_exporter import svg_graph
from stable_fit import fit,flatten

def paths(case):
    base=W/'ml_geometry/local_only'/case if case=='fine_features' else E/'results'/case
    source=(W/'ml_geometry/local_only'/case if case=='fine_features' else E/'inputs'/case)/'working.png'
    return base,source

def chain_graph(curves,width,height):
    chains=[]
    for i,item in enumerate(curves):
        cc=np.asarray(item['curves'])
        chains.append({'id':i,'closed':bool(np.array_equal(cc[0,0],cc[-1,-1])),'adjacent_face_labels':[1,2],
                       'segments':[dict(type='C',**{k:p.tolist() for k,p in zip(['p0','p1','p2','p3'],c)}) for c in cc]})
    return {'width':width,'height':height,'chains':chains,'faces':{}}

def build(case):
    base,source=paths(case);rgb=np.asarray(Image.open(source).convert('RGB'));h,w=rgb.shape[:2]
    old=R/'experiments/EXP_RAW_FACE_JUNCTION_01/results'/case/'source_probe/source_evidence.npz'
    if case=='fine_features':old=W/'raw_face_junction/external_results/fine_features/source_probe/source_evidence.npz'
    if old.exists():classical=np.load(old)['persistent_edges'];origin=str(old)
    else:
        arrays,_=extract(rgb);classical=arrays['persistent_edges'];origin='unchanged historical extract(rgb)'
    probability=np.load(base/'ML/predictions.npz')['native_sigmoid']
    ml=apply_hysteresis_threshold(probability,.3,.5)
    near=ndimage.distance_transform_edt(~classical)<=1.5 if classical.any() else np.zeros_like(classical)
    hybrid_field=np.where(near | (probability>=.7),probability,0.)
    hybrid=apply_hysteresis_threshold(hybrid_field,.3,.5)
    for name,evidence in [('Classical',classical),('ML',ml),('Hybrid',hybrid)]:
        folder=base/name;folder.mkdir(parents=True,exist_ok=True)
        if (folder/'construction.json').exists():raise RuntimeError('Preserve existing candidates')
        started=time.monotonic();sk=skeletonize(evidence);raw,adjacency=_trace(sk)
        np.savez_compressed(folder/'discovery.npz',support=evidence,skeleton=sk)
        Image.fromarray(evidence.astype('uint8')*255).save(folder/'support.png')
        overlay=rgb.copy();overlay[sk]=(255,0,180);Image.fromarray(overlay).save(folder/'support_overlay.png')
        ranked=sorted(enumerate(raw),key=lambda z:(-np.linalg.norm(np.diff(z[1],axis=0),axis=1).sum(),z[0]))
        accepted=[];old_accepted=[];records=[];eligible=0
        for index,points in ranked:
            length=float(np.linalg.norm(np.diff(points,axis=0),axis=1).sum())
            record={'trace_id':index,'length_px':length,'source_points_xy':points.tolist()}
            if length<6:record['reason']='short_chain';records.append(record);continue
            eligible+=1
            if eligible>128:record['reason']='proposal_budget';records.append(record);continue
            if time.monotonic()-started>120:record['reason']='case_wall_budget';records.append(record);continue
            legacy,lmeta=_fit(points);record['old_fit']=lmeta
            if legacy is not None:old_accepted.append({'trace_id':index,'curves':legacy.tolist()})
            curves,meta=fit(points);record['stable_fit']=meta
            if curves is not None:
                accepted.append({'trace_id':index,'curves':curves.tolist(),'length_px':length,'fit':meta})
                record['reason']='accepted'
            else:record['reason']=meta['reason']
            records.append(record)
        for tag,items in [('old',old_accepted),('stable',accepted)]:
            graph=chain_graph(items,w,h);(folder/(tag+'.svg')).write_text(svg_graph(graph),encoding='utf-8')
        report={'case':case,'arm':name,'evidence_origin':origin if name=='Classical' else 'same DexiNed sigmoid fixed postprocessor','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'prefit':{'support_pixels':int(evidence.sum()),'density':float(evidence.mean()),'skeleton_pixels':int(sk.sum()),'components8':int(ndimage.label(sk,np.ones((3,3)))[1]),'junction_pixels':sum(len(v)>2 for v in adjacency.values()),'endpoint_pixels':sum(len(v)==1 for v in adjacency.values()),'raw_traces':len(raw),'eligible_traces':eligible},'postfit':{'old_accepted':len(old_accepted),'stable_accepted':len(accepted),'cubics':sum(len(x['curves']) for x in accepted),'rejections':dict(collections.Counter(x['reason'] for x in records if x['reason']!='accepted'))},'accepted':accepted,'traces':records,'wall_seconds':time.monotonic()-started,'integration':'Unintegrated open boundary proposals; no invented region ownership, width, holes or semantics. Complete geometry NOT_ACCEPTED.'}
        (folder/'construction.json').write_text(json.dumps(report,indent=2));print(case,name,report['prefit'],report['postfit'],report['wall_seconds'],flush=True)

if __name__=='__main__':build(sys.argv[1])

# END CHANGE AGD-ML-PACKAGE | 2026-10-30T08:17:45Z | CREATED | Author: root
