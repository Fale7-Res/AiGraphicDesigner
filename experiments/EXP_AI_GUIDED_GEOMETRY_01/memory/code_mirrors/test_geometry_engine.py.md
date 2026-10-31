# مرآة الكود التفصيلية: `test_geometry_engine.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_geometry_engine.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_geometry_engine.py`
- **الدور المعماري (`Architectural Role`):** Isolated restricted geometry tools / controller / Groq adapter / evaluator research
- **إجمالي عدد الأسطر (`Total Lines`):** `140` (`Lines 1–140`)
- **بصمة الملف (`SHA-256`):** `a84f0ef8f2c2ffc5f5f1800a7483707675790b89792f5a13d52f9fe2d56bb2c5`
- **الوصف التفصيلي:** # START CHANGE AGD-AGENTIC-TOOLS-TEST | 2026-10-31T11:54:38Z | EDITED | Author: geometry_tools

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `frozen native source/evidence/P curves; provider responses only through strict local tool schemas; evaluator refs only in measurement` | candidate IDs, source coordinates, cubic arrays, typed local requests and budgets | source-only geometry; no unrestricted execution or live requests by default |
| **يرمي إلى (`Throws To`)** | `this isolated experiment` | transaction journals, exact SVG/PNG previews, replay hashes, objective diagnostics and sanitized provider status | offline research; AI NOT_TESTED; geometry NOT_ACCEPTED; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `synthetic_trace` | `function` | `Lines 14–15` | `def synthetic_trace(tid, points):` | رمز برمجي موثق. |
| `EngineContractTests` | `class` | `Lines 18–137` | `class EngineContractTests(unittest.TestCase):` | رمز برمجي موثق. |
| `EngineContractTests.make_engine_fixture` | `method` | `Lines 19–25` | `def make_engine_fixture(self, traces=None, items=None):` | رمز برمجي موثق. |
| `EngineContractTests.test_strict_tools_schema` | `method` | `Lines 27–33` | `def test_strict_tools_schema(self):` | رمز برمجي موثق. |
| `EngineContractTests.test_atomic_commit_and_exact_rollback` | `method` | `Lines 35–46` | `def test_atomic_commit_and_exact_rollback(self):` | رمز برمجي موثق. |
| `EngineContractTests.test_pending_rejection_and_rollback` | `method` | `Lines 48–53` | `def test_pending_rejection_and_rollback(self):` | رمز برمجي موثق. |
| `EngineContractTests.test_existing_trace_not_duplicated` | `method` | `Lines 55–63` | `def test_existing_trace_not_duplicated(self):` | رمز برمجي موثق. |
| `EngineContractTests.test_closed_loop_corner_and_junction_contract` | `method` | `Lines 65–75` | `def test_closed_loop_corner_and_junction_contract(self):` | رمز برمجي موثق. |
| `EngineContractTests.test_replay_same_geometry_hash` | `method` | `Lines 77–86` | `def test_replay_same_geometry_hash(self):` | رمز برمجي موثق. |
| `EngineContractTests.test_actual_svg_renderer` | `method` | `Lines 88–97` | `def test_actual_svg_renderer(self):` | رمز برمجي موثق. |
| `EngineContractTests.test_roi_and_scale_bounds` | `method` | `Lines 99–104` | `def test_roi_and_scale_bounds(self):` | رمز برمجي موثق. |
| `EngineContractTests.test_duplicate_geometry_different_source_id` | `method` | `Lines 106–111` | `def test_duplicate_geometry_different_source_id(self):` | رمز برمجي موثق. |
| `EngineContractTests.test_nested_closed_boundaries_not_semantic_holes` | `method` | `Lines 113–120` | `def test_nested_closed_boundaries_not_semantic_holes(self):` | رمز برمجي موثق. |
| `EngineContractTests.test_allowlisted_tool_does_not_accept_path_or_code` | `method` | `Lines 122–128` | `def test_allowlisted_tool_does_not_accept_path_or_code(self):` | رمز برمجي موثق. |
| `EngineContractTests.test_usable_candidate_not_hidden_by_short_noise` | `method` | `Lines 130–137` | `def test_usable_candidate_not_hidden_by_short_noise(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `synthetic_trace` — `Lines 14–15`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `15` (`Lines 14–15`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 14–15`):**
```python
def synthetic_trace(tid, points):
    return {'trace_id': tid, 'source_points_xy': points, 'length_px': float(np.linalg.norm(np.diff(points,axis=0),axis=1).sum())}
```

