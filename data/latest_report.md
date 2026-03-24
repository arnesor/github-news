# GitHub New Releases Report 2026-03-24

**[astral-sh/uv 0.11.0](https://github.com/astral-sh/uv/releases/tag/0.11.0)**

## uv v0.11.0 Release Summary

uv 0.11.0 introduces a major overhaul of the networking stack, transitioning to more modern TLS and cryptography libraries for better system integration and performance. This release also improves Linux observability by enabling frame pointers in Python builds and refines workspace management through several critical bug fixes.

### Highlights

*   **Modernized Networking Stack:** Replaced the TLS backend with `rustls-platform-verifier` and `aws-lc`, providing more consistent certificate validation that aligns with system-native behaviors (like macOS Security.framework) and broader cryptographic algorithm support.
*   **Enhanced Linux Profiling:** Python builds on Linux x86-64 and aarch64 now include frame pointers by default, significantly improving the accuracy and ease of performance profiling.
*   **Improved `uv audit` (Preview):** The audit tool gains new `--service-format` and `--service-url` flags, allowing developers more flexibility in how they report and track vulnerabilities.

### ⚠️ Breaking Changes

*   **TLS Certificate Validation:** The move to `rustls-platform-verifier` means uv now delegates validation to the OS. While more "correct," this may result in the rejection of certificates that were previously accepted, particularly if you rely on system-level certificate stores.
*   **CLI Deprecation:** The `--native-tls` flag is deprecated in favor of `--system-certs`. While still functional, users should update their scripts to use the new name.
*   **Build Dependency:** Compiling uv from source on x86-64 or i686 Windows now requires **NASM** to build the new cryptography backend.
*   **SSL Configuration:** Empty `SSL_CERT_FILE` values are now ignored for consistency with directory-based certificate settings.
---
**[duckdb/duckdb v1.5.1](https://github.com/duckdb/duckdb/releases/tag/v1.5.1)**

DuckDB v1.5.1 is a dedicated maintenance release designed to stabilize the recent v1.5 "Variegata" series through over 100 targeted bug fixes and performance refinements. This update primarily focuses on hardening Parquet and JSON processing, improving Windows shell compatibility, and updating the broader extension ecosystem.

### Highlights
* **Robust Parquet & JSON Enhancements:** Significant improvements to Parquet cardinality estimation using file sizes and cached metadata, better handling of unsupported Parquet variant types (converting to INT64), and fixes for crashes in Arrow dictionary conversions.
* **Storage & Stability Fixes:** Resolved a critical WAL corruption issue by correctly marking checkpointed blocks, fixed memory errors when transforming to v1.0.0 ART storage, and addressed a regression in the `UnnestRewriter` for deeply nested structures.
* **Optimizations & Tooling:** Enabled column pruning for `MATERIALIZED` CTEs to reduce unnecessary data processing, introduced atomic loads for Bloom filters to improve look-up performance, and enhanced the Windows CLI with better UTF-8/UTF-16 support and Unicode entry points.

### Breaking Changes
None. This is a patch release focused on bug fixes and internal improvements. Users should note that the internal storage version has been bumped to `v1.5.1`, but it remains compatible with the v1.5.x series.

### Key Extension Updates
The release includes version bumps and fixes for several major extensions:
* **Lance, Iceberg, Delta, and Unity:** Updated to the latest versions for improved interoperability.
* **Postgres & MySQL:** Synchronization with the latest upstream changes.
* **ADBC:** Now supports concurrent statements on the same connection.