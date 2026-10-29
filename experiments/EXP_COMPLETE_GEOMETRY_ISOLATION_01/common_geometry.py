# START CHANGE AGD-ISOLATION-COMMON-GEOMETRY | 2026-10-29T06:48:34Z | CREATED | Author: root
"""Normalize chain IDs/orientation and face references WITHOUT moving geometry."""
import copy
import numpy as np

def signature(ch):
    pts=ch['pixel_crack_vertices']
    edges=frozenset(tuple(sorted((tuple(a),tuple(b)))) for a,b in zip(pts,pts[1:]))
    return tuple(sorted(ch['adjacent_face_labels'])),edges

def normalize_to_common_faces(common,candidate):
    lookup={signature(c):c for c in candidate['chains']}
    if len(lookup)!=len(candidate['chains']):raise ValueError('Ambiguous chain edge signatures')
    obj=copy.deepcopy(common);maps=[]
    for chain in obj['chains']:
        native=lookup.pop(signature(chain))
        a=chain['pixel_crack_vertices'];b=native['pixel_crack_vertices']
        directed_a={(tuple(x),tuple(y)) for x,y in zip(a,a[1:])}
        directed_b={(tuple(x),tuple(y)) for x,y in zip(b,b[1:])}
        same=directed_a==directed_b
        if not same and directed_a!={(y,x) for x,y in directed_b}:raise ValueError('Inconsistent raw orientation')
        seg=copy.deepcopy(native['segments'])
        if not same:
            seg=seg[::-1]
            for s in seg:
                s['p0'],s['p3']=s['p3'],s['p0']
                if s['type']=='C':s['p1'],s['p2']=s['p2'],s['p1']
        chain['segments']=seg
        chain['closed']=native.get('closed',False)
        maps.append({'common_chain':chain['id'],'native_chain':native['id'],'reversed':not same})
    if lookup:raise ValueError('Extra native geometry')
    obj['normalization']={'policy':'Common raw Arena face references, exact unit-edge chain matching, native curve reversal only; coordinates/control points unchanged','chain_mapping':maps}
    return obj

# END CHANGE AGD-ISOLATION-COMMON-GEOMETRY | 2026-10-29T06:48:34Z | CREATED | Author: root
