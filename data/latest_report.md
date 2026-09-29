# GitHub New Releases Report 2026-09-29

**[astral-sh/uv 0.12.20](https://github.com/astral-sh/uv/releases/tag/0.12.20)**

### Summary
uv 0.12.20 delivers targeted stability and performance improvements, notably mitigating severe cache-revalidation stalls on ext4 filesystems and resolving several resolver and CLI panics. It also improves lockfile handling by reusing lockfiles when dependency declarations are semantically equivalent and expands preview support for `pylock.toml`.

### Highlights
- **HTTP Cache Stall Mitigation**: Restores previous cache-write scheduling to eliminate severe cache-revalidation stalls observed on ext4 filesystems.
- **Semantic Lockfile Reuse**: Skips unnecessary re-locking by recognizing semantically equivalent dependency declarations.
- **Robustness & Panic Fixes**: Addresses multiple crash/panic conditions across managed Python detection, resolver trace logging, and non-ASCII whitespace requirements, while adding state restoration for interrupted `uv upgrade` calls.

### Breaking Changes
None. This is a backwards-compatible patch release.
---
**[duckdb/duckdb v1.5.6](https://github.com/duckdb/duckdb/releases/tag/v1.5.6)**

### Summary
DuckDB v1.5.6 is a comprehensive patch release focusing on query optimizer reliability, storage engine hardening, and ecosystem compatibility. It resolves multiple critical edge cases across window functions, WAL recovery, and Parquet data serialization.

### Highlights
* **Query Optimizer & Top-N Window Stability**: Delivers extensive fixes to `TopNWindowElimination`—including handling of `LIMIT 0`, nullable ordering expressions, and join projection mapping—alongside pushdown fixes for `UNNEST` and volatile projections.
* **Storage Engine & Transaction Hardening**: Hardens temporary file reads, resolves a file locking issue during WAL recovery, prevents duplicate emitted chunks in caching operators, and backports the `enable_optimistic_write` setting.
* **Data Type & Parser Correctness**: Prevents silent truncation of oversized integer literals into `HUGEINT`, corrects Parquet `TIME_NS` read/writes, and fixes state leakage across rows in ICU `strptime`.

### Breaking Changes
* **Julia Client Deprecation**: The bundled in-tree Julia client has been removed from the core repository in favor of the standalone package at [`duckdb/DuckDB.jl`](https://github.com/duckdb/DuckDB.jl). Standard SQL interfaces and core storage formats remain backward-compatible.