# START CHANGE AGD-GENERALIZATION-DATA | 2026-10-27T11:09:10Z | CREATED | Author: codex-dataset-agent; Parent: AGD-GENERALIZATION-20261027
"""Acquire a prespecified unseen raster suite; never inspect benchmark scores here."""
from pathlib import Path
import datetime
import hashlib
import io
import json
import re
import urllib.request
import html
from PIL import Image

ROOT = Path(__file__).resolve().parent
INPUTS = ROOT / 'inputs'
DATASET = ROOT / 'dataset'
BASE = 'https://raw.githubusercontent.com/scikit-image/scikit-image/v0.25.2/skimage/data/'
DOC = 'https://scikit-image.org/docs/0.25.x/api/skimage.data.html'
SPECS = [
    ('G01_coffee', 'coffee.png', ['food_beverage_photograph','wood_texture','porcelain_reflections'], 'Rachel Michetti / Pikolo Espresso Bar', 'CC0', BASE+'coffee.png', DOC, 'resize'),
    ('G02_chelsea', 'chelsea.png', ['natural_photograph','fur_texture','fine_detail'], 'Stefan van der Walt', 'CC0', BASE+'chelsea.png', DOC, 'resize'),
    ('G03_rocket', 'rocket.jpg', ['real_photograph','smoke','soft_gradients','shadow'], 'SpaceX', 'public domain', BASE+'rocket.jpg', DOC, 'resize'),
    ('G04_camera', 'camera.png', ['real_photograph','grayscale','fine_detail'], 'Jack van Gerwen', 'CC0', BASE+'camera.png', DOC, 'resize'),
    ('G05_chelsea_nativecrop', 'chelsea.png', ['natural_photograph','native_resolution_crop','fine_detail'], 'Stefan van der Walt', 'CC0', BASE+'chelsea.png', DOC, 'center_crop'),
    ('G06_arabic', 'F3l-caligraphy.png', ['arabic_lettering','illustration','thin_contours'], 'Hakeem.gadi', 'public-domain dedication', None, 'https://commons.wikimedia.org/wiki/File:F3l-caligraphy.png', 'resize'),
    ('G07_tux', 'Tux.png', ['mascot_logo','raster_illustration','alpha','smooth_shading'], 'Larry Ewing and The GIMP; lewing@isc.tamu.edu', 'attribution-only permission', 'https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png', 'https://commons.wikimedia.org/wiki/File:Tux.png', 'resize'),
    ('G08_dice_alpha', 'PNG_transparency_demonstration_1.png', ['published_3d_raster_illustration','alpha','translucency','reflections','soft_shadows'], 'Daniel G.; Ed g2s; CyberShadow', 'CC-BY-SA-3.0', 'https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png', 'https://commons.wikimedia.org/wiki/File:PNG_transparency_demonstration_1.png', 'resize'),
]

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent':'AiGraphicDesignerResearch/1.0 (licensed raster benchmarking)'})
    with urllib.request.urlopen(req, timeout=60) as response:
        return response.read(), response.url

def digest(data):
    return hashlib.sha256(data).hexdigest()

def alpha_info(image):
    alpha = image.convert('RGBA').getchannel('A')
    histogram = alpha.histogram()
    return {'unique_values':sum(v>0 for v in histogram),'transparent_pixels':histogram[0], 'partial_pixels':sum(histogram[1:255]), 'opaque_pixels':histogram[255]}

