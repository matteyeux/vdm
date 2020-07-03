FROM python:buster

WORKDIR /home

COPY . .

RUN pip3 install poetry && \
    pip3 install virtualenv && \
    virtualenv -p python3 env && \
    poetry install && \
    pwd && ls
