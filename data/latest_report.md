# GitHub New Releases Report 2026-04-16

**[astral-sh/uv 0.11.7](https://github.com/astral-sh/uv/releases/tag/0.11.7)**

### uv 0.11.7 Release Summary
uv 0.11.7 delivers a critical security update via an upgraded CPython build featuring the latest OpenSSL patches. This version focuses on hardening developer workflows with improved error reporting for version mismatches and significant fixes for workspace management and the `uv audit` preview feature.

### Highlights
- **OpenSSL Security Upgrade:** The internal CPython build has been updated to the 20260414 release to address recent security vulnerabilities.
- **Refined UX & Diagnostics:** Improved messaging for `required-version` mismatches, TLS validation, and `--exclude-newer` hints provide clearer, more actionable feedback during configuration errors.
- **CI/CD & Audit Improvements:** Added JSON report support for `uv sync --check` failures and resolved issues in `uv audit` regarding script handling and extras traversal.

### Breaking Changes
- No breaking changes are introduced in this release.
---
**[unionai-oss/pandera v0.31.1](https://github.com/unionai-oss/pandera/releases/tag/v0.31.1)**

## 🚀 Pandera v0.31.1 Release Analysis

### Summary
Pandera v0.31.1 is a focused patch release that resolves a critical dependency issue for users leveraging the Polars engine. This update ensures that the `pandera[polars]` installation works correctly in environments where the `pandas` library is not present.

### Highlights
* **Decoupled Polars Imports:** Fixed an issue where importing `pandera` with Polars support incorrectly triggered a requirement for `pandas`.
* **Improved Environment Minimalization:** Supports leaner production environments by allowing users to strictly use Polars without unnecessary dependencies.
* **Bugfix Stability:** Addresses a specific import-time regression to ensure a smoother developer experience for non-pandas workflows.

### ⚠️ Breaking Changes
None. This is a non-breaking patch release intended to fix installation and import logic.