def main():
    INPUTS.mkdir(exist_ok=True)
    (DATASET/'originals').mkdir(parents=True, exist_ok=True)
    (DATASET/'sources').mkdir(exist_ok=True)
    cases=[]
    for cid, filename, domains, author, license_name, url, source, mode in SPECS:
        stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        sourcefile = DATASET/'sources'/('scikit-image-data.html' if source==DOC else cid+'.html')
        if not sourcefile.exists():
            try:
                sourcefile.write_bytes(fetch(source)[0])
            except Exception as exc:
                print('LICENSE SNAPSHOT FAILURE', cid, str(exc), flush=True)
                raise
        if url is None:
            markup=sourcefile.read_text(encoding='utf-8')
            match=re.search(r'<a[^>]+href="([^"]+)"[^>]*>Original file</a>', markup)
            if not match:
                match=re.search(r'class="fullMedia".*?href="([^"]+)"',markup,re.S)
            if not match:
                raise RuntimeError('Cannot find original raster URL for '+cid)
            url=html.unescape(match.group(1))
            if url.startswith('//'): url='https:'+url
        original=DATASET/'originals'/filename
        if not original.exists():
            raw,resolved=fetch(url)
            original.write_bytes(raw)
        else:
            raw=original.read_bytes(); resolved=url
        image=Image.open(io.BytesIO(raw)); image.load()
        native_dimensions=list(image.size); native_alpha=alpha_info(image)
        image=image.convert('RGBA' if native_alpha['transparent_pixels']+native_alpha['partial_pixels'] else 'RGB')
        transforms=[]
        if mode=='center_crop':
            w,h=image.size; edge=min(256,w,h)
            box=((w-edge)//2,(h-edge)//2,(w+edge)//2,(h+edge)//2)
            image=image.crop(box); transforms.append({'operation':'prespecified_center_crop','box':list(box),'resampling':'none'})
        elif max(image.size)>320:
            old=image.size; scale=320/max(old)
            size=(round(old[0]*scale),round(old[1]*scale))
            image=image.resize(size,Image.Resampling.LANCZOS)
            transforms.append({'operation':'aspect_preserving_resize','from':list(old),'to':list(size),'resampling':'Pillow LANCZOS; premultiplied RGBA internally'})
        out=INPUTS/(cid+'.png'); image.save(out)
        cases.append({'id':cid,'file':out.name,'domains':domains,'source_url':source,'download_url':url,'resolved_download_url':resolved,'license':license_name,'license_url':{'CC0':'https://creativecommons.org/publicdomain/zero/1.0/','CC-BY-SA-3.0':'https://creativecommons.org/licenses/by-sa/3.0/'}.get(license_name,source),'author':author,'accessed_at_utc':stamp,'original_file':str(original.relative_to(ROOT)).replace('\\','/'),'original_dimensions':native_dimensions,'dimensions':list(image.size),'transforms':transforms,'sha256':digest(out.read_bytes()),'original_sha256':digest(raw),'original_bytes':len(raw),'native_alpha':native_alpha,'normalized_alpha':alpha_info(image),'license_snapshot':str(sourcefile.relative_to(ROOT)).replace('\\','/'),'split':'unseen_by_this_engine_before_this_cycle','linked_source_case':'G02_chelsea' if mode=='center_crop' else None})
        (INPUTS/'manifest.json').write_text(json.dumps({'cases':cases,'status':'ACQUIRING','max_edge':320},indent=2),encoding='utf-8')
        print('READY',cid,list(image.size),native_alpha,flush=True)
    manifest={'cases':cases,'status':'FROZEN_BEFORE_BENCHMARK','frozen_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'selection_policy':'Prespecified cross-domain sources, no score-based filtering; G05 is a correlated center-crop diagnostic, not an independent source. Dice is a published 3D-rendered asset, not a photograph. No new SVG rasterizations. Historical astronaut, brick, A01-A12 and synthetic fixtures excluded.','max_edge':320,'independent_source_images':7,'modifications_license':'Normalized rasters and vector reconstructions inherit original applicable license; attribution retained in this manifest. Logos used for technical comparison, no affiliation implied.'}
    frozen=json.dumps(manifest,indent=2).encode()
    (INPUTS/'manifest.json').write_bytes(frozen)
    (DATASET/'freeze.json').write_text(json.dumps({'manifest_sha256':digest(frozen),'frozen_at_utc':manifest['frozen_at_utc'],'case_count':len(cases)},indent=2))

if __name__=='__main__':
    main()
# END CHANGE AGD-GENERALIZATION-DATA | 2026-10-27T11:09:10Z | CREATED
