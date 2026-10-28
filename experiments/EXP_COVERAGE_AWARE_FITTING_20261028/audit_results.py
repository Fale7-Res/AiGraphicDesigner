"""Read saved evidence independently of fitting; export aggregate metrics and integrity."""
# START CHANGE AGD-COVERAGE-AUDIT | 2026-10-28T05:23:52Z | CREATED | Author: root
from pathlib import Path
import csv,json,xml.etree.ElementTree as ET
import numpy as np
from PIL import Image
import research as r

def audit():
    manifest=json.loads((r.ROOT/'inputs/manifest.json').read_text());rows=[];checks=[];paint_recovery=[];local=[]
    for c in manifest['cases']:
        folder=r.ROOT/'results'/c['id'];data=json.loads((folder/'result.json').read_text())
        for key,digest in c['hashes'].items():assert r.sha(c[key])==digest,(c['id'],key)
        assert r.sha(folder/'source.png')==c['hashes']['source']
        assert r.sha(folder/'coverage/maps.npz')==data['map_metadata']['maps_npz_sha256']
        signatures=set()
        for k,v in data['conditions'].items():
            svg=folder/k/'output.svg';assert r.sha(svg)==v['sha256']
            if k in ['Aflat','Agrad','B','C']:signatures.add(r.new._shape_signature(ET.parse(svg).getroot()))
            with np.load(folder/'coverage/maps.npz') as maps:
                actual,err,band=r.evaluate_extra(folder/'source.png',folder/k/'render.png',maps,folder/'Aflat/render.png')
            assert abs(actual['float_three_background_mse']-v['float_three_background_mse'])<1e-9
            assert abs(actual['heldout_float_three_background_mse']-v['heldout_float_three_background_mse'])<1e-9
            for bg in ['white','black','bluegray']:
                source=Image.open(folder/'source.png').convert('RGBA');rgba=Image.open(folder/k/'render.png').convert('RGBA')
                color={'white':(255,255,255),'black':(0,0,0),'bluegray':(40,80,120)}[bg]
                a=np.asarray(Image.alpha_composite(Image.new('RGBA',source.size,(*color,255)),source).convert('RGB'),dtype=float)
                b=np.asarray(Image.alpha_composite(Image.new('RGBA',source.size,(*color,255)),rgba).convert('RGB'),dtype=float)
                assert abs(float(((a-b)**2).mean())-v['metrics'][bg]['mse'])<1e-8
            row={'case':c['id'],'kind':c['kind'],'condition':k,'ssim_white':v['metrics']['white']['ssim'],'psnr_white':v['metrics']['white']['psnr_db'],
                'mse_3bg':v['float_three_background_mse'],'heldout_mse_3bg':v['heldout_float_three_background_mse'],'boundary_mse_3bg':v['boundary_float_three_background_mse'],
                'interior_mse_3bg':v['interior_float_three_background_mse'],'mse_white':v['float_per_background_mse']['white'],'mse_black':v['float_per_background_mse']['black'],'mse_bluegray':v['float_per_background_mse']['bluegray'],
                'alpha_mse':v['alpha_mse'],'alpha_change_from_Aflat_max_bytes':v['fixed_baseline_alpha_max_change_bytes'],'premult_rgb_rmse':v['premultiplied_rgb_rmse'],
                'worst_tile_white_rmse':v['metrics']['white']['worst_32px_tile_rmse'],'paths':v['geometry']['rgb_paths'],'tiny_bbox_le2':v['geometry']['rgb_paths_bounds_le_2px'],
                'cubic_segments':v['geometry']['cubic_segments'],'lattice_fraction':v['geometry']['coordinate_integer_lattice_fraction'],'bytes':v['structure']['bytes'],'render_seconds':v['render']['render_seconds']}
            rows.append(row)
            if c['kind']=='new_oracle' and k in ['Aflat','Agrad','B','C']:
                with np.load(folder/'coverage/maps.npz') as maps:
                    weights=maps['weights'];height=int(maps['height']);width=int(maps['width'])
                yy,xx=np.indices((height,width));xy=np.column_stack((xx.ravel()+.5,yy.ravel()+.5))
                models=r.new._models(ET.parse(svg).getroot(),r.old_fit())
                for i,t in enumerate(c['fixture']['truth_regions']):
                    if t['fill'].startswith('url('):continue
                    support=np.flatnonzero(weights[i]>1e-8);weight=weights[i,support]**2
                    expected=r.new._color(t['fill']);estimated=r.old_fit()._predict(models[i],xy[support])
                    e=((estimated-expected)**2).mean(axis=1)
                    paint_recovery.append({'case':c['id'],'condition':k,'region':t['id'],'true_flat_paint_effective_weighted_rmse':float(np.sqrt(np.average(e,weights=weight))),
                        'interpretation':'Known flat region paint bias/bleeding diagnostic; not an attribution of all rendered boundary error to adjacent color leakage.'})
                boxes=dict(c['fixture']['critical_features'])
                for thin in c['fixture']['thin_regions']:boxes[thin['id']]=thin['critical_box']
                for name,(x,y,w,h) in boxes.items():local.append({'case':c['id'],'condition':k,'region':name,'box':[x,y,w,h],'actual_three_background_local_mse':float(err[y:y+h,x:x+w].mean())})
        assert len(signatures)==1
        f=json.loads((folder/'fitting.json').read_text());resources=json.loads((r.ROOT/'reports'/f'{c["id"]}_resources.json').read_text())
        assert resources['returncode']==0 and resources['termination_reason'] is None
        checks.append({'id':c['id'],'fixed_scene_signature':next(iter(signatures)),'fitting_seconds':f['wall_seconds'],'deadline_reached':f['deadline_reached'],
            'sampled_tree_peak_mib':resources['sampled_tree_peak_mib'],'worker_seconds':resources['wall_seconds'],'map_seconds':data['map_metadata']['wall_seconds'],
            'unobservable_regions':len(data['map_metadata']['unobservable_regions']),'gram_rank':data['map_metadata']['gram_rank_threshold_1e9'],'gram_condition':data['map_metadata']['positive_gram_condition_ratio'],
            'random_operator_rmse':data['map_metadata']['random_forward_rmse_bytes'],'final_operator_rmse':f['forward_model_validation'],
            'gradient_empty_split_events':sum(v.get('reason')=='unobservable_or_split_empty' for v in f['regions']),
            'oracle_flat_color_errors':data['oracle_flat_color_errors']})
    svg_count=png_count=0
    for path in r.ROOT.rglob('*.svg'):
        root=ET.parse(path).getroot();assert all(n.tag.rsplit('}',1)[-1] not in ['image','foreignObject','script'] for n in root.iter()),path
        assert 'data:image' not in path.read_text();svg_count+=1
    for path in r.ROOT.rglob('*.png'):Image.open(path).verify();png_count+=1
    with (r.ROOT/'reports/metrics.csv').open('w',newline='',encoding='utf-8') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    r.save(r.ROOT/'reports/metrics.json',rows)
    r.save(r.ROOT/'reports/paint_recovery.json',paint_recovery)
    r.save(r.ROOT/'reports/critical_feature_errors.json',local)
    r.save(r.ROOT/'reports/integrity.json',{'status':'PASS','cases':checks,'svg_files_checked':svg_count,'png_files_checked':png_count,
        'checks':['Frozen source/baseline hashes','All final SVG hashes','NPZ hashes','Fixed scene/mask signatures','Independent recomputation actual3bg/heldout/native quantized MSE','All SVG XML/no raster/script/foreignObject','All PNG decode','All bounded workers success'],
        'limits':'No claim of arbitrary SVG topology correctness or absence of self intersections. PNG content hashes supplied in final publication inventory.'})
    print('PASS',len(checks),'cases',svg_count,'SVG',png_count,'PNG')
if __name__=='__main__':audit()
# END CHANGE AGD-COVERAGE-AUDIT | 2026-10-28T05:23:52Z | CREATED | Author: root
