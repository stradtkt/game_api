from flask import Flask
from flask_restful import Api
from game import *
from platform import *
from category import *

app = Flask(__name__)
app.secret_key = "fkdhfkdnckdcndkcndkn"
api = Api(app)


api.add_resource(Game, '/game/<string:name>')
api.add_resource(Game, '/game/<int:id>')
api.add_resource(GameList, '/games')
api.add_resource(Platform, '/platform/<string:name>')
api.add_resource(Platform, '/platform/<int:id>')
api.add_resource(PlatformList, '/platforms')
api.add_resource(Category, '/category/<string:name>')
api.add_resource(CategoryList, '/categories')
api.add_resource(Category, '/category/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)
