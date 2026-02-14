# GitHub New Releases Report 2026-02-14

**[astral-sh/ruff 0.15.1](https://github.com/astral-sh/ruff/releases/tag/0.15.1)**

### Ruff 0.15.1 Release Summary
Ruff 0.15.1 introduces significant enhancements to Markdown formatting support and expands the linting suite with new rules for Airflow 3.x migrations. This update also delivers critical stability improvements, including a fix for an infinite loop in the `unused-import` autofix and support for Python 3.14+ syntax.

### Highlights
* **Enhanced Markdown Support:** Ruff now supports formatting for Quarto Markdown, `pycon` code blocks, and provides Markdown formatting directly via the Language Server Protocol (LSP).
* **Airflow 3.x Migration Tools:** Added several new rules (`AIR321`, `AIR303`, `AIR301`) to detect deprecated imports, arguments, and attribute access, easing the transition to Airflow 3.0 and 3.1.
* **New Linting Rules:** Introduced `float-equality-comparison` (`RUF069`) and expanded detection for mutable defaults in `field` calls (`RUF008`) and non-existent mock methods (`PGH005`).

### Breaking Changes
None. Users should note that the program name in GitHub Action output has been changed from `Ruff` to `ruff`, which may affect highly specific CI log parsers.