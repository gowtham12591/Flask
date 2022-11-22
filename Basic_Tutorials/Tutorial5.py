## Inheritencec and Bootstrapping
# https://getbootstrap.com/docs/4.0/components/navbar/

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/test')
def test():
    return render_template('inherit.html')

if (__name__) == '__main__':
    app.run(debug=True) #debug=True helps to change whatever we make changes in the webpage.