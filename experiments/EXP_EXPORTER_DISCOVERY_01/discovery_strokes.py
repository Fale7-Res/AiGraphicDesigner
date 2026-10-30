# START CHANGE AGD-SOURCE-STROKES | 2026-10-29T21:58:16Z | CREATED | Author: discovery_strokes
"""Source-only paired-flank stroke proposals; no label or reference inputs."""
from __future__ import annotations

import hashlib
import json
import math
import time
from pathlib import Path

import cv2
import numpy as np
from scipy.ndimage import gaussian_filter, map_coordinates
from scipy.spatial import cKDTree
from skimage.color import rgb2lab
from skimage.morphology import skeletonize

CONFIG = {
    'version': 'paired_flank_strokes_v1', 'gaussian_sigma_px': 0.6,
    'normal_count': 8, 'flank_radii_px': [1.5, 2.5, 4.0],
    'minimum_contrast_lab': 15.0, 'maximum_flank_difference_lab': 12.0,
    'minimum_contrast_cosine': 0.9, 'nms_distance_px': 1.0,
    'profile_step_px': 0.25, 'profile_limit_px': 4.5,
    'minimum_length_px': 6.0, 'minimum_render_width_px': 0.5,
    'maximum_width_px': 6.0, 'rdp_epsilon_px': 0.35,
    'corner_angle_degrees': 60.0, 'maximum_sampled_deviation_px': 0.6,
    'curve_samples_per_segment': 32, 'raw_sampling_step_px': 0.25,
    'maximum_cubic_segments': 64, 'maximum_proposals': 128,
    'maximum_source_pixels': 1000000, 'wall_budget_seconds': 60,
    'sampled_memory_budget_mib': 512,
}


def _sample(field, x, y):
    shape = np.asarray(x).shape
    x, y = np.atleast_1d(x), np.atleast_1d(y)
    if field.ndim == 2:
        return map_coordinates(field, [y, x], order=1, mode='nearest').reshape(shape)
    return np.stack([map_coordinates(field[..., c], [y, x], order=1,
                                     mode='nearest') for c in range(3)], axis=-1).reshape(shape+(3,))


def _ridge_evidence(rgb):
    lab = gaussian_filter(rgb2lab(rgb / 255.0), sigma=(0.6, 0.6, 0))
    h, w = rgb.shape[:2]
    yy, xx = np.mgrid[:h, :w].astype(float)
    best = np.zeros((h, w)); angle = np.zeros((h, w)); radius = np.zeros((h, w))
    for k in range(8):
        theta = k * math.pi / 8
        nx, ny = math.cos(theta), math.sin(theta)
        for r in CONFIG['flank_radii_px']:
            left = _sample(lab, xx-r*nx, yy-r*ny)
            right = _sample(lab, xx+r*nx, yy+r*ny)
            a, b = lab-left, lab-right
            ca, cb = np.linalg.norm(a, axis=-1), np.linalg.norm(b, axis=-1)
            cosine = np.sum(a*b, axis=-1) / np.maximum(ca*cb, 1e-12)
            valid = ((ca >= 15) & (cb >= 15) & (cosine >= .9) &
                     (np.linalg.norm(left-right, axis=-1) <= 12) &
                     (xx-r*abs(nx) >= 0) & (xx+r*abs(nx) < w-1) &
                     (yy-r*abs(ny) >= 0) & (yy+r*abs(ny) < h-1))
            score = np.where(valid, np.minimum(ca, cb)/r, 0)
            improve = score > best
            best[improve] = score[improve]; angle[improve] = theta; radius[improve] = r
    nx, ny = np.cos(angle), np.sin(angle)
    keep = ((best > 0) & (best >= _sample(best, xx+nx, yy+ny)) &
            (best >= _sample(best, xx-nx, yy-ny)))
    return lab, best, angle, radius, keep, skeletonize(keep)


