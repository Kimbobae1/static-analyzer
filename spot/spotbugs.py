from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/log', methods=['GET'])
def log_result():
    try:
        compile_process = subprocess.run(['javac', 'Test.java'], capture_output=True, text=True)
        if compile_process.returncode == 0:
            print("Java 파일이 성공적으로 컴파일되었습니다.")

            result = subprocess.check_output(['spotbugs', '-textui', 'Test.class']).decode('utf-8')
        
            data = {"log": result}
            return jsonify(data)
        

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)