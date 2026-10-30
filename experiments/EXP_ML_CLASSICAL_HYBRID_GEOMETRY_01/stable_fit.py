# START CHANGE AGD-ML-FIT-CONTROL | 2026-10-30T07:55:54Z | CREATED | Author: fitting_stability
"""Bounded chord-aware cubic fitting; source polylines only, no reference inputs.

External research control, not a production geometry engine. The raw trace can
still encode incorrect/missing geometry. Curve acceptance does not validate it.
"""
from __future__ import annotations

import math
import time
import cv2
import numpy as np
from shapely.geometry import LineString, Point


def flatten(curve, epsilon=.002, depth=0):
    """Adaptive control-hull distance bound, excluding unresolved recursion."""
    p = np.asarray(curve, float)
    chord = p[3]-p[0]
    denom = float(chord@chord)
    t = np.clip((p[1:3]-p[0])@chord/denom, 0, 1) if denom else np.zeros(2)
    if np.linalg.norm(p[1:3]-(p[0]+t[:, None]*chord), axis=1).max() <= epsilon:
        return np.array([p[0], p[3]])
    if depth >= 24:
        raise ValueError('Unresolved curve flattening')
    a = (p[:-1]+p[1:])/2
    b = (a[:-1]+a[1:])/2
    c = (b[0]+b[1])/2
    return np.concatenate([flatten([p[0],a[0],b[0],c], epsilon, depth+1)[:-1],
                           flatten([c,b[1],a[2],p[3]], epsilon, depth+1)])


def sample_segments(points, step=.01):
    pieces = []
    for a,b in zip(points[:-1],points[1:]):
        n = max(1,int(math.ceil(np.linalg.norm(b-a)/step)))
        pieces.append(a+(b-a)*np.arange(n)[:,None]/n)
    return np.concatenate(pieces+[np.asarray(points[-1:])])


def measure(points, curves, step=.01, epsilon=.002):
    """Segment distances, never nearest sampled-vertex distances.

    Dense numerical estimates include step/2 + flatten tolerance envelopes.
    Floating predicates and flattening are not exact arithmetic certificates.
    """
    flat = np.concatenate([flatten(c,epsilon)[:-1] for c in curves]+[curves[-1,-1:]])
    raw_line, fit_line = LineString(points), LineString(flat)
    raw_samples, fit_samples = sample_segments(points,step), sample_segments(flat,step)
    # Shapely 2 vectorized distance avoids a Python Point object per sample.
    import shapely
    rd = shapely.distance(shapely.points(raw_samples), fit_line)
    fd = shapely.distance(shapely.points(fit_samples), raw_line)
    return {'raw_to_curve_max_px':float(rd.max()),'curve_to_raw_max_px':float(fd.max()),
            'numerical_upper_envelope_px':float(max(rd.max(),fd.max())+step/2+epsilon),
            'curve_to_raw_worst_xy':fit_samples[int(np.argmax(fd))].tolist(),
            'raw_to_curve_worst_xy':raw_samples[int(np.argmax(rd))].tolist(),
            'flatten_tolerance_px':epsilon,'sampling_step_px':step,
            'curve_is_simple_numerical':bool(fit_line.is_simple),
            'continuous_exact_certification':False}


def construct(vertices):
    """Per-chord handles; long neighbors cannot stretch a short chord's handle."""
    delta=np.diff(vertices,axis=0)
    lengths=np.linalg.norm(delta,axis=1)
    units=delta/np.maximum(lengths[:,None],1e-12)
    tangents=[None]*len(vertices)
    corners=np.ones(len(vertices),bool)
    for i in range(1,len(vertices)-1):
        angle=math.degrees(math.acos(float(np.clip(units[i-1]@units[i],-1,1))))
        if angle < 60:
            direction=units[i-1]+units[i]
            tangents[i]=direction/max(np.linalg.norm(direction),1e-12)
            corners[i]=False
    curves=[]
    for i,(a,b) in enumerate(zip(vertices[:-1],vertices[1:])):
        ta=units[i] if corners[i] else tangents[i]
        tb=units[i] if corners[i+1] else tangents[i+1]
        curves.append([a,a+ta*lengths[i]/3,b-tb*lengths[i]/3,b])
    return np.asarray(curves),int(corners[1:-1].sum())


def fit(points, maximum_deviation=.6, maximum_segments=64):
    """Frozen RDP, chord handles, <=8 rounds subdivision, no grid fallback.

    An unsafe candidate is rejected. Refinement adds a raw support vertex only
    when a measured failure identifies a local interval; never emits raw boxes.
    """
    started=time.perf_counter()
    points=np.asarray(points,float)
    if points.ndim!=2 or points.shape[1]!=2 or len(points)<2 or not np.isfinite(points).all():
        return None,{'reason':'invalid_input'}
    if np.any(np.linalg.norm(np.diff(points,axis=0),axis=1)<=1e-12):
        return None,{'reason':'duplicate_adjacent_points'}
    vertices=cv2.approxPolyDP(points.astype(np.float32).reshape(-1,1,2),.35,False).reshape(-1,2).astype(float)
    if len(vertices)<2:
        return None,{'reason':'insufficient_vertices'}
    # RDP vertices are original samples; establish increasing raw intervals.
    indices=[];previous=-1
    for vertex in vertices:
        remaining=np.arange(previous+1,len(points))
        found=remaining[np.argmin(np.linalg.norm(points[remaining]-vertex,axis=1))]
        indices.append(int(found));previous=int(found)
    for round_index in range(9):
        if len(indices)-1>maximum_segments:
            return None,{'reason':'cubic_budget','segments':len(indices)-1}
        if time.perf_counter()-started>30:
            return None,{'reason':'wall_budget'}
        curves,corners=construct(points[indices])
        metrics=measure(points,curves)
        if metrics['numerical_upper_envelope_px']<=maximum_deviation:
            return curves,dict(metrics,reason='accepted',segments=len(curves),
                               subdivision_rounds=round_index,intentional_corner_count=corners,
                               wall_seconds=time.perf_counter()-started)
        if round_index==8:
            break
        # Match each curve only to its frozen raw interval, conservatively
        # refining the worst interval and retaining every existing knot.
        scores=[]
        for i,c in enumerate(curves):
            local=points[indices[i]:indices[i+1]+1]
            scores.append(measure(local,np.asarray([c]))['numerical_upper_envelope_px'])
        worst=int(np.argmax(scores));lo,hi=indices[worst:worst+2]
        if hi-lo<2:
            return None,dict(metrics,reason='no_subdivision_support',segments=len(curves))
        indices.insert(worst+1,(lo+hi)//2)
    return None,dict(metrics,reason='deviation_budget',segments=len(curves))
# END CHANGE AGD-ML-FIT-CONTROL | 2026-10-30T07:55:54Z | CREATED | Author: fitting_stability
