# GitHub New Releases Report 2026-03-25

**[astral-sh/uv 0.11.1](https://github.com/astral-sh/uv/releases/tag/0.11.1)**

## uv v0.11.1 Release Notes

### Summary
`uv` v0.11.1 is a maintenance release focused on refining Python version resolution and improving compatibility with specific hardware architectures and package indices. It addresses several regressions and edge cases discovered following the recent 0.11.0 milestone.

### Highlights
- **Refined Python Versioning:** Added special-casing for `==` Python version request ranges to ensure more predictable environment matching and resolution.
- **Architecture & Index Fixes:** Resolved missing hash verification for RISC-V 64 Linux (MUSL) and optimized PyTorch index sourcing by removing `torchdata` from the specialized index list.
- **Enhanced Download Reliability:** Implemented a fallback mechanism to direct downloads when direct URL streaming is unsupported, ensuring better compatibility with various remote hosting environments.

### Breaking Changes
None. This release consists of bug fixes, reverts to previous behavior, and documentation improvements.
---
**[narwhals-dev/narwhals v2.18.1](https://github.com/narwhals-dev/narwhals/releases/tag/v2.18.1)**

### Narwhals v2.18.1 Release Analysis

#### Summary
Narwhals v2.18.1 is a maintenance patch focused on resolving a specific bug in string operations and improving internal codebase stability. This release ensures better compatibility for users leveraging pandas DataFrames backed by pyarrow large-string types.

#### Highlights
*   **Bug Fix for `concat_str`**: Resolved an issue where string concatenation failed for pandas DataFrames utilizing pyarrow-backed large-string columns.
*   **Codebase Maintenance**: Improved exception handling by adding proper attribute annotations to exception messages.
*   **Noise Reduction**: Silenced unavoidable third-party `DeprecationWarnings` and marked tests affected by external pandas regressions to ensure cleaner CI/CD runs.

#### Breaking Changes
None. This is a non-breaking patch release.

#### Priority
**Bugfix**