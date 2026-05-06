# GitHub New Releases Report 2026-05-06

**[astral-sh/uv 0.11.10](https://github.com/astral-sh/uv/releases/tag/0.11.10)**

### Summary
`uv` version 0.11.10 is a focused maintenance release that resolves a specific edge case in Python version resolution. This update ensures that pre-release Python requests containing non-zero patch versions are correctly handled during environment setup and dependency resolution.

### Highlights
* **Enhanced Pre-release Support:** Fixed a bug where Python requests for pre-release versions (like alphas, betas, or RCs) with non-zero patch versions were being improperly restricted.
* **Improved Development Flexibility:** This fix is particularly important for developers testing against the latest upstream Python builds and non-standard pre-release distributions.
* **Verified Build Integrity:** All release artifacts continue to support GitHub Artifact Attestations, allowing users to verify the provenance of their binaries using the GitHub CLI.

### Breaking Changes
No breaking changes have been identified in this release.

### Priority
This is a standard bugfix release.
---
**[marimo-team/marimo 0.23.5](https://github.com/marimo-team/marimo/releases/tag/0.23.5)**

# marimo 0.23.5 Release Summary

### Summary
marimo 0.23.5 introduces interactive coding within slide views and expands observability with OpenTelemetry distributed tracing support. This update also improves the WASM experience by patching Polars network I/O and refining the developer CLI workflow.

### 🌟 Highlights
* **Editable Code in Slides**: Users can now toggle an inline code editor during presentations (press `C`), enabling live code execution and experimentation directly within the slide view or fullscreen mode.
* **OpenTelemetry Support**: Added OTLP export and W3C trace context propagation, bringing enterprise-grade distributed tracing and observability to marimo applications.
* **WASM Enhancements**: Patched Polars network I/O specifically for WASM notebooks, ensuring more reliable data handling in browser-based environments.

### ⚠️ Breaking Changes
* **None**: This release contains no documented breaking changes and focuses on feature enhancements and bug fixes.