# START CHANGE AGD-THIN-CROWN-REVIEW | 2026-10-29T11:45:56Z | CREATED | Author: root
from pathlib import Path
import sys,json,datetime,shutil,re,hashlib,importlib.util
from PIL import Image,ImageDraw
r=Path(__file__).resolve().parent;repo=r.parents[1];sys.path.insert(0,str(r));sys.dont_write_bytecode=True
from study import destination,PREVIOUS
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
p=r/'REPRODUCIBILITY.md';p.write_text(p.read_text(encoding='utf-8').replace('EXP_COMPLETE_GEOMETRY_ISOLATION_01/REPRODUCIBILITY.md','EXP_COMPLETE_GEOMETRY_ISOLATION_01/REPRODUCE.md'),encoding='utf-8')
# QA report is supplied separately; no automatic QA fabrication.
out=destination('A01_shield');im=Image.open(out/'working.png').convert('RGB');ref=json.loads((PREVIOUS/'references/shield_complete_boundary_reference.json').read_text(encoding='utf-8'))
overlay=im.copy();draw=ImageDraw.Draw(overlay)
for c in ref['components']:
 if c['id'].startswith('crown'):
  for line in c['polylines']:draw.line([tuple(p) for p in line],fill='#00ffff',width=1)
box=(118,65,254,165)
im.crop(box).resize((544,400),Image.Resampling.NEAREST).save(out/'crown_source_pixels_4x.png')
overlay.crop(box).resize((544,400),Image.Resampling.NEAREST).save(out/'crown_uncertain_reference_4x.png')
sheet=Image.new('RGB',(1088,850),'white');d=ImageDraw.Draw(sheet)
items=[('Source raster pixels (not high-res contour truth)',out/'crown_source_pixels_4x.png'),('Inherited uncertain evaluator guides',out/'crown_uncertain_reference_4x.png'),('Baseline actual SVG render at4x',out/'baseline_review_4x.png'),('B actual SVG render at4x: unchanged',out/'B_review_4x.png')]
for i,(label,path) in enumerate(items):
 x=(i%2)*544;y=(i//2)*425;d.text((x+4,y+4),label,fill='black');pic=Image.open(path).convert('RGBA');bg=Image.new('RGBA',pic.size,'white');bg.alpha_composite(pic);sheet.paste(bg.convert('RGB'),(x,y+25))
sheet.save(out/'crown_comparison.png')
p=r/'index.html';html=p.read_text(encoding='utf-8');html=html.replace('<p>Dedicated complete crown comparison.', '<div class="grid"><figure><img src="results/A01_shield/crown_comparison.png"><figcaption>Source and evaluator guides above; actual SVG renders below. No improved crown is demonstrated.</figcaption></figure></div><p>Dedicated complete crown comparison.')
p.write_text(html,encoding='utf-8')

# END CHANGE AGD-THIN-CROWN-REVIEW | 2026-10-29T11:45:56Z | CREATED | Author: root
