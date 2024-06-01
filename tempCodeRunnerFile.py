from flask import Flask

# Flask 애플리케이션을 생성합니다.
app = Flask(__name__)

# 루트 URL에 대한 라우팅 및 처리기 함수를 정의합니다.
@app.route('/')
def hello_world():
    return 'Hello, World!'

# '/about' URL에 대한 라우팅 및 처리기 함수를 정의합니다.
@app.route('/about')
def about():
    return 'About page'

# 웹 서버를 실행합니다.
if __name__ == '__main__':
    app.run(debug=True)
