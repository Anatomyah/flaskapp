from flaskapp import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
