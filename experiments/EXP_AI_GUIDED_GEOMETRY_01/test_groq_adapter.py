# START CHANGE AGD-GROQ-ADAPTER | 2026-10-31T11:57:22Z | EDITED | Author: groq_adapter
"""No network. Synthetic credential values only; no owner environment inspection."""
import base64
from dataclasses import replace
import hashlib
import json
import unittest
from unittest.mock import patch
from groq_adapter import FreeAccountVerification, GroqAdapter, GroqBudget, ProviderGateError

IMAGE = b"\x89PNG\r\n\x1a\nsynthetic-fixture"
HASH = hashlib.sha256(IMAGE).hexdigest()
MESSAGES = [{"role": "user", "content": [
    {"type": "text", "text": "Inspect geometry using local tools"},
    {"type": "image_url", "image_url": {"url": "data:image/png;base64," + base64.b64encode(IMAGE).decode()}}]}]
TOOLS = [{"type": "function", "function": {"name": "inspect_region", "parameters": {
    "type": "object", "properties": {}, "required": [], "additionalProperties": False}}}]
VERIFIED = FreeAccountVerification("owner_console", "a" * 64, 1000, True, True, True, 4, 16000, (HASH,))


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


if __name__ == "__main__":
    unittest.main()
# END CHANGE AGD-GROQ-ADAPTER | 2026-10-31T11:57:22Z | EDITED | Author: groq_adapter
