from app_package import app, db


class user(db.Model):
    userId = db.Column(db.Integer,
                       nullable=False,
                       primary_key=True)

    username = db.Column(db.String(15),
                         unique=True,
                         primary_key=True,
                         nullable=True)

    email = db.Column(db.String(30), nullable=False, unique=True)
    pwd = db.Column(db.String(30), nullable=False, unique=True)
    phoneNo = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()
