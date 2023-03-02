from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec2e5161526a1d4668d7df8ad8af8e38b07c9e5e'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cheapGoods.db" 

db = SQLAlchemy(app)

import app_package.views
import app_package.models
