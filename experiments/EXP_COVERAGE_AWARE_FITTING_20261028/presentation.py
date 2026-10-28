"""Owner-review visuals from completed coverage-aware results; no fitting or tracing."""
# START CHANGE AGD-CA-PRESENTATION | 2026-10-28T05:22:51Z | CREATED | Author: package_generalization
from pathlib import Path
import argparse,html,json,os,sys
import numpy as np
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'EXP_GEOMETRY_APPEARANCE_ABLATION_01'))
import run_experiment as inherited
BACKGROUND_COLORS={'white':(255,255,255),'black':(0,0,0),'bluegray':(40,80,120)}
LABELS={'source':'Prepared source','pixel':'Pixel fidelity reference','Agrad':'Agrad inherited interior','B':'B coverage flat','C':'C coverage adaptive','truth':'Known vector truth','Aflat':'Aflat inherited flat'}
SHORT={'source':'S NN','pixel':'P','Agrad':'Ag','B':'B','C':'C','truth':'T'}

def rgb_on(image,background='white'):
    rgba=image.convert('RGBA')
    return Image.alpha_composite(Image.new('RGBA',rgba.size,(*BACKGROUND_COLORS[background],255)),rgba).convert('RGB')

def number(value,decimals=6):
    if value is None:return 'exact / undefined'
    return f'{value:.{decimals}f}' if isinstance(value,(float,int)) else html.escape(str(value))

def three_background_error(source,predicted):
    """Float composited three-background residual, matching driver's local-error policy."""
    a=np.asarray(source.convert('RGBA'),dtype=float);b=np.asarray(predicted.convert('RGBA'),dtype=float)
    aa=a[:,:,3:4]/255;ba=b[:,:,3:4]/255;ap=a[:,:,:3]*aa;bp=b[:,:,:3]*ba
    errors=[]
    for color in BACKGROUND_COLORS.values():
        bg=np.array(color);errors.append(((bp+(1-ba)*bg)-(ap+(1-aa)*bg))**2)
    return np.mean(np.mean(errors,axis=0),axis=2)

def choose_boxes(source,predicted,case):
    """Worst complete 24px tile plus preregistered thin-feature box or center."""
    w,h=source.size;edge=min(24,w,h);error=three_background_error(source,predicted)
    xs=sorted(set(range(0,w-edge+1,edge))|{w-edge});ys=sorted(set(range(0,h-edge+1,edge))|{h-edge})
    score,x,y=max((float(error[y:y+edge,x:x+edge].mean()),x,y) for y in ys for x in xs)
    fixture=case.get('fixture',{});thin=fixture.get('thin_regions',[])
    if thin:
        bx,by,bw,bh=thin[0]['critical_box'];cx,cy=bx+bw/2,by+bh/2;name='thin_feature'
    else:cx,cy=w/2,h/2;name='center_detail'
    x2=int(np.clip(round(cx-edge/2),0,w-edge));y2=int(np.clip(round(cy-edge/2),0,h-edge))
    return [('worst_C_error',[x,y,edge,edge]),(name,[x2,y2,edge,edge])]

