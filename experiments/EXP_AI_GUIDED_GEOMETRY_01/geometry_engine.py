# START CHANGE AGD-AGENTIC-TOOLS | 2026-10-31T11:54:38Z | EDITED | Author: geometry_tools
"""Restricted research geometry tools: frozen evidence in, reversible curves out.

No provider, shell-tool dispatch, evaluator, detector, or network capability.
Only render_geometry invokes a fixed trusted renderer with generated filenames.
"""
from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import math
import subprocess
import sys
import time

import numpy as np
from PIL import Image


def engine_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def geometry_digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def validate_tool_value(value, schema):
    """Validate the deliberately small strict JSON-schema subset used here."""
    kind = schema['type']
    if kind == 'object':
        if not isinstance(value, dict):
            raise ValueError('Expected object')
        if set(value) - set(schema['properties']) or set(schema.get('required', [])) - set(value):
            raise ValueError('Unknown or missing properties')
        for key, item in value.items():
            validate_tool_value(item, schema['properties'][key])
    elif kind == 'array':
        if not isinstance(value, list) or not schema.get('minItems', 0) <= len(value) <= schema.get('maxItems', 100):
            raise ValueError('Invalid array length')
        if schema.get('uniqueItems') and len(set(json.dumps(x, sort_keys=True) for x in value)) != len(value):
            raise ValueError('Duplicate array values')
        for item in value:
            validate_tool_value(item, schema['items'])
    elif kind in ('number', 'integer'):
        try:
            finite_number = not isinstance(value,bool) and isinstance(value,(int,float)) and math.isfinite(value)
        except OverflowError:
            finite_number = False
        if not finite_number:
            raise ValueError('Expected finite numeric value')
        if kind == 'integer' and not isinstance(value, int):
            raise ValueError('Expected integer')
        if not schema.get('minimum', -math.inf) <= value <= schema.get('maximum', math.inf):
            raise ValueError('Numeric bounds exceeded')
        if 'enum' in schema and value not in schema['enum']:
            raise ValueError('Unexpected numeric choice')
    elif kind == 'string':
        if not isinstance(value, str) or ('enum' in schema and value not in schema['enum']):
            raise ValueError('Unexpected string')
    else:
        raise ValueError('Unsupported schema')


def geometry_tool_schemas():
    empty = {'type': 'object', 'properties': {}, 'additionalProperties': False}
    roi = {'type': 'array', 'items': {'type': 'number', 'minimum': 0, 'maximum': 1}, 'minItems': 4, 'maxItems': 4}
    schemas = {
        'inspect_region': dict(empty, properties={'roi': roi}, required=['roi']),
        'get_candidates': dict(empty, properties={'roi': roi, 'limit': {'type': 'integer', 'minimum': 1, 'maximum': 16}}, required=['roi', 'limit']),
        'stage_candidates': dict(empty, properties={'trace_ids': {'type': 'array', 'items': {'type': 'integer', 'minimum': 0, 'maximum': 1000000}, 'minItems': 1, 'maxItems': 4, 'uniqueItems': True}}, required=['trace_ids']),
        'commit_change': empty,
        'rollback_change': empty,
        'validate_geometry': empty,
        'render_geometry': dict(empty, properties={'scale': {'type': 'integer', 'enum': [1, 4, 16], 'minimum': 1, 'maximum': 16}}, required=['scale']),
    }
    # Integer enum is checked explicitly in dispatch as well.
    return [{'type': 'function', 'function': {'name': name, 'description': 'Bounded local geometry operation: ' + name, 'parameters': schema}} for name, schema in schemas.items()]