def _trace(skeleton):
    """Visit undirected graph edges once; suppress redundant diagonal chords."""
    pixels = set(map(tuple, np.argwhere(skeleton)))
    adjacency = {}
    for y, x in sorted(pixels):
        near = []
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if not (dx or dy) or (y+dy, x+dx) not in pixels:
                    continue
                if dx and dy and ((y+dy, x) in pixels or (y, x+dx) in pixels):
                    continue
                near.append((y+dy, x+dx))
        adjacency[y, x] = sorted(near)
    used = set(); chains = []
    def walk(a, b):
        chain = [a]; current = a
        while True:
            used.add(tuple(sorted((current, b)))); chain.append(b)
            if b == a or len(adjacency[b]) != 2:
                break
            candidates = [p for p in adjacency[b] if p != current]
            current, b = b, candidates[0]
            if tuple(sorted((current, b))) in used:
                break
        return np.asarray([(x+.5, y+.5) for y, x in chain], dtype=float)
    for a in sorted(adjacency, key=lambda p: (len(adjacency[p]) == 2, p)):
        for b in adjacency[a]:
            if tuple(sorted((a, b))) not in used:
                chains.append(walk(a, b))
    return chains, adjacency


def _resample_polyline(points, step):
    output = []
    for a, b in zip(points[:-1], points[1:]):
        n = max(1, int(math.ceil(np.linalg.norm(b-a)/step)))
        output.extend(a + (b-a)*t/n for t in range(n))
    return np.asarray(output+[points[-1]])


def _fit(points):
    vertices = cv2.approxPolyDP(points.astype(np.float32).reshape(-1, 1, 2),
                                .35, False).reshape(-1, 2).astype(float)
    if len(vertices) < 2:
        return None, {'reason': 'insufficient_vertices'}
    if len(vertices)-1 > 64:
        return None, {'reason': 'cubic_budget', 'segments': len(vertices)-1}
    tangents = []
    corners = []
    for i in range(len(vertices)):
        if i == 0 or i == len(vertices)-1:
            tangents.append(None); corners.append(True); continue
        before, after = vertices[i]-vertices[i-1], vertices[i+1]-vertices[i]
        cosine = np.dot(before, after)/max(np.linalg.norm(before)*np.linalg.norm(after), 1e-12)
        corner = math.degrees(math.acos(float(np.clip(cosine, -1, 1)))) >= 60
        tangents.append((vertices[i+1]-vertices[i-1])/2); corners.append(corner)
    curves = []
    for i, (a, b) in enumerate(zip(vertices[:-1], vertices[1:])):
        ta = b-a if corners[i] else tangents[i]
        tb = b-a if corners[i+1] else tangents[i+1]
        curves.append(np.asarray([a, a+ta/3, b-tb/3, b]))
    samples = []
    t = np.linspace(0, 1, 33)[:, None]
    for a, b, c, d in curves:
        samples.append((1-t)**3*a + 3*(1-t)**2*t*b + 3*(1-t)*t*t*c + t**3*d)
    fitted = np.concatenate(samples)
    raw = _resample_polyline(points, .25)
    deviation = max(float(cKDTree(raw).query(fitted)[0].max()),
                    float(cKDTree(fitted).query(raw)[0].max()))
    meta = {'sampled_symmetric_deviation_px': deviation,
            'segments': len(curves), 'intentional_corner_count': sum(corners[1:-1])}
    if deviation > .6:
        return None, dict(meta, reason='curve_deviation')
    return np.asarray(curves), meta


def _width(lab, points, angle, radius):
    widths = []
    for x, y in points:
        iy, ix = int(np.clip(y-.5, 0, lab.shape[0]-1)), int(np.clip(x-.5, 0, lab.shape[1]-1))
        theta, r = float(angle[iy, ix]), float(radius[iy, ix])
        if r == 0:
            continue
        x, y = x-.5, y-.5
        center = _sample(lab, np.asarray(x), np.asarray(y))
        distances = []
        for sign in (-1, 1):
            nx, ny = sign*math.cos(theta), sign*math.sin(theta)
            flank = _sample(lab, np.asarray(x+r*nx), np.asarray(y+r*ny))
            direction = center-flank
            denom = float(np.dot(direction, direction))
            previous, crossing = 1., None
            for distance in np.arange(.25, 4.5+.125, .25):
                value = _sample(lab, np.asarray(x+distance*nx), np.asarray(y+distance*ny))
                fraction = float(np.dot(value-flank, direction)/max(denom, 1e-12))
                if fraction <= .5:
                    crossing = distance-.25 + .25*(previous-.5)/max(previous-fraction, 1e-12)
                    break
                previous = fraction
            if crossing is not None:
                distances.append(crossing)
        if len(distances) == 2:
            widths.append(sum(distances))
    return float(np.median(widths)) if widths else None, len(widths)


