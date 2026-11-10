# GitHub New Releases Report 2026-11-10

**[unionai-oss/pandera v0.36.0](https://github.com/unionai-oss/pandera/releases/tag/v0.36.0)**

### Summary
Pandera v0.36.0 introduces the new `pandera.decisions` API alongside `ParsedField` and `ParsedColumn` constructs, allowing schemas to dynamically derive fields using decision models. This release also patches a critical remote code execution (RCE) vulnerability in tensordict deserialization and brings several ecosystem-wide bug fixes.

### Highlights
* **Derived Columns & `pandera.decisions` API**: Introduced `ParsedField` and `ParsedColumn` to automatically derive and validate fields from source columns using decision models (e.g., LLMs or open-weight models for tasks like classification and scoring).
* **Security Fix (RCE Prevention)**: Resolved a critical Remote Code Execution vulnerability when loading `tensordict` structures ([GHSA-vpwq-239f-3cf7](https://github.com/unionai-oss/pandera/pull/2627)).
* **Native Enum & Literal Categoricals**: Added automatic mapping of Python `Enum` and `Literal` types to dataframe categorical dtypes, complete with comparable and hashable Polars enum support.

### Breaking Changes
No breaking changes were introduced in this release.