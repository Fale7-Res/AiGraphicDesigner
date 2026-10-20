#!/usr/bin/env python3
import runpy
from pathlib import Path

target = Path(__file__).resolve().parents[3] / "tools" / "memory_guard" / Path(__file__).name
runpy.run_path(str(target), run_name="__main__")
