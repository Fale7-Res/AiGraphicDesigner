# مرآة الكود التفصيلية للإصدار: `version-04-claude-challenger/src/finalize_metrics.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED VERSION MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `versions/version-04-claude-challenger/src/finalize_metrics.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)** لهذا الإصدار. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py --version version-04-claude-challenger`.

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `src/finalize_metrics.py`
- **الإصدار المعماري (`Architecture Version`):** `version-04-claude-challenger`
- **إجمالي عدد الأسطر (`Total Lines`):** `245` (`Lines 1–245`)
- **بصمة الملف (`SHA-256`):** `3a5dd8a53cd64edfc9da913eefddcd2d25fe5b1e260f0f71cf71a124504b33b1`
- **الوصف:** موديول برمجي تنفيذي ضمن معمارية الإصدار `version-04-claude-challenger`.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **حوكمة الإصدار الأب (`Parent Version`)** | `version-04-claude-challenger` | يتبع مواصفة معمارية هذا الإصدار | مراجعة تكامل الإصدار عند التعديل. |
| **الحوكمة المركزية (`Global Governance`)** | `AGENTS.md` | يخضع للدستور وقواعد منع التكرار المشتركة | التحقق الحوكمي الإلزامي. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `Sampler` | `class` | `Lines 18–33` | `class Sampler:` | Sample this Python process RSS every 10ms; not a system-wide peak. |
| `Sampler.__init__` | `method` | `Lines 20–21` | `def __init__(self):` | رمز برمجي موثق للإصدار. |
| `Sampler._loop` | `method` | `Lines 22–26` | `def _loop(self):` | رمز برمجي موثق للإصدار. |
| `Sampler.__enter__` | `method` | `Lines 27–29` | `def __enter__(self):` | رمز برمجي موثق للإصدار. |
| `Sampler.__exit__` | `method` | `Lines 30–33` | `def __exit__(self, *args):` | رمز برمجي موثق للإصدار. |
| `mean` | `function` | `Lines 36–38` | `def mean(rows, key):` | رمز برمجي موثق للإصدار. |
| `write_report` | `function` | `Lines 41–107` | `def write_report(rows, summary):` | رمز برمجي موثق للإصدار. |
| `save_progress` | `function` | `Lines 110–116` | `def save_progress(rows):` | Durable per-image checkpoint so one slow SVG does not lose completed work. |
| `main` | `function` | `Lines 119–243` | `def main():` | رمز برمجي موثق للإصدار. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `Sampler` — `Lines 18–33`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `33` (`Lines 18–33`)
- **الوظيفة:** Sample this Python process RSS every 10ms; not a system-wide peak.
- **الكود الفعلي (`Lines 18–33`):**
```python
class Sampler:
    """Sample this Python process RSS every 10ms; not a system-wide peak."""
    def __init__(self):
        self.proc = psutil.Process(os.getpid()); self.peak = 0; self.stop = False
    def _loop(self):
        while not self.stop:
            try: self.peak = max(self.peak, self.proc.memory_info().rss)
            except psutil.Error: pass
            time.sleep(.01)
    def __enter__(self):
        self.peak = self.proc.memory_info().rss
        self.thread = threading.Thread(target=self._loop, daemon=True); self.thread.start(); return self
    def __exit__(self, *args):
        self.stop = True; self.thread.join(2)
        try: self.peak = max(self.peak, self.proc.memory_info().rss)
        except psutil.Error: pass
```

### `Sampler.__init__` — `Lines 20–21`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `20` إلى السطر `21` (`Lines 20–21`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 20–21`):**
```python
    def __init__(self):
        self.proc = psutil.Process(os.getpid()); self.peak = 0; self.stop = False
```

### `Sampler._loop` — `Lines 22–26`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `22` إلى السطر `26` (`Lines 22–26`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 22–26`):**
```python
    def _loop(self):
        while not self.stop:
            try: self.peak = max(self.peak, self.proc.memory_info().rss)
            except psutil.Error: pass
            time.sleep(.01)
```

