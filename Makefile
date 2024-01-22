setup:
	@poetry install

test:
	@poetry run pytest ./tests

test-matching:
	poetry run pytest -vv -k $(K)

coverage:
	@poetry run pytest --cov=src --cov-report=term-missing --cov-report=xml ./tests/

update: poetry.lock
	@poetry update

run:
	@poetry run python run.py
