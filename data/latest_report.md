# GitHub New Releases Report 2026-09-30

**[astral-sh/uv 0.12.21](https://github.com/astral-sh/uv/releases/tag/0.12.21)**

### Summary
uv 0.12.21 updates bundled CPython builds to OpenSSL 3.5.9 alongside cleaner lockfile formatting. It also delivers targeted bug fixes for Python version pinning safety and version bound compatibility checks.

### Highlights
- **CPython OpenSSL Update**: Upgraded CPython toolchains to use OpenSSL 3.5.9 for enhanced security and platform stability.
- **Safety Fix for Python Pinning**: Fixed a bug where running `uv python pin --rm` could unintentionally remove a global `.python-versions` file when `--global` was not specified.
- **Cleaner Lockfiles**: Omitted empty `[manifest]` tables when only subtables exist, with ongoing preview work (`resolution-inputs`) to strip redundant runtime constraints from `uv.lock`.

### Breaking Changes
None.