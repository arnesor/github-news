# GitHub New Releases Report 2026-10-05

**[psf/black 26.10.0](https://github.com/psf/black/releases/tag/26.10.0)**

### Summary
Black 26.10.0 delivers substantial performance optimizations across multi-file runs and complex syntax trees, alongside extensive stability fixes for formatting comments and modern Python syntax. This release also introduces standard CLI configuration improvements, including native `NO_COLOR` support and editor-friendly error reporting.

### Highlights
- **Performance Optimizations:** Resolved superlinear runtime growth when processing multiple files and significantly sped up formatting for deeply nested expressions, soft keywords (`match`/`case`), and large string collections.
- **Robust Comment & Syntax Handling:** Fixed numerous crashes and unparseable outputs related to `# fmt: skip` directives on brackets/ternaries, PEP 695 type parameter lists, and nested comments.
- **CLI & CI Improvements:** Added support for the `NO_COLOR` environment variable, standardized parser failure messages to `path:line:column` format, and added granular output metrics to the official GitHub Action.

### Breaking Changes
- **Stricter Configuration Validation:** `pyproject.toml` now strictly rejects non-string values for `include` and `force-exclude`, and invalid `BLACK_NUM_WORKERS` values now trigger usage errors.
- **Removed Utility:** The deprecated, unused `migrate-black` script has been removed.