# GitHub New Releases Report 2026-11-25

**[astral-sh/uv 0.13.10](https://github.com/astral-sh/uv/releases/tag/0.13.10)**

### Summary
`uv` 0.13.10 is a security and maintenance release addressing security advisory GHSA-vjvj-3m3f-fgmm. It brings stricter validation and better diagnostics for `uv.lock`, upstream-portable lockfiles for proxy indexes, and updated managed Python runtime builds.

### Highlights
- **Security & Integrity**: Fixes GHSA-vjvj-3m3f-fgmm and introduces strict validation to ensure dependency requirements in `uv.lock` actually match locked package versions.
- **Improved `--locked` Diagnostics**: Now clearly explains *why* `uv.lock` is out of date when `--locked` rejects it, and reports dependencies with missing package entries.
- **Portable Proxy Index Lockfiles (Preview)**: Allows the use of proxy indexes while ensuring lockfiles remain portable to upstream indexes via reversible artifact URLs.

### Breaking Changes
None explicitly marked as breaking. However, teams using `uv.lock` with invalid state or corrupted wheels (mismatched ZIP data descriptors) may see builds fail as validation has been tightened to patch vulnerabilities and ensure consistency.
---
**[marimo-team/marimo 0.26.0](https://github.com/marimo-team/marimo/releases/tag/0.26.0)**

### Summary
marimo 0.26.0 introduces a unified client–server host protocol that fundamentally revamps notebook execution, client synchronization, and coding agent pairing. This release modernizes the platform's foundation, streamlines configuration resolution, and updates minimum runtime requirements.

### Highlights
* **Streamlined Coding Agent Pairing:** Native CLI tooling now allows agents (Codex, Claude Code, OpenCode) to auto-discover running notebooks. Paired agents display in the editor footer, and users can push cell code and tracebacks directly to agent chats with "Send error to agent."
* **Unified Host Protocol Architecture:** Notebook lifecycle operations—including cell runs, document sync, outputs, and session states—now operate over a standardized host protocol, enabling consistent behavior across the editor, CLI, and headless clients.
* **Lazy Table Paging & Config Tools:** Added `mo.ui.table.lazy()` to page through Polars, DuckDB, and Ibis tables without computing total row counts upfront. Configuration resolution is now deterministic, inspectable with `--show-sources`, and overridable via the `--config` CLI flag.

### 🚨 Breaking Changes
* **Python Requirement:** Python 3.11 or newer is now required (Python 3.10 support has been dropped).
* **Removed Features:** Experimental real-time collaboration (`experimental.rtc_v2`), the `marimo new <PROMPT>` command, and Codeium completion support have all been removed.
* **Default Caching Mechanism:** Caching now uses the lazy loader by default instead of pickle. Restore the previous behavior by setting `loader = "pickle"` under `[cache]` in your marimo config.
* **Dotenv Resolution:** An explicit empty list `runtime.dotenv = []` now overrides and skips project `.env` files across all config sources.
---
**[pola-rs/polars py-2.2.0](https://github.com/pola-rs/polars/releases/tag/py-2.2.0)**

### Summary
Polars `py-2.2.0` introduces out-of-core join capabilities and major memory optimization enhancements across streaming, windowing, and Parquet decoding. It also substantially expands the SQL interface with write operations, advanced window frames, and deeper integration with attached Iceberg catalogs.

### Highlights
- **Out-of-Core Joins**: The streaming equi-join build side is now fully spillable to disk, enabling memory-efficient joins over datasets that significantly exceed available RAM (#30679, #30558).
- **Major SQL & Iceberg Capabilities**: Extensive SQL engine expansion including table mutations (`INSERT`, `UPDATE`, `DELETE`, `MERGE INTO`), catalog schema evolution, compaction calls, and time-travel querying on attached Iceberg catalogs (#30958, #30633, #30751).
- **Streaming & Aggregation Optimizations**: Added parallel streaming cumulative aggregations, branchless binary searches for sorted numeric slices, and native vectorized calculations across groups and scans (#31062, #30568, #30808).

### ⚠️ Breaking Changes
- **String Offset Return Types**: `Expr.str.find(_many)` now returns character offsets instead of byte offsets. Binary byte searches should now use `Expr.bin.find(_many)` (#31026).
- **Scalar Arguments at Plan Time**: Scalar function arguments must now be known and provided at query plan time (#30914).
- **SQLContext State Mutation**: Running a SQL `DELETE` statement will now directly mutate and update the registered table within the active `SQLContext` (#30869).