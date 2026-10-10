# GitHub New Releases Report 2026-10-10

**[astral-sh/ruff 0.17.0](https://github.com/astral-sh/ruff/releases/tag/0.17.0)**

### Summary
Ruff 0.17.0 introduces official code-signing and Apple notarization for release executables alongside modernized defaults for Python target versions. This release also completes the deprecation cycle of the legacy `ruff-lsp`, fully transitioning users to Ruff's native language server.

### Highlights
* **Code-Signed Binaries & Wheels**: Executables for macOS (Apple Developer ID signed and notarized) and Windows (timestamped Azure Authenticode) are now signed, reducing antivirus false positives and supporting publisher allowlisting.
* **Removal of `ruff-lsp`**: The legacy Python-based `ruff-lsp` has been completely removed in favor of the high-performance native language server integrated into Ruff.
* **Rule & Formatter Stabilizations**: Stabilized rules `TID254` (lazy import mismatch), `TID255` (lazy import resolved), and `RUF071` (`os.path.commonprefix`). Formatter and line-length rules now consistently ignore trailing pragma comments.

### Breaking Changes
⚠️ **Warning: Several breaking changes are present in this release:**
* **Target Version Bump**: Unconfigured projects now default to Python 3.11 (up from 3.10), and syntax checks without a specified version default to 3.15.
* **Default Rule Set Changes**: Multiple `flake8-datetimez` rules (`DTZ001`, `DTZ005`–`007`, `DTZ011`–`012`, `DTZ901`) are no longer enabled by default, while `F406` (nested star import syntax error) is now enabled by default.
* **Dropped `ruff-lsp`**: Editor configs explicitly relying on `ruff-lsp` or `ruff.nativeServer` must migrate to the native language server.
* **Conda-Forge Packaging**: The conda package no longer ships as a Python package; run `ruff` directly instead of `python -m ruff`.
---
**[astral-sh/uv 0.13.0](https://github.com/astral-sh/uv/releases/tag/0.13.0)**

### Summary
uv 0.13.0 transitions the default stable Python version to Python 3.15 and revamps internal cache formats to improve performance and reduce storage overhead. The release also introduces several strictness and correctness improvements across dependency constraints, CLI argument parsing, and archive handling.

### Highlights
- **Python 3.15 by Default**: Adds support for CPython 3.15.0 and defaults to it for unpinned environments and automatic downloads.
- **Native Windows ARM64 Preference**: Aligns with official CPython distributions by preferring native ARM64 (`aarch64`) interpreters over emulated `x86_64` on Windows.
- **Cache & HTTP Performance**: Revalidates cached HTTP responses faster by avoiding rewrites of unchanged payloads, while reducing memory allocations and cache storage.

### ⚠️ Breaking Changes
Several breaking changes are present in this release:
- **Default Python Target**: Unpinned commands (e.g., `uv venv`, `uv python install`) now default to Python 3.15 instead of 3.14 (opt out with `uv python pin 3.14` or `--python 3.14`).
- **Stricter Constraints Handling**: uv now enforces `--require-hashes` inside nested constraints files (missing hashes will cause failures) and explicitly rejects editable (`-e`) requirements inside constraints files.
- **CLI Path Splitting**: Arguments passed to `-c` (`--constraint`), `--override`, `--exclude`, and `--build-constraint` are no longer split on spaces. Use repeated flags for multiple files (e.g., `-c a.txt -c b.txt`).
- **Archive Validation**: Switched to `tar-codec` by default, rejecting archives with hard links or unsupported extensions (opt out with `UV_LEGACY_TAR_BACKEND=1`).
- **Build Directory Safety**: `uv build --clear` will abort if the output directory contains the build source to prevent accidental source deletion.
---
**[psf/black 26.10.1](https://github.com/psf/black/releases/tag/26.10.1)**

### Summary
Black 26.10.1 delivers an urgent security fix for Black's bundled GitHub Action alongside multiple stability and formatting improvements. This patch release resolves unexpected syntax mutations in Jupyter notebook assignment magics, refines `--line-ranges` handling, and adds flexible cache directory configuration.

### Highlights
- **GitHub Action Security Fix (GHSA-cg8m-r9f2-5wm2):** Resolves a security vulnerability in the bundled GitHub Action by rejecting URL references and unreleased versions inside `tool.black.required-version`.
- **Jupyter & Partial Formatting Fixes:** Prevents IPython assignment magics (e.g., `x = !ls -la`) from being wrapped in unrunnable parentheses, and fixes crashes and unintended formatting when using `--line-ranges`.
- **New CLI Cache Option & Performance Boost:** Adds the `--cache-dir` CLI flag, fixes `.gitignore` parsing when prefixed with a UTF-8 BOM, and resolves quadratic runtime on lines with deeply nested trailing bracket pairs.

### Breaking Changes
⚠️ **GitHub Action Version Pinning:** If your workflow specifies git URLs or arbitrary references in `tool.black.required-version`, the GitHub Action will now reject them and fail. Only officially released version specifiers are permitted.