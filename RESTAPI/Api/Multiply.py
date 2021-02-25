from flask_restful import Resource

class Multiply(Resource):        
    def get(self, num1, num2):
          return {"result" : num1 * num2}