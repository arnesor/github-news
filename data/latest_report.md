# GitHub New Releases Report 2026-02-18

**[astral-sh/uv 0.10.4](https://github.com/astral-sh/uv/releases/tag/0.10.4)**

# uv 0.10.4 Release Notes

### Summary
uv 0.10.4 is a maintenance update focused on resolving regressions and improving the reliability of workspace discovery. This release specifically addresses file-locking issues on network-mounted filesystems (NFS) and fixes a potential panic during project initialization.

### Highlights
* **NFS Compatibility Restore**: Reverted a recent change to file locking that caused issues on NFS mounts, ensuring stable operation for users working in networked environments.
* **Refined Workspace Discovery**: `uv` now skips workspace members that only contain git-ignored files, preventing unnecessary processing of ignored directories and sub-directories.
* **Build Backend Fixes**: Corrected file permissions for `wheel` and `sdist` artifacts produced by the `uv_build` backend to ensure proper distribution and installation.

### Breaking Changes
None.
---
**[pandas-dev/pandas v3.0.1](https://github.com/pandas-dev/pandas/releases/tag/v3.0.1)**

### Pandas v3.0.1 Release Analysis

#### Summary
Pandas 3.0.1 is a maintenance patch in the 3.0.x series, primarily delivering critical regression fixes and bug resolutions. It is a highly recommended upgrade for all users currently on version 3.0.0 to ensure stability and performance.

#### Highlights
* **Regression Fixes**: Addresses specific issues introduced in the major 3.0.0 release to restore expected behavior in core workflows.
* **Bug Fixes**: Includes various stability improvements and patches for bugs identified since the last major rollout.
* **Modern Python Support**: Reaffirms the version's commitment to modern infrastructure, requiring Python 3.11 or higher.

#### Breaking Changes
None. As a patch release, v3.0.1 focuses on stability and does not introduce intentional breaking changes. However, users upgrading from the 2.x series should remember that Python 3.11+ is now strictly required.

#### Priority
Bugfix