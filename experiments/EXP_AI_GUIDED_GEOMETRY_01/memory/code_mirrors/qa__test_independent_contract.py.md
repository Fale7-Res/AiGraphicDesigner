# مرآة الكود التفصيلية: `qa/test_independent_contract.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `qa/test_independent_contract.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `qa/test_independent_contract.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `132` (`Lines 1–132`)
- **بصمة الملف (`SHA-256`):** `8b8c0821a52488576fa00f80287f1d1b6b03ed8d95520bc1fb021bd0a05a6f71`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `independent_record_digest` | `function` | `Lines 22–23` | `def independent_record_digest(value):` | رمز برمجي موثق. |
| `IndependentEngineAudit` | `class` | `Lines 26–127` | `class IndependentEngineAudit(unittest.TestCase):` | رمز برمجي موثق. |
| `IndependentEngineAudit.audit_fixture` | `method` | `Lines 27–37` | `def audit_fixture(self):` | رمز برمجي موثق. |
| `IndependentEngineAudit.test_reject_arbitrary_execution_and_argument_injection` | `method` | `Lines 39–55` | `def test_reject_arbitrary_execution_and_argument_injection(self):` | رمز برمجي موثق. |
| `IndependentEngineAudit.test_huge_integer_and_nonstring_tool_fail_closed` | `method` | `Lines 57–64` | `def test_huge_integer_and_nonstring_tool_fail_closed(self):` | رمز برمجي موثق. |
| `IndependentEngineAudit.test_transaction_revert_does_not_erase_audit_or_refund_calls` | `method` | `Lines 66–91` | `def test_transaction_revert_does_not_erase_audit_or_refund_calls(self):` | رمز برمجي موثق. |
| `IndependentEngineAudit.test_rejected_calls_consume_finite_budget` | `method` | `Lines 93–100` | `def test_rejected_calls_consume_finite_budget(self):` | رمز برمجي موثق. |
| `IndependentEngineAudit.test_replay_geometry_and_real_svg_are_identical` | `method` | `Lines 102–127` | `def test_replay_geometry_and_real_svg_are_identical(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `independent_record_digest` — `Lines 22–23`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `22` إلى السطر `23` (`Lines 22–23`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 22–23`):**
```python
def independent_record_digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()
```

