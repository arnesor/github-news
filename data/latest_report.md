# GitHub New Releases Report 2026-05-29

**[astral-sh/ruff 0.15.15](https://github.com/astral-sh/ruff/releases/tag/0.15.15)**

### Summary
Ruff version 0.15.15 brings key performance optimizations targeting memory footprint and AST efficiency, alongside minor bug fixes and tool improvements. This patch release also introduces enhanced duplicate import reporting in type-checking blocks and refines formatting for nested lambdas in f-strings.

### Highlights
- **AST & Memory Enhancements:** Significantly reduced memory usage and optimized lexer speed by introducing `ThinVec` to shrink AST `Stmt` nodes, avoiding redundant `TokenValue` drops, and sizing token vectors more efficiently.
- **Parser and Linter Updates (`F811` & `F821`):** Preview rule `F811` now reports duplicate imports within `typing.TYPE_CHECKING` blocks, while `F821` correctly treats function-scope bare annotations as locals according to PEP 526.
- **Formatter and Server Fixes:** Resolved a formatting bug with lambdas nested inside f-strings and improved LSP stability by ensuring code actions are returned for `codeAction/resolve` requests lacking a valid URL.

### Breaking Changes
None.
---
**[astral-sh/uv 0.11.17](https://github.com/astral-sh/uv/releases/tag/0.11.17)**

### Summary
`uv` version 0.11.17 introduces PEP 794 support for package builds and improves developer UX with helpful CLI diagnostics, such as warning users when attempting to add standard library modules. This release also brings robust offline stability, virtual environment safety safeguards, and critical bug fixes to environment management.

### Highlights
- **PEP 794 Support in `uv-build`**: Added support for `import-names` and `import-namespaces`, bringing `uv` closer to modern Python packaging standards.
- **Developer UX & Diagnostic Polish**: `uv add` now warns you if you try to add a standard library module, while the "403 Forbidden" hint now suggests utilizing `ignore-error-codes`.
- **Offline & Safety Safeguards**: Lock freshness checks for direct URLs are now skipped while offline to prevent command failures, and `uv venv --clear` is now blocked from accidentally deleting non-virtual environments.

### Breaking Changes
No breaking changes. However, safety validations have been tightened: `uv venv --clear` will now reject deleting non-virtual environments, duplicate script metadata blocks are rejected, and using binary names like "python3" as script entry points is now banned.