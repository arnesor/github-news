# GitHub New Releases Report 2026-11-21

**[duckdb/duckdb v2.0.1](https://github.com/duckdb/duckdb/releases/tag/v2.0.1)**

### Summary
DuckDB v2.0.1 is a patch release addressing several bugs, stability issues, and ecosystem integration rough edges identified following the major v2.0.0 milestone. It delivers vital correctness fixes across the query planner and Parquet reader while stabilizing core extensions across WebAssembly and Windows environments.

### Highlights
* **Query Engine & Optimizer Corrections**: Fixes row-mapping preservation in runtime filters, improves candidate retention in greedy join ordering, and corrects evaluation semantics for `ANY` and `ALL` operations against `ARRAY(SELECT ...)` subqueries.
* **Parquet & Type Casting Enhancements**: Adds the `parquet_can_have_nan` configuration option, preserves min/max column statistics for NULL-only row groups in Parquet files, and introduces casts from `TIMESTAMPTZ_NS` to `TIMESTAMP`.
* **Extension & Cloud Storage Improvements**: Bumps and stabilizes key extensions (AWS, Iceberg, Glue, Azure, and DuckLake), expands Glue autoloading and Wasm support, and hardens safe mode by redacting secret `refresh_info`.

### Breaking Changes
None. This is a backwards-compatible patch release dedicated to bug fixes, extension updates, and platform stability.