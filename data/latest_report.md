# GitHub New Releases Report 2026-07-09

**[marimo-team/marimo 0.23.13](https://github.com/marimo-team/marimo/releases/tag/0.23.13)**

## marimo 0.23.13

### Summary
Marimo version 0.23.13 delivers targeted bug fixes to improve notebook parsing stability and code formatting reliability. This patch release addresses edge cases when pasting notebooks and ensures class decorators are preserved during formatting, alongside preliminary work on a new formatter.

### Highlights
* **Pasted Notebook Parsing Fix:** Resolved edge cases encountered when parsing pasted notebooks, making code migration and sharing smoother (#10033).
* **Class Decorator Preservation:** Fixed a formatting bug to ensure that class decorators on exposed classes are properly preserved (#10042).
* **WIP JAX/Flax Formatter:** Introduced initial work on a dedicated formatter for JAX/Flax, laying the groundwork for better ML-ecosystem integration (#9902).

### Breaking Changes
None. This is a non-breaking patch release.