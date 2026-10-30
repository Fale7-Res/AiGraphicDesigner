# START CHANGE AGD-ML-QA-FIT | 2026-10-30T08:12:09Z | EDITED | Author: ml_geometry_qa
"""Dense independent Bernstein evaluation of saved cubics; no fitting rerun."""
from pathlib import Path
import json,hashlib,sys
import numpy as np
sys.path.insert(0,str(Path.cwd()/'work/geometry-deps'))
import shapely
from shapely.geometry import LineString
W=Path.cwd()/'work';F=W/'ml_geometry/fitting_control';rows=[]
for p in sorted((F/'results').glob('chain_*.json')):
    data=json.loads(p.read_text());raw=np.array(data['source']);rep=json.loads((F/'replication'/p.name).read_text())
    assert data['source']==rep['source'] and data['old_curves']==rep['old_curves'] and data['new_curves']==rep['new_curves']
    assert hashlib.sha256(raw.astype('<f8').tobytes()).hexdigest()==data['row']['source_points_sha256']
    item={'chain':data['row']['chain_id'],'replicated_coordinates_exact':True}
    for tag in ['old','new']:
        t=np.linspace(0,1,1025)[:,None];pieces=[]
        for a,b,c,d in np.array(data[tag+'_curves']):pieces.append((1-t)**3*a+3*(1-t)**2*t*b+3*(1-t)*t*t*c+t**3*d)
        points=np.concatenate(pieces);overshoot=float(shapely.distance(shapely.points(points),LineString(raw)).max())
        item[tag+'_independent_dense_curve_to_raw']=overshoot
        assert abs(overshoot-data['row'][tag]['curve_to_raw_max_px'])<.003
    assert item['old_independent_dense_curve_to_raw']>.6 and item['new_independent_dense_curve_to_raw']<.6
    rows.append(item)
(W/'ml_geometry/qa/FIT_CONTROL_AUDIT.json').write_text(json.dumps(rows,indent=2));print(json.dumps(rows,indent=2))
# END CHANGE AGD-ML-QA-FIT | 2026-10-30T08:12:09Z | EDITED | Author: ml_geometry_qa
