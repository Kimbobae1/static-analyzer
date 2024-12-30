from flask import Flask, request, render_template, redirect, url_for
import subprocess, os

app = Flask(__name__)

# 처음 시작하면 로딩 페이지 보여주기
# loading.html에서 init api를 불러옴.
@app.route('/')
def loading_init():
    return render_template('loading_init.html')

# 초기 컨테이너 생성(실행은 x), 완료되면 메인페이지(index.html) 보여주기 
@app.route('/initialize', methods=['GET'])
def initialize():
    subprocess.run(["docker-compose", "create"])
    return redirect(url_for('index'))

# 메인페이지 보여주는 api
@app.route('/index')
def index():
    return render_template('index.html')

# 분석 로딩 화면을 보여주는 api
@app.route('/loading_analyze')
def loading_analyze():
    return render_template('loading_analyze.html')

# 파일 분석을 진행하는 api
@app.route('/analyze', methods=['POST'])
def analyze_file():

    # 파일 업로드, 반환값이 None이라면 '파일없음' 표출
    filename = upload_files()
    if filename is None:
        return render_template('index.html', content="파일 없음")
    
    # # 파일 작성언어 저장, 반환값이 None이라면 분석가능 언어가 아님을 표출
    # file_language = detect_language(filename)
    # if file_language is None:
    #     return render_template('index.html', content="Java, Python, C, C++ 언어만 분석 가능합니다.")
    

    # # 사용할 분석기 리스트 생성, 빈 리스트면 아직 분석가능한 정적분석기가 없는 것.(이거는 필요 없을 것 같긴 함)
    # static_analyzers = determine_static_analyzers(file_language)
    # if not static_analyzers:
    #     return render_template('index.html', content="해당 파일에 대해 실행 가능한 정적분석기가 없습니다.")


    static_analyzers = ['infer', 'ikos', 'bandit', 'cppcheck', 'semgrep', 'spotbugs', 'devskim', 'framac', 'rats', 'pylint']
    analysis = {static_analyzer:run_analyzer_container(static_analyzer) for static_analyzer in static_analyzers}


    # 분석 후 파일 삭제
    delete_file()

    # 분석한 내용 반환
    return render_template('result.html', content=analysis)



# /input 경로 내의 파일 저장(업로드) 함수
def upload_files():
    # 허용할 파일 확장자
    allowed_extensions = {'.java', '.py', '.c', '.cpp'}

    # 'file' 키에 해당하는 파일 리스트 가져오기
    uploaded_files = request.files.getlist('file')
    if not uploaded_files:
        return None

    # 파일 저장 (허용된 확장자만 저장)
    saved_files = []
    for file in uploaded_files:
        extension = os.path.splitext(file.filename)[1].lower()  # 확장자를 소문자로 비교
        if extension in allowed_extensions and file.filename:
            # 디렉토리 경로 제거
            filename = os.path.basename(file.filename)
            save_path = os.path.join('./input', filename)
            file.save(save_path)
            saved_files.append(filename)

    return saved_files



# # 파일 언어 파악 함수
# def detect_language(filename):
#     # (이름, 확장자 분리한 후) 파일의 확장자 가져오기.
#     extension = os.path.splitext(filename)[1]

#     if extension == '.java':
#         return 'java'
#     elif extension == '.py':
#         return 'python'
#     elif extension == '.c':
#         return 'c'
#     elif extension == '.cpp':
#         return 'cpp'
#     else:
#         return None

# # 언어에 맞는 정적분석기 필터링 함수
# def determine_static_analyzers(language):
#     static_analyzer = {
#         'infer' : ['java', 'c', 'cpp'],
#         'ikos' : ['c', 'cpp'],
#         'bandit' : ['python'],
#         'cppcheck' : ['c', 'cpp'],
#         'semgrep' : ['java', 'python', 'c', 'cpp'],
#         'spotbugs' : ['java'],
#         'devskim' : ['java', 'python', 'c', 'cpp'],
#         'framac' : ['c'],
#         'rats' : ['python', 'c', 'cpp'],
#         'pylint' : ['python'],
#         'sonarqube' : ['java', 'python', 'c', 'cpp'],
#     }
#     static_analyzers = [key for key, value in static_analyzer.items() if language in value]
#     return static_analyzers

# 각 정적분석기 컨테이너 실행 함수
def run_analyzer_container(static_anayzer):

    # 컨테이너 실행 (docker-compose 파일의 각 서비스에 정의된 command 실행)
    process = subprocess.Popen(
        ["docker-compose", "up", static_anayzer],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # 지금은 error 안 난다고 가정하고 stdout(표준출력)만 쓰지만 나중에 stderr도 쓸 것 같음.
    stdout, stderr = process.communicate()

    return stdout
    

# /input 경로 내의 파일 삭제 함수
def delete_file() :
    for filename in os.listdir('./input'):
        file_path = os.path.join('./input', filename)
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"{file_path} 삭제 실패: {e}")


if __name__ == '__main__':
    app.run(debug=True)