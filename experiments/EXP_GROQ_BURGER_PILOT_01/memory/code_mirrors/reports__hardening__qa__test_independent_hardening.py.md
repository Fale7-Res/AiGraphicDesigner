# مرآة الكود التفصيلية: `reports/hardening/qa/test_independent_hardening.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `reports/hardening/qa/test_independent_hardening.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `reports/hardening/qa/test_independent_hardening.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `197` (`Lines 1–197`)
- **بصمة الملف (`SHA-256`):** `313bc1c210c7f1b60937f32edf238f67bcf3627f4ef961484b36faeb00b0ca1b`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `IndependentEngineDouble` | `class` | `Lines 18–27` | `class IndependentEngineDouble:` | رمز برمجي موثق. |
| `IndependentEngineDouble.__init__` | `method` | `Lines 19–22` | `def __init__(self):` | رمز برمجي موثق. |
| `IndependentEngineDouble.state_hash` | `method` | `Lines 23–24` | `def state_hash(self):` | رمز برمجي موثق. |
| `IndependentEngineDouble.dispatch` | `method` | `Lines 25–27` | `def dispatch(self,name,args):` | رمز برمجي موثق. |
| `independent_response` | `function` | `Lines 30–35` | `def independent_response(call_ids=('q1',)):` | رمز برمجي موثق. |
| `IndependentAdapterDouble` | `class` | `Lines 38–46` | `class IndependentAdapterDouble:` | رمز برمجي موثق. |
| `IndependentAdapterDouble.__init__` | `method` | `Lines 40–41` | `def __init__(self,response=None):` | رمز برمجي موثق. |
| `IndependentAdapterDouble._prepare` | `method` | `Lines 42–43` | `def _prepare(self,messages,tools):` | رمز برمجي موثق. |
| `IndependentAdapterDouble.request` | `method` | `Lines 44–46` | `def request(self,*_):` | رمز برمجي موثق. |
| `IndependentHardeningAudit` | `class` | `Lines 49–193` | `class IndependentHardeningAudit(unittest.TestCase):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.setUp` | `method` | `Lines 50–56` | `def setUp(self):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.approve_current` | `method` | `Lines 57–59` | `def approve_current(self):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.request_builder` | `method` | `Lines 60–61` | `def request_builder(self,engine,state):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.next_preview` | `method` | `Lines 62–66` | `def next_preview(self,engine,state):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.run_step` | `method` | `Lines 67–69` | `def run_step(self,adapter=None,now=100):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.test_source_identity_or_no_approval_stops_before_transport` | `method` | `Lines 71–77` | `def test_source_identity_or_no_approval_stops_before_transport(self):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.test_bool_index_and_stale_preview_approval_fail` | `method` | `Lines 79–82` | `def test_bool_index_and_stale_preview_approval_fail(self):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.test_all_proposals_validate_before_any_effect` | `method` | `Lines 84–90` | `def test_all_proposals_validate_before_any_effect(self):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.test_ambiguous_failure_is_reserved_and_not_resumable` | `method` | `Lines 92–102` | `def test_ambiguous_failure_is_reserved_and_not_resumable(self):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.test_ambiguous_failure_is_reserved_and_not_resumable.FailingAdapter` | `nested_class` | `Lines 93–96` | `class FailingAdapter(IndependentAdapterDouble):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.test_ambiguous_failure_is_reserved_and_not_resumable.FailingAdapter.request` | `method` | `Lines 94–96` | `def request(self,*_):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.test_restart_does_not_refund_tokens_tools_or_requests` | `method` | `Lines 104–110` | `def test_restart_does_not_refund_tokens_tools_or_requests(self):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.test_different_request_image_stops_without_reservation` | `method` | `Lines 112–117` | `def test_different_request_image_stops_without_reservation(self):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.test_journal_chain_gap_or_tampering_fail_closed` | `method` | `Lines 119–123` | `def test_journal_chain_gap_or_tampering_fail_closed(self):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.test_journal_duplicate_json_key_rejected` | `method` | `Lines 125–129` | `def test_journal_duplicate_json_key_rejected(self):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.test_private_proof_duplicate_key_rejected` | `method` | `Lines 131–134` | `def test_private_proof_duplicate_key_rejected(self):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.test_missing_geometry_event_stops_before_reservation` | `method` | `Lines 136–147` | `def test_missing_geometry_event_stops_before_reservation(self):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.test_observation_records_remain_untrusted_and_redacted` | `method` | `Lines 149–159` | `def test_observation_records_remain_untrusted_and_redacted(self):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.test_usage_extras_are_not_persisted` | `method` | `Lines 161–167` | `def test_usage_extras_are_not_persisted(self):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.test_known_usage_survives_invalid_observation` | `method` | `Lines 169–176` | `def test_known_usage_survives_invalid_observation(self):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.test_changed_implementation_stops_before_transport` | `method` | `Lines 178–183` | `def test_changed_implementation_stops_before_transport(self):` | رمز برمجي موثق. |
| `IndependentHardeningAudit.test_credential_shaped_tool_identity_is_not_journaled` | `method` | `Lines 185–193` | `def test_credential_shaped_tool_identity_is_not_journaled(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `IndependentEngineDouble` — `Lines 18–27`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `27` (`Lines 18–27`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 18–27`):**
```python
class IndependentEngineDouble:
    def __init__(self):
        self.items=[];self.pending=None;self.history=[];self.events=[];self.commits=0
        self.source_pin='independent-frozen-source'
        self.schemas={t['function']['name']:t['function']['parameters'] for t in geometry_tool_schemas()}
    def state_hash(self):
        return digest(self.items)
    def dispatch(self,name,args):
        self.events.append(dict(tool=name,arguments=args))
        return dict(status='observed')
```

