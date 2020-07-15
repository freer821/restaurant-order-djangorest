# pull official base image
FROM python:3.8.3-alpine

ENV TERM=xterm \
    TZ=Europe/Berlin \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    locales \
	vim-gtk \
	git \
	libmysqlclient-dev \
	build-essential \
	libssl-dev \
	libffi-dev \
	nginx \
	supervisor &&\
#	pip3 install -U pip setuptools && \
   rm -rf /var/lib/apt/lists/*

# install chinese
RUN locale-gen en_US.UTF-8
RUN locale-gen zh_CN.UTF-8

# install uwsgi now because it takes a little while
RUN pip3 install uwsgi

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .