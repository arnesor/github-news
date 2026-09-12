# GitHub New Releases Report 2026-09-12

**[marimo-team/marimo 0.24.2](https://github.com/marimo-team/marimo/releases/tag/0.24.2)**

### Summary
marimo 0.24.2 is a patch release delivering targeted bug fixes and minor UI improvements to enhance notebook execution and readability. This update ensures consistent file storage metadata display, resolves DuckDB string alias compatibility issues, and improves layout flexibility for Markdown content.

### Highlights
* **Markdown Display Flexibility**: Removed the arbitrary prose width cap on Markdown elements, allowing text to better utilize available screen real estate.
* **DuckDB SQL Compatibility**: Added support for MSSQL string type aliases within DuckDB queries, preventing unexpected parsing errors.
* **Execution & Metadata Fixes**: Fixed cell lifecycle handling to properly finalize cells after post-execution hook interrupts, and enabled persistent visibility for file storage metadata.

### Breaking Changes
None. This is a backwards-compatible patch release.