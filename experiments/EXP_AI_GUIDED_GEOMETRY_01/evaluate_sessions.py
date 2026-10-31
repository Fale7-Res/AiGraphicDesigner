# START CHANGE AGD-AGENTIC-EVALUATE | 2026-10-31T15:16:13Z | EDITED | Author: root
"""Reference-only evaluation and actual vector rendering, never controller input."""
from run_sessions import R,W,E,L
from pathlib import Path
import sys,json,time,copy,subprocess,html
import numpy as np
from PIL import Image,ImageDraw,ImageOps
from scipy import ndimage
from xml.etree import ElementTree as ET
from evaluate import references,topology_diagnostics,micro_diagnostics
from evaluate_results import support_stats,samples_from_items,xy,render
from stable_fit import sample_segments
from region_integration import integrate
from monitor import supervise

def evaluate_sessions():
 protocol=json.loads((E/'protocol.json').read_text());rows=[]
 for case,cfg in protocol['cases'].items():
  out=E/'results'/case
  if not (out/'WORKER.json').exists():continue
  rgb,target,holes,tag=references(case,out/'source.png');h,w=rgb.shape[:2];raws=json.loads((out/'frozen_traces.json').read_text())['traces'];rawdict={t['trace_id']:t for t in raws};rawpts=np.unique(np.concatenate([np.asarray(t['source_points_xy']) for t in raws]),axis=0)
  if case=='H03_original_vector':
   truthpng=out/'truth_8x.png';render(E/'references/H03_source.svg',truthpng,w,h,8);pixels=np.asarray(Image.open(truthpng).convert('RGB'));mask=np.linalg.norm(pixels.astype(float)-255,axis=2)>8;target=xy(mask^ndimage.binary_erosion(mask))/8;tag='Independent first-party source-vector8x mask boundary; evaluator-only'
  guides=json.loads((R/'experiments/EXP_COMPLETE_GEOMETRY_ISOLATION_01/references/shield_complete_boundary_reference.json').read_text()) if case=='A01_shield' else None
  for condition in ['A','B','M']:
   data=json.loads((out/(condition+'.json')).read_text());items=data['accepted'];lines,points=samples_from_items(items);top=topology_diagnostics(items,rawdict);graph,audit=integrate(items,w,h,rgb)
   m=dict(case=case,condition=condition,AI_performance='NOT_TESTED',reference=tag,paths=len(items),cubics=sum(len(i['curves']) for i in items),source_trace_support=support_stats(rawpts,points,1.25),topology=top,micro=micro_diagnostics(items),atomic_faces=audit['bounded_atomic_faces'],integration_limit='Evaluation only. Engine outputs boundary proposals; atomic partitions are not semantic regions/holes.',render_seconds={},api_requests=0,actual_api_cost_usd=0,geometry='NOT_ACCEPTED')
   if target is not None:m['boundary_1_25px']=support_stats(target,points,1.25);m['hole_support_NOT_ownership']=[support_stats(q,points,1.25) for q in holes]
   if guides:
    m['critical_guides']=[]
    for g in guides['components']+guides['appearance_only']:
     q=np.concatenate([sample_segments(np.asarray(p,float),.25) for p in g['polylines']]);m['critical_guides'].append(dict(id=g['id'],uncertainty_px=g['uncertainty_px'],required=g.get('structural_boundary_required',False),support=support_stats(q,points,g['uncertainty_px'])))
   for scale in [1,4]:m['render_seconds'][str(scale)]=render(out/(condition+'.svg'),out/(condition+f'_{scale}x.png'),w,h,scale)
   root=ET.parse(out/(condition+'.svg')).getroot();assert not any(el.tag.rsplit('}',1)[-1] in ['image','rect','script','foreignObject'] for el in root.iter())
   roi=[115,70,145,100] if case=='A01_shield' else [w//4,h//4,min(128,w//2),min(96,h//2)];root.set('viewBox',' '.join(map(str,roi)));root.set('width',str(roi[2]));root.set('height',str(roi[3]));(out/(condition+'_detail.svg')).write_text(ET.tostring(root,encoding='unicode'))
   for scale in [1,4,16]:m['render_seconds']['detail'+str(scale)]=render(out/(condition+'_detail.svg'),out/(condition+f'_detail_{scale}x.png'),roi[2],roi[3],scale)
   Image.fromarray(rgb).convert('RGBA').save(out/'source_rgba.png');overlay=Image.fromarray(rgb).convert('RGBA');overlay.alpha_composite(Image.open(out/(condition+'_1x.png')).convert('RGBA'));overlay.save(out/(condition+'_overlay.png'))
   from scipy.spatial import cKDTree
   missing=rawpts if not len(points) else rawpts[cKDTree(points).query(rawpts)[0]>1.25];diag=Image.fromarray(rgb.copy());draw=ImageDraw.Draw(diag)
   for x,y in missing:draw.point((int(x),int(y)),fill=(255,0,140))
   diag.save(out/(condition+'_missing_source_trace.png'));m['missing_overlay_limit']='Magenta absent raw trace evidence, may be lighting/texture; not exact missing artwork truth.'
   if condition!='A':
    m.update(calls=data['calls'],commits=data['commits'],decision_hash=data['decision_hash']);m['event_status_counts']={s:sum(ev['status']==s for ev in data['tool_events']) for s in ['ok','rejected']}
   (out/(condition+'_metrics.json')).write_text(json.dumps(m,indent=2));rows.append(m)
  sheet=Image.new('RGB',(4*330,300),'white');draw=ImageDraw.Draw(sheet)
  for i,c in enumerate(['source','A','B','M']):
   im=Image.open(out/('source.png' if c=='source' else c+'_1x.png')).convert('RGBA');white=Image.new('RGBA',im.size,'white');white.alpha_composite(im);sheet.paste(ImageOps.contain(white.convert('RGB'),(314,260)),(i*330+8,30));draw.text((i*330+8,8),{'source':'Source','A':'A automatic P','B':'B deterministic tools','M':'M fixed MOCK; NOT AI'}[c],fill='black')
  sheet.save(out/'comparison.png');print(case,'evaluated',flush=True)
  (E/'reports/METRICS.json').write_text(json.dumps(rows,indent=2))
 return rows

if __name__=='__main__':
 if '--worker' in sys.argv:evaluate_sessions()
 else:
  result=supervise([sys.executable,Path(__file__),'--worker'],E/'reports/evaluation.log',wall_seconds=600);(E/'reports/EVALUATION_RESOURCES.json').write_text(json.dumps(result,indent=2));print(result)
# END CHANGE AGD-AGENTIC-EVALUATE | 2026-10-31T15:16:13Z | EDITED | Author: root
