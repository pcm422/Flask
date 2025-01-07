from flask import Flask
from flask_restful import Api
from resources.item import Item

app = Flask(__name__)
api = Api(app)
    
api.add_resource(Item, '/item/<string:name>')  # <string:name> : URL에 들어갈 변수명

if __name__ == '__main__':
    app.run(debug=True)