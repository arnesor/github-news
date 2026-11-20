# GitHub New Releases Report 2026-11-20

**[astral-sh/ruff 0.17.6](https://github.com/astral-sh/ruff/releases/tag/0.17.6)**

### Summary
Ruff 0.17.6 is a patch release focusing on linting correctness, safer autofixes, and output performance. It resolves key false positives and syntax issues across several rules while speeding up notebook parsing and JSON diagnostic streaming.

### Highlights
- **Safer Autofixes:** Addressed a critical bug where the autofix for `useless-finally` (`RUF072`) introduced syntax errors on inline `try` bodies, and eliminated redundant `bool` wrappers in `SIM208` fixes.
- **Improved Rule Accuracy:** Fixed false positives in `PLR1733` and `PLR1736` when mutating collections within loops, corrected a false negative in `F823` for reassigned names, and stopped flagging `__traceback_hide__` as an unused variable (`F841`).
- **Performance Enhancements:** Optimized execution times by short-circuiting exact qualified-name lookups, streaming JSON diagnostics directly to the output writer, and decoding in-memory Jupyter notebooks directly from source strings.

### Breaking Changes
None. This is a non-breaking patch release.