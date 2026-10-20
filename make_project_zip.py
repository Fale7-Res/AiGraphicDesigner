#!/usr/bin/env python3
"""Full-repository archiver for AI Graphic Designer."""
# START CHANGE P0-ARCH-REVIEW-ENV | 2026-10-17T07:41:00Z | EDITED | Author: orchestrator-planner
import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
from pathlib import Path
# END CHANGE P0-ARCH-REVIEW-ENV | 2026-10-17T07:41:00Z | EDITED
from zipfile import ZIP_DEFLATED, ZipFile

SOURCE_DIR = Path(__file__).resolve().parent
OUTPUT_ZIP = SOURCE_DIR / "ai_graphic_designer_project.zip"
EXCLUDED_DIRS = {".git", "node_modules", "__pycache__", ".venv"}


def build_archive() -> Path:
    """Create a clean ZIP archive of all project files."""
    with ZipFile(OUTPUT_ZIP, "w", compression=ZIP_DEFLATED) as archive:
        for file_path in sorted(SOURCE_DIR.rglob("*")):
            if not file_path.is_file():
                continue
            if file_path.resolve() == OUTPUT_ZIP.resolve():
                continue
            if any(part in EXCLUDED_DIRS for part in file_path.relative_to(SOURCE_DIR).parts[:-1]):
                continue
            archive.write(file_path, file_path.relative_to(SOURCE_DIR))
    print(f"تم إنشاء الأرشيف بنجاح: {OUTPUT_ZIP}")
    return OUTPUT_ZIP


if __name__ == "__main__":
    build_archive()
