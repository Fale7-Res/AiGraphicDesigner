"""Verify and package saved outputs only; never trace or render an SVG."""
# START CHANGE AGD-GEN-CLOSURE | 2026-10-27T14:33:48Z | CREATED | Author: package_generalization
import argparse, json, os, re, sys, xml.etree.ElementTree as ET
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw
ROOT=Path(os.environ.get('AGD_GENERALIZATION_ROOT',Path(__file__).resolve().parent))
sys.path.insert(0,str(ROOT.parent/'EXP_CODEX_WINDOWS_FIDELITY_20261027'))
from windows_search import compare, extra_metrics
from acquire_dataset import digest as digest_bytes
BACKGROUNDS={'white':(255,255,255),'black':(0,0,0),'bluegray':(40,80,120)}

def saved_file_digest(path):
    """Read-only content digest."""
    return digest_bytes(path.read_bytes())

def saved_inventory():
    """Freeze inherited evidence independently of packaging artifacts."""
    paths=[p for name in ('inputs','dataset','results') for p in (ROOT/name).rglob('*') if p.is_file()]
    return {p.relative_to(ROOT).as_posix():{'bytes':p.stat().st_size,'sha256':saved_file_digest(p)} for p in sorted(paths)}

def appearance(image,bg):
    """Apply saved evaluator's exact 8-bit sRGB compositing policy."""
    rgba=image.convert('RGBA')
    return Image.alpha_composite(Image.new('RGBA',rgba.size,BACKGROUNDS[bg]+(255,)),rgba).convert('RGB')

def check_saved_evidence():
    """Independently decode all artifacts and recompute selected appearance metrics."""
    manifest_path=ROOT/'inputs/manifest.json'
    manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
    freeze=json.loads((ROOT/'dataset/freeze.json').read_text())
    assert saved_file_digest(manifest_path)==freeze['manifest_sha256'],'Frozen manifest drift'
    assert len(manifest['cases'])==freeze['case_count']==8
    assert len({c['original_sha256'] for c in manifest['cases']})==manifest['independent_source_images']==7
    summaries=[]
    for case in manifest['cases']:
        folder=ROOT/'results'/case['id'];row=json.loads((folder/'case_result.json').read_text())
        ranking=json.loads((folder/'baseline_search/ranking.json').read_text())
        assert saved_file_digest(ROOT/'inputs'/case['file'])==case['sha256']==row['source_sha256']
        assert saved_file_digest(ROOT/case['original_file'])==case['original_sha256']
        assert row['dataset_manifest_sha256']==freeze['manifest_sha256']
        assert row['status']=='ok' and row['failed_candidates']==0 and not ranking['failed']
        assert len(ranking['ranked'])==row['baseline_candidates']==ranking['evaluated_candidates']
        for candidate in ranking['ranked']:
            trial=folder/'baseline_search'/candidate['trial']
            assert (trial/'output.svg').is_file() and (trial/'render.png').is_file()
        assert row['inherited']['trial']==row['new']['trial'],'Reranker winner changed'
        assert saved_file_digest(folder/'inherited.svg')==saved_file_digest(folder/'new.svg')
        assert saved_file_digest(folder/'inherited.png')==saved_file_digest(folder/'new.png')
        source=Image.open(folder/'prepared/reference_srgb_rgba.png').convert('RGBA')
        rendered=Image.open(folder/'new.png').convert('RGBA')
        assert source.size==rendered.size==tuple(case['dimensions'])
        recomputed={};expected=row['new']['background_metrics'] if row['has_alpha'] else {'white':row['new']['metrics']}
        for bg,stored in expected.items():
            a,b=np.asarray(appearance(source,bg)),np.asarray(appearance(rendered,bg))
            actual=compare(a,b)|extra_metrics(a,b)
            for key in ('ssim','psnr_db','mse','mae','highpass_rmse_sigma1','delta_e76_mean'):
                x,y=actual[key],stored[key]
                assert (x is None and y is None) or np.isclose(x,y,rtol=1e-12,atol=1e-12),(case['id'],bg,key,x,y)
            recomputed[bg]=actual
        delta=np.abs(np.asarray(source)[:,:,3].astype(float)-np.asarray(rendered)[:,:,3].astype(float))
        if row['has_alpha']:
            assert float(delta.max())==row['new']['alpha_max_error_0_255']==0
            assert float(delta.mean())==row['new']['alpha_mae_0_255']==0
        nodes=list(ET.parse(folder/'new.svg').getroot().iter());paths=[p for p in nodes if p.tag.rsplit('}',1)[-1]=='path']
        cubic_count=len(re.findall('[CcQq]',' '.join(p.get('d','') for p in paths)))
        assert cubic_count==0,'Saved pixel-mode finding differs'
        summaries.append({'id':case['id'],'dimensions':case['dimensions'],'has_alpha':row['has_alpha'],
          'candidates':row['baseline_candidates'],'inherited_trial':row['inherited']['trial'],'new_trial':row['new']['trial'],
          'svg_sha256':saved_file_digest(folder/'new.svg'),'svg_bytes':(folder/'new.svg').stat().st_size,'path_count':len(paths),
          'cubic_quadratic_commands':cubic_count,'metrics_recomputed':recomputed,'alpha_mae_0_255':float(delta.mean()),
          'alpha_max_error_0_255':float(delta.max()),'wall_seconds_recorded':row['total_wall_seconds'],
          'sampled_worker_peak_mib_recorded':row['maximum_sampled_worker_tree_mib']})
    assert sum(r['candidates'] for r in summaries)==140
    png_count=svg_count=0
    for name in ('inputs','dataset','results'):
        for path in sorted((ROOT/name).rglob('*')):
            if path.suffix.lower() in ('.png','.jpg','.jpeg'):
                with Image.open(path) as im:im.load();assert im.width>0 and im.height>0
                png_count+=path.suffix.lower()=='.png'
            elif path.suffix.lower()=='.svg':
                root=ET.parse(path).getroot();assert root.tag.rsplit('}',1)[-1]=='svg'
                for node in root.iter():
                    tag=node.tag.rsplit('}',1)[-1]
                    assert tag not in ('image','script','foreignObject','feImage'),(str(path),tag)
                    for key,value in node.attrib.items():
                        if key.rsplit('}',1)[-1]=='href':assert value.startswith('#'),(str(path),value)
                        assert 'data:image' not in value.lower(),str(path)
                svg_count+=1
    return {'status':'PASS','operation':'Saved decoding/metric recomputation only; no tracing or rendering',
      'case_count':8,'independent_originals':7,'candidates':140,'failed_candidates':0,'same_winner_cases':8,
      'reconstruction_improvement_demonstrated':False,'pngs_decoded':png_count,'svgs_parsed_raster_free':svg_count,
      'cases':summaries,'architecture':'NOT_APPROVED'}

