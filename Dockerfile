FROM python:3.11-alpine

RUN pip install Flask

WORKDIR /app
COPY . /app

CMD ["python", "index.py"]