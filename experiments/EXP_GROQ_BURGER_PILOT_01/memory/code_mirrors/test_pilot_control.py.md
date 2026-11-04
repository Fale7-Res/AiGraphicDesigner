# مرآة الكود التفصيلية: `test_pilot_control.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_pilot_control.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_pilot_control.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `120` (`Lines 1–120`)
- **بصمة الملف (`SHA-256`):** `63900d3f1be9558f4fae1fde946b11d7861f2b51ed86e5bbc0e5246c11ee5984`
- **الوصف التفصيلي:** # START CHANGE AGD-PILOT-TEST | 2026-10-31T16:16:43Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `reply` | `function` | `Lines 13–15` | `def reply(cid='call_1', content=None):` | رمز برمجي موثق. |
| `FakeEngine` | `class` | `Lines 18–25` | `class FakeEngine:` | رمز برمجي موثق. |
| `FakeEngine.__init__` | `method` | `Lines 19–22` | `def __init__(self):` | رمز برمجي موثق. |
| `FakeEngine.state_hash` | `method` | `Lines 23–23` | `def state_hash(self):return digest(self.items)` | رمز برمجي موثق. |
| `FakeEngine.dispatch` | `method` | `Lines 24–25` | `def dispatch(self,name,args):` | رمز برمجي موثق. |
| `SyntheticAdapter` | `class` | `Lines 28–32` | `class SyntheticAdapter:` | رمز برمجي موثق. |
| `SyntheticAdapter.__init__` | `method` | `Lines 30–30` | `def __init__(self,value=None):self.value=value or reply();self.calls=0` | رمز برمجي موثق. |
| `SyntheticAdapter._prepare` | `method` | `Lines 31–31` | `def _prepare(self,*args):return b'',args[0][0]['hashes'],1000` | رمز برمجي موثق. |
| `SyntheticAdapter.request` | `method` | `Lines 32–32` | `def request(self,*args):self.calls+=1;return copy.deepcopy(self.value)` | رمز برمجي موثق. |
| `ControlsTest` | `class` | `Lines 35–116` | `class ControlsTest(unittest.TestCase):` | رمز برمجي موثق. |
| `ControlsTest.setUp` | `method` | `Lines 36–39` | `def setUp(self):` | رمز برمجي موثق. |
| `ControlsTest.tearDown` | `method` | `Lines 40–40` | `def tearDown(self):self.tmp.cleanup()` | رمز برمجي موثق. |
| `ControlsTest.build` | `method` | `Lines 41–41` | `def build(self,e,s):return [dict(hashes=[s['preview']['sha256']])],[]` | رمز برمجي موثق. |
| `ControlsTest.preview` | `method` | `Lines 42–45` | `def preview(self,e,s):` | رمز برمجي موثق. |
| `ControlsTest.approve` | `method` | `Lines 46–47` | `def approve(self):` | رمز برمجي موثق. |
| `ControlsTest.step` | `method` | `Lines 48–48` | `def step(self,a=None,clock=100):return self.s.step(self.engine,a or SyntheticAdapter(),self.build,self.preview,lambda:clock)` | رمز برمجي موثق. |
| `ControlsTest.test_two_steps_restart_preserves_budget` | `method` | `Lines 49–56` | `def test_two_steps_restart_preserves_budget(self):` | رمز برمجي موثق. |
| `ControlsTest.test_wrong_identity_index_and_hash` | `method` | `Lines 57–59` | `def test_wrong_identity_index_and_hash(self):` | رمز برمجي موثق. |
| `ControlsTest.test_preview_substitution` | `method` | `Lines 60–63` | `def test_preview_substitution(self):` | رمز برمجي موثق. |
| `ControlsTest.test_duplicate_call_no_reexecution` | `method` | `Lines 64–67` | `def test_duplicate_call_no_reexecution(self):` | رمز برمجي موثق. |
| `ControlsTest.test_invalid_model_consumes_reservation_and_halts` | `method` | `Lines 68–73` | `def test_invalid_model_consumes_reservation_and_halts(self):` | رمز برمجي موثق. |
| `ControlsTest.test_ambiguous_provider_failure_never_retried` | `method` | `Lines 74–80` | `def test_ambiguous_provider_failure_never_retried(self):` | رمز برمجي موثق. |
| `ControlsTest.test_ambiguous_provider_failure_never_retried.Fail` | `nested_class` | `Lines 75–76` | `class Fail(SyntheticAdapter):` | رمز برمجي موثق. |
| `ControlsTest.test_ambiguous_provider_failure_never_retried.Fail.request` | `method` | `Lines 76–76` | `def request(self,*a):raise RuntimeError('do not log arbitrary provider body')` | رمز برمجي موثق. |
| `ControlsTest.test_reserved_crash_state_blocks_resume` | `method` | `Lines 81–83` | `def test_reserved_crash_state_blocks_resume(self):` | رمز برمجي موثق. |
| `ControlsTest.test_journal_tampering_and_missing_record` | `method` | `Lines 84–86` | `def test_journal_tampering_and_missing_record(self):` | رمز برمجي موثق. |
| `ControlsTest.test_lock_blocks_competing_process` | `method` | `Lines 87–89` | `def test_lock_blocks_competing_process(self):` | رمز برمجي موثق. |
| `ControlsTest.test_observation_sanitized_without_authority` | `method` | `Lines 90–94` | `def test_observation_sanitized_without_authority(self):` | رمز برمجي موثق. |
| `ControlsTest.test_observation_extra_keys_nan_and_degenerate_roi` | `method` | `Lines 95–100` | `def test_observation_extra_keys_nan_and_degenerate_roi(self):` | رمز برمجي موثق. |
| `ControlsTest.test_image_set_and_token_limits_before_transport` | `method` | `Lines 101–108` | `def test_image_set_and_token_limits_before_transport(self):` | رمز برمجي موثق. |
| `ControlsTest.test_tool_budget_never_refilled` | `method` | `Lines 109–112` | `def test_tool_budget_never_refilled(self):` | رمز برمجي موثق. |
| `ControlsTest.test_live_adapter_cannot_enter_synthetic_session` | `method` | `Lines 113–116` | `def test_live_adapter_cannot_enter_synthetic_session(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `reply` — `Lines 13–15`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `15` (`Lines 13–15`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 13–15`):**
```python
def reply(cid='call_1', content=None):
    obs=dict(missing_components=['unverified local contour'],roi=[0,0,1,1],uncertainty=.7,chosen_action='inspect candidates',unavailable_capabilities=['new boundaries'],stop_reason='')
    return dict(status='SYNTHETIC',message=dict(content=content or json.dumps(obs),tool_calls=[dict(id=cid,type='function',function=dict(name='get_candidates',arguments='{"roi":[0,0,1,1],"limit":2}'))]),usage=dict(prompt_tokens=80,completion_tokens=20,total_tokens=100))
```

