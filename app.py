from flask import Flask
from flask_restful import Api
from game import *
from platform import *
import db

app = Flask(__name__)
app.secret_key = "fkdhfkdnckdcndkcndkn"
api = Api(app)


api.add_resource(Game, '/game/<string:name>')
api.add_resource(GameList, '/games')
api.add_resource(Platform, '/platform/<string:name>')
api.add_resource(PlatformList, '/platforms')

if __name__ == '__main__':
    app.run(debug=True)
