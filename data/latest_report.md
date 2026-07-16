# GitHub New Releases Report 2026-07-16

**[astral-sh/uv 0.11.29](https://github.com/astral-sh/uv/releases/tag/0.11.29)**

### Summary
uv version 0.11.29 introduces significant performance optimizations by caching workspace discovery and widening resolver version ranges, alongside key usability enhancements like JSON output for `uv tree` and CUDA 13.2 support. This release also resolves several panic-inducing edge cases, improves path security for build backends, and refines PEP 440 range ordering.

### Highlights
* **Workspace Discovery & Performance Boosts:** Performance is heavily optimized across `uv sync`, `uv tree`, `uv export`, `uv format`, and `uv audit` by reusing workspace discovery results and deferring client/build setup for no-op sync operations.
* **JSON Output for `uv tree`:** Programmatic analysis of your dependency tree is now much easier with the addition of native JSON output support to the `uv tree` command ([#19978](https://github.com/astral-sh/uv/pull/19978)).
* **Robustness & Security Hardening:** Enhanced security by rejecting PEP 517 build-backend paths that escape the source tree via symlinks. Additionally, several panic scenarios (such as invalid cloud credentials, invalid `pylock.toml` URLs, and non-UTF-8 virtualenv paths) have been replaced with clean error diagnostics.

### Breaking Changes
⚠️ **No breaking changes** are introduced in this release.