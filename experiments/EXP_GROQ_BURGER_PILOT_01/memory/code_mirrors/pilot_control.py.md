# مرآة الكود التفصيلية: `pilot_control.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `pilot_control.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `pilot_control.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `267` (`Lines 1–267`)
- **بصمة الملف (`SHA-256`):** `7cdea3ebd52f3cfe378aeca6f225ad8aef17bb5247047f1e86568ea6f4d04eaf`
- **الوصف التفصيلي:** # START CHANGE AGD-PILOT-HARDEN | 2026-11-04T15:37:25Z | EDITED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `PilotStop` | `class` | `Lines 17–18` | `class PilotStop(ValueError):` | رمز برمجي موثق. |
| `digest` | `function` | `Lines 21–22` | `def digest(value):` | رمز برمجي موثق. |
| `strict_json` | `function` | `Lines 25–31` | `def strict_json(text):` | رمز برمجي موثق. |
| `unique_pairs` | `function` | `Lines 34–39` | `def unique_pairs(items):` | رمز برمجي موثق. |
| `safe_text` | `function` | `Lines 42–46` | `def safe_text(value):` | رمز برمجي موثق. |
| `observation` | `function` | `Lines 49–65` | `def observation(content):` | رمز برمجي موثق. |
| `engine_snapshot` | `function` | `Lines 68–69` | `def engine_snapshot(engine):` | رمز برمجي موثق. |
| `implementation_pin` | `function` | `Lines 72–79` | `def implementation_pin(engine):` | رمز برمجي موثق. |
| `PilotSession` | `class` | `Lines 82–258` | `class PilotSession:` | One owner-approved preview per request; all budgets survive restarts. |
| `PilotSession.__init__` | `method` | `Lines 86–87` | `def __init__(self, directory):` | رمز برمجي موثق. |
| `PilotSession.locked` | `method` | `Lines 90–100` | `def locked(self):` | رمز برمجي موثق. |
| `PilotSession.read` | `method` | `Lines 102–119` | `def read(self):` | رمز برمجي موثق. |
| `PilotSession.append` | `method` | `Lines 121–132` | `def append(self, state, kind):` | رمز برمجي موثق. |
| `PilotSession.create` | `method` | `Lines 134–149` | `def create(self, identity, engine, preview, context, mode='synthetic', preview_source=None):` | رمز برمجي موثق. |
| `PilotSession._check_preview` | `method` | `Lines 151–154` | `def _check_preview(self, preview):` | رمز برمجي موثق. |
| `PilotSession.approve` | `method` | `Lines 156–164` | `def approve(self, identity, request_index, sha256):` | رمز برمجي موثق. |
| `PilotSession.step` | `method` | `Lines 166–258` | `def step(self, engine, adapter, build_request, make_preview, clock):` | Reserve durably before provider/tool effects; failures stay HALTED. |
| `strict_json_record` | `function` | `Lines 261–266` | `def strict_json_record(path):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `PilotStop` — `Lines 17–18`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `17` إلى السطر `18` (`Lines 17–18`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 17–18`):**
```python
class PilotStop(ValueError):
    pass
```

### `digest` — `Lines 21–22`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `21` إلى السطر `22` (`Lines 21–22`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 21–22`):**
```python
def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()
```

### `strict_json` — `Lines 25–31`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `25` إلى السطر `31` (`Lines 25–31`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 25–31`):**
```python
def strict_json(text):
    if not isinstance(text, str) or len(text.encode()) > 16000:
        raise PilotStop('Invalid bounded JSON')
    try:
        return json.loads(text, object_pairs_hook=unique_pairs, parse_constant=lambda _: (_ for _ in ()).throw(PilotStop('Nonfinite JSON')))
    except (ValueError, RecursionError):
        raise PilotStop('Invalid JSON') from None
```

### `unique_pairs` — `Lines 34–39`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `34` إلى السطر `39` (`Lines 34–39`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 34–39`):**
```python
def unique_pairs(items):
    result={}
    for key,value in items:
        if key in result:raise PilotStop('Duplicate JSON key')
        result[key]=value
    return result
```

