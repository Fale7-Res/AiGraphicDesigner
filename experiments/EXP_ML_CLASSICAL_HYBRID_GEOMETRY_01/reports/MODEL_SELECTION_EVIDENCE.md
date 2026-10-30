<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-30T08:21:42Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-30T08:21:42Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-30T08:21:42Z"}
END_DOC_PROVENANCE -->
# CPU-first model-selection evidence

Audit date: 2026-10-30. Author: ml_model_audit. This audit downloaded no weights, installed no packages, and made no repository changes. Owner vision and previous NEXT_MILESTONE_ML.md were read completely. Geometry remains NOT_ACCEPTED; production architecture remains NOT_APPROVED.

## Recommendation and bounded decision

Select the published OpenCV DexiNed ONNX as the primary learned-edge candidate. It is small enough for a supervised CPU smoke test and does not require installing PyTorch. Select SAM2.1 Hiera Tiny only as a separately budgeted region-proposal candidate; no claim of native Windows feasibility is established yet. TEED is a credible lightweight fallback if DexiNed exceeds budget, but adds checkpoint/implementation work and provides the same evidence category rather than a different region baseline.

Neither model produces complete SVG geometry. Save pre-fit predictions and compare discovery independently of the common curve fitter. No known evidence establishes better crown completeness or Arabic topology for any candidate.

## DexiNed artifact identity and rights

