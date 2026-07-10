# GitHub New Releases Report 2026-07-10

**[astral-sh/ruff 0.15.21](https://github.com/astral-sh/ruff/releases/tag/0.15.21)**

### Summary
Ruff version 0.15.21 delivers a robust suite of performance optimizations alongside practical additions to its linting and formatting toolkits. Key updates include new CLI flags for rule ignoring and exclusion, alongside improved syntax handling for Jupyter notebooks.

### Highlights
* **New CLI Capabilities**: Introduces `--add-ignore` (in preview) to programmatically append `ruff:ignore` comments to your code, and `--extend-exclude` for the `ruff format` command to extend exclude patterns without overwriting existing defaults.
* **Massive Performance Enhancements**: Optimizes the formatter and linter via cached parenthesized expression boundaries, inlining of hot paths (like `fits_element`), lazy builtin bindings, and enabling ICF (Identical Code Folding) for macOS release builds.
* **Improved Rule & Parsing Safety**: Marks executable/type-stubs autofixes (`EXE004` and `PYI061`) as unsafe to prevent unintended side effects, and refines syntax error detection in individual Jupyter notebook cells.

### Breaking Changes
* **None**. There are no breaking API changes in this release. Note that some rule autofixes have been marked as unsafe, meaning they will no longer run automatically during default `--fix` passes.