### `IndependentEngineAudit` — `Lines 26–127`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `26` إلى السطر `127` (`Lines 26–127`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 26–127`):**
```python
class IndependentEngineAudit(unittest.TestCase):
    def audit_fixture(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        rgb = np.full((32, 32, 3), 255, dtype=np.uint8)
        rgb[4:5, 4:24] = 0
        traces = [
            {'trace_id': 1, 'source_points_xy': [[4,4],[24,4],[24,24],[4,24],[4,4]]},
            {'trace_id': 2, 'source_points_xy': [[4,4],[4,1],[12,1]]},
        ]
        return target.GeometryToolEngine(rgb, traces, [], Path(temp.name)/'session',
            Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner'), BASE/'work')

    def test_reject_arbitrary_execution_and_argument_injection(self):
        attacks = [
            ('__class__', {}), ('exec', {'code': 'arbitrary'}),
            ('render_geometry', {'scale': 1, 'path': '../escape.svg'}),
            ('inspect_region', {'roi': [0,0,1,1], 'url': 'https://invalid.example'}),
            ('stage_candidates', {'trace_ids': [True]}),
            ('get_candidates', {'roi': [0,0,1,1], 'limit': 1.0}),
            ('inspect_region', {'roi': [0,0,float('inf'),1]}),
            ('stage_candidates', {'trace_ids': [1,1]}),
            ('stage_candidates', {'trace_ids': [999999]}),
        ]
        for name,args in attacks:
            engine = self.audit_fixture()
            result = engine.dispatch(name,args)
            self.assertIn('error', result, (name,args))
            self.assertEqual(engine.state_hash(), engine.initial_hash)
            self.assertEqual(len(engine.events), 1)

    def test_huge_integer_and_nonstring_tool_fail_closed(self):
        for name,args in [('stage_candidates', {'trace_ids': [10**1000]}),
                          ([], {}), (None, {}),
                          ('get_candidates', {'roi':[0,0,1,1], 'limit':10**1000})]:
            engine = self.audit_fixture()
            result = engine.dispatch(name,args)
            self.assertIn('error',result)
            self.assertEqual(engine.state_hash(),engine.initial_hash)

    def test_transaction_revert_does_not_erase_audit_or_refund_calls(self):
        engine = self.audit_fixture()
        staged = engine.dispatch('stage_candidates', {'trace_ids':[1]})
        self.assertGreater(staged['added_paths'],0)
        self.assertEqual(engine.state_hash(),engine.initial_hash)
        self.assertEqual(engine.dispatch('commit_change',{})['status'],'committed')
        changed = engine.state_hash()
        self.assertNotEqual(changed,engine.initial_hash)
        self.assertEqual(engine.dispatch('rollback_change',{})['status'],'committed_edit_reverted')
        self.assertEqual(engine.state_hash(),engine.initial_hash)
        self.assertEqual(len(engine.events),3)
        self.assertEqual(engine.commits,1)
        previous = engine.source_pin
        for index,event in enumerate(engine.events):
            self.assertEqual(event['sequence'],index)
            self.assertEqual(event['previous_record_hash'],previous)
            disk = json.loads((engine.output/f'event_{index:03d}.json').read_text())
            self.assertEqual(disk,event)
            record = dict(disk)
            supplied = record.pop('record_hash')
            self.assertEqual(independent_record_digest(record),supplied)
            previous = supplied
        modified = copy.deepcopy(engine.events[1])
        modified['after_hash'] = '0'*64
        recorded = modified.pop('record_hash')
        self.assertNotEqual(independent_record_digest(modified),recorded)

    def test_rejected_calls_consume_finite_budget(self):
        engine = self.audit_fixture()
        for _ in range(engine.max_calls):
            self.assertIn('error',engine.dispatch('not_a_tool',{}))
        with self.assertRaises(ValueError):
            engine.dispatch('validate_geometry',{})
        self.assertEqual(len(engine.events),engine.max_calls)
        self.assertEqual(engine.state_hash(),engine.initial_hash)

    def test_replay_geometry_and_real_svg_are_identical(self):
        plan = [('inspect_region',{'roi':[0,0,1,1]}),
                ('get_candidates',{'roi':[0,0,1,1],'limit':4}),
                ('stage_candidates',{'trace_ids':[1,2]}),
                ('commit_change',{}), ('validate_geometry',{}),
                ('render_geometry',{'scale':1})]
        first, second = self.audit_fixture(), self.audit_fixture()
        rendered = []
        for engine in (first,second):
            for name,args in plan:
                answer = engine.dispatch(name,args)
                self.assertNotIn('error',answer)
            svg = (engine.output/answer['svg']).read_bytes()
            rendered.append(svg)
            root = ET.fromstring(svg)
            tags = [node.tag.rsplit('}',1)[-1] for node in root.iter()]
            self.assertNotIn('image',tags)
            self.assertNotIn('rect',tags)
            self.assertNotIn('script',tags)
            self.assertNotIn('foreignObject',tags)
            self.assertEqual(tags.count('path'),len(engine.items))
            self.assertTrue((engine.output/answer['png']).exists())
        self.assertEqual(first.source_pin,second.source_pin)
        self.assertEqual(first.state_hash(),second.state_hash())
        self.assertEqual(rendered[0],rendered[1])
        self.assertEqual([e['status'] for e in first.events],[e['status'] for e in second.events])
```

### `IndependentEngineAudit.audit_fixture` — `Lines 27–37`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `27` إلى السطر `37` (`Lines 27–37`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 27–37`):**
```python
    def audit_fixture(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        rgb = np.full((32, 32, 3), 255, dtype=np.uint8)
        rgb[4:5, 4:24] = 0
        traces = [
            {'trace_id': 1, 'source_points_xy': [[4,4],[24,4],[24,24],[4,24],[4,4]]},
            {'trace_id': 2, 'source_points_xy': [[4,4],[4,1],[12,1]]},
        ]
        return target.GeometryToolEngine(rgb, traces, [], Path(temp.name)/'session',
            Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner'), BASE/'work')
```

### `IndependentEngineAudit.test_reject_arbitrary_execution_and_argument_injection` — `Lines 39–55`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `39` إلى السطر `55` (`Lines 39–55`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 39–55`):**
```python
    def test_reject_arbitrary_execution_and_argument_injection(self):
        attacks = [
            ('__class__', {}), ('exec', {'code': 'arbitrary'}),
            ('render_geometry', {'scale': 1, 'path': '../escape.svg'}),
            ('inspect_region', {'roi': [0,0,1,1], 'url': 'https://invalid.example'}),
            ('stage_candidates', {'trace_ids': [True]}),
            ('get_candidates', {'roi': [0,0,1,1], 'limit': 1.0}),
            ('inspect_region', {'roi': [0,0,float('inf'),1]}),
            ('stage_candidates', {'trace_ids': [1,1]}),
            ('stage_candidates', {'trace_ids': [999999]}),
        ]
        for name,args in attacks:
            engine = self.audit_fixture()
            result = engine.dispatch(name,args)
            self.assertIn('error', result, (name,args))
            self.assertEqual(engine.state_hash(), engine.initial_hash)
            self.assertEqual(len(engine.events), 1)
```

