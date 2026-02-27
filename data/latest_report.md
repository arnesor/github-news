# GitHub New Releases Report 2026-02-27

**[astral-sh/ruff 0.15.4](https://github.com/astral-sh/ruff/releases/tag/0.15.4)**

### Summary
Ruff 0.15.4 is a targeted patch release that resolves a critical panic triggered by the newly introduced `PLR1712` rule. This update ensures stability for users employing type annotation (`ANN`) or docstring (`D`) rules alongside the latest linting additions.

### Highlights
- **Panic Resolution:** Fixed a crash occurring when rule `PLR1712` was enabled in conjunction with rules that analyze definitions (such as the `ANN` and `D` suites).
- **Pyflakes False Positive:** Resolved an issue in `F821` where names used before `del` in stub files (`.pyi`) were incorrectly flagged.
- **Documentation Clarity:** Updated guidance on how Ruff detects first-party imports and corrected examples for the `import-heading` rule.

### Breaking Changes
None.