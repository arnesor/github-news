# GitHub New Releases Report 2026-03-14

**[astral-sh/uv 0.10.10](https://github.com/astral-sh/uv/releases/tag/0.10.10)**

## uv 0.10.10 Release Summary

uv 0.10.10 introduces the ability to check for outdated global tools and adds support for the latest CPython 3.15 alpha. This release also focuses on refining the `uv audit` preview feature and improving stability across Windows and Linux environments.

### Highlights
* **Tool Management:** Added the `--outdated` flag to `uv tool list`, making it easy to identify which globally installed tools require updates.
* **Security Auditing:** Enhanced the `uv audit` preview with better report formatting, direct links to vulnerability details, and optimized performance via batched OSV queries.
* **Compatibility & Stability:** This version adds support for CPython 3.15.0a7, introduces a `riscv64` musl build target, and fixes a critical decompression panic affecting large wheels on Windows.

### Breaking Changes
* None.