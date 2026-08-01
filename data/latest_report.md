# GitHub New Releases Report 2026-08-01

**[astral-sh/uv 0.12.1](https://github.com/astral-sh/uv/releases/tag/0.12.1)**

### Summary
uv 0.12.1 introduces package-specific pre-release policies, preview automatic fixes for `uv check`, and faster lockfile parsing. This release also resolves workspace dependency group access, adds Xonsh shell activation support, and accelerates SHA-256 hashing on ARM64 platforms.

### Highlights
- **Package-Specific Pre-releases**: Target specific packages for pre-release installation policies using the new `--prerelease-package` flag.
- **Auto-Fixes & Xonsh Shell Support**: Added preview support for `--fix` in `uv check` alongside virtual environment activation scripts for Xonsh (`activate.xsh`).
- **Performance Optimizations**: Faster canonical lockfile parsing direct from TOML and accelerated SHA-256 hashing on non-Windows ARM64 hardware.

### Breaking Changes
None.
---
**[marimo-team/marimo 0.23.16](https://github.com/marimo-team/marimo/releases/tag/0.23.16)**

### marimo 0.23.16 Release Summary

**Summary**
marimo v0.23.16 introduces automatic local data source discovery alongside an upgraded UI for `mo.callout` components and presentation slides. This release also delivers various developer experience improvements, LLM updates, and critical bug fixes across DuckDB connections, Windows kernels, and frontend rendering.

**Highlights**
* **Automatic Data Source Discovery**: Scans environment variables to auto-detect and quickly add connections to Postgres, MySQL, Trino, AWS, PyIceberg, and PySpark through a new editor UI.
* **Callout & Admonition Glow-up**: Added an optional `title` parameter with matching icons to `mo.callout`, featuring unified, GitHub-inspired styling for markdown admonitions.
* **UX & Engine Enhancements**: Introduced "scroll for more" hints for overflowing slides, improved S3 container credential handling, editable line copy hotkeys, and fixed `Ctrl+C` killing the Windows kernel.

**Breaking Changes**
None.