### `EngineContractTests` — `Lines 18–137`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `137` (`Lines 18–137`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 18–137`):**
```python
class EngineContractTests(unittest.TestCase):
    def make_engine_fixture(self, traces=None, items=None):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        rgb = np.full((32,32,3),255,np.uint8)
        rgb[8:10,:] = 0
        source = traces or [synthetic_trace(0,[[2,8],[8,8],[14,8],[24,8]])]
        return GeometryToolEngine(rgb,source,items or [],Path(directory.name)/'session',REPO,WORK)

    def test_strict_tools_schema(self):
        engine = self.make_engine_fixture()
        for name, args in [('exec',{'command':'x'}),('get_candidates',{'roi':[0,0,1,1],'limit':True}),('inspect_region',{'roi':[0,0,float('nan'),1]}),('inspect_region',{'roi':[0,0,1,1],'path':'outside'}),('stage_candidates',{'trace_ids':[0,0]})]:
            result=engine.dispatch(name,args)
            self.assertIn('error',result)
        self.assertEqual(engine.state_hash(),engine.initial_hash)
        self.assertTrue(all(x['arguments'] is None for x in engine.events))

    def test_atomic_commit_and_exact_rollback(self):
        engine=self.make_engine_fixture()
        before=engine.state_hash()
        staged=engine.dispatch('stage_candidates',{'trace_ids':[0]})
        self.assertEqual(staged['added_paths'],1)
        self.assertEqual(engine.state_hash(),before)
        committed=engine.dispatch('commit_change',{})
        self.assertEqual(committed['status'],'committed')
        self.assertNotEqual(engine.state_hash(),before)
        engine.dispatch('rollback_change',{})
        self.assertEqual(engine.state_hash(),before)
        self.assertEqual(len(engine.items),0)

    def test_pending_rejection_and_rollback(self):
        engine=self.make_engine_fixture()
        engine.dispatch('stage_candidates',{'trace_ids':[0]})
        self.assertIn('error',engine.dispatch('stage_candidates',{'trace_ids':[0]}))
        self.assertEqual(engine.dispatch('rollback_change',{})['status'],'pending_discarded')
        self.assertEqual(engine.state_hash(),engine.initial_hash)

    def test_existing_trace_not_duplicated(self):
        engine=self.make_engine_fixture()
        engine.dispatch('stage_candidates',{'trace_ids':[0]});engine.dispatch('commit_change',{})
        out=engine.dispatch('stage_candidates',{'trace_ids':[0]})
        self.assertNotIn('error',out,repr(out))
        self.assertEqual(out['added_paths'],0)
        self.assertEqual(out['ledger'][0]['reason'],'existing_trace')
        self.assertIn('error',engine.dispatch('commit_change',{}))
        self.assertEqual(len(engine.items),1)

    def test_closed_loop_corner_and_junction_contract(self):
        traces=[synthetic_trace(0,[[4,4],[20,4],[20,20],[4,20],[4,4]]),synthetic_trace(1,[[20,4],[26,4],[28,4]])]
        engine=self.make_engine_fixture(traces)
        out=engine.dispatch('stage_candidates',{'trace_ids':[0,1]})
        self.assertGreaterEqual(out['added_paths'],1)
        engine.dispatch('commit_change',{})
        closed=[x for x in engine.items if x.get('closed')]
        self.assertEqual(len(closed),1)
        cc=np.asarray(closed[0]['curves'])
        self.assertTrue(np.array_equal(cc[0,0],cc[-1,-1]))
        self.assertTrue(np.array_equal(cc[:-1,-1],cc[1:,0]))

    def test_replay_same_geometry_hash(self):
        plan=[('get_candidates',{'roi':[0,0,1,1],'limit':4}),('stage_candidates',{'trace_ids':[0]}),('commit_change',{}),('validate_geometry',{})]
        first,second=self.make_engine_fixture(),self.make_engine_fixture()
        for engine in [first,second]:
            for name,args in plan:engine.dispatch(name,args)
        self.assertEqual(first.state_hash(),second.state_hash())
        self.assertEqual(first.replay_decision_hash(),second.replay_decision_hash())
        self.assertEqual(first.source_pin,second.source_pin)
        for event in first.events:
            self.assertEqual(json.loads((first.output/('event_%03d.json'%event['sequence'])).read_text())['record_hash'],event['record_hash'])

    def test_actual_svg_renderer(self):
        engine=self.make_engine_fixture()
        engine.dispatch('stage_candidates',{'trace_ids':[0]});engine.dispatch('commit_change',{})
        for scale in [1,4,16]:
            result=engine.dispatch('render_geometry',{'scale':scale})
            self.assertNotIn('error',result)
            svg=(engine.output/result['svg']).read_text()
            self.assertIn(' C',svg)
            self.assertNotIn('<image',svg)
            self.assertTrue((engine.output/result['png']).exists())

    def test_roi_and_scale_bounds(self):
        engine=self.make_engine_fixture()
        self.assertIn('error',engine.dispatch('inspect_region',{'roi':[.8,0,.2,1]}))
        self.assertIn('error',engine.dispatch('render_geometry',{'scale':2}))
        self.assertIn('error',engine.dispatch('stage_candidates',{'trace_ids':[999]}))
        self.assertEqual(engine.state_hash(),engine.initial_hash)

    def test_duplicate_geometry_different_source_id(self):
        points=[[2,8],[8,8],[14,8],[24,8]]
        engine=self.make_engine_fixture([synthetic_trace(0,points),synthetic_trace(1,points)])
        result=engine.dispatch('stage_candidates',{'trace_ids':[0,1]})
        self.assertEqual(result['added_paths'],1)
        self.assertEqual(result['ledger'][1]['rejections'][0]['reason'],'duplicate_curve')

    def test_nested_closed_boundaries_not_semantic_holes(self):
        engine=self.make_engine_fixture([synthetic_trace(0,[[2,2],[28,2],[28,28],[2,28],[2,2]]),synthetic_trace(1,[[8,8],[20,8],[20,20],[8,20],[8,8]])])
        staged=engine.dispatch('stage_candidates',{'trace_ids':[0,1]})
        self.assertEqual(staged['added_paths'],2)
        engine.dispatch('commit_change',{})
        diagnostic=engine.dispatch('validate_geometry',{})
        self.assertEqual(diagnostic['closed_paths'],2)
        self.assertEqual(diagnostic['region_ownership'],'NOT_ESTABLISHED')

    def test_allowlisted_tool_does_not_accept_path_or_code(self):
        engine=self.make_engine_fixture()
        result=engine.dispatch('render_geometry',{'scale':1,'renderer':'untrusted'})
        self.assertIn('error',result)
        self.assertEqual(len(list(engine.output.glob('*.svg'))),0)
        self.assertIn('error',engine.dispatch([],{}))
        self.assertIn('error',engine.dispatch('get_candidates',{'roi':[0,0,1,1],'limit':10**1000}))

    def test_usable_candidate_not_hidden_by_short_noise(self):
        short=[synthetic_trace(tid,[[2,8],[3,8]]) for tid in range(20)]
        long=synthetic_trace(99,[[2,24],[12,24],[24,24]])
        engine=self.make_engine_fixture(short+[long])
        result=engine.dispatch('get_candidates',{'roi':[0,0,1,1],'limit':4})
        self.assertEqual(result['candidates'][0]['trace_id'],99)
        self.assertTrue(result['candidates'][0]['eligible'])
        self.assertFalse(result['candidates'][1]['eligible'])
```

