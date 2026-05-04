# GitHub New Releases Report 2026-05-04

**[python-poetry/poetry 2.4.0](https://github.com/python-poetry/poetry/releases/tag/2.4.0)**

## Poetry 2.4.0 Release Analysis

Poetry 2.4.0 introduces sophisticated dependency filtering based on release age to improve supply chain security and environment stability. This version also hardens the CLI experience with stricter input validation and addresses several critical bugs in publishing workflows and Windows environments.

### Highlights
*   **Dependency Age Filtering:** A new set of `solver.min-release-age` configurations allows teams to ignore packages released within a specific window (e.g., the last 2 days). This is a major win for supply chain security, helping users avoid "day-zero" malicious releases or buggy updates.
*   **Stricter `poetry update` Validation:** To prevent configuration drift and silent failures, `poetry update` now raises an explicit error if you pass a package name that is not currently a project dependency.
*   **Improved Build & Publish Reliability:** This release fixes a critical issue where `poetry publish --build` would ignore failed builds and upload stale artifacts. Additionally, it resolves a memory error encountered when calculating hashes for very large wheels.

### Breaking Changes
*   **CLI Behavior:** `poetry update <pkg>` now errors instead of silently ignoring the command if `<pkg>` is not a dependency. This may require updates to CI/CD scripts that rely on the old silent behavior.
*   **Dependency Requirements:** Poetry now requires `installer >= 1.0.0` and `findpython >= 0.8`.
*   **Metadata Changes:** The lock file marker ordering is now deterministic, which may cause a one-time diff in your `poetry.lock` files upon the next update.

### Priority: Minor