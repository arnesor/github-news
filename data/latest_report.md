# GitHub New Releases Report 2026-02-24

**[narwhals-dev/narwhals v2.17.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.17.0)**

## Summary
Narwhals v2.17.0 introduces enhanced functionality for `Series.scatter` and improves compatibility with key backends like PySpark and DuckDB. The release also includes critical bug fixes for numeric comparisons and SQL-like operations to ensure consistent behavior across dataframes.

## Highlights
*   **Flexible Scattering:** `Series.scatter` now accepts `Series` objects for both indices and values, enabling more dynamic and idiomatic data updates.
*   **Expanded Numeric Comparisons:** Added `Decimal` data type support to the `is_close` method for both Series and Expressions, broadening precision-based filtering.
*   **Ecosystem Alignment:** Resolved compatibility issues with DuckDB 1.5 (`fetch_arrow_table` deprecation) and PySpark to maintain seamless cross-library integration.

## Breaking Changes
None reported in this release.

## Priority
Minor