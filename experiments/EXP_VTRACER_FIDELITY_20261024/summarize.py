# START CHANGE VTRACER-FOLLOWUP-SUMMARY | 2026-10-25T04:45:28Z | EDITED | Author: vtracer_sources
"""Reproducible twelve-image evidence tables and native-render comparisons."""
# START CHANGE VTRACER-SUMMARY | 2026-10-24T23:42:36Z | CREATED | Author: vtracer_sources
from pathlib import Path
import argparse,csv,json,sys,shutil
import numpy as np
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'src'))
from evaluate import load_rgb
from search import fidelity_score


def local_errors(source,prediction,centers=None):
    """Fixed 4x4 tile RGB errors plus independent historical seed-center disks."""
    residual=source.astype(float)-prediction.astype(float);h,w=source.shape[:2]
    tiles=[]
    for y in range(4):
        for x in range(4):
            y0,y1=y*h//4,(y+1)*h//4;x0,x1=x*w//4,(x+1)*w//4
            tiles.append({'bbox':[x0,y0,x1,y1],'rmse':float(np.sqrt(np.mean(residual[y0:y1,x0:x1]**2)))})
    result={'tiles':tiles,'tile_rmse_worst':max(t['rmse'] for t in tiles),'tile_rmse_median':float(np.median([t['rmse'] for t in tiles]))}
    if centers:
        yy,xx=np.indices((h,w));mask=np.zeros((h,w),bool)
        for x,y in centers:mask|=(xx+.5-x)**2+(yy+.5-y)**2<=2.5**2
        result['seed_center_rmse']=float(np.sqrt(np.mean(residual[mask]**2)));result['seed_center_pixels']=int(mask.sum())
    return result


