from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# Ensure you have the correct path for your SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Classifier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), unique=False, nullable=False)
    location = db.Column(db.String(150), unique=False, nullable=False)
    # Add other fields as necessary


class Classification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classifier_id = db.Column(db.Integer, db.ForeignKey('classifier.id'), nullable=False)
    ad_id = db.Column(db.Integer, nullable=False)
    classification = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    classifier = db.relationship('Classifier', backref=db.backref('classifications', lazy=True))

def init_db():
    db.create_all()

if __name__ == '__main__':
    init_db()
