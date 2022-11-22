# Dynamic allocation using HTML templates

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html') #Purely sharing the template

@app.route("/<name>")
def user(name):
    return render_template('index.html', content = name, variable = 10) #Dynamically allocating values with template


if __name__ == '__main__':
    app.run()