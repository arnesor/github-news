# GitHub New Releases Report 2026-09-17

**[astral-sh/ruff 0.16.8](https://github.com/astral-sh/ruff/releases/tag/0.16.8)**

### Summary
Ruff 0.16.8 introduces forward-looking support for Python 3.15 lazy imports alongside PEP 728 `TypedDict` class keywords. This release also refines several type-checking and `pyupgrade` rules while introducing flexible banned-API configuration options.

### Highlights
- **Python 3.15 & Lazy Import Support**: Added detection for `__lazy_modules__` and updated `flake8-type-checking` (`TC001`–`TC003`) to prefer lazy imports over `TYPE_CHECKING` blocks on Python 3.15+.
- **Modern Typing Additions**: Added recognition for PEP 728 `TypedDict` class keyword arguments and quoted type expressions inside `typing.TypeForm`.
- **Expanded Configuration**: Added `extend-banned-api` to `flake8-tidy-imports`, allowing projects to append to existing banned API lists without overriding parent configurations.

### Breaking Changes
None. Note that the autofix for `UP040` (type alias syntax) is now categorized as unsafe and will no longer apply automatically without the `--unsafe-fixes` flag.