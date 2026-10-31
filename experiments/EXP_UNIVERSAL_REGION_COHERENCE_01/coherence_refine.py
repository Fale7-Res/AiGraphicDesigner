# START CHANGE AGD-UNIVERSAL-COHERENCE | 2026-10-31T11:07:29Z | EDITED | Author: coherence_control
"""Bounded source-only refitting of exact P intervals, with chain rollback.

No image IDs, GT, segmentation edits, detector thresholds, or SVG fallback.
Caller provides the unchanged partition_fit and stable_fit modules on sys.path.
Flattened numerical predicates are not exact continuous topology certificates.
"""
from __future__ import annotations
import copy
import math
import time
import numpy as np
from shapely.geometry import LineString, Polygon
from stable_fit import flatten, measure
from partition_fit import source_partitions, signed_area

CONSTANTS = dict(deviation_px=.6, partitions_max_cubics=64,
                 trace_max_cubics=512, recursion_depth=10,
                 processed_chain_cap=32, wall_seconds=30,
                 minimum_improvement_cubics=1, flatten_epsilon_px=.002,
                 numerical_certification='sampled envelope, not exact predicates')


def polyline(curves):
    c=np.asarray(curves,float)
    return np.concatenate([flatten(v)[:-1] for v in c]+[c[-1,-1:]])


def curve_quality(curves):
    """Derivative/curvature are diagnostics, separate from pathcount/span proxies."""
    c=np.asarray(curves,float);u=np.linspace(0,1,17)
    spans=[];lengths=[];curvatures=[];turns=[];grid=[]
    for v in c:
        xy=((1-u)**3)[:,None]*v[0]+(3*(1-u)**2*u)[:,None]*v[1]+(3*(1-u)*u*u)[:,None]*v[2]+(u**3)[:,None]*v[3]
        d=3*((1-u)**2)[:,None]*(v[1]-v[0])+6*((1-u)*u)[:,None]*(v[2]-v[1])+3*(u*u)[:,None]*(v[3]-v[2])
        dd=6*(1-u)[:,None]*(v[2]-2*v[1]+v[0])+6*u[:,None]*(v[3]-2*v[2]+v[1])
        speed=np.linalg.norm(d,axis=1);good=speed>1e-8
        curvatures.extend((np.abs(d[good,0]*dd[good,1]-d[good,1]*dd[good,0])/speed[good]**3).tolist())
        angles=np.unwrap(np.arctan2(d[good,1],d[good,0]));turns.append(float(np.abs(np.diff(angles)).sum()))
        spans.append(float(np.linalg.norm(np.ptp(xy,axis=0))));lengths.append(float(np.linalg.norm(np.diff(xy,axis=0),axis=1).sum()))
        grid.extend((np.abs(xy-np.round(xy))<.05).all(axis=1).tolist())
    jumps=[]
    for a,b in zip(c[:-1],c[1:]):
        x=a[3]-a[2];y=b[1]-b[0];den=np.linalg.norm(x)*np.linalg.norm(y)
        jumps.append(math.degrees(math.acos(float(np.clip(x@y/den,-1,1)))) if den>1e-15 else 180.)
    total=sum(lengths)
    return dict(cubics=len(c),sampled_curve_length_px=total,
                short_cubic_count=sum(x<=2 for x in spans),
                length_fraction_cubic_span_le2px=float(sum(l for s,l in zip(spans,lengths) if s<=2)/max(total,1e-15)),
                maximum_tangent_jump_degrees=max(jumps,default=0.),
                tangent_jump_sum_degrees=sum(jumps),
                within_cubic_absolute_turn_radians=sum(turns),
                sampled_curvature_max=max(curvatures,default=0.),
                sampled_curvature_p95=float(np.quantile(curvatures,.95)) if curvatures else 0.,
                sampled_integer_lattice_fraction=float(np.mean(grid)))


def _unit(vector):
    size=float(np.linalg.norm(vector))
    return vector/size if size>1e-12 else None


