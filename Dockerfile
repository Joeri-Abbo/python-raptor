FROM python:alpine3.16

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.16/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.16/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

# Some packages
RUN apk add --update --no-cache --virtual .tmp-build-deps

RUN apk add gcc
RUN apk add libc-dev
RUN apk add linux-headers
# RUN apk add postgresql-dev
RUN apk add g++
RUN apk add libffi-dev
RUN apk add chromium
# upgrade pip
RUN pip install --upgrade pip

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python3 -m main