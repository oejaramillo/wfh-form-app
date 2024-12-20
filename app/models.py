from app import db
from datetime import datetime

class Classifier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    institution = db.Column(db.String(150), nullable=False)
    study_field = db.Column(db.String(150), nullable=False)
    adsGroup = db.Column(db.Integer, nullable=False)
    adCount = db.Column(db.Integer, nullable=False, default=0)
    adoptions = db.Column(db.Integer, nullable=False)

class TempClassifier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    location = db.Column(db.String(150))
    institution = db.Column(db.String(150))
    study_field = db.Column(db.String(150))    
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Classification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classifier_id = db.Column(db.Integer, db.ForeignKey('classifier.id'), nullable=False)
    ad_id = db.Column(db.Integer, nullable=False)
    classification = db.Column(db.String(50), nullable=False)
    ease = db.Column(db.String(7), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    classifier = db.relationship('Classifier', backref=db.backref('classifications', lazy=True))

    def __repr__(self):
        return f'<Classification {self.id}>'