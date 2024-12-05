FROM facthunder/ikos

# 저장소 변경
RUN sed -i 's|http://archive.ubuntu.com/ubuntu|http://archive.ubuntu.com/ubuntu|g' /etc/apt/sources.list && \
    sed -i 's|http://security.ubuntu.com/ubuntu|http://security.ubuntu.com/ubuntu|g' /etc/apt/sources.list && \
    sed -i 's|disco|focal|g' /etc/apt/sources.list

# 패키지 업데이트 및 Python3 설치
RUN apt-get update && apt-get install -y python3

# 작업 디렉토리 설정
WORKDIR /

COPY /ikos / 
