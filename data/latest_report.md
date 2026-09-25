# GitHub New Releases Report 2026-09-25

**[astral-sh/ruff 0.16.9](https://github.com/astral-sh/ruff/releases/tag/0.16.9)**

### Summary
Ruff 0.16.9 is a maintenance release focused on eliminating false positives across core linting rules and improving diagnostic clarity. It also introduces forward-looking updates to LibCST-based fixes to ensure compatibility with Python 3.15.

### Highlights
- **Reduced False Positives in `flake8-bugbear`**: Resolved false positive triggers for function calls utilizing keyword arguments across rules `B009`, `B010`, and `B043` ([#28776](https://github.com/astral-sh/ruff/pull/28776)).
- **Deferred Annotations with Lazy Imports**: Updated `flake8-tidy-imports` (`TID255`) to permit lazy imports when used within deferred type annotations ([#28767](https://github.com/astral-sh/ruff/pull/28767)).
- **Python 3.15 Readiness**: Updated LibCST-based autofixes to support upcoming syntax and AST changes in Python 3.15 ([#28616](https://github.com/astral-sh/ruff/pull/28616)).

### Breaking Changes
None. This release is fully backwards-compatible.
---
**[astral-sh/uv 0.12.19](https://github.com/astral-sh/uv/releases/tag/0.12.19)**

### Summary
uv 0.12.19 delivers targeted fixes to dependency resolution and direct-URL package caching, alongside expanded interpreter support for newer PyPy and GraalPy builds. It also adds opt-in preview capabilities for lazy build-backend imports on CPython 3.15+ and smarter `uv.lock` freshness checks.

### Highlights
- **Direct-URL Caching Fix**: Preserves signed and encoded query parameters in direct-URL metadata, preventing unnecessary reinstalls of unchanged remote packages.
- **Lockfile & Build Previews**: Adds experimental flags to run build-backend hooks with lazy imports on CPython 3.15+ (`build-lazy-imports`) and omit unused resolution settings from `uv.lock` to reduce churn (`resolution-inputs`).
- **Resolver & Specifier Corrections**: Fixes installed-package verification where `1.0.0` did not satisfy arbitrary equality `===1`, and avoids git checkout marker collisions with `.ok` files in dependencies.

### Breaking Changes
None. This release also restores the public `FlatDistributions` export and `BTreeMap` conversion for downstream Rust API consumers.