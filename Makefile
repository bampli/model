default: test
.PHONY: default

install_prerequisites:
	pip install behave
.PHONY: install_prerequisites

generate_tests:
	hiptest-publisher --config behave.conf --token "$(SECRET_TOKEN)" --without=actionwords
.PHONY: generate_tests

test: install_prerequisites
	behave
.PHONY: test
