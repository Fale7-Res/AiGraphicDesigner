<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-27T09:01:44Z", "last_action": "CREATED", "last_change_id": "ADAPTIVE-DELIVERY", "last_edited_at_utc": "2026-10-27T09:01:44Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-27T09:01:44Z"}
END_DOC_PROVENANCE -->
# Adaptive VTracer fidelity research

Architecture remains **NOT_APPROVED**. This isolated extension reuses the frozen evaluator in sibling `EXP_VTRACER_FIDELITY_20261024` at repository commit `4ba5ed56df11001b0e3050383883e7107003751a`. No historical file is replaced.

## Install and run

Extract into your AiGraphicDesigner project root. The archive adds `experiments/EXP_ADAPTIVE_VTRACER_20261027/`; if this directory exists, extract to a separate review folder instead of overwriting.

```bash
python -m pip install -r experiments/EXP_ADAPTIVE_VTRACER_20261027/requirements.txt
# Install Inkscape and ensure inkscape is on PATH (measured version1.2.2).
python -m unittest discover -s experiments/EXP_ADAPTIVE_VTRACER_20261027 -p 'test_*.py'
python experiments/EXP_ADAPTIVE_VTRACER_20261027/optimizer.py --input YOUR_IMAGE.png --output NEW_EMPTY_FOLDER --max-candidates 24 --max-seconds 720
python experiments/EXP_ADAPTIVE_VTRACER_20261027/review.py NEW_EMPTY_FOLDER
```

Open `NEW_EMPTY_FOLDER/review.html` for top-five actual SVG renders, configuration/metrics, opacity slider and SVGlinks. Delivered suite comparisons start at `index.html`. This is reusable CLI/review tooling, not a deployed upload service or approved architecture.

To repeat the suite without overwriting evidence, copy the source files and unseen/ into a new sibling experiment directory alongside the old VTracer experiment, run `benchmark.py --workers 2`, then `review.py`. Complete rankings are reused; interrupted nonempty directories are refused. Preserve interrupted results before retrying in a fresh destination.

## Search and evaluation contract

13 diverse pilots cover Color/Watershed/Binary and all fitting families, then family-leader coordinate probes. Default maximum24 candidates,720second dispatch budget; stop after2 globally stagnant rounds below1e-5 improvement. A current worker may add up to180seconds. This is bounded search, not exhaustive optimality; late probes can be unexecuted. The owner preset is first. All actual candidates, failures and duplicate-rejection history are retained.

Ranking reuses the historical score unchanged: .40SSIM + .15min(PSNR/60,1) + .20edgeF1 + .15exp(-meanDeltaE76/12) + .10exp(-highpassRMSE/20), with no complexity penalty. Highest score need not mean highest SSIM or human preference. Local residuals and visual review remain necessary. Pertrial JSON includes full pathcommands/controlcoordinates/bytes, traceCPU/wall, render time and separate worker/renderer peakmemory (not simultaneous process-tree RSS).

Default rejects nonopaque inputs. `--alpha-policy white` explicitly evaluates appearance composited onwhite, not transparency-preserving SVG. Singleframe dimensions>=7 only. ICC→sRGB uses frozen Pillow conversion; untaggedRGB assumedsRGB. Native dimensions retained. ArbitraryICC/HDR/16bit/animation/nativeWindows/hugeinput support is not certified.

Pixel geometry is acceptable for current fidelity research and reported honestly. Dense paths are not semantic layers or professional cleanvector. No embeddedrasters, rasterfilters, learnedmodel or paidAPI. VTracer1.0.0a4 is prerelease, pinned, MIT ORApache-2.0. Upgrading requires a fresh parameter/render audit. Realtransferdata attribution is in unseen/manifest.json.

## Recovery coverage

Workspace maintenance deleted prior uncommitted adaptive work before delivery. This directory reconstructs the missing implementation and runs fresh evidence. Earlier adaptive measurements quoted in conversation are not used as current evidence. The previously committed October25 VTracer research remains the historical baseline.
