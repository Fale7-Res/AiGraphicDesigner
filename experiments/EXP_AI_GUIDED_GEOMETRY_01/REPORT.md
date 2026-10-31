<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-31T15:16:24Z", "last_action": "EDITED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-31T15:18:14Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-31T15:16:24Z"}
END_DOC_PROVENANCE -->
# AI-guided geometry tool proof of concept — offline evidence and live decision

Geometry **NOT_ACCEPTED**. Production architecture **NOT_APPROVED**. Real AI performance **NOT_TESTED**.

## Decision and verified state

**VERIFIED:** a restricted local tool engine executes recorded sessions end-to-end: source inspection, source-derived candidate queries, partitioned cubic fitting, transactional staging/commit/rejection, rendering, validation and exact rollback/replay controls. Fourteen deterministic/mock sessions across seven cases produced168 immutable linked events and real SVGs. This validates infrastructure, not a vision model or architectural superiority.

**SUPPORTED BUT LIMITED:** the deterministic controller adds small amounts of source-supported geometry in Shield, Burger, Logo and Astronaut. It does not recover complete artwork. Arabic, K01 and the new known-vector holdout receive no additions. Atomic region counts stay unchanged. The mock is explicitly NOT AI.

**NOT ESTABLISHED:** better AI planning, complete crown/Burger/Arabic geometry, semantic hole ownership, universal reconstruction, final visual fidelity or production readiness. No real Groq inference, image upload or billable request occurred; actual API requests0, costUSD0 because nothing was requested. Synthetic transport tests that return a LIVE status are fixtures, not provider execution.

Starting clean local main and actual remote main were `46870cbf109454dfd243a7bffab692a692bc2b52`. The owner-published Universal Region/Coherence package is present. Original vision was read completely and remains unchanged: image generation, future professional SVG, Arabic typography, semantic layers, Magic Layers, editability and visual QA remain future requirements. No final appearance code was added.

## Architecture implemented and reused

Provider-neutral planner contract: structured local function proposals. The optional Groq adapter handles only the fixed Groq HTTPS API; it never executes model tool names. The host allowlist validates tool arguments, and mandatory geometry guards cannot be overridden by the model. Images and model/tool text are untrusted observations. No arbitrary Python, shell, file, network or Git command is exposed to the planner.

The minimal engine tools are `inspect_region`, `get_candidates`, `stage_candidates`, `commit_change`, `rollback_change`, `validate_geometry`, `render_geometry`. Geometry edits select frozen trace IDs, not emitted control coordinates. Only normalized inspection ROI coordinates are accepted. Immutable per-call event files record validated arguments, source/state hashes, outcomes and rejection ledgers. Exclusive-file creation prevents accidental overwrite. Hash links detect tampering but do not make local disk tamper-proof against its owner.

Reused: frozen Classical evidence/traces, P source partitioning and cubic fitter,0.6px numerical deviation gate, conservative raw-vs-fitted crossing guards, corrected compound-path SVG serializer, resvg, process-tree monitoring, independent reference definitions and geometry diagnostics. Region integration is reused by the evaluator to assess potential faces; it is not exposed as a completed model-editing tool. No old model inference or benchmark search was repeated.

The engine can query and add excluded existing source contours. It currently cannot discover a wholly absent boundary, move/refine accepted geometry, create missing junctions, repair segmentation, establish object/hole ownership or perform region topology edits. Visual reasoning cannot compensate for missing execution capabilities. This is a meaningful but deliberately restricted tool-controller proof of concept, not the full proposed universal engine.

## Frozen controls, fairness and resource bounds

Protocol/source/schema/constructor pins were frozen before new candidate sessions. Six automatic baselines are exact saved Classical P outputs. H03 is a new first-party analytic vector illustration, rendered to a raster and processed with unchanged classical extraction/P; its source SVG enters evaluation only, never tools or prompts. It is a previously unoptimized synthetic holdout, not proof of real-world unseen-image generalization. Shield/Burger/Arabic/Logo/K01/Astronaut cover the other required categories. No image-specific engine thresholds/templates/geometry are used.

