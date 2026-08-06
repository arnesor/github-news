# GitHub New Releases Report 2026-08-06

**[astral-sh/uv 0.12.2](https://github.com/astral-sh/uv/releases/tag/0.12.2)**

### Summary
uv version 0.12.2 introduces performance optimizations for `uv.lock` parsing and file metadata handling alongside support for CPython 3.15.0rc1 and 3.14.7. It also adds preview features like tool vulnerability auditing and new configuration options for execution file limits.

### Highlights
- **Tool Security Auditing (Preview):** Audit single or all installed CLI tools for vulnerabilities using `uv tool audit`.
- **Lockfile & Build Performance:** Significantly faster parsing of wheel/sdist entries in `uv.lock` and reduced filesystem metadata lookups during compilation and builds.
- **Execution File Limits:** Set custom open-file descriptors limit for commands executed via `uv run` using `UV_RUN_RLIMIT_NOFILE`.

### Breaking Changes
None.
---
**[dynaconf/dynaconf 3.3.5](https://github.com/dynaconf/dynaconf/releases/tag/3.3.5)**

### Dynaconf 3.3.5 Release Summary

**Summary**
Dynaconf 3.3.5 is a patch release focused on improving stability by resolving core issues in key casing, configuration precedence, and history tracking. Additionally, it updates the test matrix to add initial support for Python 3.14.

**Highlights**
* **Dotted Key Persistence Fix:** Resolved an issue where calling `get` or `get_fresh` with dotted keys stopped working after the initial call (#1423).
* **Override Precedence Restoration:** Fixed a regression regarding override precedence by ensuring proper cleanup of dynaconf tokens (#1438).
* **DataDict Deepcopy Support:** Added `__deepcopy__` implementation to `DataDict` for consistency with `DataList` (#1440).

**Breaking Changes**
None. This is a fully backward-compatible patch release.
---
**[pola-rs/polars rs-0.55.1](https://github.com/pola-rs/polars/releases/tag/rs-0.55.1)**

### Summary
Polars `rs-0.55.1` brings significant query engine performance optimizations, enhanced Hive partitioning support, and initial out-of-core (OOC) spilling capabilities. Matching Python DSL 1.43.2, this release also delivers dozens of memory-safety, SQL compatibility, and join/slicing bug fixes.

### Highlights
- **Hive Partitioning & Cloud IO Optimizations**: Introduced pre-partitioned joins on Hive-partitioned datasets and byte-based concurrency control for cloud IO operations.
- **Out-of-Core (OOC) Spilling**: Added experimental out-of-core memory spilling support controlled via `POLARS_OOC_DISK_BUDGET_MB` to manage workloads larger than system RAM.
- **New Expression Features**: Added `struct.drop()`, a unified `list` expression for packing elements, and `Series.degrees()` / `radians()` trig helpers.

### Breaking Changes
⚠️ **No hard breaking API changes**, but several deprecations and strict enforcement updates were introduced:
- **Deprecations**: Direct casts from string to temporal dtypes, numeric/categorical cross-casts, and `.explode()` calls without specifying `empty_as_null`.
- **Behavior Changes**: Decimal sums now raise a `ComputeError` on overflow instead of silently wrapping values.