from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec2e5161526a1d4668d7df8ad8af8e38b07c9e5e'


import app_package.views
