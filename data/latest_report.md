# GitHub New Releases Report 2026-08-25

**[pola-rs/polars py-1.44.0](https://github.com/pola-rs/polars/releases/tag/py-1.44.0)**

### Summary
Polars `py-1.44.0` delivers significant performance optimizations across the query engine alongside major enhancements to Apache Iceberg and SQL capabilities. This release also lays the groundwork for the upcoming 2.0 milestone by introducing deprecation notices for chunking APIs and struct operations.

### Highlights
* **Deeper Apache Iceberg Integration**: Expanded native `scan_iceberg` support to handle schema evolution, V3 deletion vectors, snapshot properties, and direct object storage paths.
* **SQL & Optimizer Improvements**: Added CTE caching in the SQL layer, support for correlated `IN` subqueries, and optimized `when/then/otherwise` evaluation by masking out unevaluated branches.
* **Cloud I/O & Struct Enhancements**: Introduced an adaptive HTTP rate-limiter for resilient cloud reads, native integer fixed-array dot products, and the new `struct.drop()` expression.

### Breaking Changes
**No immediate breaking changes**, but several deprecations have been introduced ahead of the 2.0 release:
* The `rechunk` parameter is now deprecated across all `read_*` and `scan_*` functions.
* `Expr.rechunk()` is deprecated.
* Passing an incorrect number of fields to `struct.rename_fields()` is now deprecated (use the new `struct.drop()` for field removal).