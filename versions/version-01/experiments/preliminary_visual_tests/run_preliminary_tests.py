#!/usr/bin/env python3
"""Run preliminary visual tests on the 12 initial images using Version 01 baseline pipeline.

Executes local color quantization, contour extraction, and Bézier vectorization.
Records telemetry (latency, paths, nodes, file sizes) and exports SVG files.
"""
from pathlib import Path
import json
import sys
import time

# START CHANGE TASK-PRELIM-VIS-01 | 2026-10-17T10:10:00Z | CREATED | Author: orchestrator-planner
HERE = Path(__file__).resolve().parent
EXPERIMENTS_DIR = HERE.parent
VERSION_ROOT = EXPERIMENTS_DIR.parent
PROJECT_ROOT = HERE.parents[3]

sys.path.insert(0, str(VERSION_ROOT))
from src.pipeline import SequentialPipeline

INPUT_DIR = PROJECT_ROOT / "AI_Graphic_Designer_Test_Images_Initial_12"
OUTPUT_DIR = HERE / "outputs"


def run_preliminary_tests() -> dict:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    pipeline = SequentialPipeline(error_tolerance_px=2.0, max_nodes_per_path=36)

    manifest_path = INPUT_DIR / "DATASET_MANIFEST.json"
    images_meta = {}
    if manifest_path.exists():
        with open(manifest_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
            for item in meta.get("images", []):
                images_meta[item["file"]] = item

    results: list[dict] = []
    print("=" * 80)
    print("STARTING PRELIMINARY VISUAL TESTS — VERSION 01 SEQUENTIAL BASELINE")
    print("=" * 80)

    for img_file in sorted(INPUT_DIR.glob("*.png")):
        meta_info = images_meta.get(img_file.name, {})
        img_id = meta_info.get("id", img_file.stem)
        difficulty = meta_info.get("difficulty", "unknown")

        print(f"\nProcessing [{img_id}] {img_file.name} (Tier: {difficulty})...")
        svg_content, telemetry = pipeline.process_image(
            image_path=img_file,
            n_colors=6,
            min_contour_area=16.0,
        )

        out_svg_path = OUTPUT_DIR / f"{img_id}_v01_vector.svg"
        with open(out_svg_path, "w", encoding="utf-8") as f:
            f.write(svg_content)

        res_entry = {
            "id": img_id,
            "filename": img_file.name,
            "difficulty": difficulty,
            "dimensions": telemetry["dimensions"],
            "clusters_count": telemetry["clusters_count"],
            "total_layers": telemetry["total_layers"],
            "total_paths": telemetry["total_paths"],
            "total_nodes": telemetry["total_nodes"],
            "elapsed_ms": telemetry["elapsed_ms"],
            "svg_size_bytes": telemetry["svg_size_bytes"],
            "svg_path": str(out_svg_path.relative_to(PROJECT_ROOT)),
        }
        results.append(res_entry)
        print(f"  -> Generated {telemetry['total_paths']} paths, {telemetry['total_nodes']} nodes, "
              f"{telemetry['svg_size_bytes']} bytes in {telemetry['elapsed_ms']} ms")

    summary_payload = {
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "version_id": "version-01",
        "pipeline_strategy": "Sequential Monolith (K-Means RGB/LAB + Schneider Bézier)",
        "test_status": "COMPLETED_PRELIMINARY_TESTS",
        "total_images_tested": len(results),
        "results": results,
    }

    summary_file = HERE / "results_summary.json"
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(summary_payload, f, indent=2)

    print("\n" + "=" * 80)
    print(f"ALL 12 PRELIMINARY TESTS COMPLETED! Summary saved to {summary_file}")
    print("=" * 80)
    return summary_payload


if __name__ == "__main__":
    run_preliminary_tests()
# END CHANGE TASK-PRELIM-VIS-01 | 2026-10-17T10:10:00Z | CREATED
