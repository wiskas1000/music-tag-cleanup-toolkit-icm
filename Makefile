# Project-wide Makefile
# Variables
PYTHON := uv run python
SRC_DIR := src
MAIN := $(SRC_DIR)/main.py
TESTS := tests
DOCS_DIR := docs

# Run the main script
run:
	@$(PYTHON) $(MAIN)

# # Install dependencies
# install:
# 	@uv install
#
# # Run tests
# test:
# 	@uv run pytest $(TESTS)
#
# # Clean up cache and build files
# clean:
# 	@find . -type d -name "__pycache__" -exec rm -r {} +
# 	@find . -type f -name "*.pyc" -delete
# 	@rm -rf .pytest_cache $(DOCS_DIR)/build
#
# # Generate Sphinx documentation
# docs:
# 	@make -C $(DOCS_DIR) html
#
# # Check for style issues with black and flake8
# lint:
# 	@uv run black $(SRC_DIR)
# 	@uv run flake8 $(SRC_DIR)

# Display help
help:
	@echo "make 					- Basic build, run"
	@echo "make run       - Run the main Python script"
	# @echo "make install   - Install dependencies using uv"
	# @echo "make test      - Run all tests"
	# @echo "make clean     - Remove cache and temporary files"
	# @echo "make docs      - Build Sphinx documentation"
	# @echo "make lint      - Run code style checks with Black and Flake8"
#
#
#
# # Variables
# PYTHON := uv run
# SPHINXBUILD := $(PYTHON) sphinx-build
# SPHINXDIR := docs
# SPHINXOPTS :=
#
# # Phony targets
# .PHONY: install test docs clean
#
# # Install dependencies via uv
# # install:
# # 	uv install --no-root
# build:
# 	uv run python src/main.py
#
# # Run pytest
# test:
# 	$(PYTHON) pytest
#
# # Build Sphinx documentation
# docs:
# 	$(SPHINXBUILD) -b html $(SPHINXDIR)/source $(SPHINXDIR)/build/html
#
# # Clean the Sphinx documentation build files
# clean-docs:
# 	$(SPHINXBUILD) -M clean $(SPHINXDIR)/source $(SPHINXDIR)/build
#
# # Clean Python build artifacts (e.g., pyc files, cache)
# clean-pyc:
# 	find . -name '*.pyc' -exec rm -f {} +
# 	find . -name '__pycache__' -exec rm -rf {} +
#
# # Clean everything (docs, pyc files)
# clean: clean-docs clean-pyc
#
