FROM python:3.9-alpine

WORKDIR /app
RUN apk add gcc musl-dev libffi-dev postgresql-libs postgresql-dev g++
RUN pip install poetry && poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock /app/
RUN poetry install

EXPOSE 8000
CMD uvicorn --factory bookclub.main:create_app --host 0.0.0.0 --reload