### `IndependentEngineDouble.__init__` — `Lines 19–22`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `19` إلى السطر `22` (`Lines 19–22`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 19–22`):**
```python
    def __init__(self):
        self.items=[];self.pending=None;self.history=[];self.events=[];self.commits=0
        self.source_pin='independent-frozen-source'
        self.schemas={t['function']['name']:t['function']['parameters'] for t in geometry_tool_schemas()}
```

### `IndependentEngineDouble.state_hash` — `Lines 23–24`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `23` إلى السطر `24` (`Lines 23–24`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 23–24`):**
```python
    def state_hash(self):
        return digest(self.items)
```

### `IndependentEngineDouble.dispatch` — `Lines 25–27`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `25` إلى السطر `27` (`Lines 25–27`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 25–27`):**
```python
    def dispatch(self,name,args):
        self.events.append(dict(tool=name,arguments=args))
        return dict(status='observed')
```

### `independent_response` — `Lines 30–35`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `30` إلى السطر `35` (`Lines 30–35`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 30–35`):**
```python
def independent_response(call_ids=('q1',)):
    obs=dict(missing_components=['Unverified boundary'],roi=[0,0,1,1],uncertainty=.8,
        chosen_action='Inspect only',unavailable_capabilities=['region ownership'],stop_reason='')
    calls=[dict(id=cid,type='function',function=dict(name='get_candidates',arguments='{"roi":[0,0,1,1],"limit":1}')) for cid in call_ids]
    return dict(status='SYNTHETIC',message=dict(content=json.dumps(obs),tool_calls=calls),
        usage=dict(prompt_tokens=70,completion_tokens=20,total_tokens=90))
```

### `IndependentAdapterDouble` — `Lines 38–46`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `38` إلى السطر `46` (`Lines 38–46`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 38–46`):**
```python
class IndependentAdapterDouble:
    live=False
    def __init__(self,response=None):
        self.calls=0;self.response=response or independent_response()
    def _prepare(self,messages,tools):
        return b'',messages[0]['image_hashes'],2000
    def request(self,*_):
        self.calls+=1
        return copy.deepcopy(self.response)
```

### `IndependentAdapterDouble.__init__` — `Lines 40–41`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `40` إلى السطر `41` (`Lines 40–41`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 40–41`):**
```python
    def __init__(self,response=None):
        self.calls=0;self.response=response or independent_response()
```

### `IndependentAdapterDouble._prepare` — `Lines 42–43`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `42` إلى السطر `43` (`Lines 42–43`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 42–43`):**
```python
    def _prepare(self,messages,tools):
        return b'',messages[0]['image_hashes'],2000
```

