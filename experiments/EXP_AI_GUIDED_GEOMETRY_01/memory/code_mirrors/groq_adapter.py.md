# مرآة الكود التفصيلية: `groq_adapter.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `groq_adapter.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `groq_adapter.py`
- **الدور المعماري (`Architectural Role`):** Isolated restricted geometry tools / controller / Groq adapter / evaluator research
- **إجمالي عدد الأسطر (`Total Lines`):** `231` (`Lines 1–231`)
- **بصمة الملف (`SHA-256`):** `e6dfe0a9d09005a044bff7d06c67ac6bc473ef746f0da810245ccd1a7014efff`
- **الوصف التفصيلي:** # START CHANGE AGD-GROQ-ADAPTER | 2026-10-31T11:57:22Z | EDITED | Author: groq_adapter

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `frozen native source/evidence/P curves; provider responses only through strict local tool schemas; evaluator refs only in measurement` | candidate IDs, source coordinates, cubic arrays, typed local requests and budgets | source-only geometry; no unrestricted execution or live requests by default |
| **يرمي إلى (`Throws To`)** | `this isolated experiment` | transaction journals, exact SVG/PNG previews, replay hashes, objective diagnostics and sanitized provider status | offline research; AI NOT_TESTED; geometry NOT_ACCEPTED; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `ProviderGateError` | `class` | `Lines 15–16` | `class ProviderGateError(ValueError):` | A request was stopped before provider execution. |
| `FreeAccountVerification` | `class` | `Lines 20–35` | `class FreeAccountVerification:` | Trusted host input, NEVER populated from model responses. |
| `GroqBudget` | `class` | `Lines 39–61` | `class GroqBudget:` | رمز برمجي موثق. |
| `GroqBudget.validate` | `method` | `Lines 49–61` | `def validate(self):` | رمز برمجي موثق. |
| `_secret_safe` | `function` | `Lines 64–69` | `def _secret_safe(value, secret=""):` | رمز برمجي موثق. |
| `_groq_https` | `function` | `Lines 72–87` | `def _groq_https(payload, secret):` | Fixed host/path, no redirects, retries, SDK, URL fetching, or error-body logs. |
| `GroqAdapter` | `class` | `Lines 90–230` | `class GroqAdapter:` | Provider-neutral API: request(messages, tools, case_id) -> result. |
| `GroqAdapter.__init__` | `method` | `Lines 97–110` | `def __init__(self, *, live=False, verification=None, budget=None, transport=None,` | رمز برمجي موثق. |
| `GroqAdapter.request` | `method` | `Lines 112–148` | `def request(self, messages, tools, case_id):` | رمز برمجي موثق. |
| `GroqAdapter._check_live` | `method` | `Lines 150–168` | `def _check_live(self, case_id, reservation, image_hashes):` | رمز برمجي موثق. |
| `GroqAdapter._prepare` | `method` | `Lines 170–230` | `def _prepare(self, messages, tools):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `ProviderGateError` — `Lines 15–16`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `15` إلى السطر `16` (`Lines 15–16`)
- **الوظيفة:** A request was stopped before provider execution.
- **الكود الفعلي (`Lines 15–16`):**
```python
class ProviderGateError(ValueError):
    """A request was stopped before provider execution."""
```

### `FreeAccountVerification` — `Lines 20–35`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `20` إلى السطر `35` (`Lines 20–35`)
- **الوظيفة:** Trusted host input, NEVER populated from model responses.
- **الكود الفعلي (`Lines 20–35`):**
```python
class FreeAccountVerification:
    """Trusted host input, NEVER populated from model responses.

    A hashed owner-console record must establish free plan, actual remaining quota,
    model access and zero-charge status. Public docs/key presence are insufficient.
    This object records evidence; it does not itself prove a provider billing state.
    """
    verified_by: str = "UNVERIFIED"
    record_sha256: str = ""
    checked_at_unix: float = 0
    free_plan: bool = False
    zero_charge_verified: bool = False
    model_available: bool = False
    requests_remaining: int = 0
    tokens_remaining: int = 0
    permitted_image_sha256: tuple = ()
