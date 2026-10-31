# START CHANGE AGD-UNIVERSAL-QA | 2026-10-31T10:57:08Z | CREATED | Author: universal_qa
"""Independent saved shared-reference/atomic-region predicates, no integration run."""
import json
import sys
from pathlib import Path
import numpy as np
work=Path.cwd()/'work'
sys.path.insert(0,str(work/'geometry-deps'))
from shapely.geometry import Polygon
repo=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner')
exp=repo/'experiments/EXP_UNIVERSAL_REGION_COHERENCE_01'
protocol=json.loads((exp/'protocol.json').read_text())
rows=[];failures=[]

def dense_region_curve_samples(curves):
    u=np.linspace(0,1,129)[:,None]
    pieces=[(1-u)**3*c[0]+3*(1-u)**2*u*c[1]+3*(1-u)*u*u*c[2]+u**3*c[3] for c in curves]
    return np.concatenate([p[:-1] for p in pieces]+[pieces[-1][-1:]])

for case in protocol['cases']:
    folder=work/'universal_geometry/local_only'/case if case=='fine_features' else exp/'results'/case
    for tag,base in [('R','P'),('SR','S')]:
        if not (folder/(tag+'_graph.json')).exists():continue
        graph=json.loads((folder/(tag+'_graph.json')).read_text())
        inputs=json.loads((folder/(base+'.json')).read_text())['accepted']
        curves={c['id']:np.asarray([[s[k] for k in ('p0','p1','p2','p3')] for s in c['segments']]) for c in graph['chains']}
        for c,i in zip(graph['chains'],inputs):
            if not np.array_equal(curves[c['id']],np.asarray(i['curves'])):failures.append(case+tag+': controls changed')
        faces={};directed={}
        for fid,rings in graph['faces'].items():
            paths=[]
            for ring in rings:
                pieces=[]
                for ref in ring:
                    cc=curves[ref['chain']]
                    if not ref['forward']:cc=cc[::-1,::-1]
                    directed.setdefault((ref['chain'],ref['forward']),[]).append(fid)
                    pieces.append(cc)
                cc=np.concatenate(pieces)
                if not np.array_equal(cc[0,0],cc[-1,-1]):failures.append(case+tag+': face not exactly closed')
                if any(not np.array_equal(a[-1],b[0]) for a,b in zip(cc,cc[1:])):failures.append(case+tag+': ring disconnection')
                paths.append(dense_region_curve_samples(cc))
            polygon=Polygon(paths[0],paths[1:])
            if not polygon.is_valid or polygon.area<=1e-8:failures.append(case+tag+': invalid sampled atomic polygon')
            faces[fid]=polygon
        for edge,owners in directed.items():
            if len(owners)>1:failures.append(case+tag+': same directed edge owned by multiple faces')
        ids=list(faces);maxoverlap=0.
        for a,fid in enumerate(ids):
            for oid in ids[a+1:]:
                intersection=faces[fid].intersection(faces[oid]).area
                maxoverlap=max(maxoverlap,intersection)
                if intersection>1e-6:failures.append(case+tag+': positive atomic overlap '+str(intersection))
        rows.append({'case':case,'condition':tag,'atomic_faces':len(faces),'maximum_sampled_interior_overlap_px2':maxoverlap,
                     'geometry_changed':False,'semantic_ownership':'NOT_ESTABLISHED'})
result={'rows':rows,'failures':failures,'passed':not failures,'continuous_exact_certification':False,
        'note':'129 Bernstein samples/cubic validate shared-reference topology numerically; hole semantics not certified.'}
Path(__file__).with_name('REGION_AUDIT.json').write_text(json.dumps(result,indent=2))
print(json.dumps({'conditions':len(rows),'atomic_faces':sum(r['atomic_faces'] for r in rows),'failures':failures[:20]}))
# END CHANGE AGD-UNIVERSAL-QA | 2026-10-31T10:57:08Z | CREATED | Author: universal_qa
