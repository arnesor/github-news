### Project Overview
`github-news` is a utility to monitor GitHub repositories for new releases and generate a summarized report.

### Build and Configuration Instructions

#### Prerequisites
- Python 3.13+
- [uv](https://github.com/astral-sh/uv)

#### Installation
1. Install dependencies:
   ```bash
   uv sync
   ```

#### Environment Variables
Create a `.env` file in the root directory with the following content:
```env
GITHUB_TOKEN=your_github_personal_access_token
```
A GitHub token is required to avoid rate limiting and access the API.

### 1. Environment & Runtime
- **Target Runtime:** Python 3.13.
- **Dependency Management:** Use `uv` exclusively. 
- **Execution:** All scripts should be designed to run via `uv run <script_name>.py`.
- **Environment Variables:** Load secrets (e.g., `GITHUB_TOKEN`) from a `.env` file using `python-dotenv`.

### 2. Coding Standards
- **Type Hinting:** Use modern PEP 585 and PEP 604 syntax.
    - *Example:* Use `list[str]` instead of `List[str]`.
    - *Example:* Use `str | None` instead of `Optional[str]`.
- **Asynchronous I/O:** Use `asyncio` for all network-bound tasks. Prefer `httpx.AsyncClient` for GitHub API interactions.
- **File operations:** Use `pathlib.Path` for file operations.
- **Linting:** Code must be compatible with `ruff` formatting and linting rules.

### 3. Documentation (Google Format)
Every function, class, and module must have a docstring following the Google style guide. 
Include sections for:
- `Args`: Detailed parameter descriptions without type hints.
- `Returns`: Description of the return value without type hints

### Testing Information

#### Running Tests
This project uses the `pytest` framework. To run the tests, use:
```bash
uv run pytest
```

#### Adding New Tests
When adding new tests, follow these guidelines:
- Place test files in the root or a `tests/` directory (if created).
- Name test files with the `test_` prefix (e.g., `test_logic.py`).
- Use `pytest-mock` to mock external API calls (especially GitHub API).

### Additional Development Information

#### Code Style and Quality
The project uses `ruff` for linting/formatting and `mypy` for type checking.
- **Linting/Formatting**: Run `uv run ruff check --fix .` and `uv run ruff format .`
- **Type Checking**: Run `uv run mypy .`

#### Configuration Files
- `pyproject.toml`: Contains dependencies, ruff configuration, and mypy settings.
- `data/repos_list.csv`: List of GitHub repository URLs to check.
- `data/known_releases.json`: Automatically updated file storing the last seen release for each repo.

#### Development Workflow
1. Add new repositories to `data/repos_list.csv`.
2. Run `python check_releases.py` to check for updates.
3. If new releases are found, they will be printed in the console and `data/known_releases.json` will be updated.