def comparison_images(source,panels,destination,case):
    """Preserve full native panels and fixed post-hoc visual crops at 100/200/400%."""
    destination.mkdir(parents=True,exist_ok=True);h,w=source.shape[:2]
    boxes={'full':[0,0,w,h],'center':[w//4,h//4,3*w//4,3*h//4]}
    if case.startswith('A03'):boxes['sesame']=[135,25,min(w,255),min(h,85)]
    if case.startswith('A09'):boxes['lettering']=[w//8,h//8,7*w//8,7*h//8]
    if case.startswith('A10'):boxes['lettering']=[w//8,int(h*.40),7*w//8,int(h*.95)]
    for crop,box in boxes.items():
        for scale in ([1] if crop=='full' else [1,2,4]):
            tw,th=(box[2]-box[0])*scale,(box[3]-box[1])*scale
            sheet=Image.new('RGB',(tw*len(panels),th+26),'white');draw=ImageDraw.Draw(sheet)
            for i,(name,pred) in enumerate(panels.items()):
                patch=Image.fromarray(pred).crop(box).resize((tw,th),Image.Resampling.NEAREST)
                sheet.paste(patch,(i*tw,26));draw.text((i*tw+3,7),name,fill='black')
            sheet.save(destination/f'{crop}_{scale*100}.png')
    (destination/'crops.json').write_text(json.dumps({'boxes':boxes,'note':'Fixed visual crops selected by image category, not pixel labels or semantic GT. Enlarged PNGs use nearest-neighbor source-resolution renders, not highresolution truth.'},indent=2))


def collect(root,output):
    """Require all twelve searches and eight frozen holdouts before writing summaries."""
    protocol=json.loads((root/'protocol.json').read_text());inputs=sorted((root/'inputs').glob('*.png'))
    if len(inputs)!=12:raise ValueError('Expected 12 source PNGs')
    base=json.loads((root/'results_baselines/summary.json').read_text())
    if len(base)!=37:raise ValueError('Expected all37 historical baseline renders')
    for p in inputs:
        if not (root/'results'/p.stem/'ranking.json').exists():raise ValueError('Incomplete search: '+p.stem)
        if p.stem[:3] in protocol['holdout'] and not (root/'holdout_common'/p.stem/'ranking.json').exists():raise ValueError('Incomplete frozen holdout: '+p.stem)
    if any('highpass_rmse_sigma1' not in b['metrics'] for b in base):raise ValueError('Baselines must use common sigma1 highpass metric')
    output.mkdir(parents=True,exist_ok=True);(output/'reports').mkdir(exist_ok=True)
    seed=json.loads((root/'annotations/seeds_reference.json').read_text())['confirmed_centers'];rows=[];summary={'cases':{},'protocol':protocol,'frozen_common':json.loads((root/'frozen_common.json').read_text()),'limitations':['All best rows are source-image-tuned; frozen common was selected on four development images only.','Score is a fixed numerical ranking, not universal perceptual quality.','Seed centers cover20clear seeds only; no complete detectionfalsepositive rate.','Tile errors are spatial diagnostics, not semantic region accuracy.']}
    for p in inputs:
        name=p.stem;source=load_rgb(p);rank=json.loads((root/'results'/name/'ranking.json').read_text());successful=rank['ranked'];best=successful[0];owner=next(r for r in successful if r['trial']=='trial_00');spline=max((r for r in successful if r['config']['mode']=='spline'),key=lambda r:r['score'])
        selected={'owner':owner,'best_spline':spline,'best':best};render_paths={k:root/'results'/name/v['trial']/'render.png' for k,v in selected.items()}
        historical=[r for r in base if r['case']==name]
        for label in ['original','repair']:
            selected[label]=next(r for r in historical if r['label']==label);render_paths[label]=root/'results_baselines'/name/label/'render.png'
        recent=[r for r in historical if r['label'] not in ['original','repair']]
        if recent:
            chosen=max(recent,key=lambda r:fidelity_score(r['metrics']));selected['best_recent']=chosen;render_paths['best_recent']=root/'results_baselines'/name/chosen['label']/'render.png'
        if name[:3] in protocol['holdout']:
            common=json.loads((root/'holdout_common'/name/'ranking.json').read_text())['ranked'][0];selected['frozen_common']=common;render_paths['frozen_common']=root/'holdout_common'/name/common['trial']/'render.png'
        else:
            config=summary['frozen_common']['config'];common=next(r for r in successful if r['config']==config);selected['frozen_common']=common;render_paths['frozen_common']=root/'results'/name/common['trial']/'render.png'
        case={'conditions':{},'successful_trials':len(successful),'failed_trials':rank['failed'],'total_search_wall_seconds':sum(v.get('isolated_process_wall_seconds',0) for v in successful+rank['failed'])};panels={'Original':source}
        for label,record in selected.items():
            pred=load_rgb(render_paths[label]);local=local_errors(source,pred,seed if name.startswith('A03') else None);st=record['structure'];metric=record['metrics'];cond={'metrics':metric,'structure':st,'local':local,'score':record.get('score',fidelity_score(metric)),'trial':record.get('trial'),'config':record.get('config'),'historical_label':record.get('label'),'performance':record.get('performance',record.get('resources',{}))}
            case['conditions'][label]=cond
            row={'case':name,'split':'development' if name[:3] in protocol['development'] else 'holdout','condition':label,'trial':record.get('trial',''),'historical_label':record.get('label',''),'score':cond['score'],**metric,'paths':st['elements'].get('path',0),'rectangles':st['elements'].get('rect',0),'path_commands':sum(st['path_commands'].values()),'cubic_segments':st['cubic_segments'],'explicit_coordinate_pairs_excluding_HV':st['explicit_path_coordinate_pairs'],'svg_bytes':st['bytes'],'tile_rmse_worst':local['tile_rmse_worst'],'tile_rmse_median':local['tile_rmse_median'],'seed_center_rmse':local.get('seed_center_rmse')};rows.append(row)
            if label in ['owner','best_spline','best','original','repair']:panels[{'owner':'Owner preset','best_spline':'Best spline','best':'Best ranked','original':'Original V04','repair':'Repaired V04'}[label]]=pred
        comparison_images(source,panels,output/'comparisons'/name,name);summary['cases'][name]=case
    means={}
    for label in ['owner','best_spline','best','original','repair','frozen_common']:
        selected=[r for r in rows if r['condition']==label]
        means[label]={key:float(np.mean([r[key] for r in selected])) for key in ['ssim','psnr_db','edge_f1_1_5px','delta_e76_mean','highpass_rmse_sigma1','tile_rmse_worst','svg_bytes','path_commands']}
    summary['all12_means']=means
    summary['holdout8_means']={label:{key:float(np.mean([r[key] for r in rows if r['condition']==label and r['split']=='holdout'])) for key in ['ssim','psnr_db','edge_f1_1_5px','delta_e76_mean','highpass_rmse_sigma1']} for label in ['frozen_common','best','best_spline','original','repair']}
    summary['acceptance_numeric']={label:{'all12_ssim_ge_.95':all(c['conditions'][label]['metrics']['ssim']>=.95 for c in summary['cases'].values()),'mean_ssim_ge_.97':means[label]['ssim']>=.97,'all12_psnr_ge30':all(c['conditions'][label]['metrics']['psnr_db']>=30 for c in summary['cases'].values()),'all12_edge_ge_.9':all(c['conditions'][label]['metrics']['edge_f1_1_5px']>=.9 for c in summary['cases'].values()),'all12_deltaE_le3':all(c['conditions'][label]['metrics']['delta_e76_mean']<=3 for c in summary['cases'].values()),'visual_acceptance':'requires separate human review; numeric gates are not sufficient'} for label in ['best','best_spline','frozen_common']}
    (output/'summary.json').write_text(json.dumps(summary,indent=2));fields=list(rows[0])
    with (output/'reports/metrics.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
    (output/'reports/RESULTS.md').write_text(report(summary));return summary



def finalize_followup(root,output,summary):
    """Select final numerical candidates while preserving separate primary/extension evidence."""
    freeze_path=root/'extension/freeze.json'
    if not freeze_path.exists():raise ValueError('Follow-up freeze is missing')
    freeze=json.loads(freeze_path.read_text());holdout=summary['protocol']['holdout']
    expected=[p.stem for p in (root/'inputs').glob('*.png') if p.stem[:3] in holdout]
    if freeze['advance_to_holdout'] and any(not (root/'extension'/case/'frozen/result.json').exists() for case in expected):raise ValueError('Follow-up frozen holdout is incomplete')
    final={'selection':'Highest fixed fidelity score across actually evaluated primary, bounded post-hoc extension and fixed-geometry refit candidates. This is per-image selection, not generalization. Parent visual review remains separate.','extension_freeze':freeze,'cases':{},'extension_holdout':{}}
    dest=output/'best_outputs';dest.mkdir(parents=True,exist_ok=True)
    seed=json.loads((root/'annotations/seeds_reference.json').read_text())['confirmed_centers']
    for case,primary in summary['cases'].items():
        source=load_rgb(root/'inputs'/f'{case}.png');ranking=json.loads((root/'results'/case/'ranking.json').read_text());candidates=[]
        for row in ranking['ranked']:
            directory=root/'results'/case/row['trial'];candidates.append({'origin':'primary','source_svg':str((directory/'output.svg').relative_to(root)),'source_png':str((directory/'render.png').relative_to(root)),**row})
        for path in sorted((root/'extension'/case).glob('*/result.json')):
            row=json.loads(path.read_text())
            if row.get('status')=='ok':candidates.append({'origin':'posthoc_extension','source_svg':str((path.parent/'output.svg').relative_to(root)),'source_png':str((path.parent/'render.png').relative_to(root)),**row})
            if path.parent.name=='frozen':final['extension_holdout'][case]=row
        refit=root/'refinement'/case/'results.json'
        if refit.exists():
            data=json.loads(refit.read_text())
            for label,row in data['conditions'].items():
                candidates.append({'origin':'fixed_geometry_refit_'+label,'source_svg':str((refit.parent/f'{label}.svg').relative_to(root)),'source_png':str((refit.parent/f'{label}.png').relative_to(root)),'config':data['config'],**row})
        best=max(candidates,key=lambda r:r['score']);pred=load_rgb(root/best['source_png']);best['local']=local_errors(source,pred,seed if case.startswith('A03') else None)
        best['evaluated_candidate_count']=len(candidates);best['all_candidate_scores']=[{k:v for k,v in c.items() if k in ['origin','score','source_svg','source_png','config','trial']} for c in candidates];final['cases'][case]=best
        shutil.copyfile(root/best['source_svg'],dest/f'{case}.svg');shutil.copyfile(root/best['source_png'],dest/f'{case}.png')
        (dest/f'{case}.json').write_text(json.dumps(best,indent=2))
        panels={'Original':source,'Owner preset':load_rgb(root/'results'/case/'trial_00/render.png'),'Final selected':pred,'Original V04':load_rgb(root/'results_baselines'/case/'original/render.png'),'Repaired V04':load_rgb(root/'results_baselines'/case/'repair/render.png')}
        comparison_images(source,panels,output/'comparisons_final'/case,case)
    keys=['ssim','psnr_db','edge_f1_1_5px','delta_e76_mean','highpass_rmse_sigma1']
    final['all12_mean_metrics']={key:float(np.mean([v['metrics'][key] for v in final['cases'].values()])) for key in keys}
    final['extension_holdout8_mean_metrics']={key:float(np.mean([v['metrics'][key] for v in final['extension_holdout'].values()])) for key in keys}
    (output/'finalists.json').write_text(json.dumps(final,indent=2))
    lines=['\n## Separate bounded follow-up and final deliverables\n','The primary and frozen-common results above are unchanged. The follow-up was selected after primary evidence and a negative visible-color refit diagnostic. Its configuration was selected using the four development images, frozen, then applied once to each remaining image. It is a second, exploratory round; do not merge it into the primary held-out claim.','\n| Image | Final origin | SSIM | PSNR dB | Edge F1 | DeltaE76 | Total path commands |','|---|---|---:|---:|---:|---:|---|']
    for case,row in final['cases'].items():lines.append(f"| {case} | {row['origin']} | {row['metrics']['ssim']:.4f} | {row['metrics']['psnr_db']:.3f} | {row['metrics']['edge_f1_1_5px']:.4f} | {row['metrics']['delta_e76_mean']:.3f} | {sum(row['structure']['path_commands'].values())} |")
    lines+=['\nAll12 final mean metrics:','```json',json.dumps(final['all12_mean_metrics'],indent=2),'```','Separate follow-up frozen8 mean metrics:','```json',json.dumps(final['extension_holdout8_mean_metrics'],indent=2),'```','Final selected SVG/PNG pairs are in best_outputs/. Their JSON sidecars record exact source candidate, settings, all candidate scores and structure. Highest score remains a numerical choice subject to the separately documented visual review.']
    with (output/'reports/RESULTS.md').open('a') as f:f.write('\n'.join(lines)+'\n')
    return final


def report(summary):
    """Format measured comparisons with split, model and complexity limitations."""
    lines=['# VTracer fidelity search: measured results','','These are native source-size SVG renders. Best means the highest fixed multi-metric score among the bounded tested candidates, not a global optimum. Pixel geometry remains eligible under the owner fidelity-first instruction; it is not clean scalable reconstruction.','','| Image | Owner SSIM | Best spline SSIM | Best ranked SSIM | Best mode | Original V04 | Repaired V04 | Best recent internal |','|---|---:|---:|---:|---|---:|---:|---:|']
    for name,case in summary['cases'].items():
        c=case['conditions'];recent=f"{c['best_recent']['metrics']['ssim']:.4f} ({c['best_recent']['historical_label']})" if 'best_recent' in c else 'not available'
        lines.append(f"| {name} | {c['owner']['metrics']['ssim']:.4f} | {c['best_spline']['metrics']['ssim']:.4f} | {c['best']['metrics']['ssim']:.4f} | {c['best']['config']['mode']} | {c['original']['metrics']['ssim']:.4f} | {c['repair']['metrics']['ssim']:.4f} | {recent} |")
    lines+=['','## All12 mean metrics','','| Condition | SSIM | PSNR dB | Edge F1 | DeltaE76 mean | High-pass RMSE sigma1 | Worst tile RMSE mean |','|---|---:|---:|---:|---:|---:|---:|']
    for label,v in summary['all12_means'].items():lines.append(f"| {label} | {v['ssim']:.4f} | {v['psnr_db']:.3f} | {v['edge_f1_1_5px']:.4f} | {v['delta_e76_mean']:.3f} | {v['highpass_rmse_sigma1']:.3f} | {v['tile_rmse_worst']:.3f} |")
    lines+=['','## Frozen common preset: held-out eight only','','The common preset was chosen from13shared pilot configurations on A01/A03/A05/A10, frozen, then evaluated on A02/A04/A06/A07/A08/A09/A11/A12 before their per-image tuning. Those images were previously known historical benchmarks, but their current results did not choose the common preset. This is a small held-out configuration test, not unseen-domain validation.','','```json',json.dumps(summary['frozen_common']['config'],indent=2),'```','','| Condition | Holdout SSIM | PSNR dB | Edge F1 | DeltaE76 | High-pass RMSE |','|---|---:|---:|---:|---:|---:|']
    for label,v in summary['holdout8_means'].items():lines.append(f"| {label} | {v['ssim']:.4f} | {v['psnr_db']:.3f} | {v['edge_f1_1_5px']:.4f} | {v['delta_e76_mean']:.3f} | {v['highpass_rmse_sigma1']:.3f} |")
    lines+=['','## Complexity and search cost','','All path commands include implicit repetitions and H/V/L commands. Coordinate-pair counts exclude H/V and arc implicit coordinates; do not mistake them for all free parameters. V04 rectangles are reported separately, not counted as zero geometry.','','| Image | Best paths | Rectangles | All path commands | Cubics | SVG bytes | Full search wall s |','|---|---:|---:|---:|---:|---:|---:|']
    for name,case in summary['cases'].items():
        st=case['conditions']['best']['structure'];lines.append(f"| {name} | {st['elements'].get('path',0)} | {st['elements'].get('rect',0)} | {sum(st['path_commands'].values())} | {st['cubic_segments']} | {st['bytes']} | {case['total_search_wall_seconds']:.2f} |")
    lines+=['','The CSV contains complexity for every selected historical and VTracer condition. Every trial result records generation CPU/wall time, render time and separate worker/renderer peak memory. Full search wall is the sum of isolated trial wall times; excludes comparison generation and historical SVG generation.','','## Local detail evidence','','Fixed4x4 tiles provide worst and median RGB RMSE for every condition in summary.json/CSV. They are spatial windows, not semantic ground truth. The Burger subset uses20historical manually confirmed seed centers,2.5pixel-radius disks at pixel centers; it never enters candidate selection.','','| Burger condition | Seed-center RMSE | Worst tile RMSE |','|---|---:|---:|']
    for name,case in summary['cases'].items():
        if name.startswith('A03'):
            for label,v in case['conditions'].items():lines.append(f"| {label} | {v['local']['seed_center_rmse']:.3f} | {v['local']['tile_rmse_worst']:.3f} |")
    lines+=['','## Proposed milestone numerical gates','','These thresholds were research proposals recorded before benchmark results, not owner approval. Visual acceptance remains separate.','','```json',json.dumps(summary['acceptance_numeric'],indent=2),'```','','## Reproduction and scope','','Every tested parameter set, native SVG, PNG, metric record and failure remains in its trial directory. The best spline and overall candidate configurations are in summary.json; they may be different. Full native comparison sheets and100/200/400% crop expansions are under comparisons/. Enlarged PNGs expose source-resolution defects; they are not a claim of higher-resolution truth. No OCR, semantic layers, alpha-preserving vectorization or universal preset is established.']
    return '\n'.join(lines)+'\n'

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=ROOT);parser.add_argument('--output',type=Path,default=ROOT);parser.add_argument('--primary-only',action='store_true');args=parser.parse_args();summary=collect(args.root.resolve(),args.output.resolve())
    if not args.primary_only:finalize_followup(args.root.resolve(),args.output.resolve(),summary)
# END CHANGE VTRACER-SUMMARY | 2026-10-24T23:42:36Z | CREATED | Author: vtracer_sources

# END CHANGE VTRACER-FOLLOWUP-SUMMARY | 2026-10-25T04:45:28Z | EDITED | Author: vtracer_sources
