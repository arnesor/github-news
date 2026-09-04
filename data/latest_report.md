# GitHub New Releases Report 2026-09-04

**[astral-sh/ruff 0.16.6](https://github.com/astral-sh/ruff/releases/tag/0.16.6)**

### Summary
Ruff 0.16.6 delivers targeted bug fixes, parser enhancements, and incremental preview rule improvements across multiple linting categories. This patch release resolves parser panics, refines built-in call detection, and introduces early compatibility support for Python 3.15 match patterns.

### Highlights
* **Panic & Parser Fixes**: Resolved a crash on `match` subjects in `flake8-bugbear` (`B031`) and added proper validation for unary expressions during parsing.
* **Expanded Builtin Detection**: Updated `flake8-async` (`ASYNC230`) and `pylint` (`PLW1514`) rules to properly recognize calls via `builtins.open`.
* **Autofix Refinements**: Added an autofix for `flake8-pytest-style` (`PT020`), resolved an autofix loop between `TID254` and `TID255`, and excluded pragma comments from line length calculation in `isort` (`I001`).

### Breaking Changes
*None.* This is a backwards-compatible patch release focused on bug fixes and preview feature refinements.