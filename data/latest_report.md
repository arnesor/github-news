# GitHub New Releases Report 2026-03-20

**[astral-sh/ruff 0.15.7](https://github.com/astral-sh/ruff/releases/tag/0.15.7)**

### Ruff 0.15.7 Release Summary
Ruff 0.15.7 focuses on refining the developer experience through improved LSP precision and enhanced diagnostic visibility in preview modes. This release also updates project metadata to PEP 639 standards and provides clearer documentation for formatting code within Markdown.

#### 🚀 Highlights
*   **Refined LSP Behavior:** The server now correctly suppresses `noqa` hovers and code actions for non-Python documents, ensuring a cleaner experience when working in polyglot environments.
*   **Visual Severity in Preview:** Preview output now explicitly displays diagnostic severity levels, allowing developers to better prioritize and triage issues during local development.
*   **Markdown Formatting Documentation:** New guides have been added to explain how to leverage Ruff’s editor features for formatting Python code snippets embedded within Markdown files.

#### ⚠️ Breaking Changes
*   None.

#### 📦 Other Notable Changes
*   **Rule Update:** `pycodestyle` (E501) now recognizes `pyrefly:` as a valid pragma comment to ignore line length limits.
*   **Compliance:** Added a company AI policy to the contributing guide and updated licensing info to follow PEP 639.
*   **Pylint:** Improved phrasing for rule `PLC0208`.
---
**[astral-sh/uv 0.10.12](https://github.com/astral-sh/uv/releases/tag/0.10.12)**

### Summary
`uv 0.10.12` expands its interpreter compatibility by adding support for legacy Python 3.6 and the latest PyPy 3.11.15 release. This version also improves CLI visibility for security auditing and refines dependency management behavior, including better comment preservation in configuration files.

### Highlights
- **Extended Python Support**: Support for Python 3.6 interpreters has been added to accommodate legacy environments, while documentation and policies have been updated to include the upcoming Python 3.15 and move Pyodide to Tier 2 support.
- **CLI & Reporting Enhancements**: The `uv version` report now includes the target triple for easier platform debugging, and the `uv audit` preview feature is now explicitly shown in the CLI help menu.
- **Improved Dependency Handling**: The tool now preserves end-of-line comments when removing dependencies and allows for more flexible configuration by supporting comma-separated values in the `--no-emit-package` flag.

### Breaking Changes
No breaking changes are identified in this release.

### Priority