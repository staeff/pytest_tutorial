SHELL := /bin/bash
APP_DIR := .
VENV := ./.venv
BIN := $(VENV)/bin
PYTHON := $(BIN)/python

.PHONY: help
help: ## Show this help
	@grep -Eh '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: venv
venv: ## Make a new virtual environment
	python3 -m venv $(VENV)

.PHONY: install
install: venv ## Make venv and install requirements
	$(BIN)/pip install -r requirements.txt

.PHONY: update
update: ## Update requirements using pip-compile
	$(BIN)/pip-compile requirements.in
	$(BIN)/pip install -r requirements.txt

.PHONY: setup
setup: venv install ## Set up the repo, create venv, install requirements

.PHONY: test
test: ## Run tests
	$(BIN)/pytest \
		--cov \
		--cov-report=term-missing \
		--cov-report html:coverage \
		-x \
		$(args)

.PHONY: format
format: ## Format code with isort/black
	$(BIN)/isort .
	$(BIN)/black **/*.py
