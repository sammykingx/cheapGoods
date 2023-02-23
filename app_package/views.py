from app_package import app
from app_package.forms import login, register
from flask import render_template, url_for


@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def index():
    return render_template('index.html')

@app.route('/about', strict_slashes=False)
def about():
    return render_template('about.html')

@app.route('/blog', strict_slashes=False)
def blog():
    return render_template('blog.html')

@app.route('/contact', strict_slashes=False)
def contact():
    return render_template('contact.html')

@app.route('/login', strict_slashes=False)
def signin():
    lg_form = login()
    return render_template('login.html', form=lg_form)

@app.route('/register', strict_slashes=False, methods = ['GET', 'POST'])
def signup():
    reg_form = register()
    return '<h2>Resister Page</h2>'

@app.route('/shop', strict_slashes=False)
def shop():
    return '<h2>This is the shop page</h2>'
