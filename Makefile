# Use bash for all commands
SHELL := /bin/bash

# Define the virtual environment directory and executables
VENV_DIR := .venv
PYTHON := $(VENV_DIR)/bin/python
SPHINX := $(VENV_DIR)/bin/sphinx-build

# Phony targets don't represent files
.PHONY: help setup generate preview clean

# Default target: Show help message
help:
	@echo "Available commands:"
	@echo "  setup      - Create a virtual environment and install dependencies using uv."
	@echo "  generate   - Generate RST documentation from product YAML files."
	@echo "  preview    - Build the HTML documentation for local preview."
	@echo "  clean      - Remove the virtual environment and all generated files."

# Target to set up the development environment
setup:
	@if ! command -v uv &> /dev/null; then \
		echo "Error: 'uv' is not installed. Please install it first:"; \
		echo "  sudo snap install astral-uv --classic"; \
		exit 1; \
	fi
	@echo "--> Creating virtual environment in $(VENV_DIR)..."
	@uv venv $(VENV_DIR)
	@echo "--> Installing dependencies from requirements.txt..."
	@uv pip install -r requirements.txt --python $(PYTHON)
	@echo "✅ Setup complete. You can now run 'make generate'."

# Target to generate the RST files
generate:
	@echo "--> Generating RST files from product definitions..."
	@$(PYTHON) scripts/build_product_pages.py

# Target to build the local HTML preview
preview: generate
	@echo "--> Building HTML documentation..."
	@$(SPHINX) docs docs/_build/html
	@echo "✅ Build complete. Open docs/_build/html/index.html in your browser."

# Target to clean up the project
clean:
	@echo "--> Cleaning up generated files and virtual environment..."
	@rm -rf $(VENV_DIR)
	@rm -rf docs/_build
	@rm -rf docs/products