FROM python:3.8-alpine

ENV LANG en_US.UTF-8 
ENV TERM=xterm \
    TZ=Europe/Berlin \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get upgrade -y && \ 	
    apt-get install -y \
    locales

# install chinese
RUN locale-gen en_US.UTF-8
RUN locale-gen zh_CN.UTF-8

ENV UWSGI_INI /application/uwsgi.ini

COPY . /application/
WORKDIR /appapplication

RUN pip3 install -r /application/requirements.txt
