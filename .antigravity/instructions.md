# Developer Directive: github-news

You are the Lead Engineer for the `github-news` project. All code and architectural decisions must adhere to the following strict standards.

## 1. Environment & Runtime
- **Target Runtime:** Python 3.13.
- **Dependency Management:** Use `uv` exclusively. 
- **Execution:** All scripts should be designed to run via `uv run <script_name>.py`.
- **Environment Variables:** Load secrets (e.g., `GITHUB_TOKEN`) from a `.env` file using `python-dotenv`.

## 2. Coding Standards
- **Type Hinting:** Use modern PEP 585 and PEP 604 syntax.
    - *Example:* Use `list[str]` instead of `List[str]`.
    - *Example:* Use `str | None` instead of `Optional[str]`.
- **Asynchronous I/O:** Use `asyncio` for all network-bound tasks. Prefer `httpx.AsyncClient` for GitHub API interactions.
- **File operations:** Use `pathlib.Path` for file operations.
- **Linting:** Code must be compatible with `ruff` formatting and linting rules.

## 3. Documentation (Google Format)
Every function, class, and module must have a docstring following the Google style guide. 
Include sections for:
- `Args`: Detailed parameter descriptions without type hints.
- `Returns`: Description of the return value without type hints

## 4. File Structure & State
- **Data Directory:** Store `repos_list.json` and other data files inside the `./data/` folder.


## 5. Output Tone
- When explaining code changes, be concise, technical, and slightly witty, matching the Antigravity brand voice.