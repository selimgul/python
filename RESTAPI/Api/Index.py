from flask import request
from flask_restful import Resource

class Index(Resource):
    def get(self):
        return {"about":"Hello World!"}

    def post(self):
        req = request.get_json()
        return {"you sent" :req}