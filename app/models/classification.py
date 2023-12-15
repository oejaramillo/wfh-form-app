from app import db
from datetime import datetime

class Classification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classifier_id = db.Column(db.Integer, db.ForeignKey('classifier.id'), nullable=False)
    ad_id = db.Column(db.Integer, nullable=False)
    classification = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    classifier = db.relationship('Classifier', backref=db.backref('classifications', lazy=True))

    def __repr__(self):
        return f'<Classification {self.id}>'