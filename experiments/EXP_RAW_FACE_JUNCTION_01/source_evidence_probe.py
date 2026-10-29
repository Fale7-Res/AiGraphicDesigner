# START CHANGE AGD-RAWFACE-SOURCE-EVIDENCE-PROBE | 2026-10-29T12:20:15Z | CREATED | Author: root
"""Fixed source-only evidence probe; no segmentation, references or geometry."""
from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

import numpy as np
from scipy.ndimage import distance_transform_edt
from skimage.color import rgb2lab
from skimage.feature import canny
from skimage.filters import sato

CONFIG = {
    'version': 'source_evidence_only_v1',
    'edge_sigmas': [0.6, 1.2],
    'low_threshold': 0.04,
    'high_threshold': 0.10,
    'use_quantiles': False,
    'mode': 'reflect',
    'persistence_distance_px': 1.0,
    'ridge_sigmas': [0.7, 1.2, 2.0],
    'dense_edge_fraction_warning': 0.15,
    'constructor_uses_labels_or_references': False,
    'output_is_reconstructed_geometry': False,
}


def _near(mask: np.ndarray, radius: float) -> np.ndarray:
    # scipy EDT on all-True arrays has implicit outside behavior; no support
    # must remain no support rather than creating evidence at array corners.
    if not mask.any():
        return np.zeros_like(mask, dtype=bool)
    return distance_transform_edt(~mask) <= radius


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
    # The per-image maximum is an explicit display scale, never calibrated confidence.


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source_rgb')
    parser.add_argument('new_output_directory')
    args = parser.parse_args()
    save(args.source_rgb, args.new_output_directory)

# END CHANGE AGD-RAWFACE-SOURCE-EVIDENCE-PROBE | 2026-10-29T12:20:15Z | CREATED | Author: root
