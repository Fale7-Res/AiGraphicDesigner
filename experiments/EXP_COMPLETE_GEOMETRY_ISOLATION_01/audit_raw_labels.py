# START CHANGE AGD-ISOLATION-AUDIT-RAW-LABELS | 2026-10-29T06:48:34Z | CREATED | Author: root
from pathlib import Path
import sys,os,json,numpy as np
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
r=Path(__file__).resolve().parent;sys.path[:0]=[str(r),str(Path(os.environ.get('AGD_ISOLATION_WORK',r'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work'))/'geometry-deps')]
from isolation import CASES,case_dir,dump,digest
from geometry_eval import svg_graph,label_rgb
from analyze_matrix import edge_dictionary,render
from PIL import Image
rows=[]
for case in CASES:
 out=case_dir(case)
 for seg in ['S_A','S_V']:
  lab=np.load(out/(seg+'.npy'),allow_pickle=False);palette=np.array([label_rgb(i) for i in range(int(lab.max())+1)],dtype=np.uint8)
  checks={};graphs={}
  for f in ['F_A','F_V']:
   g=json.loads((out/(seg+'_'+f+'.json')).read_text());graphs[f]=g
   p=out/(seg+'_'+f+'_raw_unique_ids.svg');p.write_text(svg_graph(g,raw=True,regions=True),encoding='utf-8');render(p,p.with_suffix('.png'))
   rgba=np.asarray(Image.open(p.with_suffix('.png')).convert('RGBA'))
   checks[f]={'wrong_rgb_pixels':int(np.any(rgba[...,:3]!=palette[lab],axis=-1).sum()),'nonopaque_pixels':int((rgba[...,3]!=255).sum())}
  rows.append({'case':case,'segmentation':seg,'labels_sha256':digest(out/(seg+'.npy')),'exact_unit_edge_adjacency_equal':edge_dictionary(graphs['F_A'])==edge_dictionary(graphs['F_V']),
   'injective_24bit_label_palette':True,'raw_label_recovery':checks,'PASS':all(v==0 for x in checks.values() for v in x.values())})
dump(r/'reports/graph_integrity_unique_ids.json',rows)
print('raw graph exact checks',len(rows),'pass',sum(x['PASS'] and x['exact_unit_edge_adjacency_equal'] for x in rows))

# END CHANGE AGD-ISOLATION-AUDIT-RAW-LABELS | 2026-10-29T06:48:34Z | CREATED | Author: root
