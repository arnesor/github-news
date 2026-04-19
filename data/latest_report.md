# GitHub New Releases Report 2026-04-19

**[pola-rs/polars py-1.40.0](https://github.com/pola-rs/polars/releases/tag/py-1.40.0)**

Polars 1.40.0 delivers a major upgrade to the streaming engine and memory management, enabling more complex operations on datasets that exceed available RAM. This release focuses on lowering numerous expressions to streaming primitives while introducing a robust lock-free memory manager with spill-to-disk support.

### 🏆 Highlights
*   **Advanced Streaming Support:** The streaming engine now supports grouped `AsOf` joins, `over()` expressions, `cov`, `corr`, and `interpolate`, significantly reducing memory overhead for complex time-series and windowed analysis.
*   **OOC Memory Management:** A new lock-free memory manager featuring spill-to-disk capabilities and a fully Out-Of-Core (OOC) multiplexer allows Polars to handle massive workloads far exceeding physical memory.
*   **Multi-Frame Merge:** The introduction of `pl.merge_sorted` now supports operating on multiple frames at once, streamlining the unification of pre-sorted data sources.

### ⚠️ Breaking Changes & Deprecations
*   **Default Behavior Changes:** `unnest()` now targets all columns by default (previously required explicit naming), and `scan_read_lines` changed its default output column name from `"lines"` to `"line"`.
*   **Deprecation:** Support for the DataFrame interchange protocol (`__dataframe__`) is now deprecated and will be removed in a future version.
*   **API Warning:** `LazyFrame.map_batches` now defaults to no optimizations to prevent unexpected behavior with custom Python functions.