# GitHub New Releases Report 2026-08-19

**[wntrblm/nox 2026.08.17](https://github.com/wntrblm/nox/releases/tag/2026.08.17)**

### Nox 2026.08.17 Release Overview

**Summary**
Nox `2026.08.17` is a targeted maintenance release that improves parallel execution compatibility on legacy Windows environments. It resolves character encoding issues within the parallel reporter alongside routine internal developer tooling updates.

**Highlights**
* **Legacy Windows Encoding Support**: Added support for legacy encodings in the parallel reporter to prevent encoding-related failures on older Windows systems (#1160).
* **Stricter Type & Test Configs**: Tightened `mypy` and `pytest` configurations to enforce better code quality (#1167).
* **Tooling & CI Updates**: Upgraded pre-commit hooks and GitHub Actions dependencies (#1162, #1163).

**Breaking Changes**
* None.