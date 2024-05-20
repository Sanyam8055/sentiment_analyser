FROM ubuntu:20.04

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y software-properties-common && \
    apt-get install -y build-essential curl && \
    apt-get install -y python3.9 python3.9-dev python3.9-distutils

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3.9 get-pip.py && \
    pip install --upgrade pip && \
    pip install connexion

WORKDIR /

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY ./ /

