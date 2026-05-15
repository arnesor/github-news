# GitHub New Releases Report 2026-05-15

**[astral-sh/ruff 0.15.13](https://github.com/astral-sh/ruff/releases/tag/0.15.13)**

### Summary
Ruff 0.15.13 focuses on refining existing linting rules and enhancing developer experience with a new preview rule for lazy import evaluation. This release also addresses several key false positives in core rules and improves CLI visibility with colorized success messages.

### Highlights
* **Lazy Import Evaluation Rule**: Added a preview rule ([#25016](https://github.com/astral-sh/ruff/pull/25016)) to detect instances where lazy imports are eagerly evaluated, preventing unintended performance overhead.
* **Refined Bug Fixes**: Resolved notable false positives, specifically for class method redeclarations (`F811`), f-string debug specifiers (`PYI016`), and commented-out code detection involving leading whitespace (`ERA001`).
* **CLI & UX Upgrades**: Improved the `ruff check` output with colorized success messages and updated the `--config` help text to include practical TOML examples for better configuration management.

### Breaking Changes
None.

### Priority