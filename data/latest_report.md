# GitHub New Releases Report 2026-04-01

**[marimo-team/marimo 0.22.0](https://github.com/marimo-team/marimo/releases/tag/0.22.0)**

Marimo 0.22.0 introduces a unified Table Explorer and reliability fixes for the programmatic notebook API to power the new `marimo-pair` AI agent skill. This release also features significant performance gains in persistent caching, smarter data table formatting, and a standard approach to cache directory management.

### ⭐ Highlights
- **Unified Table Explorer:** Row viewing and column exploration are now merged into a single tabbed pane with persistent state, streamlining data discovery within the UI.
- **AI Pair Programming:** Reliability fixes for the experimental `_code` API enable the [marimo-pair](https://github.com/marimo-team/marimo-pair) agent skill, allowing for more robust agentic notebook editing.
- **Performance & Data Scaling:** `mo.persistent_cache` now supports parallel read/writes, while data tables now utilize virtualization when pagination is disabled to handle large datasets smoothly.

### 🚨 Breaking Changes
- **`mo.image` uint8 handling:** `uint8` arrays are no longer normalized to `[0, 1]` float range automatically; they now render in the `[0, 255]` range. Use `vmin=0, vmax=1` explicitly to restore the previous behavior.
- **Cache Location & Format:** The `__marimo__` directory now follows `sys.pycache_prefix`, and the internal cache version has been bumped. **Existing caches will be invalidated and can be safely deleted.**

### ✨ Key Enhancements
* **SQL Improvements:** Enhanced SQLAlchemy engine with safe execution and inspector methods for Snowflake, plus lazy schema fetching in the datasource panel.
* **CLI UX:** Added a contextual startup tips system to the CLI.
* **Formatting:** Numeric columns are now auto-right-aligned with normalized decimal formatting for better readability.