### `FakeEngine` — `Lines 18–25`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `25` (`Lines 18–25`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 18–25`):**
```python
class FakeEngine:
    def __init__(self):
        from geometry_engine import geometry_tool_schemas
        self.items=[];self.pending=None;self.history=[];self.events=[];self.commits=0;self.source_pin='source'
        self.schemas={t['function']['name']:t['function']['parameters'] for t in geometry_tool_schemas()}
    def state_hash(self):return digest(self.items)
    def dispatch(self,name,args):
        self.events.append(dict(tool=name,arguments=args));return dict(status='observed')
```

### `FakeEngine.__init__` — `Lines 19–22`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `19` إلى السطر `22` (`Lines 19–22`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 19–22`):**
```python
    def __init__(self):
        from geometry_engine import geometry_tool_schemas
        self.items=[];self.pending=None;self.history=[];self.events=[];self.commits=0;self.source_pin='source'
        self.schemas={t['function']['name']:t['function']['parameters'] for t in geometry_tool_schemas()}
```

### `FakeEngine.state_hash` — `Lines 23–23`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `23` إلى السطر `23` (`Lines 23–23`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 23–23`):**
```python
    def state_hash(self):return digest(self.items)
```

### `FakeEngine.dispatch` — `Lines 24–25`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `24` إلى السطر `25` (`Lines 24–25`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 24–25`):**
```python
    def dispatch(self,name,args):
        self.events.append(dict(tool=name,arguments=args));return dict(status='observed')
```

### `SyntheticAdapter` — `Lines 28–32`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `28` إلى السطر `32` (`Lines 28–32`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 28–32`):**
```python
class SyntheticAdapter:
    live=False
    def __init__(self,value=None):self.value=value or reply();self.calls=0
    def _prepare(self,*args):return b'',args[0][0]['hashes'],1000
    def request(self,*args):self.calls+=1;return copy.deepcopy(self.value)
```

