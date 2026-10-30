# START CHANGE AGD-ML-INDEPENDENT-METRICS | 2026-10-30T08:05:08Z | CREATED | Author: ml_geometry_qa
"""Independent saved-support metric audit using chunked brute-force distances."""
from pathlib import Path
import json,math,xml.etree.ElementTree as ET
import numpy as np
from PIL import Image
from scipy.spatial.distance import cdist
R=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner');E=R/'experiments/EXP_ML_CLASSICAL_HYBRID_GEOMETRY_01'
W=Path.cwd()/'work';OUT=W/'ml_geometry/qa'
def dists(a,b):
    if not len(b):return np.full(len(a),np.inf)
    return np.concatenate([cdist(a[i:i+64],b).min(axis=1) for i in range(0,len(a),64)])
def sample(p):
    output=[]
    for a,b in zip(p[:-1],p[1:]):
        n=max(1,math.ceil(float(np.linalg.norm(b-a))/.25))
        output.extend(a+(b-a)*i/n for i in range(n))
    return np.array(output+[p[-1]])
guide=json.loads((R/'experiments/EXP_COMPLETE_GEOMETRY_ISOLATION_01/references/shield_complete_boundary_reference.json').read_text())
results=[]
for arm in ['Classical','ML','Hybrid']:
    folder=E/'results/A01_shield'/arm
    sk=np.load(folder/'discovery.npz')['skeleton'];pre=np.argwhere(sk)[:,::-1]+.5
    metrics=json.loads((folder/'metrics.json').read_text())
    for g in guide['components']+guide['appearance_only']:
        target=np.concatenate([sample(np.array(p,float)) for p in g['polylines']])
        recall=float(np.mean(dists(target,pre)<=g['uncertainty_px']))
        reported=next(x for x in metrics['critical_guides'] if x['id']==g['id'])['raw']['recall']
        assert abs(recall-reported)<1e-12,(arm,g['id'],recall,reported)
        results.append({'arm':arm,'guide':g['id'],'raw_recall':recall,'reported_exact':True})
# Independent mask-boundary extraction: manual four-neighbor interior,8x samples.
manifest=json.loads((R/'experiments/EXP_COMPLETE_GEOMETRY_ISOLATION_01/references/known_control_reference_manifest.json').read_text())['references']
known=[]
for case in ['fine_features','K01_linear_corner_hole']:
    ref=next(x for x in manifest if x['id']==case);mask=np.asarray(Image.open(ref['local_only_mask_path']).convert('L'))>=128
    pad=np.pad(mask,1);inside=mask & pad[:-2,1:-1] & pad[2:,1:-1] & pad[1:-1,:-2] & pad[1:-1,2:]
    target=(np.argwhere(mask & ~inside)[:,::-1]+.5)/8
    # Deterministic subset checks individual distances, not stochastic CI.
    subset=target[::max(1,len(target)//200)]
    root=W/'ml_geometry/local_only'/case if case=='fine_features' else E/'results'/case
    for arm in ['Classical','ML','Hybrid']:
        folder=root/arm;sk=np.load(folder/'discovery.npz')['skeleton'];pre=np.argwhere(sk)[:,::-1]+.5
        from scipy.spatial import cKDTree
        brute=dists(subset,pre);tree=cKDTree(pre).query(subset)[0] if len(pre) else np.full(len(subset),np.inf)
        assert np.array_equal(brute<=1.25,tree<=1.25)
        full=dists(target,pre);recall=float(np.mean(full<=1.25));reported=json.loads((folder/'metrics.json').read_text())['boundary_1_25px']['raw_all']['recall']
        assert abs(recall-reported)<1e-12
        known.append({'case':case,'arm':arm,'target_samples':len(target),'raw_recall':recall,'reported_exact':True})
rois=[]
for p in E.glob('results/*/*/detail.svg'):
    root=ET.parse(p).getroot();box=[float(v) for v in root.attrib['viewBox'].split()]
    native=Image.open(p.with_name('detail_1x.png')).size
    high=Image.open(p.with_name('detail_16x.png')).size
    assert high==(native[0]*16,native[1]*16)
    assert native==(int(box[2]),int(box[3]))
    rois.append({'path':str(p),'viewBox':box,'native':native,'render16x':high})
rows=json.loads((E/'reports/METRICS.json').read_text())
summaries=[]
for row in rows:
    summary={'case':row['case'],'arm':row['arm'],'paths':row['vector']['paths'],'crossing_pairs':len(row['topology']['mutual_crossing_or_overlap_pairs'])}
    if 'boundary_1_25px' in row:summary['boundary']=row['boundary_1_25px']
    if 'critical_guides' in row:
        summary['critical_guides']=[{'id':g['id'],'raw':g['raw']['recall'],'selected':g['selected']['recall'],'fitted':g['fitted']['recall']} for g in row['critical_guides']]
    summaries.append(summary)
(OUT/'METRICS_AUDIT.json').write_text(json.dumps({'shield_guide_checks':results,'known_checks':known,'true_svg_roi_checks':rois,'reported_stage_summaries':summaries},indent=2))
print('Exact Shield guide checks:',len(results),'Known controls:',len(known),'True SVG ROI checks:',len(rois))
# END CHANGE AGD-ML-INDEPENDENT-METRICS | 2026-10-30T08:05:08Z | CREATED | Author: ml_geometry_qa
