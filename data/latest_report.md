# GitHub New Releases Report 2026-04-25

**[astral-sh/ruff 0.15.12](https://github.com/astral-sh/ruff/releases/tag/0.15.12)**

### Ruff 0.15.12 Release Analysis

Ruff 0.15.12 introduces more granular suppression controls through new file-level and logical-line ignore comments. This release also refines rules for Airflow and pandas-vet while fixing cache permission handling on Unix systems.

#### Highlights
* **Advanced Suppressions (Preview):** Added `#ruff:file-ignore` for entire files and `#ruff:ignore` for logical-line suppressions, offering more flexibility than standard line-based `noqa` comments.
* **New Airflow Rule:** Implementation of `AIR004` (`task-branch-as-short-circuit`) helps Airflow users identify suboptimal branching patterns in their DAGs.
* **CLI Permission Fix:** The CLI now correctly respects default Unix permissions for cache files, improving security and consistency in multi-user environments.

#### Breaking Changes
* None. (Note: LSP diagnostic severity changes in preview were reverted to previous behavior).
---
**[marimo-team/marimo 0.23.3](https://github.com/marimo-team/marimo/releases/tag/0.23.3)**

## Summary
marimo 0.23.3 introduces a dedicated slide configuration sidebar for easier presentation management and significantly improves system stability through architectural hardening. This release also marks a major internal shift by replacing `pickle` with `msgspec` for faster and safer Inter-Process Communication (IPC).

## Highlights
* **Presentation Sidebar:** A new slide configuration form in the sidebar allows users to manage slide types and layouts directly, streamlining the workflow for building reactive presentations.
* **IPC Serialization Overhaul:** The transition from `pickle` to `msgspec` for internal serialization improves performance and security when transferring data between the kernel and the frontend.
* **Security & Stability Hardening:** This update includes critical fixes for cyclic data handling, non-finite float decoding in complex types, and hardened trust-bearing window globals for exported notebooks.

## Breaking Changes
None. This is a patch release focused on enhancements and bug fixes. The change in internal serialization (pickle to msgspec) is intended to be transparent to the end user.

## Priority