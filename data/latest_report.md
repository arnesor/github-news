# GitHub New Releases Report 2026-09-21

**[python-poetry/poetry 2.5.1](https://github.com/python-poetry/poetry/releases/tag/2.5.1)**

### Poetry 2.5.1 Release Summary

**Summary**  
Poetry 2.5.1 is a focused patch release addressing a package removal issue. It resolves a `TypeError` that occurred when uninstalling a package with the `installer.builtin-uninstall` setting enabled.

**Highlights**  
* Resolved a `TypeError` that caused package uninstallation to fail when `installer.builtin-uninstall` was configured ([#11077](https://github.com/python-poetry/poetry/pull/11077)).

**Breaking Changes**  
* None. This is a non-breaking bugfix release.