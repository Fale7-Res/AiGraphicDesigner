# START CHANGE AGD-CONTOUR-CLOSURE | 2026-10-30T15:21:28Z | CREATED | Author: root
from run_case import R,E,W,OLD,destination,chain_graph,svg_graph
import json,time,hashlib,datetime,sys
from pathlib import Path
import numpy as np
from stable_fit import fit

def execute_cap_only(arm):
    protocol=json.loads((E/'protocol.json').read_text());base=Path(protocol['cases']['K01_linear_corner_hole']['base']);a=json.loads((base/arm/'construction.json').read_text());out=E/'results/K01_linear_corner_hole'/arm
    assert not (out/'CAP512.json').exists();records=[];accepted=[];start=time.monotonic()
    for trace in a['traces']:
        points=np.asarray(trace['source_points_xy']);curves,meta=fit(points,maximum_deviation=.6,maximum_segments=512)
        records.append({'trace_id':trace['trace_id'],'old_reason':trace['reason'],'new_status':meta['reason'],'meta':meta,'length_px':trace['length_px']})
        if curves is not None:accepted.append({'trace_id':trace['trace_id'],'curves':curves.tolist()})
    result={'case':'K01_linear_corner_hole','arm':arm,'condition':'CAP512_DIAGNOSTIC','only_change':'oldstablefitmaximum_segments64to512;no partition/periodic/changed .6gate','records':records,'accepted':accepted,'wall_seconds':time.monotonic()-start,'not_main_condition':True}
    (out/'CAP512.json').write_text(json.dumps(result,indent=2));(out/'CAP512.svg').write_text(svg_graph(chain_graph(accepted,192,160)),encoding='utf-8');print(arm,[(r['trace_id'],r['new_status']) for r in records],flush=True)

if __name__=='__main__':execute_cap_only(sys.argv[1])

# END CHANGE AGD-CONTOUR-CLOSURE | 2026-10-30T15:21:28Z | CREATED | Author: root
