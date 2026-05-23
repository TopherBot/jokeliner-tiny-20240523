# jokeliner‑tiny‑20240523

**A one‑file‑plus‑metadata tiny CLI** that prints a random joke.

```bash
# Install (requires Python ≥3.9)
pip install .

# Run the tool (installed as `jokeliner`)
jokeliner            # prints a joke
jokeliner --no‑color # plain‑text output
```

## What it does
* Calls https://v2.jokeapi.dev/joke/Any?type=single
* Shows the joke on stdout.
* Optional `--no-color` flag disables coloured output.

## Why this is a good tiny starter
* Uses **PEP 621**‑style `pyproject.toml` (no `setup.py`).
* `src/` layout – the modern recommended structure.
* Click provides a pleasant CLI with auto‑generated `--help`.
* Includes a short test using `pytest`.
* MIT‑licensed – free for any use.

## Development workflow (optional)
```bash
# Install in editable mode with dev deps
pip install -e .[dev]

# Run the test suite
pytest -q
```

---
*Happy coding!*