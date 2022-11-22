# Writing pytho codes in html template

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('loops.html', contents = [1, 2, 3, 4, 5, 6])

if (__name__) == '__main__':
    app.run()