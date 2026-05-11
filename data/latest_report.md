# GitHub New Releases Report 2026-05-11

**[astral-sh/uv 0.11.13](https://github.com/astral-sh/uv/releases/tag/0.11.13)**

uv version 0.11.13 is a maintenance update that resolves key issues in build consistency and security verification for Python projects. It also extends support for the latest Python development cycles by adding CPython 3.14.5.

### Highlights
1. **Editable Build Improvements:** Correctly includes data files in editable builds, ensuring development environments accurately mirror production installations.
2. **Lockfile Security:** Fixes a critical bug to ensure the `--require-hashes` flag is strictly respected when installing dependencies from `pylock.toml` files.
3. **Expanded Python Support:** Adds official support for CPython 3.14.5, keeping the toolchain compatible with the latest experimental and upcoming Python releases.

### Breaking Changes
None.