### `SyntheticAdapter.__init__` — `Lines 30–30`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `30` إلى السطر `30` (`Lines 30–30`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 30–30`):**
```python
    def __init__(self,value=None):self.value=value or reply();self.calls=0
```

### `SyntheticAdapter._prepare` — `Lines 31–31`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `31` إلى السطر `31` (`Lines 31–31`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 31–31`):**
```python
    def _prepare(self,*args):return b'',args[0][0]['hashes'],1000
```

### `SyntheticAdapter.request` — `Lines 32–32`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `32` إلى السطر `32` (`Lines 32–32`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 32–32`):**
```python
    def request(self,*args):self.calls+=1;return copy.deepcopy(self.value)
```

### `ControlsTest` — `Lines 35–116`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `35` إلى السطر `116` (`Lines 35–116`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 35–116`):**
```python
class ControlsTest(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);self.engine=FakeEngine();self.s=PilotSession(self.root/'s')
        p=self.root/'image.png';p.write_bytes(b'synthetic preview zero');self.h=hashlib.sha256(p.read_bytes()).hexdigest()
        self.s.create('test',self.engine,dict(file='preview_00.png',sha256=self.h),{},preview_source=p)
    def tearDown(self):self.tmp.cleanup()
    def build(self,e,s):return [dict(hashes=[s['preview']['sha256']])],[]
    def preview(self,e,s):
        e.dispatch('render_geometry',{})
        p=self.s.directory/f"preview_{s['requests']:02d}.png";p.write_bytes(str(s['requests']).encode())
        return dict(file=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest()),{}
    def approve(self):
        state,_,_=self.s.read();self.s.approve('test',state['requests'],state['preview']['sha256'])
    def step(self,a=None,clock=100):return self.s.step(self.engine,a or SyntheticAdapter(),self.build,self.preview,lambda:clock)
    def test_two_steps_restart_preserves_budget(self):
        self.approve();first=self.step();self.assertEqual(first['phase'],'WAITING_APPROVAL')
        self.s=PilotSession(self.s.directory);self.engine=FakeEngine()
        with self.assertRaises(PilotStop):self.step(SyntheticAdapter(reply('call_2')),200)
        self.approve();second=self.step(SyntheticAdapter(reply('call_2')),200)
        self.assertEqual((second['requests'],second['reserved_tokens'],second['completion_tokens']),(2,2000,40))
        self.assertEqual(len(second['actions']),2)
        with self.assertRaises(PilotStop):self.step(clock=300)
    def test_wrong_identity_index_and_hash(self):
        for ident,index,h in [('other',0,self.h),('test',1,self.h),('test',0,'0'*64)]:
            with self.assertRaises(PilotStop):self.s.approve(ident,index,h)
    def test_preview_substitution(self):
        self.approve();(self.s.directory/'preview_00.png').write_bytes(b'changed');a=SyntheticAdapter()
        with self.assertRaises(PilotStop):self.step(a)
        self.assertEqual(a.calls,0)
    def test_duplicate_call_no_reexecution(self):
        self.approve();self.step();self.approve();a=SyntheticAdapter(reply())
        with self.assertRaises(PilotStop):self.step(a,200)
        self.assertEqual(self.s.read()[0]['phase'],'HALTED');self.assertEqual(len(self.engine.events),3)
    def test_invalid_model_consumes_reservation_and_halts(self):
        self.approve();a=SyntheticAdapter(reply(content='not JSON'))
        with self.assertRaises(PilotStop):self.step(a)
        state,_,_=self.s.read();self.assertEqual((state['requests'],state['reserved_tokens'],state['phase']),(1,1000,'HALTED'))
        with self.assertRaises(PilotStop):self.step(a,200)
        self.assertEqual(a.calls,1)
    def test_ambiguous_provider_failure_never_retried(self):
        class Fail(SyntheticAdapter):
            def request(self,*a):raise RuntimeError('do not log arbitrary provider body')
        self.approve()
        with self.assertRaises(PilotStop):self.step(Fail())
        self.assertNotIn('arbitrary', ''.join(p.read_text() for p in self.s.directory.glob('record*')))
        with self.assertRaises(PilotStop):self.step(clock=200)
    def test_reserved_crash_state_blocks_resume(self):
        s,_,_=self.s.read();s['phase']='RESERVED';s['requests']=1;s['reserved_tokens']=1000;self.s.append(s,'REQUEST_RESERVED')
        with self.assertRaises(PilotStop):self.step()
    def test_journal_tampering_and_missing_record(self):
        self.approve();p=self.s.directory/'record_001.json';data=json.loads(p.read_text());data['state']['requests']=1;p.write_text(json.dumps(data))
        with self.assertRaises(PilotStop):self.s.read()
    def test_lock_blocks_competing_process(self):
        (self.s.directory/'LOCK').write_text('')
        with self.assertRaises(PilotStop):self.approve()
    def test_observation_sanitized_without_authority(self):
        raw=json.loads(reply()['message']['content']);raw['chosen_action']='gsk_SYNTHETIC_NOT_A_REAL_CREDENTIAL Bearer dummysecret'
        self.approve();self.step(SyntheticAdapter(reply(content=json.dumps(raw))))
        text=''.join(p.read_text() for p in self.s.directory.glob('record*'))
        self.assertNotIn('dummysecret',text);self.assertNotIn('gsk_SYNTHETIC',text);self.assertIn('UNTRUSTED_PLANNER_OBSERVATION',text)
    def test_observation_extra_keys_nan_and_degenerate_roi(self):
        raw=json.loads(reply()['message']['content'])
        for key,value in [('authority','accepted'),('roi',[0,0,0,1]),('uncertainty',float('nan'))]:
            bad=dict(raw);bad[key]=value
            with self.assertRaises(PilotStop):observation(json.dumps(bad))
        with self.assertRaises(PilotStop):observation('{"roi":[],"roi":[]}')
    def test_image_set_and_token_limits_before_transport(self):
        self.approve();a=SyntheticAdapter()
        a._prepare=lambda *x:(b'', ['wrong'],1000)
        with self.assertRaises(PilotStop):self.step(a)
        self.assertEqual(a.calls,0)
        a._prepare=lambda *x:(b'',[self.h],15001)
        with self.assertRaises(PilotStop):self.step(a)
        self.assertEqual(a.calls,0)
    def test_tool_budget_never_refilled(self):
        state,_,_=self.s.read();state['engine']['events']=[{}]*12;self.s.append(state,'TEST_EXHAUSTED');self.approve()
        with self.assertRaises(PilotStop):self.step()
        self.assertEqual(self.s.read()[0]['phase'],'HALTED')
    def test_live_adapter_cannot_enter_synthetic_session(self):
        self.approve();a=SyntheticAdapter();a.live=True
        with self.assertRaises(PilotStop):self.step(a)
        self.assertEqual(a.calls,0)
```

