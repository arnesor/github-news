# GitHub New Releases Report 2026-07-28

**[pola-rs/polars py-1.43.1](https://github.com/pola-rs/polars/releases/tag/py-1.43.1)**

### Polars `py-1.43.1` Release Analysis

**Summary**
Polars `py-1.43.1` is a patch release focused heavily on engine correctness, SQL compliance, and stability fixes across cloud and catalog integrations. It also introduces minor boolean expression performance improvements and enables callback sinks for Polars Cloud.

**Highlights**
- **Engine & Join Stability**: Resolved undefined behavior on `first/last_non_null` with empty chunks, fixed self-join panics on Delta/Iceberg scans, and corrected slice handling in ordered joins.
- **SQL & Logic Corrections**: Addressed 3-valued logic (3VL) edge cases with SQL `NOT IN` interactions on `NULL` values and ensured `SUM`/`CORR` aggregates return `NULL` for all-null inputs.
- **Cloud & Integration Features**: Enabled callback sinks on cloud environments and fixed shared `SchemaError` issues across Delta and Iceberg table readers.

**Breaking Changes**
None.