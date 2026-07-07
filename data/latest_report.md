# GitHub New Releases Report 2026-07-07

**[astral-sh/uv 0.11.27](https://github.com/astral-sh/uv/releases/tag/0.11.27)**

### Summary
`uv` version 0.11.27 introduces a wide range of performance optimizations alongside key bug fixes and preview feature enhancements. This release focuses on speeding up core tasks like lockfile parsing, caching, and site-package scanning to deliver an even faster developer experience.

### Highlights
* **Broad Performance Gains:** Key optimizations include SIMD-accelerated TOML parsing (#20079), avoiding full site-packages scans for direct reinstalls (#20119), reducing allocations during version specifier parsing (#20105), and caching default dependency markers when reading locks (#20125).
* **Workspace Shebang Script Discovery (Preview):** The `uv workspace list --scripts` command has been enhanced to automatically discover extensionless shebang scripts (#20099).
* **Robustness & Ecosystem Support:** Re-adds public APIs used by the Pixi package manager (#20074) and improves stability by raising a proper error instead of panicking when a registry package lacks a version in `uv.lock` (#19855).

### Breaking Changes
* None. This is a backward-compatible patch release.