```

### `GroqBudget` — `Lines 39–61`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `39` إلى السطر `61` (`Lines 39–61`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 39–61`):**
```python
class GroqBudget:
    maximum_requests: int = 4
    maximum_iterations_per_case: int = 2
    maximum_output_tokens: int = 512
    maximum_input_bytes: int = 2_000_000
    maximum_total_reserved_tokens: int = 16_000
    maximum_request_reserved_tokens: int = 7_500
    minimum_request_interval_seconds: float = 61.0
    maximum_cost_usd: float = 0.0

    def validate(self):
        values = (self.maximum_requests, self.maximum_iterations_per_case,
                  self.maximum_output_tokens, self.maximum_input_bytes,
                  self.maximum_total_reserved_tokens, self.maximum_request_reserved_tokens)
        if any(type(v) is not int or v <= 0 for v in values):
            raise ProviderGateError("Invalid integer budget")
        if not (self.maximum_requests <= 4 and self.maximum_iterations_per_case <= 2
                and self.maximum_output_tokens <= 512 and self.maximum_input_bytes <= 2_000_000
                and self.maximum_total_reserved_tokens <= 16_000
                and self.maximum_request_reserved_tokens <= 7_500
                and 61 <= self.minimum_request_interval_seconds <= 3600
                and self.maximum_cost_usd == 0):
            raise ProviderGateError("Budget exceeds bounded free-only pilot")
```

### `GroqBudget.validate` — `Lines 49–61`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `49` إلى السطر `61` (`Lines 49–61`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 49–61`):**
```python
    def validate(self):
        values = (self.maximum_requests, self.maximum_iterations_per_case,
                  self.maximum_output_tokens, self.maximum_input_bytes,
                  self.maximum_total_reserved_tokens, self.maximum_request_reserved_tokens)
        if any(type(v) is not int or v <= 0 for v in values):
            raise ProviderGateError("Invalid integer budget")
        if not (self.maximum_requests <= 4 and self.maximum_iterations_per_case <= 2
                and self.maximum_output_tokens <= 512 and self.maximum_input_bytes <= 2_000_000
                and self.maximum_total_reserved_tokens <= 16_000
                and self.maximum_request_reserved_tokens <= 7_500
                and 61 <= self.minimum_request_interval_seconds <= 3600
                and self.maximum_cost_usd == 0):
            raise ProviderGateError("Budget exceeds bounded free-only pilot")
```

### `_secret_safe` — `Lines 64–69`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `64` إلى السطر `69` (`Lines 64–69`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 64–69`):**
```python
def _secret_safe(value, secret=""):
    text = json.dumps(value, ensure_ascii=True)
    if secret:
        text = text.replace(secret, "[REDACTED]")
    text = re.sub(r"gsk_[A-Za-z0-9_-]+", "[REDACTED]", text)
    return json.loads(text)
```

### `_groq_https` — `Lines 72–87`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `72` إلى السطر `87` (`Lines 72–87`)
- **الوظيفة:** Fixed host/path, no redirects, retries, SDK, URL fetching, or error-body logs.
- **الكود الفعلي (`Lines 72–87`):**
```python
def _groq_https(payload, secret):
    """Fixed host/path, no redirects, retries, SDK, URL fetching, or error-body logs."""
    connection = http.client.HTTPSConnection("api.groq.com", timeout=45)
    try:
        connection.request("POST", "/openai/v1/chat/completions", body=payload,
                           headers={"Authorization": "Bearer " + secret,
                                    "Content-Type": "application/json"})
        response = connection.getresponse()
        if response.status != 200:
            raise ProviderGateError("Provider request failed; no automatic retry")
        raw = response.read(1_000_001)
        if len(raw) > 1_000_000:
            raise ProviderGateError("Provider response exceeded byte limit")
        return json.loads(raw)
    finally:
        connection.close()
```

