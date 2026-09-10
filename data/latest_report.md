# GitHub New Releases Report 2026-09-10

**[astral-sh/uv 0.12.12](https://github.com/astral-sh/uv/releases/tag/0.12.12)**

### Summary
uv 0.12.12 introduces official code signing for macOS and Windows binaries and wheels to enhance supply chain security and reduce antivirus false positives. It also patches an issue where distributions uploaded after the `exclude-newer` cutoff were mistakenly included in lockfiles and requirement hashes.

### Highlights
- **macOS & Windows Code Signing**: Executables and wheels are now signed and notarized (Apple Developer ID on macOS, Azure Authenticode on Windows), supporting publisher-based allowlisting and eliminating OS security warnings.
- **`exclude-newer` Consistency Fix**: Distributions uploaded after the configured `exclude-newer` timestamp are now strictly excluded from lockfiles and generated requirement hashes ([#21539](https://github.com/astral-sh/uv/pull/21539)).
- **Supply Chain Verification**: Release assets continue to support GitHub Artifact Attestations, allowing easy cryptographic integrity verification via the GitHub CLI.

### Breaking Changes
None. This is a backwards-compatible patch release.
---
**[pola-rs/polars py-1.44.2](https://github.com/pola-rs/polars/releases/tag/py-1.44.2)**

### Summary
Polars `py-1.44.2` is a targeted patch release for Python users that backports critical fixes to the 1.44 release branch. This update focuses on stability and maintenance without introducing new features or breaking changes.

### Highlights
- **Backport 1.44.2 (#29216)**: Consolidates upstream fixes and stability patches directly into the 1.44.x series.
- **Patch Stability**: Focuses strictly on reliability and bug resolution for existing workflows.
- **Contributor Fixes**: Incorporates key community-driven improvements across the Polars engine.

### Breaking Changes
None. This is a routine patch release backward-compatible with the 1.44.x series.