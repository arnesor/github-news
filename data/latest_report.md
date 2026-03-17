# GitHub New Releases Report 2026-03-17

**[astral-sh/uv 0.10.11](https://github.com/astral-sh/uv/releases/tag/0.10.11)**

### Summary
uv 0.10.11 focuses on refining project management flexibility and improving metadata handling for both internal processes and external tools like Ruff. This patch release also addresses macOS-specific interpreter discovery and optimizes internal distribution ID performance.

### Highlights
* **Flexible `--project` Flag**: The `--project` flag now allows direct references to `pyproject.toml` files and provides a warning instead of a hard error when pointing to other file types.
* **macOS Interpreter Discovery**: Improved Python interpreter querying on macOS by disabling `SYSTEM_VERSION_COMPAT`, ensuring more accurate version detection in legacy-compatibility environments.
* **Metadata & Performance**: Enhancements include fetching Ruff release metadata from an Astral mirror for better reliability and optimized distribution ID performance for faster dependency resolution.

### Breaking Changes
No breaking changes were introduced in this release.

### Priority
---
**[marimo-team/marimo 0.21.0](https://github.com/marimo-team/marimo/releases/tag/0.21.0)**

### Summary
Marimo 0.21.0 introduces a major architecture update for interactive Matplotlib and adds native export functionality to the Jupyter `.ipynb` format. This release also enhances the developer experience with refined reactive components, improved cache controls, and new authentication options for Snowflake.

### Highlights
*   **Built-in Interactive Matplotlib:** `mo.mpl.interactive()` has been rewritten to use marimo's internal communication channel. This removes the need for background threads or separate server processes, making interactive plots more stable and performant.
*   **Native Jupyter Export:** You can now export marimo notebooks as `.ipynb` files directly from the editor's download menu. Exported files maintain visual cell order and include captured outputs for better interoperability with the wider data science ecosystem.
*   **Enhanced Data & UI Tooling:** This update adds reactive histogram selection support, Snowflake authentication options in the UI, and Ruff configuration discovery for automatic notebook cell formatting.

### 🚨 Breaking Changes
*   **Altair Chart Scaling:** Altair charts no longer default to `width: "container"`. This change prevents aspect ratio distortion and ensures charts match the official Altair documentation defaults. To fill the container width, you must now explicitly set `width="container"` in your chart specification.
---
**[unionai-oss/pandera v0.30.0](https://github.com/unionai-oss/pandera/releases/tag/v0.30.0)**

# 📦 Pandera v0.30.0 Release Summary

### Summary
Pandera v0.30.0 officially introduces support for Pandas 3.0, ensuring compatibility with the latest evolution of the Python data ecosystem. This release also focuses on performance optimizations for `DataFrameModel` and expands feature parity for Polars users.

### Highlights
* **Pandas 3.0 Support:** Full compatibility with Pandas 3.0, including a transition to using pandas-native strings by default to leverage modern memory efficiencies.
* **Polars Enhancements:** Added `PydanticModel` support for the Polars backend and improved error reporting for regex-based column validation.
* **Performance Optimizations:** Refactored `DataFrameModel` to eliminate expensive deep copy operations during empty DataFrame creation, resulting in faster schema initializations.

### Breaking Changes
⚠️ **Behavioral Changes:**
* Under Pandas 3.0, the default string type now maps to pandas-native strings. 
* The vestigial `ordering` parameter has been removed from Polars `Categorical` schemas.
* `geopandas` has been unpinned, which may lead to version shifts in your environment if not explicitly managed.

### What's Changed
* **Fixes:** Resolved issues in optional nested validation, custom parsers, and built-in checks when dropping invalid rows.
* **Maintenance:** Replaced `pre-commit` with `prek` for internal linting and fixed various documentation references.
* **Documentation:** Added `AGENTS.md` to provide better context for AI-assisted development and tool usage.