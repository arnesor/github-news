# GitHub New Releases Report 2026-10-04

**[astral-sh/uv 0.12.23](https://github.com/astral-sh/uv/releases/tag/0.12.23)**

### Summary
uv 0.12.23 introduces preview capabilities to inspect, sync, and export directly from a `uv.lock` file without requiring a workspace manifest. The release also adds support for CPython 3.15.0rc3 and delivers key fixes for Windows ARM64 wheel emulation and workspace dependency conflicts.

### Highlights
- **Manifest-free Lockfile Operations (Preview)**: Run `uv sync`, `uv export`, `uv tree`, and `uv workspace metadata` using `--frozen` with `frozen-lockfile` directly against `uv.lock` without needing a workspace manifest present.
- **Windows ARM64 Emulation Improvements**: Allows x86-64 Python interpreters running under emulation on Windows ARM64 to install prebuilt `win_amd64` wheels rather than falling back to building from source.
- **Workspace Source Conflict Fix**: Rejects alternate sources for workspace members across conflicting dependency selections, preventing the generation of un-installable lockfiles.

### Breaking Changes
None. This is a backward-compatible patch release.