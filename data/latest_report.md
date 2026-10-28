# GitHub New Releases Report 2026-10-28

**[narwhals-dev/narwhals v2.28.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.28.0)**

### Summary
Narwhals v2.28.0 expands cross-backend capabilities by introducing plugin support for IO and `from_*` constructors alongside expanded list operations for Dask. The release also brings critical compatibility adjustments for DuckDB 2.0 and refines statistical aggregations across SQL and lazy backends.

### Highlights
- **Extended Plugin System**: Adds support for custom plugins in IO methods and `from_*` constructors, unlocking deeper integration for third-party engines.
- **Expanded Dask List Methods**: Implements a full suite of list operations on Dask Series, including `list.{len, get, min, max, mean, median, sum, sort}`.
- **DuckDB 2.0 Readiness**: Addresses multiple compatibility gaps with DuckDB 2.0, including join typing, duration calculations (`dt.total_*`), and deprecated API removals.

### Breaking Changes
None reported in this release.
---
**[pytest-dev/pytest 9.2.0](https://github.com/pytest-dev/pytest/releases/tag/9.2.0)**

### Summary
pytest 9.2.0 delivers significant CI and test execution performance improvements, headlined by content-hash-based bytecode caching for rewritten test modules and lazy assertion diff formatting. This release also enforces stricter validation for test parametrization arguments, CLI options, and plugin startup failures while deprecating legacy fixture patterns ahead of pytest 10.

### Highlights
- **Hash-Based Rewrite Caching**: Cached rewritten modules in `__pycache__` are now invalidated by source content hash rather than file modification time (`mtime`). This prevents CI environments from constantly invalidating caches and re-rewriting all test modules on fresh checkouts.
- **Lazy Diff & Traceback Performance**: Assertion diffs are now constructed lazily and capped to truncation budgets to avoid rendering huge diffs. Additionally, `RecursionError` tracebacks trim repetitive intermediate frames by default, and `tmp_path` avoids quadratic directory traversal.
- **Smart Test Ordering for Parametrized Fixtures**: Tests parametrized with higher-than-function scopes are now grouped by parameter value rather than index, preventing expensive fixtures from being redundantly set up and torn down.

### Breaking Changes
⚠️ **Breaking changes are present in this release:**
- **Parametrize Arguments are Keyword-Only**: Passing `indirect`, `ids`, and `scope` positionally to `Metafunc.parametrize()` or `@pytest.mark.parametrize()` now raises a `TypeError` (e.g., `parametrize("x", [(1, 2)], indirect=True)` must be explicit).
- **Stricter `-c` Configuration Checks**: Passing a non-existent path, a directory, or an unsupported file format to `-c` now raises a usage error instead of being ignored or throwing an unhandled `FileNotFoundError`.
- **Plugin Import Exit Codes**: Plugin import failures at startup now exit with standardized `ExitCode.USAGE_ERROR` (`4`) or `INTERNAL_ERROR` (`3`) instead of raising `ImportError` with exit code `1`.