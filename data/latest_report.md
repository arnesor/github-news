# GitHub New Releases Report 2026-08-31

**[unionai-oss/pandera v0.33.0](https://github.com/unionai-oss/pandera/releases/tag/v0.33.0)**

### Summary
Pandera v0.33.0 introduces a dedicated command-line interface (CLI) for data validation, schema inference, and test data generation directly from your terminal. This release also broadens ecosystem compatibility with first-class `pyarrow.Table` schema validation, improved Narwhals backend support, and critical parser and lazy validation fixes across backends.

### Highlights
* **New Pandera CLI**: Introduced built-in CLI commands (`pandera validate`, `infer`, and `generate`) equipped with backend metadata inspection.
* **Native PyArrow Validation**: Added first-class schema validation support for `pyarrow.Table` data structures.
* **Expanded Narwhals & Typing Support**: Brought Pandas schema API parity to the Narwhals backend and added a unified, backend-neutral `FieldType[T]` typing contract.

### Breaking Changes
⚠️ **Polars Dependency Minimum Version**: The minimum supported version for the Polars backend has been increased to `polars >= 1.20.0`.