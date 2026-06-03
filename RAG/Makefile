install:
	uv sync --extra dev

run:
	uv run python -m student

debug:
	uv run python -m pdb -m student

lint:
	uv run flake8 .
	uv run mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	uv run flake8 .
	uv run mypy . --strict

format:
	uv run ruff format src
	uv run ruff check --fix src

serve:
	uv run uvicorn student.api:app --host 127.0.0.1 --port 8000

clean:
	rm -rf data/processed data/output
	find . -type d -name __pycache__ -exec rm -rf {} +
	rm -rf .mypy_cache .ruff_cache

.PHONY: install run debug serve lint lint-strict format clean
