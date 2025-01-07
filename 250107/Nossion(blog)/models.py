# Model -> Table 생성
# 게시글 - board
# 유저 - user

from db import db

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp()) # timestamp로 만드는법을 모르겠어서 datatime으로 했습니다