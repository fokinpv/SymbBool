.PHONY: all
all: help

.PHONY: help
help:
	@echo 'Makefile help:                 '
	@echo '                               '
	@echo '  tests:          Run unittests'

.PHONY: tests
tests:
	@python3 -m unittest discover -s tests -v
