# GitHub New Releases Report 2026-03-18

**[dynaconf/dynaconf 3.2.13](https://github.com/dynaconf/dynaconf/releases/tag/3.2.13)**

# Dynaconf 3.2.13 Release Notes

### Summary
Dynaconf 3.2.13 is a security-focused maintenance release addressing critical vulnerabilities within the configuration templating system. This update specifically patches security risks in `@jinja` and `@format` tokens while resolving functional bugs in the internal converter logic.

### Highlights
- **Templating Security:** Patched vulnerabilities in `@jinja` and `@format` processing to prevent potential exploitation via configuration strings.
- **Converter Fix:** Resolved an issue where the `@get` converter was failing, ensuring configuration cross-references work as expected.
- **Maintenance:** Stability improvements for the 3.2.x release branch.

### Breaking Changes
- **None:** This is a patch release focused on security and bug fixes; no breaking changes are introduced.
---
**[pola-rs/polars py-1.39.2](https://github.com/pola-rs/polars/releases/tag/py-1.39.2)**

## Polars py-1.39.2 Release Analysis

### Summary
Polars version 1.39.2 is a maintenance release for the Python package that contains no functional code changes. It likely serves to synchronize version numbers or address internal packaging and CI/CD requirements within the repository.

### Highlights
* **Version Synchronization:** This release aligns the Python package version without introducing new logic or modifications to the engine.
* **Maintenance Update:** The update is purely administrative, ensuring consistency across the Polars ecosystem.
* **No Impact on Usage:** Developers will experience no changes in functionality, performance, or API behavior compared to the previous patch.

### Breaking Changes
* None.
---
**[unionai-oss/pandera v0.30.1](https://github.com/unionai-oss/pandera/releases/tag/v0.30.1)**

## 🚀 Pandera v0.30.1 Release Notes

### Summary
Pandera v0.30.1 introduces architectural refinements to schema management and enhances validation capabilities for Polars users. This update primarily focuses on refactoring internal accessors to use a centralized schema registry while expanding type support within the Polars engine.

### Highlights
*   **Schema Registry Refactor**: Pandera accessors have been refactored to utilize a schema registry, improving how schemas are managed and tracked internally.
*   **Enhanced Polars Support**: This release adds support for instance types in Polars, allowing for more granular validation within Polars-based workflows.
*   **Community Growth**: This version includes contributions from new community members, expanding the reach of the Polars integration.

### ⚠️ Breaking Changes
None. This is a patch release focused on internal improvements and incremental feature additions.