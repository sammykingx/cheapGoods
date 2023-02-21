from app_package import app
from app_package.forms import login, register
from flask import render_template


@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def index():
    return render_template('base.html')

@app.route('/login', strict_slashes=False)
def signin():
    lg_form = login()
    return render_template('login.html')

@app.route('/register', strict_slashes=False)
def signup():
    reg_form = register()
    return '<h1>Resister Page</h1>'