A = saved automatic P. B = non-AI full-frame candidate controller. M = non-AI fixed recorded top-half/bottom-half ROI plan. B and M each use12 calls, at most2commits and2candidate IDs per edit,144paths/4096cubics. The engine schema has a general4-ID ceiling, but both comparison controllers and the optional live-host schema enforce the matched2-ID limit. C = real Groq-guided control, NOT_TESTED. A's zero extra actions is contextual baseline; any B-versus-A gain is not evidence of AI value. C must beat B under matched operation budgets to support the AI hypothesis.

Candidate queries prioritize eligible>=6px traces, then fixed source-gradient/closure/local-support rank. Short ineligible traces cannot hide usable candidates, but the inherited6px construction limit still blocks them. Mean-RGB gradient can miss isoluminant color edges and score lighting/texture highly. No semantic structural precision follows from this confidence.

Each edit stages a separate snapshot; numerical source fitting and duplicate/new-crossing/complexity checks precede commit. Rollback restores previous committed geometry exactly and does not replenish budgets. Every rejection also consumes calls. Existing raw crossings remain uncertain; inherited-validity is not retrospectively certified. Numerical flattening/deviation checks are not continuous exact-arithmetic proofs.

Budgets: CPU-only, one thread;20s cooperative staging,30s trusted-render timeout,300s worker,768MiB sampled process-tree cap,700MiB available-RAM reserve,3600s study limit and150MiB public artifact target. No global installation or model download.

## Per-image actual results

Source recall is proximity to frozen trace evidence at1.25px, NOT semantic structural precision; retaining a reflection can improve it. B/M are not AI. All geometry gates remain NOT_ACCEPTED.

|Case|A source recall|B source recall|M source recall|Paths A/B/M|Atomic faces A/B/M|
|---|---:|---:|---:|---|---|
|A01_shield|0.5459|0.5500|0.5501|128/132/132|0/0/0|
|A03_burger|0.1841|0.1860|0.1860|128/132/132|18/18/18|
|G06_arabic|1.0000|1.0000|1.0000|8/8/8|7/7/7|
|A10_logo|0.7876|0.7929|0.7928|128/132/132|12/12/12|
|K01_linear_corner_hole|1.0000|1.0000|1.0000|3/3/3|3/3/3|
|H02_astronaut|0.1951|0.1960|0.1960|128/132/132|1/1/1|
|H03_original_vector|1.0000|1.0000|1.0000|5/5/5|5/5/5|

Shield uncertain crown-guide recall A0.3036/B0.3082/M0.3201. The central ornament fold remains0.7703 and upper/lower band support0.2141/0.6134; crown tips and material separation are still incomplete. Guide uncertainty is1.2–2px, without independently human-certified1px contours. More source proximity is not complete crown correspondence.

Burger receives four added strokes per controller but constituent boundaries, fillings/lettuce/cheese and seeds are not completed. Logo and Astronaut similarly receive small additions rather than complete regions; physical edges versus texture/lighting remain ambiguous. Arabic proxy recall stays0.9730, K01 known-boundary recall0.9994, and H03 analytic boundary recall0.9975. These boundary numbers do not establish true Arabic font outlines, semantic counters or filled-region ownership. K01's reference foreground excludes an intended interior decoration, limiting full-artwork precision interpretation.

All21 measured outputs have zero measured proper-cross/overlap pairs, but this numerical screen is not a certified topology proof. New B/M paths total32; independent257-point Bernstein samples per cubic found maximum curve-to-raw displacement0.515955px. That audit is one-sided sampled corroboration; the inherited fitter supplies its own bidirectional numerical gate. No threshold was relaxed. Microgeometry remains: short-cubic length fraction generally increases slightly after additions, and actual16x views show staircases. No raster embedding, rectangle mosaic or source-grid fallback was introduced; that alone is not professional vector acceptance.

## Replay, negative results and independent QA

