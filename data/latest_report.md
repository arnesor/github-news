# GitHub New Releases Report 2026-07-24

**[astral-sh/ruff 0.16.0](https://github.com/astral-sh/ruff/releases/tag/0.16.0)**

### Summary
Ruff 0.16.0 significantly expands its default linter footprint by enabling 413 rules out of the box and adding automatic Python formatting inside Markdown files. This update also introduces native `ruff: ignore` comment support, richer CLI diffs, and CI output formatting.

### Highlights
- **Markdown Code Block Formatting**: Ruff now automatically formats Python code snippets embedded within Markdown files by default.
- **Native Comment Suppressions**: Supports `# ruff: ignore[RULE]` inline or on preceding lines as an alternative to `# noqa`.
- **Improved CI & Diff Tooling**: Fixes and diffs are now shown directly in `check` and `format --check`, alongside support for `--output-format github` / `gitlab` annotations.

### Breaking Changes
⚠️ **Action Required**:
- **Default Rules Expanded**: Default enabled rules increased drastically from 59 to 413. Review your configuration if you prefer minimal defaults.
- **Markdown Formatting Active by Default**: `ruff format` will now format Python blocks inside `.md` files by default.
- **JSON Output Nullability**: Fields like `filename`, `location`, and `end_location` in JSON output can now be `null` instead of defaulting to empty strings or row 1, column 1.
---
**[astral-sh/uv 0.11.32](https://github.com/astral-sh/uv/releases/tag/0.11.32)**

## uv 0.11.32 Release Overview

### Summary
`uv` version 0.11.32 introduces stricter canonical lockfile enforcement, targeted package filtering for `uv check`, and improved upgrades across multi-marker package declarations. It also optimizes dependency-group conflict resolution performance and fixes a edge case in universal resolution python requirement discovery.

### Highlights
- **Strict Lockfile Formatting:** `uv lock --check` and commands using `--locked` now reject non-canonically formatted lockfiles. You can automatically fix these using `uv lock --refresh`.
- **Targeted Package Checks:** Added `--package` and `--all-packages` flags to `uv check` for granular workspace package validation.
- **Improved Multi-Marker Upgrades:** `uv upgrade` now supports updating multiple marker-specific declarations of the same package simultaneously.

### Breaking Changes
**None.** However, note that CI pipelines using `--locked` or `uv lock --check` will now reject lockfiles that are not canonically formatted. Regenerate affected lockfiles using `uv lock --refresh`.
---
**[marimo-team/marimo 0.23.15](https://github.com/marimo-team/marimo/releases/tag/0.23.15)**

## Marimo 0.23.15 Release Summary

### Summary
Marimo version 0.23.15 delivers a broad collection of stability improvements, security updates, and UX enhancements across data handling, AI tooling, and rendering. This patch release addresses data editor column corruption, improves agent session routing, and introduces streaming file downloads directly from disk.

### Highlights
* **Data Integrity & Visualization Fixes:** Resolved `data_editor` corruption on `int8`/`uint8`/`float16` columns, switched pandas serialization to Arrow IPC, and restored retina rendering for Matplotlib figures.
* **AI & Agent Session Upgrades:** Added precise session targeting so AI agents reliably connect to the correct active notebook, queued follow-up messages while the assistant streams, and updated the LLM model catalog.
* **File Management & Diagnostics:** Enabled streaming file-browser downloads directly from disk, added searchable comboboxes for secrets/environment variables, and introduced previewable diagnostics in feedback modals.

### Breaking Changes
None. This is a non-breaking patch release.