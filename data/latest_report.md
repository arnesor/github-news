# GitHub New Releases Report 2026-08-18

**[marimo-team/marimo 0.24.0](https://github.com/marimo-team/marimo/releases/tag/0.24.0)**

### Summary
marimo 0.24.0 elevates data workflow management by adding first-class Hugging Face Hub remote storage support and visual indicators for data-bound variables. The release also introduces a unified notebook export interface, AI capabilities in the chat sidebar, and updated file browser defaults.

### Highlights
* **Hugging Face Hub Integration**: Auto-detects `huggingface_hub.HfApi` to browse datasets, models, spaces, and buckets directly from the storage sidebar, with native `hf://` file reading across Polars, pandas, and DuckDB.
* **Unified Export Dialog**: Provides a centralized, customizable modal for exporting notebooks to various target formats with format-specific configuration options.
* **AI Capabilities & Data Previews**: Adds modular tool access (such as web search) to the AI chat sidebar and introduces interactive indicator icons on variables bound to external data sources.

### ⚠️ Breaking Changes
* **`mo.ui.file_browser` default behavior**: `restrict_navigation` now defaults to `True`, preventing users from navigating outside the specified root directory unless explicitly overridden.