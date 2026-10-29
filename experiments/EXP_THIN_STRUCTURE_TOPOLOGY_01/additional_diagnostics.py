# START CHANGE AGD-THIN-ADDITIONAL-DIAGNOSTICS | 2026-10-29T11:43:50Z | CREATED | Author: root
from pathlib import Path
import sys,json,copy,time,datetime
import numpy as np
from PIL import Image,ImageDraw
r=Path(__file__).resolve().parent;sys.path.insert(0,str(r));sys.dont_write_bytecode=True
from study import CASES,destination,dump,PREVIOUS
from geometry_eval import svg_graph,chain_points
from analyze_matrix import render
from xml.etree import ElementTree as ET
rows=[]
for case in CASES:
 out=destination(case)
 base=json.loads((out/'baseline.json').read_text(encoding='utf-8'))
 b=json.loads((out/'B.json').read_text(encoding='utf-8'));audit=json.loads((out/'B_audit.json').read_text(encoding='utf-8'))
 accepted=set(audit['accepted_chains'])
 # Include accepted groups, otherwise one rejected group: this exposes failures too.
 ids=accepted or set(audit['events'][0]['chains'][:6] if audit['events'] else [])
 selected=[c for c in base['chains'] if c['id'] in ids]
 if selected:
  points=np.concatenate([np.asarray(c['pixel_crack_vertices']) for c in selected]);lo=points.min(0)-2;hi=points.max(0)+2
  view=f'{lo[0]} {lo[1]} {max(4,hi[0]-lo[0])} {max(4,hi[1]-lo[1])}'
  for n,g,raw in [('raw',base,True),('original',base,False),('safe',b,False)]:
   only=copy.deepcopy(g);only['chains']=[c for c in only['chains'] if c['id'] in ids]
   tree=ET.fromstring(svg_graph(only,raw=raw));tree.set('viewBox',view);tree.set('width','640');tree.set('height','400')
   for node in tree:node.set('stroke-width','.12')
   path=out/f'B_mechanism_{n}.svg';path.write_text(ET.tostring(tree,encoding='unicode'),encoding='utf-8');render(path,path.with_suffix('.png'))
 for n in ['baseline','A','B']:
  g=json.loads((out/(n+'.json')).read_text(encoding='utf-8'))
  raw_length=0.;stair_length=0.;curved=0;total=0;segments=0
  for c in g['chains']:
   p=np.asarray(c['pixel_crack_vertices'],float);d=np.diff(p,axis=0);length=np.linalg.norm(d,axis=1);raw_length+=float(length.sum())
   if len(d)>1:
    axis=(np.isclose(d[:,0],0)|np.isclose(d[:,1],0)) & np.isclose(length,1)
    turns=axis[:-1]&axis[1:]&np.isclose(np.sum(d[:-1]*d[1:],axis=1),0)
    stair_length+=float(np.sum(length[1:][turns]))
   for s in c['segments']:
    segments+=1
    if s['type']=='C':
     total+=1;a=np.asarray(s['p0']);z=np.asarray(s['p3']);v=z-a
     if np.linalg.norm(v)>1e-12:
      crosses=[abs(float(v[0]*(np.asarray(s[k])-a)[1]-v[1]*(np.asarray(s[k])-a)[0]))/np.linalg.norm(v) for k in ['p1','p2']]
      curved+=int(max(crosses)>1e-6)
  rows.append({'case':case,'condition':n,'raw_crack_length_px':raw_length,'raw_unit_axis_right_turn_step_length_px':stair_length,'raw_stair_proxy_fraction':stair_length/max(1e-12,raw_length),'cubic_commands':total,'noncollinear_cubic_commands':curved,'segments':segments,'note':'Raw staircase diagnostic measures inherited source-grid evidence, not final visual staircase length. Noncollinear cubics do not certify coherent geometry; exact sharp-corner fidelity remains unverified.'})
dump(r/'reports/GRID_COMPLEXITY_DIAGNOSTICS.json',rows)
# Crown reference overlay is evaluator-only: never supplied to constructors.
ref=json.loads((PREVIOUS/'references/shield_complete_boundary_reference.json').read_text(encoding='utf-8'))
print('reference keys',list(ref));print('reference first',str(ref)[:1200])
print('diagnostics',len(rows))

# END CHANGE AGD-THIN-ADDITIONAL-DIAGNOSTICS | 2026-10-29T11:43:50Z | CREATED | Author: root
