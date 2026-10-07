# GitHub New Releases Report 2026-10-07

**[pola-rs/polars py-2.0.0](https://github.com/pola-rs/polars/releases/tag/py-2.0.0)**

### Summary
Polars `py-2.0.0` marks a major milestone featuring the official release of Python Polars 2.0 with out-of-core (OOC) processing enabled by default at an 80% RAM threshold. This release introduces significant performance gains across the streaming engine, expanded SQL capabilities, and faster cloud I/O.

### Highlights
- **Default Out-of-Core (OOC) Processing**: OOC execution is now enabled by default with an 80% RAM threshold and a 64 GB disk budget, complemented by a new streaming out-of-core sort.
- **SQL Frontend Expansion**: Added support for advanced SQL analytics including `GROUP BY GROUPING SETS`, `ROLLUP`, `CUBE`, `QUALIFY`, and new window functions (`PERCENT_RANK`, `CUME_DIST`, `NTILE`).
- **Engine & I/O Optimizations**: Major throughput boosts across Parquet/IPC out-of-order scans, improved Iceberg/Lance pushdowns, vectorized decimal math, and optimized join/group-by hash tables.

### Breaking Changes
⚠️ **Breaking changes are present in this release:**
- **SQL Behavior**: Exact SQL numeric literals are now typed as `Decimal`, and SQL `%`/`DIV` operations now truncate. `QUALIFY` now evaluates before projection, and SQL window functions over grouped rows evaluate on the aggregated rows.
- **Parquet Enums**: Parquet `ENUM` logical types are now read as `pl.String`.
- **API Deprecations**: `cut` and `qcut` have been deprecated in favor of binning functions.
- **Plugin CSE/CSPE**: Expression plugins must now explicitly opt in to Common Subexpression Elimination.
---
**[unionai-oss/pandera v0.34.1](https://github.com/unionai-oss/pandera/releases/tag/v0.34.1)**

### Summary
Pandera v0.34.1 lays foundational groundwork with an architectural specification for a generic, dataframe-agnostic schema API. Additionally, this release highlights recent ecosystem expansions by announcing PyTorch TensorDict support across documentation banners.

### Highlights
* **Dataframe-Agnostic Schema Spec**: Introduced an initial specification for a unified, backend-agnostic schema API to improve consistency across different dataframe implementations ([#2401](https://github.com/unionai-oss/pandera/pull/2401)).
* **PyTorch TensorDict Documentation**: Added announcements across docs banners showcasing Pandera's validation capabilities for PyTorch `TensorDict` structures ([#2544](https://github.com/unionai-oss/pandera/pull/2544)).

### Breaking Changes
* None. This release contains non-breaking specification and documentation updates.