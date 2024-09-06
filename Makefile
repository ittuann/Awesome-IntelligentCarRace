MAKEFLAGS = --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

.PHONY: build serve live-serve install lint pre-commit unit-tests

.DEFAULT_GOAL := build

build:
	python -m scripts.split
	python -m scripts.build

serve:
	python -m http.server --directory site 8000 --bind localhost

live-serve:
	mkdocs serve -f ./docs/mkdocs.yml

install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

lint:
	black --color --diff ./scripts
	autoflake --remove-all-unused-imports --remove-unused-variables --recursive ./scripts
	ruff check --fix .
	mypy ./scripts
	pyupgrade --py311-plus ./scripts/build.py

pre-commit:
	pre-commit run --verbose --all-files

unit-tests:
	pytest
