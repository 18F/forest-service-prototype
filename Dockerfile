FROM python:3.5

RUN mkdir /app
WORKDIR /app

ADD ./requirements.txt /app
RUN pip install -r requirements.txt

WORKDIR /app/forestserviceprototype
