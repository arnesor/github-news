# GitHub New Releases Report 2026-06-05

**[astral-sh/ruff 0.15.16](https://github.com/astral-sh/ruff/releases/tag/0.15.16)**

### Summary
Ruff version 0.15.16 introduces key preview features targeting async patterns and loop terminal analysis, alongside valuable parsing performance improvements. It also delivers several bug fixes to prevent unintended syntax changes and false positives, particularly in formatting rules and comment eradication.

### Highlights
* **Parser Performance Enhancements:** Ruff continues to optimize its lightning-fast engine by dropping excess capacity from statement suites during parsing and shrinking additional parser AST collections to reduce memory footprint.
* **Smarter Comment Handling (`ERA001` / `RUF100`):** Resolves frustrating false positives where `ruff:ignore` comments were incorrectly flagged as dead code, and fixes conflicts when `noqa` directives are placed on commented-out code.
* **Safer Code Fixes (`F523` & `UP032`):** Enhances automated refactoring safety by ensuring Ruff avoids removing or converting `.format()` calls when doing so would introduce side effects or alter runtime behavior.

### Breaking Changes
⚠️ No breaking changes are introduced in this release.
---
**[marimo-team/marimo 0.23.9](https://github.com/marimo-team/marimo/releases/tag/0.23.9)**

### Summary
Marimo v0.23.9 improves the multi-tab notebook experience by introducing non-destructive local takeover alongside new UI controls for table column visibility. It also tightens server-side sharing security and refines the slides presentation layout for a more robust development workflow.

### Highlights
* **Multi-Tab Non-Destructive Takeover**: Opening a notebook in a second tab no longer disconnects the first. The new tab acts as a live, read-only viewer, allowing you to seamlessly take over editing control from either side with a single click.
* **Table Column Visibility**: `mo.ui.table` now supports `hidden_columns` and `visible_columns` parameters. Users can also interactively hide/show columns, perform smart prefix-based searches in the Column Explorer, and quickly "Unhide all".
* **Slide Editor & Sharing Security Upgrades**: Cells with no output are no longer lost in slide edit mode, remaining visible in the minimap for easy editing. Security is also hardened server-side with a new machine-wide `MARIMO_RESTRICT_SHARING` environment variable.

### Breaking Changes
* **None**: This release is backward-compatible. Note that `hidden_columns` and `visible_columns` in `mo.ui.table` are mutually exclusive.