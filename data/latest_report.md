# GitHub New Releases Report 2026-09-06

**[python-poetry/poetry 2.4.3](https://github.com/python-poetry/poetry/releases/tag/2.4.3)**

### Poetry 2.4.3 Release Overview

**Summary**
Poetry 2.4.3 is a targeted patch release addressing an archive extraction failure affecting specific Python runtimes. It restores the ability to properly extract source distributions (sdists) on select patch releases of Python 3.10 and 3.11.

**Highlights**
- Fixed an issue preventing sdist extraction on Python versions 3.10.0–3.10.12 and 3.11.0–3.11.4 ([#11037](https://github.com/python-poetry/poetry/pull/11037)).

**Breaking Changes**
None.