# GitHub New Releases Report 2026-04-09

**[astral-sh/uv 0.11.5](https://github.com/astral-sh/uv/releases/tag/0.11.5)**

### uv 0.11.5 Release Analysis

**Summary**
This release updates `uv` with support for the latest CPython releases and adds granular control over package index timing. It focuses on hardening the tool's error handling and improving the developer experience for auditing and project initialization.

**Highlights**
- **New Python Toolchains:** Support has been added for CPython 3.13.13, 3.14.4, and the 3.15.0a8 alpha, ensuring compatibility with the latest language developments.
- **Granular Index Control:** A new preview feature allows applying `exclude-newer` constraints to specific `[[tool.uv.index]]` entries, enabling more precise reproducible builds when managing multiple package sources.
- **Improved Error Resilience:** This version replaces a potential panic with a clean error message for TLS certificate issues and fixes a Windows-specific bug where Python junctions weren't cleared properly during uninstallation.

**Breaking Changes**
- None. (Note: A legacy documentation redirect file `PIP_COMPATIBILITY.md` was removed, but this does not affect CLI functionality).