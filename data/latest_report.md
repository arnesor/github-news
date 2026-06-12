# GitHub New Releases Report 2026-06-12

**[astral-sh/ruff 0.15.17](https://github.com/astral-sh/ruff/releases/tag/0.15.17)**

### Summary
Ruff v0.15.17 introduces several ergonomic improvements under its preview flag, notably allowing the use of human-readable rule names in suppression comments and CLI outputs. This release also brings targeted rule updates for `pytest`, `pyupgrade`, and `pylint`, alongside performance optimizations and bug fixes.

### Highlights
1. **Human-Readable Suppression Names (Preview):** You can now use human-readable rule names in suppression comments (e.g., `# ruff: ignore unused-import` instead of codes like `F401`) and prioritize them in the CLI output, making codebase triage and maintenance much more intuitive.
2. **Automatic `from __future__ import annotations` (Preview):** The `pyupgrade` rules (`UP007`, `UP045`) can now automatically insert this future import to streamline and modernize type-hinting styles.
3. **Enhanced Pytest Linting (Preview):** This release adds a new rule banning `pytest` autouse fixtures (`RUF076`) and expands `flake8-pytest-style` coverage to check `pytest_asyncio` fixtures.

### Breaking Changes
No breaking changes are present in this release. *(Note: The autofix for `np.in1d` (`NPY201`) has been dropped, which changes linting behavior but does not break compatibility.)*
---
**[astral-sh/uv 0.11.21](https://github.com/astral-sh/uv/releases/tag/0.11.21)**

### Summary
`uv` version 0.11.21 introduces support for CPython 3.13.14 and 3.14.6 alongside significant performance improvements like parallelized Python discovery. This release also hardens package metadata parsing to prevent panics, optimizes cache pruning, and updates preview behaviors to streamline project initialization.

### Highlights
* **Packaged Applications by Default**: Under preview features, `uv init` now defaults to creating a packaged application structure, aligning new project initialization with modern best practices.
* **Parallel Python Discovery**: Performance of `uv python list` has been improved with parallel discovery of local Python versions, making environment audits much faster.
* **Robust Parser & Cache Hardening**: Outlawed several potential panic vectors (such as invalid UTF-8 in URL credentials or malformed source distribution filenames) and improved CI cache pruning to avoid accidentally wiping cached Python downloads.

### Breaking Changes
* **None**. (Note: The change to make packaged applications the default for `uv init` is a behavior shift, but it is currently gated behind preview features).