class GeometryToolEngine:
    """One source image, frozen traces, append-only transactions, no geometry hints."""

    def __init__(self, rgb, traces, initial_items, output_dir, repo, work, renderer=None):
        self.rgb = np.asarray(rgb, dtype=np.uint8).copy()
        if self.rgb.ndim != 3 or self.rgb.shape[2] != 3 or max(self.rgb.shape[:2]) > 2048:
            raise ValueError('RGB source dimensions exceed frozen contract')
        self.height, self.width = self.rgb.shape[:2]
        self.output = Path(output_dir).resolve()
        self.output.mkdir(parents=True, exist_ok=True)
        if list(self.output.iterdir()):
            raise ValueError('New isolated output directory required')
        self.repo, self.work = Path(repo), Path(work)
        sys.path[:0] = [str(self.work / 'geometry-deps'), str(self.repo / 'experiments/EXP_LOSS_ACCOUNTED_CONTOUR_CONSTRUCTION_01'), str(self.repo / 'experiments/EXP_ML_CLASSICAL_HYBRID_GEOMETRY_01'), str(self.repo / 'experiments/EXP_EXPORTER_DISCOVERY_01')]
        self.partition = engine_module(self.repo / 'experiments/EXP_LOSS_ACCOUNTED_CONTOUR_CONSTRUCTION_01/partition_fit.py', 'agentic_frozen_partition')
        self.serializer = engine_module(self.repo / 'experiments/EXP_EXPORTER_DISCOVERY_01/svg_exporter.py', 'agentic_corrected_serializer')
        from shapely.geometry import LineString
        self.LineString = LineString
        self.renderer = Path(renderer or self.work / 'resvg/resvg.exe').resolve()
        self.traces = {}
        for trace in traces:
            tid = trace['trace_id']
            if isinstance(tid, bool) or not isinstance(tid, int) or tid < 0 or tid in self.traces:
                raise ValueError('Invalid frozen trace ID')
            points = np.asarray(trace['source_points_xy'], float)
            if points.ndim != 2 or points.shape[1] != 2 or len(points) < 2 or not np.isfinite(points).all():
                raise ValueError('Invalid frozen source trace')
            if np.any(points < 0) or np.any(points[:, 0] > self.width) or np.any(points[:, 1] > self.height):
                raise ValueError('Trace outside source coordinates')
            self.traces[tid] = dict(trace, source_points_xy=points.tolist())
        self.items = copy.deepcopy(initial_items)
        self.pending = None
        self.history = []
        self.events = []
        self.max_paths, self.max_cubics = 144, 4096
        self.max_calls, self.max_commits = 12, 2
        self.commits = 0
        self.schemas = {x['function']['name']: x['function']['parameters'] for x in geometry_tool_schemas()}
        self.initial_hash = self.state_hash()
        self._validate_state(self.items)
        self.source_pin = geometry_digest({'rgb_sha256': hashlib.sha256(self.rgb.tobytes()).hexdigest(), 'traces': list(self.traces.values()), 'initial': self.items})

    def state_hash(self):
        return geometry_digest(self.items)

    def _validate_state(self, items):
        if len(items) > self.max_paths or sum(len(x['curves']) for x in items) > self.max_cubics:
            raise ValueError('Geometry complexity budget exceeded')
        for item in items:
            cc = np.asarray(item['curves'], float)
            if cc.ndim != 3 or cc.shape[1:] != (4, 2) or not len(cc) or not np.isfinite(cc).all():
                raise ValueError('Invalid cubic array')
            if not np.array_equal(cc[:-1, -1], cc[1:, 0]):
                raise ValueError('Disconnected cubic chain')
            if item.get('closed') and not np.array_equal(cc[0, 0], cc[-1, -1]):
                raise ValueError('False closed-chain declaration')

    def _region_bounds(self, roi):
        x0, y0, x1, y1 = roi
        if not x0 < x1 or not y0 < y1:
            raise ValueError('ROI must have positive extent')
        return [max(0, int(x0*self.width)), max(0, int(y0*self.height)), min(self.width, math.ceil(x1*self.width)), min(self.height, math.ceil(y1*self.height))]

    def _inspect_region(self, roi):
        bounds = self._region_bounds(roi)
        x0,y0,x1,y1 = bounds
        name = 'crop_%02d.png' % len(self.events)
        Image.fromarray(self.rgb[y0:y1, x0:x1]).save(self.output / name)
        return {'bounds_xyxy': bounds, 'preview': name, 'source_only': True, 'state_hash': self.state_hash()}

    def _get_candidates(self, roi, limit):
        x0,y0,x1,y1 = self._region_bounds(roi)
        existing = {x['trace_id'] for x in self.items}
        rows = []
        gray = self.rgb.astype(float).mean(axis=2)/255
        gy,gx = np.gradient(gray)
        gradient = np.hypot(gx,gy)
        normalization = max(float(np.quantile(gradient,.9)),1e-6)
        for tid,t in self.traces.items():
            if tid in existing:
                continue
            p = np.asarray(t['source_points_xy'])
            local = (p[:,0] >= x0)&(p[:,0] < x1)&(p[:,1] >= y0)&(p[:,1] < y1)
            if not local.any():
                continue
            ix = np.clip(p[:,0].astype(int),0,self.width-1);iy = np.clip(p[:,1].astype(int),0,self.height-1)
            contrast = float(np.mean(np.clip(gradient[iy,ix]/normalization,0,1)))
            length = float(np.linalg.norm(np.diff(p,axis=0),axis=1).sum())
            closed = bool(np.array_equal(p[0],p[-1]))
            score = .6*contrast+.25*closed+.15*float(local.mean())
            rows.append({'trace_id': tid, 'score': score, 'source_gradient_support': contrast, 'length_px': length, 'closed_source': closed, 'bbox_xyxy': [float(p[:,0].min()),float(p[:,1].min()),float(p[:,0].max()),float(p[:,1].max())], 'eligible': length >= 6, 'structure_vs_lighting': 'UNVERIFIED'})
        rows.sort(key=lambda r:(not r['eligible'],-r['score'],r['trace_id']))
        return {'candidates': rows[:limit], 'total_candidates_in_roi': len(rows), 'policy': 'unchanged >=6px eligibility first, then fixed source-gradient/closure/local-support; no evaluator evidence'}

    def _stage_candidates(self, trace_ids):
        if self.pending is not None:
            raise ValueError('Resolve pending transaction first')
        if any(tid not in self.traces for tid in trace_ids):
            raise ValueError('Unknown frozen trace ID')
        snapshot = copy.deepcopy(self.items)
        existing = {x['trace_id'] for x in snapshot}
        proposed, ledger = [], []
        deadline = time.monotonic()+20
        lines = [self.LineString(self.partition.flattened(np.asarray(x['curves'],float))) for x in snapshot]
        raws = [self.LineString(self.traces[x['trace_id']]['source_points_xy']) for x in snapshot]
        for tid in trace_ids:
            if tid in existing:
                ledger.append({'trace_id': tid, 'status': 'rejected', 'reason': 'existing_trace'}); continue
            points = np.asarray(self.traces[tid]['source_points_xy'])
            raw = self.LineString(points)
            fitted = self.partition.fit_trace(points, periodic=False, deadline=deadline)
            entry = {'trace_id': tid, 'interval_ledger': fitted['ledger'], 'accepted_paths': 0, 'rejections': []}
            for chain in fitted['chains']:
                cc = np.asarray(chain['curves'])
                line = self.LineString(self.partition.flattened(cc))
                reason = None
                if raw.is_simple and not line.is_simple:
                    reason = 'new_selfintersection'
                for other, otherraw in zip(lines,raws):
                    if reason: break
                    if line.equals(other): reason = 'duplicate_curve'
                    elif line.crosses(other) and not raw.crosses(otherraw): reason = 'new_crossing'
                    elif line.overlaps(other) and not raw.overlaps(otherraw): reason = 'new_overlap'
                    elif (line.crosses(other) or line.overlaps(other)) and not line.intersection(other).difference(raw.intersection(otherraw).buffer(.6)).is_empty: reason = 'crossing_displacement'
                item = dict(chain, trace_id=tid)
                trial = snapshot+proposed+[item]
                try: self._validate_state(trial)
                except ValueError as exc: reason = str(exc)
                if reason:
                    entry['rejections'].append({'partition_ids': chain['partition_ids'], 'reason': reason})
                else:
                    proposed.append(item);lines.append(line);raws.append(raw);entry['accepted_paths'] += 1
            entry['status'] = 'staged' if entry['accepted_paths'] else 'rejected'
            ledger.append(entry)
        self.pending = {'before_hash': self.state_hash(), 'items': snapshot+proposed, 'ledger': ledger, 'added_paths': len(proposed)}
        return {'status': 'pending_validation' if proposed else 'no_safe_edit', 'added_paths': len(proposed), 'ledger': ledger, 'before_hash': self.state_hash(), 'pending_hash': geometry_digest(self.pending['items']), 'geometry_accepted': False}

    def _commit_change(self):
        if self.pending is None:
            raise ValueError('No pending transaction')
        if self.commits >= self.max_commits:
            raise ValueError('Commit budget exceeded')
        if self.pending['before_hash'] != self.state_hash():
            raise ValueError('Stale pending snapshot')
        if not self.pending['added_paths']:
            raise ValueError('No safe geometry to commit; roll back pending state')
        self._validate_state(self.pending['items'])
        self.history.append(copy.deepcopy(self.items))
        self.items = self.pending['items'];self.pending = None;self.commits += 1
        return {'status': 'committed', 'state_hash': self.state_hash(), 'paths': len(self.items), 'geometry_accepted': False}

    def _rollback_change(self):
        if self.pending is not None:
            self.pending = None
            return {'status': 'pending_discarded', 'state_hash': self.state_hash()}
        if not self.history:
            raise ValueError('No transaction available to roll back')
        self.items = self.history.pop()
        return {'status': 'committed_edit_reverted', 'state_hash': self.state_hash()}

    def _validate_geometry(self):
        self._validate_state(self.items)
        return {'state_hash': self.state_hash(), 'paths': len(self.items), 'cubics': sum(len(x['curves']) for x in self.items), 'closed_paths': sum(bool(x.get('closed')) for x in self.items), 'pending': self.pending is not None, 'region_ownership': 'NOT_ESTABLISHED', 'new_geometry_is_source_fitted': True, 'geometry': 'NOT_ACCEPTED'}

    def _render_geometry(self, scale):
        if scale not in (1,4,16):
            raise ValueError('Scale must be 1,4,16')
        # Budget vector zoom rendering to 16 million pixels per preview.
        if self.width*self.height*scale*scale > 16000000:
            raise ValueError('Preview pixel budget exceeded; inspect source ROI instead')
        chains = []
        for index,item in enumerate(self.items):
            cc = np.asarray(item['curves'])
            chains.append({'id': index, 'closed': bool(np.array_equal(cc[0,0],cc[-1,-1])), 'adjacent_face_labels': [1,2], 'segments': [dict(type='C', **{key: point.tolist() for key,point in zip(('p0','p1','p2','p3'),c)}) for c in cc]})
        graph = {'width': self.width, 'height': self.height, 'chains': chains, 'faces': {}}
        name = 'geometry_%02d_%dx' % (len(self.events),scale)
        svg = self.output / (name+'.svg');png = self.output / (name+'.png')
        svg.write_text(self.serializer.svg_graph(graph),encoding='utf-8')
        started = time.monotonic()
        result = subprocess.run([str(self.renderer), '--width', str(self.width*scale), str(svg), str(png)],capture_output=True,timeout=30)
        if result.returncode:
            raise ValueError('Trusted SVG renderer failed')
        return {'svg': svg.name, 'png': png.name, 'state_hash': self.state_hash(), 'render_seconds': time.monotonic()-started, 'scale': scale}

    def dispatch(self, name, arguments):
        if len(self.events) >= self.max_calls:
            raise ValueError('Tool-call budget exceeded')
        before = self.state_hash()
        validated = False
        try:
            if not isinstance(name,str) or name not in self.schemas:
                raise ValueError('Tool is not allowlisted')
            validate_tool_value(arguments,self.schemas[name]);validated = True
            result = getattr(self,'_'+name)(**arguments)
            status = 'ok'
        except (ValueError, KeyError, TypeError, subprocess.TimeoutExpired) as exc:
            result = {'error': str(exc)};status = 'rejected'
        event = {'sequence': len(self.events), 'tool': name if isinstance(name,str) and name in self.schemas else 'UNKNOWN_TOOL', 'arguments': arguments if validated else None, 'status': status, 'result': result, 'before_hash': before, 'after_hash': self.state_hash(), 'previous_record_hash': self.events[-1]['record_hash'] if self.events else self.source_pin}
        # Runtime metadata belongs to journal evidence, never geometry identity.
        event['record_hash'] = geometry_digest(event)
        file = self.output / ('event_%03d.json' % len(self.events))
        with file.open('x',encoding='utf-8') as handle: json.dump(event,handle,indent=2,allow_nan=False)
        self.events.append(event)
        return copy.deepcopy(result)

    def export_state(self):
        return {'accepted': copy.deepcopy(self.items), 'state_hash': self.state_hash(), 'initial_hash': self.initial_hash, 'pending': self.pending is not None, 'commits': self.commits, 'calls': len(self.events), 'source_pin': self.source_pin, 'geometry': 'NOT_ACCEPTED', 'region_ownership': 'NOT_ESTABLISHED'}

    def replay_decision_hash(self):
        """Stable geometry/action decisions, independent of measured durations."""
        rows = []
        for event in self.events:
            result = event['result']
            ledger = [{'trace_id': row['trace_id'], 'status': row['status'], 'accepted_paths': row.get('accepted_paths',0), 'rejections': row.get('rejections',[]), 'intervals': [{key: interval.get(key) for key in ('lo','hi','status','reason','cubics')} for interval in row.get('interval_ledger',[])]} for row in result.get('ledger',[])]
            rows.append({'tool': event['tool'], 'arguments': event['arguments'], 'status': event['status'], 'before_hash': event['before_hash'], 'after_hash': event['after_hash'], 'decision': result.get('status'), 'error': result.get('error'), 'ledger': ledger})
        return geometry_digest(rows)
# END CHANGE AGD-AGENTIC-TOOLS | 2026-10-31T11:54:38Z | EDITED | Author: geometry_tools
