import unittest
from app import app, db
from app.models.classifier import Classifier
from app.models.classification import Classification
from app.config import TestConfig  # Corrected import

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.config.from_object(TestConfig)  # Use TestConfig directly
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_demo_form_submission(self):
        # Example test for demo form submission
        response = self.app.post('/submit_classifier', data={
            'age': 30,
            'gender': 'Male',
            'location': 'New York'
        })
        self.assertEqual(response.status_code, 302)  # Assuming redirection after submission

        with app.app_context():
            classifier = Classifier.query.first()
            self.assertIsNotNone(classifier)
            self.assertEqual(classifier.age, 30)
            self.assertEqual(classifier.gender, 'Male')
            self.assertEqual(classifier.location, 'New York')

    # Add more tests for other routes

if __name__ == '__main__':
    unittest.main()
