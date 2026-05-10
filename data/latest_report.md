# GitHub New Releases Report 2026-05-10

**[python-poetry/poetry 2.4.1](https://github.com/python-poetry/poetry/releases/tag/2.4.1)**

### Summary
Poetry 2.4.1 is a maintenance patch that resolves a regression affecting the update command for transitive dependencies. It also adjusts dependency constraints to restore compatibility with specific versions of the internal installer component.

### Highlights
- **Fixed Transitive Updates:** Resolved an issue where running `poetry update <package>` would fail if the specified package was a transitive dependency rather than a direct one.
- **Installer Compatibility:** Updated dependency constraints to re-allow `installer==0.7.0`, ensuring smoother installations across different environments.

### Breaking Changes
- None. This is a targeted patch release focused on stability and bug fixes.

### Priority
Bugfix