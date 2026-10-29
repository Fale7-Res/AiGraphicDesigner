# START CHANGE AGD-ISOLATION-MAKE-OVERLAYS | 2026-10-29T07:02:00Z | CREATED | Author: root
"""Diagnostic actual-SVG raw/fit overlays; no reconstruction is performed."""
import os,sys,json,copy
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from isolation import ROOT,WORK,CASES,case_dir
sys.path.insert(0,str(WORK/'geometry-deps'))
import numpy as np
from PIL import Image,ImageChops,ImageEnhance
from xml.etree import ElementTree as ET
from geometry_eval import svg_graph
from analyze_matrix import render,ZOOMS

for case in CASES:
    out=case_dir(case)
    for seg in ['S_A','S_V']:
        for f in ['F_A','F_V']:
            name=seg+'_'+f;g=json.loads((out/(name+'.json')).read_text())
            raw=ET.fromstring(svg_graph(g,raw=True));fit=ET.fromstring(svg_graph(g))
            for tree,color in [(raw,'#ed3153'),(fit,'#00a6ba')]:
                for node in tree:node.set('stroke',color);node.set('stroke-width','.55')
            combined=copy.deepcopy(raw)
            for node in fit:combined.append(copy.deepcopy(node))
            svg=out/(name+'_raw_fit_overlay.svg');svg.write_text(ET.tostring(combined,encoding='unicode'),encoding='utf-8')
            lines=out/(name+'_raw_fit_lines.png');render(svg,lines)
            source=Image.open(out/'working.png').convert('RGBA');source.alpha_composite(Image.open(lines).convert('RGBA'));source.convert('RGB').save(out/(name+'_source_overlay.png'))
            a=Image.open(out/(name+'_raw.png')).convert('RGBA');b=Image.open(out/(name+'_curves.png')).convert('RGBA')
            # Native-render alpha difference is a visualization, not a source
            # geometry ground-truth score or photometric reconstruction metric.
            d=ImageChops.difference(a.getchannel('A'),b.getchannel('A'));d=ImageEnhance.Brightness(d).enhance(4)
            Image.merge('RGB',(d,Image.new('L',d.size,0),Image.new('L',d.size,0))).save(out/(name+'_render_difference_x4.png'))
    print(case,'diagnostic overlays ready',flush=True)

# END CHANGE AGD-ISOLATION-MAKE-OVERLAYS | 2026-10-29T07:02:00Z | CREATED | Author: root
