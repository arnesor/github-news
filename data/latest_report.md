# GitHub New Releases Report 2026-10-23

**[astral-sh/ruff 0.17.2](https://github.com/astral-sh/ruff/releases/tag/0.17.2)**

### Ruff 0.17.2 Release Overview

**Summary**  
Ruff 0.17.2 is a maintenance release delivering targeted bug fixes, performance improvements, and rule refinements. It also introduces a configurable allowlist for magic values and enhances autofix safety around comment deletion.

**Highlights**  
- **Configurable Allowlist for `PLR2004`**: Users can now configure an allowlist for `magic-value-comparison`, allowing common domain-specific constants without disabling the rule.
- **Safer Autofixes**: Fixes that would inadvertently delete comments are now marked as unsafe across `PLR5501`, `PLW0120`, and `UP035` to prevent accidental loss of code annotations.
- **Engine & Parser Performance**: Core performance boosts through UTF-8 byte prefiltering for bidirectional Unicode checks, shared postfix parsing, and reduced overhead during lint name resolution.

**Breaking Changes**  
None.
---
**[pandas-dev/pandas v3.1.0](https://github.com/pandas-dev/pandas/releases/tag/v3.1.0)**

### Summary
pandas 3.1.0 delivers key performance enhancements alongside improved DataFrame querying capabilities. This release brings faster, parallelized CSV ingestion for large datasets and introduces a new selection interface.

### Highlights
- **New `DataFrame.select()` & Updated `DataFrame.filter()`**: Introduces a streamlined method for selecting subset data along with behavior updates to filtering.
- **Parallel `pd.read_csv()`**: Significantly accelerates reading large CSV files by leveraging multi-threaded parallel execution.
- **Performance & Stability Fixes**: General performance improvements and bug fixes across core DataFrame operations.

### Breaking Changes
No breaking changes are explicitly listed in this release summary. However, review the detailed release notes for any deprecated behaviors or API nuances before upgrading in production.