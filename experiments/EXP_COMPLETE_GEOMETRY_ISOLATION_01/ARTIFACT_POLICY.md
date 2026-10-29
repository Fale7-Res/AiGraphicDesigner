<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T06:54:23Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T06:54:23Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T06:54:23Z"}
END_DOC_PROVENANCE -->
# Artifact bytes, size and external rights

Frozen references, metrics and candidate graphs use SHA256 over exact file bytes. The initial freeze commit was made while Git's checkout newline conversion was active: the Shield JSON Git blob used LF, while the frozen working file and recorded hash used CRLF. This was detected during final artifact QA.

The scoped `.gitattributes` now disables newline conversion for this experiment. A normal append-only commit records the original frozen working bytes. **References, annotation coordinates, thresholds and recorded hashes do not change.** No history is rewritten. The initial freeze remains historical evidence; the final checkpoint restores byte-exact cross-platform retrieval.

The research package is approximately112MB uncompressed; the largest file is about4.3MB. No file approaches GitHub's50MiB warning or100MiB block. Git compression/deduplication is retained; no history cleanup or destructive garbage collection is performed.

The fine_features external fixture and its derived artwork are excluded from the public repository because redistribution rights remain unresolved. They are preserved locally with exact file hashes and ZIP retrieval requirements in external/LOCAL_EVIDENCE_MANIFEST.json, and copied into the owner-only local review output. This is an explicit rights limitation, not missing experimental execution. No Arena implementation is copied into the product or repository.

Environments, toolchains, downloaded executable binaries, package caches and Python bytecode are excluded. Source, dependency lockfiles, licenses, tests, evaluator configuration, labels, candidate graphs, SVG/PNG evidence, metrics, failure diagnostics, reports and QA remain in the scoped experiment.