### `GroqAdapter` — `Lines 90–230`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `90` إلى السطر `230` (`Lines 90–230`)
- **الوظيفة:** Provider-neutral API: request(messages, tools, case_id) -> result.
- **الكود الفعلي (`Lines 90–230`):**
```python
class GroqAdapter:
    """Provider-neutral API: request(messages, tools, case_id) -> result.

    Message content supports text and local data:image/png|jpeg;base64 only.
    The returned assistant tool calls are proposals; the host engine must validate
    names, arguments, transactions and geometry. This adapter never invokes tools.
    """
    def __init__(self, *, live=False, verification=None, budget=None, transport=None,
                 clock=time.time):
        if type(live) is not bool:
            raise ProviderGateError("Live opt-in must be an explicit boolean")
        self.live = live
        self.verification = verification or FreeAccountVerification()
        self.budget = budget or GroqBudget()
        self.budget.validate()
        self._transport = transport or _groq_https
        self._clock = clock
        self._requests = 0
        self._reserved_tokens = 0
        self._case_iterations = {}
        self._last_request = None

    def request(self, messages, tools, case_id):
        if not isinstance(case_id, str) or not re.fullmatch(r"[A-Za-z0-9_-]{1,80}", case_id):
            raise ProviderGateError("Invalid case identifier")
        payload, image_hashes, reservation = self._prepare(messages, tools)
        summary = {"provider": "Groq", "model": MODEL, "images": image_hashes,
                   "reserved_tokens": reservation, "request_bytes": len(payload),
                   "estimated_cost_usd": 0.0, "zero_cost_conditional_on_verified_free_access": True}
        if not self.live:
            return {"status": "DRY_RUN", "ai_performance": "NOT_TESTED", **summary}
        self._check_live(case_id, reservation, image_hashes)
        secret = os.environ.get("GROQ_API_KEY", "")
        if not secret or not secret.isascii() or any(c.isspace() for c in secret):
            raise ProviderGateError("A valid GROQ_API_KEY environment value is required")
        # Reserve before transport: failed requests cannot bypass the bounded budget.
        self._requests += 1
        self._reserved_tokens += reservation
        self._case_iterations[case_id] = self._case_iterations.get(case_id, 0) + 1
        self._last_request = self._clock()
        try:
            data = self._transport(payload, secret)
            if not isinstance(data, dict) or not isinstance(data.get("choices"), list) or len(data["choices"]) != 1:
                raise ProviderGateError("Malformed provider response")
            message = data["choices"][0]["message"]
            if not isinstance(message, dict) or message.get("role") != "assistant":
                raise ProviderGateError("Invalid assistant message")
            usage = data.get("usage", {})
            for name in ("prompt_tokens", "completion_tokens", "total_tokens"):
                if type(usage.get(name)) is not int or usage[name] < 0:
                    raise ProviderGateError("Missing validated provider token usage")
            if usage["total_tokens"] > reservation or usage["completion_tokens"] > self.budget.maximum_output_tokens:
                self._requests = self.budget.maximum_requests
                raise ProviderGateError("Usage exceeded reservation; pilot stopped")
            return _secret_safe({"status": "LIVE", **summary, "message": message,
                                 "usage": usage, "actual_cost_usd": 0.0}, secret)
        except Exception:
            # Never echo provider bodies, exception strings, headers or credential.
            raise ProviderGateError("Live provider request stopped; inspect sanitized status only") from None

    def _check_live(self, case_id, reservation, image_hashes):
        v = self.verification
        age = self._clock() - v.checked_at_unix
        if not (v.verified_by == "owner_console" and re.fullmatch(r"[0-9a-f]{64}", v.record_sha256)
                and 0 <= age <= 86400 and v.free_plan is True
                and v.zero_charge_verified is True and v.model_available is True):
            raise ProviderGateError("Free account, model access and zero charges are NOT VERIFIED")
        if type(v.requests_remaining) is not int or type(v.tokens_remaining) is not int:
            raise ProviderGateError("Account quota must be verified integer counts")
        if any(h not in v.permitted_image_sha256 for h in image_hashes):
            raise ProviderGateError("Image transmission is not authorized")
        if self._requests >= min(self.budget.maximum_requests, v.requests_remaining):
            raise ProviderGateError("Request budget exhausted")
        if self._case_iterations.get(case_id, 0) >= self.budget.maximum_iterations_per_case:
            raise ProviderGateError("Case iteration budget exhausted")
        if self._reserved_tokens + reservation > min(self.budget.maximum_total_reserved_tokens, v.tokens_remaining):
            raise ProviderGateError("Token quota exhausted")
        if self._last_request is not None and self._clock() - self._last_request < self.budget.minimum_request_interval_seconds:
            raise ProviderGateError("Rate budget requires waiting; no automatic sleep or retry")

    def _prepare(self, messages, tools):
        if not isinstance(messages, list) or not 1 <= len(messages) <= 32 or not isinstance(tools, list) or len(tools) > 16:
            raise ProviderGateError("Invalid bounded message/tool arrays")
        image_hashes = []
        for message in messages:
            if not isinstance(message, dict) or message.get("role") not in ("system", "user", "assistant", "tool"):
                raise ProviderGateError("Invalid message")
            content = message.get("content")
            if isinstance(content, list):
                for part in content:
                    if not isinstance(part, dict) or part.get("type") not in ("text", "image_url"):
                        raise ProviderGateError("Unsupported content")
                    if part["type"] == "text":
                        if not isinstance(part.get("text"), str):
                            raise ProviderGateError("Invalid text")
                    else:
                        url = part.get("image_url", {}).get("url", "")
                        if isinstance(url, str) and len(url) > self.budget.maximum_input_bytes:
                            raise ProviderGateError("Encoded image byte budget exceeded")
                        if not isinstance(url, str) or not re.fullmatch(r"data:image/(png|jpeg);base64,[A-Za-z0-9+/=]+", url):
                            raise ProviderGateError("Only explicitly permitted inline PNG/JPEG images are supported")
                        try:
                            raw = base64.b64decode(url.split(",", 1)[1], validate=True)
                        except Exception:
                            raise ProviderGateError("Invalid encoded image") from None
                        if not (raw.startswith(b"\x89PNG\r\n\x1a\n") or raw.startswith(b"\xff\xd8\xff")):
                            raise ProviderGateError("Invalid image signature")
                        image_hashes.append(hashlib.sha256(raw).hexdigest())
            elif content is not None and not isinstance(content, str):
                raise ProviderGateError("Invalid message content")
        if len(image_hashes) > 3:
            raise ProviderGateError("At most three images per request")
        for tool in tools:
            if not isinstance(tool, dict) or not isinstance(tool.get("function"), dict):
                raise ProviderGateError("Invalid tool specification")
            function = tool["function"]
            if tool.get("type") != "function" or not isinstance(function.get("name"), str) or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]{0,63}", function["name"]):
                raise ProviderGateError("Only named local function tools are supported")
            schema = function.get("parameters", {})
            if not isinstance(schema, dict) or schema.get("type") != "object" or schema.get("additionalProperties") is not False:
                raise ProviderGateError("Local tool requires a closed typed object schema")
        request = {"model": MODEL, "messages": messages, "tools": tools, "tool_choice": "auto" if tools else "none",
                   "parallel_tool_calls": False, "temperature": 1, "stream": False,
                   "max_completion_tokens": self.budget.maximum_output_tokens}
        try:
            payload = json.dumps(request, allow_nan=False, separators=(",", ":")).encode("utf-8")
        except Exception:
            raise ProviderGateError("Request is not finite JSON") from None
        if len(payload) > self.budget.maximum_input_bytes:
            raise ProviderGateError("Request byte budget exceeded")
        # Conservative UTF-8-byte text bound, plus documented image tokens.
        stripped = json.loads(payload)
        for message in stripped["messages"]:
            if isinstance(message.get("content"), list):
                for part in message["content"]:
                    if part["type"] == "image_url":
                        part["image_url"]["url"] = "[INLINE_IMAGE]"
        reservation = len(json.dumps(stripped, ensure_ascii=False).encode("utf-8")) + 2048 * len(image_hashes) + self.budget.maximum_output_tokens
        if reservation > self.budget.maximum_request_reserved_tokens:
            raise ProviderGateError("Conservative context/token reservation exceeded")
        return payload, image_hashes, reservation
```

