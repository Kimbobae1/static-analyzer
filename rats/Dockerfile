# 사용자 이미지임. 공식 X
FROM ociotec/rats:latest

# apt-get을 지원하는 Debian 계열의 이미지가 아니어서 다르게.
RUN apk update && apk add --no-cache python3

WORKDIR /

COPY /rats /
