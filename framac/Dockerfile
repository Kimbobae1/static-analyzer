FROM framac/frama-c:dev-stripped

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgio-2.0-dev-bin \
    python3

WORKDIR /
COPY /framac /
