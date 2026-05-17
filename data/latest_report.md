# GitHub New Releases Report 2026-05-17

**[narwhals-dev/narwhals v2.21.2](https://github.com/narwhals-dev/narwhals/releases/tag/v2.21.2)**

### Narwhals v2.21.2 Analysis

#### Summary
Narwhals v2.21.2 introduces support for the negation unary operator in expressions and series, streamlining numeric data manipulation. The release also focuses on infrastructure stability and proactive preparation for upcoming upstream changes in the pandas ecosystem.

#### Highlights
* **Unary Negation Operator:** Users can now use the `-` operator directly on Narwhals expressions and series objects, simplifying mathematical transformations.
* **DuckDB Stability:** Reverted a previous fix regarding `float('nan')` values in joins for DuckDB to maintain broader engine compatibility.
* **Pandas Future-Proofing:** Initiated internal updates to handle the upcoming deprecation of `inplace` arguments in pandas, ensuring long-term compatibility.

#### Breaking Changes
None. This is a maintenance patch focused on stability and a minor feature addition.

#### Priority: Bugfix
---
**[psf/black 26.5.0](https://github.com/psf/black/releases/tag/26.5.0)**

### Summary
Black 26.5.0 introduces early support for Python 3.15, incorporating new syntactic features like unpacking in comprehensions and lazy imports. The release also focuses on improving developer experience through clearer parse error reporting and refining stable formatting edge cases.

### Highlights
* **Python 3.15 Compatibility:** Syntactic support for PEP 798 (unpacking in comprehensions) and PEP 810 (lazy imports) is now live, with CI updated to include Python 3.15 testing.
* **Enhanced Parse Error Reporting:** The introduction of `SourceASTParseError` and multi-line output with error pointers makes it easier to distinguish between source syntax errors and internal tool failures.
* **Stable Style Refinements:** Fixed several edge cases where `# fmt: skip` was ignored in nested expressions or compound statements, and resolved a crash involving f-strings following `# fmt: off` comments.

### Breaking Changes
No direct breaking changes to formatting logic were introduced in this release. Note that `blackd` users will now receive HTTP 400 (Bad Request) instead of HTTP 500 for source parse failures, which may require minor adjustments to automated monitoring systems.

### Priority
Minor