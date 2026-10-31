# START CHANGE AGD-UNIVERSAL-REGION-R | 2026-10-31T11:07:29Z | EDITED | Author: region_integration
"""Bounded exact-endpoint cubic DCEL research; no source/evaluator file IO.

Flattening is numerical screening only. Original cubic references are exported.
Face validity is bounded numerical evidence, not a continuous topology proof.
"""
from __future__ import annotations
import copy
import math
import time
from collections import defaultdict
import numpy as np
from shapely.geometry import LineString, Polygon, Point


def _flat(c, tolerance=.005, depth=0, deadline=None):
    if deadline is not None and time.monotonic()>deadline:raise TimeoutError('integration_wall_budget')
    chord=c[3]-c[0]; norm=np.linalg.norm(chord)
    distances=[abs(chord[0]*(v[1]-c[0,1])-chord[1]*(v[0]-c[0,0])) for v in c[1:3]]
    distance=max(distances)/norm if norm else max(np.linalg.norm(c[1:]-c[0],axis=1))
    # Collinear reversing controls can overshoot a chord while perpendicular
    # distance is zero; the polygon-length excess prevents that false shortcut.
    excess=float(np.linalg.norm(np.diff(c,axis=0),axis=1).sum()-norm)
    if distance<=tolerance and excess<=tolerance:
        return [c[0],c[3]]
    if depth>=16:raise ValueError('diagnostic_flattening_depth_budget')
    a=(c[:-1]+c[1:])/2;b=(a[:-1]+a[1:])/2;m=(b[0]+b[1])/2
    return _flat(np.array([c[0],a[0],b[0],m]),tolerance,depth+1,deadline)[:-1]+_flat(np.array([m,b[1],a[2],c[3]]),tolerance,depth+1,deadline)


def _points(curves,deadline=None):
    out=[]
    for c in curves:out.extend(_flat(c,deadline=deadline)[:-1])
    out.append(curves[-1,-1]);return np.asarray(out)


def _angle(curves,forward):
    c=curves[0] if forward else curves[-1,::-1]
    for p in c[1:]:
        d=p-c[0]
        if np.linalg.norm(d)>1e-12:return math.atan2(d[1],d[0])
    raise ValueError('zero endpoint tangent')


def _area(p):return float(np.sum(p[:-1,0]*p[1:,1]-p[1:,0]*p[:-1,1])/2)


def _reverse(refs):return [dict(chain=r['chain'],forward=not r['forward']) for r in refs[::-1]]