All seven M sessions replay to identical geometry and semantic-decision hashes. Per-run event hashes can differ because observational fitter/render times differ; timings are excluded from deterministic decision identity. Failed/rejected/no-op states and their ledgers remain explicit. All168 B/M calls preserve the original P prefix, have no unresolved pending transaction and respect the common call/commit/complexity limits.

Packaged tests:12 engine,10 provider and6 planner-loop controls. Independent QA adds seven adversarial/parser tests and separate saved-output audits. They cover strict closed schemas, finite bounds/huge integers, unknown tool/path/code injection, transactions, rollback without budget refund, duplicates, loops/corners/junctions, real rendering, hash-chain integrity/replay, safe provider errors, no unauthorized network/env access, duplicate JSON keys and matched live-host IDs. Source/reference separation and real SVG path controls were independently inspected. See `qa/FINAL_QA.md`; passing infrastructure does not accept reconstructed artwork.

Burger's first worker was stopped by the existing available-RAM safety gate. Its complete partial attempt remains `results/A03_burger_attempt01_STOPPED_RAM`. After system available RAM recovered to1955MiB, one identical-code/input/budget retry completed; no resource threshold was weakened. Failed attempt and retry telemetry remain separate. This was not hidden as an uninterrupted pass.

Primary workers including the stopped attempt took93.231s summed monitored wall; retry13.983s. Maximum sampled tree RSS across these sessions212.652MiB. Evaluation/rendering separately completed in45.645s at sampled tree peak210.055MiB. Monitor includes descendants/renderer processes; summed RSS can double-count shared pages and sampling misses transient peaks. The same pinned monitor was previously validated with descendant allocation/limit-stop controls.

## Groq model and live prerequisites

