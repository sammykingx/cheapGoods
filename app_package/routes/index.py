from app_package import app


@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def index():
    return "<h1>Hello Sammy</h1>"
