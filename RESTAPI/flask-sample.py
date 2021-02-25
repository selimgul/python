from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if (request.method == "POST"):
        req = request.get_json()
        return jsonify({"you sent" :req})
    else:
        return jsonify({"about":"Hello World!"})

@app.route("/multi/<int:num1>/<int:num2>")
def multiplty(num1, num2):
    return jsonify({"result" : num1 * num2})

if (__name__ == '__main__'):
    app.run() 