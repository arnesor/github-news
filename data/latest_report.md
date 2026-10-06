# GitHub New Releases Report 2026-10-06

**[narwhals-dev/narwhals v2.27.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.27.0)**

### Summary
Narwhals v2.27.0 introduces key functionality enhancements including frame-level schema casting and expanded `list.contains` backend compatibility. This release also ships dozens of consistency improvements and bug fixes across pandas, PyArrow, Dask, DuckDB, and Polars backends.

### Highlights
* **Frame-level `.cast()` Support**: Added `{DataFrame, LazyFrame}.cast` to streamline schema casting across entire frames without needing manual expression loops (#3815, #4016).
* **Expanded `list.contains`**: Added `list.contains` support for PyArrow, pandas, and Dask, while aligning lazy backend null-handling with Polars behavior (#4001, #3996).
* **File-like Object I/O**: `{read,scan}_*` methods now support file-like objects (such as `io.BytesIO` and `io.StringIO`), improving in-memory workflows (#3956).

### Breaking Changes
None. Note that validation has been tightened across backends to match Polars conventions: operations like `str.slice` with negative lengths, `str.zfill` with negative widths, and duplicate `struct` field names now consistently raise errors instead of returning undefined backend-specific results.
---
**[unionai-oss/pandera v0.34.0](https://github.com/unionai-oss/pandera/releases/tag/v0.34.0)**

### Summary
Pandera v0.34.0 introduces native validation support for PyTorch `TensorDict` alongside nested `DataFrameModel` validation for Polars workflows. This release also tightens validation behavior across backends, eliminating silent failures in integer coercion, parser configurations, and schema serialization.

### Highlights
* **PyTorch `TensorDict` Backend**: Added dedicated `TensorDictSchema` and `TensorDictModel` classes to validate tensor shapes, PyTorch dtypes, and batch sizes for machine learning and reinforcement learning pipelines.
* **Nested Polars Models**: Introduced support for validating nested `DataFrameModel` schemas within the Polars backend.
* **Safer Coercion & Check Validation**: Integer coercion now halts on overflow instead of wrapping silently, Polars fails loudly when user-declared parsers are provided instead of skipping them, and `Check.str_length` explicitly rejects reversed bounds.

### Breaking Changes
No intentional breaking API changes are introduced. However, behavioral tightening—such as raising errors on integer coercion overflow and rejecting invalid bounds in `Check.str_length`—may cause previously unnoticed invalid states to fail loudly.