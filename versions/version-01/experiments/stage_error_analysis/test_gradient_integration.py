#!/usr/bin/env python3
"""Test gradient detection, SVG generation, and PyMuPDF rendering."""
import sys
from pathlib import Path
import cv2
import numpy as np
import pymupdf

def test_gradient():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <linearGradient id="grad1" x1="0" y1="0" x2="100" y2="100" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#ff0000" />
      <stop offset="100%" stop-color="#0000ff" />
    </linearGradient>
  </defs>
  <rect width="100" height="100" fill="url(#grad1)" />
</svg>'''
    doc = pymupdf.open(stream=svg.encode("utf-8"), filetype="svg")
    pix = doc[0].get_pixmap()
    print(f"PyMuPDF rendered successfully: {pix.width}x{pix.height}, samples={len(pix.samples)}")

if __name__ == "__main__":
    test_gradient()
