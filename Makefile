MAKEFLAGS = --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

.PHONY: build serve live-serve install lint format pre-commit unit-tests

.DEFAULT_GOAL := build

build:
	python -m scripts.split
	python -m scripts.build

serve:
	python -m http.server --directory site 8000 --bind localhost

live-serve:
	mkdocs serve -f ./docs/mkdocs.yml

install:
	python -m pip install ".[dev]"
	pre-commit install

lint:
	ruff check --fix .
	mypy scripts tests

format:
	black --color .

pre-commit:
	pre-commit run --verbose --all-files

unit-tests:
	pytest
