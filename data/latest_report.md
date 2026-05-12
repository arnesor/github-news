# GitHub New Releases Report 2026-05-12

**[marimo-team/marimo 0.23.6](https://github.com/marimo-team/marimo/releases/tag/0.23.6)**

### marimo 0.23.6 Release Summary

Marimo 0.23.6 focuses on refining the WASM/Pyodide experience with improved loading states and export options, while significantly enhancing kernel stability and AI tool integrations. This release also introduces important fixes for media rendering, Windows file path handling, and provides better feedback for kernel exit events.

#### 🚀 Highlights
*   **Enhanced WASM/Pyodide UX**: Notebooks now render a snapshot while Pyodide initializes, and the `marimo export html-wasm` command gains an `--execute` flag to enable session previews.
*   **Improved Kernel Lifecycle**: A new kernel exit classification and notification system has been implemented to help users understand exactly why a session ended.
*   **Expanded AI Integration**: Added support for "GPT-5.5" and new Weights & Biases models, alongside "unified thinking" support for Pydantic AI integrations.

#### ⚠️ Breaking Changes
*   **MarimoIslandGenerator Filenames**: Notebook filenames are now propagated through `MarimoIslandGenerator.from_file`. This is a correctness fix for island generation but may affect users who built custom logic relying on the previously missing filename metadata.

#### 🐛 Key Bug Fixes
*   **Windows Support**: Fixed issues with backslashes in inserted image URLs.
*   **Media Rendering**: Implemented remounting for `<img>` tags on source changes in `mo.Html` to prevent stale frames.
*   **Stability**: Resolved a `RecursionError` when formatting objects with `__getattr__` traps and prevented Matplotlib figure DPI from compounding on cell reruns.
*   **Virtual Files**: Added support for HTTP Range requests on virtual files, improving performance for large media assets.
---
**[pandas-dev/pandas v3.0.3](https://github.com/pandas-dev/pandas/releases/tag/v3.0.3)**

### 🐼 Pandas v3.0.3 Release Analysis

**Summary**
Pandas 3.0.3 is a targeted patch release in the 3.0.x series, specifically designed to address regressions and critical bug fixes. It is a recommended upgrade for all users currently running Pandas 3.0 to ensure environment stability and data correctness.

**Highlights**
* **Regression Fixes:** Resolves high-priority issues introduced in earlier 3.0.x versions to restore expected library behavior.
* **Stability Improvements:** Includes various bug fixes that enhance the reliability of core data structures and operations.
* **Python 3.11+ Support:** Continues the 3.0 series' commitment to modern Python environments, requiring Python 3.11 or higher.

**Breaking Changes**
* **None.** This is a patch release focused on fixes; no breaking API changes or deprecations are introduced in this version.

**Installation**
To update to the latest version, use one of the following commands:

```bash
# PyPI
python -m pip install --upgrade pandas==3.0.3

# Conda-forge
conda install -c conda-forge pandas=3.0.3
```