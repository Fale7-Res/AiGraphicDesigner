"""Paired native-resolution evaluator; structural counts are not semantic scores."""
# START CHANGE EXP-AUTO-20261021 | 2026-10-21T20:03:54Z | CREATED | Author: benchmark
from pathlib import Path
import argparse
import json
import re
import subprocess
import time
import xml.etree.ElementTree as ET
from collections import Counter
import numpy as np
from PIL import Image, ImageDraw
from scipy.ndimage import distance_transform_edt
from skimage.feature import canny
from skimage.color import rgb2gray
from skimage.metrics import structural_similarity
# END CHANGE EXP-AUTO-20261021 | 2026-10-21T20:03:54Z | CREATED

# START CHANGE EXP-AUTO-20261021 | 2026-10-21T20:03:54Z | CREATED | Author: benchmark
def load_rgb(path):
    """Composite transparent pixels on white, without resizing or color conversion."""
    im = Image.open(path).convert('RGBA')
    white = Image.new('RGBA', im.size, (255, 255, 255, 255))
    return np.array(Image.alpha_composite(white, im).convert('RGB'))
# END CHANGE EXP-AUTO-20261021 | 2026-10-21T20:03:54Z | CREATED

# START CHANGE EXP-AUTO-20261021 | 2026-10-21T20:03:54Z | CREATED | Author: benchmark
def render_svg(path, png, width, height):
    """Adapt original V04 rasterize_svg protocol; native page, common Inkscape."""
    Path(png).parent.mkdir(parents=True, exist_ok=True)
    start = time.perf_counter()
    proc = subprocess.run(['inkscape', str(Path(path).resolve()), '--export-area-page',
                           '--export-type=png', f'--export-filename={Path(png).resolve()}',
                           f'--export-width={width}', f'--export-height={height}'],
                          capture_output=True, text=True, timeout=120)
    if proc.returncode:
        raise RuntimeError(proc.stderr[-2000:])
    if Image.open(png).size != (width, height):
        raise ValueError('Renderer dimensions differ from source')
    return {'render_seconds': time.perf_counter()-start,
            'renderer': subprocess.check_output(['inkscape', '--version'], text=True).strip()}
# END CHANGE EXP-AUTO-20261021 | 2026-10-21T20:03:54Z | CREATED

# START CHANGE EXP-AUTO-20261021 | 2026-10-21T20:03:54Z | CREATED | Author: benchmark
def compare(ref, pred):
    """RGB 0..255 errors and 1.5px-tolerance Canny edge agreement, not geometry GT."""
    if ref.shape != pred.shape or ref.ndim != 3 or ref.shape[2] != 3:
        raise ValueError('Expected equal HxWx3 arrays; implicit resizing is forbidden')
    delta = ref.astype(float)-pred.astype(float)
    mse = float(np.mean(delta**2))
    a = canny(rgb2gray(ref.astype(float)/255), sigma=1, low_threshold=.1, high_threshold=.2)
    b = canny(rgb2gray(pred.astype(float)/255), sigma=1, low_threshold=.1, high_threshold=.2)
    # Empty edge maps have no meaningful precision or recall: represent as null.
    precision = float(np.mean(distance_transform_edt(~a)[b] <= 1.5)) if b.any() and a.any() else None
    recall = float(np.mean(distance_transform_edt(~b)[a] <= 1.5)) if a.any() and b.any() else None
    f1 = (2*precision*recall/(precision+recall) if precision+recall else 0.) if precision is not None and recall is not None else None
    return {'mae': float(np.mean(abs(delta))), 'mse': mse, 'rmse': float(np.sqrt(mse)),
            'psnr_db': float(10*np.log10(255**2/mse)) if mse else None,
            'identical': mse == 0,
            'ssim': float(structural_similarity(ref.astype(float), pred.astype(float), channel_axis=2, data_range=255)),
            'edge_precision_1_5px': precision, 'edge_recall_1_5px': recall, 'edge_f1_1_5px': f1,
            'source_edge_pixels': int(a.sum()), 'render_edge_pixels': int(b.sum())}
# END CHANGE EXP-AUTO-20261021 | 2026-10-21T20:03:54Z | CREATED

