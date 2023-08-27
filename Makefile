setup:
	@poetry install

test:
	@poetry run pytest ./tests

test-matching:
	poetry run pytest -vv -k $(K)

generate-coverage:
	@poetry run pytest $(COVERAGE_OPTS) ${1:-tests-local}

update: poetry.lock
	@poetry update
