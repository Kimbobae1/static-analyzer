import os
import subprocess

# /input 디렉토리에서 파일 목록 가져오기
input_dir = '/input'
files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

if not files:
    print("분석할 파일이 없습니다.")
else:
    for file in files:
        file_path = os.path.join(input_dir, file)
        print(f"분석 중: {file}")

        # DevSkim으로 파일 분석
        run_result = subprocess.run(["devskim", "analyze", "--source-code", file_path, "-f", "text"], capture_output=True, text=True)


        print(f"{file} 분석 결과:\n{run_result.stdout}\n{run_result.stderr}")
