# مرآة الكود التفصيلية: `reports/hardening/qa/audit_saved_v3.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `reports/hardening/qa/audit_saved_v3.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `reports/hardening/qa/audit_saved_v3.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `86` (`Lines 1–86`)
- **بصمة الملف (`SHA-256`):** `a2796ffe9f8f03021cec4d08ced45a38df0329973c1b2fb86499b21141d10cc9`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `saved_digest` | `function` | `Lines 10–11` | `def saved_digest(value):` | رمز برمجي موثق. |
| `unique_saved_pairs` | `function` | `Lines 13–18` | `def unique_saved_pairs(pairs):` | رمز برمجي موثق. |
| `read_saved` | `function` | `Lines 20–21` | `def read_saved(path):` | رمز برمجي موثق. |
| `inspect_saved_session` | `function` | `Lines 23–75` | `def inspect_saved_session(folder):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `saved_digest` — `Lines 10–11`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `10` إلى السطر `11` (`Lines 10–11`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 10–11`):**
```python
def saved_digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()
```

### `unique_saved_pairs` — `Lines 13–18`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `18` (`Lines 13–18`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 13–18`):**
```python
def unique_saved_pairs(pairs):
    out={}
    for key,value in pairs:
        assert key not in out
        out[key]=value
    return out
```

### `read_saved` — `Lines 20–21`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `20` إلى السطر `21` (`Lines 20–21`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 20–21`):**
```python
def read_saved(path):
    return json.loads(path.read_text(),object_pairs_hook=unique_saved_pairs)
```

### `inspect_saved_session` — `Lines 23–75`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `23` إلى السطر `75` (`Lines 23–75`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 23–75`):**
```python
def inspect_saved_session(folder):
    previous='ROOT';prior_requests=0;prior_reserved=0;reserved=0;usage_records=0
    records=sorted(folder.glob('record_*.json'))
    for i,path in enumerate(records):
        assert path.name==f'record_{i:03d}.json'
        record=read_saved(path);supplied=record.pop('hash')
        assert saved_digest(record)==supplied
        assert record['sequence']==i and record['previous']==previous
        previous=supplied;state=record['state']
        if i==0:source_pin=state['source_pin'];implementation=state['implementation_pin']
        assert state['source_pin']==source_pin and state['implementation_pin']==implementation
        if record['kind']=='REQUEST_RESERVED':
            reserved+=1
            assert state['requests']==prior_requests+1 and state['reserved_tokens']>prior_reserved
        else:assert state['requests']==prior_requests and state['reserved_tokens']==prior_reserved
        prior_requests=state['requests'];prior_reserved=state['reserved_tokens']
        if record['kind']=='USAGE_RECEIVED':usage_records+=1
        for usage in state.get('usage',[]):
            assert set(usage)=={'prompt_tokens','completion_tokens','total_tokens'}
            assert all(type(v) is int and v>=0 for v in usage.values())
            assert usage['prompt_tokens']+usage['completion_tokens']==usage['total_tokens']
        assert all(obs['authority']=='UNTRUSTED_PLANNER_OBSERVATION' for obs in state['observations'])
        assert hashlib.sha256((folder/state['preview']['file']).read_bytes()).hexdigest()==state['preview']['sha256']
        assert len(state['engine']['events'])<=12 and state['engine']['commits']<=2
    assert records and state['phase']=='COMPLETE' and state['mode']=='synthetic'
    assert (reserved,usage_records,state['requests'])==(2,2,2)
    assert [a['request_index'] for a in state['approvals']]==[0,1]
    assert len(state['call_ids'])==len(set(state['call_ids']))==2
    assert state['geometry_hash']==saved_digest(state['engine']['items'])
    prior_event=source_pin
    for i,event in enumerate(state['engine']['events']):
        assert read_saved(folder/'initial_engine'/f'event_{i:03d}.json')==event
        row=dict(event);supplied=row.pop('record_hash')
        assert saved_digest(row)==supplied and event['previous_record_hash']==prior_event
        prior_event=supplied
    files=[ROOT/'pilot_control.py',ROOT/'hardened_pilot.py',OLD/'geometry_engine.py',
        ROOT.parent/'EXP_LOSS_ACCOUNTED_CONTOUR_CONSTRUCTION_01/partition_fit.py',
        ROOT.parent/'EXP_EXPORTER_DISCOVERY_01/svg_exporter.py']
    current_pin=saved_digest({str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest() for p in files})
    rendered=next(e['result'] for e in reversed(state['engine']['events']) if e['tool']=='render_geometry')
    svg=ET.parse(folder/'initial_engine'/rendered['svg']).getroot()
    tags=[el.tag.rsplit('}',1)[-1] for el in svg.iter()]
    assert not set(tags)&{'image','rect','script','foreignObject'}
    assert tags.count('path')==len(state['engine']['items'])==132
    with Image.open(folder/'initial_engine'/rendered['png']) as image:image.verify()
    summary=read_saved(folder/'SUMMARY.json')
    assert summary['real_requests']==0 and summary['AI_performance']=='NOT_TESTED'
    return dict(folder=folder.name,records=len(records),requests_synthetic=state['requests'],
        reserved_tokens=state['reserved_tokens'],completion_tokens=state['completion_tokens'],
        tool_calls=len(state['engine']['events']),commits=state['engine']['commits'],
        geometry_hash=state['geometry_hash'],implementation_pin=implementation,
        current_implementation_matches=implementation==current_pin,
        final_preview_sha256=state['preview']['sha256'],passed=True),summary
```
