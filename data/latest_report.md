# GitHub New Releases Report 2026-10-15

**[astral-sh/uv 0.13.1](https://github.com/astral-sh/uv/releases/tag/0.13.1)**

### Summary
uv 0.13.1 introduces crucial stability and concurrency fixes to eliminate race conditions during lockfile writes, cache cleans, and parallel tool operations. This release also delivers performance improvements that decrease binary size and accelerate Simple API parsing, alongside early support for CPython 3.16.0a1.

### Highlights
- **Concurrency & Race Condition Hardening:** Resolved multiple concurrency hazards to prevent corruptions during simultaneous tool installations, cache clean operations, and reads on partially written lockfiles or sysconfig files.
- **Safer Tool & Python Uninstalls:** Fixed an issue where uninstalling tools or managed Python interpreters could mistakenly remove unrelated files adjacent to storage directories.
- **Performance & Footprint Reductions:** Shrunk uv's binary size while reducing overhead in package metadata parsing and accelerating Simple API parsing.

### Breaking Changes
None. This is a backwards-compatible patch release focusing on stability, bug fixes, and performance.