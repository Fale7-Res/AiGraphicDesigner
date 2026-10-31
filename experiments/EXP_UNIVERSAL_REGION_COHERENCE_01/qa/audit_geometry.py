# START CHANGE AGD-UNIVERSAL-QA | 2026-10-31T10:53:38Z | CREATED | Author: universal_qa
"""Independent Bernstein and spatial checks of saved C changes only."""
import sys
import json
from pathlib import Path
import numpy as np
work=Path.cwd()/'work'
sys.path.insert(0,str(work/'geometry-deps'))
from shapely.geometry import LineString
from shapely import points as shapely_points
from shapely import distance
repo=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner')
exp=repo/'experiments/EXP_UNIVERSAL_REGION_COHERENCE_01'
protocol=json.loads((exp/'protocol.json').read_text())
rows=[];failures=[]

def dense(cc):
    u=np.linspace(0.,1.,129)[:,None]
    pieces=[(1-u)**3*c[0]+3*(1-u)**2*u*c[1]+3*(1-u)*u*u*c[2]+u**3*c[3] for c in np.asarray(cc)]
    return np.concatenate([p[:-1] for p in pieces]+[pieces[-1][-1:]])

def sampled_source(p):
    out=[]
    for a,b in zip(p,p[1:]):
        count=max(1,int(np.ceil(np.linalg.norm(b-a)/.05)))
        out.extend(a+(b-a)*np.arange(count)[:,None]/count)
    return np.asarray(out+[p[-1]])

for case in protocol['cases']:
    folder=work/'universal_geometry/local_only'/case if case=='fine_features' else exp/'results'/case
    if not (folder/'WORKER.json').exists():continue
    pp=json.loads((folder/'P.json').read_text())['accepted']
    cc=json.loads((folder/'C.json').read_text())['accepted']
    audit=json.loads((folder/'C_audit.json').read_text())
    original={r['trace_id']:np.asarray(r['source_points_xy'],float) for r in json.loads((folder/'frozen_traces.json').read_text())['traces']}
    p_lines=[LineString(dense(item['curves'])) for item in pp]
    c_lines=[LineString(dense(item['curves'])) for item in cc]
    maxforward=0.;maxreverse=0.;changes=0;newconflicts=[]
    for row in audit['chains']:
        if row['status']!='accepted':continue
        changes+=1;i=row['item_index'];item=cc[i];curves=np.asarray(item['curves']);src=original[item['trace_id']];cursor=0
        for part in row['partitions']:
            lo,hi=part['lo'],part['hi'];raw=src[lo:hi+1]
            stop=cursor
            while stop<len(curves) and not np.array_equal(curves[stop,-1],raw[-1]):stop+=1
            if stop>=len(curves):failures.append(case+': missing partition endpoint');break
            fit=dense(curves[cursor:stop+1]);cursor=stop+1
            forward=float(distance(shapely_points(fit),LineString(raw)).max())
            reverse=float(distance(shapely_points(sampled_source(raw)),LineString(fit)).max())
            maxforward=max(maxforward,forward);maxreverse=max(maxreverse,reverse)
            if max(forward,reverse)>.603:failures.append(case+': independent deviation exceeds .603 sampling allowance')
        if cursor!=len(curves):failures.append(case+': C partition controls unaccounted')
        if not c_lines[i].is_simple:failures.append(case+': C new nonsimple chain')
        for j in range(len(cc)):
            if j==i or not (c_lines[i].envelope.intersects(c_lines[j].envelope) or p_lines[i].envelope.intersects(p_lines[j].envelope)):continue
            if c_lines[i].crosses(c_lines[j]) and not p_lines[i].crosses(p_lines[j]):newconflicts.append([i,j,'cross'])
            if c_lines[i].overlaps(c_lines[j]) and not p_lines[i].overlaps(p_lines[j]):newconflicts.append([i,j,'overlap'])
            if c_lines[i].intersects(c_lines[j])!=p_lines[i].intersects(p_lines[j]):newconflicts.append([i,j,'incidence'])
    if newconflicts:failures.append(case+': sampled C conflicts '+str(newconflicts))
    rows.append({'case':case,'accepted_changes':changes,'sampled_curve_to_raw_max_px':maxforward,
                 'sampled_raw_to_curve_max_px':maxreverse,'new_conflicts':newconflicts,
                 'independent_sampling_points_per_cubic':129,'raw_sampling_spacing_max_px':.05})
result={'rows':rows,'failures':failures,'passed':not failures,'exact_continuous_certification':False,
        'allowance_px':.003,'note':'Numerical independent corroboration, not strict mathematical bound.'}
Path(__file__).with_name('GEOMETRY_AUDIT.json').write_text(json.dumps(result,indent=2))
print(json.dumps({'cases':len(rows),'changed_chains':sum(x['accepted_changes'] for x in rows),
                  'failures':failures,'max_sampled_px':max([max(x['sampled_curve_to_raw_max_px'],x['sampled_raw_to_curve_max_px']) for x in rows],default=0)}))
# END CHANGE AGD-UNIVERSAL-QA | 2026-10-31T10:53:38Z | CREATED | Author: universal_qa
