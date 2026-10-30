# START CHANGE AGD-EXPORTER-CORRECTNESS | 2026-10-29T21:55:44Z | CREATED | Author: exporter_correctness
"""Research graph SVG serialization; no graph repair, fitting or raster fallback.

Closed-chain closure is expanded into an explicit oriented line before chains
are joined. Only an entire face contour emits Z. This respects SVG's current
subpath origin while preserving the in-memory chain's implied straight closure.
"""
import math
from html import escape


def _point(value):
    if len(value) != 2 or not all(math.isfinite(float(x)) for x in value):
        raise ValueError('A finite 2D point is required')
    return tuple(float(x) for x in value)


def _same(a, b):
    return math.dist(a, b) <= 1e-8


def chain_segments(chain, raw=False, forward=True):
    """Return directed L/C segments, including a logical chain closure.

    Reverse the complete geometric walk, including its implied closure. Merely
    reversing the stored segments first rotates an implicitly closed chain's
    anchor and can disconnect its shared junction from its containing face.
    """
    result = []
    if raw:
        points = [_point(p) for p in chain['pixel_crack_vertices']]
        if len(points) < 2:
            raise ValueError('Chain needs at least two raw points')
        result = [('L', (a, b)) for a, b in zip(points, points[1:])]
    else:
        for segment in chain['segments']:
            kind = segment['type']
            if kind == 'L':
                points = (_point(segment['p0']), _point(segment['p3']))
            elif kind == 'C':
                points = tuple(_point(segment[k]) for k in ('p0','p1','p2','p3'))
            else:
                raise ValueError('Unsupported segment type: ' + str(kind))
            if result and not _same(result[-1][1][-1], points[0]):
                raise ValueError('Disconnected chain segments')
            result.append((kind, points))
        if not result:
            raise ValueError('Empty fitted chain')
    start, end = result[0][1][0], result[-1][1][-1]
    if chain.get('closed') and not _same(start, end):
        result.append(('L', (end, start)))
    if not forward:
        result = [(kind, tuple(reversed(points))) for kind, points in reversed(result)]
    return result


def _coordinate(point, precision):
    return ','.join(format(value, f'.{precision}g') for value in point)


def _commands(segments, move=True, precision=17):
    result = ['M' + _coordinate(segments[0][1][0], precision)] if move else []
    result.extend(kind + ' '.join(_coordinate(p, precision) for p in points[1:])
                  for kind, points in segments)
    return ' '.join(result)


def _color(label):
    value = (int(label) * 0x9e3779) & 0xffffff
    return '#%06x' % value


def svg_graph(graph, raw=False, regions=False, foreground=None, *, precision=17):
    """API-compatible strict replacement for research geometry_eval.svg_graph.

    Region contours must already form connected closed walks. No snapping,
    bridge creation, polygon repair, orientation changes, or topology changes.
    The inherited evenodd rule is preserved for compound regions and holes.
    """
    if precision not in (8,17):
        raise ValueError('Only 8-significant-digit legacy isolation or 17-digit roundtrip is supported')
    chains = {chain['id']: chain for chain in graph['chains']}
    if len(chains) != len(graph['chains']):
        raise ValueError('Duplicate chain IDs')
    parts = []
    if regions:
        for label, loops in graph['faces'].items():
            if int(label) == 0 or (foreground is not None and int(label) not in foreground):
                continue
            contours = []
            for refs in loops:
                joined = []
                if not refs:
                    raise ValueError('Empty face contour')
                for ref in refs:
                    directed = chain_segments(chains[ref['chain']], raw, ref['forward'])
                    if joined and not _same(joined[-1][1][-1], directed[0][1][0]):
                        raise ValueError('Disconnected face contour')
                    joined.extend(directed)
                if not _same(joined[-1][1][-1], joined[0][1][0]):
                    raise ValueError('Open face contour; exporter will not repair it')
                contours.append(_commands(joined, precision=precision) + ' Z')
            color = 'black' if foreground is not None else _color(label)
            parts.append(f'<path data-region="{escape(str(label), quote=True)}" fill="{color}" fill-rule="evenodd" d="{" ".join(contours)}"/>')
    else:
        for chain in graph['chains']:
            directed = chain_segments(chain, raw)
            data = _commands(directed, precision=precision) + (' Z' if chain.get('closed') else '')
            color = '#607d8b' if 0 in chain['adjacent_face_labels'] else '#111827'
            parts.append(f'<path data-chain="{escape(str(chain["id"]), quote=True)}" d="{data}" fill="none" stroke="{color}" stroke-width="0.35"/>')
    width, height = float(graph['width']), float(graph['height'])
    if not all(math.isfinite(v) and v > 0 for v in (width, height)):
        raise ValueError('Positive finite SVG dimensions required')
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.17g}" height="{height:.17g}" viewBox="0 0 {width:.17g} {height:.17g}">' + ''.join(parts) + '</svg>'
# END CHANGE AGD-EXPORTER-CORRECTNESS | 2026-10-29T21:55:44Z | CREATED | Author: exporter_correctness
