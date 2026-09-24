# GitHub New Releases Report 2026-09-24

**[marimo-team/marimo 0.25.0](https://github.com/marimo-team/marimo/releases/tag/0.25.0)**

### Summary
marimo 0.25.0 introduces an overhauled notebook sandboxing architecture with new Pixi backend support, enabling Conda dependencies and multi-language runtimes. This release also brings portable single-file and offline WebAssembly exports, persistent expanded cell outputs, and faster asynchronous editor startup.

### Highlights
* **Pixi Sandbox Support**: Adds `--sandbox=pixi` alongside default `uv` sandboxes, allowing notebooks to manage Conda packages, native libraries, and non-Python runtimes (such as R) directly via inline metadata.
* **Revamped Sandbox Lifecycle & UI**: Decouples editor startup from kernel environment provisioning for near-instant editor access, complete with in-editor package manifest recovery if environment setup fails.
* **Portable WebAssembly Exports**: Enables exporting interactive WASM notebooks as fully self-contained single-file HTML (`--single-file`) or offline-ready bundles (`--offline`) requiring no internet connection.

### Breaking Changes
No strict breaking API changes, and existing CLI commands remain backwards-compatible. However, the underlying sandbox execution and environment lifecycle have been substantially reworked to run asynchronously per notebook, which may alter behavior in advanced or custom execution workflows.