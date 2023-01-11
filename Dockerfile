FROM python:3.10-alpine

ENV PYTHONBUFFERED 1

RUN apk update
RUN apk add musl-dev mariadb-dev gcc

RUN mkdir /envoy
WORKDIR /envoy

COPY . .
COPY ./requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

RUN adduser -D dev
USER dev