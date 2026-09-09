# GitHub New Releases Report 2026-09-09

**[astral-sh/uv 0.12.11](https://github.com/astral-sh/uv/releases/tag/0.12.11)**

### Summary
uv 0.12.11 delivers substantial performance improvements for package installation and local wheel extraction alongside tighter hash verification safeguards. It also refines preview support for PEP 751 (`pylock.toml`) lockfiles and resolves various cross-platform CLI issues.

### Highlights
- **Optimized Installs & Wheel Extraction**: Significantly speeds up installation and overwrites by eliminating per-file temporary directories and adopting positioned reads with reusable buffers for local ZIP/wheel extraction.
- **Pre-Build Source Hash Verification**: Closes a security gap by verifying source archives against recorded hashes in `uv.lock` before reading package metadata or executing build backends.
- **PEP 751 (`pylock.toml`) Compliance**: Automatically generates missing artifact hashes when exporting `pylock.toml` files and warns when hash tables are empty.

### Breaking Changes
None. Note that empty `pylock.toml` artifact hash tables now emit a deprecation warning and will be rejected in an upcoming release.
---
**[narwhals-dev/narwhals v2.26.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.26.0)**

### Summary
Narwhals v2.26.0 brings key performance optimizations for selector routing and pandas-like statistical operations alongside critical PyArrow backend bug fixes. This release also stabilizes typing across selectors and concatenation while deprecating `cat.get_categories` to maintain alignment with upstream Polars updates.

### Highlights
- **Engine Performance Improvements**: Optimized bare selector evaluation via `simple_select` and accelerated pandas-like execution for `is_finite`, `sqrt`, `kurtosis`, and `skew`.
- **PyArrow Bug Fixes**: Corrected `clip` behavior to preserve nulls rather than replacing them with boundary values, and fixed series length preservation in `shift` when offset `n` exceeds array length.
- **Typing & API Modernization**: Improved type stability for selectors and `concat` with stable frame classes, and transitioned category retrieval to use `dtype.categories` on `pl.Enum`.

### Breaking Changes
None. Note that `cat.get_categories` has been formally deprecated following its removal in upstream Polars.