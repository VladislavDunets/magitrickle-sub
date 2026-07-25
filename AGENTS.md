# Repository Guidelines

## Project Structure & Module Organization

- `scripts/build.py` is the generator. It downloads v2fly domain categories and official Telegram CIDRs, normalizes them, and writes subscription files.
- `sources/config.json` defines upstream URLs, excluded attributes, subscription names, v2fly categories, and manual domain additions.
- `subscriptions/*.txt` contains generated MagiTrickle inputs. Treat these files as build artifacts; change the generator or configuration instead of editing them directly.
- `.github/workflows/update-subscriptions.yml` runs the generator daily, on demand, and when generator-related files change.
- `README.md` documents public raw URLs and end-user behavior.

There is currently no separate test or asset directory. Add focused tests under `tests/` if generator logic grows beyond straightforward validation.

## Build, Test, and Development Commands

Use Python 3.12 to match GitHub Actions. The project uses only the standard library, so no dependency installation is required.

```bash
python scripts/build.py
python -m py_compile scripts/build.py
git diff -- subscriptions/
```

The first command regenerates all lists and requires network access. The second performs a fast syntax check. Always inspect the generated diff; unexpected large removals, empty lists, or malformed CIDRs should block a change.

## Coding Style & Naming Conventions

Follow PEP 8 with four-space indentation, type hints, descriptive `snake_case` functions and variables, and `UPPER_SNAKE_CASE` constants. Keep network access and parsing errors actionable. Preserve UTF-8 and deterministic, sorted output.

Use lowercase kebab-case for subscription names (for example, `telegram-ip`), which map directly to `subscriptions/<name>.txt`. Keep JSON keys and Python identifiers in snake_case.

## Testing Guidelines

No test framework or coverage threshold is configured. Before submitting changes, run the generator and syntax check above. Verify that every generated file has its header, contains rules, is sorted, and has no unintended duplicates. For parsing changes, add unit tests using `unittest` and name files `tests/test_<feature>.py`; avoid live-network dependencies in unit tests.

## Commit & Pull Request Guidelines

Prefer concise imperative commits, optionally using Conventional Commit prefixes seen in history, such as `chore: update subscriptions`. Keep generated output in the same commit as its source/configuration change.

Pull requests should explain the motivation, identify affected subscriptions, summarize validation commands, and call out upstream-source changes. Link relevant issues. Include generated diffs or rule-count changes; screenshots are unnecessary for this text-only repository.
