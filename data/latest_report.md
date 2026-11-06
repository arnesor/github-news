# GitHub New Releases Report 2026-11-06

**[astral-sh/ruff 0.17.4](https://github.com/astral-sh/ruff/releases/tag/0.17.4)**

### Summary
Ruff 0.17.4 delivers substantial internal performance optimizations across the formatting and linting engines alongside several parser and diagnostic bug fixes. It also improves terminal UX by honoring standard color suppression environment variables and adds new preview lint rules.

### Highlights
- **Performance Optimizations**: Substantial speedups across the pipeline, including a Bloom filter for comment lookups, cached callee qualified names across lint rules, and reduced source-slice overhead during formatting.
- **Parser & Crash Fixes**: Resolves a panic triggered by BOM-prefixed files in the diagnostic renderer and fixes syntax handling for semicolons preceding `raise` statements and `match` identifiers.
- **CLI Color Standards**: Diagnostics now honor `CLICOLOR=0` and give proper precedence to `NO_COLOR` across Ruff tool invocations.

### Breaking Changes
None. This is a backwards-compatible patch release.