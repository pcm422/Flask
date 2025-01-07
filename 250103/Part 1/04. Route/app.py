from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, This is Main Page!'

# Alit + Shift + 화살표 위/아래 : 코드 복사
@app.route('/about')
def about():
    return 'This is About Page!'

@app.route('/company')
def about():
    return 'This is Company Page!'

# 동적으로 URL 파라미터 값을 받아서 처리
# http://localhost:5000/user/Cheolmin
@app.route('/user/<username>')
def user_profile(username):
    return f'User Name : {username}'

@app.route('/number/<int:number>')
def number(number):
    return f'Number : {number}'

# post 요청 날리는 법
# (1) postman
# (2) request
import requests
@app.route('/test')
def test():
    url = "http://localhost:5000/submit" # http:// 를 안붙히면 에러가 남
    data = 'test data'
    response = requests.post(url=url, data=data)

    return response.text # 리턴값은 response 객체이므로 text로 변환해야 함

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)

    if request.method == 'GET':
        print('GET method')
    elif request.method == 'POST':
        print('***POST method***', request.data)

    return Response("Successfully submitted!", status=200)

if __name__ == '__main__':
    app.run()