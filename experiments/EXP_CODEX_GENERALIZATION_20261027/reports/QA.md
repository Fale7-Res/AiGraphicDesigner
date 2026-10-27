<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-27T14:48:24Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-27T14:48:24Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-27T14:48:24Z"}
END_DOC_PROVENANCE -->
# Saved generalization evidence QA

Executed 2026-10-27T14:48:22+00:00. This is packaging-author verification, not independent parent approval or owner visual acceptance. Architecture remains **NOT_APPROVED**.

Command, from the experiment directory:

```text
C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work\agd-native\Scripts\python.exe -B -m unittest test_saved_evidence -v
```

Final run: **6 tests passed in 44.448 seconds**, exit 0. The prior pre-import-cleanup run also passed six tests in 31.124 seconds. The final run used the deduplicated digest helper imported from `acquire_dataset.py`; that module's acquisition `main` was not invoked.

1. Frozen source/original/manifest hashes, eight cases, seven originals, 140 successful candidate pairs, no recorded failed candidate.
2. All eight inherited and selected SVG/PNG aliases byte-identical; no improvement claim.
3. Three selected RGBA cases reproduce exact tested-dimension alpha; no claim for all nonwinning candidates or arbitrary dimensions.
4. Independent saved winning metric recomputation on the prepared sRGB reference, including ICC-normalized Rocket; 213 SVGs parsed without embedded raster/external href/script/foreign-object content and 553 PNGs fully decoded.
5. Entire saved inputs/dataset/results inventory unchanged by packaging and matching saved digest inventory.
6. Every generated comparison PNG fully decoded; dashboard contains every case.

Visually inspected the Rocket white sheet and dice black sheet through the image tool. Captions and all four columns are legible, sources/renders align, and amplified residuals remain visible. PNG worst-tile enlargement is explicitly described as a raster diagnostic. The dashboard embeds actual saved SVGs and offers 1x/4x/16x browser display, but interactive browser operation and independent-renderer equivalence were not certified by this packaging task.

Scoped governance reused the existing isolated Windows governance loader with its ROOT redirected in a private module. It indexed four first-party Python files / 21 symbols, found zero duplicate functions, and document provenance/source-stamp verification passed. Root governance's preexisting blockers are outside this scope and were not repaired or concealed. No saved input, source snapshot, result, runner, historical implementation, or owner vision was modified.
