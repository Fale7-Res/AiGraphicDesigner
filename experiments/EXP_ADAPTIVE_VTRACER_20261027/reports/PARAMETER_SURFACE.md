<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-27T09:01:44Z", "last_action": "CREATED", "last_change_id": "ADAPTIVE-DELIVERY", "last_edited_at_utc": "2026-10-27T09:01:44Z", "last_editor": "root", "tracking_started_at_utc": "2026-10-27T09:01:44Z"}
END_DOC_PROVENANCE -->
# Installed VTracer parameter surface

Test target: Python VTracer **1.0.0a4**, native **1.0.0-alpha.4**. Exact source snapshot: immutable sibling `EXP_VTRACER_FIDELITY_20261024/reference/vtracer_1.0.0-alpha.4/`, especially `crates/vtracer/src/config.rs.txt` and `crates/vtracer-py/src/lib.rs.txt`. Upstream https://github.com/visioncortex/vtracer, MIT OR Apache-2.0. A prerelease version string alone does not establish byte-identical upstream master source.

| Python parameter | Meaning / applicability | Bounded search coverage |
|---|---|---|
| clustering | color-cluster, watershed, bw | All three families |
| hierarchical | stacked painter order or cutout shared-boundary mosaic; all families | Both |
| mode | pixel lattice polylines, polygon simplified lines, spline cubics | All three overall, not every cross-product |
| filter_speckle | Side length squared gives minimum area | 0 pilots, 1/2 neighbors |
| color_precision | Significant RGB bits 1..8; Color frontend | 8 pilots, 7/6 neighbors |
| layer_difference | Color gradient-layer tolerance; Binary cutout merge tolerance also | Color0/1 pilots, 1/2/8/0 neighbors; Binary cutout retained |
| corner_threshold | Spline corner angle degrees | 60;45 neighbor |
| length_threshold | Spline segment length pixels | 4;2 neighbor |
| max_iterations | Least-squares refinement per spline segment | 10;20 neighbor |
| splice_threshold | Spline splice angle degrees | 45;30 neighbor |
| simplify | Additional spline refit tolerance px; None disables; inactive pixel/polygon | 1.5/None pilots; .25/.75 neighbors |
| path_precision | Output coordinate decimals, also quantization | 0/3 pilots;5/1 neighbors |
| palette | Fixed palette, overrides max_colors | Supported, not searched |
| max_colors | Automatic palette size | Supported, not searched |
| optimize | 0off,1quantize+cleanup,2also shorthands/grouping | 1 pilots,0 neighbor;2 not searched |
| binary_threshold | Fixed grayscale cutoff0..255; ignored if adaptive | 128 pilot,96/160/192 neighbors |
| adaptive | Bradley–Roth local threshold | Fixed and adaptive pilots |
| adaptive_window | Localwindow side;0auto about1/8 shorter image side | 0pilot,15/31neighbors |
| adaptive_t | Percentage below local mean | 15pilot,5/25neighbors |
| watershed_detail | Hierarchy cut, higher keeps more regions, uncapped above255 | 128/256/512pilots, doubling/halving bounded at2048 |

Gradient Step maps to layer_difference; it does not emit SVG gradients. Pixel mode preserves pixel-grid geometry, not clean scalable curves. Watershed cutout uses upstream merge tolerance `max((255-detail)/8,2)`: detail512 still has a merging floor2. Stacked remains a distinct eligible alternative. Binary cutout uses layer_difference even though its frontend ignores Color precision. A missing Binary cutout layer_difference uses upstream default16 rather than owner0.

The table describes the available domain and candidate generator, not proof all neighbors ran. Default budget24 includes13pilots; two globally stagnant rounds can stop before late curve/precision/speckle controls. Actual config.json files are authoritative executed settings. No universal or exhaustive optimum is claimed. Alpha-preserving SVG, semantic layers and editable typography are not implemented.
