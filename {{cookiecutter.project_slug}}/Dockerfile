FROM python:3.8

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install -r /requirements.txt

RUN mkdir /app
COPY . /app
WORKDIR /app