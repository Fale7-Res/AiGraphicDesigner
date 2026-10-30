# START CHANGE AGD-CONTOUR-QA-ORIGINAL | 2026-10-30T08:40:00Z | CREATED | Author: contour_qa
"""Read-only audit of frozen construction trace accounting; no detector reruns."""
import collections
import hashlib
import json
import math
from pathlib import Path

R = Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner')
W = Path(__file__).resolve().parents[2]
E = R/'experiments/EXP_ML_CLASSICAL_HYBRID_GEOMETRY_01'
rows = []
for case in ['A01_shield','G06_arabic','K01_linear_corner_hole','fine_features','H01_horse','H02_astronaut']:
    base = W/'ml_geometry/local_only'/case if case == 'fine_features' else E/'results'/case
    for arm in ['Classical','ML','Hybrid']:
        path = base/arm/'construction.json'
        data = json.loads(path.read_text())
        reasons = collections.Counter()
        lengths = collections.Counter()
        closed = []
        occurrences = collections.Counter()
        ids = []
        for trace in data['traces']:
            ids.append(trace['trace_id'])
            p = trace['source_points_xy']
            actual = sum(math.dist(a,b) for a,b in zip(p,p[1:]))
            assert math.isclose(actual, trace['length_px'], abs_tol=1e-7)
            reasons[trace['reason']] += 1
            lengths[trace['reason']] += actual
            if p[0] == p[-1]:
                closed.append({'trace_id':trace['trace_id'],'points':len(p),'length_px':actual,'reason':trace['reason'],'old_fit':trace.get('old_fit'),'stable_fit':trace.get('stable_fit')})
            for a,b in zip(p,p[1:]):
                occurrences[tuple(sorted([tuple(a),tuple(b)]))] += 1
        assert len(ids) == len(set(ids)) == data['prefit']['raw_traces']
        assert set(ids) == set(range(len(ids)))
        rows.append({'case':case,'arm':arm,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'trace_count':len(ids),'reasons':dict(reasons),'length_by_reason':dict(lengths),'total_length_px':sum(lengths.values()),'duplicate_undirected_edges':sum(v-1 for v in occurrences.values() if v>1),'closed_traces':closed})
out = Path(__file__).parent/'ORIGINAL_TRACE_AUDIT.json'
out.write_text(json.dumps(rows,indent=2))
print(json.dumps({'cases':len(rows),'all_trace_ids_and_lengths_valid':True,'total_traces':sum(x['trace_count'] for x in rows),'duplicate_edge_occurrences':sum(x['duplicate_undirected_edges'] for x in rows),'k01':[{k:v for k,v in x.items() if k not in ['length_by_reason','source_sha256']} for x in rows if x['case'].startswith('K01')]},indent=2))
# END CHANGE AGD-CONTOUR-QA-ORIGINAL | 2026-10-30T08:40:00Z | CREATED | Author: contour_qa