### `IndependentAdapterDouble.request` — `Lines 44–46`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `44` إلى السطر `46` (`Lines 44–46`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 44–46`):**
```python
    def request(self,*_):
        self.calls+=1
        return copy.deepcopy(self.response)
```

### `IndependentHardeningAudit` — `Lines 49–193`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `49` إلى السطر `193` (`Lines 49–193`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 49–193`):**
```python
class IndependentHardeningAudit(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.base=Path(self.tmp.name);self.engine=IndependentEngineDouble()
        self.session=PilotSession(self.base/'session')
        file=self.base/'source.png';file.write_bytes(b'independent synthetic image')
        self.sha=hashlib.sha256(file.read_bytes()).hexdigest()
        self.session.create('independent',self.engine,dict(file='preview_00.png',sha256=self.sha),{},preview_source=file)
    def approve_current(self):
        state,_,_=self.session.read()
        self.session.approve(state['identity'],state['requests'],state['preview']['sha256'])
    def request_builder(self,engine,state):
        return [dict(image_hashes=[state['preview']['sha256']])],[]
    def next_preview(self,engine,state):
        engine.dispatch('render_geometry',{})
        file=self.session.directory/f"preview_{state['requests']:02d}.png"
        file.write_bytes(str(state['requests']).encode())
        return dict(file=file.name,sha256=hashlib.sha256(file.read_bytes()).hexdigest()),{}
    def run_step(self,adapter=None,now=100):
        return self.session.step(self.engine,adapter or IndependentAdapterDouble(),
            self.request_builder,self.next_preview,lambda:now)

    def test_source_identity_or_no_approval_stops_before_transport(self):
        adapter=IndependentAdapterDouble()
        with self.assertRaises(PilotStop):self.run_step(adapter)
        self.approve_current();self.engine.source_pin='different-source'
        with self.assertRaises(PilotStop):self.run_step(adapter)
        self.assertEqual(adapter.calls,0)
        self.assertEqual(self.session.read()[0]['requests'],0)

    def test_bool_index_and_stale_preview_approval_fail(self):
        with self.assertRaises(PilotStop):self.session.approve('independent',False,self.sha)
        self.approve_current();self.run_step()
        with self.assertRaises(PilotStop):self.session.approve('independent',0,self.sha)

    def test_all_proposals_validate_before_any_effect(self):
        self.approve_current()
        bad=independent_response(('same','same'))
        with self.assertRaises(PilotStop):self.run_step(IndependentAdapterDouble(bad))
        self.assertEqual(self.engine.events,[])
        state,_,_=self.session.read()
        self.assertEqual((state['phase'],state['requests'],state['reserved_tokens']),('HALTED',1,2000))

    def test_ambiguous_failure_is_reserved_and_not_resumable(self):
        class FailingAdapter(IndependentAdapterDouble):
            def request(self,*_):
                self.calls+=1
                raise RuntimeError('Bearer synthetic-marker-never-log')
        adapter=FailingAdapter();self.approve_current()
        with self.assertRaises(PilotStop):self.run_step(adapter)
        self.session=PilotSession(self.session.directory)
        with self.assertRaises(PilotStop):self.run_step(adapter,200)
        self.assertEqual(adapter.calls,1)
        self.assertNotIn('synthetic-marker-never-log',''.join(p.read_text() for p in self.session.directory.glob('record*')))

    def test_restart_does_not_refund_tokens_tools_or_requests(self):
        self.approve_current();first=self.run_step()
        self.engine=IndependentEngineDouble();self.session=PilotSession(self.session.directory)
        self.approve_current();second=self.run_step(IndependentAdapterDouble(independent_response(('q2',))),200)
        self.assertEqual((second['requests'],second['reserved_tokens'],second['completion_tokens']),(2,4000,40))
        self.assertEqual(len(second['engine']['events']),6)
        with self.assertRaises(PilotStop):self.run_step(now=300)

    def test_different_request_image_stops_without_reservation(self):
        self.approve_current();adapter=IndependentAdapterDouble()
        adapter._prepare=lambda *_:(b'', ['f'*64],2000)
        with self.assertRaises(PilotStop):self.run_step(adapter)
        self.assertEqual(adapter.calls,0)
        self.assertEqual(self.session.read()[0]['requests'],0)

    def test_journal_chain_gap_or_tampering_fail_closed(self):
        self.approve_current()
        file=self.session.directory/'record_001.json'
        file.rename(self.session.directory/'record_002.json')
        with self.assertRaises(PilotStop):self.session.read()

    def test_journal_duplicate_json_key_rejected(self):
        file=self.session.directory/'record_000.json'
        text=file.read_text()
        file.write_text('{"sequence":999,'+text[1:])
        with self.assertRaises(PilotStop):self.session.read()

    def test_private_proof_duplicate_key_rejected(self):
        file=self.base/'proof.json'
        file.write_text('{"free_plan":false,"free_plan":true}')
        with self.assertRaises(PilotStop):strict_json_record(file)

    def test_missing_geometry_event_stops_before_reservation(self):
        self.engine.events=[dict(sequence=0,tool='get_candidates')]
        self.engine._validate_state=lambda _:None
        self.engine.output=self.base/'engine_records'
        self.engine.output.mkdir()
        preview=self.session.directory/'preview_00.png'
        self.session=PilotSession(self.base/'evidence_session')
        self.session.create('independent',self.engine,dict(file='preview_00.png',sha256=self.sha),{},preview_source=preview)
        self.approve_current();adapter=IndependentAdapterDouble()
        with self.assertRaises(PilotStop):self.run_step(adapter)
        self.assertEqual(adapter.calls,0)
        self.assertEqual(self.session.read()[0]['requests'],0)

    def test_observation_records_remain_untrusted_and_redacted(self):
        self.approve_current();response=independent_response()
        obs=json.loads(response['message']['content'])
        obs['missing_components']=['Bearer synthetic-observation-secret']
        obs['unavailable_capabilities']=['authorization=synthetic-auth-token']
        response['message']['content']=json.dumps(obs)
        state=self.run_step(IndependentAdapterDouble(response))
        saved=''.join(p.read_text() for p in self.session.directory.glob('record*'))
        self.assertNotIn('synthetic-observation-secret',saved)
        self.assertNotIn('synthetic-auth-token',saved)
        self.assertEqual(state['observations'][0]['authority'],'UNTRUSTED_PLANNER_OBSERVATION')

    def test_usage_extras_are_not_persisted(self):
        self.approve_current();response=independent_response()
        response['usage']['unexpected_private_debug']='Bearer synthetic-unvalidated-usage-marker'
        self.run_step(IndependentAdapterDouble(response))
        saved=''.join(p.read_text() for p in self.session.directory.glob('record*'))
        self.assertNotIn('synthetic-unvalidated-usage-marker',saved)
        self.assertNotIn('unexpected_private_debug',saved)

    def test_known_usage_survives_invalid_observation(self):
        self.approve_current();response=independent_response()
        response['message']['content']=None
        with self.assertRaises(PilotStop):self.run_step(IndependentAdapterDouble(response))
        state,_,_=self.session.read()
        self.assertEqual(state['phase'],'HALTED')
        self.assertEqual(state['completion_tokens'],20)
        self.assertEqual(state['usage'][0]['total_tokens'],90)

    def test_changed_implementation_stops_before_transport(self):
        self.approve_current();adapter=IndependentAdapterDouble()
        with patch('pilot_control.implementation_pin',return_value='different-implementation'):
            with self.assertRaises(PilotStop):self.run_step(adapter)
        self.assertEqual(adapter.calls,0)
        self.assertEqual(self.session.read()[0]['requests'],0)

    def test_credential_shaped_tool_identity_is_not_journaled(self):
        marker='gsk_'+'qa_marker'
        self.approve_current()
        with self.assertRaises(PilotStop):
            self.run_step(IndependentAdapterDouble(independent_response((marker,))))
        saved=''.join(p.read_text() for p in self.session.directory.glob('record*'))
        self.assertNotIn(marker,saved)
        self.assertEqual(self.engine.events,[])
        self.assertEqual(self.session.read()[0]['phase'],'HALTED')
```

