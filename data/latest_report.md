# GitHub New Releases Report 2026-07-02

**[marimo-team/marimo 0.23.12](https://github.com/marimo-team/marimo/releases/tag/0.23.12)**

### marimo v0.23.12 Release

**Summary**
Marimo version 0.23.12 introduces key enhancements to frontend performance, accessibility, and machine learning framework integrations. This release updates model catalogs, improves mobile layout responsiveness, and adds native array protocol support for PyTorch and JAX in audio components.

**Highlights**
* **Audio & Framework Integrations**: Adds native array protocol support (including `torch.Tensor` and JAX) inside `mo.audio`, alongside support for `pydantic-ai` v2.
* **WASM & Frontend Upgrades**: Upgrades the frontend to Tailwind v4.3, implements a LazyStore dual-mode WASM backend, and enables direct JSON payload hydration for islands.
* **Accessibility & UX Polishing**: Adds keyboard and screen-reader support to `mo.ui.file_browser`, improves mobile layout clipping, and suppresses kernel-dependent table controls during static exports.

**Breaking Changes**
* 🛠️ None.
---
**[narwhals-dev/narwhals v2.23.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.23.0)**

### Summary
Narwhals v2.23.0 introduces new selector capabilities, broader datatype support, and top-level covariance expressions to enhance compatibility across backend engines. This release also fixes several backend-specific edge cases (including PyArrow and Polars), improves typing preservation for expression chains, and expands downstream CI testing.

### Highlights
1. **New Datatype & Selector Features**: Added `selectors.enum` to simplify targeting categorical enum columns and introduced support for the `Float16` datatype.
2. **Covariance & PyArrow Enhancements**: Added top-level covariance (`cov`) expressions and resolved null-handling issues for correlation (`corr`) within PyArrow, exposing both in `stable.v1`.
3. **Improved Expression Typing**: Fixed a typing issue to preserve stable `Expr` subclasses through complex `when/then/otherwise` chains, improving developer experience and type safety.

### Breaking Changes
⚠️ **No breaking changes** are introduced in this release. All updates are backward-compatible.