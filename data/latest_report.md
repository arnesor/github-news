# GitHub New Releases Report 2026-06-02

**[astral-sh/uv 0.11.18](https://github.com/astral-sh/uv/releases/tag/0.11.18)**

### Summary
`uv` version 0.11.18 introduces a new preview command `uv check` alongside important performance restorations and bug fixes. This release resolves a recent regression affecting local wheel installations and updates virtual environment activation scripts with upstream improvements.

### Highlights
* **Preview: `uv check` Integration**: Adds a new preview command `uv check` to run the `ty` tool directly via `uv` ([#19605](https://github.com/astral-sh/uv/pull/19605)).
* **Performance Recovery**: Resolves a performance regression during the unzipping of local wheels, restoring `uv`'s signature install speeds ([#19637](https://github.com/astral-sh/uv/pull/19637)).
* **Upstream Activation Fixes**: Updates environment activation scripts with upstream fixes to improve reliability across various shell environments ([#19628](https://github.com/astral-sh/uv/pull/19628)).

### Breaking Changes
⚠️ **None.** (Note: The Minimum Supported Rust Version (MSRV) has been bumped to 1.94 in [#19600](https://github.com/astral-sh/uv/pull/19600), which only impacts developers building `uv` from source).
---
**[narwhals-dev/narwhals v2.22.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.22.0)**
- Error generating summary: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}