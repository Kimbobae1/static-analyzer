FROM debian:bullseye-slim


RUN apt-get update && apt-get install -y python3

# mkdir the man/man1 directory due to Debian bug #863199
RUN apt-get update && \
    mkdir -p /usr/share/man/man1 && \
    apt-get install --yes --no-install-recommends \
      curl \
      libc6-dev \
      openjdk-11-jdk-headless \
      sqlite3 \
      xz-utils \
      zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*
    
# Download the Infer release
RUN INFER_VERSION=v1.1.0; \
    cd /opt && \
    curl -sL \
      https://github.com/facebook/infer/releases/download/${INFER_VERSION}/infer-linux64-${INFER_VERSION}.tar.xz | \
    tar xJ && \
    rm -f /infer && \
    ln -s ${PWD}/infer-linux64-$INFER_VERSION /infer

# Install infer
ENV PATH /infer/bin:${PATH}


# 작업 디렉토리 설정
WORKDIR /

COPY /infer /