### `safe_text` — `Lines 42–46`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `42` إلى السطر `46` (`Lines 42–46`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 42–46`):**
```python
def safe_text(value):
    if not isinstance(value, str) or len(value) > 500:
        raise PilotStop('Invalid observation text')
    value = re.sub(r'gsk_[A-Za-z0-9_-]+|(?i:Bearer)\s+\S+|(?i:(?:api[_ -]?key|authorization))\s*[:=]\s*\S+', '[REDACTED]', value)
    return ''.join(c for c in value if c >= ' ' and c not in '\x7f')
```

### `observation` — `Lines 49–65`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `49` إلى السطر `65` (`Lines 49–65`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 49–65`):**
```python
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
```

### `engine_snapshot` — `Lines 68–69`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `68` إلى السطر `69` (`Lines 68–69`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 68–69`):**
```python
def engine_snapshot(engine):
    return copy.deepcopy({k: getattr(engine, k) for k in ('items', 'pending', 'history', 'events', 'commits')})
```

### `implementation_pin` — `Lines 72–79`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `72` إلى السطر `79` (`Lines 72–79`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 72–79`):**
```python
def implementation_pin(engine):
    import sys
    paths=[Path(__file__),Path(sys.modules[engine.__class__.__module__].__file__)]
    for name in ('partition','serializer'):
        if hasattr(engine,name):paths.append(Path(getattr(engine,name).__file__))
    cli=Path(__file__).with_name('hardened_pilot.py')
    if cli.exists():paths.append(cli)
    return digest({str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
```

### `PilotSession` — `Lines 82–258`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `82` إلى السطر `258` (`Lines 82–258`)
- **الوظيفة:** One owner-approved preview per request; all budgets survive restarts.
- **الكود الفعلي (`Lines 82–258`):**
```python
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
```

### `PilotSession.__init__` — `Lines 86–87`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `86` إلى السطر `87` (`Lines 86–87`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 86–87`):**
```python
    def __init__(self, directory):
        self.directory = Path(directory)
```

### `PilotSession.locked` — `Lines 90–100`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `90` إلى السطر `100` (`Lines 90–100`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 90–100`):**
```python
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
```

### `PilotSession.read` — `Lines 102–119`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `102` إلى السطر `119` (`Lines 102–119`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 102–119`):**
```python
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
```

### `PilotSession.append` — `Lines 121–132`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `121` إلى السطر `132` (`Lines 121–132`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 121–132`):**
```python
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
```

### `PilotSession.create` — `Lines 134–149`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `134` إلى السطر `149` (`Lines 134–149`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 134–149`):**
```python
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
```

### `PilotSession._check_preview` — `Lines 151–154`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `151` إلى السطر `154` (`Lines 151–154`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 151–154`):**
```python
    def _check_preview(self, preview):
        path = self.directory/preview['file']
        if Path(preview['file']).name != preview['file'] or not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != preview['sha256']:
            raise PilotStop('Preview substitution or invalid path')
```

### `PilotSession.approve` — `Lines 156–164`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `156` إلى السطر `164` (`Lines 156–164`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 156–164`):**
```python
    def approve(self, identity, request_index, sha256):
        with self.locked():
            s, _, _ = self.read()
            self._check_preview(s['preview'])
            if s['phase'] != 'WAITING_APPROVAL' or identity != s['identity'] or type(request_index) is not int or request_index != s['requests'] or sha256 != s['preview']['sha256']:
                raise PilotStop('Approval identity/index/hash mismatch')
            s['approvals'].append(dict(identity=identity, request_index=request_index, sha256=sha256, authority='OWNER_LOCAL_CLI'))
            s['phase'] = 'APPROVED'
            self.append(s, 'PREVIEW_APPROVED')
```

### `PilotSession.step` — `Lines 166–258`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `166` إلى السطر `258` (`Lines 166–258`)
- **الوظيفة:** Reserve durably before provider/tool effects; failures stay HALTED.
- **الكود الفعلي (`Lines 166–258`):**
```python
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
```

### `strict_json_record` — `Lines 261–266`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `261` إلى السطر `266` (`Lines 261–266`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 261–266`):**
```python
def strict_json_record(path):
    # Geometry snapshots can exceed model JSON limits; finite JSON still mandatory.
    try:
        return json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=unique_pairs,parse_constant=lambda _:(_ for _ in ()).throw(PilotStop('Nonfinite journal')))
    except (ValueError,RecursionError):
        raise PilotStop('Invalid journal') from None
```