### `ControlsTest.setUp` — `Lines 36–39`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `36` إلى السطر `39` (`Lines 36–39`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 36–39`):**
```python
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);self.engine=FakeEngine();self.s=PilotSession(self.root/'s')
        p=self.root/'image.png';p.write_bytes(b'synthetic preview zero');self.h=hashlib.sha256(p.read_bytes()).hexdigest()
        self.s.create('test',self.engine,dict(file='preview_00.png',sha256=self.h),{},preview_source=p)
```

### `ControlsTest.tearDown` — `Lines 40–40`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `40` إلى السطر `40` (`Lines 40–40`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 40–40`):**
```python
    def tearDown(self):self.tmp.cleanup()
```

### `ControlsTest.build` — `Lines 41–41`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `41` إلى السطر `41` (`Lines 41–41`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 41–41`):**
```python
    def build(self,e,s):return [dict(hashes=[s['preview']['sha256']])],[]
```

### `ControlsTest.preview` — `Lines 42–45`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `42` إلى السطر `45` (`Lines 42–45`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 42–45`):**
```python
    def preview(self,e,s):
        e.dispatch('render_geometry',{})
        p=self.s.directory/f"preview_{s['requests']:02d}.png";p.write_bytes(str(s['requests']).encode())
        return dict(file=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest()),{}
```

### `ControlsTest.approve` — `Lines 46–47`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `46` إلى السطر `47` (`Lines 46–47`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 46–47`):**
```python
    def approve(self):
        state,_,_=self.s.read();self.s.approve('test',state['requests'],state['preview']['sha256'])
```

