# GitHub New Releases Report 2026-10-26

**[pola-rs/polars py-2.1.0](https://github.com/pola-rs/polars/releases/tag/py-2.1.0)**

### Summary
Polars 2.1.0 delivers significant scalability upgrades with comprehensive out-of-core (OOC) streaming memory management improvements and deep Iceberg catalog integration. The release also adds support for encrypted Parquet read/write while introducing stricter typing rules for mixed arithmetic.

### Highlights
- **Streaming & Out-of-Core (OOC) Overhaul**: Drastically lowers memory pressure via immediate OS memory return during spills, spill-aware file readers, and OOC group-by operations with shuffles.
- **Expanded Iceberg & SQL Capabilities**: Added Iceberg catalog attachment to `SQLContext` with `CREATE`/`DROP TABLE` support, dynamic partition overwrites via `sink_iceberg`, and SQL recursive CTEs (`WITH RECURSIVE`).
- **Encrypted Parquet & Masked NumPy**: Added native read and write support for encrypted Parquet files, experimental GeoParquet, and conversion utilities to/from masked NumPy arrays.

### ⚠️ Breaking Changes
- **Mixed Arithmetic Disallowed**: Mixed string <=> numeric arithmetic is no longer permitted in eager operations (#30071).
- **Python 3.10 Deprecated**: Support for Python 3.10 has been officially dropped in build pipelines (#29888).