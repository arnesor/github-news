# GitHub New Releases Report 2026-10-16

**[astral-sh/ruff 0.17.1](https://github.com/astral-sh/ruff/releases/tag/0.17.1)**

### Summary
Ruff 0.17.1 is a maintenance release focusing on bug fixes and rule accuracy across multiple lint plugins. This update eliminates invalid comprehension suggestions in `perflint`, refines type-stub inspections in `flake8-pyi`, and improves mutability detection for standard library containers.

### Highlights
- **Perflint False Suggestions**: Avoids invalid comprehension rewrites previously triggered by `PERF401` and `PERF403`.
- **`flake8-pyi` Fixes**: Resolved false positives on quoted annotations (`PYI036`) and added detection for legacy positional-only parameters in `__new__` methods (`PYI063`).
- **Expanded Container Mutability**: Enhanced detection to recognize more `collections` and `weakref` containers as mutable, improving accuracy across related lint checks.

### Breaking Changes
None. This is a backward-compatible patch release.