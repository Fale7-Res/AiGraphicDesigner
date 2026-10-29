# START CHANGE AGD-THIN-TRACK-B | 2026-10-29T11:31:15Z | EDITED | Author: /root/appearance_fit
"""Bounded unit-L initialization correction; no source pixels or truth accepted."""
from __future__ import annotations
import ast,copy,importlib.util,os,time
from pathlib import Path
import numpy as np
from shapely.geometry import Polygon,LineString,box
from shapely.strtree import STRtree

FROZEN_CONFIG={'model':'single_cubic_A_B_B_C','area_epsilon':1e-6,
 'min_repaired_area_ratio':.1,'endpoint_gap_max':.001,'flatten_bound':.01,
 'near_pair_distance':.02,'collinear_chord_tolerance':1e-8,
 'max_eligible_chains':256,'max_passes':2,'max_chain_proposals':512,'max_wall_seconds':540}

def _utilities():
    location=os.environ.get('AGD_GEOMETRY_EVAL')
    directory=Path(location).parent if location else Path(__file__).resolve().parent.parent/'EXP_COMPLETE_GEOMETRY_ISOLATION_01'
    spec=importlib.util.spec_from_file_location('track_b_inherited_geometry_eval',directory/'geometry_eval.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    source=directory/'exact_area_check.py';syntax=ast.parse(source.read_text(encoding='utf-8'))
    definition=next(n for n in syntax.body if isinstance(n,ast.FunctionDef) and n.name=='segment_area')
    namespace={'np':np}
    exec(compile(ast.Module(body=[definition],type_ignores=[]),str(source),'exec'),namespace)
    return module,namespace['segment_area']

def _ring_records(graph,utilities,segment_area):
    chains={c['id']:c for c in graph['chains']}
    fitted={key:utilities.chain_points(c) for key,c in chains.items()}
    raw={key:utilities.chain_points(c,raw=True) for key,c in chains.items()}
    areas={}
    for key,chain in chains.items():
        area=sum(segment_area(s) for s in chain['segments'])
        if chain.get('closed') and chain['segments']:
            a=chain['segments'][-1]['p3'];b=chain['segments'][0]['p0'];area+=(a[0]*b[1]-a[1]*b[0])/2
        areas[key]=float(area)
    records={}
    for face,loops in graph['faces'].items():
        if int(face)==0:continue
        for index,refs in enumerate(loops):
            p,gap=utilities.ring_points(refs,fitted);r,rawgap=utilities.ring_points(refs,raw)
            poly=Polygon(p) if len(p)>=3 else Polygon();rawpoly=Polygon(r) if len(r)>=3 else Polygon()
            records[(str(face),index)]={'chains':{ref['chain'] for ref in refs},'raw_area':utilities.signed_area(r),
              'area':sum(areas[ref['chain']]*(1 if ref['forward'] else -1) for ref in refs),
              'poly':poly,'rawpoly':rawpoly,'valid':not poly.is_empty and poly.is_valid and gap<=.001,
              'rawvalid':not rawpoly.is_empty and rawpoly.is_valid and rawgap<=.001}
    return records,fitted

def _collapsed(row):
    return abs(row['raw_area'])>FROZEN_CONFIG['area_epsilon'] and abs(row['area'])<=FROZEN_CONFIG['area_epsilon']

def _unit_l(chain):
    p=np.asarray(chain['pixel_crack_vertices'],float)
    if p.shape!=(3,2) or chain.get('closed'):return False
    legs=np.diff(p,axis=0)
    return bool(np.all(np.sum(np.abs(legs),axis=1)==1) and float(legs[0]@legs[1])==0)

def _chord_collapsed(chain):
    raw=np.asarray(chain['pixel_crack_vertices'],float);a,b=raw[0],raw[-1];v=b-a;d=float(v@v)
    if d==0:return False
    points=[s[k] for s in chain['segments'] for k in (('p0','p1','p2','p3') if s['type']=='C' else ('p0','p3'))]
    if not points:return True
    if np.linalg.norm(np.asarray(chain['segments'][0]['p0'])-a)>1e-8 or np.linalg.norm(np.asarray(chain['segments'][-1]['p3'])-b)>1e-8:return False
    p=np.asarray(points);projection=a+np.clip(((p-a)@v)/d,0,1)[:,None]*v
    return bool(np.max(np.linalg.norm(p-projection,axis=1))<=1e-8)

def _pair_defects(lines,changed):
    ids=list(lines);objects=[lines[key] for key in ids];tree=STRtree(objects);bad=set();near=set()
    for key in changed:
        if key not in lines:continue
        line=lines[key]
        for index in tree.query(line.buffer(.02).envelope):
            otherkey=ids[int(index)]
            if key==otherkey:continue
            pair=tuple(sorted((key,otherkey)));other=lines[otherkey];inter=line.intersection(other)
            if inter.is_empty:
                if line.distance(other)<.02:near.add(pair)
                continue
            if line.crosses(other):bad.add(('crossing',*pair));continue
            if line.overlaps(other) or inter.length>1e-8:bad.add(('overlap',*pair));continue
            allowed=[np.asarray(a) for a in (line.coords[0],line.coords[-1]) if any(np.linalg.norm(np.asarray(a)-b)<1e-6 for b in (other.coords[0],other.coords[-1]))]
            parts=list(inter.geoms) if hasattr(inter,'geoms') else [inter]
            for part in parts:
                if part.geom_type!='Point' or not any(np.linalg.norm(np.asarray(part.coords[0])-p)<=1e-6 for p in allowed):
                    bad.add(('unexpected_touch',*pair));break
    return bad,near

def _validate_component(before,after,changed,utilities,segment_area):
    previous,oldpoints=_ring_records(before,utilities,segment_area);rows,newpoints=_ring_records(after,utilities,segment_area)
    reasons=[];affected={key for key,row in rows.items() if row['chains']&changed};faces={key[0] for key in affected}
    for key in affected:
        old,row=previous[key],rows[key]
        if not row['rawvalid']:reasons.append({'code':'invalid_raw_ring','ring':list(key)});continue
        if not row['valid'] or abs(row['area'])<=1e-6:reasons.append({'code':'invalid_or_zero_affected_ring','ring':list(key)});continue
        if row['area']*row['raw_area']<=0:reasons.append({'code':'raw_winding_changed','ring':list(key)})
        if _collapsed(old) and abs(row['area'])<max(1e-6,.1*abs(row['raw_area'])):reasons.append({'code':'insufficient_repaired_area','ring':list(key)})
    for face in faces:
        keys=[key for key in rows if key[0]==face]
        if any(not rows[key]['rawvalid'] for key in keys):reasons.append({'code':'affected_face_has_invalid_raw_ring','face':face});continue
        for i,a in enumerate(keys):
            for b in keys[i+1:]:
                if a not in affected and b not in affected:continue
                ra,rb=rows[a],rows[b]
                rawrel=(ra['rawpoly'].contains(rb['rawpoly']),rb['rawpoly'].contains(ra['rawpoly']),ra['rawpoly'].disjoint(rb['rawpoly']))
                rel=(ra['poly'].contains(rb['poly']),rb['poly'].contains(ra['poly']),ra['poly'].disjoint(rb['poly']))
                if rel!=rawrel:reasons.append({'code':'raw_hole_containment_or_disjointness_changed','rings':[list(a),list(b)]})
    oldlines={key:LineString(p) for key,p in oldpoints.items() if len(p)>=2};lines={key:LineString(p) for key,p in newpoints.items() if len(p)>=2}
    for key in changed:
        if key not in lines or not lines[key].is_simple:reasons.append({'code':'changed_chain_not_simple','chain':key})
        elif lines[key].difference(box(0,0,after['width'],after['height'])).length>1e-8:reasons.append({'code':'changed_chain_escapes_frame','chain':key})
    oldbad,_=_pair_defects(oldlines,changed);newbad,near=_pair_defects(lines,changed)
    for defect in sorted(newbad-oldbad):reasons.append({'code':'new_'+defect[0],'chains':list(defect[1:])})
    for pair in sorted(near):reasons.append({'code':'unresolved_near_pair','chains':list(pair)})
    return reasons,{'affected_rings':len(affected),'baseline_bad_pairs':len(oldbad),'candidate_bad_pairs':len(newbad),'unresolved_near_pairs':len(near)}

def initialize_safe(graph,config=None):
    """Apply only locally checked corrections; unrepaired geometry stays rejected."""
    if config is not None and config!=FROZEN_CONFIG:raise ValueError('Track B configuration is frozen')
    started=time.monotonic();utilities,segment_area=_utilities();result=copy.deepcopy(graph)
    baseline,_=_ring_records(graph,utilities,segment_area);targets={key for key,row in baseline.items() if _collapsed(row)}
    eligible=[];excluded=[]
    for chain in graph['chains']:
        incident=[row for key,row in baseline.items() if key in targets and chain['id'] in row['chains']]
        if incident and _unit_l(chain) and _chord_collapsed(chain):
            if any(row['rawvalid'] for row in incident):eligible.append(chain['id'])
            else:excluded.append({'chain':chain['id'],'reason':'no_valid_raw_target_ring'})
    eligible.sort();over=eligible[256:];eligible=eligible[:256];groups=[];remaining=set(eligible)
    while remaining:
        group={min(remaining)};front=list(group);remaining-=group
        while front:
            key=front.pop();neighbors=set().union(*(row['chains'] for row in baseline.values() if key in row['chains']))&remaining
            group|=neighbors;remaining-=neighbors;front.extend(neighbors)
        groups.append(sorted(group))
    events=[];accepted=set();attempts=0
    for iteration in range(2):
        progress=False
        for group in groups:
            if set(group)<=accepted:continue
            if attempts+len(group)>512 or time.monotonic()-started>=540:break
            attempts+=len(group);candidate=copy.deepcopy(result);lookup={c['id']:c for c in candidate['chains']}
            for key in group:
                chain=lookup[key];a,b,c=copy.deepcopy(chain['pixel_crack_vertices'])
                chain['segments']=[{'type':'C','p0':a,'p1':b,'p2':copy.deepcopy(b),'p3':c}]
            reasons,checks=_validate_component(result,candidate,set(group),utilities,segment_area)
            events.append({'pass':iteration,'chains':group,'accepted':not reasons,'rejections':reasons,**checks})
            if not reasons:result=candidate;accepted.update(group);progress=True
        if not progress:break
    final,_=_ring_records(result,utilities,segment_area)
    unrepaired=[{'face':int(key[0]),'ring':key[1],'raw_area':row['raw_area'],'fitted_area':row['area'],'raw_valid':row['rawvalid']} for key,row in final.items() if _collapsed(row)]
    assert result['faces']==graph['faces'] and len(result['chains'])==len(graph['chains'])
    for old,new in zip(graph['chains'],result['chains']):
        assert {k:v for k,v in old.items() if k!='segments'}=={k:v for k,v in new.items() if k!='segments'}
        if new['id'] in accepted:
            assert new['segments'][0]['p0']==old['pixel_crack_vertices'][0] and new['segments'][-1]['p3']==old['pixel_crack_vertices'][-1]
    audit={'config':dict(FROZEN_CONFIG),'wall_seconds':time.monotonic()-started,'target_rings_before':len(targets),
      'eligible_chains':eligible,'excluded':excluded,'over_budget_chains':over,'chain_proposals':attempts,'accepted_chains':sorted(accepted),
      'events':events,'unrepaired_collapses':unrepaired,'invalid_raw_rings_remaining':[list(key) for key,row in final.items() if not row['rawvalid']],
      'status':'BOUNDED_LOCAL_CORRECTION_ONLY_GLOBAL_GATE_NOT_CERTIFIED',
      'limitations':['Two-unit-edge L collapses only','One cubic rounds unit-L bend by about.177px; no exact sharp-corner claim','Existing unresolved invalid raw/fitted geometry retained, not silently repaired','Adaptive.01px flattening and Shapely predicates are numerical, not certified continuous topology','Area restoration is not fidelity or anti-mosaic acceptance; original unit-scale faces remain and rounded cells are not coherent artwork','No new paths/cells/topology, raw-grid fallback, appearance, source pixels or truth']}
    return result,audit
# END CHANGE AGD-THIN-TRACK-B | 2026-10-29T11:31:15Z | EDITED