def native_sheets(case,result,folder):
    """Package saved actual PNG renders with source, alpha and visible error maps."""
    saved=ROOT/'results'/case['id'];source=Image.open(saved/'source.png').convert('RGBA')
    conditions=[key for key in ('pixel','Agrad','B','C','truth') if key in result['conditions']]
    images={'source':source}|{key:Image.open(saved/key/'render.png').convert('RGBA') for key in conditions}
    w,h=source.size;column=max(w,180);labels=['source']+conditions
    for bg in BACKGROUND_COLORS:
        board=Image.new('RGB',(len(labels)*column,h+44),'white');draw=ImageDraw.Draw(board)
        for i,key in enumerate(labels):
            draw.text((i*column+5,6),LABELS[key],fill='black');draw.text((i*column+5,22),bg+' / saved actual render' if key!='source' else bg+' / source raster',fill='black')
            board.paste(rgb_on(images[key],bg),(i*column,42))
        board.save(folder/f'comparison_{bg}.png')
        error_board=Image.new('RGB',(len(conditions)*column,h+30),'white');ed=ImageDraw.Draw(error_board);ref=np.asarray(rgb_on(source,bg),dtype=float)
        for i,key in enumerate(conditions):
            delta=np.abs(ref-np.asarray(rgb_on(images[key],bg),dtype=float));heat=Image.fromarray(np.uint8(np.clip(delta*6,0,255)))
            ed.text((i*column+4,6),key+' absolute RGB error x6',fill='black');error_board.paste(heat,(i*column,28))
        error_board.save(folder/f'errors_{bg}.png')
    alpha=Image.new('RGB',(len(labels)*column,h+30),'white');ad=ImageDraw.Draw(alpha)
    for i,key in enumerate(labels):ad.text((i*column+4,6),key+' actual alpha',fill='black');alpha.paste(images[key].getchannel('A').convert('RGB'),(i*column,28))
    alpha.save(folder/'alpha.png')
    return images,conditions

def actual_zoom_sheets(case,folder,images,conditions):
    """Actual SVG viewport renders at 1x/4x/16x, never upscaled SVG screenshots."""
    saved=ROOT/'results'/case['id'];measurements=[];boxes=choose_boxes(images['source'],images['C'],case)
    for name,box in boxes:
        x,y,w,h=box
        for scale in (1,4,16):
            labels=['source']+conditions;board=Image.new('RGB',(len(labels)*w*scale,h*scale+28),'white');draw=ImageDraw.Draw(board)
            reference=rgb_on(images['source']).crop((x,y,x+w,y+h)).resize((w*scale,h*scale),Image.Resampling.NEAREST)
            board.paste(reference,(0,28));draw.text((1,6),'S NN',fill='black')
            for i,key in enumerate(conditions,1):
                svg=folder/f'{name}_{key}_{scale}x.svg'
                timing=inherited.crop_svg(saved/key/'output.svg',svg,box,scale)
                with Image.open(svg.with_suffix('.png')) as actual:image=rgb_on(actual)
                board.paste(image,(i*w*scale,28));draw.text((i*w*scale+1,6),SHORT[key],fill='black')
                measurements.append({'name':name,'box':box,'scale':scale,'condition':key,'actual_vector_viewport_render':True,'render':timing})
            board.save(folder/f'{name}_{scale}x.png')
    (folder/'zooms.json').write_text(json.dumps({'boxes':boxes,'measurements':measurements,'source_crop':'Nearest-neighbor source sample display; not high-resolution ground truth'},indent=2),encoding='utf-8')
    return boxes

def metric_table(result,background):
    parts=['<table><tr><th>Condition</th><th>SSIM</th><th>PSNR dB</th><th>MSE</th><th>Worst 32px RMSE</th><th>Mean DeltaE76</th><th>Alpha MAE</th></tr>']
    for key in ('pixel','Aflat','Agrad','B','C','truth'):
        if key not in result['conditions']:continue
        row=result['conditions'][key];m=row['metrics'][background]
        values=[key,m['ssim'],m['psnr_db'],m['mse'],m.get('worst_32px_tile_rmse'),m.get('delta_e76_mean'),row.get('alpha_mae')]
        parts.append('<tr>'+''.join('<td>'+number(value)+'</td>' for value in values)+'</tr>')
    return ''.join(parts)+'</table>'

