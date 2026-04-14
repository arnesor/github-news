# GitHub New Releases Report 2026-04-14

**[duckdb/duckdb v1.5.2](https://github.com/duckdb/duckdb/releases/tag/v1.5.2)**

DuckDB v1.5.2 is a maintenance release focused on stabilizing the v1.5 series through critical bug fixes, backports from the v1.4 branch, and performance optimizations. It addresses several edge cases in the CSV reader, Parquet writer, and window function engine while updating core cloud and database extensions.

### Highlights
* **Parquet & Variant Improvements:** Added support for Snowflake-produced shredded `VARIANT` Parquet files and enabled shredding for unsigned types during Parquet writes, significantly improving interoperability.
* **Stability & Memory Fixes:** Resolved a memory leak occurring during `PreparedStatement` reuse, fixed multiple integer overflow scenarios in storage decoding and list resizing, and patched data races in ADBC.
* **Advanced Query Engine Polishing:** Delivered critical fixes for `AsOf` joins, `TopN` window elimination, and CSV buffer-boundary handling to ensure correctness in complex analytical workloads.

### Breaking Changes
* **Storage Version Bump:** The internal storage version has been updated to `v1.5.2`; while generally compatible within the v1.x series, users should ensure all environments are updated.
* **Catalog OIDs:** Internal Object Identifiers (OIDs) now start at 20,000 to prevent collisions with reserved ranges, which may affect scripts relying on specific hardcoded system OIDs.
* **Geometry Persistance:** Changed behavior to warn instead of error when trying to persist geometry columns with CRS in older storage formats.

### Priority: Bugfix
---
**[unionai-oss/pandera v0.31.0](https://github.com/unionai-oss/pandera/releases/tag/v0.31.0)**

### Summary
Pandera v0.31.0 introduces comprehensive validation support for multidimensional and geospatial data through new `xarray` and `geopandas` integrations. This update significantly expands the library's utility for scientific and GIS workflows while delivering key performance improvements and bug fixes across Polars, PySpark, and Ibis backends.

### Highlights
*   **Full `xarray` Support:** Developers can now validate multidimensional datasets using the object-based `DatasetSchema` or the class-based `DatasetModel` API, including support for data variables, coordinates, and dimensions.
*   **First-class `geopandas` Integration:** This release adds native `GeoDataFrameSchema` and `GeoDataFrameModel` APIs, providing a streamlined way to enforce schemas on geospatial data.
*   **Direct Model Serialization:** `DatasetModel` and `DataFrameModel` classes can now be serialized directly, simplifying schema persistence and portability across different data backends.

### Breaking Changes
No explicit breaking changes are reported in this release. However, developers using `strict` and `ordered` schema configurations should note fixes to schema error handling, and those using `check_types` should be aware of internal fixes regarding inplace mutation behavior.

### Priority: Minor