def integrate(items,width,height,rgb):
    """Return graph,audit. Items remain unchanged; graph chains preserve all inputs.

    graph['faces'] includes bounded atomic faces only. audit['unintegrated'] is
    exhaustive for chains not incident to a bounded face, including rejected ones.
    Numeric flattening can miss sub-tolerance events; no global acceptance claim.
    """
    start=time.monotonic();deadline=start+30
    graph=dict(width=width,height=height,chains=[],faces={})
    audit=dict(policy='design.json',rows=[],faces=[],unintegrated=[],limits=dict(paths=128,cubics=4096,wall_seconds=30),semantic_ownership='NOT_ESTABLISHED',continuous_intersection_certificate='NOT_ESTABLISHED')
    arrays={}; lines={}; endpoints={}; reasons=defaultdict(set);total=0
    for i,item in enumerate(items):
        cc=np.asarray(item['curves'],float)
        if cc.ndim!=3 or cc.shape[1:]!=(4,2) or not len(cc) or not np.isfinite(cc).all():raise ValueError('finite Nx4x2 cubics required')
        total+=len(cc);arrays[i]=cc
        graph['chains'].append(dict(id=i,closed=bool(np.array_equal(cc[0,0],cc[-1,-1])),adjacent_face_labels=[],segments=[dict(type='C',**{k:p.tolist() for k,p in zip(('p0','p1','p2','p3'),c)}) for c in cc]))
        if i>=128 or total>4096:reasons[i].add('integration_resource_budget');continue
        if any(not np.array_equal(a[-1],b[0]) for a,b in zip(cc,cc[1:])):reasons[i].add('disconnected_chain');continue
        try:p=_points(cc,deadline)
        except (TimeoutError,ValueError) as exc:
            reasons[i].add(str(exc));continue
        line=LineString(p);lines[i]=line
        endpoints[i]=(tuple(cc[0,0]),tuple(cc[-1,-1]))
        if not line.is_simple:reasons[i].add('inherited_or_fitted_selfintersection')
        if line.length<=1e-8:reasons[i].add('degenerate_chain')
    ids=list(lines)
    for ai,i in enumerate(ids):
        if time.monotonic()>deadline:
            for k in ids:reasons[k].add('integration_wall_budget')
            break
        for j in ids[ai+1:]:
            if not lines[i].envelope.intersects(lines[j].envelope):continue
            inter=lines[i].intersection(lines[j])
            if inter.is_empty:continue
            allowed=set(endpoints[i])&set(endpoints[j])
            parts=list(inter.geoms) if hasattr(inter,'geoms') else [inter]
            valid=all(p.geom_type=='Point' and tuple(p.coords[0]) in allowed for p in parts)
            if not valid:
                reasons[i].add('crossing_overlap_or_nonendpoint_contact');reasons[j].add('crossing_overlap_or_nonendpoint_contact')
    # Rotation is formed from cubic endpoint tangents, never sampled line chords.
    outgoing=defaultdict(list)
    for i in ids:
        if reasons[i]:continue
        for forward,node in zip((True,False),endpoints[i]):
            try:angle=_angle(arrays[i],forward)
            except ValueError:reasons[i].add('zero_tangent');continue
            outgoing[node].append((angle,(i,forward)))
    for node,entries in outgoing.items():
        entries.sort(key=lambda x:x[0])
        if len(entries)>1:
            for j,(a,edge) in enumerate(entries):
                b,other=entries[(j+1)%len(entries)]
                if abs(math.atan2(math.sin(a-b),math.cos(a-b)))<=1e-10:
                    reasons[edge[0]].add('ambiguous_endpoint_rotation');reasons[other[0]].add('ambiguous_endpoint_rotation')
    outgoing={node:[e for _,e in entries if not reasons[e[0]]] for node,entries in outgoing.items()}
    nxt={}
    for i in ids:
        if reasons[i]:continue
        for f in (True,False):
            at=endpoints[i][1 if f else 0];edges=outgoing[at];twin=(i,not f)
            if twin not in edges:reasons[i].add('rotation_inconsistent');continue
            nxt[(i,f)]=edges[(edges.index(twin)-1)%len(edges)]
    seen=set();cycles=[];invalid_walks=[]
    for seed in sorted(nxt):
        if seed in seen:continue
        walk=[];cur=seed
        while cur not in walk and cur not in seen and cur in nxt and len(walk)<=2*len(ids):
            walk.append(cur);cur=nxt[cur]
        seen.update(walk)
        if cur!=seed:
            invalid_walks.append(dict(reason='nonclosing_halfedge_walk',edges=walk));continue
        pts=[]
        for i,f in walk:
            p=np.asarray(lines[i].coords);p=p if f else p[::-1];pts.extend(p[:-1])
        if not pts:continue
        pts=np.asarray(pts+[pts[0]]);area=_area(pts)
        if area<=1e-8:continue
        poly=Polygon(pts)
        if not poly.is_valid or poly.area<=1e-8:
            invalid_walks.append(dict(reason='non_simple_bounded_face',edges=walk));continue
        cycles.append(dict(refs=[dict(chain=i,forward=f) for i,f in walk],polygon=poly,area=poly.area))
    # Nested disjoint components bound atomic regions, not nested painted objects.
    parents={}
    for i,c in enumerate(cycles):
        containers=[j for j,d in enumerate(cycles) if i!=j and d['area']>c['area'] and d['polygon'].contains(c['polygon'])]
        parents[i]=min(containers,key=lambda j:cycles[j]['area']) if containers else None
    image=np.asarray(rgb)
    if image.shape[:2]!=(height,width) or image.ndim!=3 or image.shape[2]<3:raise ValueError('native RGB dimensions required')
    import cv2
    lab=cv2.cvtColor(image[...,:3].astype(np.uint8),cv2.COLOR_RGB2LAB).astype(float)
    border=np.concatenate((lab[0],lab[-1],lab[:,0],lab[:,-1]));background=np.median(border,axis=0)
    used=set()
    for i,c in enumerate(cycles):
        children=[j for j,p in parents.items() if p==i]
        atomic=c['polygon']
        for j in children:atomic=atomic.difference(cycles[j]['polygon'])
        if atomic.is_empty or not atomic.is_valid:
            invalid_walks.append(dict(reason='invalid_atomic_difference',cycle=i));continue
        label=i+1;refs=[c['refs']]+[_reverse(cycles[j]['refs']) for j in children]
        graph['faces'][str(label)]=refs
        for ring in refs:
            for ref in ring:
                used.add(ref['chain']);graph['chains'][ref['chain']]['adjacent_face_labels'].append(label)
        # Bounded reproducible samples; hint never changes graph or ownership.
        x0,y0,x1,y1=atomic.bounds;xs=np.linspace(max(0,x0),min(width-1,x1),17);ys=np.linspace(max(0,y0),min(height-1,y1),17)
        samples=[lab[int(round(y)),int(round(x))] for y in ys for x in xs if atomic.contains(Point(float(x),float(y)))]
        fraction=float(np.mean(np.linalg.norm(np.asarray(samples)-background,axis=1)<=8)) if samples else None
        audit['faces'].append(dict(region_id=label,area_px2=float(atomic.area),parent_cycle=parents[i],child_cycles=children,boundary_chains=sorted({r['chain'] for ring in refs for r in ring}),source_background_fraction=fraction,background_supported_void_hint=bool(fraction is not None and fraction>=.9),semantic_hole='NOT_ESTABLISHED'))
    for i in range(len(items)):
        row=dict(chain_id=i,trace_id=items[i].get('trace_id'),integrated=i in used,reasons=sorted(reasons[i]))
        if i not in used:
            if not row['reasons']:row['reasons']=['open_or_dangling_unbounded_stroke']
            audit['unintegrated'].append(copy.deepcopy(row))
        audit['rows'].append(row)
        labels=sorted(set(graph['chains'][i]['adjacent_face_labels']))
        graph['chains'][i]['adjacent_face_labels']=labels or [0]
    audit.update(bounded_atomic_faces=len(graph['faces']),invalid_walks=invalid_walks,input_paths=len(items),input_cubics=total,integrated_paths=len(used),preserved_unintegrated_paths=len(items)-len(used),wall_seconds=time.monotonic()-start,flattening_tolerance_px=.005,endpoint_movement_px=0,geometry='NOT_ACCEPTED')
    return graph,audit
# END CHANGE AGD-UNIVERSAL-REGION-R | 2026-10-31T11:07:29Z | EDITED | Author: region_integration
