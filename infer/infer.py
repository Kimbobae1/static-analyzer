import os
import subprocess

# /input 디렉토리에서 파일 찾기
input_dir = '/input'
files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

if not files:
    print("분석할 파일이 없습니다.")
else:
    for file in files:
        file_path = os.path.join(input_dir, file)
        file_extension = os.path.splitext(file)[1]
        print(f"분석 중: {file} ({file_extension})")

        if file_extension == '.java':
            # Java 파일 분석
            run_result = subprocess.run(['infer', 'run', '--', 'javac', file_path], capture_output=True, text=True)
        elif file_extension in ['.c', '.cpp']:
            # C 또는 C++ 파일 분석
            run_result = subprocess.run(['infer', 'run', '--', 'clang', '-c', file_path], capture_output=True, text=True)
        else:
            print(f"지원하지 않는 파일 형식: {file}")
            continue

        print(f"{file} 분석 결과:\n{run_result.stdout}\n{run_result.stderr}")
