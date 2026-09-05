# GitHub New Releases Report 2026-09-05

**[astral-sh/uv 0.12.10](https://github.com/astral-sh/uv/releases/tag/0.12.10)**

### Summary
uv 0.12.10 delivers enhanced publishing security, lockfile stability improvements, and performance optimizations across workspaces. This patch release notably adds automatic token revocation for PyPI trusted publishing and resolves several edge cases with `exclude-newer` lockfile semantics.

### Highlights
- **Trusted Publishing Token Revocation**: `uv publish` now automatically attempts to revoke short-lived PyPI trusted-publishing tokens upon completion, even when a publish fails ([#21423](https://github.com/astral-sh/uv/pull/21423)).
- **`exclude-newer` Lockfile Fixes**: Several fixes prevent false `--locked` failures and allow `uv lock --check` to correctly reuse lockfiles when cutoff dates are moved later or disabled ([#21454](https://github.com/astral-sh/uv/pull/21454), [#19571](https://github.com/astral-sh/uv/pull/19571)).
- **Performance Gains**: Workspace resolution is now faster for large projects with conflicts by filtering out unrelated extras and dependency groups during conflict simplification ([#21399](https://github.com/astral-sh/uv/pull/21399)).

### Breaking Changes
None. *(Note: `uv init` now requires an explicit `--name` flag if the inferred directory name conflicts with a reserved Python interpreter name).*