# GitHub New Releases Report 2026-08-30

**[python-poetry/poetry 2.4.2](https://github.com/python-poetry/poetry/releases/tag/2.4.2)**

### Summary
Poetry 2.4.2 is a security and maintenance release addressing multiple path traversal vulnerabilities during package downloads and source distribution extraction. It also fixes a lockfile integrity bug where unlisted artifacts could be installed if the source lacked artifact hashes.

### Highlights
- **Path Traversal in Downloads**: Patched a vulnerability that allowed path traversal when downloading files from compromised URLs or package sources ([#11029](https://github.com/python-poetry/poetry/pull/11029)).
- **Path Traversal in sdist Extraction**: Resolved a security issue on Python 3.10.0–3.10.12 and 3.11.0–3.11.4 where malicious tarballs could extract files outside the target directory ([#11027](https://github.com/python-poetry/poetry/pull/11027)).
- **Lockfile Enforcement**: Fixed a bug where Poetry installed artifacts not present in the lockfile when the package source did not provide a hash ([#11030](https://github.com/python-poetry/poetry/pull/11030)).

### Breaking Changes
None. This is a non-breaking patch release focused on security and bug fixes.