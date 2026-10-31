<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-31T15:16:24Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-31T15:16:24Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-31T15:16:24Z"}
END_DOC_PROVENANCE -->
# Groq provider boundary and verified prerequisites

Status: adapter operational with synthetic transport; **real Groq inference NOT_TESTED**. No owner credential was read, copied or used by this work package. No real HTTP request, account inquiry or image upload was executed. The credential supplied in the conversation must be revoked and replaced outside this research record; the adapter reads a replacement only from `GROQ_API_KEY` after every live gate passes.

Official documentation checked 2026-10-31:

- [Vision](https://console.groq.com/docs/vision): `qwen/qwen3.8-27b` is documented for image and text input, tool use and JSON mode. It has a documented 131K context, three-image request limit and 2048 input tokens per image. This verifies public model capability, not this owner's account access.
- [Local function calling](https://console.groq.com/docs/tool-use/local-tool-calling): the application executes named functions and returns their results. The provider only proposes calls. Our geometry engine must independently validate every function and argument and cannot expose shell/Python/filesystem/network execution.
- [Rate limits](https://console.groq.com/docs/rate-limits): public Free Plan table lists 30 RPM, 1000 RPD, 8000 TPM and 200000 TPD for this model. Limits belong to the organization, and the documentation directs users to their account's Limits page for exact current values. Published limits do not prove remaining quota or absence of billing.
- [API reference](https://console.groq.com/docs/api-reference): use the fixed `POST https://api.groq.com/openai/v1/chat/completions` endpoint, `messages`, `tools`, `tool_choice`, and `max_completion_tokens`. Parallel calls and streaming are disabled in this pilot.

The larger `meta-models/muse-spark-open` vision alternative is documented as limited preview requiring provider contact. It is not a better first bounded free-access candidate. No additional provider/model is implemented.

## What is unverified

The owner's account plan, effective model permissions, free quota remaining, zero-charge billing condition, and legal permission to transmit particular source images are **NOT ESTABLISHED**. An API key's presence is not proof. A successful models listing or public rate table would also not establish zero-charge execution. We therefore stop at dry-run and transport simulation until trusted owner-console evidence establishes those conditions.

No arbitrary fake assertion should be placed in `FreeAccountVerification` to bypass this requirement. Its values must come from owner-controlled host configuration backed by a redacted, dated console verification record. Never accept them from a model tool call, prompt, generated plan, or provider response. This evidence object records the independent verification; Python cannot independently guarantee the provider's billing state from those booleans.

## Interface

`GroqAdapter(live=False).request(messages, tools, case_id)` returns a bounded dry-run summary without reading the environment or calling its transport. The summary contains image SHA-256 values, byte count and conservative token reservation, not images, prompts, headers or credentials.

`messages` use OpenAI-compatible chat records. Inline PNG/JPEG data URLs are supported; remote URLs are rejected. Images are supplied by the trusted host, not loaded from model-selected paths. `tools` must contain only local function declarations with closed object schemas (`additionalProperties: false`). The host must additionally validate nested argument types and ranges against its canonical allowlist; the adapter does not execute geometry functions.

`GroqAdapter(live=True, verification=..., budget=...)` requires all gates, then reads `GROQ_API_KEY` solely from the environment. A transport callback can be injected for deterministic offline tests; the default transport uses standard-library HTTPS with a fixed host/path, certificate validation, bounded response size, no redirect following and no retries. Provider error bodies and raw exception strings are never exposed. Successful messages are credential-redacted before return. Returned tool calls remain untrusted proposals for the engine dispatcher.

Tool-loop host sequence: build permitted source/preview message; request proposal; validate tool arguments; execute transaction locally; render SVG; return concise objective diagnostics and permitted preview; request next proposal within the same budget. Preserve sanitized call/result records and canonical replay plans. The adapter does not create API logs or write files.

## Frozen pilot limits

- Default dry-run; explicit host opt-in is necessary, not sufficient.
- Maximum four requests globally, two request iterations per case, three images per request and 512 output tokens per request.
- Maximum request payload 2 MB; local conservative request reservation 7500 tokens, total reservation 16000 tokens. Text/schema byte count is conservatively reserved as tokens, plus documented image token charges and the output limit. This intentionally overestimates text rather than depending on an unverified tokenizer. Large schemas may be refused; use a bounded compact canonical tool set instead of raising the cap.
- Minimum 61 seconds between requests; refusal rather than sleeping/retrying. The host must wait explicitly. Failed requests consume local budget.
- Verified remaining request/token quota must cover the reservation. Account evidence expires after 24 hours. Maximum allowed cost is zero; any uncertain billing state denies execution.
- The host must allowlist each exact transmitted source/crop/render byte hash. Crops and previews need separate hashes and permission; no private Fine Features asset or other unknown-rights source may be included automatically.

For a proposed first two-call/one-case pilot, report the actual selected source and preview hashes before opt-in. Two one-image calls reserve 4096 documented image tokens in total, plus actual compact prompt/schema bytes and at most 1024 output tokens. Exact dry-run estimates must be shown before any call; the full four-request limit is not permission to consume unknown quota. No actual charge or token consumption has been measured in this offline work.

## Reproduction and tests

From the task workspace run `work\agd-native\Scripts\python.exe work\agentic_geometry\provider\test_groq_adapter.py`. Ten tests use synthetic inline bytes and synthetic environment values, never an owner key. They verify default no-network/no-environment access, independent live prerequisites, image consent, quota, schema limits, rate/iteration stopping, sanitized errors, secret echo redaction and function-call round trips through an injected mock transport. Mock transport status is a test of the code path, not actual model performance or billing verification.

Independent parent QA must review the engine's canonical schemas, rollback, allowed tool dispatch, holdout isolation and public artifact sanitization. This provider package does not establish geometry improvement. Geometry remains NOT_ACCEPTED; architecture remains NOT_APPROVED.
