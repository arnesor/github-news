# GitHub New Releases Report 2026-09-11

**[astral-sh/ruff 0.16.7](https://github.com/astral-sh/ruff/releases/tag/0.16.7)**

### Summary
Ruff 0.16.7 is a patch release focused on refining rule safety, improving internal performance, and expanding forward-compatibility for upcoming Python versions. It introduces preview rules for method receiver defaults and regex matching while tightening autofix behavior across several lint categories.

### Highlights
- **Safer Autofixes:** Prevents hazardous automated edits by marking `ISC003` (implicit string concatenation) fixes as unsafe when they would inadvertently construct docstrings, and skipping multi-member import fixes in `TID254`.
- **Performance Optimizations:** Accelerates configuration loading by speeding up inherited configuration resolution and optimizing parser name lookups during interning.
- **Python 3.15 & Typing Refinements:** Adds early compatibility adjustments for Python 3.15 (such as gating `ImportCycleError`), stops recommending the deprecated `typing.no_type_check_decorator` (`UP035`), and expands support for `slice` and `frozendict` generics.

### Breaking Changes
None. This is a non-breaking patch release.
---
**[astral-sh/uv 0.12.13](https://github.com/astral-sh/uv/releases/tag/0.12.13)**

### Summary
uv version 0.12.13 delivers resolution performance optimizations alongside newly added support for GraalPy 3.13.0. It also strengthens package integrity and Windows compatibility through metadata hash verification and improved in-memory binary launcher handling.

### Highlights
- **Optimized Dependency Resolution**: Significantly speeds up resolution by avoiding full wheel downloads, reusing supported hashes from direct URL fragments when PEP 658 metadata is available separately.
- **PEP 658 Hash Verification**: Enhances supply chain security by verifying hashes when downloading standalone PEP 658 metadata sidecars and preferring standard `core-metadata` fields.
- **Windows Launcher & Nano Server Improvements**: Edits entry-point launcher resources entirely in memory, adding support for Windows Nano Server while cutting down on antivirus file-locking contention.

### Breaking Changes
None. This is a non-breaking patch release.
---
**[marimo-team/marimo 0.24.1](https://github.com/marimo-team/marimo/releases/tag/0.24.1)**

### Summary
marimo 0.24.1 introduces slide deck exports to static HTML and interactive WebAssembly, alongside expanded file browsing across local directories and GitHub repositories. The release also brings a condensed reactive dependency graph, enhanced geospatial data workflows, and numerous stability fixes.

### Highlights
* **Export Slides to HTML & WebAssembly**: Share presentation-layout notebooks as reveal.js slide decks using `marimo export`. Supports both static HTML output with captured state and client-side interactive WebAssembly execution.
* **Expanded File & Repository Browsing**: Connect and browse GitHub repositories directly via the UI, or configure multiple named local project directories in `pyproject.toml` to access datasets and assets from the Files panel.
* **Compact Dependency Graph**: Navigate large notebooks more effectively with a condensed visual summary of variables and cell connections, featuring double-click expansion for inspecting code.

### Breaking Changes
None explicitly documented. However, experimental cache configuration has moved from `experimental.cache` to `cache.store`, which may require updates if you were configuring caching paths manually.