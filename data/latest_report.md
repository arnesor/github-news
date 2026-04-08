# GitHub New Releases Report 2026-04-08

**[astral-sh/uv 0.11.4](https://github.com/astral-sh/uv/releases/tag/0.11.4)**

### Summary
`uv` v0.11.4 expands Python version support to include the 3.15.0a8 alpha and introduces the `--upgrade-group` flag for more granular dependency management. This update also prioritizes security and reliability with stricter URL hash enforcement and several fixes for workspace resolution and exports.

### Highlights
* **Python 3.15 Alpha Support:** Users can now manage and test with the latest CPython releases, including 3.13.13, 3.14.4, and the first 3.15.0a8 alpha.
* **Targeted Upgrades:** The new `--upgrade-group` flag allows developers to upgrade specific dependency groups without forcing a full environment refresh.
* **Stricter Dependency Security:** Enhanced reproducibility by enforcing direct URL hashes for `pyproject.toml` dependencies and requiring all hash algorithms to match for a given archive.

### Breaking Changes
No explicitly breaking API changes were introduced in this release, though the stricter enforcement of URL hashes may surface inconsistencies in existing configurations that were previously ignored.

### Priority
PRIORITY: Bugfix

---
**Install uv 0.11.4**
```sh
curl --proto '=https' --tlsv1.2 -LsSf https://releases.astral.sh/github/uv/releases/download/0.11.4/uv-installer.sh | sh
```
---
**[marimo-team/marimo 0.22.5](https://github.com/marimo-team/marimo/releases/tag/0.22.5)**

### Summary
marimo v0.22.5 introduces **marimo pair**, a transformative AI agent skill that allows agents to collaborate directly within live notebook sessions with full execution control. The update also delivers a comprehensive overhaul of the data table UI, making it more responsive and feature-rich for complex data exploration.

### Highlights
*   **marimo pair**: A new agent skill for direct AI collaboration. Agents can access live variables, execute cells, and install packages alongside users. It includes a secure `--with-token` auth flow and a "Pair with an agent" modal directly in the notebook menu.
*   **Modernized Data Tables**: Tables now feature responsive column layouts that adapt to the number of columns, smarter headers with dedicated sort/menu buttons, and a persistent top toolbar for search and chart-builder actions.
*   **Developer Experience & API Enhancements**: Significant improvements to the `NotebookCell` and `_CellsView` APIs (including runtime status and better `__repr__`), enhanced LSP discovery, and support for anywidget's `MimeBundleDescriptor` API.

### Breaking Changes
No breaking changes were identified in this release.

### Priority
While this is a patch version (0.22.5), the introduction of "marimo pair" represents a significant feature addition.
---
**[pytest-dev/pytest 9.0.3](https://github.com/pytest-dev/pytest/releases/tag/9.0.3)**

### Pytest 9.0.3 Release Analysis

Pytest 9.0.3 is a maintenance release that addresses several stability issues, including a critical security vulnerability related to temporary directory handling. This version also improves developer experience by replacing internal assertion failures with clear usage errors and refining the accuracy of `pytest.approx` for mapping comparisons.

#### Highlights
*   **Security Fix (CVE-2025-71176):** Patched a vulnerability involving the use of insecure temporary directories, ensuring safer file operations during test execution.
*   **Improved Error Clarity:** Attempting to block `conftest.py` files using the `-p no:` option now raises a descriptive `UsageError` instead of triggering an internal assertion failure.
*   **Mapping Comparison Fix:** `pytest.approx` now correctly respects the key order of `collections.abc.Mapping` objects, ensuring more reliable assertions for ordered dictionaries and similar structures.

#### Breaking Changes
There are no breaking changes to the public API in this release. However, users incorrectly attempting to disable `conftest.py` files via the `-p` flag will now encounter an explicit `UsageError` where previously the system might have silently failed or crashed internally.

#### Other Notable Changes
*   Fixed a crash occurring when an `exceptiongroup` was raised with `__tracebackhide__ = True`.
*   Resolved an issue where non-string messages in `unittest.TestCase.subTest()` were omitted from output.
*   Updated documentation to clarify that capture fixtures (`capsys`, `capfd`) take precedence over command-line flags like `-s`.