from flask import request, jsonify
from flask_smorest import Blueprint, abort

def create_posts_blueprint(mysql):
    posts_blp = Blueprint('posts', __name__, description='posts api', url_prefix='/posts')
    
    @posts_blp.route('/', methods=['GET', 'POST'])
    def posts():
        cursor = mysql.connection.cursor()
        # 게시글 조회
        if request.method == "GET":
            sql = "SELECT * FROM posts"
            cursor.execute(sql)

            posts = cursor.fetchall()
            cursor.close()

            post_list = []

            for post in posts:
                post_list.append(
                    {
                        "id": post[0],
                        "title": post[1],
                        "content": post[2],
                    }
                )
            return jsonify(post_list)

        # 게시글 생성
        elif request.method == 'POST':
            title = request.json.get('title')
            content = request.json.get('content')
            if not title or not content:
                abort(400, message="Title and content cannot be empty.")            
                        
            sql = "INSERT INTO posts (title, content) VALUES (%s, %s)"
            cursor.execute(sql, (title, content))
            mysql.connection.commit()
            cursor.close()
            return jsonify({'message': 'Post created successfully.'}), 201
        
    # 특정 게시글 조회
    # 게시글 수정 및 삭제    
    @posts_blp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def post(id):
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM posts WHERE id = %s"
        cursor.execute(sql, (id,))
        post = cursor.fetchone() 
            
        if request.method == 'GET':
            if not post:
                abort(404, message="Post not found.")
            return ({"id": post[0], 
                     "title": post[1], 
                     "content": post[2]})
                
        elif request.method == 'PUT':
            title = request.json.get('title')
            content = request.json.get('content')
            
            if not post:
                abort(404, message="Post not found.")
                
            if not title or not content:
                abort(400, message="Title and content cannot be empty.")
        
            sql = "UPDATE posts SET title = %s, content = %s WHERE id = %s"
            cursor.execute(sql, (title, content, id))
            mysql.connection.commit()
            cursor.close()
            return jsonify({'message': 'Post updated successfully.'}), 200
        
        elif request.method == 'DELETE':
            if not post:
                abort(404, message="Post not found.")
                
            sql = "DELETE FROM posts WHERE id = %s"
            cursor.execute(sql, (id,))
            mysql.connection.commit()
            cursor.close()
            return jsonify({'message': 'Post deleted successfully.'}), 200

    return posts_blp