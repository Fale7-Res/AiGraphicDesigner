<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-29T12:39:52Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-29T12:39:52Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-29T12:39:52Z"}
END_DOC_PROVENANCE -->
# Independent implementation review before candidate results

Reviewed face_cycles.py, run_case.py and test_face_cycles.py. Independently executed all five abstract tests through an isolated path-configured wrapper; all passed (0.002 s test body; approximately 2.04 s process). First direct unittest launch failed import because it lacked work/geometry-deps; this was an invocation failure, not a constructor failure. run_tests.py records the successful environment.

## Confirmed implementation contracts

- Constructor accepts saved graph only, no source pixels, evaluator geometry, case identifier or annotations.
- Deep copies preserve caller input; face-loop partition is the only changed field. Directed occurrence Counters include multiplicity and direction. Assertion compares all chain and other metadata fields exactly.
- Each endpoint walk must close exactly. Splits cut at the first repeated starting endpoint and preserve the subwalk order. Empty, open and over-budget walks reject to the original without deleting them.
- Per-original-walk signed area conservation is checked before accepting its pieces. Zero-area output pieces are retained and flagged, not pruned.
- Candidate worker validates frozen hashes/pins, refuses existing output directory, copies original labels/B and newly renders O/R. Exact native/8x raw and8x fitted RGBA equality gates the unchanged B guard. Any rejection or pixel mismatch blocks RB. All conditions/negative evidence remain available.
- Abstract tests cover pinched disconnected loops, reversed occurrence, open walk rejection, zero-area retention and budget failure. They do not establish geometric reconstruction correctness.

## Limits / cautions

At initial review the constructor did not explicitly detect repeated internal-chain vertices. Such vertices are not present in the four frozen baselines according to independent audit, so the controlled comparison is not affected. Its general API should not be advertised as resolving those configurations. Root was notified before execution.

The underlying geometry_eval.svg_graph exporter and renderer are inherited shared dependencies, not independent analytic SVG parsers. Exact comparison O/R still valid for the controlled premise; final QA must inspect actual SVG markup and decoded renders. Directed occurrence preservation independently proves evenodd parity, but not correct original segmentation or physical topology.

Changed face decomposition alters group incidence/targets passed into B. Accepted chains and original-to-new mapping must be shown. This is a controlled representation-mediated guard test, not a claim that initialization alone repairs missing semantic artwork.

No current code review finding requires relaxing the frozen gate. Proceed to bounded execution; final outcome not yet reviewed. Geometry NOT_ACCEPTED; architecture NOT_APPROVED.
