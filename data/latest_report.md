# GitHub New Releases Report 2026-02-20

@everyone **[astral-sh/ruff 0.15.2](https://github.com/astral-sh/ruff/releases/tag/0.15.2)**

### Summary
Ruff 0.15.2 introduces a massive expansion to the default rule set for users in preview mode, increasing the count from 59 to 412 enabled rules. This release also focuses on parser stability, resolving edge cases in indentation tracking and async context detection.

### Highlights
*   **Massive Preview Rule Expansion:** The preview default rule set has been significantly broadened to 412 rules. While mostly a superset of stable defaults, it specifically excludes several `E` and `F` series rules (like `E401`, `E701`, and `F403`) to refine the out-of-the-box experience.
*   **Parser & Indentation Refinements:** Fixed critical parser issues, including incorrect indentation tracking after line continuations and false syntax errors when encountering match-like annotated assignments.
*   **Improved Plugin Accuracy:** Multiple bug fixes were deployed for `flake8-async` (context logic), `flake8-bugbear` (lambda false positives), and `pyupgrade` (handling of `typing.io` and `typing.re`).

### Breaking Changes
While this is a patch release, users with **preview mode enabled** will experience a significant increase in linting diagnostics due to the expanded default rule set. If you prefer the previous behavior, you must manually configure your `select` list to `["E4", "E7", "E9", "F"]`.

### Priority
MINOR