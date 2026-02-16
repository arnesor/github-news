# GitHub New Releases Report 2026-02-16

**[duckdb/duckdb v1.4.4](https://github.com/duckdb/duckdb/releases/tag/v1.4.4)**

DuckDB v1.4.4 is a maintenance release focused on stabilizing the v1.4 "Andium" branch through critical bug fixes and extension updates. This version addresses stability issues in SQL execution, storage reliability, and improves compatibility with external data formats like Parquet and Iceberg.

### Highlights
* **Refined Query Execution:** Resolved several edge cases in complex join types (ASOF SEMI/ANTI, RIGHT SEMI/ANTI) and fixed issues with view resolution stability when referencing tables across different schemas.
* **Updated Extension Ecosystem:** Significant updates to the Iceberg (now with WASM support), Spatial, Excel, VSS, and HTTPFS extensions to ensure better performance and compatibility.
* **Improved Data Safety:** Implemented more robust Parquet reading by ignoring invalid UTF-8 in string statistics instead of throwing errors, and added defensive guards against infinite loops and invalid UTF-8 in the C API.

### Breaking Changes
None. This is a dedicated bugfix release intended to be a drop-in replacement for v1.4.3.
---
@everyone **[ibis-project/ibis 12.0.0](https://github.com/ibis-project/ibis/releases/tag/12.0.0)**

### Summary
Ibis 12.0.0 introduces support for Materialize and SingleStoreDB backends alongside a new `upsert()` API for unified data synchronization. This major release modernizes the library's foundation by dropping support for Python 3.9 and older PySpark versions while significantly enhancing internal type safety.

### Highlights
*   **New Backends:** Support added for **Materialize** (streaming database) and **SingleStoreDB**, expanding the reach of the Ibis expression engine to real-time and distributed workloads.
*   **Upsert Functionality:** A new `upsert()` method implemented via `MERGE INTO` provides a standard way to update existing records or insert new ones across supported backends.
*   **Ecosystem Modernization:** Official compatibility for **Pandas 3.0** and **PySpark 4.0**, ensuring seamless integration with the latest generation of data tools.

### ⚠ Breaking Changes
*   **Python 3.9 Dropped:** Support for Python 3.9 has been officially removed; Python 3.10 or higher is now required.
*   **PySpark Requirements:** PySpark versions prior to 3.5 are no longer supported.
*   **Decimal Inference:** The engine now automatically infers decimal precision and scale, which may alter the schema behavior of existing workflows.
*   **API Refactors:** Several internal classes have been renamed (e.g., `View` to `AliasedRelation`) and certain arguments have moved to positional-only to improve maintainability.

### Key Bug Fixes
*   Fixed `asof_join` predicate handling in Postgres and Polars.
*   Resolved precision loss in SQLite division operations.
*   Improved `first()` and `last()` aggregations by adding `order_by` support.
---
@everyone **[narwhals-dev/narwhals v2.16.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.16.0)**

### Summary
Narwhals v2.16.0 introduces the `narwhals.sql` module and expands cross-backend support for advanced expressions like window functions in filters. This update significantly enhances the developer experience with new testing utilities and broader DType support across various backends.

### Highlights
* **SQL Integration:** The introduction of the `narwhals.sql` module provides a new way to interact with data using SQL syntax across supported backends.
* **Advanced Expressions:** Support has been added for window functions within `filter()` and an optional `order_by` parameter in `first` and `last` expressions.
* **Testing Utilities:** The new `narwhals.testing.assert_frame_equal` utility makes it easier for developers to validate results consistently across different dataframe libraries.

### Breaking Changes
No major breaking changes are reported in this release. Note that the interchange protocol has been removed for non-v1 versions (#3403), and the internal logic for converting `pd.ArrowDtype` to Narwhals DTypes has been simplified.

### Priority
Minor
---
**[numpy/numpy v2.4.2](https://github.com/numpy/numpy/releases/tag/v2.4.2)**

# NumPy 2.4.2 Release Notes Analysis

### Summary
NumPy 2.4.2 is a focused patch release addressing critical stability issues and memory leaks discovered following the 2.4.1 release. This update ensures robust performance for Python versions 3.11 through 3.14, specifically targeting concurrency and library-level bugs.

### Highlights
*   **Memory & Stability Fixes:** Resolves several memory leaks identified through Valgrind and fixes a race condition related to environment variable access.
*   **OpenBLAS Update:** Includes a backported update to OpenBLAS specifically designed to resolve intermittent hangs during computation.
*   **Concurrency Improvements:** Enhances thread safety for `array_getbuffer` and rectifies PyObject layout issues to better support free-threaded Python builds.

### Breaking Changes
None. As a patch release, NumPy 2.4.2 maintains full backward compatibility with the 2.4.x series.