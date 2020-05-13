from flask import Flask, render_template, request, redirect, url_for, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    x = db.Column(db.String(100))
    y = db.Column(db.String(100))
    length = db.Column(db.Integer)
    square = db.Column(db.Integer)

    def __init__(self, name, x, y, length, square=0):
        self.name = name
        self.x = x
        self.y = y
        self.length = length
        self.square = square


@app.route('/')
def index():
    all_data = Data.query.all()

    return render_template("index.html", polygons=all_data)


# this route is for inserting data to mysql database via html forms
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        length = int(request.form['length'])
        x = int(request.form['x'])
        y = int(request.form['y'])
        square = x * y * length

        my_data = Data(name, length, x, y, square)
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
        my_data.square = my_data.x * my_data.y * my_data.length

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


if __name__ == "__main__":
    app.run(debug=True)
