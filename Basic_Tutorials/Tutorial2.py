# Use of HTML templates

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home_page():
    return "Hello! this is my flask tutorial <h1>HELLO<h1>  <h2>FLASK<h2>  <h5>Tutorial<h5>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"   # This returns webpage with error, we have to add any name at the end of the url with /

@app.route('/admin')
def admin():
    return redirect(url_for('home_page')) #or instead of '/' we can specify the name of the function 'home_page'

#@app.route('/admin')
#def admin():
#    return redirect(url_for('user', name='Admin page redirected to user page!')) #for redirecting to user page as name parameter is passed


if __name__ == '__main__':
    app.run(debug = True)