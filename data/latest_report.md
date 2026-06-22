# GitHub New Releases Report 2026-06-22

**[numpy/numpy v2.5.0](https://github.com/numpy/numpy/releases/tag/v2.5.0)**

### NumPy v2.5.0 Release Summary

**Summary**
NumPy 2.5.0 is a transitional release that officially drops support for Python 3.11, completely removes `numpy.distutils`, and expires a large number of deprecations from the 2.0.x era. It also introduces significant scaling optimizations for free-threaded Python, achieves 100% typing coverage, and adds descending sort options to align with the Array API standard.

**Highlights**
* **Free-Threading & Performance Gains:** Delivers dramatically better scaling on free-threaded CPython via lock-free dispatch tables, immortal shared objects, and `mimalloc` memory allocation. Additionally, `numpy.searchsorted` is up to 20x faster for multi-key searches, and contiguous array reductions see up to 1.9x speedups.
* **Descending Sorts (Array API):** Adds a new `descending=True` keyword argument to `numpy.sort` and `numpy.argsort`, bringing sorting behavior into full compliance with the Array API standard.
* **Pattern Matching & Advanced Typing:** `numpy.ndarray` now supports structural pattern matching (`match`/`case` statements). Static typing has reached 100% submodule coverage, introducing preliminary shape-typing support for `linalg`, `fft`, and array creation functions.

**⚠️ Breaking & Compatibility Changes**
* **Python 3.11 & Distutils Dropped:** Minimum supported Python version is now 3.12. `numpy.distutils` has been completely removed.
* **`linalg.eig` Return Types:** `linalg.eig` and `linalg.eigvals` now *always* return complex arrays. If your matrix is symmetric or Hermitian, switch to `eigh` or `eigvalsh` to guarantee real-valued outputs.
* **Deprecated In-Place Mutation:** Directly setting `.shape` or `.dtype` attributes, as well as resizing arrays in-place, is now deprecated to ensure thread safety. Use `.view()` or `np.reshape` instead.
* **Strict Overflow Checking:** Arithmetic operations on `datetime64`/`timedelta64` and out-of-range Python integers in `numpy.where` now raise `OverflowError` instead of silently wrapping or truncating.