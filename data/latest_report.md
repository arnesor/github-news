# GitHub New Releases Report 2026-04-13

**[python-poetry/poetry 2.3.4](https://github.com/python-poetry/poetry/releases/tag/2.3.4)**

### Summary
Poetry 2.3.4 is a critical maintenance update focusing on performance recovery and security hardening. This release addresses a significant installation slowdown introduced in the previous version and patches a path traversal vulnerability for users on specific Python 3.10 and 3.11 environments.

### Highlights
- **Performance Restoration:** Fixes a regression in the wheel installer introduced in Poetry 2.3.3, ensuring package installation speeds return to expected levels.
- **Security Patch (Path Traversal):** Addresses a vulnerability in `sdist` extraction that could allow malicious tarballs to write files outside the target directory. 
- **Targeted Environments:** The security fix specifically protects users running Poetry on Python versions 3.10.0–3.10.12 and 3.11.0–3.11.4.

### Breaking Changes
- **None:** This is a patch release focused exclusively on fixes and contains no breaking changes to the API or CLI.

### Priority
This is a **high-priority bugfix** release. Users on Python 3.10 or 3.11 should update immediately to mitigate security risks, while all other users will benefit from the restored wheel installation performance.