### `IndependentHardeningAudit.setUp` — `Lines 50–56`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `50` إلى السطر `56` (`Lines 50–56`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 50–56`):**
```python
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.base=Path(self.tmp.name);self.engine=IndependentEngineDouble()
        self.session=PilotSession(self.base/'session')
        file=self.base/'source.png';file.write_bytes(b'independent synthetic image')
        self.sha=hashlib.sha256(file.read_bytes()).hexdigest()
        self.session.create('independent',self.engine,dict(file='preview_00.png',sha256=self.sha),{},preview_source=file)
```

### `IndependentHardeningAudit.approve_current` — `Lines 57–59`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `57` إلى السطر `59` (`Lines 57–59`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 57–59`):**
```python
    def approve_current(self):
        state,_,_=self.session.read()
        self.session.approve(state['identity'],state['requests'],state['preview']['sha256'])
```

### `IndependentHardeningAudit.request_builder` — `Lines 60–61`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `60` إلى السطر `61` (`Lines 60–61`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 60–61`):**
```python
    def request_builder(self,engine,state):
        return [dict(image_hashes=[state['preview']['sha256']])],[]
```

### `IndependentHardeningAudit.next_preview` — `Lines 62–66`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `62` إلى السطر `66` (`Lines 62–66`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 62–66`):**
```python
    def next_preview(self,engine,state):
        engine.dispatch('render_geometry',{})
        file=self.session.directory/f"preview_{state['requests']:02d}.png"
        file.write_bytes(str(state['requests']).encode())
        return dict(file=file.name,sha256=hashlib.sha256(file.read_bytes()).hexdigest()),{}
```

