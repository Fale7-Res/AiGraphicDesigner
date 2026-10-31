# مرآة الكود التفصيلية: `test_groq_adapter.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `test_groq_adapter.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `test_groq_adapter.py`
- **الدور المعماري (`Architectural Role`):** Isolated restricted geometry tools / controller / Groq adapter / evaluator research
- **إجمالي عدد الأسطر (`Total Lines`):** `116` (`Lines 1–116`)
- **بصمة الملف (`SHA-256`):** `c224d7391061ff3f1a32843d0170d653312e3b419b227654393188f74084b77e`
- **الوصف التفصيلي:** # START CHANGE AGD-GROQ-ADAPTER | 2026-10-31T11:57:22Z | EDITED | Author: groq_adapter

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `frozen native source/evidence/P curves; provider responses only through strict local tool schemas; evaluator refs only in measurement` | candidate IDs, source coordinates, cubic arrays, typed local requests and budgets | source-only geometry; no unrestricted execution or live requests by default |
| **يرمي إلى (`Throws To`)** | `this isolated experiment` | transaction journals, exact SVG/PNG previews, replay hashes, objective diagnostics and sanitized provider status | offline research; AI NOT_TESTED; geometry NOT_ACCEPTED; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `GroqAdapterTests` | `class` | `Lines 21–111` | `class GroqAdapterTests(unittest.TestCase):` | رمز برمجي موثق. |
| `GroqAdapterTests.test_dry_run_never_reads_environment_or_calls_transport` | `method` | `Lines 22–27` | `def test_dry_run_never_reads_environment_or_calls_transport(self):` | رمز برمجي موثق. |
| `GroqAdapterTests.test_unverified_live_denied_before_env_access` | `method` | `Lines 29–32` | `def test_unverified_live_denied_before_env_access(self):` | رمز برمجي موثق. |
| `GroqAdapterTests.test_expired_wrong_plan_or_no_zero_charge_evidence_denied` | `method` | `Lines 34–39` | `def test_expired_wrong_plan_or_no_zero_charge_evidence_denied(self):` | رمز برمجي موثق. |
| `GroqAdapterTests.test_image_consent_and_quota_gate` | `method` | `Lines 41–44` | `def test_image_consent_and_quota_gate(self):` | رمز برمجي موثق. |
| `GroqAdapterTests.test_mock_transport_tool_call_is_returned_not_executed` | `method` | `Lines 46–59` | `def test_mock_transport_tool_call_is_returned_not_executed(self):` | رمز برمجي موثق. |
| `GroqAdapterTests.test_mock_transport_tool_call_is_returned_not_executed.fake_transport` | `nested_function` | `Lines 48–53` | `def fake_transport(payload, secret):` | رمز برمجي موثق. |
| `GroqAdapterTests.test_error_never_echoes_credential_and_failure_consumes_budget` | `method` | `Lines 61–70` | `def test_error_never_echoes_credential_and_failure_consumes_budget(self):` | رمز برمجي موثق. |
| `GroqAdapterTests.test_error_never_echoes_credential_and_failure_consumes_budget.bad_transport` | `nested_function` | `Lines 63–64` | `def bad_transport(*_):` | رمز برمجي موثق. |
| `GroqAdapterTests.test_reply_credential_echo_is_redacted` | `method` | `Lines 72–79` | `def test_reply_credential_echo_is_redacted(self):` | رمز برمجي موثق. |
| `GroqAdapterTests.test_reply_credential_echo_is_redacted.echo_transport` | `nested_function` | `Lines 73–75` | `def echo_transport(*_):` | رمز برمجي موثق. |
| `GroqAdapterTests.test_remote_urls_and_more_than_three_images_denied` | `method` | `Lines 81–86` | `def test_remote_urls_and_more_than_three_images_denied(self):` | رمز برمجي موثق. |
| `GroqAdapterTests.test_invalid_budgets_schemas_and_nonfinite_arguments_denied` | `method` | `Lines 88–95` | `def test_invalid_budgets_schemas_and_nonfinite_arguments_denied(self):` | رمز برمجي موثق. |
| `GroqAdapterTests.test_rate_and_iteration_limits_no_automatic_retry` | `method` | `Lines 97–111` | `def test_rate_and_iteration_limits_no_automatic_retry(self):` | رمز برمجي موثق. |
| `GroqAdapterTests.test_rate_and_iteration_limits_no_automatic_retry.transport` | `nested_function` | `Lines 99–101` | `def transport(*_):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `GroqAdapterTests` — `Lines 21–111`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `21` إلى السطر `111` (`Lines 21–111`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 21–111`):**
```python
class GroqAdapterTests(unittest.TestCase):
    def test_dry_run_never_reads_environment_or_calls_transport(self):
        with patch("groq_adapter.os.environ.get", side_effect=AssertionError("unexpected env access")):
            result = GroqAdapter(transport=lambda *_: self.fail("network")).request(MESSAGES, TOOLS, "demo")
        self.assertEqual(result["status"], "DRY_RUN")
        self.assertEqual(result["ai_performance"], "NOT_TESTED")
        self.assertNotIn("base64", json.dumps(result))

    def test_unverified_live_denied_before_env_access(self):
        with patch("groq_adapter.os.environ.get", side_effect=AssertionError("unexpected env access")):
            with self.assertRaisesRegex(ProviderGateError, "NOT VERIFIED"):
                GroqAdapter(live=True).request(MESSAGES, TOOLS, "demo")

    def test_expired_wrong_plan_or_no_zero_charge_evidence_denied(self):
        for changes in ({"checked_at_unix": -100000}, {"free_plan": False},
                        {"zero_charge_verified": False}, {"model_available": False},
                        {"verified_by": "model"}, {"record_sha256": ""}):
            with self.subTest(changes=changes), self.assertRaises(ProviderGateError):
                GroqAdapter(live=True, verification=replace(VERIFIED, **changes), clock=lambda: 1000).request(MESSAGES, TOOLS, "demo")

    def test_image_consent_and_quota_gate(self):
        for changes in ({"permitted_image_sha256": ()}, {"requests_remaining": 0}, {"tokens_remaining": 1}):
            with self.subTest(changes=changes), self.assertRaises(ProviderGateError):
                GroqAdapter(live=True, verification=replace(VERIFIED, **changes), clock=lambda: 1000).request(MESSAGES, TOOLS, "demo")

    def test_mock_transport_tool_call_is_returned_not_executed(self):
        seen = []
        def fake_transport(payload, secret):
            seen.append(json.loads(payload))
            return {"choices": [{"message": {"role": "assistant", "content": None,
                "tool_calls": [{"id": "call1", "type": "function", "function": {
                    "name": "inspect_region", "arguments": "{}"}}]}}],
                "usage": {"prompt_tokens": 2100, "completion_tokens": 40, "total_tokens": 2140}}
        adapter = GroqAdapter(live=True, verification=VERIFIED, transport=fake_transport, clock=lambda: 1000)
        with patch.dict("os.environ", {"GROQ_API_KEY": "synthetic-test-value"}, clear=True):
            result = adapter.request(MESSAGES, TOOLS, "demo")
        self.assertEqual(result["message"]["tool_calls"][0]["function"]["name"], "inspect_region")
        self.assertFalse(seen[0]["parallel_tool_calls"])
        self.assertEqual(result["actual_cost_usd"], 0)

    def test_error_never_echoes_credential_and_failure_consumes_budget(self):
        secret = "synthetic-sensitive-test"
        def bad_transport(*_):
            raise RuntimeError(secret)
        adapter = GroqAdapter(live=True, verification=VERIFIED, transport=bad_transport, clock=lambda: 1000)
        with patch.dict("os.environ", {"GROQ_API_KEY": secret}, clear=True):
            with self.assertRaises(ProviderGateError) as caught:
                adapter.request(MESSAGES, TOOLS, "demo")
        self.assertNotIn(secret, str(caught.exception))
        self.assertEqual(adapter._requests, 1)

    def test_reply_credential_echo_is_redacted(self):
        def echo_transport(*_):
            return {"choices": [{"message": {"role": "assistant", "content": "synthetic-test-value"}}],
                    "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}}
        adapter = GroqAdapter(live=True, verification=VERIFIED, transport=echo_transport, clock=lambda: 1000)
        with patch.dict("os.environ", {"GROQ_API_KEY": "synthetic-test-value"}, clear=True):
            result = adapter.request(MESSAGES, TOOLS, "demo")
        self.assertEqual(result["message"]["content"], "[REDACTED]")

    def test_remote_urls_and_more_than_three_images_denied(self):
        remote = [{"role": "user", "content": [{"type": "image_url", "image_url": {"url": "https://example.com/a.png"}}]}]
        with self.assertRaises(ProviderGateError):
            GroqAdapter().request(remote, TOOLS, "demo")
        with self.assertRaises(ProviderGateError):
            GroqAdapter().request(MESSAGES * 4, TOOLS, "demo")

    def test_invalid_budgets_schemas_and_nonfinite_arguments_denied(self):
        for changes in ({"maximum_requests": 5}, {"maximum_cost_usd": .01},
                        {"maximum_iterations_per_case": 3}, {"minimum_request_interval_seconds": 0}):
            with self.subTest(changes=changes), self.assertRaises(ProviderGateError):
                GroqAdapter(budget=replace(GroqBudget(), **changes))
        for bad in ([{"type": "browser"}], ["not-a-schema"]):
            with self.assertRaises(ProviderGateError):
                GroqAdapter().request(MESSAGES, bad, "demo")

    def test_rate_and_iteration_limits_no_automatic_retry(self):
        now = [1000]
        def transport(*_):
            return {"choices": [{"message": {"role": "assistant", "content": "ok"}}],
                    "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}}
        adapter = GroqAdapter(live=True, verification=VERIFIED, transport=transport, clock=lambda: now[0])
        with patch.dict("os.environ", {"GROQ_API_KEY": "synthetic-test-value"}, clear=True):
            adapter.request(MESSAGES, TOOLS, "demo")
            with self.assertRaisesRegex(ProviderGateError, "Rate budget"):
                adapter.request(MESSAGES, TOOLS, "demo")
            now[0] += 61
            adapter.request(MESSAGES, TOOLS, "demo")
            now[0] += 61
            with self.assertRaisesRegex(ProviderGateError, "iteration"):
                adapter.request(MESSAGES, TOOLS, "demo")
```

