# GitHub New Releases Report 2026-04-28

**[astral-sh/uv 0.11.8](https://github.com/astral-sh/uv/releases/tag/0.11.8)**

### Summary
uv 0.11.8 enhances Python version management and lockfile stability while introducing several new environment variables for better environment isolation. This update also addresses edge cases in dependency resolution and improves security by hardening wheel extraction against external symlinks.

### Highlights
* **Advanced Python Discovery:** New configuration options like `UV_PYTHON_SEARCH_PATH` and `UV_PYTHON_NO_REGISTRY` provide granular control over how uv locates and identifies Python interpreters on the host system.
* **Refined Lockfile Logic:** Improved handling of `exclude-newer` fields and the introduction of sentinel timestamps ensure more stable and predictable cross-platform lockfiles, even when using relative time spans.
* **CLI & Scripting Improvements:** This release adds `pip uninstall -y` compatibility for easier automation, a `--short` flag for `uv self version`, and shifts `self-update` to use the Astral mirror for better reliability.

### Breaking Changes
None reported. Note a **notable behavior change**: uv now disables transparent Python upgrades in projects when a specific patch version is requested via `.python-version`, ensuring stricter adherence to pinned versions.

### Priority