### `IndependentHardeningAudit.run_step` — `Lines 67–69`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `67` إلى السطر `69` (`Lines 67–69`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 67–69`):**
```python
    def run_step(self,adapter=None,now=100):
        return self.session.step(self.engine,adapter or IndependentAdapterDouble(),
            self.request_builder,self.next_preview,lambda:now)
```

### `IndependentHardeningAudit.test_source_identity_or_no_approval_stops_before_transport` — `Lines 71–77`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `71` إلى السطر `77` (`Lines 71–77`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 71–77`):**
```python
    def test_source_identity_or_no_approval_stops_before_transport(self):
        adapter=IndependentAdapterDouble()
        with self.assertRaises(PilotStop):self.run_step(adapter)
        self.approve_current();self.engine.source_pin='different-source'
        with self.assertRaises(PilotStop):self.run_step(adapter)
        self.assertEqual(adapter.calls,0)
        self.assertEqual(self.session.read()[0]['requests'],0)
```

### `IndependentHardeningAudit.test_bool_index_and_stale_preview_approval_fail` — `Lines 79–82`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `79` إلى السطر `82` (`Lines 79–82`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 79–82`):**
```python
    def test_bool_index_and_stale_preview_approval_fail(self):
        with self.assertRaises(PilotStop):self.session.approve('independent',False,self.sha)
        self.approve_current();self.run_step()
        with self.assertRaises(PilotStop):self.session.approve('independent',0,self.sha)
```

### `IndependentHardeningAudit.test_all_proposals_validate_before_any_effect` — `Lines 84–90`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `84` إلى السطر `90` (`Lines 84–90`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 84–90`):**
```python
    def test_all_proposals_validate_before_any_effect(self):
        self.approve_current()
        bad=independent_response(('same','same'))
        with self.assertRaises(PilotStop):self.run_step(IndependentAdapterDouble(bad))
        self.assertEqual(self.engine.events,[])
        state,_,_=self.session.read()
        self.assertEqual((state['phase'],state['requests'],state['reserved_tokens']),('HALTED',1,2000))
```

### `IndependentHardeningAudit.test_ambiguous_failure_is_reserved_and_not_resumable` — `Lines 92–102`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `92` إلى السطر `102` (`Lines 92–102`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 92–102`):**
```python
    def test_ambiguous_failure_is_reserved_and_not_resumable(self):
        class FailingAdapter(IndependentAdapterDouble):
            def request(self,*_):
                self.calls+=1
                raise RuntimeError('Bearer synthetic-marker-never-log')
        adapter=FailingAdapter();self.approve_current()
        with self.assertRaises(PilotStop):self.run_step(adapter)
        self.session=PilotSession(self.session.directory)
        with self.assertRaises(PilotStop):self.run_step(adapter,200)
        self.assertEqual(adapter.calls,1)
        self.assertNotIn('synthetic-marker-never-log',''.join(p.read_text() for p in self.session.directory.glob('record*')))
```