### `GroqAdapterTests.test_dry_run_never_reads_environment_or_calls_transport` — `Lines 22–27`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `22` إلى السطر `27` (`Lines 22–27`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 22–27`):**
```python
    def test_dry_run_never_reads_environment_or_calls_transport(self):
        with patch("groq_adapter.os.environ.get", side_effect=AssertionError("unexpected env access")):
            result = GroqAdapter(transport=lambda *_: self.fail("network")).request(MESSAGES, TOOLS, "demo")
        self.assertEqual(result["status"], "DRY_RUN")
        self.assertEqual(result["ai_performance"], "NOT_TESTED")
        self.assertNotIn("base64", json.dumps(result))
```

### `GroqAdapterTests.test_unverified_live_denied_before_env_access` — `Lines 29–32`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `29` إلى السطر `32` (`Lines 29–32`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 29–32`):**
```python
    def test_unverified_live_denied_before_env_access(self):
        with patch("groq_adapter.os.environ.get", side_effect=AssertionError("unexpected env access")):
            with self.assertRaisesRegex(ProviderGateError, "NOT VERIFIED"):
                GroqAdapter(live=True).request(MESSAGES, TOOLS, "demo")
```

### `GroqAdapterTests.test_expired_wrong_plan_or_no_zero_charge_evidence_denied` — `Lines 34–39`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `34` إلى السطر `39` (`Lines 34–39`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 34–39`):**
```python
    def test_expired_wrong_plan_or_no_zero_charge_evidence_denied(self):
        for changes in ({"checked_at_unix": -100000}, {"free_plan": False},
                        {"zero_charge_verified": False}, {"model_available": False},
                        {"verified_by": "model"}, {"record_sha256": ""}):
            with self.subTest(changes=changes), self.assertRaises(ProviderGateError):
                GroqAdapter(live=True, verification=replace(VERIFIED, **changes), clock=lambda: 1000).request(MESSAGES, TOOLS, "demo")
```

