FROM python:3.10-alpine

RUN mkdir /envoy
WORKDIR /envoy

COPY . .
COPY ./requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

RUN adduser -D user
USER user