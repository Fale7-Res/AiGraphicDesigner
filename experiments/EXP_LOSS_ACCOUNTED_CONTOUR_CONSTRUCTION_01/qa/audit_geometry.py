# START CHANGE AGD-CONTOUR-QA-GEOMETRY | 2026-10-30T08:46:40Z | CREATED | Author: contour_qa
"""Independent Bernstein sampling and predicates on SAVED candidates only."""
import sys,json,math
from pathlib import Path
W=Path(__file__).resolve().parents[2];sys.path.insert(0,str(W/'geometry-deps'))
import numpy as np
import shapely
from shapely.geometry import LineString
from shapely.strtree import STRtree
R=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner');E=R/'experiments/EXP_LOSS_ACCOUNTED_CONTOUR_CONSTRUCTION_01'
protocol=json.loads((E/'protocol.json').read_text());rows=[]
t=np.linspace(0,1,129);B=np.stack([(1-t)**3,3*(1-t)**2*t,3*(1-t)*t*t,t**3],axis=1)
for case,config in protocol['cases'].items():
 for arm in protocol['arms']:
  original=json.loads((Path(config['base'])/arm/'construction.json').read_text());sources={x['trace_id']:np.array(x['source_points_xy']) for x in original['traces']}
  base=(W/'contour_construction/local_only'/case if case=='fine_features' else E/'results'/case)/arm
  for condition in ['P','Q']:
   if not (base/(condition+'.json')).exists():continue
   data=json.loads((base/(condition+'.json')).read_text());byid={x['trace_id']:x for x in data['traces']}
   shapes=[];rawshapes=[];chains=data['accepted'];worst=0.;worstrow=None;worst_reverse=0.;new_self=[];endpoints=0;short_cubics=0;short_chord=0.;chord_sum=0.;cubic_count=0
   for ci,chain in enumerate(chains):
    p=sources[chain['trace_id']];cc=np.array(chain['curves']);q=np.einsum('tk,nkd->ntd',B,cc).reshape(-1,2)
    spans=np.ptp(cc,axis=1).max(axis=1);chords=np.linalg.norm(cc[:,-1]-cc[:,0],axis=1);tiny=spans<=2
    short_cubics+=int(tiny.sum());short_chord+=float(chords[tiny].sum());chord_sum+=float(chords.sum());cubic_count+=len(cc)
    shape=LineString(q);raw=LineString(p);shapes.append(shape);rawshapes.append(raw)
    if raw.is_simple and not shape.is_simple:new_self.append(ci)
    offset=0
    lookup={x['partition_id']:x for x in byid[chain['trace_id']]['ledger'] if x['status']=='accepted'}
    for pi in chain['partition_ids']:
     part=lookup[pi];count=part['cubics'];curves=cc[offset:offset+count];offset+=count
     line=LineString(p[part['lo']:part['hi']+1]);sample=np.einsum('tk,nkd->ntd',B,curves).reshape(-1,2)
     error=float(shapely.distance(shapely.points(sample),line).max())
     rawpts=p[part['lo']:part['hi']+1];dense=[]
     for a,b in zip(rawpts,rawpts[1:]):
      count=max(1,int(math.ceil(np.linalg.norm(b-a)/.05)))
      dense.extend(a+(b-a)*fraction/count for fraction in range(count))
     dense.append(rawpts[-1]);reverse=float(shapely.distance(shapely.points(dense),LineString(sample)).max())
     worst_reverse=max(worst_reverse,reverse)
     if error>worst:worst=error;worstrow=[chain['trace_id'],pi]
     assert error<=.60001,(case,arm,condition,chain['trace_id'],pi,error)
     assert reverse<=.603,(case,arm,condition,chain['trace_id'],pi,reverse)
     assert np.array_equal(curves[0,0],p[part['lo']]) and np.array_equal(curves[-1,-1],p[part['hi']]);endpoints+=2
    assert offset==len(cc)
   tree=STRtree(shapes);newpairs=[];inheritedpairs=0
   for i,line in enumerate(shapes):
    for j in tree.query(line):
     j=int(j)
     if j>=i:continue
     if line.crosses(shapes[j]) or line.overlaps(shapes[j]):
      if not (rawshapes[i].crosses(rawshapes[j]) or rawshapes[i].overlaps(rawshapes[j])):newpairs.append([j,i])
      else:inheritedpairs+=1
   rows.append({'case':case,'arm':arm,'condition':condition,'chains':len(chains),'endpoint_checks':endpoints,'new_self_intersections':new_self,'new_mutual_crossing_or_overlap_pairs':newpairs,'inherited_crossing_pairs':inheritedpairs,'maximum_Bernstein_curve_to_raw_distance_px':worst,'maximum_raw_to_Bernstein_polyline_distance_px':worst_reverse,'cubic_count':cubic_count,'cubic_control_bbox_le2px':short_cubics,'short_cubic_chord_length_fraction':short_chord/max(chord_sum,1e-9),'worst_trace_and_partition':worstrow,'sampling':'129 points per cubic, direct Bernstein evaluation independent of fitter flattening; reverse source samples <=.05px step to Bernstein polyline, .003 numerical-comparison allowance. Numerical check, not exact continuous certificate.'})
out={'conditions':len(rows),'rows':rows,'all_curve_samples_within_unchanged_gate':True,'new_crossing_pairs_total':sum(len(x['new_mutual_crossing_or_overlap_pairs']) for x in rows),'new_self_intersections_total':sum(len(x['new_self_intersections']) for x in rows)}
(Path(__file__).parent/'GEOMETRY_AUDIT.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
# END CHANGE AGD-CONTOUR-QA-GEOMETRY | 2026-10-30T08:46:40Z | CREATED | Author: contour_qa
