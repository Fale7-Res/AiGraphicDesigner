# START CHANGE AGD-CONTOUR-CONSTRUCTION | 2026-10-30T08:44:39Z | CREATED | Author: root
"""Construct curves from immutable saved polylines; no detector or image inference."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
import sys,json,time,hashlib,collections,copy,shutil
R=Path(os.environ.get('AGD_REPO',r'C:\Users\Mohamed\Desktop\AiGraphicDesigner'));W=Path(os.environ.get('AGD_WORK',str(Path.cwd()/'work')))
E=R/'experiments/EXP_LOSS_ACCOUNTED_CONTOUR_CONSTRUCTION_01';OLD=R/'experiments/EXP_ML_CLASSICAL_HYBRID_GEOMETRY_01'
sys.path[:0]=[str(W/'contour_construction/implementation'),str(OLD),str(W/'geometry-deps')]
import numpy as np
from PIL import Image
from shapely.geometry import LineString
from shapely.strtree import STRtree
from partition_fit import fit_trace,flattened
from construct_geometry import chain_graph
from svg_exporter import svg_graph

def destination(case,arm):return (W/'contour_construction/local_only'/case if case=='fine_features' else E/'results'/case)/arm

def veto_chain(result,chain,reason):
    ids=set(chain['partition_ids'])
    for row in result['ledger']:
        if row.get('partition_id') in ids and row['status']=='accepted':
            row['status']='rejected';row['reason']=reason;row['guard']='global post-construction guard'

def construct_condition(frozen,condition,deadline):
    records=[];output=[];retained_shapes=[];retained_raw=[];global_cubics=0;eligible=0
    for trace in frozen['traces']:
        points=np.asarray(trace['source_points_xy'],float);n=len(points)-1;length=float(np.linalg.norm(np.diff(points,axis=0),axis=1).sum());tid=trace['trace_id']
        previous_accepted=any(x['trace_id']==tid for x in frozen['accepted'])
        common={'trace_id':tid,'raw_edges':n,'raw_length_px':length,'closed_source':bool(np.array_equal(points[0],points[-1])),'old_reason':trace['reason'],'old_accepted':previous_accepted,'old_fit_meta':trace.get('stable_fit'),'selection':'not selected'}
        if length>=6:eligible+=1
        skip='short_chain' if length<6 else 'proposal_budget' if eligible>128 else None
        if skip:
            result={'chains':[],'ledger':[{'lo':0,'hi':n,'length_px':length,'status':'rejected','reason':skip}],'total_length_px':length,'closed_source':common['closed_source']}
        elif time.monotonic()>=deadline:
            result={'chains':[],'ledger':[{'lo':0,'hi':n,'length_px':length,'status':'rejected','reason':'arm_wall_budget'}],'total_length_px':length,'closed_source':common['closed_source']};common['selection']='selected'
        else:
            common['selection']='selected';result=fit_trace(points,periodic=condition=='Q',deadline=deadline)
        safe=[]
        for chain in result['chains']:
            cc=np.asarray(chain['curves']);line=LineString(flattened(cc));raw=LineString(points);reason=None
            if raw.is_simple and not line.is_simple:reason='new_trace_selfintersection'
            if global_cubics+len(cc)>4096:reason='global_cubic_budget'
            if not reason:
                for other,otherraw in zip(retained_shapes,retained_raw):
                    if not line.envelope.intersects(other.envelope):continue
                    if line.crosses(other) and not raw.crosses(otherraw):reason='new_cross_trace_crossing';break
                    if line.overlaps(other) and not raw.overlaps(otherraw):reason='new_cross_trace_overlap';break
                    if line.equals(other):reason='duplicate_curve';break
                    if (line.crosses(other) or line.overlaps(other)) and not line.intersection(other).difference(raw.intersection(otherraw).buffer(.6)).is_empty:
                        reason='crossing_displacement';break
            if reason:veto_chain(result,chain,reason)
            else:
                safe.append(chain);retained_shapes.append(line);retained_raw.append(raw);global_cubics+=len(cc)
                output.append(dict(chain,trace_id=tid))
        result['chains']=safe
        result['accepted_length_px']=sum(x['length_px'] for x in result['ledger'] if x['status']=='accepted')
        result['rejected_length_px']=sum(x['length_px'] for x in result['ledger'] if x['status']!='accepted')
        result['closed_retained']=bool(common['closed_source'] and len(safe)==1 and safe[0]['closed'] and all(x['status']=='accepted' for x in result['ledger']))
        # Every raw edge must appear exactly once, including both sides of seam.
        cover=np.zeros(n,dtype=np.uint8)
        for row in result['ledger']:cover[row['lo']:row['hi']]+=1
        assert np.all(cover==1),(tid,cover)
        assert abs(result['accepted_length_px']+result['rejected_length_px']-length)<1e-8*max(1,length)
        result.pop('chains');records.append(dict(common,**result))
    reasons=collections.defaultdict(lambda:{'intervals':0,'length_px':0.})
    for trace in records:
        for row in trace['ledger']:
            tag=row['reason'];reasons[tag]['intervals']+=1;reasons[tag]['length_px']+=row['length_px']
    return {'condition':condition,'traces':records,'accepted':output,'summary':{'raw_trace_count':len(records),'selected_traces':sum(x['selection']=='selected' for x in records),'raw_length_px':sum(x['raw_length_px'] for x in records),'selected_length_px':sum(x['raw_length_px'] for x in records if x['selection']=='selected'),'accepted_length_px':sum(x['accepted_length_px'] for x in records),'lost_length_px':sum(x['rejected_length_px'] for x in records),'output_paths':len(output),'cubics':global_cubics,'closed_source_traces':sum(x['closed_source'] for x in records),'closed_retained_traces':sum(x['closed_retained'] for x in records),'loss_by_reason':dict(reasons)},'geometry':'NOT_ACCEPTED','region_ownership':'NOT_ESTABLISHED: stroke/contour geometry, not completed filled faces or semantics','new_source_predictions':False}

def execute(case,arm):
    protocol=json.loads((E/'protocol.json').read_text());base=Path(protocol['cases'][case]['base']);source=Path(protocol['cases'][case]['source'])
    for p in [base/arm/'construction.json',base/arm/'discovery.npz',base/'ML/predictions.npz']:
        assert hashlib.sha256(p.read_bytes()).hexdigest()==protocol['pins'][str(p)]['sha256']
    frozen=json.loads((base/arm/'construction.json').read_text());out=destination(case,arm);out.mkdir(parents=True,exist_ok=False)
    shutil.copy2(base/arm/'stable.svg',out/'O.svg')
    rgb=Image.open(source);w,h=rgb.size;start=time.monotonic()
    for condition in ['P','Q']:
        t=time.monotonic();result=construct_condition(frozen,condition,t+120)
        result.update(case=case,arm=arm,wall_seconds=time.monotonic()-t,frozen_trace_sha256=hashlib.sha256((base/arm/'construction.json').read_bytes()).hexdigest())
        (out/(condition+'.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
        (out/(condition+'.svg')).write_text(svg_graph(chain_graph(result['accepted'],w,h)),encoding='utf-8')
        print(case,arm,condition,result['summary'],'seconds',result['wall_seconds'],flush=True)
    (out/'WORKER.json').write_text(json.dumps({'wall_seconds':time.monotonic()-start,'case':case,'arm':arm},indent=2))

if __name__=='__main__':execute(*sys.argv[1:])

# END CHANGE AGD-CONTOUR-CONSTRUCTION | 2026-10-30T08:44:39Z | CREATED | Author: root
