# This is the index route where we are going to
# query on all our employee data
from flask import flash, redirect, url_for, request, render_template

from app import Data, db, app


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
        square = x*y*length

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