### `GroqAdapterTests.test_image_consent_and_quota_gate` — `Lines 41–44`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `41` إلى السطر `44` (`Lines 41–44`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 41–44`):**
```python
    def test_image_consent_and_quota_gate(self):
        for changes in ({"permitted_image_sha256": ()}, {"requests_remaining": 0}, {"tokens_remaining": 1}):
            with self.subTest(changes=changes), self.assertRaises(ProviderGateError):
                GroqAdapter(live=True, verification=replace(VERIFIED, **changes), clock=lambda: 1000).request(MESSAGES, TOOLS, "demo")
```

### `GroqAdapterTests.test_mock_transport_tool_call_is_returned_not_executed` — `Lines 46–59`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `46` إلى السطر `59` (`Lines 46–59`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 46–59`):**
```python
    def test_mock_transport_tool_call_is_returned_not_executed(self):
        seen = []
        def fake_transport(payload, secret):
            seen.append(json.loads(payload))
            return {"choices": [{"message": {"role": "assistant", "content": None,
                "tool_calls": [{"id": "call1", "type": "function", "function": {
                    "name": "inspect_region", "arguments": "{}"}}]}}],
                "usage": {"prompt_tokens": 2100, "completion_tokens": 40, "total_tokens": 2140}}
        adapter = GroqAdapter(live=True, verification=VERIFIED, transport=fake_transport, clock=lambda: 1000)
        with patch.dict("os.environ", {"GROQ_API_KEY": "synthetic-test-value"}, clear=True):
            result = adapter.request(MESSAGES, TOOLS, "demo")
        self.assertEqual(result["message"]["tool_calls"][0]["function"]["name"], "inspect_region")
        self.assertFalse(seen[0]["parallel_tool_calls"])
        self.assertEqual(result["actual_cost_usd"], 0)
```