### `ControlsTest.step` — `Lines 48–48`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `48` إلى السطر `48` (`Lines 48–48`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 48–48`):**
```python
    def step(self,a=None,clock=100):return self.s.step(self.engine,a or SyntheticAdapter(),self.build,self.preview,lambda:clock)
```

### `ControlsTest.test_two_steps_restart_preserves_budget` — `Lines 49–56`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `49` إلى السطر `56` (`Lines 49–56`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 49–56`):**
```python
    def test_two_steps_restart_preserves_budget(self):
        self.approve();first=self.step();self.assertEqual(first['phase'],'WAITING_APPROVAL')
        self.s=PilotSession(self.s.directory);self.engine=FakeEngine()
        with self.assertRaises(PilotStop):self.step(SyntheticAdapter(reply('call_2')),200)
        self.approve();second=self.step(SyntheticAdapter(reply('call_2')),200)
        self.assertEqual((second['requests'],second['reserved_tokens'],second['completion_tokens']),(2,2000,40))
        self.assertEqual(len(second['actions']),2)
        with self.assertRaises(PilotStop):self.step(clock=300)
```

### `ControlsTest.test_wrong_identity_index_and_hash` — `Lines 57–59`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `57` إلى السطر `59` (`Lines 57–59`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 57–59`):**
```python
    def test_wrong_identity_index_and_hash(self):
        for ident,index,h in [('other',0,self.h),('test',1,self.h),('test',0,'0'*64)]:
            with self.assertRaises(PilotStop):self.s.approve(ident,index,h)
```

### `ControlsTest.test_preview_substitution` — `Lines 60–63`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `60` إلى السطر `63` (`Lines 60–63`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 60–63`):**
```python
    def test_preview_substitution(self):
        self.approve();(self.s.directory/'preview_00.png').write_bytes(b'changed');a=SyntheticAdapter()
        with self.assertRaises(PilotStop):self.step(a)
        self.assertEqual(a.calls,0)
```

### `ControlsTest.test_duplicate_call_no_reexecution` — `Lines 64–67`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `64` إلى السطر `67` (`Lines 64–67`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 64–67`):**
```python
    def test_duplicate_call_no_reexecution(self):
        self.approve();self.step();self.approve();a=SyntheticAdapter(reply())
        with self.assertRaises(PilotStop):self.step(a,200)
        self.assertEqual(self.s.read()[0]['phase'],'HALTED');self.assertEqual(len(self.engine.events),3)
```

### `ControlsTest.test_invalid_model_consumes_reservation_and_halts` — `Lines 68–73`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `68` إلى السطر `73` (`Lines 68–73`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 68–73`):**
```python
    def test_invalid_model_consumes_reservation_and_halts(self):
        self.approve();a=SyntheticAdapter(reply(content='not JSON'))
        with self.assertRaises(PilotStop):self.step(a)
        state,_,_=self.s.read();self.assertEqual((state['requests'],state['reserved_tokens'],state['phase']),(1,1000,'HALTED'))
        with self.assertRaises(PilotStop):self.step(a,200)
        self.assertEqual(a.calls,1)
```

### `ControlsTest.test_ambiguous_provider_failure_never_retried` — `Lines 74–80`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `74` إلى السطر `80` (`Lines 74–80`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 74–80`):**
```python
    def test_ambiguous_provider_failure_never_retried(self):
        class Fail(SyntheticAdapter):
            def request(self,*a):raise RuntimeError('do not log arbitrary provider body')
        self.approve()
        with self.assertRaises(PilotStop):self.step(Fail())
        self.assertNotIn('arbitrary', ''.join(p.read_text() for p in self.s.directory.glob('record*')))
        with self.assertRaises(PilotStop):self.step(clock=200)
```

### `ControlsTest.test_ambiguous_provider_failure_never_retried.Fail` — `Lines 75–76`
- **النوع:** `nested_class`
- **نطاق الأسطر الدقيق:** من السطر `75` إلى السطر `76` (`Lines 75–76`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 75–76`):**
```python
        class Fail(SyntheticAdapter):
            def request(self,*a):raise RuntimeError('do not log arbitrary provider body')
```

### `ControlsTest.test_ambiguous_provider_failure_never_retried.Fail.request` — `Lines 76–76`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `76` إلى السطر `76` (`Lines 76–76`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 76–76`):**
```python
            def request(self,*a):raise RuntimeError('do not log arbitrary provider body')
```

