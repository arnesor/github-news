# GitHub New Releases Report 2026-03-06

**[astral-sh/ruff 0.15.5](https://github.com/astral-sh/ruff/releases/tag/0.15.5)**

### Summary
Ruff 0.15.5 expands its reach into documentation by enabling Markdown file discovery by default in preview mode. This release also delivers key refinements to `perflint` and `ruff` rules, alongside critical bug fixes for FastAPI, `pydocstyle`, and `pyflakes`.

### Highlights
* **Markdown Discovery**: Markdown files are now automatically discovered when running in preview mode, streamlining the formatting and linting of documentation within your codebase.
* **Expanded Performance Linting**: Rule `PERF102` now extends to comprehensions and generators, helping developers catch more instances of unnecessary list/set/dict creation.
* **FastAPI Improvements**: Fixed `FAST003` to correctly handle callable class dependencies with `__call__` methods, reducing false positives for complex dependency injection patterns.

### Breaking Changes
No breaking changes were introduced in this release.

### Priority