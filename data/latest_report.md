# GitHub New Releases Report 2026-11-22

**[python-poetry/poetry 2.5.2](https://github.com/python-poetry/poetry/releases/tag/2.5.2)**

### Summary
Poetry 2.5.2 is a maintenance release addressing key installation and dependency-handling edge cases alongside improved error reporting. Most notably, it resolves hash validation and build order issues during `poetry install` while improving path dependency cleanups.

### Highlights
- **Sdist Hash Verification Fix**: Resolved an integrity issue where `poetry install` built a source distribution (`sdist`) before validating it against the locked hash ([#11253](https://github.com/python-poetry/poetry/pull/11253)).
- **Distribution Hash Matching**: Fixed an issue where `poetry install` rejected valid distributions even when index-provided hashes matched the locked file ([#11131](https://github.com/python-poetry/poetry/pull/11131)).
- **Resilient Path Dependency Removal**: Fixed uninstall failures for path dependencies whose local source directory had already been deleted ([#11093](https://github.com/python-poetry/poetry/pull/11093)).

### Breaking Changes
None. This is a non-breaking patch release.