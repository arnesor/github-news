# GitHub New Releases Report 2026-02-12

**[astral-sh/ruff 0.15.0](https://github.com/astral-sh/ruff/releases/tag/0.15.0)**

## Ruff v0.15.0 Analysis

### Summary
Ruff v0.15.0 introduces the 2026 style guide for the formatter and adds highly requested support for block-level lint suppression comments. This release also stabilizes over a dozen rules and modernizes the project's infrastructure, including updated Docker base images and a higher MSRV.

### Highlights
*   **Block-Level Suppressions**: You can now wrap code blocks with `# ruff: disable[RULE]` and `# ruff: enable[RULE]` comments. This is ideal for suppressing linting errors (like naming conventions) across specific multi-line functions or blocks without resorting to file-wide ignores.
*   **2026 Style Guide**: The formatter has been updated with the latest style standards. Key changes include better handling of lambda parameters/bodies, parenthesized exception tuples for Python 3.14+, and more flexible blank line placement within function bodies.
*   **Markdown Code Formatting (Preview)**: Ruff can now format Python code snippets directly within Markdown files. This feature is currently in preview and must be enabled via configuration or CLI.

### ⚠️ Breaking Changes
*   **Formatter Evolution**: Running the formatter will now apply the 2026 style guide, which may cause significant diffs in existing codebases.
*   **Docker Image Updates**: The `ruff:alpine` image now uses Alpine 3.23, while `debian` images have transitioned to Debian 13 "Trixie."
*   **Architecture Support**: Prebuilt binaries for big-endian `ppc64` have been dropped.
*   **Config Resolution**: Configuration files specified via `extend` are now resolved before falling back to default Python versions, potentially altering rule application in complex setups.

### Priority: Breaking
---
**[astral-sh/uv 0.10.2](https://github.com/astral-sh/uv/releases/tag/0.10.2)**

### Summary
`uv` v0.10.2 is a focused patch update that stabilizes the installation process for users building from source via Cargo. It also introduces deprecations for non-standard ZIP compression methods to improve long-term archive reliability and standards compliance.

### Highlights
- **Source Build Fix:** Resolved a `cargo-install` failure caused by a missing `uv-test` dependency, restoring the ability to install `uv` directly via the Rust toolchain.
- **ZIP Handling Refinement:** Deprecated unexpected ZIP compression methods to align with industry standards and ensure more predictable package extraction.

### Breaking Changes
No breaking changes were introduced in this release.
---
**[cjolowicz/nox-poetry v1.2.0](https://github.com/cjolowicz/nox-poetry/releases/tag/v1.2.0)**

## 🚀 nox-poetry v1.2.0

**Summary:** This release modernizes the `nox-poetry` build ecosystem and expands compatibility for the latest Python environments. It focuses on security compliance and transitioning to standard PEP 517 build frontends for improved maintainability.

### ✨ Highlights
* **Modernized Build System:** The package now utilizes the standard `build` PEP 517 frontend for packaging, ensuring better alignment with modern Python distribution standards.
* **FIPS Compliance:** Enhanced security for restricted environments by explicitly configuring `blake2b` hashing with `usedforsecurity=False`, allowing the tool to operate under FIPS-compliant policies.
* **Updated Runtime Support:** Full integration of Python 3.13 and Ubuntu 24.04 into the build and documentation infrastructure, alongside verified support for Poetry 2.1.

### ⚠️ Breaking Changes
* **Dropped Python 3.8 Support:** In line with the ecosystem-wide shift away from end-of-life versions, Python 3.8 is no longer supported. Users must upgrade to Python 3.9 or later.

### 📦 Dependency Updates
This release includes a massive overhaul of dependencies, grouping updates for GitHub Actions, CI workflows, and documentation tools (including Sphinx 8.2) to ensure a stable and secure development environment.
---
**[dynaconf/dynaconf 3.2.12](https://github.com/dynaconf/dynaconf/releases/tag/3.2.12)**

## Dynaconf 3.2.12 Release Analysis

### Summary
Dynaconf 3.2.12 is a maintenance release focused on enhancing configuration access performance and refining type hints. These updates provide a snappier experience for high-frequency settings lookups while improving developer ergonomics through better IDE support.

### Highlights
* **Performance Optimizations:** Significant incremental improvements to the core configuration access logic for faster retrieval.
* **LRU Caching:** Added `lru_cache` to the `find_the_correct_casing` function, reducing overhead during case-insensitive key resolution.
* **Type Hint Fix:** Updated the `.get()` method to return the `Any` type, ensuring better compatibility with static analysis tools like Mypy and Pyright.

### Breaking Changes
None. This is a non-breaking patch release.

### Priority
Bugfix
---
**[pandas-dev/pandas v3.0.0](https://github.com/pandas-dev/pandas/releases/tag/v3.0.0)**

### Summary
Pandas 3.0.0 marks a significant evolution in the library’s architecture, introducing major performance improvements and long-awaited API refinements. This release transitions the ecosystem toward more efficient data handling through the default enablement of Copy-on-Write and modernized string management.

### Highlights
*   **Default Copy-on-Write (CoW):** This architectural shift ensures consistent behavior when modifying slices and finally eliminates the infamous `SettingWithCopyWarning`, providing better memory efficiency and predictability.
*   **Dedicated String Data Type:** Pandas now defaults to a specialized string data type (leveraging Arrow) instead of generic `object` types, resulting in faster string operations and significantly lower memory overhead.
*   **Modernized Python Support:** The library now requires Python 3.11 or higher, allowing the codebase to leverage newer language features and optimizations while dropping support for older environments.

### Breaking Changes
**⚠️ CRITICAL WARNING:** This is a major version release with breaking changes. Functionalities deprecated throughout the 2.x series have been removed. Users are strongly advised to upgrade to pandas 2.3 first and resolve all deprecation warnings before moving to 3.0. Additionally, be aware of the new default datetime resolution inference and the mandatory move to Python 3.11+.

### Priority: Major
---
**[pola-rs/polars rs-0.53.0](https://github.com/pola-rs/polars/releases/tag/rs-0.53.0)**

Polars 0.53.0 introduces significant performance gains through a revamped streaming engine and expanded SQL compatibility, including support for `QUALIFY` and `FETCH`. This release also debuts Extension types for custom data handling alongside major optimizations for cloud-based Parquet and IPC I/O.

### 🏆 Highlights
- **Extension Types:** Introduction of Extension types (#25322) allows for user-defined types, significantly enhancing Polars' flexibility for domain-specific data structures.
- **Streaming Engine Evolution:** Massive updates to the streaming engine include new sinks for CSV/NDJSON/Parquet, streaming decompression for NDJSON/CSV, and new streaming operators like `merge-join` and `group_by_dynamic`.
- **SQL Power-up:** The SQL interface received a major overhaul, adding support for `QUALIFY`, `FETCH`, `WINDOW` references, `ROW_NUMBER()`, `RANK()`, and improved handling of ambiguous joins.

### 🚀 Performance Key Notes
- **New Sink Pipelines:** Implemented new single-file and partitioned IO sink pipelines for Parquet and IPC, enabling zero-copy uploads to `object_store`.
- **Kernel Optimizations:** Added dedicated fast kernels for `arg_max/arg_min`, `is_nan`, and string slicing.
- **Concurrent Schema Resolution:** File schemas and metadata are now resolved concurrently, speeding up multi-file scans.

### ⚠️ Breaking Changes & Deprecations
- **Implementation Removals:** The old streaming sink implementation and old sink IR have been removed in favor of the new pipeline.
- **Deprecations:** The batched CSV reader has been deprecated and removed (#25884).
- **Internal Renames:** Several internal types were renamed (e.g., `FileType` to `FileWriteFormat` and `Operator::Divide` to `RustDivide`), which may affect low-level Rust integrations.
- **Environment Changes:** Removed the `POLARS_IDEAL_MORSEL_SIZE` monkeypatching.
---
**[psf/black 26.1.0](https://github.com/psf/black/releases/tag/26.1.0)**
- Error generating summary: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-3-flash\nPlease retry in 10.695923487s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerMinutePerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-3-flash'}, 'quotaValue': '5'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '10s'}]}}
---
**[pytest-dev/pytest 9.0.2](https://github.com/pytest-dev/pytest/releases/tag/9.0.2)**
- Error generating summary: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-3-flash\nPlease retry in 10.398450108s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerMinutePerProjectPerModel-FreeTier', 'quotaDimensions': {'model': 'gemini-3-flash', 'location': 'global'}, 'quotaValue': '5'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '10s'}]}}
---
**[python-poetry/poetry 2.3.2](https://github.com/python-poetry/poetry/releases/tag/2.3.2)**
- Error generating summary: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-3-flash\nPlease retry in 10.192287518s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerMinutePerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-3-flash'}, 'quotaValue': '5'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '10s'}]}}
---
**[unionai-oss/pandera v0.29.0](https://github.com/unionai-oss/pandera/releases/tag/v0.29.0)**
- Error generating summary: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-3-flash\nPlease retry in 9.85822016s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerMinutePerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-3-flash'}, 'quotaValue': '5'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '9s'}]}}
---
**[wntrblm/nox 2026.02.09](https://github.com/wntrblm/nox/releases/tag/2026.02.09)**
- Error generating summary: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-3-flash\nPlease retry in 9.587200626s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerMinutePerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-3-flash'}, 'quotaValue': '5'}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '9s'}]}}