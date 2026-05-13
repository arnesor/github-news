# GitHub New Releases Report 2026-05-13

**[astral-sh/uv 0.11.14](https://github.com/astral-sh/uv/releases/tag/0.11.14)**

## uv v0.11.14 Release Summary

`uv` 0.11.14 delivers targeted improvements to environment handling and dependency visualization alongside a new mirror override feature. This release fixes several edge cases in lock validation and uninstallation logic to improve overall tool reliability.

### Highlights

* **Astral Mirror Overrides:** Adds support for overriding the Astral mirror URL (#19206), facilitating easier use in restricted, air-gapped, or internal network environments.
* **Better `.env` Isolation:** Fixed an issue where `.env` files were being applied in the parent process (#19343), ensuring cleaner environment management and preventing side effects.
* **`uv tree` Accuracy:** Corrected a bug where conditional dependencies were displayed in the tree view even when the parent package was required without those specific extras (#19332).

### Breaking Changes

No breaking changes were introduced in this release.