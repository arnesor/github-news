# GitHub New Releases Report 2026-07-30

**[dynaconf/dynaconf 3.3.4](https://github.com/dynaconf/dynaconf/releases/tag/3.3.4)**

### Dynaconf 3.3.4 Release Summary

**Summary**
Dynaconf 3.3.4 is a maintenance patch release focused on resolving key resolution issues, CLI edge cases, and framework integration bugs. It improves settings merge cleanup, path parsing reliability, and Django early validation behavior without introducing breaking changes.

**Highlights**
* **CLI Initialization Fix:** Resolved an issue where passing list values for `env` during `dynaconf init` resulted in an error (#1278, #1421).
* **Path & Token Merging:** Fixed settings resolution to keep sibling keys sharing a dotted path leaf name (#1434) and cleaned up nested `dynaconf_merge` tokens when parent keys are new (#1435).
* **Django Integration:** Corrected a bug in the Django early validation integration flow (#1432).

**Breaking Changes**
None. This is a backward-compatible patch release.