### `EngineContractTests.make_engine_fixture` — `Lines 19–25`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `19` إلى السطر `25` (`Lines 19–25`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 19–25`):**
```python
    def make_engine_fixture(self, traces=None, items=None):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        rgb = np.full((32,32,3),255,np.uint8)
        rgb[8:10,:] = 0
        source = traces or [synthetic_trace(0,[[2,8],[8,8],[14,8],[24,8]])]
        return GeometryToolEngine(rgb,source,items or [],Path(directory.name)/'session',REPO,WORK)
```

### `EngineContractTests.test_strict_tools_schema` — `Lines 27–33`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `27` إلى السطر `33` (`Lines 27–33`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 27–33`):**
```python
    def test_strict_tools_schema(self):
        engine = self.make_engine_fixture()
        for name, args in [('exec',{'command':'x'}),('get_candidates',{'roi':[0,0,1,1],'limit':True}),('inspect_region',{'roi':[0,0,float('nan'),1]}),('inspect_region',{'roi':[0,0,1,1],'path':'outside'}),('stage_candidates',{'trace_ids':[0,0]})]:
            result=engine.dispatch(name,args)
            self.assertIn('error',result)
        self.assertEqual(engine.state_hash(),engine.initial_hash)
        self.assertTrue(all(x['arguments'] is None for x in engine.events))
```

