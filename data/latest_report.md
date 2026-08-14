# GitHub New Releases Report 2026-08-14

**[astral-sh/ruff 0.16.3](https://github.com/astral-sh/ruff/releases/tag/0.16.3)**

### Summary
Ruff 0.16.3 delivers significant performance improvements across major platforms through Profile-Guided Optimization (PGO) and reduced AST memory usage. This release also resolves multiple false positives in `pylint`, expands security checks in `flake8-bandit`, and introduces a preview rule for modernizing `while` loops.

### Highlights
- **Engine Performance Upgrades**: Enabled Profile-Guided Optimization (PGO) on Linux, macOS ARM64, and Windows x86-64 release binaries, reduced `Expr` AST size to 64 bytes, and updated to mimalloc v3.
- **Improved Security & Pylint Linting**: `flake8-bandit` rules (`S602`, `S603`, `S607`, `S609`) now inspect keyword arguments, alongside fixes for string formatting (`PLE1300`, `PLE1307`) and Python 3.8 `finally` blocks.
- **New Pyupgrade Rule & CLI Links**: Introduced preview rule `UP048` (`while 1` $\rightarrow$ `while True`) and added clickable terminal hyperlinks to rule codes in `ruff check --statistics` output.

### Breaking Changes
- None.
---
**[astral-sh/uv 0.12.4](https://github.com/astral-sh/uv/releases/tag/0.12.4)**

### Summary
uv 0.12.4 introduces performance optimizations for dependency resolution and Simple API parsing, alongside enhanced network security with post-quantum TLS key exchange. The release also adds finer dependency-installation controls to `uv check` and resolves various lockfile and interpreter cache edge cases.

### Highlights
- **Performance Optimizations:** Significantly speeds up resolution across long spans of unavailable package versions via range coalescing, and accelerates Simple API parsing through direct metadata deserialization.
- **Post-Quantum TLS Support:** Upgrades network transport to prefer post-quantum key exchange and introduces opt-in TLS diagnostics for troubleshooting connections.
- **Root-less `uv check` Workflow:** Adds the `--no-install-project` flag (and `UV_NO_INSTALL_PROJECT` environment variable) to install dependencies without building or installing the root project.

### Breaking Changes
None.