### `GroqAdapter.__init__` — `Lines 97–110`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `97` إلى السطر `110` (`Lines 97–110`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 97–110`):**
```python
    def __init__(self, *, live=False, verification=None, budget=None, transport=None,
                 clock=time.time):
        if type(live) is not bool:
            raise ProviderGateError("Live opt-in must be an explicit boolean")
        self.live = live
        self.verification = verification or FreeAccountVerification()
        self.budget = budget or GroqBudget()
        self.budget.validate()
        self._transport = transport or _groq_https
        self._clock = clock
        self._requests = 0
        self._reserved_tokens = 0
        self._case_iterations = {}
        self._last_request = None
```

### `GroqAdapter.request` — `Lines 112–148`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `112` إلى السطر `148` (`Lines 112–148`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 112–148`):**
```python
    def request(self, messages, tools, case_id):
        if not isinstance(case_id, str) or not re.fullmatch(r"[A-Za-z0-9_-]{1,80}", case_id):
            raise ProviderGateError("Invalid case identifier")
        payload, image_hashes, reservation = self._prepare(messages, tools)
        summary = {"provider": "Groq", "model": MODEL, "images": image_hashes,
                   "reserved_tokens": reservation, "request_bytes": len(payload),
                   "estimated_cost_usd": 0.0, "zero_cost_conditional_on_verified_free_access": True}
        if not self.live:
            return {"status": "DRY_RUN", "ai_performance": "NOT_TESTED", **summary}
        self._check_live(case_id, reservation, image_hashes)
        secret = os.environ.get("GROQ_API_KEY", "")
        if not secret or not secret.isascii() or any(c.isspace() for c in secret):
            raise ProviderGateError("A valid GROQ_API_KEY environment value is required")
        # Reserve before transport: failed requests cannot bypass the bounded budget.
        self._requests += 1
        self._reserved_tokens += reservation
        self._case_iterations[case_id] = self._case_iterations.get(case_id, 0) + 1
        self._last_request = self._clock()
        try:
            data = self._transport(payload, secret)
            if not isinstance(data, dict) or not isinstance(data.get("choices"), list) or len(data["choices"]) != 1:
                raise ProviderGateError("Malformed provider response")
            message = data["choices"][0]["message"]
            if not isinstance(message, dict) or message.get("role") != "assistant":
                raise ProviderGateError("Invalid assistant message")
            usage = data.get("usage", {})
            for name in ("prompt_tokens", "completion_tokens", "total_tokens"):
                if type(usage.get(name)) is not int or usage[name] < 0:
                    raise ProviderGateError("Missing validated provider token usage")
            if usage["total_tokens"] > reservation or usage["completion_tokens"] > self.budget.maximum_output_tokens:
                self._requests = self.budget.maximum_requests
                raise ProviderGateError("Usage exceeded reservation; pilot stopped")
            return _secret_safe({"status": "LIVE", **summary, "message": message,
                                 "usage": usage, "actual_cost_usd": 0.0}, secret)
        except Exception:
            # Never echo provider bodies, exception strings, headers or credential.
            raise ProviderGateError("Live provider request stopped; inspect sanitized status only") from None
```

