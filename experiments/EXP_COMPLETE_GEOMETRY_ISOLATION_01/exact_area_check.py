# START CHANGE AGD-ISOLATION-EXACT-AREA-CHECK | 2026-10-29T06:48:34Z | CREATED | Author: root
import os
from pathlib import Path
import sys,json,numpy as np
r=Path(__file__).resolve().parent;sys.path.insert(0,str(r))
from isolation import CASES,case_dir,dump
def segment_area(s):
 if s['type']=='L':return np.cross(np.array(s['p0']),np.array(s['p3']))/2
 p=np.array([s['p0'],s['p1'],s['p2'],s['p3']],float)
 c=np.array([p[0],3*(p[1]-p[0]),3*(p[2]-2*p[1]+p[0]),p[3]-3*p[2]+3*p[1]-p[0]])
 x=c[:,0];y=c[:,1];dx=np.arange(1,4)*x[1:];dy=np.arange(1,4)*y[1:]
 q=np.polynomial.polynomial.polymul(x,dy)-np.polynomial.polynomial.polymul(y,dx)
 return float(np.sum(q/np.arange(1,len(q)+1))/2)
rows=[]
for case in CASES:
 out=case_dir(case)
 for seg in ['S_A','S_V']:
  for f in ['F_A','F_V']:
   name=seg+'_'+f;g=json.loads((out/(name+'_common_faces.json')).read_text());m=json.loads((out/(name+'_common_metrics.json')).read_text());ch={c['id']:c for c in g['chains']};counts=0
   areas={}
   for c in g['chains']:
    a=sum(segment_area(s) for s in c['segments'])
    if c['closed'] and c['segments']:a+=np.cross(np.array(c['segments'][-1]['p3']),np.array(c['segments'][0]['p0']))/2
    areas[c['id']]=a
   for label,loops in g['faces'].items():
    for refs in loops:
     a=sum(areas[x['chain']]*(1 if x['forward'] else -1) for x in refs)
     raw=next(z['raw_signed_area'] for z in m['rings'] if z['face']==int(label) and z['ring']==loops.index(refs))
     counts+=abs(raw)>1e-6 and abs(a)<=1e-6
   rows.append({'case':case,'condition':name,'exact_polynomial_zero_rings':int(counts),'flattened_zero_rings':m['raw_nonzero_fit_degenerate_rings'],'agree':bool(counts==m['raw_nonzero_fit_degenerate_rings'])})
dump(r/'reports/exact_area_confirmation.json',rows)
print('exact polynomial counts agree',sum(x['agree'] for x in rows),'/',len(rows))

# END CHANGE AGD-ISOLATION-EXACT-AREA-CHECK | 2026-10-29T06:48:34Z | CREATED | Author: root
