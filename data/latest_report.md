# GitHub New Releases Report 2026-10-09

**[astral-sh/uv 0.12.24](https://github.com/astral-sh/uv/releases/tag/0.12.24)**

### uv 0.12.24 Release Notes

**Summary**
uv 0.12.24 delivers targeted performance optimizations and binary footprint reductions alongside enhanced cache pruning and configuration overrides. It also addresses critical edge cases across dependency resolution, script environment patch pinning, and integrity verification.

**Highlights**
- **Hardened Hash Verification**: Supplied package hashes are now verified even when `--no-require-hashes` or `require-hashes = false` is configured, preventing unintended tampering ([#22369](https://github.com/astral-sh/uv/pull/22369)).
- **Orphan Cleanup & Faster Executions**: `uv cache prune` now removes orphaned temporary build environments ([#22171](https://github.com/astral-sh/uv/pull/22171)), while interpreter cache warming accelerates subsequent commands run after environment creation ([#21304](https://github.com/astral-sh/uv/pull/21304)).
- **Resolver & Dependency Precision**: Prevents dependency overrides and constraints from inadvertently pulling in optional extras when those extras are not selected ([#22237](https://github.com/astral-sh/uv/pull/22237)), and correctly honors exact patch pins for managed Python in scripts ([#22360](https://github.com/astral-sh/uv/pull/22360)).

**Breaking Changes**
No breaking API changes. However, **malformed requirements-file options are now rejected** with an explicit error instead of being partially parsed or silently ignored ([#22317](https://github.com/astral-sh/uv/pull/22317)), which may cause previously tolerated syntax errors to fail builds.