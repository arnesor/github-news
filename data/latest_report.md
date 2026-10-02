# GitHub New Releases Report 2026-10-02

**[astral-sh/ruff 0.16.10](https://github.com/astral-sh/ruff/releases/tag/0.16.10)**

### Summary
Ruff 0.16.10 delivers memory optimizations for diagnostics alongside enhanced language server security for untrusted workspaces. This release also introduces an experimental `pyupgrade` rule for context manager iterator annotations and documents support for Python 3.15.

### Highlights
* **Untrusted Workspace Hardening:** The language server now avoids running `uv format` in untrusted workspaces to prevent unintended execution in unfamiliar projects.
* **Reduced Diagnostic Memory:** Optimized diagnostic storage reduces overall memory consumption during large-scale linting runs.
* **New Preview Rule (`UP052`):** Introduced a `pyupgrade` rule to modernize type annotations for context manager iterators.

### Breaking Changes
None. This is a backwards-compatible patch release.
---
**[astral-sh/uv 0.12.22](https://github.com/astral-sh/uv/releases/tag/0.12.22)**

### Summary
uv `0.12.22` introduces support for the latest CPython patch versions, enhances workspace lockfile tracking, and adds new architecture-level Python selection controls. It also optimizes the binary size through metadata compression and resolves several workspace synchronization bugs.

### Highlights
- **Workspace Lockfile Improvements**: Lockfiles now record default groups and dependency-group Python requirements for workspace members and non-project roots, preventing inconsistencies during frozen syncs.
- **Independent Architecture Selection (`UV_PYTHON_ARCH`)**: Added the `UV_PYTHON_ARCH` environment variable, enabling users to request a specific interpreter architecture (such as x86 vs. ARM) independently of the Python version.
- **Binary Footprint Reduction & Python Support**: Compressed embedded Python download metadata to trim the overall binary size, alongside adding support for new CPython point releases (3.10.22, 3.11.17, 3.12.15, 3.13.16, and 3.14.8).

### Breaking Changes
None.
---
**[marimo-team/marimo 0.25.1](https://github.com/marimo-team/marimo/releases/tag/0.25.1)**

### Summary
Marimo 0.25.1 delivers key security and stability improvements alongside enhancements to caching inspection and local AI agent pairing. This patch release also hardens sandboxed notebook environments and refines UI component behaviors.

### Highlights
* **Cache Management & Visibility**: Introduced `cache size` and `cache dir` commands, along with per-notebook manifest tracking for cached entries.
* **Security & Privacy Hardening**: Ensured `getpass` inputs are excluded from saved console outputs, secured language server WebSocket listeners, and improved sandbox isolation.
* **Kernel Stability**: Made the kernel `SIGINT` handler reentrancy-safe and improved cell-matching optimization logic.

### Breaking Changes
None reported in this release.