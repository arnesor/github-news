# GitHub New Releases Report 2026-02-12

**[astral-sh/uv 0.10.2](https://github.com/astral-sh/uv/releases/tag/0.10.2)**

# uv 0.10.2 Release Notes

### Summary
`uv` v0.10.2 is a focused patch release addressing a build-time dependency issue and refining archive handling consistency. This update ensures a smoother installation experience for users building from source while deprecating non-standard ZIP compression methods to improve reliability.

### Highlights
- **Cargo Installation Fix**: Resolved a failure where `cargo-install` would fail due to a missing `uv-test` dependency, restoring the ability to build and install from source via Rust's toolchain.
- **Archive Refinement**: Deprecated unexpected ZIP compression methods to maintain high compatibility and ensure predictable behavior during package extraction.

### Breaking Changes
- No breaking changes are introduced in this release.
---
**[cjolowicz/nox-poetry v1.2.0](https://github.com/cjolowicz/nox-poetry/releases/tag/v1.2.0)**

### Summary
`nox-poetry` v1.2.0 modernizes the project’s build pipeline and improves security compliance for strictly regulated environments. This update also streamlines CI/CD workflows and aligns the tool with the latest Python and Poetry ecosystems.

### Highlights
* **FIPS Compliance:** Added support for FIPS-compliant environments by configuring `blake2b` hashing with `usedforsecurity=False`.
* **PEP 517 Build Frontend:** The project now utilizes the `build` package as the standard frontend for package creation, following modern Python packaging standards.
* **Updated Support Matrix:** Enhanced the testing suite for the latest Poetry versions and updated documentation builds to use Python 3.13 and Ubuntu 24.04.

### ⚠️ Breaking Changes
* **Dropped Python 3.8 Support:** Support for Python 3.8 has been removed. Users must migrate to Python 3.9 or newer to use this version.
---
**[dynaconf/dynaconf 3.2.12](https://github.com/dynaconf/dynaconf/releases/tag/3.2.12)**

## Dynaconf 3.2.12

### Summary
Dynaconf 3.2.12 is a maintenance release focused on performance optimizations and type hint accuracy. This update introduces internal caching and refined access logic to speed up configuration lookups in Python applications.

### Highlights
- **LRU Caching for Performance**: Implemented LRU caching in the `find_the_correct_casing` function, significantly reducing overhead for repeated configuration lookups.
- **Type Hint Refinement**: Fixed the `get` method to return the `Any` type, ensuring better compatibility with static analysis tools like Mypy and improving IDE autocompletion.
- **Access Speed Improvements**: General incremental enhancements to core access performance to streamline configuration retrieval.

### Breaking Changes
- **None**: This is a patch release and maintains full backward compatibility.

### Priority
Bugfix
---
**[pandas-dev/pandas v3.0.0](https://github.com/pandas-dev/pandas/releases/tag/v3.0.0)**

### 📦 pandas v3.0.0

Pandas 3.0.0 is a milestone major release that introduces fundamental changes to data handling, including default Copy-on-Write and specialized string types. It focuses on improving performance, ensuring consistency, and modernizing the API for Python 3.11+.

#### 🚀 Highlights
* **Copy-on-Write (CoW) by Default**: Consistent behavior for views and copies is now standard, finally eliminating the notorious `SettingWithCopyWarning` and preventing accidental data mutations.
* **Dedicated String Data Type**: High-performance, memory-efficient string storage is now the default, replacing the legacy `object` dtype for text data to provide better performance and smaller memory footprints.
* **New `pd.col` Syntax**: This release introduces initial support for the `pd.col` accessor, laying the groundwork for a more expressive and readable syntax for column selection and manipulation.

#### ⚠️ Breaking Changes
* **Deprecated Feature Removal**: Functionality deprecated throughout the 2.x series has been removed. Users should upgrade to pandas 2.2/2.3 and resolve all `FutureWarning` messages before upgrading to 3.0.
* **Python Requirement**: This version requires **Python 3.11 or higher**.
* **Datetime Resolution**: Changes to the default resolution for datetime-like data may affect how your timestamps are inferred and stored.

#### 🛠️ Installation
```bash
# PyPI
python -m pip install --upgrade pandas==3.0.*

# Conda
conda install -c conda-forge pandas=3.0
```
---
**[pola-rs/polars rs-0.53.0](https://github.com/pola-rs/polars/releases/tag/rs-0.53.0)**

Polars 0.53.0 introduces a massive overhaul of the streaming engine and significant SQL compatibility improvements, headlined by the addition of Extension types. This version focuses on memory efficiency and throughput for large-scale data processing with new sink pipelines and streaming decompression support.

### 🏆 Highlights
* **Extension Types:** Polars now supports Extension types, enabling users to define custom data types to handle domain-specific logic and improve interoperability with external systems.
* **Streaming Engine Evolution:** The streaming engine receives major upgrades, including a new streaming merge-join, streaming decompression for CSV/NDJSON, and dedicated partitioned IO sink pipelines for Parquet and CSV.
* **Advanced SQL Support:** The SQL interface is now much more robust with the addition of the `QUALIFY` and `FETCH` clauses, as well as essential window functions like `ROW_NUMBER`, `RANK`, and `DENSE_RANK`.

### ⚠️ Breaking Changes
While no explicit breaking changes section is provided, this release includes several internal refactorings that may affect low-level integrations. Notable changes include the removal of the old streaming sink implementation, the deprecation of the batched CSV reader, and the renaming of `FileType` to `FileWriteFormat`. Users of the Rust API should note the restructuring of several internal crates (like `polars-buffer`).

### 🚀 Performance Key Gains
* **Parallel IO:** File schemas and metadata are now resolved concurrently, and cloud uploads for IPC sinks utilize zero-copy `object_store` puts.
* **Kernel Optimizations:** New dedicated kernels for group-by `arg_max/arg_min`, faster string slicing, and width-aware chunking to prevent degradation on wide tables.
* **Memory Efficiency:** Reduced memory usage for grouped first/last operations and optimized streaming scans for multiple Parquet files.
---
**[psf/black 26.1.0](https://github.com/psf/black/releases/tag/26.1.0)**

### Release Summary: psf/black 26.1.0
This release introduces the **2026 stable style**, graduating several formatting improvements and bug fixes into the default standard. It also includes a significant update to file-discovery logic by bumping `pathspec` to v1, aligning Black's behavior more closely with Git's `.gitignore` rules.

### Highlights
*   **2026 Stable Style Graduation**: A suite of formatting rules is now stable, including mandatory single blank lines after imports, more compact multiline string expressions, and standardized spacing for type comments.
*   **Git-Compliant File Discovery**: Upgrading to `pathspec` v1 changes how ignored/unignored directories are handled. Black now correctly respects nested `.gitignore` patterns, ensuring its behavior matches Git's own logic.
*   **Syntax & Parentheses Refinement**: The formatter now automatically removes unnecessary parentheses from the left-hand side of assignments and from multiple exception types in `except` blocks, while fixing `# fmt: skip` behavior for one-liner declarations.

### Breaking Changes
*   **Style Shift**: Projects tracking the "stable" style will see formatting changes as the 2026 ruleset is applied. 
*   **Ignore Pattern Changes**: The update to `pathspec` may cause files that were previously formatted to be ignored (or vice versa) depending on your `.gitignore` structure. You may need to update your ignore patterns to maintain previous behavior.
---
**[pytest-dev/pytest 9.0.2](https://github.com/pytest-dev/pytest/releases/tag/9.0.2)**

# pytest 9.0.2 Release Analysis

### Summary
pytest 9.0.2 is a maintenance release focused on resolving regressions and compatibility issues introduced in the 9.0.0 major update. It primarily addresses terminal rendering bugs and restores internal APIs relied upon by the broader ecosystem to ensure tool stability.

### Highlights
*   **Terminal Progress Disabled by Default:** To resolve display issues in various terminal emulators, the new progress feature is now opt-in via `-p terminalprogress` (except on Windows).
*   **Restored `config.inicfg`:** A compatibility shim has been added for the `config.inicfg` attribute, which was inadvertently broken in 9.0.0, supporting plugins that depend on this internal API.
*   **Performance Fix for Subtests:** Resolved a regression causing quadratic-time behavior when handling `unittest` subtests specifically in Python 3.10.

### Breaking Changes
*   **Feature Reversion:** Users on non-Windows systems will notice the terminal progress bar is now hidden by default.
*   **API Deprecation:** While `config.inicfg` is restored for now, it is officially scheduled for deprecation in version 9.1 and removal in version 10.

### Improved Documentation
The API Reference now features cross-referenceable documentation for all command-line flags, making it easier for developers to link to specific pytest behaviors in their own project docs.
---
**[python-poetry/poetry 2.3.2](https://github.com/python-poetry/poetry/releases/tag/2.3.2)**

Poetry 2.3.2 is a targeted maintenance release that updates core dependencies and improves platform detection logic. It primarily focuses on resolving environment parsing issues for Windows users and broadening Git library compatibility.

### Highlights
* **Broader Git Support:** Updated dependency constraints to allow `dulwich>=1.0`, ensuring compatibility with newer versions of the pure-Python Git implementation.
* **Windows Server Fix:** Includes `poetry-core` 2.3.1, which resolves a bug where `platform_release` could not be correctly parsed on Windows Server environments.
* **Improved Environment Markers:** Enhances the reliability of dependency resolution on specific Windows infrastructures by fixing underlying platform metadata parsing.

### Breaking Changes
* None. This is a patch release focused on bug fixes and dependency updates.

### Priority
Bugfix
---
**[unionai-oss/pandera v0.29.0](https://github.com/unionai-oss/pandera/releases/tag/v0.29.0)**

Pandera v0.29.0 introduces support for collection types in type-hinted functions, allowing for the validation of lists, dictionaries, and tuples containing DataFrames. This release also broadens the Ibis engine's functionality with new datatype support and includes key maintenance updates for documentation stability.

### 🚀 Highlights
* **Collection Type Support**: The `@pa.check_types` decorator now validates complex structures like `tuple[DataFrame[Schema], ...]` or `dict[str, DataFrame[Schema]]`. This is a major quality-of-life improvement for pipelines handling multiple data assets simultaneously.
* **Ibis Engine Map Support**: Added the `map` datatype to the Ibis engine implementation, improving schema parity for users working with backend-agnostic data definitions via Ibis.
* **Doc Build Stability**: Updated infrastructure by pinning the Sphinx version to prevent build regressions and ensure documentation consistency for the community.

### ⚠️ Breaking Changes
* None reported in this release.
---
**[wntrblm/nox 2026.02.09](https://github.com/wntrblm/nox/releases/tag/2026.02.09)**

### Nox 2026.02.09 Release Analysis

#### Summary
Nox 2026.02.09 is a maintenance release primarily focused on ensuring compatibility with the latest `uv 0.10.0` update and refining internal session handling. It notably re-adds support for Python 3.8 to maintain alignment with current `uv` capabilities while providing several developer experience improvements.

#### Highlights
*   **uv 0.10.0 Compatibility:** Updated the `uv` backend to support the new requirement of passing the `--clear` flag when refreshing environments.
*   **Improved Session Decorators:** Enhanced support for using multiple session decorators on a single function, resolving previous handling limitations.
*   **Enhanced Type Safety:** Provided better typing for the `.run()` method, improving the development experience for users relying on static analysis and IDE autocompletion.

#### Breaking Changes
None. While Python 3.8 support was slated for removal, it has been **temporarily restored** in this version to match `uv`'s support lifecycle.

#### Priority
Bugfix