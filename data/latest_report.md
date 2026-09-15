# GitHub New Releases Report 2026-09-15

**[astral-sh/uv 0.12.14](https://github.com/astral-sh/uv/releases/tag/0.12.14)**

### Summary
uv 0.12.14 introduces standardized diagnostics and differentiated exit codes for package operations, alongside support for resuming interrupted HTTP downloads. The release also brings notable performance optimizations across dependency resolution workflows and resolves platform-specific installation edge cases.

### Highlights
- **Resumable Downloads:** Large downloads can now resume via HTTP Range requests when supported, improving reliability on unstable network connections.
- **Resolution Performance Gains:** Accelerated dependency resolution across the board with background parsing for large index responses, streamlined local wheelhouse metadata inspection, and faster warm-cache decoding.
- **Standardized Error Diagnostics:** Package-operation errors now feature compact, labeled cause chains and actionable hints, including dedicated resolver hints when `uv tool upgrade` fails.

### Breaking Changes
⚠️ **Exit Code Semantics Changed:** Package-operation commands no longer return a uniform error code across all failures. Expected failures return exit code `1`, while recognized operational and internal errors now return `2`. Update any CI/CD scripts or wrapper tools that explicitly assert an exit code of `1`.