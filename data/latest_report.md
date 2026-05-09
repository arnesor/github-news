# GitHub New Releases Report 2026-05-09

**[astral-sh/uv 0.11.12](https://github.com/astral-sh/uv/releases/tag/0.11.12)**

### Summary
uv 0.11.12 adds support for the CPython 3.15.0b1 beta and introduces the `--no-editable` flag to `uv pip install` for better installation control. This update also refines dependency management by ensuring CLI flags correctly override environment variables and standardizing Git URL encoding.

### Highlights
* **CPython 3.15.0b1 Support**: Early-access support for the latest Python 3.15 beta release, allowing developers to test against the upcoming version.
* **Enhanced `uv pip install`**: The addition of the `--no-editable` flag provides more granular control when managing local or VCS dependencies.
* **Improved Conflict Resolution**: The `--no-dev` flag now properly takes precedence over the `UV_DEV=1` environment variable, ensuring more predictable environment states.

### Breaking Changes
None. Note that Git refs in URLs are now required to be percent-encoded, which follows standard URL practices but may require updates to legacy requirement strings.

### Priority
---
**[narwhals-dev/narwhals v2.21.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.21.0)**

## Narwhals v2.21.0 Release Analysis

### Summary
Narwhals v2.21.0 expands its cross-backend expression library with new support for `quantile` on Spark-like engines and enhanced string manipulation features. This update also delivers critical reliability fixes for window-like operations in pandas and improves consistency across DuckDB and Ibis integrations.

### Highlights
*   **Enhanced Expression Suite:** Added `Expr.quantile` for Spark-like backends and `{Expr, Series}.str.to_time`, further narrowing the gap between native expressions and cross-library abstractions.
*   **Improved Pandas Compatibility:** Resolved a bug in `over()` when using `partition_by` and `order_by` with scrambled groups, ensuring correct results during complex windowing operations.
*   **Backend Consistency:** Introduced "expressified" `str.starts_with` and `str.ends_with` alongside fixes for DuckDB join values and Ibis logarithm defaults to ensure uniform behavior across supported engines.

### Breaking Changes
None. This release maintains backward compatibility while expanding the API surface and fixing reported bugs.

### Priority
Minor