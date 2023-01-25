FROM python:3.6.12-slim

ENV FLASK_APP="main.py"

WORKDIR /opt/app

ADD requirements.txt .

RUN apt-get update && \
  apt-get install -y curl wget net-tools iputils-* && \
  pip3 install -r requirements.txt && \
  rm -rf /var/lib/apt/lists/*

ADD . .

EXPOSE 5000

ENTRYPOINT [ "python", "main.py" ]