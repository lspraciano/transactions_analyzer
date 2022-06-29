
install:
		@poetry install
		@poetry shell

format:
		@blue .

sec:
		@pip-audit

test:
		@pytest

run:
		@python -m run



