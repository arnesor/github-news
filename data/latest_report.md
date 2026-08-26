# GitHub New Releases Report 2026-08-26

**[astral-sh/uv 0.12.6](https://github.com/astral-sh/uv/releases/tag/0.12.6)**

### Summary
`uv` 0.12.6 brings significant performance boosts across major operating systems by enabling Profile-Guided Optimization (PGO) for release binaries. This patch also introduces preview flags for workspace management and delivers important bug fixes for recursive extras, index credential reuse, and Git pin resolution.

### Highlights
- **Profile-Guided Optimization (PGO):** Enabled PGO across Linux (x86-64/ARM64), macOS (ARM64), and Windows (x86-64) binaries, yielding broad speedups.
- **New Preview Features:** Added `uv workspace metadata --sync --exact` to prune packages outside the selected resolution and introduced `artifact-hash-filtering` for `uv pip compile`.
- **Resolver & Extra Fixes:** Fixed dependency handling when recursive extras mix production/extra conditions, preserved constraints in transitive extras, and resolved 40-character Git commit pins accurately.

### Breaking Changes
None. This is a non-breaking patch release.