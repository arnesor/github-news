# GitHub New Releases Report 2026-04-03

**[astral-sh/ruff 0.15.9](https://github.com/astral-sh/ruff/releases/tag/0.15.9)**

Ruff 0.15.9 delivers a suite of bug fixes and linting refinements, notably enhancing the accuracy of auto-fixes across `pyupgrade` and `pyflakes`. The release also introduces a new formatter configuration for nested string quotes and improves rule safety by better handling comments and symbol shadowing.

### Highlights
- **New Formatter Configuration:** A new `nested-string-quote-style` option has been added, providing more granular control over how quotes are handled in nested string scenarios.
- **Enhanced Rule Precision:** `pyupgrade` (UP018) now detects more unnecessarily wrapped literals, while `pyflakes` (F811) begins flagging annotated variable redeclarations in preview mode.
- **Improved Fix Safety:** Multiple rules, including `EM101` and `RUF024`, were updated to prevent variable shadowing during auto-fixes, and `RUF010` now correctly marks fixes as unsafe if they delete comments.

### Breaking Changes
- None. This is a maintenance release focusing on bug fixes and rule refinements.