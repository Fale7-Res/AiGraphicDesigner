# START CHANGE AGD-PILOT-HARDEN | 2026-11-04T15:37:25Z | EDITED | Author: root
"""Fail-closed, single-request controller. No credential access in this module.

Append-only full-state records allow audit/restart, not hostile disk-owner security.
An interrupted reserved request is ambiguous and cannot be retried automatically.
"""
import copy
import hashlib
import json
import math
import os
from pathlib import Path
import re
from contextlib import contextmanager


class PilotStop(ValueError):
    pass


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def strict_json(text):
    if not isinstance(text, str) or len(text.encode()) > 16000:
        raise PilotStop('Invalid bounded JSON')
    try:
        return json.loads(text, object_pairs_hook=unique_pairs, parse_constant=lambda _: (_ for _ in ()).throw(PilotStop('Nonfinite JSON')))
    except (ValueError, RecursionError):
        raise PilotStop('Invalid JSON') from None


def unique_pairs(items):
    result={}
    for key,value in items:
        if key in result:raise PilotStop('Duplicate JSON key')
        result[key]=value
    return result


def safe_text(value):
    if not isinstance(value, str) or len(value) > 500:
        raise PilotStop('Invalid observation text')
    value = re.sub(r'gsk_[A-Za-z0-9_-]+|(?i:Bearer)\s+\S+|(?i:(?:api[_ -]?key|authorization))\s*[:=]\s*\S+', '[REDACTED]', value)
    return ''.join(c for c in value if c >= ' ' and c not in '\x7f')


def observation(content):
    data = strict_json(content)
    keys = {'missing_components', 'roi', 'uncertainty', 'chosen_action', 'unavailable_capabilities', 'stop_reason'}
    if not isinstance(data, dict) or set(data) != keys:
        raise PilotStop('Observation schema mismatch')
    roi = data['roi']
    if not isinstance(roi, list) or len(roi) != 4 or any(type(x) not in (int, float) or not math.isfinite(x) or not 0 <= x <= 1 for x in roi) or not (roi[0] < roi[2] and roi[1] < roi[3]):
        raise PilotStop('Invalid normalized ROI')
    if type(data['uncertainty']) not in (int, float) or not math.isfinite(data['uncertainty']) or not 0 <= data['uncertainty'] <= 1:
        raise PilotStop('Invalid uncertainty')
    for key in ('missing_components', 'unavailable_capabilities'):
        if not isinstance(data[key], list) or len(data[key]) > 8:
            raise PilotStop('Invalid observation array')
        data[key] = [safe_text(x) for x in data[key]]
    for key in ('chosen_action', 'stop_reason'):
        data[key] = safe_text(data[key])
    return dict(data, authority='UNTRUSTED_PLANNER_OBSERVATION')


def engine_snapshot(engine):
    return copy.deepcopy({k: getattr(engine, k) for k in ('items', 'pending', 'history', 'events', 'commits')})


def implementation_pin(engine):
    import sys
    paths=[Path(__file__),Path(sys.modules[engine.__class__.__module__].__file__)]
    for name in ('partition','serializer'):
        if hasattr(engine,name):paths.append(Path(getattr(engine,name).__file__))
    cli=Path(__file__).with_name('hardened_pilot.py')
    if cli.exists():paths.append(cli)
    return digest({str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})


