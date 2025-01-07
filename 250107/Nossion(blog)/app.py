from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from db import db
import yaml

app = Flask(__name__)

# db.yaml 파일 읽기
with open('./db.yaml', 'r') as f:
    config = yaml.safe_load(f)  # YAML 파일 로드
    
# db.yaml에서 데이터베이스 연결 정보 가져오기
database_config = config.get('database', {})
app.config['SQLALCHEMY_DATABASE_URI'] = database_config.get('uri')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = database_config.get('track_modifications', False)
db.init_app(app)

# bluepring 설정 및 등록
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

from routes.post import post_blp

api.register_blueprint(post_blp)

from flask import render_template
@app.route('/manage-posts')
def manage_posts():
    return render_template('posts.html') # HTML 코드는 과제 페이지에서 가져왔습니다

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)