# START CHANGE EXP-AUTO-20261021 | 2026-10-21T20:04:52Z | EDITED | Author: benchmark
def svg_structure(path):
    """Count serialized elements and path commands (including implicit repetitions)."""
    raw = Path(path).read_bytes()
    root = ET.fromstring(raw)
    tags = Counter(e.tag.split('}')[-1] for e in root.iter())
    commands = Counter()
    external_refs = [value for elem in root.iter() for key,value in elem.attrib.items()
                     if key.split('}')[-1] == 'href' and not value.startswith('#')]
    coord_counts = {'M':2,'L':2,'H':1,'V':1,'C':6,'S':4,'Q':4,'T':2,'A':7,'Z':0}
    for elem in root.iter():
        if elem.tag.split('}')[-1] != 'path':
            continue
        d = elem.get('d','')
        for match in re.finditer(r'([MmLlHhVvCcSsQqTtAaZz])([^MmLlHhVvCcSsQqTtAaZz]*)',d):
            cmd, tail = match.groups(); cmd=cmd.upper()
            nums=re.findall(r'[-+]?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?',tail)
            count=len(nums)//coord_counts[cmd] if coord_counts[cmd] else 1
            if cmd=='M' and count>1:
                commands['M']+=1; commands['L']+=count-1
            else:
                commands[cmd]+=count
    return {'bytes':len(raw),'elements':dict(tags),'path_commands':dict(commands),
            'cubic_segments':commands['C']+commands['S'],
            'explicit_path_coordinate_pairs':commands['M']+commands['L']+3*commands['C']+2*commands['S']+2*commands['Q']+commands['T'],
            'raster_free':tags['image']==0 and tags['foreignObject']==0 and b'data:image' not in raw.lower(),
            'external_href_count':len(external_refs), 'script_count':tags['script'],
            'foreign_object_count':tags['foreignObject'],
            'note':'Definitions and uses counted separately; coordinate pairs omit arc and H/V implicit coordinates. No semantic editability claim.'}
# END CHANGE EXP-AUTO-20261021 | 2026-10-21T20:04:52Z | EDITED

# START CHANGE EXP-AUTO-20261021 | 2026-10-21T20:03:54Z | CREATED | Author: benchmark
def make_comparison(ref, baseline, candidate, target):
    """Six native-resolution panels; no resampling in the saved comparison."""
    h,w=ref.shape[:2]
    err=np.abs(ref.astype(float)-candidate.astype(float)).mean(2)
    heat=np.stack([np.clip(err*4,0,255),np.zeros_like(err),np.zeros_like(err)],axis=2).astype('uint8')
    overlay=np.rint((ref.astype(float)+candidate)/2).astype('uint8')
    baseerr=np.abs(ref.astype(float)-baseline.astype(float)).mean(2)
    baseheat=np.stack([np.clip(baseerr*4,0,255),np.zeros_like(baseerr),np.zeros_like(baseerr)],axis=2).astype('uint8')
    panels=[('Original',ref),('Original V04',baseline),('Automatic candidate',candidate),
            ('50% candidate + original',overlay),('V04 mean abs error x4',baseheat),('Candidate mean abs error x4',heat)]
    canvas=Image.new('RGB',(w*3,(h+28)*2),'white'); draw=ImageDraw.Draw(canvas)
    for i,(label,img) in enumerate(panels):
        x=(i%3)*w;y=(i//3)*(h+28)
        draw.text((x+6,y+6),label,fill='black');canvas.paste(Image.fromarray(img),(x,y+28))
    Path(target).parent.mkdir(parents=True,exist_ok=True);canvas.save(target)
# END CHANGE EXP-AUTO-20261021 | 2026-10-21T20:03:54Z | CREATED

# START CHANGE EXP-AUTO-20261021 | 2026-10-21T20:03:54Z | CREATED | Author: benchmark
def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--original',required=True);parser.add_argument('--baseline',required=True)
    parser.add_argument('--candidate',required=True);parser.add_argument('--out',required=True)
    args=parser.parse_args();out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    ref=load_rgb(args.original);h,w=ref.shape[:2];results={}
    for key,svg in [('baseline',args.baseline),('candidate',args.candidate)]:
        timing=render_svg(svg,out/f'{key}.png',w,h)
        results[key]={**compare(ref,load_rgb(out/f'{key}.png')),**timing,'structure':svg_structure(svg)}
    make_comparison(ref,load_rgb(out/'baseline.png'),load_rgb(out/'candidate.png'),out/'comparison.png')
    (out/'metrics.json').write_text(json.dumps(results,indent=2,allow_nan=False))
    print(json.dumps(results,indent=2,allow_nan=False))
# END CHANGE EXP-AUTO-20261021 | 2026-10-21T20:03:54Z | CREATED

# START CHANGE EXP-AUTO-20261021 | 2026-10-21T20:03:54Z | CREATED | Author: benchmark
if __name__=='__main__':
    main()
# END CHANGE EXP-AUTO-20261021 | 2026-10-21T20:03:54Z | CREATED
