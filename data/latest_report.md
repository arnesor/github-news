# GitHub New Releases Report 2026-07-23

**[duckdb/duckdb v1.5.5](https://github.com/duckdb/duckdb/releases/tag/v1.5.5)**

## Summary
DuckDB v1.5.5 is a patch release focused on critical bug fixes, memory safety, and engine stability following the v1.5.4 release. It addresses several out-of-bounds read vulnerabilities, resolves concurrency deadlocks, and bumps core extensions including HTTPFS, Iceberg, and ADBC.

## Highlights
* **Security & Memory Safety**: Fixed multiple out-of-bounds read vulnerabilities across JSON path lookahead, dictionary string decompression, string-to-struct casts, and decimal handling.
* **Concurrency & Memory Fixes**: Resolved a deadlock in `TemporaryMemoryManager`, fixed a segfault in external hash aggregation when radix bits grow, and resolved crashes during concurrent `ALTER` and `INSERT` operations.
* **Ecosystem & ADBC Updates**: Introduced support for the `duckdb://` URI scheme and ADBC Statistics API, alongside version updates for PostgreSQL, HTTPFS, Iceberg, and Lance extensions.

## Breaking Changes
None. This is a backward-compatible bug fix patch release.
---
**[dynaconf/dynaconf 3.3.3](https://github.com/dynaconf/dynaconf/releases/tag/3.3.3)**

## Dynaconf 3.3.3 Release Overview

### Summary
Dynaconf 3.3.3 is a patch release focused on resolving a regression in lazy evaluation when box behavior is disabled. It also introduces documentation improvements for configuration validation and streamlines internal deployment workflows.

### Highlights
- **Lazy Evaluation Fix:** Resolved a regression affecting lazy evaluation when `dynaboxify=False` (#1429).
- **Docs Clarification:** Improved documentation surrounding `True`, `False`, and `None` handling for `must_exist` checks (#1416).
- **CI/CD Enhancements:** Consolidated and simplified documentation publishing and backport branch workflows on CI (#1415, #1417, #1420).

### Breaking Changes
None.
---
**[pandas-dev/pandas v3.0.5](https://github.com/pandas-dev/pandas/releases/tag/v3.0.5)**

## Pandas v3.0.5 Release Analysis

### Summary
Pandas 3.0.5 is a patch release in the 3.0.x series focused on delivering critical regression and bug fixes. The maintainers recommend that all users currently running Pandas 3.0.x upgrade to this version to ensure optimal stability.

### Highlights
- **Regression Fixes**: Addresses unexpected regressions introduced in earlier 3.0.x releases.
- **Bug Fixes**: Resolves various community-reported bugs to improve overall core functionality.
- **Python 3.11+ Requirement**: Continues seamless support for modern Python runtimes (Python 3.11 and higher).

### Breaking Changes
No breaking changes are present in this patch release.