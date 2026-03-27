# GitHub New Releases Report 2026-03-27

**[astral-sh/ruff 0.15.8](https://github.com/astral-sh/ruff/releases/tag/0.15.8)**

### Ruff 0.15.8 Release Summary

Ruff 0.15.8 introduces three new internal rules in preview and provides early support for Python 3.15's `frozendict`. This update also delivers performance optimizations for diagnostic rendering alongside several bug fixes across the plugin ecosystem.

#### 🚀 Highlights
*   **New Preview Rules:** Three new lint rules are now available: `unnecessary-if` (`RUF050`), `useless-finally` (`RUF072`), and `f-string-percent-format` (`RUF073`), which warns against using the `%` operator on f-strings.
*   **Performance Improvements:** Speed optimizations have been applied to diagnostic rendering, ensuring a snappier experience during linting and IDE integration.
*   **Python 3.15 Readiness:** Ruff now recognizes `frozendict` as a built-in for projects targeting Python 3.15 and later.

#### ⚠️ Breaking Changes
*   None reported in this version.

#### 🛠️ Key Bug Fixes & Improvements
*   **Rule Refinements:** Fixed false positives/negatives in `S607` (partial paths), `F821` (conditionally deleted variables), and `SLF001` (private member access involving `Self` annotations).
*   **IPython Support:** Improved parsing for IPython assignment expressions involving the `%foo?` syntax.
*   **Code Formatter:** Nested pragma comments are now excluded from line width calculations, preventing unexpected line breaks in `E501` and `W505`.
*   **Dependency Graph:** The `analyze graph` command now correctly resolves string imports that reference specific attributes rather than just modules.
---
**[astral-sh/uv 0.11.2](https://github.com/astral-sh/uv/releases/tag/0.11.2)**

### uv 0.11.2 Release Analysis

`uv 0.11.2` focuses on hardening the self-update mechanism and optimizing internal project parsing for faster execution. This release also refines the package auditing preview feature and improves the developer experience for Windows users through better error reporting.

#### 🌟 Highlights
*   **Robust Self-Updates**: The `uv self update` command is now more reliable, prioritizing mirrors for manifest fetching, utilizing the internal `reqwest` client, and ensuring success/failure visibility even when using the `--quiet` flag.
*   **Enhanced Package Auditing**: The preview auditing functionality now correctly evaluates optional extras and dependency groups, providing a more comprehensive security assessment of your project's dependency tree.
*   **`uv run` Performance**: A bug fix eliminates redundant project configuration parsing during `uv run` invocations, leading to snappier execution times for local scripts and tools.

#### ⚠️ Breaking Changes
*   None. This is a stable patch release focused on enhancements and bug fixes.

#### 📦 How to Update
Update `uv` to the latest version using the built-in update command:
```sh
uv self update
```