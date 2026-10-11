# GitHub New Releases Report 2026-10-11

**[narwhals-dev/narwhals v2.27.1](https://github.com/narwhals-dev/narwhals/releases/tag/v2.27.1)**

### Summary
Narwhals v2.27.1 is a targeted patch release addressing edge-case behaviors in string expression functions. It improves cross-backend consistency by ensuring correct return dtypes for null object columns and fixing character-width padding on legacy Polars versions.

### Highlights
* **Accurate Return Dtype in `str.len_chars`**: Fixed an issue where computing `str.len_chars` on all-null `object` columns failed to return a proper numeric data type (#4031).
* **Correct Padding in `str.zfill` for Polars < 2.0**: Ensured that padding correctly measures character counts rather than byte lengths when running on Polars versions prior to 2.0 (#4040).

### Breaking Changes
None. This is a backwards-compatible bugfix release.
---
**[numpy/numpy v2.5.4](https://github.com/numpy/numpy/releases/tag/v2.5.4)**

### NumPy 2.5.4 Release Overview

**Summary**  
NumPy 2.5.4 is a maintenance patch release delivering critical stability, crash, and typing fixes for Python versions 3.12 through 3.15. It primarily focuses on resolving hangs in LAPACK operations, correcting `MaskedArray` type conversions, and addressing compiler-specific bugs.

**Highlights**  
- **Linear Algebra Hardening**: `numpy.linalg.svd` and `numpy.linalg.lstsq` now explicitly raise exceptions on infinite inputs, preventing process hangs on modern LAPACK implementations and eliminating garbage output.
- **Safer `MaskedArray` Fill Values**: Inherited `fill_value`s that cannot be represented in a new target `dtype` are now automatically reset to the default value rather than leaving stale, invalid states.
- **`StringDType` Hashing & Crash Fixes**: `StringDType` instances with equivalent NaN sentinels now generate identical hashes (resolving broken dictionary lookups and set deduplication), alongside fixes for segfaults in `as_arrays()` and crashes in `ufunc.accumulate`.

**Breaking Changes**  
None (patch release). Note minor behavioral adjustments: `linalg.svd` and `linalg.lstsq` will now raise an error instead of returning garbage on inputs with infinities, and conversions of `MaskedArray` with complex fill values to real dtypes may now emit a `ComplexWarning`.