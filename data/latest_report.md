# GitHub New Releases Report 2026-10-22

**[astral-sh/uv 0.13.5](https://github.com/astral-sh/uv/releases/tag/0.13.5)**

### Summary
uv 0.13.5 provides critical security updates addressing compromised eMudhra root certificates across standalone CPython builds and internal certificate chains. This release also introduces preview support for PEP 850 wheel variants alongside notable memory and resolution performance optimizations.

### Highlights
- **eMudhra Security Hardening**: Mitigates compromised eMudhra keys by updating standalone CPython builds (3.13.17+, 3.14.9+, 3.15.1+) to include patched `pip` and `certifi` bundles, while actively rejecting compromised chains via `rustls-webpki`.
- **Resolution & Export Performance**: Lowers peak memory consumption during multi-environment dependency resolutions and accelerates lockfile exports containing complex transitive extras.
- **PEP 850 Wheel Variants (Preview)**: Adds preview support for selecting and ranking platform-specific wheel variants based on PEP 850 static providers.

### Breaking Changes
- **Discontinued Docker Images**: Official uv Docker images for Python 3.9 and 3.10 are no longer published due to unpatched upstream certificate vulnerabilities in those EOL versions.
- **Strict Build Cache Keys**: Invalid custom build cache keys are now explicitly rejected with an error instead of silently falling back to default keys.
- **Action Required for Existing Environments**: Run `uv python upgrade` to fetch patched CPython builds. Existing virtual environments pinned to older patch versions will not update automatically; upgrade `pip` manually inside them.
---
**[duckdb/duckdb v2.0.0](https://github.com/duckdb/duckdb/releases/tag/v2.0.0)**

### Summary
DuckDB v2.0.0 ("Cyanoptera") marks a major milestone featuring extensive architectural upgrades across execution, storage, and file formats. This release introduces widespread asynchronous I/O, advanced optimizations for semi-structured `VARIANT` types, native nested schema support, and completely removes external ICU dependencies for timezones.

### Highlights
* **End-to-End Asynchronous I/O**: Massive I/O engine rework introducing asynchronous I/O and prefetching for Parquet reads/writes, the CSV reader, and native DuckDB table scans.
* **Optimized `VARIANT` & Semi-Structured Support**: Substantially improved JSON/Variant pipelines with shredded vector processing, direct pushdown, and `VariantIterator` traversal without requiring costly full unshredding.
* **ICU Removal & Engine Modernization**: Built-in, high-performance calendar and timezone handling replaces the external ICU dependency, paired with an upgraded optimizer featuring CTE-based duplicate elimination and aggregate reuse.

### Breaking Changes
⚠️ **Breaking Changes & Behavioral Updates:**
* **Integer Division by Zero**: Division by zero now throws a runtime error instead of silently returning `NULL`.
* **C++ and C API Adjustments**: Core classes including `Value` and `LogicalType` are now immutable, and SQL identifier handling transitioned from raw strings to dedicated `Identifier` types. C-API V2 has also begun rollout.
* **Julia Client Removal**: The in-tree Julia client has been deprecated and extracted to the standalone `duckdb/DuckDB.jl` repository.
* **Regex Semantics**: Regular expression operators have been aligned to strictly follow PostgreSQL behavior.