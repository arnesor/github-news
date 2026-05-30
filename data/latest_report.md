# GitHub New Releases Report 2026-05-30

**[pola-rs/polars py-1.41.2](https://github.com/pola-rs/polars/releases/tag/py-1.41.2)**

### Polars `py-1.41.2` Release Summary

Polars version `1.41.2` focuses on memory optimization and engine stability, notably upgrading the core allocator to a newer version of `jemalloc` to boost performance. Additionally, this patch prevents unnecessary data materialization during column and list operations while hardening the query engine against async blocking deadlocks.

#### 🚀 Highlights

*   **Jemalloc Upgrade (#27797):** Upgraded to a new version of `jemalloc` to improve memory allocation performance, resolve underlying allocator bugs, and optimize memory overhead.
*   **Reduced Data Materialization:** Optimized several column, array, and list operations (such as `list.sample`, `array.shift`, and `ScalarColumn` splits) to avoid eager materialization of broadcast values, saving CPU cycles and memory.
*   **Async Deadlock Mitigation (#27767):** Hardened the internal engine runtime to prevent async blocking deadlocks, ensuring more robust multi-threaded performance in complex pipelines.

#### ⚠️ Breaking Changes

*   **None:** This is a patch release focused on stability and optimizations; there are no breaking changes.