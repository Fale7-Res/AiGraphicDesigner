# START CHANGE VTRACER-RENDER-CHECK | 2026-10-25T04:45:58Z | CREATED | Author: parent
"""Independent renderer and native 4x geometry inspection on two declared cases."""
from pathlib import Path
import sys,json,time
import cairosvg
from evaluate import load_rgb,render_svg,compare
ROOT=Path(__file__).resolve().parents[1]
def check():
    output=ROOT/'renderer_check';output.mkdir(exist_ok=True);records={}
    for case in ['A03_burger_layers','A09_arabic_calligraphy']:
        directory=output/case;directory.mkdir(exist_ok=True);source=load_rgb(ROOT/'inputs'/f'{case}.png');h,w=source.shape[:2]
        svg=ROOT/'results'/case/'best.svg';png=directory/'cairo_native.png';start=time.perf_counter()
        cairosvg.svg2png(url=str(svg),write_to=str(png),output_width=w,output_height=h)
        cairo=load_rgb(png);native=load_rgb(ROOT/'results'/case/'best.png')
        records[case]={'renderer':'CairoSVG '+cairosvg.__version__,'wall_seconds':time.perf_counter()-start,'versus_inkscape':compare(native,cairo),'versus_source':compare(source,cairo)}
        render_svg(svg,directory/'inkscape_native400.png',w*4,h*4)
    (output/'results.json').write_text(json.dumps(records,indent=2));print(json.dumps(records,indent=2))
if __name__=='__main__':check()

# END CHANGE VTRACER-RENDER-CHECK | 2026-10-25T04:45:58Z | CREATED | Author: parent
