FROM debian:latest

RUN apt-get update && apt-get install -y cppcheck
RUN apt-get update && apt-get install -y python3

WORKDIR /

COPY /cppcheck /

