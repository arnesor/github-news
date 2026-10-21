# GitHub New Releases Report 2026-10-21

**[astral-sh/uv 0.13.4](https://github.com/astral-sh/uv/releases/tag/0.13.4)**

### Summary
uv 0.13.4 is an urgent security release addressing a compromised root Certificate Authority intermediate on the Web PKI. Users are strongly encouraged to upgrade immediately to refresh their bundled root certificates and ensure secure operations.

### Highlights
- **Critical Security Fix ([GHSA-hq85-5cpj-mr62](https://github.com/astral-sh/uv/security/advisories/GHSA-hq85-5cpj-mr62)):** Removes trust for a compromised root CA intermediate on the Web PKI.
- **Updated Root Certificates:** Updates bundled Mozilla root certificates via `webpki-root-certs` 1.0.10.
- **PEP 825 Validation (Preview):** Adds validation for PEP 825 variant metadata under the `wheel-variants` preview feature, treating invalid metadata versions as unavailable.

### Breaking Changes
None.
---
**[wntrblm/nox 2026.10.20](https://github.com/wntrblm/nox/releases/tag/2026.10.20)**

### Summary
Nox 2026.10.20 graduates parallel execution out of experimental status with `session.parallel` introspection and introduces a high-performance `rattler` backend powered by `py-rattler`. This release also enhances PEP 723 script mode, adds support for free-threaded Python builds, and expands `@nox.parametrize` capabilities.

### Highlights
* **Stabilized Parallel Execution:** Dropped the "experimental" banner from `--parallel`, introduced ASCII header fallbacks, and exposed `session.parallel` so sessions can conditionally detect if they are running inside a parallel worker.
* **New `rattler` Backend:** Added support for fast conda-style environments via `py-rattler` (available via `nox[rattler]`), complete with default config resolution and support inside `/// script` blocks.
* **Modern Python & Parametrization Enhancements:** Added support for free-threaded Python builds parsed from classifiers, updated the bundled GitHub Action to default to Python 3.11–3.15, and enabled `@nox.parametrize` to accept ranges and arbitrary iterators for single arguments.

### Breaking Changes
None. Existing Nox configurations remain backward-compatible, though teams utilizing the official GitHub Action should verify that its updated default matrix (Python 3.11–3.15) matches their test targets.