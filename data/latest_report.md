# GitHub New Releases Report 2026-05-16

**[numpy/numpy v2.4.5](https://github.com/numpy/numpy/releases/tag/v2.4.5)**

# NumPy v2.4.5 Analysis

NumPy 2.4.5 is a targeted patch release focusing on stability, memory safety, and refined type hinting for the 2.4.x series. It maintains infrastructure and provides essential bug fixes for environments running Python 3.11 through 3.14.

### Highlights

*   **Critical Memory & Safety Fixes:** Patches a heap buffer overflow in `timedelta` string casts, resolves a memory leak in `np.zeros`, and prevents a deadlock scenario caused by downstream imports during `dlopen` calls.
*   **Significant Typing Improvements:** Enhances type hint accuracy and assignability for core functions including `np.shape`, `tile`, and `sliding_window_view`, alongside a fix for `DTypeLike` runtime type-checker support.
*   **Compatibility & Regression Fixes:** Restores support for older pickles by reverting a `np.dtype()` signature deprecation and fixes in-place aliasing issues (where `out=input`) for `matvec` and `vecmat` operations.

### Breaking Changes

None. As a patch release, v2.4.5 is backward compatible. Note that `matrix_rank` now returns 0 for empty matrices; while technically a bug fix for consistency, users relying on previous edge-case behavior should verify their workflows.