def discover(rgb):
    started = time.perf_counter()
    rgb = np.asarray(rgb)
    if rgb.dtype != np.uint8 or rgb.ndim != 3 or rgb.shape[2] != 3:
        raise ValueError('Require native HxWx3 uint8 RGB')
    if min(rgb.shape[:2]) < 9 or np.prod(rgb.shape[:2]) > 1000000:
        raise ValueError('Source dimensions outside frozen budget')
    lab, score, angle, radius, support, skeleton = _ridge_evidence(rgb)
    chains, adjacency = _trace(skeleton)
    accepted, rejected = [], []
    for index, points in enumerate(chains):
        length = float(np.linalg.norm(np.diff(points, axis=0), axis=1).sum())
        audit = {'chain_id': index, 'length_px': length,
                 'source_points_xy': points.tolist()}
        if length < 6:
            rejected.append(dict(audit, reason='short_chain')); continue
        width, samples = _width(lab, points, angle, radius)
        audit.update(raw_width_px=width, width_profile_count=samples)
        if width is None or width > 6:
            rejected.append(dict(audit, reason='unsupported_or_broad_width')); continue
        curves, fit = _fit(points); audit.update(fit)
        if curves is None:
            rejected.append(audit); continue
        indices = np.rint(points-.5).astype(int)
        confidence = float(np.median(score[indices[:, 1], indices[:, 0]]))
        accepted.append(dict(audit, width_px=max(.5, width),
                             source_confidence=confidence,
                             rank_score=confidence*length, curves=curves.tolist(),
                             closed=bool(np.array_equal(points[0], points[-1]))))
    accepted.sort(key=lambda p: (-p['rank_score'], p['chain_id']))
    for item in accepted[128:]:
        rejected.append(dict(item, reason='proposal_budget'))
    accepted = accepted[:128]
    audit = {'config': CONFIG, 'rgb_array_sha256': hashlib.sha256(rgb.tobytes()).hexdigest(),
             'accepted': accepted, 'rejected': rejected,
             'source_support_pixels': int(support.sum()), 'skeleton_pixels': int(skeleton.sum()),
             'junction_count': sum(len(v)>2 for v in adjacency.values()),
             'isolated_skeleton_pixels': sum(len(v)==0 for v in adjacency.values()),
             'wall_seconds': time.perf_counter()-started,
             'integrated_into_shared_graph': False}
    return audit, {'source_score': score.astype(np.float32), 'source_support': support,
                   'source_skeleton': skeleton, 'source_normal': angle.astype(np.float32)}


def svg(audit, width, height):
    paths = []
    for item in audit['accepted']:
        curves = np.asarray(item['curves'])
        d = f'M {curves[0,0,0]:.8g} {curves[0,0,1]:.8g}'
        for curve in curves:
            d += ' C ' + ' '.join(f'{v:.8g}' for v in curve[1:].ravel())
        if item['closed']:
            d += ' Z'
        paths.append(f'<path d="{d}" stroke-width="{item["width_px"]:.8g}"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}"><g fill="none" stroke="#0066cc" '
            'stroke-linecap="round" stroke-linejoin="round">'+''.join(paths)+'</g></svg>')


def save(source, directory):
    from PIL import Image
    target = Path(directory); target.mkdir(parents=True, exist_ok=False)
    rgb = np.asarray(Image.open(source).convert('RGB'))
    audit, arrays = discover(rgb)
    audit['source_file_sha256'] = hashlib.sha256(Path(source).read_bytes()).hexdigest()
    (target/'proposals.json').write_text(json.dumps(audit, indent=2), encoding='utf-8')
    (target/'proposals.svg').write_text(svg(audit, rgb.shape[1], rgb.shape[0]), encoding='utf-8')
    np.savez_compressed(target/'evidence.npz', **arrays)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source'); parser.add_argument('new_output_directory')
    args = parser.parse_args(); save(args.source, args.new_output_directory)
# END CHANGE AGD-SOURCE-STROKES | 2026-10-29T21:58:16Z | CREATED | Author: discovery_strokes
