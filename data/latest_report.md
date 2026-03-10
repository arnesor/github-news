# GitHub New Releases Report 2026-03-10

**[duckdb/duckdb v1.5.0](https://github.com/duckdb/duckdb/releases/tag/v1.5.0)**

DuckDB v1.5.0, codenamed "Variegata," introduces a significant leap in system stability and performance, featuring buffer-managed query results and the ability to perform concurrent reads during checkpoints. This release also marks the formalization of the `VARIANT` logical type with full storage support and a complete modernization of the Command Line Interface (CLI).

### Highlights

* **Buffer-Managed Results & High Concurrency:** A new buffer-managed query result system prevents Out-of-Memory (OOM) errors during large data fetches. Furthermore, architectural improvements now allow connections to perform reads concurrently while a background checkpoint is in progress, significantly improving multi-connection availability.
* **Semi-Structured Data (`VARIANT`):** Comprehensive support for the `VARIANT` type is now integrated, including native storage implementation, automatic "shredding" for Parquet files, and optimizer pushdown for `variant_extract` and casting operations.
* **CLI & UX Overhaul:** The CLI has been refactored to use the C++ API, introducing modern features like dynamic syntax highlighting, advanced Zsh-style autocomplete, light/dark mode detection, and the new `_` token to query the results of the previous statement.

### Breaking Changes

⚠️ **Geometry & Extensions:** The `GEOMETRY` type has undergone a significant rework including logical type changes and new Coordinate Reference System (CRS) support, which may impact Spatial extension workflows. Additionally, several internal C-API structures and the serialization framework have been refactored; developers of custom extensions should recompile and verify compatibility with the new storage and binder changes.
---
**[numpy/numpy v2.4.3](https://github.com/numpy/numpy/releases/tag/v2.4.3)**

### NumPy 2.4.3 Release Summary

NumPy 2.4.3 is a maintenance patch release focused on resolving bugs and stability issues discovered in the 2.4.2 release. It provides essential fixes for threading on ARM architectures and improves memory safety across the library.

### Highlights

*   **ARM Architecture Fix:** Resolves a critical threading issue for OpenBLAS on ARM platforms, improving stability for mobile and cloud-native environments (Issue #30816).
*   **Memory Management:** Addresses several memory leaks, buffer overruns in CPU baseline validation, and NULL pointer dereferences identified via LeakSanitizer.
*   **Functional Improvements:** Fixes a weak hash function in `np.isin()`, corrects infinite recursion in masked structured arrays, and repairs boolean weekmask handling in `busdaycalendar`.

### Breaking Changes

None. This is a patch release intended to be a drop-in replacement for earlier 2.4.x versions. It maintains support for Python 3.11 through 3.14.