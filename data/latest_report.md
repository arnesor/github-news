# GitHub New Releases Report 2026-04-11

**[marimo-team/marimo 0.23.1](https://github.com/marimo-team/marimo/releases/tag/0.23.1)**

### Summary
marimo 0.23.1 introduces a visual navigation minimap for slide mode and restores full functionality to marimo islands and the Quarto extension. This patch also prioritizes platform security with a comprehensive suite of hardening fixes, including input sanitization and path traversal prevention.

### ⭐ Highlights
* **Slides Minimap:** Slide mode now features a performance-optimized, scrollable panel providing a scaled-down view of cells with support for click-to-navigate and drag-to-reorder functionality.
* **Islands & Quarto Revival:** Critical bug fixes to "marimo islands" restore the ability to embed interactive Python outputs in external HTML and bring the `quarto-marimo` extension back into full compatibility.
* **Security Hardening:** This release includes a robust set of security improvements, specifically targeting script injection in plugin slots, directory traversal via symlinks, and open redirect vulnerabilities.

### ⚠️ Breaking Changes
None. This is a quality-of-life and security-focused patch release.

### 🛠️ Other Notable Changes
* **New Lint Rule:** Added a rule to detect ordering discrepancies in top-level functions.
* **UI Fixes:** Improved `mo.ui.matplotlib` rendering on browser zoom and fixed mixed-type column sorting in data tables.
* **Dependency Updates:** Updated Ruff to version 0.15.9 and bumped the target version to Python 3.10.
---
**[wntrblm/nox 2026.04.10](https://github.com/wntrblm/nox/releases/tag/2026.04.10)**

### Summary
Nox 2026.04.10 introduces automated virtual environment recovery and enhanced session documentation while modernizing its core by dropping Python 3.8 support. This release also streamlines repository management by automatically handling `.gitignore` for the `.nox` directory and refining how tags select sessions.

### Highlights
* **Self-Healing Virtualenvs:** Nox now automatically detects broken symlinks within virtual environments (common after a system Python upgrade) and recreates them, preventing cryptic execution errors.
* **New `--usage` Command:** Developers can now access full docstrings for specific sessions directly from the CLI using `nox --usage <session>`, making complex configurations easier to navigate.
* **Automatic Git Ignore:** The `.nox` directory now automatically includes a `.gitignore` file and `CACHEDIR.TAG`, ensuring local build artifacts stay out of version control without manual setup.

### Breaking Changes
* **Python 3.8 Dropped:** Support for Python 3.8 has been officially removed. You must use Python 3.9 or newer to run Nox.
* **Tag Selection Logic:** The `-t` (tags) and `-k` (keywords) flags now select from all available sessions, ignoring `default=False` settings. This may cause sessions to run that were previously excluded by default.