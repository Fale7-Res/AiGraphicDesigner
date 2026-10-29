# START CHANGE AGD-RAWFACE-FACE-CYCLES | 2026-10-29T12:20:15Z | CREATED | Author: root
"""Exact endpoint closed-walk decomposition; no inference or curve movement."""
import copy,collections
import numpy as np
from shapely.geometry import Polygon
from shapely.validation import explain_validity
from geometry_eval import chain_points,ring_points,signed_area

def directed_occurrences(faces):
    return {str(face):collections.Counter((int(ref['chain']),bool(ref['forward'])) for ring in rings for ref in ring) for face,rings in faces.items()}

def split_closed_walk(refs,raw,max_splits=8192):
    """Partition only at exact repeated chain endpoints; retain every occurrence."""
    pending=[copy.deepcopy(refs)];result=[];splits=0
    while pending:
        walk=pending.pop();nodes=[];ends=[]
        if not walk:raise ValueError('Empty walk cannot be silently deleted')
        for ref in walk:
            p=raw[ref['chain']];p=p if ref['forward'] else p[::-1]
            if len(p)<2:raise ValueError('Unsupported raw chain')
            nodes.append(tuple(p[0]));ends.append(tuple(p[-1]))
        if any(ends[i]!=nodes[(i+1)%len(nodes)] for i in range(len(nodes))):raise ValueError('Open endpoint walk')
        seen={};cut=None
        for j,node in enumerate(nodes):
            if node in seen:cut=(seen[node],j);break
            seen[node]=j
        if cut is None:result.append(walk);continue
        i,j=cut;splits+=1
        if splits>max_splits:raise ValueError('Frozen split budget exceeded')
        # Two closed walks, no geometry inserted, removed, reordered internally.
        pending.extend([walk[:i]+walk[j:],walk[i:j]])
    return result,splits

def decompose(graph):
    original=copy.deepcopy(graph);result=copy.deepcopy(graph)
    raw={c['id']:chain_points(c,True) for c in graph['chains']}
    mapping=[];rejections=[];splits_total=0
    for face,rings in graph['faces'].items():
        new=[]
        for ri,refs in enumerate(rings):
            start=len(new);pts,gap=ring_points(refs,raw);before=Polygon(pts)
            try:
                pieces,splits=split_closed_walk(refs,raw,8192-splits_total)
                sums=sum(signed_area(ring_points(x,raw)[0]) for x in pieces)
                if abs(sums-signed_area(pts))>1e-9:raise ValueError('Signed area changed')
                if collections.Counter((x['chain'],x['forward']) for x in refs)!=collections.Counter((x['chain'],x['forward']) for q in pieces for x in q):raise ValueError('Directed occurrences changed')
            except ValueError as exc:
                pieces=[copy.deepcopy(refs)];splits=0;rejections.append({'face':face,'ring':ri,'reason':str(exc)})
            new.extend(pieces);splits_total+=splits
            records=[]
            for part in pieces:
                p,g=ring_points(part,raw);poly=Polygon(p)
                records.append({'raw_signed_area':signed_area(p),'raw_valid':bool(poly.is_valid and abs(signed_area(p))>1e-6 and g<=.001),'reason':explain_validity(poly),'refs':len(part)})
            mapping.append({'face':face,'original_ring':ri,'new_ring_indices':list(range(start,len(new))),'raw_area_before':signed_area(pts),'raw_valid_before':bool(before.is_valid and abs(signed_area(pts))>1e-6 and gap<=.001),'validity_reason_before':explain_validity(before),'splits':splits,'parts':records})
        result['faces'][face]=new
    assert result['chains']==original['chains']
    assert directed_occurrences(original['faces'])==directed_occurrences(result['faces'])
    assert {k:v for k,v in result.items() if k!='faces'}=={k:v for k,v in original.items() if k!='faces'}
    audit={'method':'exact repeated chain-endpoint walk decomposition','mapping':mapping,'splits':splits_total,'rejections':rejections,'all_non_face_fields_unchanged':True,'directed_occurrences_unchanged':True,'geometry_moved':False,'labels_changed':False,'limitations':['Point contacts remain physical point contacts; no connectivity repair','Simple rings are not a globally valid filled MultiPolygon proof','No raw internal-chain splitting or pruning of zero-area cycles','Ring count denominators change; do not infer completeness from counts']}
    return result,audit

# END CHANGE AGD-RAWFACE-FACE-CYCLES | 2026-10-29T12:20:15Z | CREATED | Author: root
