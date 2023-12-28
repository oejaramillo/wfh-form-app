from flask import render_template, request, redirect, url_for, session, jsonify
from app import app, db
from app.models import Classifier
from app.models import Classification
from datetime import datetime

## Template renders ______
@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/datos_demo')
def datos_demo():
    return render_template('datos_demo.html')

@app.route('/wfh_classification')
def wfh_classification():
    return render_template('wfh_classification.html')

## Routes for buttons _______________
@app.route('/submit', methods=['POST'])
def submit():
    age = request.form.get('age')
    gender = request.form.get('gender')
    location = request.form.get('location')

    new_classifier = Classifier(age=int(age), gender=gender, location=location)
    db.session.add(new_classifier)
    db.session.commit()

    session['classifier_id'] = new_classifier.id  # Store the new classifier's ID in the session

    return redirect(url_for('wfh_classification'))


@app.route('/submit_classification', methods=['POST'])
def submit_classification():
    data = request.json

    classifier_id = session.get('classifier_id')  # Retrieve classifier_id from the session
    if not classifier_id:
        return jsonify({'status': 'error', 'message': 'Classifier ID not found'}), 400

    new_classification = Classification(
        classifier_id=classifier_id,
        ad_id=data['ad_id'],
        classification=data['classification'],
        timestamp=datetime.utcnow()
    )

    db.session.add(new_classification)
    db.session.commit()

    return jsonify({'status': 'success', 'message': 'Classification submitted successfully'})
