# GitHub New Releases Report 2026-06-20

**[astral-sh/uv 0.11.23](https://github.com/astral-sh/uv/releases/tag/0.11.23)**

### Summary
`uv` version 0.11.23 is a targeted patch release focused on resolving regressions introduced in recent updates. This release restores critical compatibility with the `pre-commit-uv` ecosystem and corrects workspace configuration resolution issues.

### Highlights
* **Restored `pre-commit-uv` Compatibility:** Reverted a recent change to "transparent Python upgrades" in project environments to mitigate unintended breakages when running `pre-commit-uv` hooks.
* **Workspace Resolution Fix:** Restored legacy behavior where workspace members "hidden" by an intermediate `pyproject.toml` are correctly treated as standalone projects.
* **Rapid Stability Rollback:** This release acts as a focused hotfix to ensure developer environment stability and prevent CI/CD pipeline failures caused by recent toolchain updates.

### Breaking Changes
* **None.** This release does not introduce new breaking changes; instead, it actively rolls back previous changes to resolve accidental breakages and restore expected behaviors.
---
**[pytest-dev/pytest 9.1.1](https://github.com/pytest-dev/pytest/releases/tag/9.1.1)**

### pytest 9.1.1 Release Notes Summary

**Summary**
Pytest 9.1.1 is a patch release addressing critical regressions introduced in version 9.1.0 alongside typing and logic bugs. Key updates include restoring `conftest.py` loading behavior for specific invocation directories and resolving an issue with indirect fixture parametrization overrides.

**Highlights**
* **Conftest Loading Regression Fixed (#14608):** Restored the automatic loading of `conftest.py` files located in `<invocation dir>/test*` when invoking pytest without arguments, ensuring initialization hooks like `pytest_addoption` fire correctly.
* **Parametrized Fixture Overriding (#14591):** Fixed a regression that triggered a "duplicate parametrization" error when overriding a parametrized fixture using indirect `@pytest.mark.parametrize`.
* **Exception Group Assertions (#14220):** Resolved a logic bug in `pytest.RaisesGroup` that occasionally displayed incorrect and confusing mismatch messages during test failures.

**Breaking Changes**
⚠️ None. This is a patch release focused solely on bug fixes and regressions.