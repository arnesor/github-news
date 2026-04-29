# GitHub New Releases Report 2026-04-29

**[marimo-team/marimo 0.23.4](https://github.com/marimo-team/marimo/releases/tag/0.23.4)**

### marimo v0.23.4

**Summary**
Marimo v0.23.4 focuses on refining the user experience with new interactive filtering components and improved data visualization support. This patch also addresses critical backend stability issues, including platform detection for WASM environments and security updates for dependencies.

**Highlights**
* **Enhanced Visualization Support:** Updated types and snapshots for Altair v6.1.0 and Vega-Lite v6.4.1 to ensure seamless compatibility with the latest plotting features.
* **Interactive Filtering UI:** Introduced editable filter pills and standardized "top K" filter components, providing a more intuitive and consistent interface for data exploration.
* **Backend & WASM Reliability:** Resolved issues with Pyodide platform detection, improved Starlette encoding using `msgspec`, and added support for DuckDB `INET` extension types.

**Breaking Changes**
* No breaking changes are introduced in this release.

**Priority**
Bugfix