# GitHub New Releases Report 2026-06-06

**[narwhals-dev/narwhals v2.22.1](https://github.com/narwhals-dev/narwhals/releases/tag/v2.22.1)**

### Narwhals v2.22.1 Release Analysis

#### Summary
Narwhals version v2.22.1 is a lightweight patch release focused on improving ecosystem compatibility, packaging, and stability. It delivers key bug fixes for Polars and Fireducks integrations, alongside build improvements to ensure test data is packaged correctly.

#### Highlights
* **Polars Compatibility Improvements**: Backported critical fixes for Polars, including support for the `is_close` comparison on `Decimal` dtypes and correcting behavior for `semi` and `anti` joins on null values.
* **Fireducks Preservation**: Patched an issue to preserve expected execution and compatibility with Fireducks.
* **Complete Source Distribution (`sdist`)**: Included test data assets in the `sdist` build to facilitate seamless offline verification and package testing for downstream packagers.

#### Breaking Changes
* **None**: This is a non-breaking patch release designed to safely resolve bugs without affecting existing APIs.