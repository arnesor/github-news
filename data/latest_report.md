# GitHub New Releases Report 2026-07-31

**[astral-sh/ruff 0.16.1](https://github.com/astral-sh/ruff/releases/tag/0.16.1)**

### Summary
Ruff v0.16.1 is a patch release focusing on language server improvements, autofix safety refinements, and various bug fixes across linting rules. This update enhances TOML support in the editor server while tightening fix safety for `pytest` and `refurb` rules.

### Highlights
- **LSP Enhancements**: Introduced native TOML file linting in the LSP server and resolved indexing bugs for nested multi-root workspaces.
- **Refined Fix Safety**: Adjusted fix classifications across rules (`PT018` is now safe by default unless comments are present; `PT022` and `FURB105` fixes are reclassified as unsafe to prevent unintended code changes).
- **Rule & Type Analysis Fixes**: Marked `range` as immutable in `flake8-bugbear` (`B008`), resolved `TypeVar` handling for defaults (`UP040`, `UP046`, `UP047`), and fixed false positives in `RET504` and `RUF065`.

### Breaking Changes
None.