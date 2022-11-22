# Basic coomands for creating Flask API

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return "Hello! this is my flask tutorial <h1>HELLO<h1>  <h2>FLASK<h2>  <h5>Tutorial<h5>"

#@app.route("/<name>")
#def user(name):
#    return f"Hello {name}!"


if __name__ == '__main__':
    app.run()