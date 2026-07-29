# GitHub New Releases Report 2026-07-29

**[astral-sh/uv 0.12.0](https://github.com/astral-sh/uv/releases/tag/0.12.0)**

### Astral uv v0.12.0 Release Summary

**Summary**
uv 0.12.0 introduces key updates to improve correctness, security compliance, and developer experience across the Python toolchain. While many changes are defensively marked as breaking—such as stricter package validation, security hardening, and layout updates—most existing user workflows will upgrade seamlessly.

**Highlights**
- **Default Build Systems (`uv init`)**: `uv init` now configures `uv_build` by default, generating a packaged `src/` layout with executable entry points out of the box.
- **Improved Pre-release Resolution**: The dependency resolver now defaults to `if-necessary` mode, gracefully handling transitively requested pre-releases while continuing to prefer stable releases.
- **Script-Relative Project Discovery**: Executing `uv run path/to/script.py` now discovers project settings and virtual environments relative to the script's location instead of the current working directory.

**Breaking Changes**
⚠️ **Yes, breaking changes are present:**
- **Package Layout**: `uv init` defaults to a packaged layout with `uv_build` (use `--no-package` for the legacy layout).
- **Format & Archive Restrictions**: Deprecated archive formats (`.tar.bz2`, `.tar.xz`) and non-standard wheel compressions (bzip2, LZMA) are now rejected.
- **Interpreter Security**: Rejects wheels containing case-variant executable entry points (e.g., `Python.exe`) or `.data` files that could overwrite the environment's interpreter.
- **Hash & Lockfile Enforcement**: Reject MD5-only digests in `--require-hashes` mode; strictly validate `pylock.toml` structure, filenames, and reported artifact sizes.
- **Path Resolution**: Relative indexes resolve against `--directory`, and path arguments passed to `uv add` preserve their original relative/absolute forms.