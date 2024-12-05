FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y openjdk-17-jdk

# SpotBugs 설치
RUN apt-get update && \
    apt-get install -y wget unzip && \
    wget https://github.com/spotbugs/spotbugs/releases/download/4.8.6/spotbugs-4.8.6.zip && \
    unzip spotbugs-4.8.6.zip && \
    rm spotbugs-4.8.6.zip

# SpotBugs 경로 설정
ENV SPOTBUGS_HOME /spotbugs-4.8.6
ENV PATH $SPOTBUGS_HOME/bin:$PATH

# 작업 디렉토리 설정
WORKDIR /

COPY /spotbugs /