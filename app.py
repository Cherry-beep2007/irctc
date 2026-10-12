# import modules
from flask import Flask, render_template

# app creation
app = Flask(__name__)

# routes
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/profile')
def myprofile():
    return render_template('profile.html')


@app.route('/booking')
def book():
    return render_template('base.html')

# debug
if __name__ == '__main__':
    app.run(debug=True)