### `Sampler.__enter__` — `Lines 27–29`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `27` إلى السطر `29` (`Lines 27–29`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 27–29`):**
```python
    def __enter__(self):
        self.peak = self.proc.memory_info().rss
        self.thread = threading.Thread(target=self._loop, daemon=True); self.thread.start(); return self
```

### `Sampler.__exit__` — `Lines 30–33`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `30` إلى السطر `33` (`Lines 30–33`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 30–33`):**
```python
    def __exit__(self, *args):
        self.stop = True; self.thread.join(2)
        try: self.peak = max(self.peak, self.proc.memory_info().rss)
        except psutil.Error: pass
```

### `mean` — `Lines 36–38`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `36` إلى السطر `38` (`Lines 36–38`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 36–38`):**
```python
def mean(rows, key):
    values = [float(r[key]) for r in rows if r.get(key) is not None and np.isfinite(r[key])]
    return float(np.mean(values)) if values else None
```

### `write_report` — `Lines 41–107`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `41` إلى السطر `107` (`Lines 41–107`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 41–107`):**
```python
def write_report(rows, summary):
    c = summary['comparisons']; x = summary['complexity']; p = summary['performance']
    verification_path=OUT/'metrics'/'verification.json'
    if verification_path.exists():
        try:
            verification=json.loads(verification_path.read_text(encoding='utf-8'))
        except (OSError, json.JSONDecodeError):
            verification={}
    else:
        verification={}
    status_line='**Status:** completed local experimental evaluation; no global approval state modified.'
    if verification.get('all_deterministic_byte_identical') and verification.get('all_svg_xml_well_formed') and verification.get('no_embedded_raster_images') and verification.get('all_render_dimensions_match_source'):
        status_line += ' The independent verifier regenerated all 12 final SVGs byte-identically: **True**; all were XML-well-formed, rendered at input dimensions, and contained zero embedded raster image elements.'
    lines = [
        '# Version 04 Challenger — Benchmark Results', '',
        '**Representation:** hybrid **vector-only** adaptive surface tessellation plus 5-bit/channel source-derived edge-band residual paths. No `<image>` elements / embedded source raster.',
        status_line, '',
        '## Protocol', '',
        'The same 12 supplied PNGs were used at their native dimensions. The consistent Version 01 baseline is `versions/version-01/experiments/preliminary_visual_tests/outputs/A01_v01_vector.svg` through `A12_v01_vector.svg`. Every Version 01 and Version 04 file was rendered with the same local Inkscape CLI to the same width and height. Freshly rendered metrics are the primary comparison; old Version 01 experiment metrics are retained separately for provenance.', '',
        'Version 04 has two stacked vector-only parts: (1) an adaptive rectangular surface tessellation, with selected local linear gradients, and (2) a source-derived correction only along a 1-iteration 3×3-dilated Canny edge band, quantized to 5 bits per RGB channel and merged into horizontal runs within same-color SVG paths. This second component was selected after the pure surface output showed visible staircase/edge losses. It is **not** semantic object reconstruction and should not be described as a clean, professionally layered SVG.', '',
        'The edge residual intentionally refers to source edge pixels, so high edge recall partly reflects a source-driven correction. Its complexity cost is real and must be considered beside metrics.', '',
        '## Per-image results', '',
        '| Image | V01 PSNR | V04 PSNR | Δ PSNR | V01 SSIM | V04 SSIM | Δ SSIM | Edge F1 V01 → V04 | V04 cells | V04 residual paths | V01 SVG KB | V04 SVG KB |',
        '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|' ]
    for r in rows:
        lines.append(f"| {r['image_id']} | {r['v01_fresh_psnr_db']:.2f} | {r['v04_psnr_db']:.2f} | {r['v04_psnr_db']-r['v01_fresh_psnr_db']:+.2f} | {r['v01_fresh_ssim']:.4f} | {r['v04_ssim']:.4f} | {r['v04_ssim']-r['v01_fresh_ssim']:+.4f} | {r['v01_edge_f1_1px']:.3f} → {r['v04_edge_f1_1px']:.3f} | {r['v04_cells']} | {r['v04_edge_residual_color_paths']} | {r['v01_svg_bytes']/1024:.0f} | {r['v04_svg_bytes']/1024:.0f} |")
    # Baseline experiments are recorded separately from the final hybrid 12-image run.
    synth_path=OUT/'synthetic'/'S00_known_geometry_metrics.json'
    synth_hybrid_path=OUT/'synthetic'/'S00_known_geometry_hybrid_metrics.json'
    sweep_path=OUT/'metrics'/'a01_budget_sweep.json'
    lines += ['', '## Controlled experiments before the 12-image run', '']
    if synth_path.exists():
        ss=json.loads(synth_path.read_text(encoding='utf-8'))
        lines.append(f"- **S00 known geometry, surface-only baseline:** {ss['width']}×{ss['height']}, {ss['leaf_cells']} cells, PSNR {ss['psnr_db']:.2f} dB, SSIM {ss['ssim']:.4f}, SVG {ss['svg_bytes']/1024:.0f} KiB. The synthetic source includes nested shapes, highlights, a ring/hole, and a pre-composited soft shadow.")
    if synth_hybrid_path.exists():
        sh=json.loads(synth_hybrid_path.read_text(encoding='utf-8'))
        lines.append(f"- **S00 hybrid edge-band iteration:** PSNR {sh['psnr_db']:.2f} dB, SSIM {sh['ssim']:.4f}, edge F1 {sh['edge_f1_1px']:.3f}, SVG {sh['svg_bytes']/1024:.0f} KiB. This output is explicitly a source-derived hybrid vector representation.")
    if sweep_path.exists():
        sweep=json.loads(sweep_path.read_text(encoding='utf-8'))
        lines += ['', '| A01 surface-only leaf budget | PSNR | SSIM | Edge F1 | SVG KiB | Generation ms | Render ms |', '|---:|---:|---:|---:|---:|---:|---:|']
        for q in sweep:
            lines.append(f"| {q['budget']} | {q['psnr_db']:.2f} | {q['ssim']:.4f} | {q['edge_f1_1px']:.3f} | {q['svg_bytes']/1024:.0f} | {q['generation_ms']:.1f} | {q['render_ms']:.1f} |")
        lines.append('These A01 figures are for the **surface-only** iteration before edge residual paths were added; they are a budget diagnostic, not final hybrid performance.')
    lines += ['', '## Aggregate comparisons', '']
    for metric, rec in c.items():
        lines.append(f"- **{metric}:** V01 mean {rec['v01_mean']:.5f}; V04 mean {rec['v04_mean']:.5f}; V04 better on {rec['v04_better_count']}/{rec['n']} images; worse/tied on {rec['v04_worse_count']}/{rec['n']}." if rec.get('v01_mean') is not None and rec.get('v04_mean') is not None else f"- **{metric}:** insufficient finite measurements.")
        if rec.get('v04_worse_images'):
            lines.append(f"  Images where V04 was worse/tied: {', '.join(rec['v04_worse_images'])}.")
    lines += ['', '## Complexity and performance', '',
        f"- Mean V01 SVG size: {x['v01_mean_svg_bytes']/1024:.1f} KiB; mean V04 SVG size: {x['v04_mean_svg_bytes']/1024:.1f} KiB.",
        f"- Mean V01 path count: {x['v01_mean_paths']:.0f}; mean V04 total paths: {x['v04_mean_paths']:.0f}; mean V04 residual color paths: {x['v04_mean_residual_color_paths']:.0f}.",
        f"- Mean V01 estimated path anchors/control points: {x['v01_mean_estimated_path_anchors_controls']:.0f}; V04 path-command point estimate: {x['v04_mean_path_anchors_controls']:.0f}, plus {x['v04_mean_rectangles']:.0f} rectangles ({x['v04_mean_rectangles']*4:.0f} implicit corners). The V04 estimate excludes implicit SVG rectangle geometry from the path-command point total; rectangles are shown separately.",
        f"- Mean V04 surface-generation plus edge-overlay time: {p['v04_mean_generation_ms']:.1f} ms; median {p['v04_median_generation_ms']:.1f} ms.",
        (f"- Fresh Inkscape render timing (when available): V01 mean {p['v01_mean_inkscape_render_ms']:.1f} ms; V04 mean {p['v04_mean_inkscape_render_ms']:.1f} ms, based on {p.get('fresh_render_timing_images', 0)} images." if p.get('v01_mean_inkscape_render_ms') is not None and p.get('v04_mean_inkscape_render_ms') is not None else "- Fresh V01/V04 render timings were not captured together in this metrics pass; cached PNGs were reused for several images. Separate `render_performance.csv` records fresh timings when produced."),
        f"- Sampled Python-process peak RSS across the full run: {p['process_peak_rss_sampled_mb']:.1f} MiB (10 ms sampler; a sampled process value, not guaranteed to capture the instantaneous system peak).", '',
        '## Interpretation / failures', '',
        'PSNR and SSIM compare pixels; Canny edge precision/recall/F1 is threshold- and renderer-dependent. The small-edge-component recall and foreground IoU use heuristic image-derived masks, not annotated semantic ground truth. None of these metrics proves that a human finds the result more editable or professionally composed.', '',
        'Explicit regressions in this run: edge precision fell on A09 and A10 despite their edge-F1 increases (A09 0.811 → 0.675, A10 0.796 → 0.762); the small-edge-component recall proxy fell on A04. The representation also regresses strongly on object count / ease of editing: every image has 9,000 rectangular cells plus 1,111–5,268 residual color paths; average SVG size grows from about 590 KiB to 1,224 KiB. A semantic/editability score was not measured and semantic reconstruction is not implemented.\n\nThe edge-band residual can substantially improve silhouette and thin-stroke metrics, but does so by representing many source pixels as grouped, quantized SVG path runs. This increases file size and object/path counts, and means the improvement is a deliberate detail-preserving hybrid vector representation rather than recovered vector primitives. The axis-aligned base tessellation can still staircase diagonal silhouettes and cannot infer names, ownership, object overlap, meaningful groups, text semantics, transparent material layers, or separable shadows/highlights. Gradient estimates are local rank-1 RGB fits, not physically based illumination or a true optimized gradient mesh. Results should not be generalized beyond these 12 inputs.', '',
        '## Reproducibility', '',
        'From repository root: `python versions/version-04-claude-challenger/src/run_benchmark.py --budget 9000 --a01-sweep`. For just final 12-image generation / evaluation, run `python versions/version-04-claude-challenger/src/finalize_metrics.py --budget 9000`. Requires the dependencies in this folder and a local Inkscape CLI. All source inputs and Version 01 artifacts remain unchanged.', '']
    report_path=OUT/'metrics'/'RESULTS_REPORT.md'
    prior_text=report_path.read_text(encoding='utf-8') if report_path.exists() else ''
    provenance=re.search(r'<!-- DOC_PROVENANCE\n.*?\nEND_DOC_PROVENANCE -->\n?',prior_text,re.S)
    body='\n'.join(lines).rstrip()+'\n'
    if provenance:
        body=provenance.group(0).rstrip()+'\n\n'+body
    report_path.write_text(body, encoding='utf-8')
```

