#Sessions : Temporary - Stored on the server
#           Helps to access different pages during the particular time and then deletes the information even if the user close the browser
#           It is used for quick access of information and a way to pass stuff around server
#           It stores data in the form of dictionary
from crypt import methods
from flask import Flask, render_template, redirect, session, url_for, request
from datetime import timedelta   # Used to set the time/date for the session to last

app = Flask(__name__)
app.secret_key = 'Ram'    # Secret key to avoid security error
app.permanent_session_lifetime == timedelta(seconds=60) # We can set the time/date limit command - days, hours, minutes, seconds

@app.route('/')
def home():
    return render_template("inherit.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True    # This will only keep the data stored in browser as mentioned in timedelta command,
                                    # If this is set false then it will store as long the browser is closed
        user = request.form['nm']
        session['user'] = user   #This helps in redirecting to the user function
        return redirect(url_for('user'))
    else:
        if 'user' in session:                 # This is used for redriecting the page to user even though we type login
            return redirect(url_for('user'))  # If not used it will be redirected to login when typed /login (Additional details)
        return render_template('login.html')

# This stores the previous session
@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return f'<h1>{user}</h1>'
    else:
        return redirect(url_for('login'))

# To clear the previous session
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)