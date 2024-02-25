from flask import render_template, request, redirect, url_for, session, jsonify
from app import app, db
from app.models import Classifier
from app.models import Classification
from datetime import datetime
from flask import flash
import random
import json
   
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

@app.route('/despedida')
def despedida():
    return render_template('despedida.html')

@app.route('/continue_classification', methods=['POST'])
def continue_classification():
    return render_template('continuar.html')

## Routes for buttons ______________________________________________________
@app.route('/submit', methods=['POST'])
def submit():
    age = request.form.get('age')
    gender = request.form.get('gender')
    location = request.form.get('location')
    institution = request.form.get('institution')
    study_field = request.form.get('study_field')
    email = request.form.get('email')

    existing_classifier = Classifier.query.filter_by(email=email).first()
    if existing_classifier:
        flash('El correo ya existe, por favor continua desde donde lo dejaste.', 'error')
        return redirect(url_for('continuar'))
    
    # Here we should change the list of the first level keys of the JSON data
    ads_groups = ["0", "1", "2", "3", "4"]  # Assuming these are your group IDs
    assigned_group = random.choice(ads_groups)

    new_classifier = Classifier(
        age=int(age), 
        gender=gender, 
        location=location, 
        institution= institution,
        study_field=study_field,
        email=email, 
        adsGroup=assigned_group, 
        adCount=0 )
    db.session.add(new_classifier)
    db.session.commit()

    session['classifier_id'] = new_classifier.id  # Store the new classifier's ID in the session
    return redirect(url_for('wfh_classification'))

@app.route('/get_ads')
def get_ads():
    classifier_id = session.get('classifier_id')
    if classifier_id:
        classifier = Classifier.query.get(classifier_id)
        ads_group = classifier.adsGroup
        ad_count = classifier.adCount

        with open('jobads2.json', 'r') as archive:
            all_ads = json.load(archive)

        # Create a list of objects with id and aviso
        remaining_ads = [{"id": ad_id, "aviso": ad_text} 
                         for ad_id, ad_text in all_ads[str(ads_group)].items()][ad_count:]

        return jsonify(remaining_ads)

    return jsonify({'error': 'Classifier not found'}), 404


@app.route('/submit_classification', methods=['POST'])
def submit_classification():
    data = request.json

    classifier_id = session.get('classifier_id')
    if not classifier_id:
        return jsonify({'status': 'error', 'message': 'Classifier ID not found'}), 400

    new_classification = Classification(
        classifier_id=classifier_id,
        ad_id=data['ad_id'],
        classification=data['classification'],
        ease=data['ease_of_coding'],
        timestamp=datetime.utcnow()
    )

    db.session.add(new_classification)
    db.session.commit()

    # Update adCount for the classifier
    classifier = Classifier.query.get(classifier_id)
    if classifier:
        classifier.adCount += 1
        db.session.commit()

    return jsonify({'status': 'success', 
                    'message': 'Classification submitted successfully',
                    'redirect_url': url_for('despedida')})

@app.route('/submit_mail', methods=['POST'])
def submit_mail():
    email = request.form.get('email')
    classifier = Classifier.query.filter_by(email=email).first()

    if classifier:
        session['classifier_id'] = classifier.id
        return redirect(url_for('wfh_classification'))
    else:
        flash('Tu correo no esta registrado, por favor ingresa tus datos', 'error')
        return redirect(url_for('datos_demo'))  # Replace 'continue_page' with the correct route name
