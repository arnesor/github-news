# GitHub New Releases Report 2026-08-07

**[pola-rs/polars rs-0.55.2](https://github.com/pola-rs/polars/releases/tag/rs-0.55.2)**

### Polars Rust Crate `rs-0.55.2` Release Notes

**Summary**
Polars `rs-0.55.2` is a patch release for the Rust implementation focusing on cloud I/O resiliency and critical stability fixes. It introduces an adaptive HTTP rate-limiter for cloud storage access alongside a fix for a concurrency unsoundness issue in Rayon.

**Highlights**
* **Adaptive HTTP Rate-Limiter**: Automatically adjusts request rates to prevent throttling during cloud I/O operations (#28591).
* **Rayon Unsoundness Fix**: Resolved a memory safety/concurrency bug in `rayon block_on` (#28709).
* **CSPE Reliability**: Added shallow IR node equality checks alongside hashing to prevent collisions in Common Subplan Elimination (#28506).

**Breaking Changes**
* 🟢 **None**: This release contains no breaking changes.