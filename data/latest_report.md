# GitHub New Releases Report 2026-09-01

**[astral-sh/uv 0.12.8](https://github.com/astral-sh/uv/releases/tag/0.12.8)**

### Summary
uv 0.12.8 delivers performance optimizations for large lockfile operations and concurrent downloads, alongside enhancements to the experimental content-addressed cache. This patch also brings important fixes for Azure Storage integrations, workspace discovery, and security hash validation under `--require-hashes`.

### Highlights
- **Faster Lockfile Traversal & Warm Resolutions**: Speeds up dependency graph construction, dependency tree exports, audits, and warm resolutions on large lockfiles via package indexing and reduced marker interner work.
- **Content-Addressed Cache Preview**: Adds the `content-addressed-cache` preview feature to deduplicate identical files across cached wheels, optimized with buffer reuse and fast macOS cleanup.
- **Concurrency & Security Fixes**: Prevents concurrent `uv` processes from duplicating remote wheel downloads, redacts Azure SAS signature tokens from logs, and enforces strict hash validation when using `--require-hashes`.

### Breaking Changes
None.