def build_presentation():
    """Require all nine results complete; refuse to replace presentation evidence."""
    manifest=json.loads((ROOT/'inputs/manifest.json').read_text(encoding='utf-8'));cases=manifest['cases']
    if len(cases)!=9:raise ValueError('Expected nine preregistered cases')
    results={}
    for case in cases:
        file=ROOT/'results'/case['id']/'result.json'
        if not file.is_file():raise FileNotFoundError('Wait for parent completion; missing '+str(file))
        result=json.loads(file.read_text(encoding='utf-8'))
        if not all(k in result['conditions'] for k in ('Aflat','Agrad','B','C')):raise ValueError('Incomplete conditions '+case['id'])
        results[case['id']]=result
    output=ROOT/'presentation'
    if output.exists() and any(output.iterdir()):raise FileExistsError('Preserve prior presentation; choose a fresh experiment/export target')
    output.mkdir(exist_ok=True)
    order=sorted(cases,key=lambda c:min(v['ssim'] for v in results[c['id']]['conditions']['C']['metrics'].values()))
    cards=[]
    for case in order:
        cid=case['id'];result=results[cid];folder=output/cid;folder.mkdir()
        images,conditions=native_sheets(case,result,folder);boxes=actual_zoom_sheets(case,folder,images,conditions)
        worst=min(v['ssim'] for v in result['conditions']['C']['metrics'].values())
        cards.append(f'<section id="{cid}"><h2>{html.escape(cid)}</h2><p>{case["kind"]}; C worst-background SSIM {worst:.9f}. Native saved renders at {images["source"].width}×{images["source"].height}.</p>')
        c=result['conditions']['C'];ag=result['conditions']['Agrad']
        cards.append('<p>Balanced float three-background MSE: Agrad '+number(ag.get('float_three_background_mse'))+' → C '+number(c.get('float_three_background_mse'))+'. Held-out periodic-pixel MSE: '+number(ag.get('heldout_float_three_background_mse'))+' → '+number(c.get('heldout_float_three_background_mse'))+'. Geometry/mask invariant is checked separately in result.json.</p>')
        cards.append('<p>'+''.join(f'<a href="results/{cid}/{key}/output.svg">{key} full SVG</a> | ' for key in ('pixel','Aflat','Agrad','B','C','truth') if key in result['conditions'])+f'<a href="results/{cid}/source.png">Prepared source</a> | <a href="results/{cid}/result.json">All metrics</a> | <a href="results/{cid}/fitting.json">Fitting diagnostics</a> | <a href="results/{cid}/coverage/maps.json">Coverage-map diagnostics</a> | <a href="results/{cid}/coverage/maps.npz">Numerical maps</a></p>')
        for bg in BACKGROUND_COLORS:
            cards.append(f'<details {"open" if bg=="white" else ""}><summary>{bg}: native comparison, amplified errors and metrics</summary><figure><img loading="lazy" src="presentation/{cid}/comparison_{bg}.png"></figure><figure><img loading="lazy" src="presentation/{cid}/errors_{bg}.png"></figure>'+metric_table(result,bg)+'</details>')
        cards.append(f'<details><summary>Actual alpha and effective-mixture boundary mask</summary><figure><img loading="lazy" src="presentation/{cid}/alpha.png"></figure><img loading="lazy" src="results/{cid}/coverage/boundary_band.png"><p>The boundary band includes translucent interiors and is not physical contour ground truth. Fixed masks can retain source-grid dependence on real RGBA cases.</p></details>')
        for name,box in boxes:
            cards.append(f'<h3>{name}: source coordinates {box}</h3>')
            for scale in (1,4,16):
                cards.append(f'<details {"open" if scale==4 else ""}><summary>Actual SVG viewport {scale}× (S NN is raster sample display)</summary><figure><img loading="lazy" src="presentation/{cid}/{name}_{scale}x.png"></figure><p>'+''.join(f'<a href="presentation/{cid}/{name}_{key}_{scale}x.svg">{SHORT[key]} cropped SVG</a> | ' for key in conditions)+'</p></details>')
        cards.append(f'<a href="presentation/{cid}/zooms.json">Crop selection and render timing/memory</a></section>')
    document='''<!doctype html><html lang="en"><meta charset="utf-8"><title>Coverage-aware fixed-geometry fitting — owner review</title><style>body{font:16px system-ui;background:#161c24;color:#eee;margin:24px;line-height:1.5}header{max-width:1100px}section{border-top:2px solid #7089a5;margin-top:40px;padding-top:20px}figure{overflow:auto;margin:12px 0}img{max-width:none}td,th{border:1px solid #596b81;padding:5px;text-align:right}table{border-collapse:collapse}a{color:#9ad3ff}summary{cursor:pointer;padding:10px;background:#242f3e}details{margin:12px 0}h3{margin-top:28px}</style><header><h1>Coverage-aware fitting: owner visual review</h1><p>Research only. Global architecture NOT_APPROVED. All nine cases are shown, sorted worst C background SSIM first. Native metrics, geometry quality, approximation to the pixel reference and cross-category generalization are separate claims. A result is not successful merely because C improves Agrad.</p><p>S: prepared source; P: strongest saved pixel fidelity reference when available; Ag: inherited interior-only adaptive fit; B: coverage-aware flat; C: coverage-aware adaptive; T: known true vector control when available. Aflat is included in full metrics and SVG links. Analytic controls are causal fixtures, not real-image generalization evidence. New fixtures have no pixel baseline.</p><p>Comparison/error PNGs use saved actual native renders. Zoom SVGs are rendered directly at 1×,4×,16× from the original vector viewport; S NN is nearest-neighbor source raster display, not high-resolution ground truth. Error maps show absolute RGB error ×6 with saturation. Crop1 is the worst C complete 24px tile by balanced float three-background MSE; crop2 uses the fixture thin-feature location or image center. Curves and path geometry remain fixed; no stroke correction was introduced here.</p></header>'''+''.join(cards)+'</html>'
    (ROOT/'index.html').write_text(document,encoding='utf-8')
    return {'cases':len(cases),'order':[c['id'] for c in order],'dashboard':str(ROOT/'index.html'),'presentation':str(output)}

