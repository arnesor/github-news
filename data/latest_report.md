# GitHub New Releases Report 2026-06-14

**[pytest-dev/pytest 9.1.0](https://github.com/pytest-dev/pytest/releases/tag/9.1.0)**

### Pytest 9.1.0 Release Analysis 🚀

**Summary**
Pytest 9.1.0 delivers official support for Python 3.15, introduces highly requested configuration options, and refines fixture resolution mechanics. This release also actively deprecates several legacy behaviors and APIs to pave a smooth transition path toward pytest 10.

**Highlights**
*   **New Assertion & Comparison Features**: Adds the `assertion_text_diff_style` configuration option to render string equality failures as clean `Left:` and `Right:` blocks instead of `ndiff` output. Additionally, `pytest.approx` now supports comparing `datetime` and `timedelta` objects (with explicit tolerance).
*   **Strict Warning Limits**: Introduces the `--max-warnings` command-line flag (and matching `max_warnings` ini option) to fail test runs immediately when a specified warning threshold is crossed.
*   **Imperative Fixture Registration**: Adds `pytest.register_fixture()`, providing an advanced programmatic interface for plugins to register fixtures dynamically when the declarative `@pytest.fixture` decorator is unviable.

**Breaking Changes & Key Deprecations**
*   ⚠️ **Doctest Autouse Double-Execution**: Using `--doctest-modules` with inline-defined autouse fixtures (`module`, `package`, or `session` scope) may cause them to execute twice. Prevent this by moving these fixtures to a `conftest.py` file.
*   ⚠️ **Deprecations (Targeted for removal in Pytest 10)**:
    *   Class-scoped fixtures defined as instance methods without `@classmethod`.
    *   Calling `request.getfixturevalue()` during teardown for fixtures not already requested.
    *   Using non-`Collection` iterables (like generators/iterators) in `@pytest.mark.parametrize`.
    *   The private `config.inicfg` attribute (use `config.getini()` instead).
    *   `pytest.console_main` (use `pytest.main` instead).