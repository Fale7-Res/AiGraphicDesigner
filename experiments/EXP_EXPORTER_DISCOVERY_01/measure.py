# START CHANGE AGD-EXPORT-MEASURE | 2026-10-29T22:12:25Z | CREATED | Author: root
"""Corrected-export evaluation and unintegrated stroke proposal diagnostics."""
from phase_b import ROOT,WORK,PREVIOUS,THIN,destination,dump,digest,render_size
from pathlib import Path
import sys,json,shutil,collections,copy
import numpy as np
from PIL import Image
from scipy import ndimage
from scipy.spatial import cKDTree
from shapely.geometry import LineString
from shapely.strtree import STRtree
import geometry_eval,validate_geometry,final_diagnostics,evaluate_study
from svg_exporter import svg_graph
from xml.etree import ElementTree as ET
from geometry_eval import uniform_points,chain_points,compare_samples
# Patch in-memory bindings only. No historical source or saved output changes.
for module in [geometry_eval,validate_geometry,final_diagnostics,evaluate_study]:module.svg_graph=svg_graph
evaluate_study.destination=destination

def mask_metrics(truth,pred):
    inter=np.sum(truth&pred);union=np.sum(truth|pred)
    from skimage.morphology import skeletonize
    sk=skeletonize(truth);tw=ndimage.distance_transform_edt(truth)[sk]*2/8;pw=ndimage.distance_transform_edt(pred)[sk]*2/8
    return {'iou':float(inter/max(1,union)),'recall':float(inter/max(1,np.sum(truth))),'precision':float(inter/max(1,np.sum(pred))),'truth_topology':validate_geometry.mask_topology(truth),'pred_topology':validate_geometry.mask_topology(pred),'separation':evaluate_study.separation_errors(truth,pred),'reference_width_mae_px':float(np.mean(abs(tw-pw))) if len(tw) else None,'boundary':compare_samples(validate_geometry.mask_boundary(truth),validate_geometry.mask_boundary(pred)) if truth.any() and pred.any() else {'status':'EMPTY_MASK_NOT_EVALUABLE'}}

def proposal_samples(proposal):
    curves=np.asarray(proposal['curves']);t=np.linspace(0,1,65)[:,None];samples=[]
    for a,b,c,d in curves:samples.append((1-t)**3*a+3*(1-t)**2*t*b+3*(1-t)*t*t*c+t**3*d)
    return np.concatenate(samples)

