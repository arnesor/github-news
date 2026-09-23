# GitHub New Releases Report 2026-09-23

**[astral-sh/uv 0.12.18](https://github.com/astral-sh/uv/releases/tag/0.12.18)**

### Summary
uv 0.12.18 enhances CI/CD workflows and scriptability by introducing a `--check` mode and JSON output formatting to `uv pip install` and `uv pip sync`. The release also packages important stability fixes, including atomic rollback of project files on command failure and faster editable build times.

### Highlights
- **JSON Output & Dry-Run Auditing**: `uv pip install` and `uv pip sync` now support `--check` to report environment diffs without applying them, alongside `--output-format json` (compatible with `--dry-run`) for automated tooling integration.
- **Atomic State Rollbacks**: Commands such as `uv add`, `uv remove`, and `uv version` now automatically restore project manifests, script headers, and lock files if the operation fails or is interrupted.
- **Faster Editable Builds**: Editable wheel creation in `uv_build` is now faster by skipping compression for intermediate temporary wheels.

### Breaking Changes
None. All changes and additions in this release are backward-compatible.