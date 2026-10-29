# START CHANGE AGD-THIN-EVALUATE-STUDY | 2026-10-29T08:39:37Z | CREATED | Author: root
"""Evaluator-only reporting using frozen independent geometry references."""
import os,sys,json,time
from pathlib import Path
from study import ROOT,PREVIOUS,WORK,CASES,destination,dump,digest,inherited_case_dir
from geometry_eval import evaluate,svg_graph,chain_points,uniform_points
from validate_geometry import known_mask_evaluation,visible_microgeometry,mask_topology
from final_diagnostics import coverage_geometry,visible_micro
from analyze_matrix import render,ZOOMS
import numpy as np
from PIL import Image
from scipy import ndimage

def separation_errors(truth,pred):
    t,nt=ndimage.label(truth);p,npred=ndimage.label(pred)
    if nt==0:return {'status':'EMPTY_REFERENCE_NOT_EVALUABLE','false_split_excess':None,'false_join_excess':None,'truth_components':0,'pred_components':npred}
    overlaps=[]
    for a in range(1,nt+1):
        values,counts=np.unique(p[t==a],return_counts=True)
        overlaps.append([int(v) for v,n in zip(values,counts) if v and n>=max(1,.05*np.sum(t==a))])
    false_splits=sum(max(0,len(x)-1) for x in overlaps)
    false_joins=sum(max(0,sum(i in x for x in overlaps)-1) for i in range(1,npred+1))
    return {'false_split_excess':false_splits,'false_join_excess':false_joins,'truth_components':nt,'pred_components':npred,'rule':'Atleast5percentoftruthcomponentoverlap; diagnostic not exact ownership.'}

def evaluate_candidate(case,name):
    out=destination(case);g=json.loads((out/(name+'.json')).read_text(encoding='utf-8'));labels=np.load(out/(name+'_labels.npy'),allow_pickle=False)
    reference=json.loads((PREVIOUS/'references/shield_complete_boundary_reference.json').read_text(encoding='utf-8')) if case=='A01_shield' else None
    m=evaluate(g,reference);m['case']=case;m['condition']=name;m['candidate_sha256']=digest(out/(name+'.json'))
    m['microgeometry']=visible_microgeometry(g,labels)
    m['coverage']=coverage_geometry(g)
    m['visible_microgeometry']=visible_micro(g,m,out,name)
    known={x['id']:x for x in json.loads((PREVIOUS/'references/known_control_reference_manifest.json').read_text(encoding='utf-8'))['references']}
    if case in known:
        m['known_geometry']=known_mask_evaluation(case,g,labels,known[case],out,name)
        truth=np.asarray(Image.open(known[case]['local_only_mask_path']).convert('L'))>=128
        pred=np.asarray(Image.open(out/(name+'_foreground_8x.png')).convert('RGBA'))[...,3]>=128
        m['known_geometry']['separation']=separation_errors(truth,pred)
        from skimage.morphology import skeletonize
        skeleton=skeletonize(truth);tw=ndimage.distance_transform_edt(truth)[skeleton]*2/8;pw=ndimage.distance_transform_edt(pred)[skeleton]*2/8
        m['known_geometry']['reference_centerline_width_mae_px']=float(np.mean(abs(tw-pw))) if len(tw) else None
        m['known_geometry']['width_measurement_limit']='Widths evaluated at truth medial samples; zero where missing; not deployable correspondence.'
    if case=='G06_arabic':
        # Source-only binary proxy: useful topology diagnostic, NOT independent
        # high-resolution glyph truth or typography reconstruction acceptance.
        import subprocess
        from analyze_matrix import RESVG
        rgb=np.asarray(Image.open(out/'working.png').convert('RGB')).astype(float)
        proxy=np.linalg.norm(rgb-rgb[0,0],axis=-1)>8
        fg=[int(v) for v in np.unique(labels) if np.mean(proxy[labels==v])>=.5]
        pth=out/(name+'_arabic_foreground.svg');pth.write_text(svg_graph(g,regions=True,foreground=set(fg)),encoding='utf-8')
        subprocess.run([str(RESVG),'--width',str(g['width']*8),'--height',str(g['height']*8),str(pth),str(pth.with_suffix('.png'))],check=True,capture_output=True,timeout=60)
        pred=np.asarray(Image.open(pth.with_suffix('.png')).convert('RGBA'))[...,3]>=128
        proxy8=np.repeat(np.repeat(proxy,8,axis=0),8,axis=1)
        raw8=np.repeat(np.repeat(np.isin(labels,fg),8,axis=0),8,axis=1)
        m['arabic_source_proxy']={'source_topology':mask_topology(proxy8),'raw_topology':mask_topology(raw8),'fit_topology':mask_topology(pred),
          'foreground_iou':float(np.sum(proxy8&pred)/max(1,np.sum(proxy8|pred))),'separation':separation_errors(proxy8,pred),
          'reference_limit':'Native raster threshold proxy enlarged by nearest replication. Not independent font/vector GT, cannot certify subpixel Arabic contours. No typography reconstruction.'}
    timing={}
    for kind,raw,regions in [('curves',False,False),('raw',True,False),('regions',False,True)]:
        svg=out/(name+'_'+kind+'.svg');svg.write_text(svg_graph(g,raw=raw,regions=regions),encoding='utf-8');timing[kind]=render(svg,svg.with_suffix('.png'))
    import xml.etree.ElementTree as ET
    tree=ET.fromstring((out/(name+'_curves.svg')).read_text(encoding='utf-8'));x,y,w,h=ZOOMS[case]
    for scale in [1,4,16]:
        tree.set('viewBox',f'{x} {y} {w} {h}');tree.set('width',str(w*scale));tree.set('height',str(h*scale))
        pth=out/(name+f'_detail_{scale}x.svg');pth.write_text(ET.tostring(tree,encoding='unicode'),encoding='utf-8');timing[f'detail_{scale}x']=render(pth,pth.with_suffix('.png'))
    m['render_wall_seconds']=timing
    dump(out/(name+'_metrics.json'),m)
    return m

# END CHANGE AGD-THIN-EVALUATE-STUDY | 2026-10-29T08:39:37Z | CREATED | Author: root
