# GitHub New Releases Report 2026-08-15

**[astral-sh/uv 0.12.5](https://github.com/astral-sh/uv/releases/tag/0.12.5)**

### Summary
uv 0.12.5 introduces support for recent CPython patch releases, credential redaction in requirement URLs, and new preview capabilities for package indexes and SBOM exports. The release also refines Python interpreter selection prioritization and fixes relative index path resolution in PEP 723 scripts.

### Highlights
- **Credential Redaction & Clearer Errors:** Automatically redacts credentials in requirement URLs and improves error reporting for invalid editable requirements.
- **Named Index Selection (Preview):** Adds the `index-by-name` preview flag, allowing `--index` and `--default-index` to select configured package indexes by name.
- **SBOM Enhancements & CPython Updates:** Includes distribution artifact URLs and hashes by default in CycloneDX SBOM exports, alongside support for CPython 3.10.21, 3.11.16, and 3.12.14.

### Breaking Changes
None.