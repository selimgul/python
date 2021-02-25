from flask import Flask
from flask_restful import Api

from Api.Index import Index
from Api.Multiply import Multiply

app = Flask(__name__)
api = Api(app)

api.add_resource(Index, "/")
api.add_resource(Multiply, "/api/multi/<int:num1>/<int:num2>")

if (__name__ == '__main__'):
    app.run()
