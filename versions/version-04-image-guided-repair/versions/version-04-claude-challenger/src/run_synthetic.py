"""Generate a known-geometry source and run a first-pass vector rendering smoke test."""
from pathlib import Path
import json, sys, time
import numpy as np
from PIL import Image,ImageDraw,ImageFilter
HERE=Path(__file__).resolve();V4=HERE.parents[1];ROOT=HERE.parents[3]
sys.path.insert(0,str(V4))
from src.challenger import Challenger,Config,render_svg
from src.run_benchmark import metrics,load_rgb,OUT

def make_source(w=320,h=240):
    y=np.linspace(0,1,h)[:,None,None]
    top=np.array([246,242,232],dtype=float)[None,None,:];bot=np.array([220,219,214],dtype=float)[None,None,:]
    arr=np.broadcast_to(top*(1-y)+bot*y,(h,w,3)).copy().astype('uint8')
    im=Image.fromarray(arr,'RGB')
    # Soft pre-composited cast shadow.
    shade=Image.new('RGBA',(w,h),(0,0,0,0));d=ImageDraw.Draw(shade);d.ellipse((68,180,263,222),fill=(28,22,10,105));shade=shade.filter(ImageFilter.GaussianBlur(7))
    im=Image.alpha_composite(im.convert('RGBA'),shade).convert('RGB')
    d=ImageDraw.Draw(im)
    shield=[(160,25),(235,52),(225,136),(160,190),(95,136),(85,52)]
    d.polygon(shield,fill=(177,112,31),outline=(255,222,135),width=3)
    inner=[(160,38),(222,59),(214,128),(160,171),(106,128),(98,59)]
    d.polygon(inner,fill=(145,17,28),outline=(255,196,73),width=3)
    # Soft highlight region is layered as a smooth polygon in the synthetic ground truth.
    highlight=Image.new('RGBA',(w,h),(0,0,0,0));hd=ImageDraw.Draw(highlight);hd.ellipse((157,47,216,125),fill=(255,95,82,110));highlight=highlight.filter(ImageFilter.GaussianBlur(9));im=Image.alpha_composite(im.convert('RGBA'),highlight).convert('RGB')
    d=ImageDraw.Draw(im)
    crown=[(113,119),(129,76),(149,103),(160,59),(174,104),(197,77),(209,120),(196,136),(124,136)]
    d.polygon(crown,fill=(255,198,71),outline=(92,55,13),width=3)
    d.arc((121,112,200,147),start=0,end=180,fill=(255,236,169),width=4)
    d.ellipse((72,35,79,42),fill=(244,183,62));d.ellipse((240,159,247,166),fill=(230,88,52))
    return im

def main():
    dest=OUT/'synthetic';dest.mkdir(parents=True,exist_ok=True)
    src=make_source();sp=dest/'S00_known_geometry_source.png';src.save(sp)
    # Keep this synthetic test intentionally small and deterministic.
    cfg=Config(target_regions=220)
    t=time.perf_counter();svg,info=Challenger(cfg).vectorize(np.asarray(src));gen=(time.perf_counter()-t)*1000
    svgp=dest/'S00_known_geometry_v04.svg';pngp=dest/'S00_known_geometry_v04_rendered.png';svgp.write_text(svg,encoding='utf-8')
    rt=render_svg(svgp,pngp,src.width,src.height)
    result={'test':'known geometry with nested shield layers, color highlights, ring-like details and a pre-composited soft shadow','source_dimensions':[src.width,src.height],'generation_ms':gen,'render_ms':rt,**info,**metrics(np.asarray(src),load_rgb(pngp)),'embedded_raster_images':0,'limitations':['single foreground clip is not semantic object decomposition','source contains a pre-composited shadow so this does not test independent shadow-layer recovery']}
    (dest/'S00_known_geometry_metrics.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
