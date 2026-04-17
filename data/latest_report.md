# GitHub New Releases Report 2026-04-17

**[astral-sh/ruff 0.15.11](https://github.com/astral-sh/ruff/releases/tag/0.15.11)**

Ruff 0.15.11 introduces a new linting rule for Airflow and several refinements to async and security rules to reduce false positives. This patch release also streamlines Neovim integration by updating LSP configuration examples to the modern standard.

### Highlights
* **New Airflow Rule (`AIR201`)**: Implements `airflow-xcom-pull-in-template-string` to identify suboptimal XCom usage in template strings.
* **Reduced Linting Noise**: Improved handling of `asynccontextmanager` for `RUF029` and overridden methods for `ASYNC109` to prevent incorrect warnings.
* **Security Rule Improvements**: Enhanced mask analysis for `S103` (flake8-bandit) to accurately detect insecure file permissions while reducing false reports.

### Breaking Changes
None.