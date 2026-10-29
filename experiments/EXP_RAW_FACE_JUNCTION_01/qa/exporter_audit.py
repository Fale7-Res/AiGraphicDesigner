# START CHANGE AGD-RAWFACE-QA-EXPORTER-AUDIT | 2026-10-29T12:39:51Z | CREATED | Author: raw_face_qa
"""Passive exporter command-semantics audit of existing O/R; no SVG rerender."""
import sys,json,collections,hashlib
from pathlib import Path
import numpy as np
sys.dont_write_bytecode=True
sys.path[:0]=[str(Path('work/geometry-deps').resolve()),r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_COMPLETE_GEOMETRY_ISOLATION_01']
import geometry_eval as e
from PIL import Image
root=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_RAW_FACE_JUNCTION_01')
out={}
for case in ['fine_features','G06_arabic','A01_shield','K01_linear_corner_hole']:
 p=Path('work/raw_face_junction/external_results')/case if case=='fine_features' else root/'results'/case
 originals={n:json.loads((p/(n+'.json')).read_text(encoding='utf-8')) for n in ['O','R']}
 assert originals['O']['chains']==originals['R']['chains']
 records={}
 for name,g in originals.items():
  chains={c['id']:c for c in g['chains']};wrong=[];gaps=[]
  for face,loops in g['faces'].items():
   for ri,refs in enumerate(loops):
    initial=None;current=None
    for i,r in enumerate(refs):
     c=chains[r['chain']];s=c['segments'][0] if r['forward'] else c['segments'][-1]
     start=np.array(s['p0'] if r['forward'] else s['p3'],float)
     if initial is None:initial=start.copy()
     if current is not None and np.linalg.norm(current-start)>1e-6:gaps.append({'face':face,'ring':ri,'chain':c['id'],'gap':float(np.linalg.norm(current-start))})
     s=c['segments'][-1] if r['forward'] else c['segments'][0]
     end=np.array(s['p3'] if r['forward'] else s['p0'],float)
     if c.get('closed'):
      jump=float(np.linalg.norm(start-initial))
      if jump>1e-6:wrong.append({'face':face,'ring':ri,'chain_index':i,'chain':c['id'],'chain_start':start.tolist(),'containing_subpath_start':initial.tolist(),'unintended_Z_distance':jump})
      current=initial.copy()
     else:current=end
  genuine_gaps=[];fitted_points={k:e.chain_points(c) for k,c in chains.items()}
  for face,loops in g['faces'].items():
   for ri,refs in enumerate(loops):
    pts,gap=e.ring_points(refs,fitted_points)
    if gap>1e-6:genuine_gaps.append({'face':face,'ring':ri,'max_gap':gap})
  records[name]={'wrong_embedded_closepath':len(wrong),'examples':wrong[:30],'export_command_boundary_discontinuities':len(gaps),'gap_examples':gaps[:20],'actual_fitted_ring_gap_count':len(genuine_gaps),'actual_fitted_ring_gap_examples':genuine_gaps[:20]}
 checks=[]
 for kind,scale in [('raw',1),('raw',8),('fitted',8)]:
  a=np.array(Image.open(p/f'O_{kind}_regions_{scale}x.png').convert('RGBA'));b=np.array(Image.open(p/f'R_{kind}_regions_{scale}x.png').convert('RGBA'))
  checks.append({'kind':kind,'scale':scale,'different_pixels':int(np.any(a!=b,axis=2).sum())})
 out[case]={'chains_equal':True,'render_diffs':checks,**records}
Path('work/raw_face_qa/exporter_audit.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:{x:v for x,v in a.items() if x in ['chains_equal','render_diffs'] }|{n:{z:v for z,v in a[n].items() if z not in ['examples','gap_examples']} for n in ['O','R']} for k,a in out.items()},indent=2))

# END CHANGE AGD-RAWFACE-QA-EXPORTER-AUDIT | 2026-10-29T12:39:51Z | CREATED | Author: raw_face_qa
