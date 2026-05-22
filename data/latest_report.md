# GitHub New Releases Report 2026-05-22

**[astral-sh/ruff 0.15.14](https://github.com/astral-sh/ruff/releases/tag/0.15.14)**

### Summary
Ruff version 0.15.14 introduces several new preview rules targeting decorator ordering, fallible context managers, and Airflow task outputs, alongside key parser performance optimizations. The update also improves type-checking integration with PEP 798 support and resolves various false positives in existing lint rules.

### Highlights
* **New Lint Rules in Preview**: Introduces `RUF074` (incorrect decorator order) to catch misordered decorators, `RUF075` to identify fallible context managers, and `W0717` (`too-many-try-statements`) for code complexity.
* **Type-Checking and PEP 798 Support**: Incorporates support for PEP 798, treats generic `frozenset` annotations as immutable, and avoids strict-mode false positives in `flake8-type-checking` (`TC001`, `TC002`, `TC003`) when `future-annotations` are active.
* **Performance & Parser Stability**: Boosts speed by avoiding unnecessary parser lookahead for operators and adds a parser recursion limit to prevent crashes on deeply nested code.

### Breaking Changes
No breaking changes are introduced in this release. Note that the `PTH101` autofix has been downgraded to "unsafe" when the first argument is an integer-annotated class attribute to prevent potential runtime issues.
---
**[astral-sh/uv 0.11.16](https://github.com/astral-sh/uv/releases/tag/0.11.16)**

### Summary
`uv` version 0.11.16 delivers key enhancements, including support for direct archive dependencies in Git and a new environment variable to disable reading system configurations. It also brings crucial security and stability updates, such as preventing credential leaks in wheel hints and rejecting unsafe entry points during builds.

### Highlights
* **Security Hardening:** Resolves a potential credential leak in incompatible wheel hints ([#19504](https://github.com/astral-sh/uv/pull/19504)) and blocks unsafe entry points in `uv-build` ([#19495](https://github.com/astral-sh/uv/pull/19495)).
* **Git Archive Dependencies:** Introduces support for direct archive dependencies within Git ([#10072](https://github.com/astral-sh/uv/pull/10072)), providing more flexibility when sourcing packages.
* **CI/CD Isolation (`UV_NO_SYSTEM_CONFIG`):** Adds a new configuration flag ([#19476](https://github.com/astral-sh/uv/pull/19476)) to bypass reading the system-wide configuration, ensuring cleaner, more reproducible environments.

### Breaking Changes
* **None.** This is a non-breaking, backwards-compatible release.
---
**[marimo-team/marimo 0.23.7](https://github.com/marimo-team/marimo/releases/tag/0.23.7)**

### Marimo v0.23.7 Release Summary

**Summary**
Marimo v0.23.7 introduces major upgrades to data exploration and presentation workflows, featuring powerful new table column filters and speaker notes for slide views. Additionally, WASM-based notebooks can now query remote files directly via DuckDB, significantly expanding serverless data science capabilities.

**Highlights**
* **Powerful Table Column Filters:** Added full operator support across all data types. This includes regex and value pickers for text, native range selectors for numbers, and an intuitive date/time filter UI with smart ISO/US/RFC date clipboard pasting.
* **WASM Remote Queries via DuckDB:** WASM-powered notebooks can now query remote CSV, Parquet, JSON, and GeoJSON files over HTTP. Marimo achieves this by rewriting the AST with `sqlglot` to fetch and bind the remote files as Pandas DataFrames that DuckDB can scan.
* **Speaker Notes for Slides:** Presenters can now press `S` in slide view to open speaker notes alongside the active slide, which is fully supported in both fullscreen and kiosk modes.

**Breaking Changes**
No major breaking changes. However, developers utilizing internal APIs should note that `ctx.notify` has been renamed to `broadcast_raw_notification` ([#9581](https://github.com/marimo-team/marimo/pull/9581)).