def make_visual_evidence(summary):
    """Create saved-render sheets and HTML showing actual original SVG browser zoom."""
    visual=ROOT/'reports/comparisons';visual.mkdir(parents=True,exist_ok=True);articles=[]
    order=sorted(summary['cases'],key=lambda r:min(m['ssim'] for m in r['metrics_recomputed'].values()))
    for item in order:
        cid=item['id'];folder=ROOT/'results'/cid
        source=Image.open(folder/'prepared/reference_srgb_rgba.png').convert('RGBA')
        inherited=Image.open(folder/'inherited.png').convert('RGBA');selected=Image.open(folder/'new.png').convert('RGBA')
        sections=[]
        for bg in BACKGROUNDS if item['has_alpha'] else ('white',):
            images=[appearance(im,bg) for im in (source,inherited,selected)]
            delta=np.abs(np.asarray(images[0]).astype(float)-np.asarray(images[2]).astype(float))
            err=Image.fromarray(np.clip(delta*32,0,255).astype(np.uint8));w,h=source.size;column=max(w,240)
            sheet=Image.new('RGB',(4*column,h+88),'white');draw=ImageDraw.Draw(sheet)
            draw.text((8,4),f'{cid} / {bg} / actual saved renders / error x32 / same winner',fill='black')
            labels=('Original','Inherited','Selected (same)','Absolute RGB error x32')
            for i,(label,im) in enumerate(zip(labels,images+[err])):
                draw.text((i*column+8,30),label,fill='black');sheet.paste(im,(i*column,56))
            sheet_name=f'{cid}_{bg}.png';sheet.save(visual/sheet_name)
            tiles=[(float(np.mean(delta[y:y+32,x:x+32]**2)),x,y) for y in range(0,h,32) for x in range(0,w,32)]
            _,x,y=max(tiles);x,y=min(x,w-32),min(y,h-32);crop=(x,y,x+32,y+32)
            board=Image.new('RGB',(2048,570),'white');draw=ImageDraw.Draw(board)
            draw.text((8,5),f'{cid} {bg} worst sampled-error tile {crop}; nearest-neighbor 16x raster diagnostic, not a new SVG render',fill='black')
            for i,(label,im) in enumerate(zip(labels,images+[err])):
                draw.text((i*512+8,29),label,fill='black');board.paste(im.crop(crop).resize((512,512),Image.Resampling.NEAREST),(i*512,54))
            crop_name=f'{cid}_{bg}_crop16x.png';board.save(visual/crop_name)
            sections.append(f'<details><summary>{bg}: saved comparison / x32 error / 16x worst tile</summary><img class="sheet" src="comparisons/{sheet_name}"><img class="sheet" src="comparisons/{crop_name}"></details>')
        worst=min(m['ssim'] for m in item['metrics_recomputed'].values())
        figures=''.join(f'<figure><figcaption>{label}</figcaption><img width="{source.width}" height="{source.height}" src="../results/{cid}/{filename}"></figure>' for label,filename in [('Original tested raster','prepared/reference_srgb_rgba.png'),('Actual inherited SVG','inherited.svg'),('Actual selected SVG (identical)','new.svg')])
        articles.append(f'<article><h2>{cid}</h2><p>Worst-background SSIM {worst:.9f}; {item["path_count"]:,} paths; {item["svg_bytes"]:,} bytes; {item["candidates"]} candidates; {item["wall_seconds_recorded"]:.1f}s; sampled worker peak {item["sampled_worker_peak_mib_recorded"]:.1f} MiB. Zero cubic/quadratic commands. Winner unchanged.</p><p><a href="../results/{cid}/inherited.svg">Inherited SVG</a> | <a href="../results/{cid}/new.svg">Selected SVG</a> | <a href="../results/{cid}/case_result.json">Saved metrics</a></p><div class="viewport"><div class="panels">{figures}</div></div>{"".join(sections)}</article>')
    document='''<!doctype html><html lang="en"><meta charset="utf-8"><title>Generalization evidence — NOT_APPROVED</title>
<style>body{font:16px system-ui;margin:24px;background:#eee;color:#161616}header{position:sticky;top:0;background:#fff;padding:12px;z-index:2;border:1px solid #aaa}article{background:white;margin:24px 0;padding:16px}figure{margin:10px;flex:none}figcaption{margin:8px 0}.panels{display:flex;gap:12px;width:max-content}.viewport{overflow:auto;max-height:650px;background:#fff}.sheet{max-width:100%;display:block;margin:12px 0}summary{cursor:pointer;padding:10px}select{font:inherit}body[data-bg="black"] .viewport{background:black}body[data-bg="bluegray"] .viewport{background:rgb(40,80,120)}</style>
<header><b>Generalization saved evidence / architecture NOT_APPROVED</b><br>Eight cases; seven independent originals; 140 candidates; no winner changed; no reconstruction improvement. Worst SSIM first.<br>Actual SVG browser scale: <select id="zoom"><option value="1">1x</option><option value="4">4x</option><option value="16">16x</option></select> Background: <select id="bg"><option>white</option><option>black</option><option>bluegray</option></select></header>
<p>Native metrics use saved resvg 0.49.0 PNGs at tested dimensions, mostly max-edge 320. Browser zoom reveals vector structure, not a separately measured render. Pixel-cell paths and source-alpha run masks remain grid dependent. Results establish bounded raster matching, not coherent geometry, text reconstruction, semantic editing, or universal fidelity. Sheet crops are explicitly enlarged raster diagnostics. The source raster uses ordinary browser resampling at zoom; it is not higher-resolution ground truth.</p>'''
    document+=''.join(articles)+'''<script>const imgs=[...document.querySelectorAll('.panels img')];imgs.forEach(i=>{i.dataset.w=i.width;i.dataset.h=i.height});document.querySelector('#zoom').onchange=e=>imgs.forEach(i=>{i.width=Number(i.dataset.w)*Number(e.target.value);i.height=Number(i.dataset.h)*Number(e.target.value)});document.querySelector('#bg').onchange=e=>document.body.dataset.bg=e.target.value;</script></html>'''
    (ROOT/'reports/dashboard.html').write_text(document,encoding='utf-8')

def package_existing_outputs():
    """Check byte preservation before/after writing new reports and comparisons."""
    before=saved_inventory();summary=check_saved_evidence();make_visual_evidence(summary)
    (ROOT/'reports/saved_artifact_inventory.json').write_text(json.dumps(before,indent=2),encoding='utf-8')
    (ROOT/'reports/verification.json').write_text(json.dumps(summary,indent=2,allow_nan=False),encoding='utf-8')
    assert before==saved_inventory(),'Packaging modified inherited evidence'
    print(json.dumps({k:v for k,v in summary.items() if k!='cases'},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--verify-only',action='store_true');args=parser.parse_args()
    if args.verify_only:print(json.dumps(check_saved_evidence(),indent=2,allow_nan=False))
    else:package_existing_outputs()
# END CHANGE AGD-GEN-CLOSURE | 2026-10-27T14:33:48Z | CREATED | Author: package_generalization
