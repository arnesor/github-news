# GitHub New Releases Report 2026-06-30

**[dynaconf/dynaconf 3.3.2](https://github.com/dynaconf/dynaconf/releases/tag/3.3.2)**

### Summary
Dynaconf 3.3.2 is a patch release focused on resolving key stability issues, edge-case crashes, and parser anomalies in configuration handling. This update delivers critical bug fixes for validation processes, environment-based loading recursion, and list merging operations to ensure a more robust configuration experience.

### Highlights
* **Fix `RecursionError` in `from_env` (#1409):** Prevents an infinite recursion crash when environment-based loading is triggered alongside the `validate_on_update` option.
* **Safer List Merging (#1410):** Resolves a crash that occurred when attempting to merge a list marked with `dynaconf_merge` into a missing or undefined configuration key.
* **Improved Parser Precision (#1411, #1412):** Corrects validation edge cases within `validation_file.toml` and ensures strings that merely share a prefix with a converter are no longer incorrectly processed as casts.

### Breaking Changes
There are no breaking changes introduced in this patch release.
---
**[unionai-oss/pandera v0.32.1](https://github.com/unionai-oss/pandera/releases/tag/v0.32.1)**

### Pandera v0.32.1 Release Analysis 🚀

**Summary**
Pandera v0.32.1 is a patch release focused on improving thread safety, validation reliability, and ecosystem integrations across Polars, PySpark, and Xarray. It resolves critical concurrency bottlenecks while introducing minor developer experience enhancements, such as Pydantic alias support.

**Highlights**
* **Thread Safety & Concurrency Fixes:** Resolves critical concurrency bugs by isolating configuration contexts per execution context (#2380) and ensuring strict thread-safety during Pandas schema validation (#2383).
* **Pydantic Alias Support:** Adds native support for Pydantic aliases within DataFrame schemas, streamlining data validation workflows that rely on customized model field mappings (#2381).
* **Ecosystem Resilience:** Fixes builtin check registration in Polars-only installations (#2389), handles missing regex matches gracefully in PySpark (#2394), and preserves regex DataVar schemas in Xarray during validation (#2393).

**Breaking Changes**
⚠️ **None.** This is a backwards-compatible patch release.