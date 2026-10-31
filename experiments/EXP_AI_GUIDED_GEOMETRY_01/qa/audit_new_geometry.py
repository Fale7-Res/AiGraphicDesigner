# START CHANGE AGD-AGENTIC-QA-DEVIATION | 2026-10-31T14:56:09Z | CREATED | Author: agentic_qa
"""Independent dense Bernstein samples of newly committed source-fitted curves."""
from pathlib import Path
import json
import sys
import numpy as np

BASE = Path.cwd()
sys.path.insert(0,str(BASE/'work/geometry-deps'))
from shapely.geometry import LineString, Point

EXPERIMENT = Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_AI_GUIDED_GEOMETRY_01')
protocol = json.loads((EXPERIMENT/'protocol.json').read_text())
rows = []
maximum = 0.0
for case in protocol['cases']:
    folder = EXPERIMENT/'results'/case
    original = json.loads((folder/'A.json').read_text())['accepted']
    raw = {t['trace_id']:t['source_points_xy'] for t in json.loads((folder/'frozen_traces.json').read_text())['traces']}
    for condition in ('B','M'):
        state = json.loads((folder/(condition+'.json')).read_text())
        for item in state['accepted'][len(original):]:
            supported = LineString(raw[item['trace_id']])
            worst = 0.0
            t = np.linspace(0,1,257)[:,None]
            for curve in item['curves']:
                c = np.asarray(curve,float)
                points = (1-t)**3*c[0]+3*(1-t)**2*t*c[1]+3*(1-t)*t*t*c[2]+t**3*c[3]
                worst = max(worst,max(Point(p).distance(supported) for p in points))
            assert worst <= .603, (case,condition,item['trace_id'],worst)
            maximum = max(maximum,worst)
            rows.append(dict(case=case,condition=condition,trace_id=item['trace_id'],
                cubics=len(item['curves']),sampled_curve_to_raw_max_px=worst))
report = dict(paths=len(rows),maximum_observed_curve_to_raw_px=maximum,rows=rows,
    limitation='257 Bernstein samples/cubic one-sided curve-to-raw corroboration, not exact continuous proof or independent artwork accuracy')
(Path(__file__).parent/'NEW_GEOMETRY_AUDIT.json').write_text(json.dumps(report,indent=2))
print(json.dumps(dict(paths=len(rows),maximum_observed_curve_to_raw_px=maximum)))
metrics = json.loads((EXPERIMENT/'reports/METRICS.json').read_text())
for row in metrics:
    crown = next((g['support']['recall'] for g in row.get('critical_guides',[]) if g['id']=='crown_complete_visible_outline'),None)
    print(row['case'],row['condition'],'source_recall',round(row['source_trace_support']['recall'],6),
        'crown',crown,'atomic_faces',row['atomic_faces'],'tiny_length_fraction',round(row['micro']['tiny_cubic_length_weighted_fraction'],6))
# END CHANGE AGD-AGENTIC-QA-DEVIATION | 2026-10-31T14:56:09Z | CREATED | Author: agentic_qa
