# GitHub New Releases Report 2026-11-03

**[astral-sh/uv 0.13.7](https://github.com/astral-sh/uv/releases/tag/0.13.7)**

### Summary
`uv 0.13.7` brings preview improvements to schema versioning in workspace metadata and deduplicated vulnerability reporting in `uv audit`. It also delivers several key bug fixes covering Windows handle inheritance, workspace path resolution, and TOML comment preservation.

### Highlights
- **Deduplicated Vulnerability Audits**: `uv audit` now collapses aliased OSV records into a single vulnerability entry, reducing noise in security scans.
- **Improved Windows Handle Handling**: Fixed an issue where uv's Windows trampolines could inadvertently close handles they did not inherit, improving stability across sub-processes.
- **Workspace & Project CLI Refinements**: Workspace member paths added via `uv init` or `uv add` are now treated as literal paths rather than glob patterns, alongside fixes for projects starting with numbers and inline comment preservation.

### Breaking Changes
None.