# GitHub New Releases Report 2026-08-10

**[numpy/numpy v2.5.2](https://github.com/numpy/numpy/releases/tag/v2.5.2)**

### Summary
NumPy 2.5.2 is a patch release focused on critical bug fixes, memory leak resolutions, and free-threading stability improvements. It officially introduces pre-built wheels for Python 3.15.0rc1, expanding overall support across Python 3.12 through 3.15.

### Highlights
* **Python 3.15.0rc1 Wheels:** Added official pre-built wheel support for the latest Python 3.15 release candidate.
* **C API & Free-Threading Stability:** Made `PyArray_StringDTypeObject` opaque under `abi3t` to resolve structural layout crashes, alongside fixes for 32-bit systems using `abi3t`.
* **Memory & Concurrency Fixes:** Resolved reference leaks in `copyto` and SIMD sequences, addressed thread-safety/locking bugs in RNG state access, and fixed `StringDType` memory corruption in `np.fromiter`.

### Breaking Changes
⚠️ **C API Layout Modification (`abi3t` builds):** `PyArray_StringDTypeObject` is now an opaque struct when targeting the free-threaded stable ABI (`Py_TARGET_ABI3T`). C extensions compiled for `abi3t` can no longer directly access fields on this struct. Access the allocator API via `NpyString_acquire_allocator((PyArray_StringDTypeObject *)descr)` instead. *(Note: This breaking modification was applied in a patch release because direct field access previously caused crashes due to variable object header sizes).*