def _least_square(points,left,right):
    """Nonnegative endpoint handle scalars keep the inherited tangent directions."""
    p=np.asarray(points,float);arc=np.r_[0,np.cumsum(np.linalg.norm(np.diff(p,axis=0),axis=1))]
    if arc[-1]<=1e-12:raise ValueError('zero support')
    t=arc/arc[-1];a=3*(1-t)**2*t;b=3*(1-t)*t*t
    base=(1-t**3)[:,None]*p[0]+(t**3)[:,None]*p[-1]
    # P1=P0+alpha*left and P2=P3-beta*right. Endpoint base includes
    # Bernstein endpoint and handle-base terms, so endpoints remain exact.
    base=((1-t)**3+a)[:,None]*p[0]+(b+t**3)[:,None]*p[-1]
    design=np.stack([a[:,None]*left,-b[:,None]*right],axis=-1).reshape(-1,2)
    target=(p-base).reshape(-1)
    # Two-point/collinear supports underdetermine the two handle lengths.
    # Positive one-third chord handles give the standard straight cubic;
    # the same original-source deviation gate still validates the proposal.
    values=np.linalg.lstsq(design,target,rcond=None)[0] if np.linalg.matrix_rank(design)==2 else np.repeat(np.linalg.norm(p[-1]-p[0])/3,2)
    # An inadmissible tangent solution is rejected instead of flipping handles.
    if np.any(values<=1e-9) or np.any(values>arc[-1]*2):return None
    return np.asarray([p[0],p[0]+values[0]*left,p[-1]-values[1]*right,p[-1]])


def _piecewise(points,left,right,deadline,depth=0):
    if time.monotonic()>=deadline:raise TimeoutError('coherence_wall_budget')
    p=np.asarray(points,float);one=_least_square(p,left,right)
    if one is not None:
        m=measure(p,np.asarray([one]))
        if m['numerical_upper_envelope_px']<=CONSTANTS['deviation_px']:
            return np.asarray([one])
    if depth>=CONSTANTS['recursion_depth'] or len(p)<3:raise ValueError('local_fit_unsafe')
    # Source-only balanced split: no evaluator points or benchmark coordinates.
    arc=np.r_[0,np.cumsum(np.linalg.norm(np.diff(p,axis=0),axis=1))]
    k=int(np.clip(np.searchsorted(arc,arc[-1]/2),1,len(p)-2))
    before=_unit(p[k]-p[k-1]);after=_unit(p[k+1]-p[k])
    turn=math.degrees(math.acos(float(np.clip(before@after,-1,1))))
    tangent=_unit(before+after)
    if tangent is None or turn>=60:lt,rt=before,after
    else:lt=rt=tangent
    a=_piecewise(p[:k+1],left,lt,deadline,depth+1)
    b=_piecewise(p[k:],rt,right,deadline,depth+1)
    out=np.concatenate([a,b])
    if len(out)>CONSTANTS['partitions_max_cubics']:raise ValueError('partition_cubic_budget')
    return out


def _proposal(item,points,deadline):
    old=np.asarray(item['curves'],float);intervals,_=source_partitions(points)
    parts=item.get('partition_ids')
    if parts is None:raise ValueError('missing_partition_provenance')
    cursor=0;new=[];rows=[]
    for pid in parts:
        lo,hi=intervals[pid];raw=points[lo:hi+1]
        if cursor>=len(old) or not np.array_equal(old[cursor,0],raw[0]):raise ValueError('partition_start_mismatch')
        end=cursor
        while end<len(old) and not np.array_equal(old[end,-1],raw[-1]):end+=1
        if end>=len(old):raise ValueError('partition_end_mismatch')
        previous=old[cursor:end+1];cursor=end+1
        left=_unit(previous[0,1]-previous[0,0]);right=_unit(previous[-1,3]-previous[-1,2])
        if left is None or right is None:raise ValueError('degenerate_original_handle')
        proposed=_piecewise(raw,left,right,deadline)
        metric=measure(raw,proposed)
        if metric['numerical_upper_envelope_px']>CONSTANTS['deviation_px']:raise ValueError('final_deviation')
        new.extend(proposed);rows.append(dict(partition_id=int(pid),lo=int(lo),hi=int(hi),before_cubics=len(previous),after_cubics=len(proposed),deviation=metric))
    if cursor!=len(old):raise ValueError('unaccounted_original_cubics')
    out=np.asarray(new)
    if len(out)>CONSTANTS['trace_max_cubics']:raise ValueError('trace_cubic_budget')
    if len(out)>=len(old):raise ValueError('no_cubic_reduction')
    return out,rows


