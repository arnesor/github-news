# GitHub New Releases Report 2026-07-08

**[astral-sh/uv 0.11.28](https://github.com/astral-sh/uv/releases/tag/0.11.28)**

### Summary
`uv` version 0.11.28 focuses on hardening ZIP archive security against parser differentials and introduces a massive sweep of memory allocation optimizations to boost CLI execution speed. This release also refines terminal error formatting for a better user experience and addresses several package resolution and caching bugs.

### Highlights
- **Security Hardening (ZIP Parser)**: Upgraded `astral-async-zip` to v0.0.20 to protect against parser differential vulnerabilities. `uv` will now strictly reject malformed or ambiguous ZIP archives that were previously accepted.
- **Aggressive Performance Optimization**: Significantly reduced CPU and memory overhead by avoiding dozens of unnecessary string allocations and object clones during runtime processes (e.g., Git revision handling, Python compatibility checks, and dependency metadata resolution). Additionally, `uv pip install` now limits bytecode compilation strictly to newly installed distributions.
- **Polished Error Rendering**: Revamped terminal output by preserving multiline indentation for error causes, displaying complete user-error cause chains, and routing final command failures through the standard printer so they properly respect `-q` and `-qq` quiet flags.

### Breaking Changes
No formal breaking changes are present in this release. However, the security update to the ZIP parser is a **behavioral change**: some malformed or non-standard ZIP archives that previously succeeded during package installation may now be rejected.