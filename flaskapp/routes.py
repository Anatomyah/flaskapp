from flask import render_template, request
from flaskapp.forms import ProductForm
from flaskapp.models import Product
from flaskapp import app, db


@app.route("/", methods=['GET', 'POST'])
@app.route("/home",  methods=['GET', 'POST'])
def home():
    form = ProductForm()

    if form.validate_on_submit():
        product = Product(name=form.name.data, amount=form.amount.data)
        db.session.add(product)
        db.session.commit()

    return render_template('home.html', form=form)


@app.route("/about")
def about():
    return 'About'