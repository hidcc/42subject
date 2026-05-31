install:
	uv venv
lint:
	uv run ruff check src
	uv run mypy src
format:
	uv run ruff format src
	uv run ruff check --fix src
clean:
	rm -rf data/processed data/output
	find . -type d -name __pycache__ -exec rm -rf {} +

.PHONY: install lint format clean