### `IndependentHardeningAudit.test_ambiguous_failure_is_reserved_and_not_resumable.FailingAdapter` — `Lines 93–96`
- **النوع:** `nested_class`
- **نطاق الأسطر الدقيق:** من السطر `93` إلى السطر `96` (`Lines 93–96`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 93–96`):**
```python
        class FailingAdapter(IndependentAdapterDouble):
            def request(self,*_):
                self.calls+=1
                raise RuntimeError('Bearer synthetic-marker-never-log')
```

### `IndependentHardeningAudit.test_ambiguous_failure_is_reserved_and_not_resumable.FailingAdapter.request` — `Lines 94–96`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `94` إلى السطر `96` (`Lines 94–96`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 94–96`):**
```python
            def request(self,*_):
                self.calls+=1
                raise RuntimeError('Bearer synthetic-marker-never-log')
```

### `IndependentHardeningAudit.test_restart_does_not_refund_tokens_tools_or_requests` — `Lines 104–110`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `104` إلى السطر `110` (`Lines 104–110`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 104–110`):**
```python
    def test_restart_does_not_refund_tokens_tools_or_requests(self):
        self.approve_current();first=self.run_step()
        self.engine=IndependentEngineDouble();self.session=PilotSession(self.session.directory)
        self.approve_current();second=self.run_step(IndependentAdapterDouble(independent_response(('q2',))),200)
        self.assertEqual((second['requests'],second['reserved_tokens'],second['completion_tokens']),(2,4000,40))
        self.assertEqual(len(second['engine']['events']),6)
        with self.assertRaises(PilotStop):self.run_step(now=300)
```

### `IndependentHardeningAudit.test_different_request_image_stops_without_reservation` — `Lines 112–117`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `112` إلى السطر `117` (`Lines 112–117`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 112–117`):**
```python
    def test_different_request_image_stops_without_reservation(self):
        self.approve_current();adapter=IndependentAdapterDouble()
        adapter._prepare=lambda *_:(b'', ['f'*64],2000)
        with self.assertRaises(PilotStop):self.run_step(adapter)
        self.assertEqual(adapter.calls,0)
        self.assertEqual(self.session.read()[0]['requests'],0)
```

### `IndependentHardeningAudit.test_journal_chain_gap_or_tampering_fail_closed` — `Lines 119–123`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `119` إلى السطر `123` (`Lines 119–123`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 119–123`):**
```python
    def test_journal_chain_gap_or_tampering_fail_closed(self):
        self.approve_current()
        file=self.session.directory/'record_001.json'
        file.rename(self.session.directory/'record_002.json')
        with self.assertRaises(PilotStop):self.session.read()
```

### `IndependentHardeningAudit.test_journal_duplicate_json_key_rejected` — `Lines 125–129`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `125` إلى السطر `129` (`Lines 125–129`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 125–129`):**
```python
    def test_journal_duplicate_json_key_rejected(self):
        file=self.session.directory/'record_000.json'
        text=file.read_text()
        file.write_text('{"sequence":999,'+text[1:])
        with self.assertRaises(PilotStop):self.session.read()
```

### `IndependentHardeningAudit.test_private_proof_duplicate_key_rejected` — `Lines 131–134`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `131` إلى السطر `134` (`Lines 131–134`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 131–134`):**
```python
    def test_private_proof_duplicate_key_rejected(self):
        file=self.base/'proof.json'
        file.write_text('{"free_plan":false,"free_plan":true}')
        with self.assertRaises(PilotStop):strict_json_record(file)
```

