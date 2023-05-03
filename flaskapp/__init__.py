from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '123asdf445gasd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskapp.db'
db = SQLAlchemy(app)

from flaskapp import routes


with app.app_context():
    db.create_all()