### `GroqAdapter._check_live` — `Lines 150–168`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `150` إلى السطر `168` (`Lines 150–168`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 150–168`):**
```python
    def _check_live(self, case_id, reservation, image_hashes):
        v = self.verification
        age = self._clock() - v.checked_at_unix
        if not (v.verified_by == "owner_console" and re.fullmatch(r"[0-9a-f]{64}", v.record_sha256)
                and 0 <= age <= 86400 and v.free_plan is True
                and v.zero_charge_verified is True and v.model_available is True):
            raise ProviderGateError("Free account, model access and zero charges are NOT VERIFIED")
        if type(v.requests_remaining) is not int or type(v.tokens_remaining) is not int:
            raise ProviderGateError("Account quota must be verified integer counts")
        if any(h not in v.permitted_image_sha256 for h in image_hashes):
            raise ProviderGateError("Image transmission is not authorized")
        if self._requests >= min(self.budget.maximum_requests, v.requests_remaining):
            raise ProviderGateError("Request budget exhausted")
        if self._case_iterations.get(case_id, 0) >= self.budget.maximum_iterations_per_case:
            raise ProviderGateError("Case iteration budget exhausted")
        if self._reserved_tokens + reservation > min(self.budget.maximum_total_reserved_tokens, v.tokens_remaining):
            raise ProviderGateError("Token quota exhausted")
        if self._last_request is not None and self._clock() - self._last_request < self.budget.minimum_request_interval_seconds:
            raise ProviderGateError("Rate budget requires waiting; no automatic sleep or retry")
```

