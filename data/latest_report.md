# GitHub New Releases Report 2026-09-16

**[astral-sh/uv 0.12.15](https://github.com/astral-sh/uv/releases/tag/0.12.15)**

### Summary
uv 0.12.15 is a targeted patch release that resolves a critical regression from 0.12.14 affecting package installations in common environments like Docker. It also delivers performance improvements that accelerate cold-cache resolutions and HTTP cache revalidations.

### Highlights
- **Docker & Target Install Regression Fix:** Reverted the rejection of symlinked wheel installation destinations, restoring support for `uv pip install --system` in official `python:*` Docker images and commands using `--target .` ([#21699](https://github.com/astral-sh/uv/pull/21699)).
- **Faster Cache Operations:** Cold-cache dependency resolution and HTTP cache revalidation are now faster due to batching cache write operations ([#21675](https://github.com/astral-sh/uv/pull/21675)).

### Breaking Changes
None. This release restores previously broken behavior.