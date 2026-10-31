# مرآة الكود التفصيلية: `test_pilot.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_pilot.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_pilot.py`
- **الدور المعماري (`Architectural Role`):** Isolated restricted geometry tools / controller / Groq adapter / evaluator research
- **إجمالي عدد الأسطر (`Total Lines`):** `45` (`Lines 1–45`)
- **بصمة الملف (`SHA-256`):** `b8199443749f69a7446f146a0a2cdb7b45bdeeeb2e879ddb5a19578de93e4dea`
- **الوصف التفصيلي:** # START CHANGE AGD-GROQ-LOOP-TEST | 2026-10-31T15:16:13Z | EDITED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `frozen native source/evidence/P curves; provider responses only through strict local tool schemas; evaluator refs only in measurement` | candidate IDs, source coordinates, cubic arrays, typed local requests and budgets | source-only geometry; no unrestricted execution or live requests by default |
| **يرمي إلى (`Throws To`)** | `this isolated experiment` | transaction journals, exact SVG/PNG previews, replay hashes, objective diagnostics and sanitized provider status | offline research; AI NOT_TESTED; geometry NOT_ACCEPTED; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `PilotTests` | `class` | `Lines 8–43` | `class PilotTests(unittest.TestCase):` | رمز برمجي موثق. |
| `PilotTests.make_engine` | `method` | `Lines 9–12` | `def make_engine(self,path):` | رمز برمجي موثق. |
| `PilotTests.test_json_duplicate_and_nonfinite` | `method` | `Lines 13–15` | `def test_json_duplicate_and_nonfinite(self):` | رمز برمجي موثق. |
| `PilotTests.test_dryrun_no_network` | `method` | `Lines 16–19` | `def test_dryrun_no_network(self):` | رمز برمجي موثق. |
| `PilotTests.test_unverified_live_denied` | `method` | `Lines 20–23` | `def test_unverified_live_denied(self):` | رمز برمجي موثق. |
| `PilotTests.test_explicit_bounded_pacing_no_real_sleep` | `method` | `Lines 24–27` | `def test_explicit_bounded_pacing_no_real_sleep(self):` | رمز برمجي موثق. |
| `PilotTests.test_explicit_bounded_pacing_no_real_sleep.advance` | `nested_function` | `Lines 26–26` | `def advance(seconds):waits.append(seconds);clock[0]+=seconds` | رمز برمجي موثق. |
| `PilotTests.test_frozen_clock_cannot_extend_pacing_budget` | `method` | `Lines 28–31` | `def test_frozen_clock_cannot_extend_pacing_budget(self):` | رمز برمجي موثق. |
| `PilotTests.test_feedback_and_invalid_stage_preserves_commit` | `method` | `Lines 32–43` | `def test_feedback_and_invalid_stage_preserves_commit(self):` | رمز برمجي موثق. |
| `PilotTests.test_feedback_and_invalid_stage_preserves_commit.RecordedAdapter` | `nested_class` | `Lines 33–39` | `class RecordedAdapter:` | رمز برمجي موثق. |
| `PilotTests.test_feedback_and_invalid_stage_preserves_commit.RecordedAdapter.__init__` | `method` | `Lines 34–34` | `def __init__(self):self.messages=[]` | رمز برمجي موثق. |
| `PilotTests.test_feedback_and_invalid_stage_preserves_commit.RecordedAdapter.request` | `method` | `Lines 35–39` | `def request(self,messages,tools,case):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `PilotTests` — `Lines 8–43`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `8` إلى السطر `43` (`Lines 8–43`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 8–43`):**
```python
class PilotTests(unittest.TestCase):
 def make_engine(self,path):
  image=np.full((32,32,3),255,dtype=np.uint8);image[8,2:24]=0
  points=[[float(x),8.] for x in range(2,24)]
  return GeometryToolEngine(image,[dict(trace_id=0,source_points_xy=points,length_px=21)],[],path,R,W)
 def test_json_duplicate_and_nonfinite(self):
  for text in ['{"x":1,"x":2}','{"x":NaN}','{"x":Infinity}']:
   with self.assertRaises(ValueError):strict_call_arguments(text)
 def test_dryrun_no_network(self):
  with tempfile.TemporaryDirectory() as tmp:
   engine=self.make_engine(Path(tmp)/'dry');r=run_visual_planner(engine,GroqAdapter(), 'synthetic')
   self.assertEqual(r['status'],'DRY_RUN');self.assertEqual(r['requests'],0);self.assertFalse(engine.items)
 def test_unverified_live_denied(self):
  with tempfile.TemporaryDirectory() as tmp:
   engine=self.make_engine(Path(tmp)/'deny')
   with self.assertRaises(ProviderGateError):run_visual_planner(engine,GroqAdapter(live=True),'synthetic')
 def test_explicit_bounded_pacing_no_real_sleep(self):
  clock=[100.];adapter=GroqAdapter(live=True,clock=lambda:clock[0]);adapter._last_request=100.;waits=[]
  def advance(seconds):waits.append(seconds);clock[0]+=seconds
  wait_for_pilot_cadence(adapter,advance);self.assertEqual(waits,[30.,30.,1.]);self.assertEqual(clock[0],161.)
 def test_frozen_clock_cannot_extend_pacing_budget(self):
  adapter=GroqAdapter(live=True,clock=lambda:100.);adapter._last_request=100.;waits=[]
  with self.assertRaises(ProviderGateError):wait_for_pilot_cadence(adapter,lambda t:waits.append(t))
  self.assertEqual(sum(waits),61.)
 def test_feedback_and_invalid_stage_preserves_commit(self):
  class RecordedAdapter:
   def __init__(self):self.messages=[]
   def request(self,messages,tools,case):
    self.messages.append(messages)
    stage=next(t for t in tools if t['function']['name']=='stage_candidates');assert stage['function']['parameters']['properties']['trace_ids']['maxItems']==2
    args={'trace_ids':[0]} if len(self.messages)==1 else {'trace_ids':[999]}
    return dict(status='LIVE',reserved_tokens=1,message=dict(tool_calls=[dict(id='fixture_'+str(len(self.messages)),type='function',function=dict(name='stage_candidates',arguments=json.dumps(args)))]))
  with tempfile.TemporaryDirectory() as tmp:
   engine=self.make_engine(Path(tmp)/'fixture');adapter=RecordedAdapter();r=run_visual_planner(engine,adapter,'synthetic')
   self.assertEqual(engine.commits,1);self.assertEqual(len(engine.items),1);self.assertLessEqual(len(engine.events),12);self.assertIsNone(engine.pending)
   self.assertIn('committed',adapter.messages[1][-1]['content'][0]['text']);self.assertIn('geometry_diagnostics',adapter.messages[1][-1]['content'][0]['text']);self.assertEqual(adapter.messages[1][1]['role'],'assistant');self.assertEqual(adapter.messages[1][2]['role'],'tool')
```

