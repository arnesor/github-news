# GitHub New Releases Report 2026-07-21

**[astral-sh/uv 0.11.30](https://github.com/astral-sh/uv/releases/tag/0.11.30)**

### uv 0.11.30 Release Analysis

**Summary**
`uv` version 0.11.30 focuses heavily on performance optimizations for dependency resolution and caching, while also introducing early support for CPython 3.15.0b4. This release also refines workspace management in preview mode and addresses edge cases in uninstallation and environment configuration.

**Highlights**
* **Massive Resolver & Cache Performance Gains:** Accelerates lockfile serialization using `toml_writer`, limits parallel cache reads to reduce scheduling overhead, and optimizes candidate resolution by caching requirement markers and skipping candidates excluded by `exclude-newer`.
* **CPython 3.15.0b4 Support:** Adds compatibility for the latest Python 3.15 beta, allowing developers to test their environments against upcoming Python versions.
* **Workspace Usability Upgrades:** Enhances preview features by allowing `uv workspace metadata --sync` to target the active virtual environment via `--active`, and fixes centralized project environment reuse when workspaces are accessed via symlinks.

**Breaking Changes**
⚠️ **None.** This release is fully backward-compatible.