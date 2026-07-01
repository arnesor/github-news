# GitHub New Releases Report 2026-07-01

**[astral-sh/uv 0.11.26](https://github.com/astral-sh/uv/releases/tag/0.11.26)**

### Summary
The uv 0.11.26 release focuses primarily on performance optimizations to the PubGrub dependency resolver to speed up package resolution and installation pipelines. It also introduces a safety warning to prevent potential build issues when the build cache is misconfigured.

### Highlights
* **PubGrub Resolver Speedups**: Enhances dependency resolution speed by adapting uv to IDs-only PubGrub dependencies and reusing resolver work across solver iterations.
* **Memory & Search Optimizations**: Speeds up candidate selection for disjoint ranges and eliminates unnecessary allocations in `ForkMap::contains` to reduce overhead during resolution.
* **Build Cache Warning**: Adds a helpful warning when the build cache is located inside the source directory, helping developers avoid recursive build issues or cache pollution.

### Breaking Changes
None. This is a fully backward-compatible patch release.
---
**[pola-rs/polars py-1.42.1](https://github.com/pola-rs/polars/releases/tag/py-1.42.1)**

### Summary
Polars version `py-1.42.1` is a patch release focusing on engine stability through critical bug and panic fixes, notably resolving edge-case issues in temporal extraction and projection pushdowns. Additionally, this release introduces targeted performance optimizations for Parquet metadata resolution and small-datatype summation, alongside a key deprecation in `pl.concat`.

### Highlights
* **Optimized Parquet & I/O Performance**: Added a sampled resolve mode for multi-file Parquet metadata (#28111) and made path expansion non-blocking (#28073) to accelerate multi-file processing.
* **Engine Stability & Panic Fixes**: Resolved multiple panic conditions, including crashes during temporal extraction on datetime columns with nulls (#28054), projection pushdowns on `select(len())` (#28108), and `replace` operations involving expressions or object dtypes (#27433).
* **Faster Small-Dtype Summation**: Integrated an upcast sum kernel (#27958) to significantly speed up summation operations on series with smaller data types.

### Breaking Changes & Deprecations
* **Deprecation**: The `strict` parameter in `pl.concat` has been deprecated and replaced with the new `how='horizontal_extend'` option (#27965). Update your code to use the new parameter to ensure future compatibility.