### `GroqAdapter._prepare` — `Lines 170–230`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `170` إلى السطر `230` (`Lines 170–230`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 170–230`):**
```python
    def _prepare(self, messages, tools):
        if not isinstance(messages, list) or not 1 <= len(messages) <= 32 or not isinstance(tools, list) or len(tools) > 16:
            raise ProviderGateError("Invalid bounded message/tool arrays")
        image_hashes = []
        for message in messages:
            if not isinstance(message, dict) or message.get("role") not in ("system", "user", "assistant", "tool"):
                raise ProviderGateError("Invalid message")
            content = message.get("content")
            if isinstance(content, list):
                for part in content:
                    if not isinstance(part, dict) or part.get("type") not in ("text", "image_url"):
                        raise ProviderGateError("Unsupported content")
                    if part["type"] == "text":
                        if not isinstance(part.get("text"), str):
                            raise ProviderGateError("Invalid text")
                    else:
                        url = part.get("image_url", {}).get("url", "")
                        if isinstance(url, str) and len(url) > self.budget.maximum_input_bytes:
                            raise ProviderGateError("Encoded image byte budget exceeded")
                        if not isinstance(url, str) or not re.fullmatch(r"data:image/(png|jpeg);base64,[A-Za-z0-9+/=]+", url):
                            raise ProviderGateError("Only explicitly permitted inline PNG/JPEG images are supported")
                        try:
                            raw = base64.b64decode(url.split(",", 1)[1], validate=True)
                        except Exception:
                            raise ProviderGateError("Invalid encoded image") from None
                        if not (raw.startswith(b"\x89PNG\r\n\x1a\n") or raw.startswith(b"\xff\xd8\xff")):
                            raise ProviderGateError("Invalid image signature")
                        image_hashes.append(hashlib.sha256(raw).hexdigest())
            elif content is not None and not isinstance(content, str):
                raise ProviderGateError("Invalid message content")
        if len(image_hashes) > 3:
            raise ProviderGateError("At most three images per request")
        for tool in tools:
            if not isinstance(tool, dict) or not isinstance(tool.get("function"), dict):
                raise ProviderGateError("Invalid tool specification")
            function = tool["function"]
            if tool.get("type") != "function" or not isinstance(function.get("name"), str) or not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]{0,63}", function["name"]):
                raise ProviderGateError("Only named local function tools are supported")
            schema = function.get("parameters", {})
            if not isinstance(schema, dict) or schema.get("type") != "object" or schema.get("additionalProperties") is not False:
                raise ProviderGateError("Local tool requires a closed typed object schema")
        request = {"model": MODEL, "messages": messages, "tools": tools, "tool_choice": "auto" if tools else "none",
                   "parallel_tool_calls": False, "temperature": 1, "stream": False,
                   "max_completion_tokens": self.budget.maximum_output_tokens}
        try:
            payload = json.dumps(request, allow_nan=False, separators=(",", ":")).encode("utf-8")
        except Exception:
            raise ProviderGateError("Request is not finite JSON") from None
        if len(payload) > self.budget.maximum_input_bytes:
            raise ProviderGateError("Request byte budget exceeded")
        # Conservative UTF-8-byte text bound, plus documented image tokens.
        stripped = json.loads(payload)
        for message in stripped["messages"]:
            if isinstance(message.get("content"), list):
                for part in message["content"]:
                    if part["type"] == "image_url":
                        part["image_url"]["url"] = "[INLINE_IMAGE]"
        reservation = len(json.dumps(stripped, ensure_ascii=False).encode("utf-8")) + 2048 * len(image_hashes) + self.budget.maximum_output_tokens
        if reservation > self.budget.maximum_request_reserved_tokens:
            raise ProviderGateError("Conservative context/token reservation exceeded")
        return payload, image_hashes, reservation
```
