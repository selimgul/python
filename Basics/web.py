from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World."

@app.route("/register", methods=["GET"])
def register():
    if request.method == "GET":        
        return "register"

if __name__ == "__main__":
    app.run()