### `PilotTests.make_engine` — `Lines 9–12`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `12` (`Lines 9–12`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–12`):**
```python
 def make_engine(self,path):
  image=np.full((32,32,3),255,dtype=np.uint8);image[8,2:24]=0
  points=[[float(x),8.] for x in range(2,24)]
  return GeometryToolEngine(image,[dict(trace_id=0,source_points_xy=points,length_px=21)],[],path,R,W)
```

### `PilotTests.test_json_duplicate_and_nonfinite` — `Lines 13–15`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `15` (`Lines 13–15`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 13–15`):**
```python
 def test_json_duplicate_and_nonfinite(self):
  for text in ['{"x":1,"x":2}','{"x":NaN}','{"x":Infinity}']:
   with self.assertRaises(ValueError):strict_call_arguments(text)
```

### `PilotTests.test_dryrun_no_network` — `Lines 16–19`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `19` (`Lines 16–19`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 16–19`):**
```python
 def test_dryrun_no_network(self):
  with tempfile.TemporaryDirectory() as tmp:
   engine=self.make_engine(Path(tmp)/'dry');r=run_visual_planner(engine,GroqAdapter(), 'synthetic')
   self.assertEqual(r['status'],'DRY_RUN');self.assertEqual(r['requests'],0);self.assertFalse(engine.items)
```

### `PilotTests.test_unverified_live_denied` — `Lines 20–23`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `20` إلى السطر `23` (`Lines 20–23`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 20–23`):**
```python
 def test_unverified_live_denied(self):
  with tempfile.TemporaryDirectory() as tmp:
   engine=self.make_engine(Path(tmp)/'deny')
   with self.assertRaises(ProviderGateError):run_visual_planner(engine,GroqAdapter(live=True),'synthetic')
```

### `PilotTests.test_explicit_bounded_pacing_no_real_sleep` — `Lines 24–27`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `24` إلى السطر `27` (`Lines 24–27`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 24–27`):**
```python
 def test_explicit_bounded_pacing_no_real_sleep(self):
  clock=[100.];adapter=GroqAdapter(live=True,clock=lambda:clock[0]);adapter._last_request=100.;waits=[]
  def advance(seconds):waits.append(seconds);clock[0]+=seconds
  wait_for_pilot_cadence(adapter,advance);self.assertEqual(waits,[30.,30.,1.]);self.assertEqual(clock[0],161.)
```

