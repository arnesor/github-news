# GitHub New Releases Report 2026-08-21

**[astral-sh/ruff 0.16.4](https://github.com/astral-sh/ruff/releases/tag/0.16.4)**

### Ruff v0.16.4 Release Summary

**Summary**
Ruff 0.16.4 brings targeted bug fixes, parser accuracy improvements, and enhancements to language server features. This patch resolves a hardware compatibility crash on older Windows CPUs, enhances syntax error detection, and expands support for Jupyter notebook workflows.

**Highlights**
- **Language Server Enhancements**: Added support for pull diagnostics in notebook cells and introduced display-only fixes while marking safe fixes as preferred.
- **CPU & Parser Stability**: Fixed `InvalidInstruction` crashes on Windows CPUs lacking `POPCNT` instruction support and guaranteed a minimum stack size during module/expression parsing.
- **Syntax & Rule Refinements**: Added detection for duplicate keyword arguments and parameters declared as `nonlocal`, plus introduced autofix support for `flake8-use-pathlib` (`PTH116`).

**Breaking Changes**
None.
---
**[narwhals-dev/narwhals v2.25.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.25.0)**

### Summary
Narwhals v2.25.0 introduces new string and list manipulation capabilities alongside internal performance optimizations across eager execution and schema resolution. This release also delivers critical consistency fixes for null propagation, index alignment, and PyArrow/pandas-like backend behaviors.

### Highlights
- **Core Performance Boosts**: Removed redundant computation in eager `when/then` evaluation, schema resolution, selectors, and module lookups (#3797).
- **String & List API Additions**: Added `str.strip_chars_{start,end}` (#3843) and the `maintain_order` parameter for `{Expr, Series}.list.unique` (#3697).
- **Backend Consistency & Null Handling**: Fixed null propagation across string boolean methods, `is_in`, and `with_row_index`, alongside resolving left-hand index alignment rules for pandas-like `concat` (#3865, #3859, #3866).

### Breaking Changes
None reported in this release.