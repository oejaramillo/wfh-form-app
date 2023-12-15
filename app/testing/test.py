import unittest
from app import app, db

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True

    def test_index_route(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
