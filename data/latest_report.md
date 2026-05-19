# GitHub New Releases Report 2026-05-19

**[astral-sh/uv 0.11.15](https://github.com/astral-sh/uv/releases/tag/0.11.15)**

### uv 0.11.15 Release Analysis

**Summary**
uv version 0.11.15 delivers critical security patches addressing TAR parser vulnerabilities and script entry point escapes. This update also introduces enterprise-focused features like Azure request signing and JSON output for the `uv audit` preview tool.

**Highlights**
* **Security Hardening:** Resolved two security advisories (GHSA-3cv2-h65g-fgmm and GHSA-4gg8-gxpx-9rph) to prevent malicious TAR parsing differentials and unauthorized directory escapes.
* **Cloud & Enterprise Support:** Added native support for Azure request signing and structured error reporting for authentication failures, streamlining usage in Microsoft-centric cloud environments.
* **Observability & Performance:** The `uv audit` tool now supports JSON output for automated security scanning, while async wheel writing and manifest parsing have received significant performance optimizations.

**Breaking Changes**
None.
---
**[numpy/numpy v2.4.6](https://github.com/numpy/numpy/releases/tag/v2.4.6)**

### NumPy 2.4.6 Release Summary

NumPy 2.4.6 is a maintenance patch focused on resolving a specific regression discovered in the 2.4.5 release. It ensures stability across Python versions 3.11 through 3.14 and addresses critical bugs in core array and linear algebra functionality.

#### Highlights
*   **`arr.conj()` Regression Fix**: Resolves a newly discovered bug in the array conjugation method introduced in the previous version.
*   **Linear Algebra Correction**: Fixes an issue where `np.linalg.svd(..., hermitian=True)` could return non-unitary matrices, ensuring mathematical correctness.
*   **Memory Management**: Corrects improper `INCREF`/`DECREF` handling in the string allocator (`NpyStringAcquireAllocator`) to prevent potential memory corruption.

#### Breaking Changes
None. This is a targeted patch release intended to restore expected behavior without changing the API.
---
**[psf/black 26.5.1](https://github.com/psf/black/releases/tag/26.5.1)**

## Black 24.5.1 Release Analysis

### Summary
Black 24.5.1 is a patch release focused on refining stable style formatting and correcting metadata in published executables. It specifically addresses edge cases involving inline comments and expands documentation for Neovim users.

### Highlights
* **Comment Preservation**: Fixed a bug where inline comments (like `# type: ignore`) were stripped when placed immediately before a `# fmt: skip` line, preventing AST equivalence failures.
* **Subscript Formatting Fix**: Resolved an instability issue in annotated assignments where subscripts contained inline comments (e.g., `list[ # comment ]`).
* **Neovim Integration Guide**: Added a comprehensive guide for Neovim users covering modern workflows including `conform.nvim`, `ALE`, and manual command setups.

### Breaking Changes
None. This release consists of bug fixes and documentation updates that maintain compatibility with the existing stable style.

### Priority
Bugfix