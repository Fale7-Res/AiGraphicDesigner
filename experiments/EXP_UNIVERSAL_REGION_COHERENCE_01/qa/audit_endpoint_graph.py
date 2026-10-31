# START CHANGE AGD-UNIVERSAL-QA | 2026-10-31T10:59:34Z | CREATED | Author: universal_qa
"""Independent BFS multigraph rank recomputation; no selection/geometry changes."""
from pathlib import Path
import json
import collections
import numpy as np
work=Path.cwd()/'work'
exp=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_UNIVERSAL_REGION_COHERENCE_01')
rows=json.loads((exp/'reports/ENDPOINT_GRAPH_DIAGNOSTIC.json').read_text())
failures=[];result=[]
for row in rows:
    case=row['case'];folder=work/'universal_geometry/local_only'/case if case=='fine_features' else exp/'results'/case
    raw=json.loads((folder/'frozen_traces.json').read_text())['traces'];byid={r['trace_id']:r for r in raw}
    groups={'all_raw':raw,'eligible6':[r for r in raw if float(np.linalg.norm(np.diff(np.asarray(r['source_points_xy']),axis=0),axis=1).sum())>=6]}
    for tag in ('P','S'):
        d=json.loads((folder/(tag+'.json')).read_text());groups[tag+'_selected']=[byid[r['trace_id']] for r in d['traces'] if r['selection']=='selected']
    stages={}
    for stage,traces in groups.items():
        adjacency=collections.defaultdict(set);degree=collections.Counter()
        for trace in traces:
            p=trace['source_points_xy'];a,b=tuple(p[0]),tuple(p[-1]);adjacency[a].add(b);adjacency[b].add(a);degree[a]+=1;degree[b]+=1
        seen=set();components=0
        for a in adjacency:
            if a in seen:continue
            components+=1;todo=[a]
            while todo:
                n=todo.pop()
                if n in seen:continue
                seen.add(n);todo.extend(adjacency[n]-seen)
        stats={'edges':len(traces),'vertices':len(adjacency),'components':components,
               'cycle_rank':len(traces)-len(adjacency)+components,
               'junctions':sum(d>=3 for d in degree.values()),'degree1_ends':sum(d==1 for d in degree.values())}
        for key,value in stats.items():
            if row['stages'][stage][key]!=value:failures.append(case+stage+key+': mismatch')
        stages[stage]=stats
    result.append({'case':case,'stages':stages})
output={'rows':result,'failures':failures,'passed':not failures,
        'limitation':'E-V+C is abstract endpoint multigraph independent-cycle dimension; not simple physical face or hole count. Pixel/texture/junction artifacts can create cycles.'}
Path(__file__).with_name('ENDPOINT_GRAPH_AUDIT.json').write_text(json.dumps(output,indent=2))
print(json.dumps({'cases':len(result),'failures':failures}))
# END CHANGE AGD-UNIVERSAL-QA | 2026-10-31T10:59:34Z | CREATED | Author: universal_qa
