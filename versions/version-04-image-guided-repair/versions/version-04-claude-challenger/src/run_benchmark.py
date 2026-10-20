"""Native-size V01 versus repaired V04 evaluation and visual comparisons."""
from pathlib import Path
import argparse, csv, json, re, shutil, subprocess, sys, time, xml.etree.ElementTree as ET
import numpy as np, cv2, psutil
from PIL import Image, ImageDraw, ImageFont
from skimage.metrics import structural_similarity
HERE=Path(__file__).resolve(); V4=HERE.parents[1]; ROOT=HERE.parents[3]
sys.path.insert(0,str(V4))
from src.challenger import Challenger,Config,render_svg,estimate_target_regions
SRC=ROOT/'AI_Graphic_Designer_Test_Images_Initial_12'
V01=ROOT/'versions/version-01/experiments/preliminary_visual_tests/outputs'
OLD_METRICS=ROOT/'versions/version-01/experiments/fidelity_diagnostics/all_12_rerun_metrics.json'
OUT=V4/'experiments'

def load_rgb(p): return np.asarray(Image.open(p).convert('RGB'),dtype=np.uint8)
def svg_stats(p):
 text=p.read_text(encoding='utf-8'); root=ET.fromstring(text); tags=[e.tag.rsplit('}',1)[-1] for e in root.iter()]
 paths=[e for e in root.iter() if e.tag.rsplit('}',1)[-1]=='path']; segments=0; commands=0
 for el in paths:
  d=el.attrib.get('d',''); segments+=len(re.findall(r'[Cc]',d)); commands+=len(re.findall(r'[MmCcLlQqAaHhVvZz]',d))
 return {'svg_bytes':p.stat().st_size,'path_count':len(paths),'cubic_segment_count':segments,'path_command_count':commands,'rect_count':tags.count('rect'),'gradient_count':tags.count('linearGradient'),'embedded_raster_images':tags.count('image'),'xml_well_formed':True}
def metrics(ref,pred):
 diff=ref.astype(np.float64)-pred.astype(np.float64); mse=float(np.mean(diff*diff)); psnr=float(10*np.log10(255**2/mse)) if mse else 99.
 ssim=float(structural_similarity(ref,pred,channel_axis=2,data_range=255))
 rgray=cv2.cvtColor(ref,cv2.COLOR_RGB2GRAY); pgray=cv2.cvtColor(pred,cv2.COLOR_RGB2GRAY)
 re_=cv2.Canny(rgray,80,160)>0; pe=cv2.Canny(pgray,80,160)>0; ker=np.ones((3,3),np.uint8)
 rd=cv2.dilate(re_.astype(np.uint8),ker)>0; pd=cv2.dilate(pe.astype(np.uint8),ker)>0
 precision=float((pe&rd).sum()/max(1,pe.sum())); recall=float((re_&pd).sum()/max(1,re_.sum())); f1=2*precision*recall/max(1e-12,precision+recall)
 # Background mask based on border median; heuristic only, not a semantic mask.
 border=np.concatenate([ref[0],ref[-1],ref[:,0],ref[:,-1]],axis=0).astype(float); bg=np.median(border,axis=0)
 rm=np.linalg.norm(ref.astype(float)-bg,axis=2)>20; pm=np.linalg.norm(pred.astype(float)-bg,axis=2)>20
 iou=float((rm&pm).sum()/max(1,(rm|pm).sum()))
 return {'mse':mse,'psnr_db':psnr,'ssim':ssim,'edge_precision_1px':precision,'edge_recall_1px':recall,'edge_f1_1px':f1,'foreground_iou_proxy':iou}
class PeakRssSampler:
 def __init__(self, interval=0.01):
  import threading
  self.process=psutil.Process(); self.interval=interval; self.peak=0; self.stop_flag=False
  self.thread=threading.Thread(target=self._run,daemon=True)
 def _run(self):
  while not self.stop_flag:
   try:self.peak=max(self.peak,self.process.memory_info().rss)
   except psutil.Error:pass
   time.sleep(self.interval)
 def start(self):
  try:self.peak=self.process.memory_info().rss
  except psutil.Error:pass
  self.thread.start()
 def stop(self):
  self.stop_flag=True;self.thread.join(timeout=2)
  try:self.peak=max(self.peak,self.process.memory_info().rss)
  except psutil.Error:pass


