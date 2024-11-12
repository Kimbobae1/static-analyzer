# Dockerfile.reader
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사 및 requests 라이브러리 설치
COPY analyzer /app
RUN pip install requests

# Reader 프로그램 실행
CMD ["python", "analyzer.py"]