### `ControlsTest.test_reserved_crash_state_blocks_resume` — `Lines 81–83`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `81` إلى السطر `83` (`Lines 81–83`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 81–83`):**
```python
    def test_reserved_crash_state_blocks_resume(self):
        s,_,_=self.s.read();s['phase']='RESERVED';s['requests']=1;s['reserved_tokens']=1000;self.s.append(s,'REQUEST_RESERVED')
        with self.assertRaises(PilotStop):self.step()
```

### `ControlsTest.test_journal_tampering_and_missing_record` — `Lines 84–86`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `84` إلى السطر `86` (`Lines 84–86`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 84–86`):**
```python
    def test_journal_tampering_and_missing_record(self):
        self.approve();p=self.s.directory/'record_001.json';data=json.loads(p.read_text());data['state']['requests']=1;p.write_text(json.dumps(data))
        with self.assertRaises(PilotStop):self.s.read()
```

### `ControlsTest.test_lock_blocks_competing_process` — `Lines 87–89`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `87` إلى السطر `89` (`Lines 87–89`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 87–89`):**
```python
    def test_lock_blocks_competing_process(self):
        (self.s.directory/'LOCK').write_text('')
        with self.assertRaises(PilotStop):self.approve()
```

### `ControlsTest.test_observation_sanitized_without_authority` — `Lines 90–94`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `90` إلى السطر `94` (`Lines 90–94`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 90–94`):**
```python
    def test_observation_sanitized_without_authority(self):
        raw=json.loads(reply()['message']['content']);raw['chosen_action']='gsk_SYNTHETIC_NOT_A_REAL_CREDENTIAL Bearer dummysecret'
        self.approve();self.step(SyntheticAdapter(reply(content=json.dumps(raw))))
        text=''.join(p.read_text() for p in self.s.directory.glob('record*'))
        self.assertNotIn('dummysecret',text);self.assertNotIn('gsk_SYNTHETIC',text);self.assertIn('UNTRUSTED_PLANNER_OBSERVATION',text)
```

### `ControlsTest.test_observation_extra_keys_nan_and_degenerate_roi` — `Lines 95–100`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `95` إلى السطر `100` (`Lines 95–100`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 95–100`):**
```python
    def test_observation_extra_keys_nan_and_degenerate_roi(self):
        raw=json.loads(reply()['message']['content'])
        for key,value in [('authority','accepted'),('roi',[0,0,0,1]),('uncertainty',float('nan'))]:
            bad=dict(raw);bad[key]=value
            with self.assertRaises(PilotStop):observation(json.dumps(bad))
        with self.assertRaises(PilotStop):observation('{"roi":[],"roi":[]}')
```

### `ControlsTest.test_image_set_and_token_limits_before_transport` — `Lines 101–108`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `101` إلى السطر `108` (`Lines 101–108`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 101–108`):**
```python
    def test_image_set_and_token_limits_before_transport(self):
        self.approve();a=SyntheticAdapter()
        a._prepare=lambda *x:(b'', ['wrong'],1000)
        with self.assertRaises(PilotStop):self.step(a)
        self.assertEqual(a.calls,0)
        a._prepare=lambda *x:(b'',[self.h],15001)
        with self.assertRaises(PilotStop):self.step(a)
        self.assertEqual(a.calls,0)
```

### `ControlsTest.test_tool_budget_never_refilled` — `Lines 109–112`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `109` إلى السطر `112` (`Lines 109–112`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 109–112`):**
```python
    def test_tool_budget_never_refilled(self):
        state,_,_=self.s.read();state['engine']['events']=[{}]*12;self.s.append(state,'TEST_EXHAUSTED');self.approve()
        with self.assertRaises(PilotStop):self.step()
        self.assertEqual(self.s.read()[0]['phase'],'HALTED')
```

### `ControlsTest.test_live_adapter_cannot_enter_synthetic_session` — `Lines 113–116`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `113` إلى السطر `116` (`Lines 113–116`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 113–116`):**
```python
    def test_live_adapter_cannot_enter_synthetic_session(self):
        self.approve();a=SyntheticAdapter();a.live=True
        with self.assertRaises(PilotStop):self.step(a)
        self.assertEqual(a.calls,0)
```
