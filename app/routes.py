from flask import Flask, render_template, request, redirect, url_for, session, jsonify, current_app, flash
from app import app, db, mail
from app.models import Classifier
from app.models import Classification
from app.models import TempClassifier
from datetime import datetime
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask_mail import Message, Mail
import random
import json

def generate_verification_token(email):
    serializer = Serializer(current_app.config['SECRET_KEY'], salt='email-verify')
    token = serializer.dumps(email, salt='email-verify')
    return token
   
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
    temp_classifier = TempClassifier(
        age = request.form.get('age'),
        gender = request.form.get('gender'),
        location = request.form.get('location'),
        institution = request.form.get('institution'),
        study_field = request.form.get('study_field'),
        email = request.form.get('email')
    )
    
    existing_temp = TempClassifier.query.filter_by(email=temp_classifier.email).first()
    existing_classifier = Classifier.query.filter_by(email=temp_classifier.email).first()

    if existing_temp or existing_classifier:
        flash('El correo ya existe, por favor continua desde donde lo dejaste.', 'error')
        return redirect(url_for('datos_demo'))
    else:
        db.session.add(temp_classifier)
        db.session.commit()

        session['temp_id'] = temp_classifier.id

        # redirect to email verification process
        return redirect(url_for('register', email=temp_classifier.email))

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

        response = jsonify({
            'remaining_ads': remaining_ads,
            'total_ads': len(all_ads[str(ads_group)]),
            'ads_classified': ad_count
            })
        print(response)
        print("total ads ", len(all_ads[str(ads_group)]))
        return response

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

        # Check classifications are finished
        TOTAL_CLASSIFICATIONS = 8       # THIS NUMBER should be updated each time with the amount of ads
        if classifier.adCount >= TOTAL_CLASSIFICATIONS:
            send_email(classifier.email)
    
    return jsonify({'status': 'success', 
                    'message': 'Classification submitted successfully',
                    'redirect_url': url_for('despedida')})

def send_email(email):
    subject = "Gracias por participar"
    sender = app.config['MAIL_DEFAULT_SENDER']
    recipients = [email]
    body = "Gracias por ayudar en el proyecto"

    msg = Message(subject, sender=sender, recipients=recipients, body=body)

    try:
        mail.send(msg)
    except Exception as e:
        app.logger.error(f"Fallo al enviar el corre: {e}")


@app.route('/submit_mail', methods=['POST'])
def submit_mail():
    email = request.form.get('email')
    classifier = Classifier.query.filter_by(email=email).first()

    if classifier:
        session['classifier_id'] = classifier.id
        return redirect(url_for('wfh_classification'))
    else:
        flash('Tu correo no esta registrado, por favor ingresa tus datos', 'error')
        return redirect(url_for('datos_demo'))  
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    temp_id = session.get('temp_id')
    temp_classifier = TempClassifier.query.filter_by(id=temp_id).first()

    if temp_classifier and temp_classifier.email:  # Check if email is not empty
        token = generate_verification_token(temp_classifier.email)

        # Send verification email
        verify_url = url_for('verify_email', token=token, _external=True)
        msg = Message("Por favor verifica tu correo electronico", recipients=[temp_classifier.email])
        msg.body = f'El link de verificacion es: {verify_url}'
        try:
            mail.send(msg)
            print(msg)
        except Exception as e:
            print(f"Fallo al enviar correo: {e}")
    else:
        flash('Por favor ingresa un correo electronico.', 'error')
        return redirect(url_for('register'))

    # For GET requests, or if POST request but email is empty
    # Assuming you have a template named 'register.html' for the registration form
    return render_template('register.html')
    
@app.route('/verify_email/<token>')
def verify_email(token):
    serializer = Serializer(current_app.config['SECRET_KEY'], salt='email-verify')
    try:
        email = serializer.loads(token, salt='email-verify', max_age=3600) # una hora
        temp_classifier = TempClassifier.query.filter_by(email=email).first_or_404()

        # Transfer data from temp classifier to the actual classifier
        ads_groups = ["0", "1", "2", "3", "4"]  # THIS list should also be updated with the actual count of ads displayed
        assigned_group = random.choice(ads_groups)

        new_classifier = Classifier(
            age=int(temp_classifier.age),
            gender=temp_classifier.gender,
            location=temp_classifier.location,
            institution=temp_classifier.institution,
            study_field=temp_classifier.study_field,
            email=temp_classifier.email,
            adsGroup=assigned_group,
            adCount=0 
        )

        db.session.add(new_classifier)
        db.session.delete(temp_classifier)
        db.session.commit()

        session['classifier_id'] = new_classifier.id  # Store the new classifier's ID in the session

        # Podemos redirigir
        return redirect(url_for('wfh_classification'))
    except:
        return redirect(url_for('datos_demo')) 
    

    
   