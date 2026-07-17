# GitHub New Releases Report 2026-07-17

**[astral-sh/ruff 0.15.22](https://github.com/astral-sh/ruff/releases/tag/0.15.22)**

### Summary
Ruff version 0.15.22 introduces several new preview rules aimed at modernizing configuration comments alongside a new autofix for module-level import placement. This release also delivers substantial parser performance optimizations and key bug fixes for Python type stub files and loop variable checks.

### Highlights
* **Modernized Ignore Comments (`RUF105`, `RUF106`, `RUF201`)**: New preview rules encourage transitioning from legacy `# noqa` comments to `# ruff:ignore`, while promoting human-readable rule names instead of opaque codes in both inline comments and configuration selectors.
* **Autofix for `E402` (Module Level Imports)**: A new preview autofix automatically moves misplaced module-level imports to the top of the file, smoothing out import ordering workflows.
* **Parser & Lexer Performance Boosts**: Several under-the-hood optimizations have been introduced—including avoiding redundant lexer token bookkeeping, eliminating unnecessary identifier lookaheads, and reusing parser scratch buffers—to speed up linting times.

### Breaking Changes
⚠️ **None**: There are no breaking changes introduced in this release.