# START CHANGE AGD-COVERAGE-FLAT-VISUAL | 2026-10-28T05:34:38Z | CREATED | Author: root
def add_flat_comparisons():
    """Add explicit flat-pair negatives without repeating any vector rendering."""
    document=(ROOT/'index.html').read_text(encoding='utf-8')
    for case in json.loads((ROOT/'inputs/manifest.json').read_text())['cases']:
        cid=case['id'];saved=ROOT/'results'/cid;folder=ROOT/'presentation'/cid
        source=rgb_on(Image.open(saved/'source.png'));a=rgb_on(Image.open(saved/'Aflat/render.png'));b=rgb_on(Image.open(saved/'B/render.png'))
        ref=np.asarray(source,dtype=float);w,h=source.size;column=max(w,180)
        pictures=[('Source',source),('Aflat interior',a),('B coverage flat',b)]
        for label,image in [('Aflat error x6',a),('B error x6',b)]:pictures.append((label,Image.fromarray(np.uint8(np.clip(np.abs(ref-np.asarray(image,dtype=float))*6,0,255)))))
        sheet=Image.new('RGB',(column*5,h+30),'white');draw=ImageDraw.Draw(sheet)
        for i,(label,image) in enumerate(pictures):draw.text((i*column+3,5),label,fill='black');sheet.paste(image,(i*column,28))
        sheet.save(folder/'flat_pair_white.png')
        heading=f'<h2>{cid}</h2>'
        if f'presentation/{cid}/flat_pair_white.png' not in document:document=document.replace(heading,heading+f'<details><summary>Flat comparison: inspect SSIM regressions as well as MSE gains</summary><figure><img loading="lazy" src="presentation/{cid}/flat_pair_white.png"></figure></details>')
    (ROOT/'index.html').write_text(document,encoding='utf-8')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--build',action='store_true');parser.add_argument('--flat-pairs',action='store_true');args=parser.parse_args()
    if args.build:print(json.dumps(build_presentation(),indent=2));add_flat_comparisons()
    elif args.flat_pairs:add_flat_comparisons()
# END CHANGE AGD-COVERAGE-FLAT-VISUAL | 2026-10-28T05:34:38Z | CREATED | Author: root
# END CHANGE AGD-CA-PRESENTATION | 2026-10-28T05:22:51Z | CREATED | Author: package_generalization
