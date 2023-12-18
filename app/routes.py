from app import app, db
from app.models.classifier import Classifier
from app.models.classification import Classification
from flask import render_template, request, redirect, url_for
from datetime import datetime

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route('/submit_classifier', methods=['POST'])
def submit_classifier():
    age = request.form.get('age')
    gender = request.form.get('gender')
    location = request.form.get('location')

    new_classifier = Classifier(age=int(age), gender=gender, location=location)
    db.session.add(new_classifier)
    db.session.commit()

    return redirect(url_for('classify'))

@app.route('/classify')
def classify():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_classification():
    # Handle the classification submission
    if request.method == 'POST':
        classifier_id = request.form['classifier_id']
        ad_id = request.form['ad_id']
        classification = request.form['classification']

        # Create a new Classification record
        new_classification = Classification(
            classifier_id=classifier_id,
            ad_id=ad_id,
            classification=classification,
            timestamp=datetime.utcnow()
        )

        # Add to the database and commit
        db.session.add(new_classification)
        db.session.commit()

        return redirect(url_for('last'))
    
    @app.route('/last')
    def last():
        return render_template('last.html')


    return 'Error in submission', 400