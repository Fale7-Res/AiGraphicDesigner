# START CHANGE AGD-ISOLATION-ANALYZE-MATRIX | 2026-10-29T06:48:34Z | CREATED | Author: root
"""Frozen candidate analysis and SVG evidence; evaluator-only references here."""
import os,sys,json,time,subprocess,hashlib,html
from pathlib import Path
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1';os.environ['PYTHONDONTWRITEBYTECODE']='1'
from isolation import ROOT,WORK,CASES,case_dir,dump,digest
sys.path.insert(0,str(WORK/'geometry-deps'))
import numpy as np
from PIL import Image
from geometry_eval import evaluate,svg_graph
RESVG=WORK/'resvg/resvg.exe'
ZOOMS={'A01_shield':[118,65,136,100],'G07_tux':[60,40,90,90],'G06_arabic':[50,45,85,70],
 'G05_chelsea_nativecrop':[45,35,80,70],'fine_features':[20,20,65,65],'K01_linear_corner_hole':[20,20,70,65]}

def render(svg,png):
    t=time.monotonic();p=subprocess.run([str(RESVG),str(svg),str(png)],capture_output=True,timeout=60)
    if p.returncode:raise RuntimeError(p.stderr.decode(errors='replace'))
    return time.monotonic()-t

def edge_dictionary(g):
    edges={}
    for ch in g['chains']:
        pair=tuple(sorted(ch['adjacent_face_labels']))
        pts=ch['pixel_crack_vertices']
        for a,b in zip(pts,pts[1:]):
            key=tuple(sorted((tuple(a),tuple(b))))
            if key in edges:raise ValueError('Duplicate raw crack')
            edges[key]=pair
    return edges

def region_center_check(svg,labels,target):
    # Native raw polygon SVG covers exactly pixel squares: color at centers must
    # equal deterministic label paint; no antialias boundary samples are used.
    render(svg,target);rgb=np.asarray(Image.open(target).convert('RGB'))
    expected=np.stack([labels*97%200+30,labels*57%200+30,labels*137%200+30],axis=-1).astype(np.uint8)
    wrong=np.any(rgb!=expected,axis=-1)
    return {'pixels_wrong_region_id_color':int(wrong.sum()),'pixels':int(wrong.size)}

def analyze():
    ref=json.loads((ROOT/'references/shield_complete_boundary_reference.json').read_text())
    freeze=json.loads((ROOT/'references/FREEZE.json').read_text())
    for path,data in freeze['files'].items():assert digest(ROOT/'references'/path)==data['sha256']
    rows=[];integrity=[]
    for case in CASES:
        out=case_dir(case);w,h=Image.open(out/'working.png').size
        for seg in ['S_A','S_V']:
            labels=np.load(out/(seg+'.npy'),allow_pickle=False)
            a=json.loads((out/(seg+'_F_A.json')).read_text());v=json.loads((out/(seg+'_F_V.json')).read_text())
            assert a['labels_sha256']==v['labels_sha256']==digest(out/(seg+'.npy'))
            ea=edge_dictionary(a);ev=edge_dictionary(v)
            match=ea==ev
            checks={}
            for init,g in [('F_A',a),('F_V',v)]:
                rawsvg=out/(seg+'_'+init+'_raw_regions.svg');rawsvg.write_text(svg_graph(g,raw=True,regions=True),encoding='utf-8')
                checks[init]=region_center_check(rawsvg,labels,out/(seg+'_'+init+'_raw_regions.png'))
            integrity.append({'case':case,'segmentation':seg,'labels_sha256':digest(out/(seg+'.npy')),
                'exact_raw_unit_edge_and_adjacency_match':match,'raw_region_fill_checks':checks,
                'raw_edges_A':len(ea),'raw_edges_V':len(ev),'graph_equivalence':match and all(x['pixels_wrong_region_id_color']==0 for x in checks.values())})
            rgb=np.stack([labels*97%200+30,labels*57%200+30,labels*137%200+30],axis=-1).astype(np.uint8)
            Image.fromarray(rgb).save(out/(seg+'_labels.png'))
            for init,g in [('F_A',a),('F_V',v)]:
                name=seg+'_'+init;start=time.monotonic()
                metrics=evaluate(g,ref if case=='A01_shield' else None)
                metrics['analysis_wall_seconds']=time.monotonic()-start
                metrics['case']=case;metrics['condition']=name
                metrics['candidate_sha256']=digest(out/(name+'.json'))
                metrics['regions']=int(np.unique(labels).size)
                metrics['raw_graph_equivalence']=integrity[-1]['graph_equivalence']
                renders={}
                for suffix,raw,regions in [('curves',False,False),('raw',True,False),('regions',False,True)]:
                    svg=out/(name+'_'+suffix+'.svg');svg.write_text(svg_graph(g,raw=raw,regions=regions),encoding='utf-8')
                    renders[suffix]=render(svg,out/(name+'_'+suffix+'.png'))
                # True vector viewport renders, never enlarged PNG evidence.
                import xml.etree.ElementTree as ET
                tree=ET.fromstring((out/(name+'_curves.svg')).read_text())
                x,y,cw,ch=ZOOMS[case];cw=min(cw,w-x);ch=min(ch,h-y)
                for scale in [1,4,16]:
                    tree.set('viewBox',f'{x} {y} {cw} {ch}');tree.set('width',str(cw*scale));tree.set('height',str(ch*scale))
                    path=out/(name+f'_detail_{scale}x.svg');path.write_text(ET.tostring(tree,encoding='unicode'),encoding='utf-8')
                    renders[f'detail_{scale}x']=render(path,path.with_suffix('.png'))
                metrics['render_wall_seconds']=renders
                dump(out/(name+'_metrics.json'),metrics)
                brief={k:metrics[k] for k in ['case','condition','regions','chains','cubics','raw_nonzero_fit_degenerate_rings','invalid_fit_rings','invalid_raw_rings','max_junction_gap_px','shared_reference_failures','self_intersecting_chains','crossing_or_overlap_pairs','unexpected_endpoint_interior_touches','near_intersection_unresolved_pairs','ring_area_weighted_tiny_lattice_fraction','geometry_acceptance','raw_graph_equivalence','raw_to_fit']}
                rows.append(brief);dump(ROOT/'reports/metrics_summary.json',rows);dump(ROOT/'reports/graph_integrity.json',integrity)
                print(json.dumps(brief),flush=True)
    return rows

if __name__=='__main__':analyze()

# END CHANGE AGD-ISOLATION-ANALYZE-MATRIX | 2026-10-29T06:48:34Z | CREATED | Author: root
