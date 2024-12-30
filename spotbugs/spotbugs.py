import os
import subprocess

# 현재 디렉토리에서 유일한 .java 파일 찾기
java_file = next((f for f in os.listdir('/input') if f.endswith('.java')), None)

if not java_file:
    print("현재 디렉토리에 Java 파일이 없습니다.")
else:
    # Java 파일 컴파일
    compile_result = subprocess.run(['javac', '/input/'+java_file], capture_output=True, text=True)
    if compile_result.returncode != 0:
        print(f"{java_file}컴파일 실패: {compile_result.stderr}")
        exit(1)

    # 클래스 이름 추출 (파일 이름에서 .java 확장자 제거)
    main_class = os.path.splitext(java_file)[0]

    # 특정 명령어 실행 (예: 메인 클래스 실행)
    run_result = subprocess.run(['spotbugs', '-textui', '/input/'+main_class+'.class'], capture_output=True, text=True)

    # .class 파일 삭제
    class_file_path = os.path.join('/input/', main_class + '.class')
    if os.path.exists(class_file_path):
        os.remove(class_file_path)

    print(f"{main_class} 분석 결과:\n{run_result.stdout}\n{run_result.stderr}")