# GitHub New Releases Report 2026-08-02

**[pola-rs/polars py-1.43.2](https://github.com/pola-rs/polars/releases/tag/py-1.43.2)**

### Polars `py-1.43.2` Release Summary

**Summary**
Polars `py-1.43.2` is a patch release focusing heavily on query optimization fixes, Parquet/Iceberg metadata correctness, and Arrow C interop stability. It also introduces performance tweaks like `len()` pushdown for concatenated inputs and new controls for multi-file CSV schema inference.

**Highlights**
- **Multi-File CSV Schema Inference**: Added the `infer_schema_files` parameter to `scan_csv` for more reliable schema detection across file sets.
- **Join & Execution Bug Fixes**: Resolved multiple edge cases with slice pushdowns into joins, sortedness flags, and high blocking thread usage in `sink_parquet`.
- **Parquet, Iceberg & Arrow Correctness**: Fixed Parquet field IDs for Enums and Categoricals, Iceberg column mapping metadata, and Arrow C interop binview offset calculations.

**Breaking Changes**
No breaking changes. However, this release introduces deprecation warnings when casting `Categorical` columns to integer dtypes and when calling `show_graph()` without specifying `plan_stage`.