import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, Docker Flask!", response.data)

    def test_add(self):
        response = self.app.get('/add/2/3')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'"result": 5', response.data)

if __name__ == '__main__':
    unittest.main()
