# GitHub New Releases Report 2026-07-22

**[astral-sh/uv 0.11.31](https://github.com/astral-sh/uv/releases/tag/0.11.31)**

### Summary
`uv` version 0.11.31 introduces support for cross-workspace path references and new configuration options for security malware audits. This release also delivers resolution performance optimizations for transitive conflicts alongside several key bug fixes.

### Highlights
- **Cross-Workspace Path References**: Allows workspace sources to reference members located in another workspace directly by path ([#18401](https://github.com/astral-sh/uv/pull/18401)).
- **Malware Audit Configuration**: Added `audit.malware-check` and `audit.malware-check-url` settings to support automated package security checks ([#20587](https://github.com/astral-sh/uv/pull/20587)).
- **Transitive Conflict Performance**: Fixed quadratic time complexity when deduplicating transitive dependency conflicts, improving resolution speeds ([#20578](https://github.com/astral-sh/uv/pull/20578)).

### Breaking Changes
None.
---
**[pola-rs/polars py-1.43.0](https://github.com/pola-rs/polars/releases/tag/py-1.43.0)**

## Polars py-1.43.0 Release Summary

### Summary
Polars `py-1.43.0` introduces major query engine optimizations for Hive-partitioned scans and joins, along with algorithmic performance upgrades like O(n) rolling min/max operations. This release also continues API stabilization by deprecating legacy methods and implicit type coercions in favor of stricter, safer defaults.

### Highlights
- **Hive & Query Engine Optimizations**: Added pre-partitioning on Hive keys for joins and group-bys, optimized Hive inner joins into filtered partition unions, and tightened filter constraint propagation.
- **New Features & Expressions**: Introduced `ewm_sum` / `ewm_sum_by`, a consolidated `list` packing expression, `scan_arrow_c_stream`, and explicit `Series.degrees()` / `Series.radians()` helpers.
- **Memory & Streaming Upgrades**: Added `POLARS_OOC_DISK_BUDGET_MB` for out-of-core processing, removed excess memory copies in the streaming IPC sink, and implemented an O(n) monotonic deque for rolling calculations.

### Breaking Changes & Deprecations
⚠️ **Deprecations Introduced** (no immediate hard breaks, but action required):
- **Type Casts**: Deprecated casting numeric types to Categorical, as well as non-nested dtypes directly to Lists.
- **Categoricals**: Deprecated `cat.get_categories()` and `cat.to_local()` (use `Expr.cat.to()` and `Expr.cat.physical()`).
- **Bitwise & Struct Ops**: Deprecated bitwise operations between integers and booleans, and calling `.to_struct()` without explicit field names.
- **LazyFrame & Configuration**: Deprecated `LazyFrame.profile()`. Renamed parameter `missing_utf8_is_empty_string` to `empty_string_is_null`.