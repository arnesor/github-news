# GitHub New Releases Report 2026-09-19

**[astral-sh/uv 0.12.17](https://github.com/astral-sh/uv/releases/tag/0.12.17)**

### Summary
uv 0.12.17 introduces targeted resolution enhancements, build performance optimizations, and fixes for platform-specific wheel selection. This release notably adds preview support for configuring minimum libc baselines in universal resolutions alongside algorithmic speedups during package deduplication.

### Highlights
- **Minimum Libc Targeting (Preview)**: Introduced the `minimum-libc-version` setting to define minimum glibc and musl versions that universal resolutions must support ([#21651](https://github.com/astral-sh/uv/pull/21651)).
- **Build & Resolver Performance**: Eliminated quadratic overhead when handling numerous build exclusion patterns and reduced resolver memory allocations when deduplicating requests ([#21650](https://github.com/astral-sh/uv/pull/21650), [#21810](https://github.com/astral-sh/uv/pull/21810)).
- **macOS Baseline Compatibility**: Fixed a bug where `required-environments` could resolve wheels requiring a newer macOS version than the configured Darwin baseline ([#21825](https://github.com/astral-sh/uv/pull/21825)).

### Breaking Changes
None. Note that the preview command `uv workspace metadata` now defaults to read-only mode unless `--sync` is explicitly supplied.