class PilotSession:
    """One owner-approved preview per request; all budgets survive restarts."""
    limits = dict(requests=2, tools=12, commits=2, reserved_tokens=15000, completion_tokens=1024)

    def __init__(self, directory):
        self.directory = Path(directory)

    @contextmanager
    def locked(self):
        path = self.directory/'LOCK'
        try:
            fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            raise PilotStop('Session locked; interrupted work requires manual audit') from None
        try:
            os.close(fd)
            yield
        finally:
            path.unlink()

    def read(self):
        files = sorted(self.directory.glob('record_*.json'))
        if not files:
            raise PilotStop('Missing session')
        previous = 'ROOT'
        state = None
        for i, file in enumerate(files):
            if file.name != f'record_{i:03d}.json':
                raise PilotStop('Journal sequence gap')
            row = strict_json_record(file)
            h = row.pop('hash', None)
            if h != digest(row) or row['previous'] != previous or row['sequence'] != i:
                raise PilotStop('Journal integrity failure')
            previous = h
            state = row['state']
        if state['limits'] != self.limits:
            raise PilotStop('Frozen limits changed')
        return state, previous, len(files)

    def append(self, state, kind):
        files = list(self.directory.glob('record_*.json'))
        if files:
            _, previous, count = self.read()
        else:
            previous, count = 'ROOT', 0
        row = dict(sequence=count, previous=previous, kind=kind, state=state)
        row['hash'] = digest(row)
        with (self.directory/f'record_{count:03d}.json').open('x', encoding='utf-8') as f:
            json.dump(row, f, allow_nan=False, sort_keys=True)
            f.flush()
            os.fsync(f.fileno())

    def create(self, identity, engine, preview, context, mode='synthetic', preview_source=None):
        if mode not in ('synthetic', 'live') or not re.fullmatch(r'[A-Za-z0-9_-]{1,40}', identity):
            raise PilotStop('Invalid session identity/mode')
        self.directory.mkdir(parents=True, exist_ok=False)
        if preview_source is not None:
            if Path(preview['file']).name != preview['file']:
                raise PilotStop('Invalid preview path')
            import shutil
            shutil.copyfile(preview_source, self.directory/preview['file'])
        state = dict(identity=identity, mode=mode, source_pin=engine.source_pin, implementation_pin=implementation_pin(engine),
                     limits=self.limits, phase='WAITING_APPROVAL', requests=0,
                     reserved_tokens=0, completion_tokens=0, approvals=[], observations=[],
                     actions=[], call_ids=[], preview=preview, context=context,
                     engine=engine_snapshot(engine), geometry_hash=engine.state_hash(), last_request=None)
        self._check_preview(preview)
        self.append(state, 'CREATED')

    def _check_preview(self, preview):
        path = self.directory/preview['file']
        if Path(preview['file']).name != preview['file'] or not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != preview['sha256']:
            raise PilotStop('Preview substitution or invalid path')

    def approve(self, identity, request_index, sha256):
        with self.locked():
            s, _, _ = self.read()
            self._check_preview(s['preview'])
            if s['phase'] != 'WAITING_APPROVAL' or identity != s['identity'] or type(request_index) is not int or request_index != s['requests'] or sha256 != s['preview']['sha256']:
                raise PilotStop('Approval identity/index/hash mismatch')
            s['approvals'].append(dict(identity=identity, request_index=request_index, sha256=sha256, authority='OWNER_LOCAL_CLI'))
            s['phase'] = 'APPROVED'
            self.append(s, 'PREVIEW_APPROVED')

    def step(self, engine, adapter, build_request, make_preview, clock):
        """Reserve durably before provider/tool effects; failures stay HALTED."""
        with self.locked():
            s, _, _ = self.read()
            if s['phase'] != 'APPROVED' or s['requests'] >= 2:
                raise PilotStop('Request not approved or exhausted')
            self._check_preview(s['preview'])
            if s['source_pin'] != engine.source_pin:
                raise PilotStop('Source identity mismatch')
            if s['implementation_pin'] != implementation_pin(engine):
                raise PilotStop('Implementation changed since session creation')
            for key, value in s['engine'].items():
                setattr(engine, key, copy.deepcopy(value))
            if engine.state_hash() != s['geometry_hash'] or len(engine.events) > 12 or engine.commits > 2:
                raise PilotStop('Invalid geometry/budget snapshot')
            if hasattr(engine,'_validate_state'):
                engine._validate_state(engine.items)
                for i,event in enumerate(engine.events):
                    p=engine.output/f'event_{i:03d}.json'
                    if not p.is_file() or strict_json_record(p)!=event:
                        raise PilotStop('Missing or inconsistent geometry event evidence')
            messages, tools = build_request(engine, s)
            _, hashes, reserve = adapter._prepare(messages, tools)
            if hashes != [s['preview']['sha256']]:
                raise PilotStop('Request images differ from approved preview')
            if s['reserved_tokens'] + reserve > 15000 or s['completion_tokens'] + 512 > 1024:
                raise PilotStop('Persistent token budget exhausted')
            if s['last_request'] is not None and clock()-s['last_request'] < 61:
                raise PilotStop('Request cadence not satisfied')
            if s['mode'] == 'live':
                if not getattr(adapter, 'live', False):
                    raise PilotStop('Live adapter required')
                # Restore every provider-side counter before verifying current account proof.
                adapter._requests = s['requests']; adapter._reserved_tokens = s['reserved_tokens']
                adapter._case_iterations = {'A03_burger': s['requests']}; adapter._last_request = s['last_request']
                adapter._check_live('A03_burger', reserve, hashes)
            elif getattr(adapter, 'live', False):
                raise PilotStop('Synthetic session cannot invoke live adapter')
            s['phase'] = 'RESERVED'; s['requests'] += 1; s['reserved_tokens'] += reserve; s['last_request'] = clock()
            self.append(s, 'REQUEST_RESERVED')
            usage_recorded=False
            try:
                result = adapter.request(messages, tools, 'A03_burger')
                if result['status'] not in (['LIVE'] if s['mode'] == 'live' else ['SYNTHETIC']):
                    raise PilotStop('Unexpected provider result')
                usage = result['usage']
                if any(type(usage.get(k)) is not int or usage[k] < 0 for k in ('prompt_tokens','completion_tokens','total_tokens')) or usage['total_tokens'] > reserve or usage['completion_tokens'] > 512 or usage['total_tokens'] != usage['prompt_tokens']+usage['completion_tokens']:
                    raise PilotStop('Invalid usage')
                usage={k:usage[k] for k in ('prompt_tokens','completion_tokens','total_tokens')}
                s['usage']=s.get('usage',[])+[usage]
                s['completion_tokens']+=usage['completion_tokens'];usage_recorded=True
                self.append(s,'USAGE_RECEIVED')
                msg = result['message']; obs = observation(msg.get('content'))
                calls = msg.get('tool_calls', [])
                if not isinstance(calls, list) or len(calls) > 2:
                    raise PilotStop('Tool-call count exceeded')
                validated=[]; seen=set(s['call_ids'])
                # Validate ALL proposals before the first edit; never journal raw content.
                from geometry_engine import validate_tool_value
                for call in calls:
                    cid=call.get('id'); fn=call.get('function', {}); name=fn.get('name')
                    if call.get('type') != 'function' or not isinstance(cid,str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,80}',cid) or cid.lower().startswith('gsk_') or cid in seen or name not in ('get_candidates','stage_candidates','rollback_change'):
                        raise PilotStop('Invalid or duplicate tool identity')
                    seen.add(cid); args=strict_json(fn.get('arguments'))
                    validate_tool_value(args, engine.schemas[name])
                    if name=='stage_candidates' and len(args['trace_ids'])>2:
                        raise PilotStop('Matched candidate limit exceeded')
                    validated.append((cid,name,args))
                required=sum(2 if name=='stage_candidates' else 1 for _,name,_ in validated)+2
                if len(engine.events)+required>12 or engine.commits+sum(name=='stage_candidates' for _,name,_ in validated)>2:
                    raise PilotStop('Persistent tool/commit budget exhausted')
                s['observations'].append(obs)
                # Store received validated decision before any tool effects. Crash => no retry.
                s['call_ids']=list(sorted(seen))
                s['proposals']=[dict(call_id=cid,tool=name,arguments=args) for cid,name,args in validated]
                self.append(s,'VALIDATED_RESPONSE')
                for cid,name,args in validated:
                    response=engine.dispatch(name,args); decision=None
                    if name=='stage_candidates' and engine.pending is not None:
                        decision=engine.dispatch('commit_change' if response.get('added_paths',0) else 'rollback_change',{})
                    s['actions'].append(dict(call_id=cid,tool=name,arguments=args,result=response,decision=decision))
                s['diagnostics']=engine.dispatch('validate_geometry',{})
                s['preview'],s['context']=make_preview(engine,s)
                self._check_preview(s['preview'])
                s['engine']=engine_snapshot(engine);s['geometry_hash']=engine.state_hash()
                s['phase']='COMPLETE' if s['requests']==2 or obs['stop_reason'] else 'WAITING_APPROVAL'
                self.append(s,'STEP_COMPLETED')
            except Exception:
                if not usage_recorded:s['unknown_usage_requests']=s.get('unknown_usage_requests',0)+1
                s['phase']='HALTED';s['error']='Sanitized provider/model/tool failure; no automatic retry'
                self.append(s,'HALTED')
                raise PilotStop(s['error']) from None
            return s


def strict_json_record(path):
    # Geometry snapshots can exceed model JSON limits; finite JSON still mandatory.
    try:
        return json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=unique_pairs,parse_constant=lambda _:(_ for _ in ()).throw(PilotStop('Nonfinite journal')))
    except (ValueError,RecursionError):
        raise PilotStop('Invalid journal') from None
# END CHANGE AGD-PILOT-HARDEN | 2026-11-04T15:37:25Z | EDITED | Author: root