### `GroqAdapterTests.test_mock_transport_tool_call_is_returned_not_executed.fake_transport` — `Lines 48–53`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `48` إلى السطر `53` (`Lines 48–53`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 48–53`):**
```python
        def fake_transport(payload, secret):
            seen.append(json.loads(payload))
            return {"choices": [{"message": {"role": "assistant", "content": None,
                "tool_calls": [{"id": "call1", "type": "function", "function": {
                    "name": "inspect_region", "arguments": "{}"}}]}}],
                "usage": {"prompt_tokens": 2100, "completion_tokens": 40, "total_tokens": 2140}}
```

### `GroqAdapterTests.test_error_never_echoes_credential_and_failure_consumes_budget` — `Lines 61–70`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `61` إلى السطر `70` (`Lines 61–70`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 61–70`):**
```python
    def test_error_never_echoes_credential_and_failure_consumes_budget(self):
        secret = "synthetic-sensitive-test"
        def bad_transport(*_):
            raise RuntimeError(secret)
        adapter = GroqAdapter(live=True, verification=VERIFIED, transport=bad_transport, clock=lambda: 1000)
        with patch.dict("os.environ", {"GROQ_API_KEY": secret}, clear=True):
            with self.assertRaises(ProviderGateError) as caught:
                adapter.request(MESSAGES, TOOLS, "demo")
        self.assertNotIn(secret, str(caught.exception))
        self.assertEqual(adapter._requests, 1)
```

### `GroqAdapterTests.test_error_never_echoes_credential_and_failure_consumes_budget.bad_transport` — `Lines 63–64`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `63` إلى السطر `64` (`Lines 63–64`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 63–64`):**
```python
        def bad_transport(*_):
            raise RuntimeError(secret)
```

