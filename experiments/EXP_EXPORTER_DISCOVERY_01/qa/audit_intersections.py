# START CHANGE AGD-EXPORT-QA-AUDIT-INTERSECTIONS | 2026-10-29T22:12:25Z | CREATED | Author: export_discovery_qa
"""Independent sampled geometric cross/overlap consistency check, not a certificate."""
import sys,json
from pathlib import Path
import numpy as np
ROOT=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_EXPORTER_DISCOVERY_01')
WORK=Path(r'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work')
sys.path.insert(0,str(WORK/'geometry-deps'))
from shapely.geometry import LineString
from shapely.strtree import STRtree
def line(chain):
    out=[];u=np.linspace(0,1,129)[:,None]
    for seg in chain['segments']:
        if seg['type']=='L':p=np.asarray([seg['p0'],seg['p3']],float)
        else:
            a,b,c,d=[np.asarray(seg[k]) for k in ('p0','p1','p2','p3')]
            p=(1-u)**3*a+3*(1-u)**2*u*b+3*(1-u)*u*u*c+u**3*d
            p[0]=a;p[-1]=d
        out.extend(p if not out else p[1:])
    if chain.get('closed') and np.linalg.norm(np.asarray(out[-1])-out[0])>0:out.append(out[0])
    return LineString(out)
def defects(g):
    ids=[c['id'] for c in g['chains']];lines=[line(c) for c in g['chains']];tree=STRtree(lines);pairs=set()
    for i,a in enumerate(lines):
        for j in tree.query(a):
            j=int(j)
            if j>i and (a.crosses(lines[j]) or a.overlaps(lines[j])):pairs.add(tuple(sorted((ids[i],ids[j]))))
    return pairs
output={}
for case in json.loads((ROOT/'BASELINE_PINS.json').read_text())['cases']:
    folder=(WORK/'exporter_discovery/external_results' if case=='fine_features' else ROOT/'results')/case
    old=defects(json.loads((folder/'R.json').read_text()));new=defects(json.loads((folder/'RB.json').read_text()))
    output[case]={'R_pairs':sorted(old),'RB_pairs':sorted(new),'new_pairs':sorted(new-old),
        'limitations':'128 equal-parameter intervals per cubic, double-precision predicates; no certified continuous intersection or intentional-junction classification.'}
(Path(__file__).parent/'intersection_audit.json').write_text(json.dumps(output,indent=2),encoding='utf-8')
print(json.dumps(output,indent=2))

# END CHANGE AGD-EXPORT-QA-AUDIT-INTERSECTIONS | 2026-10-29T22:12:25Z | CREATED | Author: export_discovery_qa
