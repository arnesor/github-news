# GitHub New Releases Report 2026-09-02

**[astral-sh/uv 0.12.9](https://github.com/astral-sh/uv/releases/tag/0.12.9)**

### Summary
uv 0.12.9 delivers important security hardening and bug fixes alongside noticeable performance improvements for cold wheel installations. It also introduces granular CLI controls to override lock-related environment variables and adds support for CPython 3.15.0rc2.

### Highlights
- **Security Hardening & Secret Redaction**: Resolved a potential memory-safety issue when reading metadata from untrusted wheels, ensured sensitive headers are stripped during cross-realm redirects, and redacted secrets from signed URLs in retry diagnostics.
- **Faster Wheel Installs & Concurrency Fixes**: Accelerated cold wheel installs by extracting streaming ZIPs in a single blocking task with buffer reuse, while preventing redundant extraction races between concurrent uv processes.
- **Granular Lock Mode Overrides**: Introduced `--no-locked` and `--no-frozen` CLI flags to bypass `UV_LOCKED` and `UV_FROZEN` environment variables for single invocations, ensuring explicit command-line flags always take precedence.

### Breaking Changes
None.
---
**[unionai-oss/pandera v0.33.1](https://github.com/unionai-oss/pandera/releases/tag/v0.33.1)**

### Summary
Pandera v0.33.1 is a patch release focused on restoring typing semantics and adding validation options for optional columns. It also highlights ecosystem updates, including Pandera CLI and PyArrow support announcements.

### Highlights
* **Restored `T | None` Semantics**: Fixed an issue to restore expected optional-column semantics when using bare `T | None` type annotations ([#2458](https://github.com/unionai-oss/pandera/pull/2458)).
* **Missing Column Warnings**: Added the `on_missing` option to enable warnings when optional columns are missing from the dataframe ([#2447](https://github.com/unionai-oss/pandera/pull/2447)).
* **Feature Visibility**: Updated documentation banners to highlight support for the Pandera CLI and PyArrow integration ([#2456](https://github.com/unionai-oss/pandera/pull/2456)).

### Breaking Changes
None. This is a backward-compatible patch release.