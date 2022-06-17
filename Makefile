install:
		@poetry install

format:
		@blue .

sec:
		@pip-audit
test:
		@pytest
run:
		@python -m run

