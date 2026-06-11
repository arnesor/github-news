# GitHub New Releases Report 2026-06-11

**[astral-sh/uv 0.11.20](https://github.com/astral-sh/uv/releases/tag/0.11.20)**

### Summary
`uv` version 0.11.20 delivers notable enhancements to package export operations and dependency listing, alongside an early preview of a new `uv upgrade` command. The release also packs performance optimizations for large workspaces, reduced macOS binary sizes, and several robust stability bug fixes.

### Highlights
*   **Preview of `uv upgrade`**: This release introduces an early, hidden `uv upgrade` command to lay the groundwork for streamlined dependency updates, with initial restrictions in place (such as rejecting Git revisions).
*   **Better Custom Index Control**: Users can now use `--emit-index-url` and `--emit-find-links` with `uv export`, while `uv pip list` gains support for `--find-links`, facilitating smoother workflows with offline or self-hosted package registries.
*   **Workspace & Compiler Optimizations**: Discovery times for massive multi-package workspaces are significantly reduced, and macOS release builds are now compiled with Identical COMDAT Folding (ICF) to reduce binary size.

### Breaking Changes
*   **None**: This patch release is fully backward-compatible.