def refine(items,originaltraces):
    """Return unchanged-schema items plus exhaustive chain decision audit.

    Items are accepted P chains with curves, trace_id, partition_ids and closed.
    originaltraces is a list of trace_id/source_points_xy records (or dict keyed
    by trace_id). Chain rollback preserves all original curves and metadata.
    """
    start=time.monotonic();deadline=start+CONSTANTS['wall_seconds']
    source={x['trace_id']:np.asarray(x['source_points_xy'],float) for x in originaltraces} if isinstance(originaltraces,list) else {k:np.asarray(v.get('source_points_xy',v) if isinstance(v,dict) else v,float) for k,v in originaltraces.items()}
    output=copy.deepcopy(items);oldlines=[LineString(polyline(v['curves'])) for v in items];lines=list(oldlines)
    order=sorted(range(len(items)),key=lambda i:(-oldlines[i].length,i));selected=set(order[:CONSTANTS['processed_chain_cap']]);audit=[]
    for i in order:
        item=items[i];old=np.asarray(item['curves'],float)
        row=dict(item_index=i,trace_id=item['trace_id'],status='rollback',before=curve_quality(old))
        if i not in selected:row['reason']='chain_cap_not_attempted';audit.append(row);continue
        if time.monotonic()>=deadline:row['reason']='wall_budget_not_attempted';audit.append(row);continue
        try:
            candidate,partrows=_proposal(item,source[item['trace_id']],deadline)
            candidate_line=LineString(polyline(candidate));oldline=lines[i]
            if not np.array_equal(candidate[0,0],old[0,0]) or not np.array_equal(candidate[-1,-1],old[-1,-1]):raise ValueError('endpoint_moved')
            # Do not attempt to classify inherited self-crossings as intentional.
            # A nonsimple proposal is retained only as its unchanged P rollback.
            if not candidate_line.is_simple:raise ValueError('candidate_nonsimple')
            if item.get('closed'):
                if not np.array_equal(candidate[0,0],candidate[-1,-1]):raise ValueError('closure_lost')
                oa=signed_area(polyline(old));na=signed_area(polyline(candidate))
                if abs(na)<=1e-9 or oa*na<=0:raise ValueError('winding_or_area_changed')
            for j,other in enumerate(lines):
                if j==i:continue
                if not candidate_line.envelope.intersects(other.envelope) and not oldline.envelope.intersects(other.envelope):continue
                if candidate_line.equals(other):raise ValueError('duplicate_curve')
                if candidate_line.crosses(other) and not oldline.crosses(other):raise ValueError('new_mutual_crossing')
                if candidate_line.overlaps(other) and not oldline.overlaps(other):raise ValueError('new_mutual_overlap')
                if oldline.intersects(other)!=candidate_line.intersects(other):raise ValueError('junction_incidence_changed')
                if candidate_line.crosses(other) or candidate_line.overlaps(other):
                    if not candidate_line.intersection(other).difference(oldline.intersection(other).buffer(.6)).is_empty:raise ValueError('crossing_displaced')
                if item.get('closed') and items[j].get('closed') and oldline.is_simple and other.is_simple and candidate_line.is_simple:
                    if Polygon(oldline).contains(Polygon(other))!=Polygon(candidate_line).contains(Polygon(other)):raise ValueError('containment_changed')
                    if Polygon(other).contains(Polygon(oldline))!=Polygon(other).contains(Polygon(candidate_line)):raise ValueError('containment_changed')
            after=curve_quality(candidate)
            if after['maximum_tangent_jump_degrees']>max(60.,row['before']['maximum_tangent_jump_degrees'])+1e-6:raise ValueError('new_sharp_join')
            output[i]['curves']=candidate.tolist();lines[i]=candidate_line
            row.update(status='accepted',reason='fewer_cubics_same_source_envelope',partitions=partrows,after=after)
        except (ValueError,TimeoutError,np.linalg.LinAlgError) as exc:
            row.update(reason=str(exc),after=row['before'])
        audit.append(row)
    return output,dict(constants=CONSTANTS,chains=audit,wall_seconds=time.monotonic()-start,
                       accepted_changes=sum(x['status']=='accepted' for x in audit),
                       complete_geometric_acceptance=False,
                       source_deviation_gate_unchanged=True,continuous_exact_certification=False)
# END CHANGE AGD-UNIVERSAL-COHERENCE | 2026-10-31T11:07:29Z | EDITED | Author: coherence_control
