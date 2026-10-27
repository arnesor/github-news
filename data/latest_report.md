# GitHub New Releases Report 2026-10-27

**[astral-sh/ruff 0.17.3](https://github.com/astral-sh/ruff/releases/tag/0.17.3)**

### Summary
Ruff 0.17.3 delivers core performance optimizations to the lexer and formatter alongside a bug fix for `pyupgrade` f-string conversions. The release also introduces a new preview lint rule for detecting shared clock mocking issues.

### Highlights
- **Lexer & Formatter Speedups**: Optimized keyword and identifier lexing with specialized ASCII paths, alongside stdout buffering in `ruff format`.
- **f-string Conversion Fix (`UP032`)**: Resolved an issue in `pyupgrade` that caused incorrect automatic conversions to f-strings.
- **New Preview Rule**: Added `shared-clock-mock` under the `suspicious` ruleset to flag potentially problematic mock configurations.

### Breaking Changes
None.
---
**[astral-sh/uv 0.13.6](https://github.com/astral-sh/uv/releases/tag/0.13.6)**

### Summary
uv 0.13.6 delivers substantial performance and memory optimizations across workspace resolution, lockfile generation, and metadata parsing. It also introduces preview support for NVIDIA GPU capability detection and resolves an important directory cleanup issue during script execution.

### Highlights
- **Extensive Performance & Memory Reductions**: Substantially lowered peak memory usage when resolving, locking, or upgrading large workspaces, complemented by broad reductions in parsing overhead for PyPI metadata, build settings, and configuration files.
- **NVIDIA GPU Detection (Preview)**: Added automatic detection for NVIDIA GPU capabilities to help resolve and select compatible wheel variants using `wheel-variants`.
- **Directory Cleanup Safety Fix**: Prevented `uv run --active --script` and `uv sync --active --script` from inadvertently deleting directories that are not virtual environments.

### Breaking Changes
None.