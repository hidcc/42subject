install:
	uv sync --extra dev
run:
	uv run python -m
debug:
	uv eun python -m pdb
clean:
	rm -rf
lint:
	uv run flake8 .
	uv run mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
lint-strict:
	uv run flake8 .
	uv run mypy . --strict
