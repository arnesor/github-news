# GitHub New Releases Report 2026-06-04

**[astral-sh/uv 0.11.19](https://github.com/astral-sh/uv/releases/tag/0.11.19)**

### Summary
`uv` version 0.11.19 steps up its WebAssembly capabilities with support for the PEP 783 PyEmscripten platform and the Pyodide 2025 target triple, alongside early compatibility for the CPython 3.15.0b2 beta. This release also tightens up distribution integrity and refines cross-platform installation behaviors.

### Highlights
* **WebAssembly Expansion**: Added support for the PyEmscripten platform (PEP 783) and the Pyodide 2025 target triple, reinforcing `uv` as a cutting-edge tool for browser-based Python environments.
* **Enhanced Security**: Mandated SHA256 checksum computation for all remote distributions to improve package verification and secure locking.
* **Smarter Cross-Compilation**: Fixed cross-platform installations by skipping Unix-specific steps when cross-installing Windows Python distributions.

### Breaking Changes
None. All updates in this release are fully backwards-compatible.