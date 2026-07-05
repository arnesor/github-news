# GitHub New Releases Report 2026-07-05

**[numpy/numpy v2.5.1](https://github.com/numpy/numpy/releases/tag/v2.5.1)**

### Summary
NumPy 2.5.1 is a patch release focused on fixing bugs, refining type hints, and continuing preparation for Python 3.15. Most notably, this release restores backwards compatibility for downstream packages via a critical fix to the Cython Datetime API and resolves several memory leaks.

### Highlights
* **Cython Datetime API Fix ([#31835](https://github.com/numpy/numpy/pull/31835)):** Fixes compatibility issues with the NumPy datetime Cython APIs, allowing downstream libraries to seamlessly support NumPy versions older than 2.5.
* **Memory & Threading Fixes:** Resolves critical memory leaks in `reduceat` and `accumulate` operations ([#31833](https://github.com/numpy/numpy/pull/31833), [#31842](https://github.com/numpy/numpy/pull/31842)) and prevents potential deadlocks within the `NpyString` API ([#31832](https://github.com/numpy/numpy/pull/31832)).
* **Regression & Bug Patches:** Fixes a regression in `np.ma.masked_array` introduced in 2.5.0 ([#31837](https://github.com/numpy/numpy/pull/31837)), corrects dtype inference for empty lists in `asarray([])` ([#31836](https://github.com/numpy/numpy/pull/31836)), and prevents a segfault in MT19937 random seeding ([#31857](https://github.com/numpy/numpy/pull/31857)).

### Breaking Changes
* **Toolchain Requirements:** While there are no breaking runtime API changes, the minimum supported GCC version for compiling NumPy from source has been updated from **9.3.0 to 10.3.0** ([#31849](https://github.com/numpy/numpy/pull/31849)).