- Publisher: OpenCV model mirror, referencing Xavier Soria's upstream DexiNed.
- Model: `edge_detection_dexined_2024sep.onnx`.
- Frozen HF revision: `01a752eb4006688376e576dc24941c54608f6dd0`.
- Exact bytes: `47235563`; SHA256: `a50d01dc8481549c7dedb9eb3e0123b810a016520df75e4669a504609982cdd0`.
- [Pinned artifact](https://huggingface.co/opencv/edge_detection_dexined/blob/01a752eb4006688376e576dc24941c54608f6dd0/edge_detection_dexined_2024sep.onnx).
- [OpenCV Git LFS pointer](https://raw.githubusercontent.com/opencv/opencv_zoo/main/models/edge_detection_dexined/edge_detection_dexined_2024sep.onnx) independently identifies those bytes.
- [Model card](https://huggingface.co/opencv/edge_detection_dexined/blob/main/README.md) explicitly applies MIT to all files in this model directory. [License](https://huggingface.co/opencv/edge_detection_dexined/blob/main/LICENSE) credits Xavier Soria Poma. Retain notice. This is an explicit publisher statement about the model directory, stronger evidence than assuming the framework license covers a checkpoint.

The [upstream wrapper](https://raw.githubusercontent.com/opencv/opencv_zoo/main/models/edge_detection_dexined/dexined.py) uses BGR, 512x512 resizing, scale 1 and mean (103.5,116.2,123.6). It produces sigmoid maps and then independently normalizes each prediction before resizing. Preserve logits/sigmoid before display normalization; per-image normalization changes the meaning of a common confidence threshold. Freeze selection of fused versus averaged output before evaluation. The wrapper's default uses the fused output. Direct 512-square resizing distorts aspect ratios; use the documented transform consistently and map coordinates back explicitly.

The current README specifies OpenCV>=5, while the wrapper uses basic ONNX/DNN operations. OpenCV4.13 compatibility is therefore NOT_ESTABLISHED, rather than disproven. Test the pinned model with the isolated existing version first. Do not upgrade the baseline merely to satisfy a broad README requirement. Suggested isolated package pin if necessary: `opencv-python-headless==4.13.0.92`; [PyPI metadata](https://pypi.org/pypi/opencv-python-headless/4.13.0.92/json) identifies CPU wheels. Use only one cv2 wheel family. Pin actual resolved NumPy and other packages in the environment manifest, rather than treating this recommendation as a tested lockfile.

Expected purpose: learned boundary confidence. Limitations: no region identities, no structure/lighting guarantee, unknown domain transfer to metallic artwork/Arabic. A broad edge halo can improve tolerance-based recall while worsening true localization; measure edge thickness and precision separately.

## SAM2.1 Hiera Tiny artifact identity and rights

- Official [SAM2 repository](https://github.com/facebookresearch/sam2), [installation](https://github.com/facebookresearch/sam2/blob/main/INSTALL.md), and [model card](https://huggingface.co/facebook/sam2.1-hiera-tiny).
- Official release checkpoint: `https://dl.fbaipublicfiles.com/segment_anything_2/092824/sam2.1_hiera_tiny.pt`.
- HF frozen revision: `de431c4043854a71d8101e17995dfe596bf101a5`.
- Alternate official HF `model.safetensors`, about156MB; SHA256 `48c14467e5cf9e51870511feb72c89688e82dd74523142c0538b663e193ac2a7`, from [artifact details](https://huggingface.co/facebook/sam2.1-hiera-tiny/blob/main/model.safetensors).
- The HF card declares Apache2.0. Upstream README separately explicitly licenses SAM2 checkpoints Apache2.0. Keep its [Apache license](https://github.com/facebookresearch/sam2/blob/main/LICENSE). Optional cctorch has a separate BSD notice; demo fonts have separate terms, irrelevant if no demo/font assets are used.

Upstream lists38.9M parameters. Published91.2FPS is measured on A100, not this laptop. Native Windows CPU latency and peak working memory remain unmeasured. The38.9M float32 parameter floor is approximately156MB, not total inference RAM.

[Setup](https://github.com/facebookresearch/sam2/blob/main/setup.py) requires Python>=3.10, torch>=2.5.1 and torchvision>=0.20.1, plus Hydra/iopath/Pillow/NumPy/tqdm. CPU-compatible APIs take `device="cpu"`; CUDA build can be omitted using `SAM2_BUILD_CUDA=0`. The omitted optional extension removes small-hole/sprinkle postprocessing; disclose this because holes matter here. WSL is recommended upstream, but installing WSL/system CUDA is outside this experiment's intended minimal environment intervention.

Two safe implementation choices must remain distinct:

1. Pinned official SAM2 code + official state dict, explicit `torch.load(...,weights_only=True,map_location="cpu")`, no remote checkpoint code, `device="cpu"`, float32, no CUDA autocast, no compile. Freeze the exact Git commit before downloading. The current Git code SHA was not established in this audit.
2. Official HF safetensors + pinned Transformers native SAM2 implementation, `trust_remote_code=False`, `use_safetensors=True`, CPU only. This avoids pickle; it is a separate implementation and conversion, not automatically equivalent to the original code. [Transformers SAM2 documentation](https://huggingface.co/docs/transformers/model_doc/sam2) supports this path.

Compatibility proposal for the original-code route: Python3.11 isolated environment, torch2.6.0 CPU + torchvision0.21.0 from the official [matched-version installation table](https://pytorch.org/get-started/previous-versions/). These satisfy upstream minima. They are a compatibility proposal, not a current security guarantee or tested installation. Prefer a newer already-validated CPU pair when available; do not silently resolve unbounded versions. Pin Hydra1.3.2 and iopath0.1.10; record all final transitive versions and wheel hashes after installation. No training dependencies or notebook extras are necessary for image-only inference.

Freeze an automatic prompt grid (for example4x4 at normalized cell centers) with batch1 and no crop expansion; all sixteen prompts are source-independent, not evaluator annotations. Keep all resulting candidate masks and predicted scores; do not select the best mask against truth. Small crown components may receive no suitable prompt. This is a limited automatic proposal test, not proof of mask completeness. Default official automatic mask generation can be far more expensive and should not be used accidentally.

## Lightweight fallback: TEED

[Official TEED](https://github.com/xavysp/TEED) describes a58K-parameter learned edge detector. [Root license](https://github.com/xavysp/TEED/blob/main/LICENSE) is MIT, and an [official checkpoint tree](https://github.com/xavysp/TEED/tree/main/checkpoints/BIPED) exists. No checkpoint revision/hash or checkpoint-specific scope beyond repository MIT was resolved in this audit. Resolve before download. Do not substitute third-party ControlNet/preprocessor bundles and assume identical rights. Tiny parameter count does not prove CPU latency or better fine-feature detection. Prefer it only as a fallback, rather than expanding the model catalogue.

## Resource protocol proposed before inference

These are conservative stop limits, not measured model requirements. Run sequentially, two CPU inference threads, no GPU, record available RAM immediately before launch. Require at least6GiB free physical RAM and retain2GiB operating-system headroom. Supervisor samples process-tree working set every0.25s and records sample interval; sampled maximum is not an exact allocation peak.

| Work | Wall limit | Process-tree working-set stop | Other bound |
|---|---:|---:|---|
| DexiNed load+one smoke image | 120s | 3GiB | batch1,512x512 |
| DexiNed per image after load | 90s | 3GiB | one fused field |
| SAM2 load+first image embedding | 240s | 4GiB | one image, float32 |
| SAM2 per image proposals | 240s | 4GiB |16 fixed prompts,batch1,no crops |
| Any installation | 15min | no inference concurrently |2GiB download ceiling; no CUDA wheels |

If the supervisor is unavailable, do not claim an enforced memory cap. On a timeout or memory stop preserve the log and SKIPPED_RESOURCE/FAILED_RESOURCE status, do not repeatedly lower input resolution until a result looks successful. Test SAM2 only after the edge candidate is operational. A prior environment review found MX1302GiB; this audit did not repeat or independently verify current hardware. All VRAM inference should remain zero by configuration and be measured where tooling permits.

## Integrity and interpretation

Use immutable revision URLs and verify downloaded bytes before loading; keep weights and environments outside Git. Download requests contain no benchmark images. Disable hosted inference and telemetry where controllable. Preserve notices and plain metadata, not credentials. Fixed sources and withheld evaluator references must never be used to choose inference prompts or confidence thresholds. Do not use a Crown crop specified by evaluator-only detail guides to drive model inference.

Classical, learned and hybrid confidence maps are not calibrated on the same scale. A hybrid intersection can improve apparent precision merely by deleting difficult features; union can improve apparent recall merely by adding shading edges. Freeze the fusion rule and report both precision and recall, critical components, and pre-/post-fit stages separately. Learned edges/regions cannot independently settle whether a metallic transition is material geometry or lighting; uncertain guides remain uncertain.

<!-- DOC_PROVENANCE {"created_at_utc":"2026-10-30T07:56:42Z","last_edited_at_utc":"2026-10-30T07:56:42Z","last_action":"CREATED","last_change_id":"AGD-ML-MODEL-AUDIT-01","last_editor":"ml_model_audit"} -->