### `save_progress` — `Lines 110–116`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `110` إلى السطر `116` (`Lines 110–116`)
- **الوظيفة:** Durable per-image checkpoint so one slow SVG does not lose completed work.
- **الكود الفعلي (`Lines 110–116`):**
```python
def save_progress(rows):
    """Durable per-image checkpoint so one slow SVG does not lose completed work."""
    checkpoint = OUT/'metrics'/'partial_benchmark_results.json'
    checkpoint.write_text(json.dumps(rows, indent=2), encoding='utf-8')
    if rows:
        with (OUT/'metrics'/'partial_benchmark_results.csv').open('w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
```

### `main` — `Lines 119–243`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `119` إلى السطر `243` (`Lines 119–243`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 119–243`):**
```python
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--budget', type=int, default=9000)
    parser.add_argument('--inkscape', default='inkscape')
    parser.add_argument('--skip-v01-render', action='store_true', help='Reuse an existing fresh V01 PNG render when it exists')
    args = parser.parse_args()
    if args.budget < 100 or args.budget > 100000:
        raise SystemExit('--budget must be between 100 and 100000')
    if shutil.which(args.inkscape) is None and not Path(args.inkscape).exists():
        raise SystemExit(f'Inkscape executable not found: {args.inkscape}. Install it and pass --inkscape.')
    for sub in ['outputs','rendered/v01','rendered/v04','comparisons','metrics','logs']:
        (OUT/sub).mkdir(parents=True, exist_ok=True)
    sources = sorted(p for p in SRC_DIR.glob('A*.png') if re.match(r'A\d\d_', p.name))
    if len(sources) != 12: raise RuntimeError(f'Expected 12 source images, found {len(sources)}')
    recorded_data = json.loads(V01_RECORDED_JSON.read_text(encoding='utf-8'))
    recorded = {item['image_id']: item for item in recorded_data}
    checkpoint_path = OUT/'metrics'/'partial_benchmark_results.json'
    rows = []
    if checkpoint_path.exists():
        try:
            prior = json.loads(checkpoint_path.read_text(encoding='utf-8'))
            rows = [r for r in prior if r.get('v04_cells') == args.budget and r.get('v04_final_representation','').startswith('hybrid vector surface tessellation plus quantized edge-band residual') and (OUT/'outputs'/f"{r.get('filename','').rsplit('.',1)[0]}_v04.svg").exists() and (OUT/'rendered'/'v04'/f"{r.get('image_id','')}_v04.png").exists()]
        except Exception:
            rows = []
    done_ids = {r['image_id'] for r in rows}
    visuals = []
    repeat_determinism = []
    with Sampler() as sampler:
        for idx, src_path in enumerate(sources, 1):
            aid = src_path.name.split('_')[0]
            if aid in done_ids:
                print(f'[{idx}/12] {aid}: reusing checkpointed hybrid SVG/render/metrics', flush=True)
                continue
            src = load_rgb(src_path); h, w = src.shape[:2]
            v01_svg = V01_SVG_DIR/f'{aid}_v01_vector.svg'
            v01_png = OUT/'rendered'/'v01'/f'{aid}_v01.png'
            v04_svg = OUT/'outputs'/f'{src_path.stem}_v04.svg'
            v04_png = OUT/'rendered'/'v04'/f'{aid}_v04.png'
            if not v01_svg.exists(): raise FileNotFoundError(v01_svg)
            if not (args.skip_v01_render and v01_png.exists()):
                v01_render_ms = rasterize_svg(v01_svg, v01_png, w, h, args.inkscape)
            else: v01_render_ms = None
            start = time.perf_counter()
            surface_svg, surface_stats = AdaptiveVectorSurface(Config(max_cells=args.budget)).vectorize(src)
            hybrid_svg, edge_stats = add_edge_residual_layer(surface_svg, src, dilation=1, color_bits=5)
            gen_ms = (time.perf_counter()-start)*1000
            previous_svg = v04_svg.read_text(encoding='utf-8') if v04_svg.exists() else None
            saved_matches = previous_svg == hybrid_svg
            repeat_determinism.append(saved_matches)
            check_ms = 0.0  # standalone verifier performs a second independent regeneration
            if not saved_matches:
                v04_svg.write_text(hybrid_svg, encoding='utf-8')
            if saved_matches and v04_png.exists():
                v04_render_ms = 0.0  # cached prior render of this exact byte-identical SVG
            else:
                v04_render_ms = rasterize_svg(v04_svg, v04_png, w, h, args.inkscape)
            m0 = compare(src, load_rgb(v01_png)); m1 = compare(src, load_rgb(v04_png))
            s0 = svg_structure(v01_svg); s1 = svg_structure(v04_svg)
            old = recorded.get(aid, {})
            row = {
                'image_id': aid, 'filename': src_path.name, 'width': w, 'height': h,
                'v01_recorded_mse': old.get('mse'), 'v01_recorded_psnr_db': old.get('psnr_db'), 'v01_recorded_ssim': old.get('ssim'),
                'v01_fresh_mse': m0['mse'], 'v01_fresh_psnr_db': m0['psnr_db'], 'v01_fresh_ssim': m0['ssim'],
                'v01_edge_precision_1px': m0['edge_precision_1px'], 'v01_edge_recall_1px': m0['edge_recall_1px'], 'v01_edge_f1_1px': m0['edge_f1_1px'],
                'v01_small_edge_component_recall_proxy': m0['small_edge_component_recall_proxy'], 'v01_foreground_iou_proxy': m0['border_background_foreground_iou_proxy'],
                'v01_paths': s0['path_count'], 'v01_estimated_path_anchors_controls': s0['estimated_path_anchors_and_controls'], 'v01_svg_bytes': s0['svg_bytes'], 'v01_render_ms': v01_render_ms,
                'v04_mse': m1['mse'], 'v04_psnr_db': m1['psnr_db'], 'v04_ssim': m1['ssim'],
                'v04_edge_precision_1px': m1['edge_precision_1px'], 'v04_edge_recall_1px': m1['edge_recall_1px'], 'v04_edge_f1_1px': m1['edge_f1_1px'],
                'v04_small_edge_component_recall_proxy': m1['small_edge_component_recall_proxy'], 'v04_foreground_iou_proxy': m1['border_background_foreground_iou_proxy'],
                'v04_cells': surface_stats['leaf_cells'], 'v04_rectangles': s1['rectangle_count'], 'v04_gradients': s1['linear_gradients'],
                'v04_paths': s1['path_count'], 'v04_path_anchors_controls': s1['estimated_path_anchors_and_controls'],
                'v04_implicit_rect_corners': s1['rectangle_count']*4, 'v04_svg_bytes': s1['svg_bytes'],
                'v04_surface_generation_ms': surface_stats['generation_ms'], 'v04_edge_overlay_and_total_generation_ms': round(gen_ms,3),
                'v04_determinism_check_generation_ms': round(check_ms,3), 'v04_render_ms': round(v04_render_ms,3),
                'v04_edge_residual_pixels': edge_stats['edge_residual_pixels'], 'v04_edge_residual_runs': edge_stats['edge_residual_horizontal_runs'],
                'v04_edge_residual_color_paths': edge_stats['edge_residual_color_paths'], 'v04_edge_residual_corners': edge_stats['edge_residual_implicit_corners'],
                'v04_edge_residual_color_bits': edge_stats['edge_residual_color_bits_per_channel'],
                'v04_embedded_raster_images': s1['embedded_raster_images'], 'v04_xml_well_formed': s1['xml_well_formed'],
                'v04_final_representation': edge_stats['representation'],
            }
            rows.append(row)
            save_progress(rows)
            comparison = OUT/'comparisons'/f'{aid}_original_vs_v01_vs_v04.png'
            make_comparison(aid, src_path, v01_png, v04_png, comparison)
            visuals.append({'image_id':aid,'source_path':str(src_path),'v01_render_path':str(v01_png),'v04_render_path':str(v04_png)})
            print(f"[{idx}/12] {aid}: PSNR {m0['psnr_db']:.2f} -> {m1['psnr_db']:.2f} dB; SSIM {m0['ssim']:.4f} -> {m1['ssim']:.4f}; edge F1 {m0['edge_f1_1px']:.3f} -> {m1['edge_f1_1px']:.3f}; residual paths={edge_stats['edge_residual_color_paths']}; SVG={s1['svg_bytes']/1024:.0f} KiB", flush=True)
    rows.sort(key=lambda r:r['image_id'])
    # Rebuild comparison panel records for checkpointed entries as well.
    visuals = [{'image_id':r['image_id'],'source_path':str(SRC_DIR/r['filename']),'v01_render_path':str(OUT/'rendered'/'v01'/f"{r['image_id']}_v01.png"),'v04_render_path':str(OUT/'rendered'/'v04'/f"{r['image_id']}_v04.png")} for r in rows]
    (OUT/'metrics'/'benchmark_results.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
    with (OUT/'metrics'/'benchmark_results.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
    make_contact_sheet(visuals,OUT/'comparisons'/'all_12_contact_sheet.png')
    metrics=['mse','psnr_db','ssim','edge_precision_1px','edge_recall_1px','edge_f1_1px','small_edge_component_recall_proxy','foreground_iou_proxy']
    summary={'dataset_images':len(rows),'budget_cells':args.budget,'renderer':'Inkscape CLI; source native dimensions; same renderer for V01 and V04',
             'v01_baseline':'versions/version-01/experiments/preliminary_visual_tests/outputs/A##_v01_vector.svg',
             'v04_representation':'hybrid vector-only adaptive surface tessellation + 5-bit/channel source-derived dilated Canny edge-band residual',
             'previous_saved_svg_matched_current_generator_for_processed_images':(all(repeat_determinism) if repeat_determinism else None),'per_image_saved_svg_match_checks_for_newly_processed_images':repeat_determinism,
             'all_v04_xml_well_formed':all(r['v04_xml_well_formed'] for r in rows),'all_v04_embedded_raster_count_zero':all(r['v04_embedded_raster_images']==0 for r in rows),'comparisons':{}}
    for met in metrics:
        bk='v01_fresh_'+met if met in ('mse','psnr_db','ssim') else ('v01_foreground_iou_proxy' if met=='foreground_iou_proxy' else 'v01_'+met)
        nk='v04_'+met if met in ('mse','psnr_db','ssim') else ('v04_foreground_iou_proxy' if met=='foreground_iou_proxy' else 'v04_'+met)
        pairs=[r for r in rows if np.isfinite(r[bk]) and np.isfinite(r[nk])]
        better=lambda r: r[nk] < r[bk] if met=='mse' else r[nk] > r[bk]
        summary['comparisons'][met]={'v01_mean':mean(pairs,bk),'v04_mean':mean(pairs,nk),'v04_better_count':sum(better(r) for r in pairs),'v04_worse_count':sum(not better(r) for r in pairs),'n':len(pairs),'v04_worse_images':[r['image_id'] for r in pairs if not better(r)]}
    summary['complexity']={
        'v01_mean_paths':mean(rows,'v01_paths'),'v04_mean_paths':mean(rows,'v04_paths'),'v04_mean_residual_color_paths':mean(rows,'v04_edge_residual_color_paths'),
        'v01_mean_svg_bytes':mean(rows,'v01_svg_bytes'),'v04_mean_svg_bytes':mean(rows,'v04_svg_bytes'),
        'v01_mean_estimated_path_anchors_controls':mean(rows,'v01_estimated_path_anchors_controls'),'v04_mean_path_anchors_controls':mean(rows,'v04_path_anchors_controls'),
        'v04_mean_rectangles':mean(rows,'v04_rectangles'),'v04_mean_gradients':mean(rows,'v04_gradients'),'v04_mean_residual_runs':mean(rows,'v04_edge_residual_runs')}
    fresh_perf_path=OUT/'metrics'/'render_performance.csv'
    fresh_perf=[]
    if fresh_perf_path.exists():
        with fresh_perf_path.open(newline='',encoding='utf-8') as f: fresh_perf=list(csv.DictReader(f))
    fresh_perf=[r for r in fresh_perf if r.get('v01_render_ms') and r.get('v04_render_ms')]
    summary['performance']={'v04_mean_generation_ms':mean(rows,'v04_edge_overlay_and_total_generation_ms'),'v04_median_generation_ms':float(np.median([r['v04_edge_overlay_and_total_generation_ms'] for r in rows])),
        'v04_mean_surface_generation_ms':mean(rows,'v04_surface_generation_ms'),
        'v04_mean_inkscape_render_ms':float(np.mean([float(r['v04_render_ms']) for r in fresh_perf])) if fresh_perf else None,
        'v01_mean_inkscape_render_ms':float(np.mean([float(r['v01_render_ms']) for r in fresh_perf])) if fresh_perf else None,
        'fresh_render_timing_images':len(fresh_perf),
        'process_peak_rss_sampled_mb':round(sampler.peak/(1024*1024),3),'rss_sampling_interval_ms':10,
        'note':'Local runtime; Python process RSS sampled every 10 ms. Per-image v04_render_ms=0 in benchmark_results indicates a cached render reuse. Fresh renderer timings, when present, are separate paired reruns recorded in render_performance.csv.'}
    (OUT/'metrics'/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    write_report(rows,summary)
    print('\nSUMMARY\n'+json.dumps(summary,indent=2),flush=True)
```
