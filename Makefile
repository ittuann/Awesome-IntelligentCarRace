MAKEFLAGS = --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

.PHONY: build serve install lint unit-tests

.DEFAULT_GOAL := build

build:
	python ./scripts/split.py
	python ./scripts/build.py

serve:
	python -m http.server --directory site 8000 --bind localhost

install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

lint:
	black --color --diff ./scripts
	ruff check --fix .
	mypy ./scripts
	autoflake --remove-all-unused-imports --remove-unused-variables --recursive ./scripts

unit-tests:
	coverage run -m pytest
	coverage report
	coverage xml && coverage html
