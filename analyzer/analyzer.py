import subprocess
import os

# 언어별 분석기 매핑 설정
ANALYZERS = {
    "python": ["bandit", "pylint", "rats", "devskim", "sonarqube", "joern", "semgrep"],
    "c": ["infer", "ikos", "frama-c", "rats", "devskim", "cppcheck", "sonarqube", "joern", "semgrep"],
    "cpp": ["infer", "ikos", "rats", "devskim", "cppcheck", "sonarqube", "joern", "semgrep"],
    "java": ["infer", "spotbugs", "rats", "devskim", "sonarqube", "joern", "semgrep"]
}

# 파일 확장자를 기반으로 언어를 추정하고 분석기 리스트 반환
def get_language_and_analyzers(filename):
    ext = os.path.splitext(filename)[1].lower()
    if ext == ".py":
        return "python", ANALYZERS["python"]
    elif ext == ".c":
        return "c", ANALYZERS["c"]
    elif ext in [".cpp", ".cc", ".cxx", ".hpp", ".h"]:
        return "cpp", ANALYZERS["cpp"]
    elif ext == ".java":
        return "java", ANALYZERS["java"]
    else:
        return None, []

# 각 분석기를 docker-compose 명령으로 실행하여 결과를 수집
def run_docker_analyzer(analyzer, filename):
    try:
        command = [
            "docker-compose", "run", "--rm", analyzer,
            "bash", "-c", f"{analyzer} /app/{filename}"
        ]
        result = subprocess.check_output(command, text=True)
        return {f"{analyzer}_log": result}
    except subprocess.CalledProcessError as e:
        return {f"{analyzer}_error": str(e)}

# 파일을 분석하고 결과를 종합
def analyze_file(filename):
    language, analyzers = get_language_and_analyzers(filename)
    if not analyzers:
        return {"error": "지원되지 않는 파일 형식이거나 사용 가능한 분석기가 없습니다."}

    print(f"[ 언어 감지됨 ]: {language}")
    results = {}

    for analyzer in analyzers:
        print(f"[ 실행 중: {analyzer} 분석기 ]...")
        results.update(run_docker_analyzer(analyzer, filename))

    return results

if __name__ == "__main__":
    filename = "test.c"  # 분석할 파일명
    analysis_results = analyze_file(filename)
    print("[ 분석 결과 ]: \n", analysis_results)
