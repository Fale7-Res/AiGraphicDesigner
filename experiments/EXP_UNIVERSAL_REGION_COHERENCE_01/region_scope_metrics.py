# START CHANGE AGD-UNIVERSAL-REGION-SCOPE | 2026-10-31T11:07:29Z | EDITED | Author: root
"""Separate preserved proposal metrics from actually integrated face boundaries."""
from universal_run import E,output_folder
from evaluate import references
from evaluate_results import samples_from_items,support_stats,xy
from stable_fit import sample_segments
import json
import numpy as np
def separate_region_scope():
 allrows=json.loads((E/'reports/METRICS.json').read_text());p=json.loads((E/'protocol.json').read_text())
 for case in p['cases']:
  out=output_folder(case);_,target,_,tag=references(case,out/'source.png');source=xy(np.load(out/'evidence.npz')['skeleton'])
  for c in ['R','SR']:
   d=json.loads((out/(c+'.json')).read_text());audit=json.loads((out/(c+'_audit.json')).read_text());indices={r['chain_id'] for r in audit['rows'] if r['integrated']};items=[v for i,v in enumerate(d['accepted']) if i in indices];_,pts=samples_from_items(items);m=next(m for m in allrows if m['case']==case and m['condition']==c)
   m['metric_geometry_scope']='Default topology/contour metrics describe ALL preserved P/S proposals including unintegrated strokes. Region SVG shows only integrated atomic faces; separate integrated_only metrics below. A filled region is not inferred from successful stroke rendering.'
   m['integrated_only']=dict(paths=len(items),source_proxy=support_stats(source,pts,1.25),boundary=support_stats(target,pts,1.25) if target is not None else None)
   if m.get('critical_guides'):
    from universal_run import R
    guides=json.loads((R/'experiments/EXP_COMPLETE_GEOMETRY_ISOLATION_01/references/shield_complete_boundary_reference.json').read_text());m['integrated_only']['critical_guides']=[]
    for g in guides['components']+guides['appearance_only']:
     q=np.concatenate([sample_segments(np.asarray(v,float),.25) for v in g['polylines']]);m['integrated_only']['critical_guides'].append(dict(id=g['id'],fitted=support_stats(q,pts,g['uncertainty_px'])))
   (out/(c+'_metrics.json')).write_text(json.dumps(m,indent=2))
 (E/'reports/METRICS.json').write_text(json.dumps(allrows,indent=2))
if __name__=='__main__':separate_region_scope()
# END CHANGE AGD-UNIVERSAL-REGION-SCOPE | 2026-10-31T11:07:29Z | EDITED | Author: root
