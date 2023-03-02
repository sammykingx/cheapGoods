from app_package import app, db


class user(db.Model):
   """ Creating a user table in our database"""

   username = db.Column(db.String(15), primary_key=True, unique=True,
                       nullable=False)

   name = db.Column(db.String(30), nullable=False)
   email = db.Column(db.String(30), nullable=False)
   phone = db.Column(db.String(15), nullable=False)
   password = db.Column(db.String(30), nullable=False)
   location = db.Column(db.String(50), db.ForeignKey('location.street'))


class location(db.Model):
   """ Creating the location table """

   userID = db.Column(db.Integer, primary_key=True, nullable=False)

   street = db.Column(db.String(40), nullable=False)

   user = db.relationship('user', backref='address')

   city = db.Column(db.String(20), nullable=False)
   landmark = db.Column(db.String(30), nullable=False)
   country = db.Column(db.String(15), nullable=False)


class products(db.Model):
   """ Creates products table """

   productId = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(30), nullable=False)
#   image = db.Column(db.Blob, nullable=False)
   description = db.Column(db.Text, nullable=False)
   qty = db.Column(db.Integer, nullable=False)
   condition = db.Column(db.String(15), nullable=False)
   cost = db.Column(db.Integer, nullable=False)
   seller = db.Column(db.String(30), nullable=False)
   seller_phone = db.Column(db.Integer, nullable=False)


class order(db.Model):
   """ creates the order table """

   orderID = db.Column(db.Integer, nullable=False, primary_key=True)
   name = db.Column(db.String(30), nullable=False)
   buyerName = db.Column(db.String(30), nullable=False)
   buyerNo = db.Column(db.Integer, nullable=False)
   location = db.Column(db.String(50), nullable=False)
   qty = db.Column(db.Integer, nullable=False)
   cost = db.Column(db.Integer, nullable=False)
   seller = db.Column(db.String(30), nullable=False)
   Seller_phone = db.Column(db.Integer, nullable=False)


with app.app_context():
    db.create_all()