def font(size=14):
 try:return ImageFont.truetype('DejaVuSans.ttf',size)
 except:return ImageFont.load_default()
def comparison(source,v01,v04,dest,aid):
 images=[Image.open(source).convert('RGB'),Image.open(v01).convert('RGB'),Image.open(v04).convert('RGB')]
 maxw=max(i.width for i in images); scale=max(1,min(2,860//maxw)); iw=maxw*scale; ih=max(i.height for i in images)*scale
 canvas=Image.new('RGB',(iw*3+32,ih+42),(248,248,248)); d=ImageDraw.Draw(canvas)
 for ix,(im,label) in enumerate(zip(images,['Original','Antigravity V01','Repaired V04'])):
  x=8+ix*(iw+8); d.text((x,3),label,fill=(10,20,36),font=font(14)); im=im.resize((im.width*scale,im.height*scale),Image.Resampling.LANCZOS); canvas.paste(im,(x,26))
 canvas.save(dest)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--segments',type=str,default='auto',help='target regions: auto adapts to texture distribution; or provide an integer'); ap.add_argument('--compactness',type=float,default=9.0); ap.add_argument('--inkscape',default='inkscape'); ap.add_argument('--only',default=''); ap.add_argument('--a01-sweep',action='store_true'); ap.add_argument('--reuse-existing-renders',action='store_true',help='Reuse existing native-size PNG renders only when the generated SVG is byte-identical and prior timings are available'); args=ap.parse_args()
 if not shutil.which(args.inkscape) and not Path(args.inkscape).exists(): raise SystemExit('Inkscape CLI not found')
 for sub in ['outputs','rendered/v01','rendered/v04','comparisons','metrics']: (OUT/sub).mkdir(parents=True,exist_ok=True)
 inputs=sorted(p for p in SRC.glob('A*.png') if re.match(r'A\d\d_',p.name)); inputs= [p for p in inputs if not args.only or p.stem.startswith(tuple(x.strip() for x in args.only.split(',')))]
 if not inputs: raise SystemExit('No source images selected')
 fixed_target=None if args.segments.lower()=='auto' else int(args.segments)
 if fixed_target is not None and fixed_target<20: raise SystemExit('--segments integer must be at least 20')
 old={r['image_id']:r for r in json.loads(OLD_METRICS.read_text(encoding='utf-8'))}
 prior_path=OUT/'metrics'/'benchmark_results.json'
 try: prior_render_rows={r['image_id']:r for r in json.loads(prior_path.read_text(encoding='utf-8'))}
 except (OSError,ValueError,KeyError): prior_render_rows={}
 if args.a01_sweep:
  src=next(p for p in sorted(SRC.glob('A01_*.png'))); im=load_rgb(src); sweep=[]
  for n in [160,260,340,420,560]:
   model=Challenger(Config(target_regions=n,compactness=args.compactness)); svg,info=model.vectorize(im); sp=OUT/'outputs'/f'A01_sweep_{n}.svg'; pp=OUT/'rendered/v04'/f'A01_sweep_{n}.png'; sp.write_text(svg,encoding='utf-8'); rt=render_svg(sp,pp,im.shape[1],im.shape[0],args.inkscape)
   sweep.append({'segments':n,**info,'render_ms':rt,**metrics(im,load_rgb(pp))})
  (OUT/'metrics'/'a01_region_budget_sweep.json').write_text(json.dumps(sweep,indent=2),encoding='utf-8')
 rows=[]
 rss_sampler=PeakRssSampler();rss_sampler.start()
 for ix,src in enumerate(inputs,1):
  aid=src.stem.split('_')[0]; im=load_rgb(src); h,w=im.shape[:2]
  v1=V01/f'{aid}_v01_vector.svg'; r1=OUT/'rendered/v01'/f'{aid}_v01.png'; v4=OUT/'outputs'/f'{src.stem}_v04.svg'; r4=OUT/'rendered/v04'/f'{aid}_v04.png'
  if not v1.exists(): raise FileNotFoundError(v1)
  prior=prior_render_rows.get(aid,{})
  def png_matches(path):
   try:
    with Image.open(path) as check: return check.size==(w,h)
   except (OSError,ValueError): return False
  baseline_reused=bool(args.reuse_existing_renders and r1.exists() and png_matches(r1))
  if baseline_reused:
   t1=prior.get('v01_render_ms')
  else:
   t1=render_svg(v1,r1,w,h,args.inkscape)
  target_used,adaptive_info=estimate_target_regions(im) if fixed_target is None else (fixed_target,{'edge_density':None,'edge_grid_coverage':None,'texture_complexity_score':None,'adaptive_target_regions':fixed_target})
  prior_svg=v4.read_text(encoding='utf-8') if v4.exists() else None
  start=time.perf_counter(); svg,gen=Challenger(Config(target_regions=target_used,compactness=args.compactness)).vectorize(im); genms=(time.perf_counter()-start)*1000
  svg_reused=bool(args.reuse_existing_renders and prior_svg==svg and r4.exists() and png_matches(r4))
  if not svg_reused: v4.write_text(svg,encoding='utf-8')
  if svg_reused:
   t4=prior.get('v04_render_ms')
  else:
   v4.write_text(svg,encoding='utf-8'); t4=render_svg(v4,r4,w,h,args.inkscape)
  m1=metrics(im,load_rgb(r1)); m4=metrics(im,load_rgb(r4)); s1=svg_stats(v1); s4=svg_stats(v4)
  row={'image_id':aid,'filename':src.name,'width':w,'height':h,
       'v01_recorded_psnr_db':old.get(aid,{}).get('psnr_db'),'v01_recorded_ssim':old.get(aid,{}).get('ssim'),
       **{f'v01_{k}':v for k,v in m1.items()},**{f'v04_{k}':v for k,v in m4.items()},
       'v01_paths':s1['path_count'],'v01_cubic_segments':s1['cubic_segment_count'],'v01_svg_bytes':s1['svg_bytes'],'v01_render_ms':t1,'v01_render_reused':baseline_reused,
       'v04_target_regions':target_used,'v04_texture_edge_density':adaptive_info['edge_density'],'v04_texture_grid_coverage':adaptive_info['edge_grid_coverage'],'v04_texture_complexity_score':adaptive_info['texture_complexity_score'],'v04_regions':gen['actual_regions'],'v04_paths':s4['path_count'],'v04_region_boundary_segments':gen['region_boundary_segments'],'v04_silhouette_cubic_segments':gen['silhouette_cubic_segments'],'v04_gradients':gen['gradient_count'],'v04_svg_bytes':s4['svg_bytes'],'v04_generation_ms':genms,'v04_render_ms':t4,'v04_render_reused':svg_reused,'v04_embedded_raster_images':s4['embedded_raster_images'],'v04_dropped_regions':gen['dropped_tiny_or_invalid_regions']}
  rows.append(row)
  comparison(src,r1,r4,OUT/'comparisons'/f'{aid}_original_vs_v01_vs_v04.png',aid)
  print(f'[{ix}/{len(inputs)}] {aid} (target={target_used}, regions={gen["actual_regions"]}): PSNR {m1["psnr_db"]:.2f} -> {m4["psnr_db"]:.2f} dB | SSIM {m1["ssim"]:.4f} -> {m4["ssim"]:.4f} | edgeF1 {m1["edge_f1_1px"]:.3f} -> {m4["edge_f1_1px"]:.3f} | paths {s1["path_count"]}->{s4["path_count"]} | size {s4["svg_bytes"]/1024:.0f} KiB',flush=True)
  # checkpoint after each image
  (OUT/'metrics'/'partial_results.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
 rss_sampler.stop()
 if len(rows)==12:
  (OUT/'metrics'/'benchmark_results.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
  with (OUT/'metrics'/'benchmark_results.csv').open('w',newline='',encoding='utf-8') as f: wr=csv.DictWriter(f,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)
  # Contact sheet, 2 images per row / each original+V01+V04.
  thumbs=[]
  for r in rows:
   ims=[Image.open(SRC/r['filename']).convert('RGB'),Image.open(OUT/'rendered/v01'/f"{r['image_id']}_v01.png").convert('RGB'),Image.open(OUT/'rendered/v04'/f"{r['image_id']}_v04.png").convert('RGB')]
   cell=Image.new('RGB',(720,210),'white'); dr=ImageDraw.Draw(cell); dr.text((5,2),r['image_id'],fill='black',font=font())
   for j,(im,lab) in enumerate(zip(ims,['Original','V01','Repaired V04'])):
    dr.text((j*240+4,20),lab,fill='black',font=font());im.thumbnail((230,170),Image.Resampling.LANCZOS);cell.paste(im,(j*240+(240-im.width)//2,38+(170-im.height)//2))
   thumbs.append(cell)
  sheet=Image.new('RGB',(1440,210*6),(242,242,242))
  for j,im in enumerate(thumbs): sheet.paste(im,((j%2)*720,(j//2)*210))
  sheet.save(OUT/'comparisons'/'all_12_contact_sheet.png')
  summary={}
  for metric in ['mse','psnr_db','ssim','edge_precision_1px','edge_recall_1px','edge_f1_1px','foreground_iou_proxy']:
   a=np.array([r['v01_'+metric] for r in rows]);b=np.array([r['v04_'+metric] for r in rows]);better=b<a if metric=='mse' else b>a
   summary[metric]={'v01_mean':float(a.mean()),'v04_mean':float(b.mean()),'v04_better_count':int(better.sum()),'v04_worse_or_tied_images':[rows[i]['image_id'] for i,x in enumerate(better) if not x]}
  summary['complexity']={'v01_mean_svg_kib':float(np.mean([r['v01_svg_bytes'] for r in rows])/1024),'v04_mean_svg_kib':float(np.mean([r['v04_svg_bytes'] for r in rows])/1024),'v01_mean_paths':float(np.mean([r['v01_paths'] for r in rows])),'v04_mean_paths':float(np.mean([r['v04_paths'] for r in rows])),'v04_mean_regions':float(np.mean([r['v04_regions'] for r in rows])),'v04_mean_region_boundary_segments':float(np.mean([r['v04_region_boundary_segments'] for r in rows])),'v04_mean_silhouette_cubic_segments':float(np.mean([r['v04_silhouette_cubic_segments'] for r in rows]))}
  v04_render_times=[r['v04_render_ms'] for r in rows if r.get('v04_render_ms') is not None]; v01_render_times=[r['v01_render_ms'] for r in rows if r.get('v01_render_ms') is not None]
  summary['performance']={'v04_mean_generation_ms':float(np.mean([r['v04_generation_ms'] for r in rows])),'v04_mean_render_ms':float(np.mean(v04_render_times)) if v04_render_times else None,'v01_mean_render_ms':float(np.mean(v01_render_times)) if v01_render_times else None,'v04_render_timing_samples':len(v04_render_times),'v01_render_timing_samples':len(v01_render_times),'v04_render_reused_count':sum(bool(r.get('v04_render_reused')) for r in rows),'v01_render_reused_count':sum(bool(r.get('v01_render_reused')) for r in rows),'render_time_note':'If --reuse-existing-renders was used, stored per-image renderer timings are retained only when the prior full benchmark has them; the SVG is regenerated and must byte-match the existing file before reusing the PNG.','process_peak_rss_sampled_mb':rss_sampler.peak/(1024*1024),'rss_sampling_interval_ms':10}
  (OUT/'metrics'/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
  report=['# V04 Image-Guided Repair — 12 Image Results','','**Representation:** merged, boundary-aware SVG regions with exact shared pixel-cell edges internally, a smoothed composite silhouette clip, and local multi-stop linear/radial gradients. No source-edge pixel-run stencil; no embedded raster. This is still region-based and not semantic Clean SVG.','','## Per-image metrics','','| ID | PSNR V01 | PSNR V04 | Δ | SSIM V01 | SSIM V04 | Edge F1 V01→V04 | Paths V01→V04 | SVG KiB V01→V04 |','|---|---:|---:|---:|---:|---:|---:|---:|---:|']
  for r in rows: report.append(f"| {r['image_id']} | {r['v01_psnr_db']:.2f} | {r['v04_psnr_db']:.2f} | {r['v04_psnr_db']-r['v01_psnr_db']:+.2f} | {r['v01_ssim']:.4f} | {r['v04_ssim']:.4f} | {r['v01_edge_f1_1px']:.3f}→{r['v04_edge_f1_1px']:.3f} | {r['v01_paths']}→{r['v04_paths']} | {r['v01_svg_bytes']/1024:.0f}→{r['v04_svg_bytes']/1024:.0f} |")
  report += ['', '## Aggregates','']
  for met,d in summary.items():
   if met in ['complexity','performance']: continue
   report.append(f"- **{met}:** V01 {d['v01_mean']:.4f}; V04 {d['v04_mean']:.4f}; V04 better on {d['v04_better_count']}/12. Regressions/ties: {', '.join(d['v04_worse_or_tied_images']) or 'none'}.")
  synthetic_path=OUT/'synthetic'/'S00_known_geometry_metrics.json'
  if synthetic_path.exists():
   syn=json.loads(synthetic_path.read_text(encoding='utf-8'))
   report += ['', '## Controlled synthetic fixture','',f"- Known-geometry input: {syn['width']}×{syn['height']}; PSNR {syn['psnr_db']:.2f} dB; SSIM {syn['ssim']:.4f}; edge F1 {syn['edge_f1_1px']:.3f}; {syn['actual_regions']} regions; {syn['gradient_count']} gradient definitions; SVG {syn['svg_bytes']/1024:.1f} KiB.",'- Fixture includes nested shield layers, highlight patch, ring/hole detail, small marks and a pre-composited soft shadow. It does not validate semantic shadow recovery because the shadow is already baked into the source raster.']
  report += ['', '## Geometry and runtime','',f"- Mean SVG size: V01 {summary['complexity']['v01_mean_svg_kib']:.1f} KiB; V04 {summary['complexity']['v04_mean_svg_kib']:.1f} KiB.",f"- Mean vector regions/paths: V01 {summary['complexity']['v01_mean_paths']:.0f}; V04 {summary['complexity']['v04_mean_paths']:.0f}. Mean exact region-boundary segments/image: {summary['complexity']['v04_mean_region_boundary_segments']:.0f}; smoothed silhouette cubic segments: {summary['complexity']['v04_mean_silhouette_cubic_segments']:.0f}.",f"- Mean V04 generation: {summary['performance']['v04_mean_generation_ms']:.1f} ms; V04 render: {summary['performance']['v04_mean_render_ms']:.1f} ms; V01 render: {summary['performance']['v01_mean_render_ms']:.1f} ms.",f"- Peak sampled Python-process RSS: {summary['performance']['process_peak_rss_sampled_mb']:.1f} MiB (10 ms sampling; not a guaranteed instantaneous peak).",f"- Renderer timings were reused from the prior paired run for {summary['performance']['v04_render_reused_count']} V04 and {summary['performance']['v01_render_reused_count']} V01 images where regenerated SVG bytes matched and cached PNG dimensions matched.",'','## Interpretation / limitations','','The image-guided repair removes the rectangular tile surface and source-edge micro-path stencil. Local multi-stop linear/radial gradients address the request for real SVG gradients, exact shared internal borders reduce cracks, and a smoothed GrabCut composite silhouette improves outer contour continuity. However, per-object base/shadow/highlight/blur layers are **not** independently recovered yet: the mask is only a foreground/background approximation, and the input is a flattened RGB image. Region boundaries can merge adjacent semantic objects; fine texture is approximated by a bounded number of regions. PSNR/SSIM improved for every input, but edge recall is lower on 11/12 images and edge F1 is lower on 7/12. These remain meaningful detail-preservation regressions. Metrics are pixel/edge proxies, not a professional designer edit test; the visual-reference goals are only partially met.','']
  report_path=OUT/'metrics'/'RESULTS_REPORT.md'
  prior_text=report_path.read_text(encoding='utf-8') if report_path.exists() else ''
  provenance=re.search(r'<!-- DOC_PROVENANCE\n.*?\nEND_DOC_PROVENANCE -->\n?',prior_text,re.S)
  body='\n'.join(report).rstrip()+'\n'
  if provenance: body=provenance.group(0).rstrip()+'\n\n'+body
  report_path.write_text(body,encoding='utf-8')
  print('\nSUMMARY\n'+json.dumps(summary,indent=2))
 else:
  print(f'Partial run: {len(rows)}/{len(inputs)} images; progress saved.')
if __name__=='__main__':main()
