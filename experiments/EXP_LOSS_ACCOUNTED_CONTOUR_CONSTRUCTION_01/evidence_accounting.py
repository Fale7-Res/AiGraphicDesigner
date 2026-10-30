# START CHANGE AGD-CONTOUR-CLOSURE | 2026-10-30T15:21:28Z | CREATED | Author: root
from run_case import R,E,W,OLD,destination
import json,hashlib
from pathlib import Path
import numpy as np
protocol=json.loads((E/'protocol.json').read_text());rows=[]
for case,paths in protocol['cases'].items():
    base=Path(paths['base'])
    for arm in protocol['arms']:
        a=json.loads((base/arm/'construction.json').read_text());arr=np.load(base/arm/'discovery.npz');skeleton=arr['skeleton'];covered=np.zeros_like(skeleton,bool)
        for trace in a['traces']:
            pts=np.asarray(trace['source_points_xy']);indices=np.rint(pts-.5).astype(int)
            assert np.max(abs(indices+.5-pts))<1e-8
            assert skeleton[indices[:,1],indices[:,0]].all()
            covered[indices[:,1],indices[:,0]]=True
        row={'case':case,'arm':arm,'detected_support_pixels':int(arr['support'].sum()),'skeleton_pixels':int(skeleton.sum()),'trace_covered_skeleton_pixels':int(covered.sum()),'untraced_skeleton_vertices':int((skeleton&~covered).sum()),'untraced_explanation':'Frozen historical tracer omits isolateddegree0vertices. No vectorpointbirth or gridfallback in this constructionstudy; counts retained as stage0loss, not fitterloss.','raw_trace_count':len(a['traces']),'all_trace_points_are_frozen_skeleton_centers':True}
        rows.append(row)
(E/'reports/EVIDENCE_TRACE_ACCOUNTING.json').write_text(json.dumps(rows,indent=2));print([(r['case'],r['arm'],r['untraced_skeleton_vertices']) for r in rows])

# END CHANGE AGD-CONTOUR-CLOSURE | 2026-10-30T15:21:28Z | CREATED | Author: root