### `IndependentHardeningAudit.test_missing_geometry_event_stops_before_reservation` — `Lines 136–147`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `136` إلى السطر `147` (`Lines 136–147`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 136–147`):**
```python
    def test_missing_geometry_event_stops_before_reservation(self):
        self.engine.events=[dict(sequence=0,tool='get_candidates')]
        self.engine._validate_state=lambda _:None
        self.engine.output=self.base/'engine_records'
        self.engine.output.mkdir()
        preview=self.session.directory/'preview_00.png'
        self.session=PilotSession(self.base/'evidence_session')
        self.session.create('independent',self.engine,dict(file='preview_00.png',sha256=self.sha),{},preview_source=preview)
        self.approve_current();adapter=IndependentAdapterDouble()
        with self.assertRaises(PilotStop):self.run_step(adapter)
        self.assertEqual(adapter.calls,0)
        self.assertEqual(self.session.read()[0]['requests'],0)
```

### `IndependentHardeningAudit.test_observation_records_remain_untrusted_and_redacted` — `Lines 149–159`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `149` إلى السطر `159` (`Lines 149–159`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 149–159`):**
```python
    def test_observation_records_remain_untrusted_and_redacted(self):
        self.approve_current();response=independent_response()
        obs=json.loads(response['message']['content'])
        obs['missing_components']=['Bearer synthetic-observation-secret']
        obs['unavailable_capabilities']=['authorization=synthetic-auth-token']
        response['message']['content']=json.dumps(obs)
        state=self.run_step(IndependentAdapterDouble(response))
        saved=''.join(p.read_text() for p in self.session.directory.glob('record*'))
        self.assertNotIn('synthetic-observation-secret',saved)
        self.assertNotIn('synthetic-auth-token',saved)
        self.assertEqual(state['observations'][0]['authority'],'UNTRUSTED_PLANNER_OBSERVATION')
```

### `IndependentHardeningAudit.test_usage_extras_are_not_persisted` — `Lines 161–167`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `161` إلى السطر `167` (`Lines 161–167`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 161–167`):**
```python
    def test_usage_extras_are_not_persisted(self):
        self.approve_current();response=independent_response()
        response['usage']['unexpected_private_debug']='Bearer synthetic-unvalidated-usage-marker'
        self.run_step(IndependentAdapterDouble(response))
        saved=''.join(p.read_text() for p in self.session.directory.glob('record*'))
        self.assertNotIn('synthetic-unvalidated-usage-marker',saved)
        self.assertNotIn('unexpected_private_debug',saved)
```

### `IndependentHardeningAudit.test_known_usage_survives_invalid_observation` — `Lines 169–176`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `169` إلى السطر `176` (`Lines 169–176`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 169–176`):**
```python
    def test_known_usage_survives_invalid_observation(self):
        self.approve_current();response=independent_response()
        response['message']['content']=None
        with self.assertRaises(PilotStop):self.run_step(IndependentAdapterDouble(response))
        state,_,_=self.session.read()
        self.assertEqual(state['phase'],'HALTED')
        self.assertEqual(state['completion_tokens'],20)
        self.assertEqual(state['usage'][0]['total_tokens'],90)
```

### `IndependentHardeningAudit.test_changed_implementation_stops_before_transport` — `Lines 178–183`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `178` إلى السطر `183` (`Lines 178–183`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 178–183`):**
```python
    def test_changed_implementation_stops_before_transport(self):
        self.approve_current();adapter=IndependentAdapterDouble()
        with patch('pilot_control.implementation_pin',return_value='different-implementation'):
            with self.assertRaises(PilotStop):self.run_step(adapter)
        self.assertEqual(adapter.calls,0)
        self.assertEqual(self.session.read()[0]['requests'],0)
```

### `IndependentHardeningAudit.test_credential_shaped_tool_identity_is_not_journaled` — `Lines 185–193`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `185` إلى السطر `193` (`Lines 185–193`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 185–193`):**
```python
    def test_credential_shaped_tool_identity_is_not_journaled(self):
        marker='gsk_'+'qa_marker'
        self.approve_current()
        with self.assertRaises(PilotStop):
            self.run_step(IndependentAdapterDouble(independent_response((marker,))))
        saved=''.join(p.read_text() for p in self.session.directory.glob('record*'))
        self.assertNotIn(marker,saved)
        self.assertEqual(self.engine.events,[])
        self.assertEqual(self.session.read()[0]['phase'],'HALTED')
```
