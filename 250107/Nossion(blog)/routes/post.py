from flask import jsonify, request
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import Post

post_blp = Blueprint("Posts", "posts", description="Operations on posts", url_prefix="/posts")

# API LIST
# 전체 게시글 불러오기 GET
# 게시글을 작성 POST
@post_blp.route("/")
class PostList(MethodView):
    def get(self):
        posts = Post.query.all()
            
        return jsonify([{"id": post.id, 
                         "title": post.title, 
                         "content": post.content,
                         "created_at": post.created_at}
                        for post in posts])
        
    def post(self):
        data = request.json
        new_post = Post(title=data["title"], content=data["content"])
        print(new_post)
        
        db.session.add(new_post)
        db.session.commit()
        
        return jsonify({"msg": "Post created successfully"}), 201

# 하나의 게시글 불러오기 GET
# 특정 게시글 수정하기 PUT
# 특정 게시글 삭제하기 DELETE
@post_blp.route("/<int:post_id>")
class PostResource(MethodView):
    def get(self, post_id):
        post = Post.query.get_or_404(post_id)
        
        return jsonify({"id": post.id, 
                        "title": post.title, 
                        "content": post.content, 
                        "created_at": post.created_at})
        
    def put(self, post_id):
        data = request.json
        post = Post.query.get_or_404(post_id)
        post.title = data["title"]
        post.content = data["content"]
        db.session.commit()
        
        return jsonify({"msg": "Post updated successfully"}), 201
    
    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        
        return jsonify({"msg": "Post deleted successfully"}), 204