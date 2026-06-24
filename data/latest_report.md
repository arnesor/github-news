# GitHub New Releases Report 2026-06-24

**[astral-sh/ruff 0.15.19](https://github.com/astral-sh/ruff/releases/tag/0.15.19)**

### Summary
Ruff version 0.15.19 delivers a suite of micro-optimizations alongside improved editor integrations and minor rule adjustments. This patch release focuses on reducing memory allocations during parsing and formatting while enhancing the overall developer experience within IDEs.

### Highlights
1. **Performance Micro-Optimizations**: Multiple internal enhancements—such as using `ArrayVec` for qualified name segments, lazily creating source files, and avoiding allocations during string literal parsing—further boost Ruff's blazing-fast execution speeds.
2. **Improved Hover & Code Actions**: Added preview support for displaying human-readable rule names when hovering over suppression comments (e.g., `# noqa`) and within IDE code actions.
3. **Resilient Editor Integration**: Resolves a panic crash when inserting text at notebook cell boundaries and ensures Ruff safely falls back to default configurations when invalid editor-only settings are encountered.

### Breaking Changes
None.
---
**[astral-sh/uv 0.11.24](https://github.com/astral-sh/uv/releases/tag/0.11.24)**

### uv v0.11.24 Release Summary

**Summary**
Astral's `uv` version 0.11.24 delivers early support for CPython 3.15.0b3 alongside relocatable project environments behind its preview flag. This update also optimizes dependency resolution performance and resolves several bugs surrounding Python upgrades and shell environment activations.

**Highlights**
*   **Relocatable Project Environments (Preview):** Project environments can now be made relocatable under the preview flag (`#19965`), complemented by fixes to make `activate.fish` relocatable and expand support for broader Fish shell versions (`#19856`).
*   **CPython 3.15.0b3 Support:** Out-of-the-box support has been added for CPython 3.15.0b3, letting developers proactively test their pipelines against the next Python release (`#19964`).
*   **Performance & Control Improvements:** Leverages a compact index for lazy version maps to boost speed (`#19959`), allows developers to disable the `exclude-newer` configuration (`#19934`), and reapplies a key fix for transparent Python upgrades in project environments (`#19928`).

**Breaking Changes**
*   None.