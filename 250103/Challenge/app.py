from flask import Flask, render_template  # Flask 프레임워크와 템플릿 렌더링 함수 임포트

app = Flask(__name__)  # Flask 애플리케이션 객체 생성. __name__은 현재 모듈의 이름

@app.route('/')  # 루트 URL('/')에 접속했을 때 실행될 함수를 지정하는 데코레이터
def view():  # 루트 URL에 접속했을 때 실행될 함수
    users = [  # 유저 정보를 담고 있는 리스트. 각 유저는 딕셔너리 형태로 저장됨
        {"username": "traveler", "name": "Alex"},
        {"username": "photographer", "name": "Sam"},
        {"username": "gourmet", "name": "Chris"}
    ]
    
    # render_template 함수를 사용하여 index.html 템플릿을 렌더링
    # users 리스트를 'users'라는 이름으로 템플릿에 전달
    return render_template('index.html', users=users)

if __name__ == '__main__':  # 현재 스크립트가 직접 실행될 때만 아래 코드를 실행
    app.run(debug=True)  # Flask 개발 서버 실행. debug=True는 디버그 모드를 활성화하여 에러 발생 시 디버깅 정보 출력