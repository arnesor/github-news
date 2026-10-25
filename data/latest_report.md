# GitHub New Releases Report 2026-10-25

**[unionai-oss/pandera v0.35.0](https://github.com/unionai-oss/pandera/releases/tag/v0.35.0)**

### Summary
Pandera v0.35.0 introduces native schema validation support for Apache DataFusion using both `DataFrameSchema` and class-based `DataFrameModel` interfaces. This release also delivers substantial enhancements to TensorDict validation alongside numerous serialization and backend stability fixes across Polars, Pandas, and Dask.

### Highlights
* **Apache DataFusion Support**: Validate DataFusion DataFrames directly using standard Pandera schema definitions or declarative models via the narwhals-datafusion integration.
* **Expanded TensorDict Validation**: Added support for nested keys, element-level check errors, custom field checks, and compatibility with the `@check_types` decorator.
* **Schema Serialization Improvements**: Enhanced YAML and JSON round-tripping for MultiIndex options, parametrized Polars datatypes, and default column values.

### Breaking Changes
No breaking API changes are introduced. However, note minor validation behavioral adjustments: `Check.str_length` now actively rejects conflicting length arguments, and `unique_values_eq` now ignores nulls across Polars and Ibis backends.