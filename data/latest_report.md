# GitHub New Releases Report 2026-07-11

**[marimo-team/marimo 0.23.14](https://github.com/marimo-team/marimo/releases/tag/0.23.14)**

### Summary
Marimo v0.23.14 introduces powerful new features including anywidget composition with hot-reloading, an experimental debugger with per-line execution timing, and major upgrades to the AI assistant. It also brings cached WASM exports, allowing published interactive notebooks to instantly hydrate cell outputs from a bundled cache instead of recomputing them in the browser.

### Highlights
*   **Anywidget Composition & Hot Reloading:** Parent widgets can now render child widgets passed as values. Frontend widget code hot-reloads instantly in place, preserving widget state during live edits.
*   **Experimental Debugger & Per-Line Timing:** A new experimental execution lifecycle adds frame-watching to highlight running code, support breakpoints, and display a helpful elapsed-time pill on any line executing for over ~500ms.
*   **Upgraded AI Assistant & WASM Caching:** The AI chat panel now supports web search, prompt caching, and a "Fix in Chat" tool that imports error tracebacks as context. Additionally, `marimo export html-wasm --execute` can now bundle runtime caches to run heavy computations (like PyTorch or JAX) instantly in-browser.

### Breaking Changes
None. All features are backwards-compatible, and new caching/debugging execution lifecycles are strictly opt-in.