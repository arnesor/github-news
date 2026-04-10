# GitHub New Releases Report 2026-04-10

**[astral-sh/ruff 0.15.10](https://github.com/astral-sh/ruff/releases/tag/0.15.10)**

Ruff 0.15.10 focuses on refining Python 3.12 compatibility and improving the stability of linting rules across various Python versions. This release also introduces custom file extension support for the Ruff server, enhancing its flexibility in specialized development environments.

### Highlights

*   **Improved F-String Validation**: The formatter and fixers now strictly avoid emitting multi-line f-string elements for Python targets older than 3.12, preventing potential syntax errors in legacy environments.
*   **Server Custom Extensions**: The Ruff server now supports custom file extensions, allowing developers to apply linting and formatting to files that do not use the standard `.py` or `.pyi` extensions.
*   **Stability & Rule Fixes**: This version resolves a panic in `pyupgrade` (`UP012`) and improves the robustness of several rules, including better handling of non-self-named variables in `flake8-self` (`SLF`) and closures in `flake8-logging`.

### Breaking Changes

No breaking changes were introduced in this release.
---
**[astral-sh/uv 0.11.6](https://github.com/astral-sh/uv/releases/tag/0.11.6)**

### uv 0.11.6 Release Analysis

### Summary
This release primarily addresses a low-severity security vulnerability where malformed wheel `RECORD` entries could lead to arbitrary file deletion during the uninstallation process. It also introduces critical fixes for virtual environment file protection and path normalization issues on Windows.

### Highlights
- **Security Fix (GHSA-pjjw-68hj-v9mw):** Prevents `uv` from removing files outside of the virtual environment during uninstallation, closing a loophole where malicious wheels could trigger arbitrary file deletion.
- **Wheel RECORD Integrity:** Added logic to validate and "heal" wheel `RECORD` files during installation, ensuring that package metadata is accurate and safe for future operations.
- **Windows Cache Management:** Fixed a bug in `uv cache clean` that caused errors on Windows due to improper Win32 path normalization.

### Breaking Changes
None. This is a patch release focused on security and stability.
---
**[marimo-team/marimo 0.23.0](https://github.com/marimo-team/marimo/releases/tag/0.23.0)**

### marimo 0.23.0

Marimo 0.23.0 is a critical update that addresses a high-severity security vulnerability (CVE-2026-39987) involving unauthenticated remote code execution. Alongside this essential hardening, the release introduces reactive selection support for new Plotly chart types and several quality-of-life improvements for data filtering and the AI chat interface.

#### Highlights
* **Critical Security Patch:** Authenticates the `/terminal/ws` endpoint to prevent unauthenticated users from executing code remotely. This is vital for users exposing editable notebooks to shared networks or the public internet.
* **Reactive Plotly Charts:** Added reactive selection support for **violin plots** and **area charts**, allowing these visualizations to dynamically trigger updates in downstream notebook cells.
* **Improved Data Handling:** Resolved an issue with table filtering for `NaN` values in pandas string columns and refined the AI chat experience by ensuring the `Tab` key indents code rather than triggering autocomplete.

#### Breaking Changes
* **None.** While terminal access now strictly requires authentication, this is a security hardening measure and does not alter the public API or notebook functionality.