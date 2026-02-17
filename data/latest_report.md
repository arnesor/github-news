# GitHub New Releases Report 2026-02-17

**[astral-sh/uv 0.10.3](https://github.com/astral-sh/uv/releases/tag/0.10.3)**

### Summary
`uv` 0.10.3 introduces enhanced control over the `uv format` preview feature via Ruff version constraints and adds support for the latest CPython 3.15.0a6. This update also delivers critical stability improvements, including fixes for workspace panics and more precise Python version matching logic.

### Highlights
* **Advanced Formatting Control:** `uv format` now supports Ruff version constraints and `exclude-newer` (preview), enabling tighter control over formatting reproducibility across environments.
* **Precise Python Versioning:** Fixed a bug where version prefixes matched incorrectly (e.g., `3.1` will no longer match `3.10`) and added support for the CPython 3.15.0a6 alpha.
* **Improved Stability and DX:** Resolved a panic related to unmanaged workspace members and synchronized Windows trampoline error messages with the core `uv` CLI for better cross-platform consistency.

### Breaking Changes
No breaking changes are identified in this release.

### Priority