### `PilotTests.test_explicit_bounded_pacing_no_real_sleep.advance` — `Lines 26–26`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `26` إلى السطر `26` (`Lines 26–26`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 26–26`):**
```python
  def advance(seconds):waits.append(seconds);clock[0]+=seconds
```

### `PilotTests.test_frozen_clock_cannot_extend_pacing_budget` — `Lines 28–31`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `28` إلى السطر `31` (`Lines 28–31`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 28–31`):**
```python
 def test_frozen_clock_cannot_extend_pacing_budget(self):
  adapter=GroqAdapter(live=True,clock=lambda:100.);adapter._last_request=100.;waits=[]
  with self.assertRaises(ProviderGateError):wait_for_pilot_cadence(adapter,lambda t:waits.append(t))
  self.assertEqual(sum(waits),61.)
```

### `PilotTests.test_feedback_and_invalid_stage_preserves_commit` — `Lines 32–43`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `32` إلى السطر `43` (`Lines 32–43`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 32–43`):**
```python
 def test_feedback_and_invalid_stage_preserves_commit(self):
  class RecordedAdapter:
   def __init__(self):self.messages=[]
   def request(self,messages,tools,case):
    self.messages.append(messages)
    stage=next(t for t in tools if t['function']['name']=='stage_candidates');assert stage['function']['parameters']['properties']['trace_ids']['maxItems']==2
    args={'trace_ids':[0]} if len(self.messages)==1 else {'trace_ids':[999]}
    return dict(status='LIVE',reserved_tokens=1,message=dict(tool_calls=[dict(id='fixture_'+str(len(self.messages)),type='function',function=dict(name='stage_candidates',arguments=json.dumps(args)))]))
  with tempfile.TemporaryDirectory() as tmp:
   engine=self.make_engine(Path(tmp)/'fixture');adapter=RecordedAdapter();r=run_visual_planner(engine,adapter,'synthetic')
   self.assertEqual(engine.commits,1);self.assertEqual(len(engine.items),1);self.assertLessEqual(len(engine.events),12);self.assertIsNone(engine.pending)
   self.assertIn('committed',adapter.messages[1][-1]['content'][0]['text']);self.assertIn('geometry_diagnostics',adapter.messages[1][-1]['content'][0]['text']);self.assertEqual(adapter.messages[1][1]['role'],'assistant');self.assertEqual(adapter.messages[1][2]['role'],'tool')
```

### `PilotTests.test_feedback_and_invalid_stage_preserves_commit.RecordedAdapter` — `Lines 33–39`
- **النوع:** `nested_class`
- **نطاق الأسطر الدقيق:** من السطر `33` إلى السطر `39` (`Lines 33–39`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 33–39`):**
```python
  class RecordedAdapter:
   def __init__(self):self.messages=[]
   def request(self,messages,tools,case):
    self.messages.append(messages)
    stage=next(t for t in tools if t['function']['name']=='stage_candidates');assert stage['function']['parameters']['properties']['trace_ids']['maxItems']==2
    args={'trace_ids':[0]} if len(self.messages)==1 else {'trace_ids':[999]}
    return dict(status='LIVE',reserved_tokens=1,message=dict(tool_calls=[dict(id='fixture_'+str(len(self.messages)),type='function',function=dict(name='stage_candidates',arguments=json.dumps(args)))]))
```

### `PilotTests.test_feedback_and_invalid_stage_preserves_commit.RecordedAdapter.__init__` — `Lines 34–34`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `34` إلى السطر `34` (`Lines 34–34`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 34–34`):**
```python
   def __init__(self):self.messages=[]
```

### `PilotTests.test_feedback_and_invalid_stage_preserves_commit.RecordedAdapter.request` — `Lines 35–39`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `35` إلى السطر `39` (`Lines 35–39`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 35–39`):**
```python
   def request(self,messages,tools,case):
    self.messages.append(messages)
    stage=next(t for t in tools if t['function']['name']=='stage_candidates');assert stage['function']['parameters']['properties']['trace_ids']['maxItems']==2
    args={'trace_ids':[0]} if len(self.messages)==1 else {'trace_ids':[999]}
    return dict(status='LIVE',reserved_tokens=1,message=dict(tool_calls=[dict(id='fixture_'+str(len(self.messages)),type='function',function=dict(name='stage_candidates',arguments=json.dumps(args)))]))
```
