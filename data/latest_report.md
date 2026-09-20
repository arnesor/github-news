# GitHub New Releases Report 2026-09-20

**[python-poetry/poetry 2.5.0](https://github.com/python-poetry/poetry/releases/tag/2.5.0)**

### Summary
Poetry 2.5.0 brings major performance optimizations across dependency resolution, CLI startup times, and wheel installation, alongside official support for Python 3.15. This release also tightens credential security and introduces a native uninstaller to bypass calling `pip uninstall`.

### Highlights
- **Significant Performance Upgrades:** Major speedups across dependency resolution, wheel selection, repository page processing, schema validation caching, and faster CLI startup via deferred imports.
- **Credential Security Hardening:** Prevents credentials configured for `https` from being leaked over unencrypted `http`, and fixes cross-repository credential mixing on shared hosts.
- **Built-in Uninstaller:** Adds the `installer.builtin-uninstall` setting, enabling package removals using Poetry's internal uninstaller instead of delegating to `pip`.

### Breaking Changes
- **Stricter Python Compatibility Checks:** If `virtualenvs.create` is set to `false`, Poetry will now hard-fail with an error if the running Python environment does not satisfy the project's Python version constraints.
- **HTTPS Credential Restrictions:** Any credentials configured for HTTPS endpoints will strictly no longer be transmitted over unencrypted HTTP requests.