from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Importing models
from models.classifier import Classifier
from models.classification import Classification

@app.route('/')
def index():
    # Display the homepage or job ads
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

        return redirect(url_for('index'))

    return 'Error in submission', 400

if __name__ == '__main__':
    app.run(debug=True)