Official Groq [vision documentation](https://console.groq.com/docs/vision) and [model page](https://console.groq.com/docs/model/qwen/qwen3.8-27b) list `qwen/qwen3.8-27b` with image input and tool use. Images count2048 input tokens each, at most3 per request. [Local tool calling](https://console.groq.com/docs/tool-use/local-tool-calling) uses model-proposed functions executed by this application. The geometry engine remains provider-neutral; no xAI integration is used.

The [published free-plan table](https://console.groq.com/docs/rate-limits) lists30RPM,1000RPD,8000TPM,200000TPD for this model, while explicitly directing exact account limits to the organization console. **Account model access, remaining quota, free-plan billing status and no-charge guarantee remain NOT_VERIFIED.** Public documentation, a successful API request, an API-key prefix or remaining-token headers cannot establish those billing facts. No account inference request was made to guess.

`GROQ_API_KEY` is read only by live transport after all gates. The credential pasted in chat was never used, copied or recorded; it should be revoked and replaced locally. No new credential should be posted in chat. Live opt-in requires explicit `--live`, a trusted recent owner-console evidence record confirming free model access/no charges/remaining quota, approved image hashes and bounded request/iteration/token budgets. Neither model output nor images can enable these conditions. Defaults are dry-run. No built-in browser/code/remote tools, arbitrary host URLs, redirects or automatic retry are enabled.

Conservative limits: at most4requests overall,2percase,512completion tokens/request,7500reserved tokens/request,16000total,61s spacing,2MB request bytes, at most3images/request, allowed costUSD0. Input reservations use a conservative text-byte bound plus published image tokens, not an exact tokenizer. If a schema/context cannot fit, the adapter stops rather than raising limits. Usage is validated after responses. Zero cost is conditional on externally verified free-only access, not magically enforced by a token estimate on a paid account.

The optional pilot loop passes source/current-geometry contact sheets plus source-only candidate summaries; it processes validated function proposals locally, commits only safe stages, renders actual output, and sends action outcomes, mandatory diagnostics and a current preview into the next turn. It follows assistant/tool-result message identities. No evaluator guides/masks are sent. Invalid stages cannot undo a prior valid commit accidentally. All live outputs remain untested; transport fixtures are clearly labeled tests.

**Proposed first live pilot, pending owner verification:** Burger only, two requests/iterations, common12-tool-call/2commit/2-ID budget, at most16000reserved tokens and1024completion tokens overall; USD0maximum, free-only. Transmissions would be local contact-sheet PNGs containing the published Burger source and current boundary geometry, plus candidate IDs/diagnostics—not repository files or secrets. The first dry-run preview is recorded by hash under `results/A03_burger/C_dry_run`. A changed second preview has an unknown hash until the first edit; the current gate intentionally rejects it unless separately authorized. A trusted derived-preview approval/resume workflow must be established before claiming unattended two-turn live readiness. No silent allowlist expansion occurs.

Privacy: image pixels and geometry diagnostics would leave the laptop for GroqCloud. [Groq data policies](https://console.groq.com/docs/your-data) must be reviewed for the selected account; this is not local/private inference. Owner rights and provider-transmission permission must cover the exact source and previews. Fine Features/private Arena assets are excluded. Account proof stays outside Git and is never sent to the provider.

## Engineering judgment and next decision

The hypothesis is technically plausible: a vision planner could prioritize meaningful source-supported contours and reject illumination fragments while deterministic tools provide precision. Recognition is not geometry, however. Current tools cannot recover structure absent from their trace pool or form missing source-supported junctions; no planner can overcome that by merely describing a crown.

Keep network-aware diagnostics as a core capability, and evaluate source-supported network assembly as an independent future tool. Do not throw away the prior evidence that per-trace eligibility destroys closure. Do not simultaneously change the detector/geometry engine and claim that a better planner caused the result.

**GO:** preserve this offline tool infrastructure and, only after account/quota/image/derived-preview gates are independently satisfied, authorize a matched zero-charge pilot against B. **NO-GO:** claim AI improvement now, promote a production architecture, start appearance, or promise universal reconstruction. If live prerequisites cannot be established, stop with AI NOT_TESTED. Current evidence does not justify replacing the engine. A later richer toolset (network assembly/refinement/region edits) requires its own bounded controls and owner decision.

## Publication and reproduction

New work is isolated in `EXP_AI_GUIDED_GEOMETRY_01`. One scoped Git staging attempt failed on `.git/index.lock: Permission denied`; no ACL/security bypass or repeated denied write. New work is uncommitted/unpublished. `Publish-Research.ps1` checks main/origin, staged scope, fetch/ancestry, commits only if needed, pushes normally and verifies remote SHA. Run it in the owner terminal. No API keys, model weights, environments or private account records belong in Git.

The seven candidate sessions are complete: do not rerun them. Source pins/decisions and actualSVG/PNG evidence permit independent replay in a separate empty workspace. `run_sessions.py` refuses existing output folders. `groq_pilot.py` defaults to dry-run and also refuses an existing session directory. Original candidate code/schema pins remain immutable; the optional provider-loop implementation/tests and evaluation/dashboard code were finalized after offline construction and are recorded separately. No new AI performance measurement results from those infrastructure tests.


## Final implementation closure

The optional host explicitly paces requests with at most61seconds of bounded waiting in<=30second chunks and no transport retry; a frozen-clock control cannot extend this budget. Provider-loop tool replies, matched2-ID arguments, invalid-stage rollback safety and sanitized request-status records pass six loop tests. Total packaged tests28; seven independent tests are separate. A final dry-run session used the final wrapper, made zero requests and is preserved as `C_dry_run_final_validation`. Original candidate code/schema pins remain unchanged; post-construction wrapper/evaluator/replay sources are separately inventoried. H03 is explicitly labeled a newly constructed automatic holdout control.


## Governance and publication closure

Scoped provenance/mirrors pass with100 indexed symbols and no duplicate function names. Repository-wide root governance still FAILS on global/historical provenance registry drift; full diagnostic is preserved in `reports/ROOT_GOVERNANCE.txt`. No historical or global registry was rewritten. The scoped publisher passed its read-only `-CheckOnly` validation; no new commit or upload is claimed. Starting/ending verified remote is46870cbf109454dfd243a7bffab692a692bc2b52, with only this experiment uncommitted. Final independentQA, exact artifact inventory and hashes accompany this report. Stop for owner review before any live inference or new production milestone.
