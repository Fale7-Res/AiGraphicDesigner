<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-18T08:28:11Z", "last_action": "EDITED", "last_change_id": "TASK-UPDATE-SYS-DEFECTS-02", "last_edited_at_utc": "2026-10-19T02:55:41Z", "last_editor": "orchestrator-planner", "tracking_started_at_utc": "2026-10-18T08:28:11Z"}
END_DOC_PROVENANCE -->
# Shared Baseline Evidence & LF Normalization Report (`AGD_SHARED_BASELINE_EVIDENCE`)

**Date:** 2026-10-19T02:50:00Z  
**Baseline Identifier:** `BASE_REVIEW_SHARED_20261018_V01`  
**Status:** `BASELINE_SHARED_EVIDENCE`  
**Global Architecture Status:** `NOT_APPROVED` (`PROPOSED_FOR_OWNER_REVIEW`)

---

## 1. Technical Explanation of the Hash Discrepancy (CRLF vs. Canonical LF)

During the previous baseline establishment, an apparent discrepancy was observed between the physical disk hash and the canonical in-memory serialization hash:
- **Physical Disk File (CRLF):** 221,716 bytes, SHA-256 `42c3413ca19d899a1dfc08abdc2a0bf276d31cd54c24f9c597a39630f9ccae42`.
- **In-Memory Canonical LF Serialization:** 217,320 bytes, SHA-256 `e2e97edb4b686224c09e1716ebd9c5a0afdecb40f510e3df8d99e9fb001d37ef`.

### Root Cause Analysis:
1. Python's `pathlib.Path.write_text(..., encoding='utf-8')` on Windows automatically performs newline translation, replacing Unix line feeds (`\n`) with Windows carriage return + line feeds (`\r\n`).
2. The inventory JSON contains exactly 4,396 lines. The insertion of 4,396 `\r` (0x0D) bytes expanded the file from 217,320 bytes to 221,716 bytes:
   $$\Delta = 221,716 - 217,320 = 4,396 \text{ bytes}$$
3. Because SHA-256 operates on raw binary streams, the added `\r` bytes altered the file digest from `e2e97edb...` to `42c3413c...`.

### Permanent Normalization Applied:
1. `tools/update_packages/state_manager.py` was refactored: all baseline files and registry state files are now written strictly via binary streams using `Path.write_bytes(inventory.to_json().encode("utf-8"))`.
2. `BASE_REVIEW_SHARED_20261018_V01.json` was re-saved to disk using canonical LF bytes.
3. **Verified Result:**
   - Physical File Size on Disk: **217,320 bytes** (exact match).
   - Physical Disk SHA-256: `e2e97edb4b686224c09e1716ebd9c5a0afdecb40f510e3df8d99e9fb001d37ef` (exact match).

---

## 2. Provenance of `BASE_REVIEW_SHARED_20261018_V01`

`BASE_REVIEW_SHARED_20261018_V01` represents the audited 626-file shared scope:
- **617 files** delivered and independently verified from `AGD_UPDATE_0005_20261018T023644Z.zip`.
- **9 files** explicitly excluded from UPDATE_0005 (large raster assets, benchmark datasets, and PNG renderings) which were recovered with identical SHA-256 hashes from prior archives.
- **Sorted File Digest (`sorted_files_sha256`):** `cb01296fa875dd444f9695f90af2112720ee0889ad46a5ed74d2c48c425adea2`.
- **Canonical Inventory Serialization Digest (`inventory_json_sha256`):** `e2e97edb4b686224c09e1716ebd9c5a0afdecb40f510e3df8d99e9fb001d37ef`.

---

## 3. Governance Acknowledgment Clarification

The field `acknowledged_by="Owner/Auditor"` in `tools/update_packages/registry/update_state.json` is strictly an internal operational tracking note for the update system's local state machine.
- It denotes that the recipient/auditor has acknowledged receipt of the baseline inventory structure.
- **It does NOT constitute official owner approval or acceptance.** Official owner acceptance is strictly reserved for authenticated governance directives and explicit records in `memory/decisions/` and `docs/product/`.

---

## 4. Archive Contents

This archive (`AGD_SHARED_BASELINE_EVIDENCE_20261018T081500Z.zip`) contains:
1. `tools/update_packages/registry/baselines/BASE_REVIEW_SHARED_20261018_V01.json` (canonical LF, 217,320 bytes, SHA-256 `e2e97edb...`).
2. `tools/update_packages/registry/update_state.json` (current update system state).
3. `README_METADATA_EVIDENCE.md` (this explanatory document).
