<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-30T15:21:31Z", "last_action": "CREATED", "last_change_id": "AGD-CODEX-WIN-PORT", "last_edited_at_utc": "2026-10-30T15:21:31Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-30T15:21:31Z"}
END_DOC_PROVENANCE -->
<!-- DOC_PROVENANCE {"created_at_utc":"2026-10-30T08:41:02Z","last_edited_at_utc":"2026-10-30T08:41:02Z","tracking_started_at_utc":"2026-10-30T08:41:02Z","last_action":"CREATED","last_change_id":"AGD-LOSS-CONTOUR-PARTITION","last_editor":"contour_partition"} -->
# Source-only partition fitter API

`partition_fit.fit_trace(points, periodic=False, deadline=None, maximum_trace_cubics=512)` receives only a finite Nx2 frozen source polyline. A truly closed trace repeats its initial point at the end. `deadline` is an absolute monotonic wall time supplied by the arm runner.

The module imports the unchanged historical `stable_fit.fit`, `measure`, and `flatten`. Put the previous experiment and numerical dependencies on PYTHONPATH; do not duplicate these functions. No image, detector confidence, reference, case identity or semantic template enters construction.

P (`periodic=False`) and Q (`True`) have identical source-index partitions. Cuts use .35px RDP support turning, 60degree intentional corners, 35degree accumulated turning, and a maximum32px original arc budget. Raw raster staircase turns are not automatically independent semantic corners. A source edge longer than32px is explicitly rejected rather than inventing evidence. Each raw edge has one ledger owner, using `[lo,hi)` edge intervals and `[lo,hi]` point slices.

Each partition uses the unchanged stable fitter: maximum64 cubics, eight subdivision rounds and .6px bidirectional numerical upper envelope. Original trace cap512 cubics. Q only changes genuine closed traces: smooth partition joins receive matching source-derived tangent directions with shared bounded handle magnitude, including the seam. Sharp source/RDP corners retain independent handles. Every partition is remeasured afterward; failed periodic adjustments are rejected, never silently substituted by P output.

Return `chains` contains ordered contiguous accepted cubic runs, with exact endpoints, `closed` and constituent `partition_ids`. Partial loops remain explicitly open. A complete loop is closed only if all intervals survive and its nonzero source area retains winding. Nested loops retain individual orientation; they do not establish hole ownership or filled regions. `ledger` records every partition and reason, including budget/time limits. Aggregate lengths and edge-accounting error quantify loss.

`periodic_joins` records proposed joins, preserved corners, unavailable partitions, both-partitions-retained status and measured retained tangent angles. Part-level numerical predicates reject selfcrossing introduced into simple source intervals and crossings inconsistent with previously accepted source intervals. These flattened predicates are not exact arithmetic certification. Parent must separately audit cross-original-trace conflicts, global budget, deduplication and candidate/reference integrity. Any parent rejection must update its own loss ledger rather than silently dropping curves.

Run `work\agd-native\Scripts\python.exe work\contour_construction\implementation\run_tests.py` from the session cwd. Nine source-only synthetic tests cover closure/C1, corners, longtraces, opposite-winding nested loops, source-junction endpoints, budget/time loss accounting, duplicates and shorttrace policy. No benchmark matrix was executed by this module's author.