### `IndependentEngineAudit.test_huge_integer_and_nonstring_tool_fail_closed` — `Lines 57–64`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `57` إلى السطر `64` (`Lines 57–64`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 57–64`):**
```python
    def test_huge_integer_and_nonstring_tool_fail_closed(self):
        for name,args in [('stage_candidates', {'trace_ids': [10**1000]}),
                          ([], {}), (None, {}),
                          ('get_candidates', {'roi':[0,0,1,1], 'limit':10**1000})]:
            engine = self.audit_fixture()
            result = engine.dispatch(name,args)
            self.assertIn('error',result)
            self.assertEqual(engine.state_hash(),engine.initial_hash)
```

### `IndependentEngineAudit.test_transaction_revert_does_not_erase_audit_or_refund_calls` — `Lines 66–91`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `66` إلى السطر `91` (`Lines 66–91`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 66–91`):**
```python
    def test_transaction_revert_does_not_erase_audit_or_refund_calls(self):
        engine = self.audit_fixture()
        staged = engine.dispatch('stage_candidates', {'trace_ids':[1]})
        self.assertGreater(staged['added_paths'],0)
        self.assertEqual(engine.state_hash(),engine.initial_hash)
        self.assertEqual(engine.dispatch('commit_change',{})['status'],'committed')
        changed = engine.state_hash()
        self.assertNotEqual(changed,engine.initial_hash)
        self.assertEqual(engine.dispatch('rollback_change',{})['status'],'committed_edit_reverted')
        self.assertEqual(engine.state_hash(),engine.initial_hash)
        self.assertEqual(len(engine.events),3)
        self.assertEqual(engine.commits,1)
        previous = engine.source_pin
        for index,event in enumerate(engine.events):
            self.assertEqual(event['sequence'],index)
            self.assertEqual(event['previous_record_hash'],previous)
            disk = json.loads((engine.output/f'event_{index:03d}.json').read_text())
            self.assertEqual(disk,event)
            record = dict(disk)
            supplied = record.pop('record_hash')
            self.assertEqual(independent_record_digest(record),supplied)
            previous = supplied
        modified = copy.deepcopy(engine.events[1])
        modified['after_hash'] = '0'*64
        recorded = modified.pop('record_hash')
        self.assertNotEqual(independent_record_digest(modified),recorded)
```

### `IndependentEngineAudit.test_rejected_calls_consume_finite_budget` — `Lines 93–100`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `93` إلى السطر `100` (`Lines 93–100`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 93–100`):**
```python
    def test_rejected_calls_consume_finite_budget(self):
        engine = self.audit_fixture()
        for _ in range(engine.max_calls):
            self.assertIn('error',engine.dispatch('not_a_tool',{}))
        with self.assertRaises(ValueError):
            engine.dispatch('validate_geometry',{})
        self.assertEqual(len(engine.events),engine.max_calls)
        self.assertEqual(engine.state_hash(),engine.initial_hash)
```

### `IndependentEngineAudit.test_replay_geometry_and_real_svg_are_identical` — `Lines 102–127`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `102` إلى السطر `127` (`Lines 102–127`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 102–127`):**
```python
    def test_replay_geometry_and_real_svg_are_identical(self):
        plan = [('inspect_region',{'roi':[0,0,1,1]}),
                ('get_candidates',{'roi':[0,0,1,1],'limit':4}),
                ('stage_candidates',{'trace_ids':[1,2]}),
                ('commit_change',{}), ('validate_geometry',{}),
                ('render_geometry',{'scale':1})]
        first, second = self.audit_fixture(), self.audit_fixture()
        rendered = []
        for engine in (first,second):
            for name,args in plan:
                answer = engine.dispatch(name,args)
                self.assertNotIn('error',answer)
            svg = (engine.output/answer['svg']).read_bytes()
            rendered.append(svg)
            root = ET.fromstring(svg)
            tags = [node.tag.rsplit('}',1)[-1] for node in root.iter()]
            self.assertNotIn('image',tags)
            self.assertNotIn('rect',tags)
            self.assertNotIn('script',tags)
            self.assertNotIn('foreignObject',tags)
            self.assertEqual(tags.count('path'),len(engine.items))
            self.assertTrue((engine.output/answer['png']).exists())
        self.assertEqual(first.source_pin,second.source_pin)
        self.assertEqual(first.state_hash(),second.state_hash())
        self.assertEqual(rendered[0],rendered[1])
        self.assertEqual([e['status'] for e in first.events],[e['status'] for e in second.events])
```
