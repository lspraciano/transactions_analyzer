export FLASK_ENV = development
#export FLASK_ENV = test
#export FLASK_ENV = production


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



