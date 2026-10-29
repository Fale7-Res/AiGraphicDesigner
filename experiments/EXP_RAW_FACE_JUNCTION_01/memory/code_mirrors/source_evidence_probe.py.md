# مرآة الكود التفصيلية: `source_evidence_probe.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `source_evidence_probe.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `source_evidence_probe.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `132` (`Lines 1–132`)
- **بصمة الملف (`SHA-256`):** `7b008c93c390a19769e686f7e95947f301c55f7c93ee31e0cb5eef331de4b222`
- **الوصف التفصيلي:** # START CHANGE AGD-RAWFACE-SOURCE-EVIDENCE-PROBE | 2026-10-29T12:20:15Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `_near` | `function` | `Lines 31–36` | `def _near(mask: np.ndarray, radius: float) -> np.ndarray:` | رمز برمجي موثق. |
| `extract` | `function` | `Lines 39–94` | `def extract(rgb: np.ndarray) -> tuple[dict[str, np.ndarray], dict]:` | Extract fixed maps from native uint8 RGB. Never infer region ownership. |
| `save` | `function` | `Lines 97–120` | `def save(rgb_path: str | Path, output_dir: str | Path) -> None:` | CLI wrapper reads only source image and writes immutable evidence maps. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `_near` — `Lines 31–36`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `31` إلى السطر `36` (`Lines 31–36`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 31–36`):**
```python
def _near(mask: np.ndarray, radius: float) -> np.ndarray:
    # scipy EDT on all-True arrays has implicit outside behavior; no support
    # must remain no support rather than creating evidence at array corners.
    if not mask.any():
        return np.zeros_like(mask, dtype=bool)
    return distance_transform_edt(~mask) <= radius
```

### `extract` — `Lines 39–94`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `39` إلى السطر `94` (`Lines 39–94`)
- **الوظيفة:** Extract fixed maps from native uint8 RGB. Never infer region ownership.
- **الكود الفعلي (`Lines 39–94`):**
```python
def extract(rgb: np.ndarray) -> tuple[dict[str, np.ndarray], dict]:
    """Extract fixed maps from native uint8 RGB. Never infer region ownership."""
    started = time.perf_counter()
    rgb = np.asarray(rgb)
    if rgb.dtype != np.uint8 or rgb.ndim != 3 or rgb.shape[-1] != 3:
        raise ValueError('Require native HxWx3 uint8 RGB')
    if min(rgb.shape[:2]) < 3:
        raise ValueError('Require at least three pixels per spatial dimension')
    lab = rgb2lab(rgb.astype(np.float64) / 255.0)
    normalized = lab / np.array([100.0, 128.0, 128.0])
    arrays = {}
    unions = []
    for scale_index, sigma in enumerate(CONFIG['edge_sigmas']):
        channels = []
        for channel in range(3):
            edge = canny(normalized[..., channel], sigma=sigma,
                         low_threshold=CONFIG['low_threshold'],
                         high_threshold=CONFIG['high_threshold'],
                         use_quantiles=False, mode='reflect')
            arrays[f'edge_scale_{scale_index}_channel_{channel}'] = edge
            channels.append(edge)
        union = np.logical_or.reduce(channels)
        arrays[f'edge_scale_{scale_index}'] = union
        unions.append(union)
    persistent = ((unions[0] & _near(unions[1], 1.0)) |
                  (unions[1] & _near(unions[0], 1.0)))
    arrays['persistent_edges'] = persistent
    luminance = normalized[..., 0]
    for polarity, black in [('dark', True), ('light', False)]:
        responses = []
        for index, sigma in enumerate(CONFIG['ridge_sigmas']):
            response = sato(luminance, sigmas=[sigma],
                            black_ridges=black, mode='reflect')
            arrays[f'ridge_{polarity}_scale_{index}'] = response.astype(np.float32)
            responses.append(response)
        arrays[f'ridge_{polarity}_maximum'] = np.maximum.reduce(responses).astype(np.float32)
    density = float(persistent.mean())
    metadata = {
        'config': CONFIG,
        'shape': list(rgb.shape),
        'rgb_array_sha256': hashlib.sha256(rgb.tobytes()).hexdigest(),
        'persistent_edge_pixels': int(persistent.sum()),
        'persistent_edge_fraction': density,
        'clutter_warning': density > CONFIG['dense_edge_fraction_warning'],
        'ridge_maxima': {p: float(arrays[f'ridge_{p}_maximum'].max())
                         for p in ['dark', 'light']},
        'wall_seconds': time.perf_counter() - started,
        'limitations': [
            'Evidence maps are not recovered curves, regions or physical boundaries.',
            'Canny output is pixel-indexed; subpixel localization is not implemented.',
            'Sato intensity ridges may be shading and do not establish width or topology.',
            'Chromatic ridges without luminance contrast can be missed by Sato.',
            'No threshold tuning or postprocessing to improve benchmark scores.',
        ],
    }
    return arrays, metadata
```

### `save` — `Lines 97–120`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `97` إلى السطر `120` (`Lines 97–120`)
- **الوظيفة:** CLI wrapper reads only source image and writes immutable evidence maps.
- **الكود الفعلي (`Lines 97–120`):**
```python
def save(rgb_path: str | Path, output_dir: str | Path) -> None:
    """CLI wrapper reads only source image and writes immutable evidence maps."""
    from PIL import Image
    import skimage
    path = Path(rgb_path)
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=False)
    rgb = np.asarray(Image.open(path).convert('RGB'))
    arrays, metadata = extract(rgb)
    metadata['source_file_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
    metadata['numpy_version'] = np.__version__
    metadata['skimage_version'] = skimage.__version__
    np.savez_compressed(output / 'source_evidence.npz', **arrays)
    (output / 'source_evidence.json').write_text(
        json.dumps(metadata, indent=2, sort_keys=True), encoding='utf-8')
    edge = arrays['persistent_edges']
    overlay = rgb.copy()
    overlay[edge] = (255, 0, 255)
    Image.fromarray(overlay).save(output / 'persistent_edges_overlay.png')
    for polarity in ['dark', 'light']:
        field = arrays[f'ridge_{polarity}_maximum']
        scale = float(field.max())
        display = np.zeros(field.shape, np.uint8) if scale == 0 else np.rint(255 * field / scale).astype(np.uint8)
        Image.fromarray(display).save(output / f'ridge_{polarity}_DISPLAY_ONLY.png')
```
