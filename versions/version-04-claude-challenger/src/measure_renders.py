"""Measure fresh, paired Inkscape render times for already-generated SVGs.

Uses a separate output directory so benchmark PNGs remain untouched. Re-run with
--ids to measure chunks; results are merged into render_performance.csv.
"""
from pathlib import Path
import argparse, csv, json, re, shutil, sys
HERE=Path(__file__).resolve(); VERSION_DIR=HERE.parents[1]; ROOT=HERE.parents[3]
sys.path.insert(0,str(VERSION_DIR))
from src.challenger import rasterize_svg
from src.run_benchmark import SRC_DIR,V01_SVG_DIR,OUT,load_rgb

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--ids',default='A01,A02,A03,A04,A05,A06,A07,A08,A09,A10,A11,A12')
    ap.add_argument('--inkscape',default='inkscape')
    args=ap.parse_args()
    if shutil.which(args.inkscape) is None and not Path(args.inkscape).exists(): raise SystemExit('Inkscape not found')
    target=OUT/'metrics'/'render_performance.csv'; target.parent.mkdir(parents=True,exist_ok=True)
    existing={}
    if target.exists():
        with target.open(newline='',encoding='utf-8') as f:
            for r in csv.DictReader(f): existing[r['image_id']]=r
    base=OUT/'rendered'/'performance_v01'; new=OUT/'rendered'/'performance_v04'
    base.mkdir(parents=True,exist_ok=True); new.mkdir(parents=True,exist_ok=True)
    for aid in [x.strip() for x in args.ids.split(',') if x.strip()]:
        src_path=next((p for p in SRC_DIR.glob(f'{aid}_*.png')),None)
        if src_path is None: raise FileNotFoundError(f'No source for {aid}')
        src=load_rgb(src_path); h,w=src.shape[:2]
        v01=V01_SVG_DIR/f'{aid}_v01_vector.svg'
        v04=next(OUT.joinpath('outputs').glob(f'{aid}_*_v04.svg'))
        t0=rasterize_svg(v01,base/f'{aid}_v01.png',w,h,args.inkscape)
        t1=rasterize_svg(v04,new/f'{aid}_v04.png',w,h,args.inkscape)
        existing[aid]={'image_id':aid,'width':w,'height':h,'renderer':'Inkscape CLI','v01_render_ms':round(t0,3),'v04_render_ms':round(t1,3),'v01_svg_bytes':v01.stat().st_size,'v04_svg_bytes':v04.stat().st_size}
        rows=[existing[k] for k in sorted(existing)]
        with target.open('w',newline='',encoding='utf-8') as f:
            writer=csv.DictWriter(f,fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
        print(f'{aid}: V01 {t0:.1f} ms, V04 hybrid {t1:.1f} ms',flush=True)
if __name__=='__main__':main()
