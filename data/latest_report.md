# GitHub New Releases Report 2026-09-18

**[astral-sh/uv 0.12.16](https://github.com/astral-sh/uv/releases/tag/0.12.16)**

### Summary
uv 0.12.16 improves supply chain security by verifying downloaded wheels and source distributions against index-supplied hashes. This release also broadens the usability of `uv check` in non-managed projects and resolves several URL-parsing panic conditions.

### Highlights
- **Package Hash Verification**: Downloaded wheels and sdists are now automatically checked against hashes provided by package indexes, with hash support also added to `build-constraint-dependencies` ([#21562](https://github.com/astral-sh/uv/pull/21562), [#21467](https://github.com/astral-sh/uv/pull/21467)).
- **Standalone `uv check` Execution**: `uv check` can now run in projects not managed by uv or outside workspaces, and respects `--python` / `UV_PYTHON` flags ([#21777](https://github.com/astral-sh/uv/pull/21777), [#21744](https://github.com/astral-sh/uv/pull/21744)).
- **Credential Redaction & Crash Prevention**: Azure Shared Access Signatures (SAS) are now redacted from displayed URLs and logs, while malformed URLs, proxy settings, and unsupported Git schemes now return clean errors instead of panicking ([#21755](https://github.com/astral-sh/uv/pull/21755), [#21779](https://github.com/astral-sh/uv/pull/21779), [#21784](https://github.com/astral-sh/uv/pull/21784)).

### Breaking Changes
None. Note that unsupported Git URL schemes will now fail fast with a parsing error when reading lockfiles rather than panicking during frozen exports.
---
**[pandas-dev/pandas v3.0.6](https://github.com/pandas-dev/pandas/releases/tag/v3.0.6)**

### pandas v3.0.6 Release Overview

**Summary**
Pandas 3.0.6 is a maintenance patch release for the 3.0.x series aimed at resolving functional bugs and regressions. It also marks the first release in the project's history to introduce support for Python 3.15.

**Highlights**
* **Python 3.15 Support:** First release to officially provide compatibility with Python 3.15.
* **Regression Fixes:** Targeted fixes resolving behavior regressions introduced in earlier 3.0.x versions.
* **Stability Improvements:** General bug fixes; recommended upgrade for all users currently running pandas 3.0.x.

**Breaking Changes**
* None. This is a patch release backward-compatible with the 3.0.x series.