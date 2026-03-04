# GitHub New Releases Report 2026-03-04

**[astral-sh/uv 0.10.8](https://github.com/astral-sh/uv/releases/tag/0.10.8)**

### Summary
`uv` 0.10.8 strengthens infrastructure and security by introducing hardened Docker images with SBOM attestations and transitioning to Astral-hosted mirrors for CPython and binary downloads. The update also streamlines developer workflows with improved resolver hints, expanded build compatibility, and critical fixes for dependency exclusions.

### Highlights
* **Astral Mirror Defaults:** `uv` now fetches CPython and its own updates from Astral’s mirrors by default, providing a more reliable and controlled distribution path for core assets.
* **Enhanced Security & Containers:** New Docker images based on "Hardened Images" are now available, featuring SBOM (Software Bill of Materials) attestations to improve supply chain transparency.
* **Improved Resolution Logic:** Added smarter resolver hints when `--exclude-newer` filters out all versions and fixed bugs where `uv tool upgrade` or inline scripts ignored specified dependency exclusions.

### Breaking Changes
No breaking changes were identified in this release.

### Priority
---
**[marimo-team/marimo 0.20.3](https://github.com/marimo-team/marimo/releases/tag/0.20.3)**

### Summary
Marimo 0.20.3 introduces professional PDF slide exports and spreadsheet-style cell statistics for interactive data tables. This update also streamlines data workflows with a new storage connection UI and smarter cell previews in the dependency minimap.

### Highlights
*   **Professional PDF Slide Export:** You can now export notebooks as slide decks using `marimo export pdf --as=slides`. A new `--rasterize-outputs` flag captures interactive widgets (like Plotly and anywidgets) as static images, ensuring your interactive components are preserved in the final document.
*   **Interactive Table Statistics:** Selecting two or more cells in `mo.ui.table` or `mo.ui.dataframe` now instantly calculates count, sum, and average for numeric values. This brings familiar spreadsheet-style data exploration directly into the notebook UI.
*   **Storage & Database UI Enhancements:** This release adds a dedicated interface for storage and database connections, including a file viewer and the ability to stream virtual files. This significantly improves the experience when working with remote data sources and large datasets.

### Breaking Changes
No breaking changes were identified in this release.

### Priority
Minor