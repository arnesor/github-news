# GitHub New Releases Report 2026-08-11

**[wntrblm/nox 2026.08.10](https://github.com/wntrblm/nox/releases/tag/2026.08.10)**

### Overview
Nox release `2026.08.10` introduces experimental parallel session execution alongside a new `python-discovery` engine for enhanced interpreter lookup and version specifier support. It also refines CLI option precedence, improves Conda version handling, and enforces stricter global flag validation.

### Highlights
- **Parallel Session Execution**: Run sessions concurrently using `--parallel` / `-j` (requires session opt-in or `--allow-parallel`).
- **Upgraded Python Discovery**: Powered by `python-discovery`, improving interpreter lookup, version specifier sets, and `requires-python` support in script mode.
- **Fixed Option Precedence**: Explicit command-line options now reliably override noxfile and alias default values.

### Breaking Changes
⚠️ **Stricter CLI Option Validation**: Unrecognized global options now result in an error instead of being silently ignored. CI scripts or workflows passing invalid or obsolete flags will need to be updated.