from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Classifier

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/datos_demo')
def datos_demo():
    return render_template('datos_demo.html')

@app.route('/submit', methods=['POST'])
def submit():
    age = request.form.get('age')
    gender = request.form.get('gender')
    location = request.form.get('location')

    new_entry = Classifier(age=age, gender=gender, location=location)
    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('inicio'))
