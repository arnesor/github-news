# GitHub New Releases Report 2026-05-21

**[duckdb/duckdb v1.5.3](https://github.com/duckdb/duckdb/releases/tag/v1.5.3)**

### Summary
DuckDB v1.5.3 is a focused bugfix release resolving various stability, performance, and compatibility issues identified after the v1.5.2 release. This update notably integrates the Jemalloc allocator directly into the core engine for better memory management while delivering critical fixes for Parquet, CSV, and timezone parsing.

### Highlights
* **Jemalloc Migrated to Core:** To streamline memory management and building pipelines, Jemalloc has been moved from an extension directly into the DuckDB core engine, with options added to toggle linking and heap profiling.
* **Smart Memory flushing for Row Groups:** Introduced the `write_buffer_row_group_memory_limit` setting, allowing DuckDB to flush row groups to disk based on actual memory consumption rather than relying solely on arbitrary row counts.
* **Ecosystem & Compatibility Enhancements:** Added the `pg_catalog.pg_collation` view to support SQLAlchemy 2.0.45 reflection, patched ADBC memory leaks on error paths, and fixed SQL timezone parsing for `UTC±NN00` formats.

### Breaking Changes
No breaking SQL or API changes are introduced in this patch. However, developers packaging DuckDB or using custom build scripts should note that Jemalloc is no longer compiled as an extension but is now a core dependency, which may require minor adjustments to build configurations.