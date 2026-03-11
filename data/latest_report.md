# GitHub New Releases Report 2026-03-11

**[narwhals-dev/narwhals v2.18.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.18.0)**

## Narwhals v2.18.0 Release Analysis

### Summary
Narwhals v2.18.0 focuses on strengthening backend compatibility, specifically enhancing support for SQLFrame and resolving edge cases in PyArrow. This release prioritizes ecosystem stability through significant updates to downstream CI and stricter expression handling.

### Highlights
*   **Enhanced SQLFrame Integration**: Added support for `Expr.replace_strict` and enabled `Expr.skew` functionality, further closing the feature gap for SQL-based backends.
*   **PyArrow `when/then` Fix**: Resolved a critical bug affecting conditional logic when handling null values in the PyArrow backend, ensuring more reliable data transformations.
*   **CI/DX Improvements**: Streamlined downstream testing for `marimo` (migrating to `uv`), `altair`, and `hierarchicalforecast` to ensure seamless integration for users of these libraries.

### Breaking Changes
None. This release maintains backward compatibility while expanding the feature set for existing backends.