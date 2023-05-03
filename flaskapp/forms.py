from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class ProductForm(FlaskForm):
    name = StringField('Product Name')
    amount = IntegerField('Amount')
    submit = SubmitField('Submit')

