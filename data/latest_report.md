# GitHub New Releases Report 2026-10-20

**[astral-sh/uv 0.13.3](https://github.com/astral-sh/uv/releases/tag/0.13.3)**

### Summary
`uv` version 0.13.3 is a targeted maintenance release addressing a specific performance regression. It resolves an issue where running `uv export` experienced severe slowdowns when processing dependency graphs containing package extras.

### Highlights
- **`uv export` Performance Fix**: Resolved an issue causing severe execution slowdowns when resolving dependency graphs that include extras ([#22750](https://github.com/astral-sh/uv/pull/22750)).

### Breaking Changes
- None. This release contains exclusively non-breaking performance improvements.
---
**[marimo-team/marimo 0.25.2](https://github.com/marimo-team/marimo/releases/tag/0.25.2)**

### Summary
marimo 0.25.2 introduces support for Python 3.15 alongside new GeoJSON and GeoParquet export capabilities for geospatial datasets. This release also delivers critical editor responsiveness improvements, offline WebAssembly builds, and preview architecture for host notebook integrations.

### Highlights
* **Python 3.15 Support**: Build and run reactive marimo notebooks on the latest Python release.
* **Geospatial Data Exports**: Download geospatial tables (GeoPandas, DuckDB geometry, PyArrow) as GeoJSON or GeoParquet directly from `mo.ui.table` and `mo.ui.dataframe`.
* **Editor & LSP Enhancements**: Language server diagnostics and completions now evaluate current unexecuted editor text, significantly improving inline completion responsiveness and SQL interpolation handling.

### 🚨 Breaking Changes
marimo no longer automatically applies a dark theme to **matplotlib, Plotly, Bokeh, or HoloViews** plots when the notebook is in dark mode. Plots now strictly follow the library’s native configuration. If you require dark plots, you must set the theme explicitly in your plotting code.