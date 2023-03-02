from app_package import app, db
from app_package.forms import login, register
from app_package.models import user
from flask import flash, render_template, redirect, request, url_for


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
   """
        This metho is called when the route /register is hit by the client

        @Args:
             name
        @Chks: for whitespace
   """
   form = register()
   if request.method == 'POST':
       pwd = request.form['pwd']

       if pwd != request.form['conf_pwd']:
           flash("password don't match", "warning")

       else:
           new_user = user(username=request.form['username'],
                           name=request.form['name'],
                           email=request.form['email'],
                           phone=request.form['phoneNo'],
                           password=pwd                  
                       )
           with app.app_context():
               db.session.add(new_user)
               db.session.commit()

               flash("Account successfully created", "success")

           return render_template('dashboard.html')

   return render_template('signup.html', form=form)

@app.route('/shop', strict_slashes=False)
def shop():
   return '<h2>This is the shop page</h2>'
