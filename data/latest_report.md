# GitHub New Releases Report 2026-04-07

**[narwhals-dev/narwhals v2.19.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.19.0)**

### Narwhals v2.19.0 Release Summary

**Summary**
Narwhals v2.19.0 introduces expanded functionality for string operations and new statistical capabilities, further bridging the gap between Polars, pandas, and SQL backends. This update also focuses on internal consistency and developer experience through improved typing and standardized naming conventions.

**Highlights**
* **Enhanced `str.contains`**: Users can now pass `Expr` or `Series` objects as patterns in `str.contains` for Polars and SQL-like backends, enabling dynamic, column-based pattern matching.
* **New `nw.corr` Function**: Added native support for calculating correlation coefficients, expanding the library's statistical toolkit across supported dataframes.
* **Internal API Cleanup**: Standardized date handling by replacing `weekday` with `day_of_week` for pandas and Dask backends to ensure cross-library consistency.

**Breaking Changes**
* None.