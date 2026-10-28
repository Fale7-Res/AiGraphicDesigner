# START CHANGE AGD-BOTTLENECK-ORACLE | 2026-10-28T03:38:01Z | EDITED | Author: root (original implementation: appearance_fit)
"""Known-source-geometry oracle; inherited fitter and reconstruction evidence immutable."""
from pathlib import Path
import argparse
import copy
import hashlib
import importlib.util
import json
import os
import shutil
import sys
import time
import xml.etree.ElementTree as ET

import numpy as np
from PIL import Image, ImageDraw

SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)
CASES = ("K01_linear_corner_hole", "K02_radial_shared_curves")


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_historical(repo):
    prior = Path(repo) / "experiments/EXP_GEOMETRY_APPEARANCE_ABLATION_01"
    sys.path.insert(0, str(prior))
    spec = importlib.util.spec_from_file_location("oracle_historical_run", prior / "run_experiment.py")
    run = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(run)
    from fit_appearance import fit_svg
    return prior, run, fit_svg


def flat_initialization(source, destination):
    """Remove original gradient paint only, preserving source geometry and solid paint."""
    root = ET.parse(source).getroot()
    replaced = []
    for parent in root.iter():
        for child in list(parent):
            if child.tag in (f"{{{SVG}}}linearGradient", f"{{{SVG}}}radialGradient"):
                parent.remove(child)
    for i, path in enumerate(root.iter(f"{{{SVG}}}path")):
        if path.get("fill", "").startswith("url("):
            replaced.append(i)
            path.set("fill", "#777777")
    for child in list(root):
        if child.tag == f"{{{SVG}}}defs" and not list(child):
            root.remove(child)
    ET.ElementTree(root).write(destination, encoding="utf-8", xml_declaration=True)
    return replaced


def _write_json(path, data):
    Path(path).write_text(json.dumps(data, indent=2, allow_nan=False), encoding="utf-8")



def gradient_metadata(root):
    return [{"type": node.tag.rsplit("}", 1)[-1], "attributes": dict(node.attrib), "stops": [dict(stop.attrib) for stop in node]} for node in root.iter() if node.tag in (f"{{{SVG}}}linearGradient", f"{{{SVG}}}radialGradient")]

