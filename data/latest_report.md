# GitHub New Releases Report 2026-06-27

**[astral-sh/uv 0.11.25](https://github.com/astral-sh/uv/releases/tag/0.11.25)**

### Summary
`uv` version 0.11.25 delivers critical security updates to harden package extraction alongside substantial enhancements to dependency scoping and lockfile management. This release also introduces highly anticipated preview features, including centralized virtual environment storage and script listings for workspaces.

### Highlights
* **Tar Parser Security Hardening**: Upgraded to `astral-tokio-tar` v0.6.3 to protect against parser differential exploits, bringing stricter and safer validation to source distribution extraction.
* **Scoped Dependency Management**: Added robust support for scoped overrides, additions, and exclusions, giving developers highly granular control over dependency resolution.
* **Centralized Project Environments (Preview)**: Introduced preview support for centralized environment storage in `uv venv` and project workflows, streamlining local environment management.

### Breaking Changes
⚠️ **Stricter Package Validation**: `uv` will now reject wheels containing multiple `.dist-info` directories and may reject legacy source distributions with ambiguous or malformed tar headers that were previously accepted.
---
**[dynaconf/dynaconf 3.3.1](https://github.com/dynaconf/dynaconf/releases/tag/3.3.1)**

### Dynaconf 3.3.1 Release Analysis

#### Summary
Dynaconf 3.3.1 introduces crucial compatibility updates, adding early support for Python 3.14 while officially dropping support for the end-of-life Python 3.9. This release also delivers key stability fixes, resolving a recursion error during dotted path assignments and ensuring deterministic key ordering during dictionary merges.

#### Highlights
* **Python 3.14 Support**: Adds forward compatibility for Python 3.14, adapting to its new Union type representation and dictionary iteration behaviors.
* **Recursion Error Resolution**: Fixes a critical `RecursionError` triggered when performing dotted path assignments (`dotted set`) containing brackets in the first segment.
* **Nested Merge Ordering**: Ensures key order is preserved in nested dictionaries when the `object_merge` function merges old configurations into new ones.

#### Breaking Changes
⚠️ **Python 3.9 EOL Drop**: Support for Python 3.9 has been officially removed. If your deployment environment still runs on Python 3.9, you must upgrade your runtime or pin your Dynaconf dependency to `< 3.3.1`.