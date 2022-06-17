install:
		@poetry install

format:
		@blue .

sec:
		@pip-audit
test:
		@pytest -x
run:
		@python -m run

