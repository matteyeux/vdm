FROM python:3.7-stretch

WORKDIR /home

COPY . .

RUN pip3 install poetry && \
    poetry install && \
    pip3 install virtualenv && \
    python3 -m venv env && \
    . env/bin/activate
    
RUN apt-get update && \
    apt-get install -y nginx

    # virtualenv -p python3 env && 