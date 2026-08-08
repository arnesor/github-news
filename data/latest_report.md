# GitHub New Releases Report 2026-08-08

**[astral-sh/ruff 0.16.2](https://github.com/astral-sh/ruff/releases/tag/0.16.2)**

### Summary
Ruff 0.16.2 is a lightweight patch release focused on refining LSP server capabilities and linting accuracy. This update resolves false positive type-hinting warnings for `singledispatch` functions and optimizes language server behavior around TOML files.

### Highlights
- **LSP TOML Formatting Exclusions:** Language server formatting capabilities are now registered dynamically to properly exclude TOML files from formatting requests ([#27332](https://github.com/astral-sh/ruff/pull/27332)).
- **`flake8-pyi` False Positive Fix (`PYI041`):** Resolved incorrect rule violations triggered on `singledispatch` functions ([#27335](https://github.com/astral-sh/ruff/pull/27335)).

### Breaking Changes
None.
---
**[astral-sh/uv 0.12.3](https://github.com/astral-sh/uv/releases/tag/0.12.3)**

### Summary
`uv` version 0.12.3 delivers targeted performance improvements for Linux startup times, memory efficiency in large workspaces, and dependency resolution. It also introduces support for CPython 3.13.15 alongside enhancements to workspace metadata tooling.

### Highlights
- **Linux & Discovery Performance:** Significantly reduced Linux startup latency by optimizing cache initialization and avoiding slow `/proc` reads during Python interpreter discovery.
- **Lower Memory Footprint:** `uv workspace metadata` now streams JSON output, drastically reducing memory usage when querying large monorepos.
- **Faster Dependency Resolutions:** Accelerated conflict-heavy package resolutions by avoiding unnecessary materialized range complements.

### Breaking Changes
None.