def evaluate_discovery(case):
    out=destination(case);folder=out/'discovery';audit=json.loads((folder/'proposals.json').read_text());g=json.loads((out/'O.json').read_text());w,h=g['width'],g['height']
    original=ET.parse(folder/'proposals.svg').getroot();render_size(folder/'proposals.svg',folder/'proposals_native.png',w,h);render_size(folder/'proposals.svg',folder/'proposals_8x.png',w,h,8)
    rendered=np.asarray(Image.open(folder/'proposals_8x.png').convert('RGBA'))[...,3]>=128
    lines=[LineString(proposal_samples(p)) for p in audit['accepted']];cross=[];selfbad=[];near=[]
    for i,line in enumerate(lines):
        if not line.is_simple:selfbad.append(i)
        for j in range(i):
            if line.crosses(lines[j]) or line.overlaps(lines[j]):cross.append([i,j])
            elif line.distance(lines[j])<.02:near.append([i,j])
    baseline_lines=[LineString(chain_points(c)) for c in g['chains']];tree=STRtree(baseline_lines);baseline_cross=0
    for line in lines:
        for j in tree.query(line):
            if line.crosses(baseline_lines[int(j)]):baseline_cross+=1
    records=[];allpts=[]
    for p,line in zip(audit['accepted'],lines):
        pts=proposal_samples(p);allpts.append(pts);span=np.ptp(pts,axis=0)
        distances=[line.distance(baseline_lines[int(tree.nearest(line))])]
        records.append({'chain_id':p['chain_id'],'length_px':p['length_px'],'width_px':p['width_px'],'cubics':len(p['curves']),'span_px':span.tolist(),'bbox_within2px':bool(max(span)<=2),'half_integer_sample_fraction':float(np.mean(np.min(abs(pts*2-np.round(pts*2)),axis=1)<.02)),'source_confidence_heuristic':p['source_confidence'],'fit_sampled_deviation_px':p['sampled_symmetric_deviation_px']})
    m={'case':case,'accepted_proposals':len(audit['accepted']),'rejected_proposals':len(audit['rejected']),'rejections':dict(collections.Counter(x['reason'] for x in audit['rejected'])),'source_support_pixels':audit['source_support_pixels'],'skeleton_pixels':audit['skeleton_pixels'],'source_junction_count':audit['junction_count'],'cubics':sum(len(p['curves']) for p in audit['accepted']),'proposals':records,'centerline_self_intersections':selfbad,'centerline_cross_or_overlap_pairs':cross,'unresolved_near_or_touch_pairs':near,'crossings_with_inherited_boundaries':baseline_cross,'integration':'UNINTEGRATED_STROKE_PROPOSALS; crossings may be intentional or incompatible; no regionownership/junction certification','geometry_gate':'NOT_ACCEPTED','svg_bytes':(folder/'proposals.svg').stat().st_size,'rendered_8x_covered_area_px2':float(rendered.sum()/64),'anti_mosaic':'Continuouscubicstrokes,minlength6,width<=6; no newlabelcells,rectanglesorunderlay. Half-lattice starts/source skeleton are not subpixel localization.'}
    # Actual diagnostic SVG union preserves proposals as independent stroke objects.
    if case in ['fine_features','K01_linear_corner_hole','G06_arabic']:
        baseline=out/('O_arabic_foreground.svg' if case=='G06_arabic' else 'O_foreground.svg')
        tree_union=ET.parse(baseline).getroot()
        for element in original:tree_union.append(copy.deepcopy(element))
        union=folder/'hypothetical_union.svg';union.write_text(ET.tostring(tree_union,encoding='unicode'),encoding='utf-8');render_size(union,union.with_suffix('.png'),w,h,8)
        u=np.asarray(Image.open(union.with_suffix('.png')).convert('RGBA'))[...,3]>=128
        if case=='G06_arabic':
            rgb=np.asarray(Image.open(out/'working.png').convert('RGB')).astype(float);truth=np.repeat(np.repeat(np.linalg.norm(rgb-rgb[0,0],axis=-1)>8,8,axis=0),8,axis=1);m['reference']='SOURCE_THRESHOLD_PROXY_NOT_GLYPH_TRUTH'
        else:
            refs=json.loads((PREVIOUS/'references/known_control_reference_manifest.json').read_text())['references'];ref=next(x for x in refs if x['id']==case);assert digest(ref['local_only_mask_path'])==ref['mask_sha256'];truth=np.asarray(Image.open(ref['local_only_mask_path']).convert('L'))>=128;m['reference']='INDEPENDENT_KNOWN_VECTOR_8X_SAMPLED_MASK'
        m['proposal_only']=mask_metrics(truth,rendered);m['hypothetical_union']=mask_metrics(truth,u);m['hypothetical_union_limit']='ActualSVGpaintunion, not safelyintegratedsharedregiongraph; maycoverholes/overlapwrongobjects.'
        for item in ['proposal_only','hypothetical_union']:
            p=rendered if item=='proposal_only' else u;Image.fromarray(np.stack([truth*255,p*255,np.zeros_like(p)],axis=-1).astype(np.uint8)).save(folder/(item+'_error.png'))
    if case=='A01_shield':
        ref=json.loads((PREVIOUS/'references/shield_complete_boundary_reference.json').read_text());pts=np.concatenate(allpts) if allpts else np.empty((0,2));m['critical_guide_stroke_support']=[]
        for c in ref['components']:
            q=np.concatenate([uniform_points(p) for p in c['polylines']]);dist=cKDTree(pts).query(q)[0] if len(pts) else np.full(len(q),np.inf)
            m['critical_guide_stroke_support'].append({'id':c['id'],'centerline_support_within_uncertainty_band':float(np.mean(dist<=c['uncertainty_px'])),'uncertainty_px':c['uncertainty_px'],'limit':'Stroke centerlineproximity, notcorrectrecoveredregionboundary/physicalstructure.'})
    dump(folder/'METRICS.json',m);return m

def run():
    rows=[];discoveries=[];inputs=json.loads((ROOT/'BASELINE_PINS.json').read_text())['cases']
    for case,items in inputs.items():
        out=destination(case)
        for n in ['O','R','B','A','RB']:
            if not (out/(n+'.json')).exists():continue
            if n!='A':shutil.copy2(out/'labels.npy',out/(n+'_labels.npy'))
            m=evaluate_study.evaluate_candidate(case,n);old=json.loads(Path(items.get(n+'_metrics.json',items['B_metrics.json'])['path']).read_text()) if n!='RB' else None
            r={k:m.get(k) for k in ['case','condition','chains','cubics','invalid_raw_rings','invalid_fit_rings','raw_nonzero_fit_degenerate_rings','shared_reference_failures','max_junction_gap_px','crossing_or_overlap_pairs','self_intersecting_chains','near_intersection_unresolved_pairs','coverage','known_geometry','arabic_source_proxy','critical_component_diagnostics','visible_microgeometry','render_wall_seconds']};r['ring_count']=len(m['rings'])
            if old:r['historical_affected_metrics']={'known_geometry':old.get('known_geometry'),'arabic_source_proxy':old.get('arabic_source_proxy'),'visible_microgeometry':old.get('visible_microgeometry'),'status':'PRESERVED_IN_ORIGINAL_FOLDER; fittedcompoundexport-derivedvaluespotentiallyaffected. Correctedvalueshereonly.'}
            rows.append(r)
        discoveries.append(evaluate_discovery(case));dump(ROOT/'reports/SUMMARY.json',rows);dump(ROOT/'reports/DISCOVERY_SUMMARY.json',discoveries);print(case,'measured',flush=True)

if __name__=='__main__':run()

# END CHANGE AGD-EXPORT-MEASURE | 2026-10-29T22:12:25Z | CREATED | Author: root
