# GitHub New Releases Report 2026-05-23

**[pola-rs/polars py-1.41.0](https://github.com/pola-rs/polars/releases/tag/py-1.41.0)**

## Polars py-1.41.0 Release Summary

### Summary
Polars version `py-1.41.0` delivers massive performance optimizations alongside critical stabilization updates to its streaming engine and Parquet reader. This release also introduces several key API enhancements, such as `LazyFrame.gather` and float16 stabilization, while marking `StringCache` as deprecated.

### Highlights
1. **Stabilized Streaming Engine (#27497):** The out-of-core streaming engine is now officially stabilized, providing highly reliable and efficient execution for datasets that exceed RAM limits.
2. **`LazyFrame.gather` (#27501):** Added native support for gathering/indexing rows lazily, enabling richer optimization pushdowns and cleaner expression composition.
3. **Blazing Fast Parquet Metadata Decoding (#27427):** Implemented a hand-written Thrift decoder that drastically speeds up Parquet file metadata parsing, reducing overhead during query planning.

### Breaking Changes & Deprecations
* ⚠️ **Deprecation of `StringCache` (#27580):** The global `StringCache` is now deprecated. Developers should transition to local scoped contexts (`with pl.StringCache(): ...`) to prevent state leaks and prepare for future removal.
* *Note:* No immediate breaking changes have been introduced in this release.