### `EngineContractTests.test_atomic_commit_and_exact_rollback` — `Lines 35–46`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `35` إلى السطر `46` (`Lines 35–46`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 35–46`):**
```python
    def test_atomic_commit_and_exact_rollback(self):
        engine=self.make_engine_fixture()
        before=engine.state_hash()
        staged=engine.dispatch('stage_candidates',{'trace_ids':[0]})
        self.assertEqual(staged['added_paths'],1)
        self.assertEqual(engine.state_hash(),before)
        committed=engine.dispatch('commit_change',{})
        self.assertEqual(committed['status'],'committed')
        self.assertNotEqual(engine.state_hash(),before)
        engine.dispatch('rollback_change',{})
        self.assertEqual(engine.state_hash(),before)
        self.assertEqual(len(engine.items),0)
```

### `EngineContractTests.test_pending_rejection_and_rollback` — `Lines 48–53`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `48` إلى السطر `53` (`Lines 48–53`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 48–53`):**
```python
    def test_pending_rejection_and_rollback(self):
        engine=self.make_engine_fixture()
        engine.dispatch('stage_candidates',{'trace_ids':[0]})
        self.assertIn('error',engine.dispatch('stage_candidates',{'trace_ids':[0]}))
        self.assertEqual(engine.dispatch('rollback_change',{})['status'],'pending_discarded')
        self.assertEqual(engine.state_hash(),engine.initial_hash)
```

### `EngineContractTests.test_existing_trace_not_duplicated` — `Lines 55–63`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `55` إلى السطر `63` (`Lines 55–63`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 55–63`):**
```python
    def test_existing_trace_not_duplicated(self):
        engine=self.make_engine_fixture()
        engine.dispatch('stage_candidates',{'trace_ids':[0]});engine.dispatch('commit_change',{})
        out=engine.dispatch('stage_candidates',{'trace_ids':[0]})
        self.assertNotIn('error',out,repr(out))
        self.assertEqual(out['added_paths'],0)
        self.assertEqual(out['ledger'][0]['reason'],'existing_trace')
        self.assertIn('error',engine.dispatch('commit_change',{}))
        self.assertEqual(len(engine.items),1)
```

### `EngineContractTests.test_closed_loop_corner_and_junction_contract` — `Lines 65–75`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `65` إلى السطر `75` (`Lines 65–75`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 65–75`):**
```python
    def test_closed_loop_corner_and_junction_contract(self):
        traces=[synthetic_trace(0,[[4,4],[20,4],[20,20],[4,20],[4,4]]),synthetic_trace(1,[[20,4],[26,4],[28,4]])]
        engine=self.make_engine_fixture(traces)
        out=engine.dispatch('stage_candidates',{'trace_ids':[0,1]})
        self.assertGreaterEqual(out['added_paths'],1)
        engine.dispatch('commit_change',{})
        closed=[x for x in engine.items if x.get('closed')]
        self.assertEqual(len(closed),1)
        cc=np.asarray(closed[0]['curves'])
        self.assertTrue(np.array_equal(cc[0,0],cc[-1,-1]))
        self.assertTrue(np.array_equal(cc[:-1,-1],cc[1:,0]))
```

### `EngineContractTests.test_replay_same_geometry_hash` — `Lines 77–86`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `77` إلى السطر `86` (`Lines 77–86`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 77–86`):**
```python
    def test_replay_same_geometry_hash(self):
        plan=[('get_candidates',{'roi':[0,0,1,1],'limit':4}),('stage_candidates',{'trace_ids':[0]}),('commit_change',{}),('validate_geometry',{})]
        first,second=self.make_engine_fixture(),self.make_engine_fixture()
        for engine in [first,second]:
            for name,args in plan:engine.dispatch(name,args)
        self.assertEqual(first.state_hash(),second.state_hash())
        self.assertEqual(first.replay_decision_hash(),second.replay_decision_hash())
        self.assertEqual(first.source_pin,second.source_pin)
        for event in first.events:
            self.assertEqual(json.loads((first.output/('event_%03d.json'%event['sequence'])).read_text())['record_hash'],event['record_hash'])
```

