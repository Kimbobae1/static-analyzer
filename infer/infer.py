
import os
import subprocess

# /input 디렉토리에서 파일 찾기
file = next((f for f in os.listdir('/input') if os.path.isfile(os.path.join('/input/', f))), None)

if not file:
    print("파일 없음")
else:
    # 파일 확장자에 맞는 분석 명령어 결정
    file_path = os.path.join('/input/', file)
    file_extension = os.path.splitext(file)[1]
    print(file_extension)

    if file_extension == '.java':
        # Java 파일 분석
        run_result = subprocess.run(['infer', 'run', '--', 'javac', file_path], capture_output=True, text=True)
    elif file_extension in ['.c', '.cpp']:
        # C 또는 C++ 파일 분석
        run_result = subprocess.run(['infer', 'run', '--', 'clang', '-c', file_path], capture_output=True, text=True)
    else:
        print("지원하지 않는 파일 확장자입니다.")
        exit(1)

    # 결과 출력
    if run_result.returncode == 0:
        print(f"{file} 분석 결과:\n{run_result.stdout}")
    else:
        print(f"{file} 분석 실패: {run_result.stderr}")
