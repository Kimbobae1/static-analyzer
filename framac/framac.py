import os
import subprocess

# /input 디렉토리에서 파일 찾기
file = next((f for f in os.listdir('/input') if os.path.isfile(os.path.join('/input/', f))), None)

if not file:
    print("파일 없음")
else:
    file_path = os.path.join('input', file)
    run_result = subprocess.run(["frama-c", "-wp", "-eva", file_path], capture_output=True, text=True)

    # 결과 출력
    if run_result.returncode == 0:
        print(f"{file} 분석 결과:\n{run_result.stdout}\n{run_result.stderr}")
    else:
        print(f"{file} 분석 실패: {run_result.stderr}\n{run_result.stdout}")