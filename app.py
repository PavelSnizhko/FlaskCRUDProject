from math import fabs, tan

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_injector import FlaskInjector
from injector import inject

from models import service, parser
from config import Config
from models.adapter_parser import AdapterPolygon
from dependencies import configure
from models.service import Meters

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    n = db.Column(db.Integer)
    length = db.Column(db.Integer)
    square = db.Column(db.Integer)

    def __init__(self, name, x, y, number_side, length, square=0):
        self.name = name
        self.x = x
        self.y = y
        self.n = number_side
        self.length = length
        self.square = square


@app.route('/')
def index():
    all_data = Data.query.all()

    return render_template("index.html", polygons=all_data)


# this route is for inserting data to mysql database via html forms
@inject
@app.route('/insert', methods=['POST'])
def insert(parser: parser.Parser):
    if request.method == 'POST':
        if request.args.get('str_param') != 1:
            name = request.form['name']
            length = int(request.form['length'])
            x = int(request.form['x'])
            y = int(request.form['y'])
            n = int(request.form['number_side'])
            square = n * length ** 2 / 4.0 * fabs(tan(180 / float(n)))

            my_data = Data(name=name,number_side=n, length=length, x=x, y=y, square=square)
        else:
            args_string = request.form['str_param']
            calculator = service.CalculateService()
            adapter = AdapterPolygon(parser)
            adapter.add_observer(calculator)
            model = adapter.get_polygon(args_string)
            square = Meters(calculator).calculate()
            my_data = Data(name=model.get_type(), y=model.get_y(), x=model.get_x(), number_side=model.get_n, length=model.get_side,
                           square=square)

        db.session.add(my_data)
        db.session.commit()

        flash("Polygon Inserted Successfully")

        return redirect(url_for('index'))


# this is our update route where we are going to update our employee
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.length = int(request.form['length'])
        my_data.x = int(request.form['x'])
        my_data.y = int(request.form['y'])
        my_data.n = int(request.form['number_side'])
        my_data.square = my_data.n * my_data.length ** 2 / 4.0 * fabs(tan(180 / float(my_data.n)))

        db.session.commit()
        flash("Employee Updated Successfully")

        return redirect(url_for('index'))


# This route is for deleting our employee
@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Polygon Deleted Successfully")

    return redirect(url_for('index'))


FlaskInjector(app=app, modules=[configure])
if __name__ == "__main__":
    app.run(debug=True)