### `GroqAdapterTests.test_reply_credential_echo_is_redacted` — `Lines 72–79`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `72` إلى السطر `79` (`Lines 72–79`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 72–79`):**
```python
    def test_reply_credential_echo_is_redacted(self):
        def echo_transport(*_):
            return {"choices": [{"message": {"role": "assistant", "content": "synthetic-test-value"}}],
                    "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}}
        adapter = GroqAdapter(live=True, verification=VERIFIED, transport=echo_transport, clock=lambda: 1000)
        with patch.dict("os.environ", {"GROQ_API_KEY": "synthetic-test-value"}, clear=True):
            result = adapter.request(MESSAGES, TOOLS, "demo")
        self.assertEqual(result["message"]["content"], "[REDACTED]")
```

### `GroqAdapterTests.test_reply_credential_echo_is_redacted.echo_transport` — `Lines 73–75`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `73` إلى السطر `75` (`Lines 73–75`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 73–75`):**
```python
        def echo_transport(*_):
            return {"choices": [{"message": {"role": "assistant", "content": "synthetic-test-value"}}],
                    "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}}
```

### `GroqAdapterTests.test_remote_urls_and_more_than_three_images_denied` — `Lines 81–86`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `81` إلى السطر `86` (`Lines 81–86`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 81–86`):**
```python
    def test_remote_urls_and_more_than_three_images_denied(self):
        remote = [{"role": "user", "content": [{"type": "image_url", "image_url": {"url": "https://example.com/a.png"}}]}]
        with self.assertRaises(ProviderGateError):
            GroqAdapter().request(remote, TOOLS, "demo")
        with self.assertRaises(ProviderGateError):
            GroqAdapter().request(MESSAGES * 4, TOOLS, "demo")
```

### `GroqAdapterTests.test_invalid_budgets_schemas_and_nonfinite_arguments_denied` — `Lines 88–95`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `88` إلى السطر `95` (`Lines 88–95`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 88–95`):**
```python
    def test_invalid_budgets_schemas_and_nonfinite_arguments_denied(self):
        for changes in ({"maximum_requests": 5}, {"maximum_cost_usd": .01},
                        {"maximum_iterations_per_case": 3}, {"minimum_request_interval_seconds": 0}):
            with self.subTest(changes=changes), self.assertRaises(ProviderGateError):
                GroqAdapter(budget=replace(GroqBudget(), **changes))
        for bad in ([{"type": "browser"}], ["not-a-schema"]):
            with self.assertRaises(ProviderGateError):
                GroqAdapter().request(MESSAGES, bad, "demo")
```

### `GroqAdapterTests.test_rate_and_iteration_limits_no_automatic_retry` — `Lines 97–111`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `97` إلى السطر `111` (`Lines 97–111`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 97–111`):**
```python
    def test_rate_and_iteration_limits_no_automatic_retry(self):
        now = [1000]
        def transport(*_):
            return {"choices": [{"message": {"role": "assistant", "content": "ok"}}],
                    "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}}
        adapter = GroqAdapter(live=True, verification=VERIFIED, transport=transport, clock=lambda: now[0])
        with patch.dict("os.environ", {"GROQ_API_KEY": "synthetic-test-value"}, clear=True):
            adapter.request(MESSAGES, TOOLS, "demo")
            with self.assertRaisesRegex(ProviderGateError, "Rate budget"):
                adapter.request(MESSAGES, TOOLS, "demo")
            now[0] += 61
            adapter.request(MESSAGES, TOOLS, "demo")
            now[0] += 61
            with self.assertRaisesRegex(ProviderGateError, "iteration"):
                adapter.request(MESSAGES, TOOLS, "demo")
```

### `GroqAdapterTests.test_rate_and_iteration_limits_no_automatic_retry.transport` — `Lines 99–101`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `99` إلى السطر `101` (`Lines 99–101`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 99–101`):**
```python
        def transport(*_):
            return {"choices": [{"message": {"role": "assistant", "content": "ok"}}],
                    "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}}
```