### `EngineContractTests.test_actual_svg_renderer` — `Lines 88–97`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `88` إلى السطر `97` (`Lines 88–97`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 88–97`):**
```python
    def test_actual_svg_renderer(self):
        engine=self.make_engine_fixture()
        engine.dispatch('stage_candidates',{'trace_ids':[0]});engine.dispatch('commit_change',{})
        for scale in [1,4,16]:
            result=engine.dispatch('render_geometry',{'scale':scale})
            self.assertNotIn('error',result)
            svg=(engine.output/result['svg']).read_text()
            self.assertIn(' C',svg)
            self.assertNotIn('<image',svg)
            self.assertTrue((engine.output/result['png']).exists())
```

### `EngineContractTests.test_roi_and_scale_bounds` — `Lines 99–104`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `99` إلى السطر `104` (`Lines 99–104`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 99–104`):**
```python
    def test_roi_and_scale_bounds(self):
        engine=self.make_engine_fixture()
        self.assertIn('error',engine.dispatch('inspect_region',{'roi':[.8,0,.2,1]}))
        self.assertIn('error',engine.dispatch('render_geometry',{'scale':2}))
        self.assertIn('error',engine.dispatch('stage_candidates',{'trace_ids':[999]}))
        self.assertEqual(engine.state_hash(),engine.initial_hash)
```

### `EngineContractTests.test_duplicate_geometry_different_source_id` — `Lines 106–111`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `106` إلى السطر `111` (`Lines 106–111`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 106–111`):**
```python
    def test_duplicate_geometry_different_source_id(self):
        points=[[2,8],[8,8],[14,8],[24,8]]
        engine=self.make_engine_fixture([synthetic_trace(0,points),synthetic_trace(1,points)])
        result=engine.dispatch('stage_candidates',{'trace_ids':[0,1]})
        self.assertEqual(result['added_paths'],1)
        self.assertEqual(result['ledger'][1]['rejections'][0]['reason'],'duplicate_curve')
```

### `EngineContractTests.test_nested_closed_boundaries_not_semantic_holes` — `Lines 113–120`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `113` إلى السطر `120` (`Lines 113–120`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 113–120`):**
```python
    def test_nested_closed_boundaries_not_semantic_holes(self):
        engine=self.make_engine_fixture([synthetic_trace(0,[[2,2],[28,2],[28,28],[2,28],[2,2]]),synthetic_trace(1,[[8,8],[20,8],[20,20],[8,20],[8,8]])])
        staged=engine.dispatch('stage_candidates',{'trace_ids':[0,1]})
        self.assertEqual(staged['added_paths'],2)
        engine.dispatch('commit_change',{})
        diagnostic=engine.dispatch('validate_geometry',{})
        self.assertEqual(diagnostic['closed_paths'],2)
        self.assertEqual(diagnostic['region_ownership'],'NOT_ESTABLISHED')
```

### `EngineContractTests.test_allowlisted_tool_does_not_accept_path_or_code` — `Lines 122–128`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `122` إلى السطر `128` (`Lines 122–128`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 122–128`):**
```python
    def test_allowlisted_tool_does_not_accept_path_or_code(self):
        engine=self.make_engine_fixture()
        result=engine.dispatch('render_geometry',{'scale':1,'renderer':'untrusted'})
        self.assertIn('error',result)
        self.assertEqual(len(list(engine.output.glob('*.svg'))),0)
        self.assertIn('error',engine.dispatch([],{}))
        self.assertIn('error',engine.dispatch('get_candidates',{'roi':[0,0,1,1],'limit':10**1000}))
```

### `EngineContractTests.test_usable_candidate_not_hidden_by_short_noise` — `Lines 130–137`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `130` إلى السطر `137` (`Lines 130–137`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 130–137`):**
```python
    def test_usable_candidate_not_hidden_by_short_noise(self):
        short=[synthetic_trace(tid,[[2,8],[3,8]]) for tid in range(20)]
        long=synthetic_trace(99,[[2,24],[12,24],[24,24]])
        engine=self.make_engine_fixture(short+[long])
        result=engine.dispatch('get_candidates',{'roi':[0,0,1,1],'limit':4})
        self.assertEqual(result['candidates'][0]['trace_id'],99)
        self.assertTrue(result['candidates'][0]['eligible'])
        self.assertFalse(result['candidates'][1]['eligible'])
```
