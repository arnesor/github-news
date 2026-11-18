# GitHub New Releases Report 2026-11-18

**[astral-sh/uv 0.13.9](https://github.com/astral-sh/uv/releases/tag/0.13.9)**

### uv 0.13.9 Release Summary

**Summary**  
uv 0.13.9 introduces preview support for PEP 832 `.venv` redirect files alongside lockfile optimizations that reduce file size and accelerate parsing. The release also addresses critical bug fixes regarding lockfile platform marker equivalence, package name validation, and HTTP/2 connection handling.

**Highlights**  
- **PEP 832 `.venv` Redirect Files (Preview)**: Adds experimental support for PEP 832 redirect files, enabling projects to reference virtual environments located outside the project root directory.
- **Lockfile Performance & Deduplication**: Significantly reduces lockfile size and improves read times by factoring out repeated conditions in environment markers.
- **Lockfile Normalization & Security Fixes**: Fixes false-positive failures in `uv lock --locked` caused by equivalent platform markers written in different syntax, and rejects wheels served by an index under mismatched package names.

**Breaking Changes**  
None. (Note: Building uv from source now requires Rust 1.98 or higher, but prebuilt binaries are unaffected.)
---
**[narwhals-dev/narwhals v2.29.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.29.0)**

### Summary
Narwhals v2.29.0 introduces native support and `.get` operations for the `Map` data type alongside expanded Arrow integration via `Series.__arrow_c_array__` and `Series.from_arrow`. It also initiates the extraction of Dask functionality into a dedicated plugin and brings robustness fixes to indexing operations like `Series.scatter`.

### Highlights
* **`Map` Datatype Support**: Introduced native support for the `Map` data type and implemented the `.get` operation for map elements (#3861, #4115).
* **Dask Plugin Transition**: Moved the Dask backend to an external `narwhals-dask` plugin and deprecated built-in Dask support in the core package (#4151).
* **Interoperability & Indexing Improvements**: Added `Series.from_arrow` and `__arrow_c_array__` integration (#4122), while resolving multiple edge cases in `Series.scatter` across negative, duplicate, out-of-bounds, and null indices (#4146, #4164, #4138).

### Breaking Changes
None in this release. However, built-in Dask support is now officially **deprecated** in favor of the standalone `narwhals-dask` plugin. Users relying on Dask integration should install the separate plugin to prepare for future removal.