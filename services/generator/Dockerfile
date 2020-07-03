FROM python:buster

WORKDIR /home

COPY requirements.txt .

COPY lib lib

RUN pip3 install -r requirements.txt

RUN apt-get update && \
    apt-get install -y php