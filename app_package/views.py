from app_package import app
from flask import render_template
import forms


@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def index():
    return render_template('base.html')

@app.route('/login', strict_slashes=False)
def login():
    lg_form = forms.login()
    return render_template('login.html')

@app.route('/register', strict_slashes=False)
def register():
    reg_form = forms.register()
    return'<h1>Resister Page</h1>'
