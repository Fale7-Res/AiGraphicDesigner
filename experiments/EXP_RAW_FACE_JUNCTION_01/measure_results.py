# START CHANGE AGD-RAWFACE-MEASURE-RESULTS | 2026-10-29T12:39:51Z | CREATED | Author: root
"""Evaluator-only metrics and visual exports; never feeds candidate construction."""
from run_case import ROOT,OLD,WORK,destination,dump,digest
import sys,json,shutil,time,collections
import numpy as np
from PIL import Image
from shapely.geometry import LineString,Point
from shapely.strtree import STRtree
from scipy.spatial import cKDTree
import evaluate_study as inherited
from geometry_eval import chain_points,uniform_points
inherited.destination=destination

def measure():
    summary=[];cases=json.loads((ROOT/'protocol.json').read_text(encoding='utf-8'))['cases']
    for case in cases:
        out=destination(case);original=json.loads((out/'O.json').read_text(encoding='utf-8'))
        audit=json.loads((out/'R_audit.json').read_text(encoding='utf-8'));labels=np.load(out/'labels.npy',allow_pickle=False)
        junctions=[];lookup={c['id']:c for c in original['chains']}
        for row in audit['mapping']:
            if not row['splits']:continue
            refs=original['faces'][row['face']][row['original_ring']];starts=[]
            for ref in refs:
                p=lookup[ref['chain']]['pixel_crack_vertices'];starts.append(tuple(p[0] if ref['forward'] else p[-1]))
            for p,n in collections.Counter(starts).items():
                if n<2:continue
                x,y=map(int,p);block=labels[max(0,y-1):min(labels.shape[0],y+1),max(0,x-1):min(labels.shape[1],x+1)]
                junctions.append({'face':row['face'],'ring':row['original_ring'],'xy':list(p),'visits':n,'pixel_neighborhood_2x2':block.tolist(),'note':'Diagonal/pinched contact evidence, not semantic object connectivity.'})
        dump(out/'JUNCTION_DIAGNOSTICS.json',junctions)
        for name in ['O','R','B','RB']:
            if not (out/(name+'.json')).exists():continue
            shutil.copy2(out/'labels.npy',out/(name+'_labels.npy'))
            m=inherited.evaluate_candidate(case,name)
            raw_valid=sum(x['raw_valid_ring'] for x in m['rings']);fitted_valid=sum(x['fit_valid_ring'] for x in m['rings'])
            row={k:m.get(k) for k in ['case','condition','chains','cubics','invalid_raw_rings','invalid_fit_rings','raw_nonzero_fit_degenerate_rings','crossing_or_overlap_pairs','shared_reference_failures','max_junction_gap_px','near_intersection_unresolved_pairs','self_intersecting_chains','geometry_acceptance','raw_to_fit','known_geometry','arabic_source_proxy','critical_component_diagnostics','coverage','visible_microgeometry','render_wall_seconds']}
            row.update(ring_count=len(m['rings']),raw_valid_rings=raw_valid,fitted_valid_rings=fitted_valid)
            summary.append(row)
        # Probe evaluation is separate, consumes maps only after their immutable generation.
        maps=np.load(out/'source_probe/source_evidence.npz',allow_pickle=False);edge=maps['persistent_edges'];ys,xs=np.nonzero(edge);points=np.c_[xs+.5,ys+.5]
        lines=[LineString(chain_points(c,True)) for c in original['chains']];tree=STRtree(lines)
        distances=np.array([Point(p).distance(lines[int(tree.nearest(Point(p)))]) for p in points])
        absent=np.zeros(edge.shape,bool)
        if len(distances):absent[ys[distances>2],xs[distances>2]]=True
        np.save(out/'source_probe/edge_evidence_farther_than_2px.npy',absent)
        rgb=np.asarray(Image.open(out/'working.png').convert('RGB'));overlay=rgb.copy();overlay[edge]=(0,180,255);overlay[absent]=(255,0,180);Image.fromarray(overlay).save(out/'source_probe/evidence_vs_raw_overlay.png')
        md=json.loads((out/'source_probe/source_evidence.json').read_text(encoding='utf-8'))
        dump(out/'source_probe/EVALUATION_ONLY.json',{'persistent_edge_pixels':int(edge.sum()),'persistent_edge_fraction':md['persistent_edge_fraction'],'farther_than_2px_from_raw_cracks':int(absent.sum()),'fraction_of_evidence_farther_than_2px':float(absent.sum()/max(1,edge.sum())),'coordinate_convention':'Raster element[y,x] at geometric(x+.5,y+.5); raw pixel cracks use integer corners. Distance to complete raw line segments using Shapely doubles.','clutter_warning':md['clutter_warning'],'interpretation':'Unrepresented source contrast, not verified missing structural geometry. Texture, AA, illumination and noise can contribute. No discovered region, stroke or component claim.'})
        dump(ROOT/'reports/SUMMARY.json',summary)
        print(case,'measured',flush=True)

if __name__=='__main__':measure()

# END CHANGE AGD-RAWFACE-MEASURE-RESULTS | 2026-10-29T12:39:51Z | CREATED | Author: root
