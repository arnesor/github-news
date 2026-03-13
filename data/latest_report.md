# GitHub New Releases Report 2026-03-13

**[astral-sh/ruff 0.15.6](https://github.com/astral-sh/ruff/releases/tag/0.15.6)**

## Ruff 0.15.6 Release Analysis

Ruff 0.15.6 introduces foundational support for lazy imports and PEP 798 star-unpacking in comprehensions, aligning the linter with upcoming Python language evolutions. This update also resolves critical CLI bugs affecting shebangs and whitespace, alongside expanding specialized linting for Airflow and the standard library.

### Highlights
*   **Lazy Import Integration:** Added support for parsing the `lazy` keyword, including `isort` compatibility and new rules (`TID254`) to either enforce or ban lazy imports.
*   **PEP 798 & Modern Python Support:** Implemented star-unpacking for comprehensions (PEP 798) and updated rule logic for Python 3.13 (`FURB101`) and Python 3.15 (`RUF017`).
*   **CLI & Formatter Stability:** Fixed regressions where `--add-noqa` could corrupt file shebangs or inject unwanted whitespace, and improved formatter handling for multiline lambdas and type expressions.

### Breaking Changes
None. Users utilizing the **preview** release channel should note that a few rules were removed from the preview default set, which may slightly alter linting results.
---
**[pola-rs/polars py-1.39.0](https://github.com/pola-rs/polars/releases/tag/py-1.39.0)**

Polars 1.39.0 significantly bolsters the streaming engine with new nodes for joins and aggregations while optimizing cloud I/O performance for CSV and NDJSON. The release also matures SQL compatibility and expands integration with the Iceberg ecosystem, including new sink capabilities.

### Highlights
*   **Streaming Engine Upgrades:** Introduced a streaming `AsOf` join node and lowered `arg_min`, `arg_max`, and several `GroupBy` operations to the streaming engine to improve out-of-core processing efficiency.
*   **Cloud & Data Lake Enhancements:** Improved performance for cloud-based CSV/NDJSON reads and sinks, added `sas_token` support for Azure, and introduced unstable `sink_iceberg` support alongside `scan_iceberg` table identifier support.
*   **Expanded SQL & Expressions:** Added SQL support for `FETCH`, `ARRAY` literals, and `LPAD`/`RPAD` functions, plus new expression features like a `truncate` rounding mode and holiday support for business day calculations.

### Breaking Changes
*   **Namespace Registration:** Custom namespace registration can no longer override standard Polars methods or properties (#26450).
*   **Parquet Sinks:** The behavior of the `arrow_schema` parameter on `sink_parquet` has been reworked to support Iceberg V2 types (#26621).
*   **Deprecations:** `read_csv_batched` now issues a deprecation warning, and the `cache` argument in `{read, scan}_ndjson` is deprecated (#26530, #26711).
*   **Casting:** The `strict` parameter in `replace_strict` and nested casts now more aggressively raises errors on invalid conversions (#26453, #26499).

### Priority: Minor
---
**[psf/black 26.3.1](https://github.com/psf/black/releases/tag/26.3.1)**

### Black 26.3.1 Release Analysis

#### Summary
This patch release focuses on improving the reliability of Jupyter notebook formatting and enhancing the security posture of the `blackd` HTTP server. Key updates include a safer mechanism for handling notebook magic commands and new constraints to prevent unauthorized or excessive requests to the server.

#### Highlights
- **Jupyter Magic Protection**: Implemented exact-length placeholders for notebook magics to prevent cell corruption and added safety checks to abort formatting if unmasking becomes unsafe.
- **`blackd` Security Hardening**: Improved server stability by disabling browser-originated requests by default and introducing configurable origin allowlisting and request body limits.
- **Improved Cache Integrity**: Cache filename components for `--python-cell-magics` are now consistently hashed, ensuring custom magic names do not interfere with system cache paths.

#### Breaking Changes
- **`blackd` Default Policy**: Requests originating from web browsers are now disabled by default. Users relying on browser-based interactions with `blackd` will need to update their configuration to allowlist specific origins.

#### Priority
Bugfix