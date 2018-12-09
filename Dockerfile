FROM python:3.7.1-alpine

MAINTAINER Kan Ouivirach

ENV APPLICATION_ROOT /app
RUN mkdir $APPLICATION_ROOT
WORKDIR $APPLICATION_ROOT

RUN pip3 install pipenv

COPY Pipfile* $APPLICATION_ROOT/
RUN pipenv install --dev

EXPOSE 8000
