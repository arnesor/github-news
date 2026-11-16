# GitHub New Releases Report 2026-11-16

**[numpy/numpy v2.5.5](https://github.com/numpy/numpy/releases/tag/v2.5.5)**

### Summary
NumPy 2.5.5 is an unusually large patch release delivering critical bug fixes across string operations, threading, and core array internals ahead of the 2.6.0 release. Supporting Python 3.12 through 3.15, this release addresses multiple race conditions, segmentation faults, and memory management issues.

### Highlights
- **Thread Safety & GIL Enhancements:** Properly acquires the GIL during error and warning handling in `nditer`, ufunc error paths, sorting routines, and datetime conversions to prevent race conditions.
- **StringDType Stability & String Fixes:** Fixed allocation and bounds-check errors in `StringDType`, resolved unicode/byte index mixups in `startswith`/`endswith` and fastsearch, and addressed a `loadtxt` crash.
- **Core Stability & Leak Fixes:** Resolved a segmentation fault in `ufunc.at` when `nin=0`, eliminated a hang in `ndarray.take` on zero-size axes, and fixed reference leaks in multi-output ufuncs.

### Breaking Changes
⚠️ **Type Casting Restriction:** Casting a structured void dtype or subarray dtype to `numpy.dtypes.StringDType` now strictly raises a `TypeError` instead of unsafely reinterpreting the element's raw bytes as UTF-8 ([#33298](https://github.com/numpy/numpy/pull/33298)).