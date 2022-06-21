# pull official base image
FROM python:3.9.10

# set work directory
WORKDIR /var/www/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# copy needed files
COPY ../poetry.lock /var/www/app
COPY ../pyproject.toml /var/www/app
COPY ../transaction_analyzer /var/www/app/transaction_analyzer
COPY ../run.py /var/www/app
COPY ../.env /var/www/app
COPY ./docker/entrypoint.sh /var/www/app
COPY ../docs/mkdocs.yml /var/www/app/docs/

# path poetry and install
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# entrypoint
ENTRYPOINT ["sh","entrypoint.sh"]