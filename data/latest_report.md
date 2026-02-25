# GitHub New Releases Report 2026-02-25

**[astral-sh/uv 0.10.6](https://github.com/astral-sh/uv/releases/tag/0.10.6)**

### Summary
uv 0.10.6 is a targeted patch release focusing on improving the reliability of environment resolution and file system operations. These updates refine how the tool handles conflicting Python version requirements and ensure file integrity during installation on Linux.

### Highlights
- **Improved Python Version Selection:** Fixed logic for scripts where `requires-python` metadata conflicted with a local `.python-version` file, ensuring the correct interpreter is used.
- **Lockfile Normalization:** Enhanced the handling of fork markers within lockfiles to ensure consistent marker normalization.
- **Linux Reflink Fix:** Resolved an issue where file permissions were not preserved when using reflinks on Linux, maintaining proper security and execution bits.

### Breaking Changes
No breaking changes are introduced in this release.

### Priority: Bugfix