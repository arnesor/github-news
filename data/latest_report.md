# GitHub New Releases Report 2026-07-12

**[wntrblm/nox 2026.07.11](https://github.com/wntrblm/nox/releases/tag/2026.07.11)**

## 🚀 Nox 2026.07.11 Release

### Summary
Nox release `2026.07.11` officially drops support for Python 3.9 while paving the way for the future with early support for Python 3.15. This update delivers major performance gains through intelligent caching and lazy module imports alongside key bug fixes and interpreter-resolution improvements.

### 🌟 Highlights
*   **Performance Boosts**: Experience faster runtimes with cached session-name normalization, `uv` detection, interpreter discovery, and metadata reads.
*   **Python 3.15 Support**: Added Python 3.15 to the test matrix, introducing lazy module imports to optimize performance on the upcoming Python release.
*   **Command Exit Codes**: The `CommandFailed` exception now exposes a `return_code` property, allowing developers to cleanly inspect and handle specific execution failures programmatically.

### ⚠️ Breaking Changes
*   **Dropped Python 3.9**: Nox now requires Python 3.10 or newer. Environments still running on Python 3.9 must be upgraded to run this version.