from flask import Flask, request, render_template, redirect, session, flash
from datetime import timedelta

app = Flask(__name__)

app.secret_key = 'flask_secret_key' # 
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7) # 7일로 설정

# admin user
users = {
    'john': 'pw123',
    'leo': 'pw123'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
        session['username'] = username
        session.permanent = True # 세션을 영구적으로 유지하기 위해 설정
        return redirect('/secret')
    else:
        flash('Invalid username or password.')
        return redirect('/')
    
@app.route('/secret')
def secret():
    if 'username' in session:
        return render_template('secret.html')
    else:
        return redirect('/')
    
# 로그아웃
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)