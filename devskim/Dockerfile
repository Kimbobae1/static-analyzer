FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build-env

RUN dotnet tool install --global Microsoft.CST.DevSkim.CLI
RUN apt-get update && apt-get install -y python3

ENV PATH="$PATH:/root/.dotnet/tools"

WORKDIR /

COPY /devskim /
