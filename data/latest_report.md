# GitHub New Releases Report 2026-11-13

**[astral-sh/ruff 0.17.5](https://github.com/astral-sh/ruff/releases/tag/0.17.5)**

### Summary
Ruff 0.17.5 delivers a substantial batch of internal performance optimizations alongside stability improvements for syntax-aware autofixes. It also introduces new preview checks—including `PLE0211` and `ASYNC401`—and enhances tooling around renamed rule redirects.

### Highlights
- **Broad Performance Improvements**: Bundles nearly twenty optimization PRs targeting core analysis and linting routines to keep Ruff blazing fast.
- **Rule Management & Redirects**: Introduces `RUF202` (`renamed-rule`), rule redirection support, and expanded suppression comment checking via `RUF101` (preview).
- **Autofix & CLI Stability**: Prevents crashes when writing to closed `stderr` pipes and fixes edge cases in autofixes involving parenthesized arguments (`B010`, `PYI034`, `UP031`) and variable shadowing (`ICN001`).

### Breaking Changes
None. All rule additions and safety adjustments (such as marking `G004` fixes as unsafe) are confined to preview mode.
---
**[astral-sh/uv 0.13.8](https://github.com/astral-sh/uv/releases/tag/0.13.8)**

### Summary
uv 0.13.8 expands hardware-aware dependency management with deeper architecture and TPU detection for preview wheel variants, alongside support for CPython 3.16.0a2. It also introduces concurrency optimizations for CLI invocations and patches several resolver and credential permission issues.

### Highlights
- **Hardware-Aware Wheel Variants**: Preview wheel variant selection now detects x86-64 microarchitecture levels, AArch64 architecture versions, and Google TPUs, with new support for installing variants from local paths, direct URLs, and Git repos.
- **Concurrent Environment Deduplication**: Optimized performance by preventing duplicate virtual environment builds when parallel `uvx` or `uv run --with` processes request matching environments.
- **Resolver & Security Fixes**: Hardened Unix credential file permissions to owner-only by default and corrected edge cases around scoped overrides with recursive extras and negative extra markers.

### Breaking Changes
None.