# GitHub New Releases Report 2026-07-14

**[narwhals-dev/narwhals v2.24.0](https://github.com/narwhals-dev/narwhals/releases/tag/v2.24.0)**

### Narwhals v2.24.0 Release Summary

**Summary**
Narwhals v2.24.0 introduces key usability enhancements, including the new `nw.list` function and broader, more flexible schema definition support. Crucially, this release also resolves potential SQL injection vulnerabilities alongside compatibility updates for PyArrow v25.

**Highlights**
* 🔒 **Security Hardening**: Patched potential SQL injection vulnerabilities in both `sink_parquet` (#3783) and `join_asof` (#3782) operations.
* 🚀 **New `nw.list` Function**: Added native `nw.list` (#3694) support, expanding Narwhals' capabilities for handling list-type data.
* 🛠️ **Improved Schema Flexibility**: Widened `IntoSchema` to seamlessly accept `IntoDType` values and sequences of `(name, dtype)` pairs (#3756), simplifying dtype mapping workflows.

**Breaking Changes**
* None reported in this release.