def finish_diagnostics(repo, output):
    """Read-only fit analysis and actual vector-render visual/ground-truth checks."""
    prior, evaluate, _ = load_historical(repo)
    output = Path(output)
    for name in CASES:
        folder = output / name
        record = json.loads((folder / "result.json").read_text())
        truth = ET.parse(folder / "oracle_truth.svg").getroot()
        fitted = ET.parse(folder / "oracle_D.svg").getroot()
        fallback = [region for region in record["fitting"]["regions"] if "reason" in region]
        representability = {"known_original_gradients": gradient_metadata(truth), "fitted_gradients": gradient_metadata(fitted), "fallback_regions": fallback, "all_regions_refitted_from_samples": not fallback, "known_solid_paint_initialization": "Original solids retained only in initialization; all output regions refitted from source pixels when no fallback is reported", "restriction": "K01 original nonuniform middle offset0.45 is excluded by equally spaced stops at the same endpoints; fitted endpoints also constrained to sample projection extent. K02 original radius101 is independent, while inherited fitter forces radius=max distance to visible interior samples. Center/focal and stop positions are further restricted. These facts show family mismatch, not a proof of globally optimal fitting or a quantitative error decomposition.", "oracle_label": "Known source metadata is diagnostic privileged information, not recovered parameters or a deployable fitter"}
        record["representability"] = representability
        # This is a new actual SVG render check, separate from earlier hash reuse.
        record["conditions"]["oracle_truth"] = evaluate.evaluate_condition(folder / "source.png", folder / "oracle_truth.svg", folder / "oracle_truth")
        assert record["conditions"]["oracle_truth"]["metrics"]["white"]["mse"] == 0
        record["ground_truth_reuse"]["fresh_native_svg_check_mse"] = 0.0
        record["ground_truth_reuse"]["fresh_native_svg_check_performed"] = True
        width, height = Image.open(folder / "source.png").size
        box = (max(0, width//2-12), max(0, height//2-12), 24, 24)
        for scale in (1, 4, 16):
            sheet = Image.new("RGB", (24 * scale * 4, 24 * scale + 24), "#20242b")
            draw = ImageDraw.Draw(sheet)
            cases = [("truth", folder / "oracle_truth.svg"), ("reconstructedD", folder / "reconstructed_D/output.svg"), ("oracleC", folder / "oracle_C.svg"), ("oracleD", folder / "oracle_D.svg")]
            for i, (label, svg) in enumerate(cases):
                viewport = folder / f"center_{label}_{scale}x.svg"
                evaluate.crop_svg(svg, viewport, box, scale)
                sheet.paste(Image.open(viewport.with_suffix(".png")).convert("RGB"), (i * 24 * scale, 24))
                draw.text((i * 24 * scale + 2, 4), label, fill="white")
            sheet.save(folder / f"center_{scale}x.png")
        _write_json(folder / "result.json", record)
    return {"diagnostics_finished": True}


def run_oracle(repo, output):
    prior, evaluate, fit_svg = load_historical(repo)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    records = []
    for name in CASES:
        folder = output / name
        if folder.exists() and any(folder.iterdir()):
            raise FileExistsError(f"Preserve previous oracle evidence: {folder}")
        folder.mkdir(exist_ok=True)
        source_svg, source_png = prior / "inputs" / f"{name}.svg", prior / "inputs" / f"{name}.png"
        manifest = json.loads((prior / "inputs/manifest.json").read_text())
        frozen = next(c for c in manifest["cases"] if c["id"] == name)
        assert digest(source_svg) == frozen["ground_truth_svg_sha256"]
        assert digest(source_png) == frozen["source_sha256"]
        shutil.copyfile(source_svg, folder / "oracle_truth.svg")
        shutil.copyfile(source_png, folder / "source.png")
        replaced = flat_initialization(source_svg, folder / "oracle_init.svg")
        t = time.perf_counter()
        fitting = fit_svg(source_png, folder / "oracle_init.svg", folder / "oracle_C.svg", folder / "oracle_D.svg", folder / "fitting.json", deadline_seconds=120)
        fitted_wall = time.perf_counter() - t
        assert evaluate.geometry_signature(source_svg) == evaluate.geometry_signature(folder / "oracle_init.svg")
        assert evaluate.geometry_signature(folder / "oracle_C.svg") == evaluate.geometry_signature(folder / "oracle_D.svg")
        assert evaluate.geometry_signature(source_svg) == evaluate.geometry_signature(folder / "oracle_D.svg")
        conditions = {}
        for condition in ("oracle_init", "oracle_C", "oracle_D"):
            conditions[condition] = evaluate.evaluate_condition(source_png, folder / f"{condition}.svg", folder / condition)
        previous = json.loads((prior / "results" / name / "result.json").read_text())
        reused = {}
        for condition in "ABCD":
            old = prior / "results" / name / condition
            reused[condition] = {"source_svg": str(old / "output.svg"), "sha256": digest(old / "output.svg"), "metrics": previous["conditions"][condition]}
            assert reused[condition]["sha256"] == previous["conditions"][condition]["sha256"]
            target = folder / f"reconstructed_{condition}"
            target.mkdir()
            for asset in ("output.svg", "render.png", "white.png", "black.png", "bluegray.png"):
                shutil.copyfile(old / asset, target / asset)
        width, height = Image.open(source_png).size
        canvas = Image.new("RGB", (width * 5, height + 24), "#20242b")
        draw = ImageDraw.Draw(canvas)
        columns = [("Truth source geometry+paint", source_png), ("Reconstructed D (saved)", folder / "reconstructed_D/white.png"), ("Oracle flat C", folder / "oracle_C/white.png"), ("Oracle gradient D", folder / "oracle_D/white.png")]
        error = np.clip(np.abs(np.asarray(Image.open(source_png).convert("RGB"), dtype=float) - np.asarray(Image.open(folder / "oracle_D/white.png"), dtype=float)) * 8, 0, 255).astype(np.uint8)
        for i, (label, path) in enumerate(columns):
            draw.text((i * width + 3, 4), label, fill="white")
            canvas.paste(Image.open(path).convert("RGB"), (i * width, 24))
        draw.text((width * 4 + 3, 4), "Oracle D error x8", fill="white")
        canvas.paste(Image.fromarray(error), (width * 4, 24))
        canvas.save(folder / "comparison.png")
        report = {"case": name, "ground_truth_reuse": {"svg_sha256": digest(source_svg), "saved_native_render_sha256": digest(source_png), "source_matches_frozen_manifest": True, "rerendered": False, "native_reference_mse": 0.0}, "replaced_gradient_path_indices": replaced, "ground_truth_geometry_signature": evaluate.geometry_signature(source_svg), "oracle_geometry_signature": evaluate.geometry_signature(folder / "oracle_D.svg"), "fitting_wall_seconds": fitted_wall, "conditions": conditions, "reused_reconstruction": reused, "fitting": fitting, "interpretation_scope": "Analytic controls only. Exact known geometry isolates appearance capacity/optimization; no natural-image geometry reconstruction or generalization claim.", "architecture": "NOT_APPROVED"}
        _write_json(folder / "result.json", report)
        records.append(report)
        print(name, {k: round(v["metrics"]["white"]["ssim"], 8) for k, v in conditions.items()}, flush=True)
    summary = {"cases": [{"case": r["case"], "oracle_C": r["conditions"]["oracle_C"]["metrics"]["white"], "oracle_D": r["conditions"]["oracle_D"]["metrics"]["white"], "reconstructed_D": r["reused_reconstruction"]["D"]["metrics"]["metrics"]["white"], "fitting_wall_seconds": r["fitting_wall_seconds"]} for r in records], "historical_fitter_sha256": digest(prior / "fit_appearance.py"), "architecture": "NOT_APPROVED"}
    _write_json(output / "summary.json", summary)
    finish_diagnostics(repo, output)
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "results/oracle")
    parser.add_argument("--diagnostics-only", action="store_true")
    args = parser.parse_args()
    (finish_diagnostics if args.diagnostics_only else run_oracle)(args.repository, args.output)
# END CHANGE AGD-BOTTLENECK-ORACLE | 2026-10-28T03:38:01Z | EDITED
