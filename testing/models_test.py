import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from app import app, db
from app.models.classifier import Classifier
from app.models.classification import Classification
from datetime import datetime

class ModelsTestCase(unittest.TestCase):

    def setUp(self):
        app.config.from_object('config.TestConfig')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_classifier_creation(self):
        classifier = Classifier(age=30, gender='Male', location='New York')
        db.session.add(classifier)
        db.session.commit()

        self.assertIsNotNone(classifier.id)
        self.assertEqual(classifier.age, 30)
        self.assertEqual(classifier.gender, 'Male')
        self.assertEqual(classifier.location, 'New York')

    def test_classification_creation(self):
        classifier = Classifier(age=30, gender='Male', location='New York')
        db.session.add(classifier)
        db.session.commit()

        classification = Classification(classifier_id=classifier.id, ad_id=123, classification='Work From Home', timestamp=datetime.utcnow())
        db.session.add(classification)
        db.session.commit()

        self.assertIsNotNone(classification.id)
        self.assertEqual(classification.classifier_id, classifier.id)
        self.assertEqual(classification.ad_id, 123)
        self.assertEqual(classification.classification, 'Work From Home')

if __name__ == '__main__':
    unittest.main()
