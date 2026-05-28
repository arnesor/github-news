# GitHub New Releases Report 2026-05-28

**[pola-rs/polars py-1.41.1](https://github.com/pola-rs/polars/releases/tag/py-1.41.1)**

Polars version 1.41.1 is a patch release focused on optimizing engine stability, resolving memory regressions, and refining query execution. This update introduces performance enhancements for unique aggregations and addresses critical bugs in Common Subexpression Elimination (CSPE) and PyArrow integrations.

### Highlights

* **CSPE Refinements (`POLARS_ALLOW_NESTED_CSPE`)**: To prevent unexpected query behavior, nested Common Subexpression Elimination (CSPE) is now opt-in via a new environment variable. Additionally, a critical bug where scan filters were dropped during CSPE filter pushdowns has been resolved.
* **Memory & Performance Improvements**: This release fixes a significant memory usage regression affecting TPCH Q22 and introduces an adaptive size dispatch (switching between hashset and radix sort) with capacity-aware resets in `agg_n_unique` for faster aggregations.
* **PyArrow and Scan Integration**: Polars now correctly post-applies residual PyArrow predicates, ensuring data integrity and accurate filtering when interfacing with PyArrow datasets.

### Breaking Changes

No breaking API changes are introduced in this patch release. However, if your workflows relied on implicit nested CSPE optimizations, you will now need to explicitly opt-in by setting the `POLARS_ALLOW_NESTED_CSPE` environment variable.