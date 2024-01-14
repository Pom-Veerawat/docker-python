FROM python:3.13.0a2-alpine3.19

WORKDIR /app

COPY . /app

CMD [ "python", "rng.py" ]