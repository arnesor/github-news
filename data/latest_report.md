# GitHub New Releases Report 2026-03-07

**[astral-sh/uv 0.10.9](https://github.com/astral-sh/uv/releases/tag/0.10.9)**
- Error generating summary: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
---
**[psf/black 26.3.0](https://github.com/psf/black/releases/tag/26.3.0)**

### Black 26.3.0 Release Analysis

**Summary**
This release focuses on performance optimizations for Windows users and improving the developer experience through clearer error reporting. It also delivers critical stability fixes, including a correction for a bug that could lead to the corruption of non-UTF-8 source files.

**Highlights**
*   **Windows Performance Boost:** Introduced `winloop` support, providing Windows users of Black and `blackd` with a high-performance event loop similar to `uvloop` on Unix systems.
*   **Actionable Error Messaging:** Replaced cryptic "INTERNAL ERROR" messages with clear, actionable warnings when the target Python version is newer than the version running Black, preventing confusion during AST safety checks.
*   **GitHub Action Hardening:** Improved security for the official GitHub Action by restricting requirement parsing to version specifiers only, rejecting potentially unsafe direct URL references.

**Breaking Changes**
*   **Action Configuration:** Users relying on direct references (e.g., `black @ https://...`) within their `pyproject.toml` for the GitHub Action will find these are now rejected. Most users will not be affected, but those using custom forks via the action should review their configurations.

**Priority**
Minor